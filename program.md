# autoresearch

This is an experiment to have the LLM do its own research — specifically on **MuJoCo RL** using a flyer model (e.g. `Ant-v4`, `HalfCheetah-v4`, or a custom flying task). The success metric is **cumulative reward / mean episode return** (higher is better).

## Setup

To set up a new experiment, work with the user to:

1. **Agree on a run tag**: propose a tag based on today's date (e.g. `mar5`). The branch `autoresearch/<tag>` must not already exist — this is a fresh run.
2. **Create the branch**: `git checkout -b autoresearch/<tag>` from current master.
3. **Read the in-scope files**: The repo is small. Read these files for full context:
   - `README.md` — repository context.
   - `train.py` — the file you modify. RL algorithm, environment setup, hyperparameters, training loop.
4. **Verify environment setup**: Confirm MuJoCo and the required gym/env packages are installed. If not, tell the human to set up the environment first.
5. **Initialize results.tsv**: Create `results.tsv` with just the header row. The baseline will be recorded after the first run.
6. **Confirm and go**: Confirm setup looks good.

Once you get confirmation, kick off the experimentation.


## Capturing Your Process (Atomic Notes)

Every experiment cycle produces an evolving Markdown file in `notes/` at the **repo root** (not relative to the worktree). Treat the TSV as your Database (metrics for machines) and the Zettelkasten as your Journal (reasoning for humans).

Notes are tracked in git. The invariant that keeps them safe: **notes commits are always separate from train.py commits**, so a discard reset never touches them.

The key metric is **mean episode return** (mean cumulative reward over evaluation episodes). Higher is better.

**Per-cycle steps:**

1. **Draft** (before touching train.py): Create `notes/YYYYMMDDHHMM_slug.md` with Hypothesis, Target Metric, and Code Change. Commit it immediately — this anchors the note in history before the experiment:
   ```
   git add notes/YYYYMMDDHHMM_slug.md
   git commit -m "Note: SLUG pre-run"
   ```

2. **Execute**: Modify `train.py` based on the note, then commit:
   ```
   git commit train.py -m "ExpN: description"
   ```

3. **Finalize**: Post-run, append the Result (mean episode return), Git Hash, and a 1-sentence Verdict to the note.

4. **Commit outcome** — always, regardless of keep or discard, and always AFTER any reset:
   ```
   git add notes/YYYYMMDDHHMM_slug.md results.tsv
   git commit -m "Log SLUG [keep|discard]"
   ```

5. **Index & Compress**: Link the note in `notes/index.md`. Every 5 cycles, summarize the last 5 notes into an `insight_NN_expXtoY.md` file.

**Safe Reset Rule**: On a discard, reset only the train.py experiment commit — the pre-run note commit immediately below it is unaffected:
```
git reset HEAD~1        # removes the train.py commit; pre-run note commit stays
git checkout -- train.py  # discard working tree changes to train.py
```
Then proceed to Finalize (step 3) and Commit outcome (step 4) as normal. Never use `git reset --hard` — it wipes the working tree.


## Experimentation

Each experiment runs on a single GPU. The training script runs for a **fixed time budget of 5 minutes** (wall clock training time, excluding startup/compilation). You launch it simply as: `uv run train.py`.

**What you CAN do:**
- Modify `train.py` — this is the only file you edit. Everything is fair game: RL algorithm, network architecture, optimizer, hyperparameters, reward shaping, training loop, etc.

**What you CANNOT do:**
- Install new packages or add dependencies. You can only use what's already in `pyproject.toml`.
- Change the environment itself (task definition, physics). The MuJoCo flying environment is fixed.

**The goal is simple: maximize mean episode return on the MuJoCo flying environment.** Since the time budget is fixed, you don't need to worry about training time — it's always 5 minutes. Everything is fair game: change the RL algorithm, the network, the optimizer, the hyperparameters, the reward shaping. The only constraint is that the code runs without crashing and finishes within the time budget.

**VRAM** is a soft constraint. Some increase is acceptable for meaningful return gains, but it should not blow up dramatically.

**Simplicity criterion**: All else being equal, simpler is better. A small improvement that adds ugly complexity is not worth it. Conversely, removing something and getting equal or better results is a great outcome — that's a simplification win. When evaluating whether to keep a change, weigh the complexity cost against the improvement magnitude. A tiny return gain that adds 20 lines of hacky code? Probably not worth it. A gain from deleting code? Definitely keep. An improvement of ~0 but much simpler code? Keep.

**The first run**: Your very first run should always be to establish the baseline, so you will run the training script as is.

## Output format

Once the script finishes it prints a summary like this:

```
---
mean_return:      1234.56
std_return:       89.12
episodes:         100
training_seconds: 300.1
total_seconds:    325.9
peak_vram_mb:     4096.0
num_steps:        150000
```

Note that the script is configured to always stop after 5 minutes, so depending on the computing platform the numbers might look different. You can extract the key metric from the log file:

```
grep "^mean_return:\|^peak_vram_mb:" run.log
```

## Logging results

When an experiment is done, log it to `results.tsv` (tab-separated, NOT comma-separated — commas break in descriptions).

The TSV has a header row and 5 columns:

```
commit	mean_return	memory_gb	status	description
```

1. git commit hash (short, 7 chars)
2. mean episode return achieved (e.g. 1234.56) — use 0.000000 for crashes
3. peak memory in GB, round to .1f (e.g. 4.0 — divide peak_vram_mb by 1024) — use 0.0 for crashes
4. status: `keep`, `discard`, or `crash`
5. short text description of what this experiment tried

Example:

```
commit	mean_return	memory_gb	status	description
a1b2c3d	850.00	4.0	keep	baseline PPO
b2c3d4e	920.50	4.1	keep	increase entropy coeff to 0.01
c3d4e5f	780.00	4.0	discard	switch to SAC (diverged)
d4e5f6g	0.000000	0.0	crash	double network width (OOM)
```

## The experiment loop

The experiment runs on a dedicated branch (e.g. `autoresearch/mujoco-rl` or `autoresearch/mujoco-rl-v2`).

LOOP FOREVER:

1. Look at the git state: the current branch/commit we're on.
2. Draft `notes/YYYYMMDDHHMM_slug.md` with Hypothesis, Target Metric, and Code Change.
3. Commit the pre-run note: `git add notes/SLUG.md && git commit -m "Note: SLUG pre-run"`
4. Tune `train.py` with the experimental idea.
5. Commit train.py: `git commit train.py -m "ExpN: description"`
6. Run the experiment: `uv run train.py > run.log 2>&1` (redirect everything — do NOT use tee or let output flood your context)
7. Read out the results: `grep "^mean_return:\|^peak_vram_mb:" run.log`
8. If the grep output is empty, the run crashed. Run `tail -n 50 run.log` to read the Python stack trace and attempt a fix. If you can't get things to work after more than a few attempts, give up.
9. Finalize the note (append mean_return, git hash, verdict) and update `results.tsv`.
10. If mean_return improved (higher): commit outcome and advance.
    `git add notes/SLUG.md results.tsv && git commit -m "Log SLUG keep"`
11. If mean_return is equal or worse: reset the train.py commit, then commit outcome.
    `git reset HEAD~1 && git checkout -- train.py`
    `git add notes/SLUG.md results.tsv && git commit -m "Log SLUG discard"`

The idea is that you are a completely autonomous researcher trying things out. If they work, keep. If they don't, discard. And you're advancing the branch so that you can iterate. If you feel like you're getting stuck in some way, you can rewind but you should probably do this very very sparingly (if ever).

**Timeout**: Each experiment should take ~5 minutes total (+ a few seconds for startup and eval overhead). If a run exceeds 10 minutes, kill it and treat it as a failure (discard and revert).

**Crashes**: If a run crashes (OOM, or a bug, or etc.), use your judgment: If it's something dumb and easy to fix (e.g. a typo, a missing import), fix it and re-run. If the idea itself is fundamentally broken, just skip it, log "crash" as the status in the tsv, and move on.

**NEVER STOP**: Once the experiment loop has begun (after the initial setup), do NOT pause to ask the human if you should continue. Do NOT ask "should I keep going?" or "is this a good stopping point?". The human might be asleep, or gone from a computer and expects you to continue working *indefinitely* until you are manually stopped. You are autonomous. If you run out of ideas, think harder — read papers referenced in the code, re-read the in-scope files for new angles, try combining previous near-misses, try more radical architectural changes. The loop runs until the human interrupts you, period.

As an example use case, a user might leave you running while they sleep. If each experiment takes you ~5 minutes then you can run approx 12/hour, for a total of about 100 over the duration of the average human sleep. The user then wakes up to experimental results, all completed by you while they slept!
