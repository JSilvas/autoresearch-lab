# insight_04_exp30to35

**Experiments covered**: Exp30 (DEPTH=2 retest), Exp31-33 (SCALAR_LR sweep), Exp34-35 (UNEMBEDDING_LR sweep)

## Key findings

### DEPTH=2 is architecturally insufficient (Exp30)
- With full optimized hyperparams (EMBEDDING_LR=0.7, MATRIX_LR=0.095, SSL, beta1=0.75), DEPTH=2 still gives 1.437080
- Only improved ~0.007 from old hyperparams run (1.444568). Confirms: DEPTH=2 fails due to capacity, not tuning.
- **Conclusion**: DEPTH=3 is the minimum viable depth. Do not retry DEPTH=2.

### SCALAR_LR peak at 0.7 (Exp31-33) — new best 1.375674
- Sweep: 0.3→1.381, 0.5→1.376 (old baseline), **0.7→1.375674** (new best), 0.9→1.376
- Clean inverted-U curve. Higher than 0.5 is better; 0.7 is optimal.
- **Why**: Per-layer scalars (resid_lambdas) set residual stream magnitude. They need to adapt quickly in the early steps to balance residual vs layer output. 0.5 was too conservative; 0.7 gives faster convergence of scale parameters.
- **Locked at 0.7**.

### UNEMBEDDING_LR optimal at 0.004 (Exp34-35)
- Sweep: 0.002→1.389, **0.004→1.376** (best), 0.008→1.380
- Both directions worse. Default 0.004 is optimal for this model size/depth.
- **Axis exhausted**.

## Current best state
- val_bpb: **1.375674** (Exp32, commit ece6e80)
- DEPTH=3, dim=192, MLP 3x, SSL, EMBEDDING_LR=0.7, MATRIX_LR=0.095, SCALAR_LR=0.7, UNEMBEDDING_LR=0.004, WEIGHT_DECAY=0.15, ADAM_BETAS=(0.75, 0.95)

## Remaining axes to explore
- ADAM_BETAS beta2 (currently 0.95 — never tuned)
- ASPECT_RATIO (currently 64 → dim=192 — smaller model could give more optimizer steps)
- MLP width at DEPTH=3 with full optimized hyperparams (2x not yet tested in this config)
- Architecture structure (no-MLP layers, HEAD_DIM variation)
