# autoresearch

This is an experiment to have the LLM do its own research.

## Setup

To set up a new experiment, work with the user to:

1. **Agree on a run tag**: propose a tag based on today's date (e.g. `mar5`). The branch `autoresearch/<tag>` must not already exist — this is a fresh run.
2. **Create the branch**: `git checkout -b autoresearch/<tag>` from current master.
3. **Read the in-scope files**: The repo is small. Read these files for full context:
   - `README.md` — repository context.
   - `prepare.py` — fixed constants, data prep, tokenizer, dataloader, evaluation. Do not modify.
   - `train.py` — the file you modify. Model architecture, optimizer, training loop.
4. **Verify data exists**: Check that `~/.cache/autoresearch/` contains data shards and a tokenizer. If not, tell the human to run `uv run prepare.py`.
5. **Initialize results.tsv**: Create `results.tsv` with just the header row. The baseline will be recorded after the first run.
6. **Confirm and go**: Confirm setup looks good.

Once you get confirmation, kick off the experimentation.

## Experimentation

Each experiment runs on a single GPU. The training script runs for a **fixed time budget of 5 minutes** (wall clock training time, excluding startup/compilation). You launch it simply as: `uv run train.py`.

**What you CAN do:**
- Modify `train.py` — this is the only file you edit. Everything is fair game: model architecture, optimizer, hyperparameters, training loop, batch size, model size, etc.

**What you CANNOT do:**
- Modify `prepare.py`. It is read-only. It contains the fixed evaluation, data loading, tokenizer, and training constants (time budget, sequence length, etc).
- Install new packages or add dependencies. You can only use what's already in `pyproject.toml`.
- Modify the evaluation harness. The `evaluate_bpb` function in `prepare.py` is the ground truth metric.

**The goal is simple: get the lowest val_bpb.** Since the time budget is fixed, you don't need to worry about training time — it's always 5 minutes. Everything is fair game: change the architecture, the optimizer, the hyperparameters, the batch size, the model size. The only constraint is that the code runs without crashing and finishes within the time budget.

**VRAM** is a soft constraint. Some increase is acceptable for meaningful val_bpb gains, but it should not blow up dramatically.

**Simplicity criterion**: All else being equal, simpler is better. A small improvement that adds ugly complexity is not worth it. Conversely, removing something and getting equal or better results is a great outcome — that's a simplification win. When evaluating whether to keep a change, weigh the complexity cost against the improvement magnitude. A 0.001 val_bpb improvement that adds 20 lines of hacky code? Probably not worth it. A 0.001 val_bpb improvement from deleting code? Definitely keep. An improvement of ~0 but much simpler code? Keep.

**The first run**: Your very first run should always be to establish the baseline, so you will run the training script as is.

## Output format

Once the script finishes it prints a summary like this:

```
---
val_bpb:          0.997900
training_seconds: 300.1
total_seconds:    325.9
peak_vram_mb:     45060.2
mfu_percent:      39.80
total_tokens_M:   499.6
num_steps:        953
num_params_M:     50.3
depth:            8
```

Note that the script is configured to always stop after 5 minutes, so depending on the computing platform of this computer the numbers might look different. You can extract the key metric from the log file:

```
grep "^val_bpb:" run.log
```

## Logging results

When an experiment is done, log it to `results.tsv` (tab-separated, NOT comma-separated — commas break in descriptions).

The TSV has a header row and 5 columns:

```
commit	val_bpb	memory_gb	status	description
```

1. git commit hash (short, 7 chars)
2. val_bpb achieved (e.g. 1.234567) — use 0.000000 for crashes
3. peak memory in GB, round to .1f (e.g. 12.3 — divide peak_vram_mb by 1024) — use 0.0 for crashes
4. status: `keep`, `discard`, or `crash`
5. short text description of what this experiment tried

Example:

```
commit	val_bpb	memory_gb	status	description
a1b2c3d	0.997900	44.0	keep	baseline
b2c3d4e	0.993200	44.2	keep	increase LR to 0.04
c3d4e5f	1.005000	44.0	discard	switch to GeLU activation
d4e5f6g	0.000000	0.0	crash	double model width (OOM)
```

## The experiment loop

The experiment runs on a dedicated branch (e.g. `autoresearch/mar5` or `autoresearch/mar5-gpu0`).

LOOP FOREVER:

1. Look at the git state: the current branch/commit we're on
2. Tune `train.py` with an experimental idea by directly hacking the code.
3. git commit
4. Run the experiment: `uv run train.py > run.log 2>&1` (redirect everything — do NOT use tee or let output flood your context)
5. Read out the results: `grep "^val_bpb:\|^peak_vram_mb:" run.log`
6. If the grep output is empty, the run crashed. Run `tail -n 50 run.log` to read the Python stack trace and attempt a fix. If you can't get things to work after more than a few attempts, give up.
7. Record the results in the tsv
8. If val_bpb improved (lower), you "advance" the branch, keeping the git commit
9. If val_bpb is equal or worse, you git reset back to where you started

The idea is that you are a completely autonomous researcher trying things out. If they work, keep. If they don't, discard. And you're advancing the branch so that you can iterate. If you feel like you're getting stuck in some way, you can rewind but you should probably do this very very sparingly (if ever).

**Timeout**: Each experiment should take ~5 minutes total (+ a few seconds for startup and eval overhead). If a run exceeds 10 minutes, kill it and treat it as a failure (discard and revert).

**Crashes**: If a run crashes (OOM, or a bug, or etc.), use your judgment: If it's something dumb and easy to fix (e.g. a typo, a missing import), fix it and re-run. If the idea itself is fundamentally broken, just skip it, log "crash" as the status in the tsv, and move on.

**NEVER STOP**: Once the experiment loop has begun (after the initial setup), do NOT pause to ask the human if you should continue. Do NOT ask "should I keep going?" or "is this a good stopping point?". The human might be asleep, or gone from a computer and expects you to continue working *indefinitely* until you are manually stopped. You are autonomous. If you run out of ideas, think harder — read papers referenced in the code, re-read the in-scope files for new angles, try combining previous near-misses, try more radical architectural changes. The loop runs until the human interrupts you, period.

As an example use case, a user might leave you running while they sleep. If each experiment takes you ~5 minutes then you can run approx 12/hour, for a total of about 100 over the duration of the average human sleep. The user then wakes up to experimental results, all completed by you while they slept!


## Research Strategy

### What We're Actually Doing

The training objective — minimizing val_bpb — is equivalent to minimizing *surprise*: how many bits the model needs to encode each byte of held-out text, given everything it has seen before. Lower val_bpb means the model's learned priors better predict the structure of the data.

The model weights ARE the prior. They encode the statistical structure of TinyStories — not specific stories, but the underlying patterns: what kinds of phrases follow what kinds of phrases, what narrative structures recur, how children's story language behaves. Training is the process of updating that prior until surprises (residuals between prediction and reality) are minimized. Once trained, generation works by repeatedly sampling the least-surprising next token — the model projects forward from its learned priors.

This framing — weights as prior, forward pass as inference, loss as surprise — is the Bayesian/free energy view (Friston), and it directly motivates the architectural experiments below.

### Research Direction: Predictive Coding (PC) Architecture

The core hypothesis: **conventional transformers process raw input state; PC-inspired transformers should process prediction error (surprise)**.

In a residual transformer, every layer refines the accumulated representation. There is no separation between "what I already knew" and "what just surprised me." Biological cortex works differently — well-predicted inputs are handled cheaply by trained circuits; only deviations from expectation demand expensive attention-level processing. This is why biological brains are far more energy-efficient: they route capacity proportional to surprise.

**The fundamental inversion:**
- Standard: `x = layer(x)` — refine the state
- PC: `error = x - prior_prediction(x)` → `x = layer(error)` — process the surprise

**Experiments to run, ordered least to most invasive:**

1. **Prior-Subtraction Residual**: The current `x0_lambdas * x0` skip *adds* the initial embedding — it should instead *subtract* it (remove the prior, leave the error). Change: `surprise = x - x0_lambdas[i] * x0`, then feed `surprise` to the block.

2. **Learned Hierarchical Top-Down Priors**: Replace the flat x0 skip with per-layer learned projections `nn.Linear(n_embd, n_embd)(x0)`. Each layer learns which aspect of the initial embedding to "explain away" at its depth. Shallower layers explain surface statistics; deeper layers explain narrative structure.

3. **Error-Unit Architecture (bold)**: Add per-layer self-predictors. Each layer predicts its own input; the block processes the error only. Only unpredicted information propagates. Well-predicted tokens contribute near-zero signal — sparsity emerges naturally.

4. **Surprise-Biased Attention**: Add prediction error magnitude as a learned bias on attention logits. High-error tokens receive more attention — salience-driven routing rather than similarity-driven. Biologically: saccades jump to high-error regions.

5. **Auxiliary PC Loss**: Add a precision-weighted reconstruction loss requiring each layer to be predictable from the layer above. Keeps backprop; adds local PC self-supervision. `L_total = L_ce + λ * Σ (1/σ²_i) * ||h_i - W_pred(h_{i+1})||²`

When evaluating whether a PC change is "worth it" (see simplicity criterion above), weight the val_bpb improvement against how much complexity it adds. A clean inversion that helps a little is better than a messy one that helps a lot.

### MPS Hardware Constraints (M4 Max, 64GB Unified Memory)

Discovered empirically — respect these or throughput collapses:

- **DEVICE_BATCH_SIZE=32**: Do not go below. MPS falls below efficient GPU utilization at 16 (191 steps vs 272).
- **TOTAL_BATCH_SIZE=2^16**: Sweet spot. Smaller hurts (fewer steps, noisier), larger unclear.
- **HEAD_DIM=128**: Do not reduce. Smaller matrix dims (64) reduce MPS throughput.
- **WINDOW_PATTERN="L"**: Do not use sliding window (SSSL etc). Masked SDPA is *slower* on MPS than full causal — no FlashAttention 3 on MPS.
- **No bfloat16 autocast**: MPS doesn't support it well. Already handled in code.
- **No torch.compile**: Disabled for MPS in train.py. Do not re-enable.
- **Thermal throttling**: Consecutive runs may produce 15-20% step count variance. Don't over-interpret small differences.

Best known hyperparameters (as of mar10-m4max, val_bpb=0.594614):
- MATRIX_LR=0.09, WARMDOWN_RATIO=0.35, FINAL_LR_FRAC=0.0
- DEPTH=4, ASPECT_RATIO=64 (model_dim=256, n_head=2), HEAD_DIM=128