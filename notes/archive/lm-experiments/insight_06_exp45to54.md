# insight_06_exp45to54

**Experiments covered**: Exp45-46 (VE sweep), Exp47-48 (EMBEDDING_LR re-tune), Exp49-53 (window size sweep), Exp54 (MATRIX_LR re-tune at S=64)

## KEY DISCOVERY: Short sliding window is the biggest lever

### Window size sweep (Exp49-53) — total Δ=-0.003915
The most impactful series of experiments in this session:
- S=1024 (FRAC=2): 1.375674 baseline
- S=512 (FRAC=4): 1.373701 → Δ-0.001973
- S=256 (FRAC=8): 1.372684 → Δ-0.001017
- S=128 (FRAC=16): 1.372200 → Δ-0.000484
- **S=64 (FRAC=32): 1.371759 → Δ-0.000441** ← NEW BEST
- S=32 (FRAC=64): 1.374682 (worse) ← floor found

**S=64 is optimal**: 64-token local window in first 2 layers. Each halving gave diminishing gains. At S=32 the context was too narrow.

**Why it works**: With seq_len=2048, the S-layers need only ~3% of the full context for initial feature extraction. The final full-attention layer handles global synthesis. This is essentially a "local feature extractor + global aggregator" pattern. Smaller S = more optimizer steps (fewer FLOPs per step) = better convergence in 5-minute budget.

**Key insight**: The step-starvation principle applies to the sliding window size, not just depth and model size. Minimizing window size (while keeping one full-context layer at the end) is a powerful free optimization.

### VE sweep confirmed (Exp45-46)
- 0 VE → 1.432, 1 VE → 1.383, 2 VE (alternating) → 1.376 (best), 3 VE → 1.387
- Inverted-U. Alternating 2/3 VE is optimal. Axis exhausted.

### EMBEDDING_LR confirmed (Exp47-48)
- 0.65→1.377, 0.7→1.376 (best), 0.75→1.376. Very flat — 0.7 confirmed optimal.

### MATRIX_LR robust (Exp54)
- MATRIX_LR=0.095 still optimal at S=64 — no interaction with window size.

## Current best state
- val_bpb: **1.371759** (Exp52, commit 5bc773a)
- DEPTH=3, dim=192, MLP 3x, SSL, S=64, EMBEDDING_LR=0.7, MATRIX_LR=0.095, SCALAR_LR=0.7, WEIGHT_DECAY=0.15, ADAM_BETAS=(0.75, 0.95), SHORT_WINDOW_FRAC=32

## Remaining exploration
- SCALAR_LR re-tune with S=64 (was optimized at S=1024)
- DEPTH=4 with AR=48 (dim=192) — now cheaper due to S=64 (18% step cost vs 50%+ before)
- MLP width at S=64 (4x may now be viable with faster S-layers)
