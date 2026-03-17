# insight_05_exp36to44

**Experiments covered**: Exp36-37 (beta2 sweep), Exp38 (MLP 2x at DEPTH=3), Exp39 (ASPECT_RATIO=56), Exp40 (Muon momentum 0.75), Exp41 (LSS window), Exp42 (HEAD_DIM=96), Exp43 (no VE), Exp44 (plain ReLU)

## Key findings

### All hyperparameter axes now exhausted
- **beta2**: 0.90→1.378, 0.95→1.376 (best), 0.99→1.379. Optimal at 0.95. ✓
- **MLP width at DEPTH=3**: 2x worse (+0.006). 3x is optimal. Capacity > steps at this scale. ✓
- **ASPECT_RATIO**: 56 worse (+0.004). dim=192 is the capacity floor. ✓
- **Muon momentum**: 0.75→1.382, 0.80→1.376 (best), 0.85→1.378. Optimal at 0.80. ✓

### Window ordering: last layer must be full (Exp41)
- "LSS" (L,S,S) = 1.381 — full first, sliding last → much worse
- "SSL" (S,S,L) = 1.375674 — sliding first, full last → optimal
- **Rule confirmed**: Last transformer layer must have global attention for autoregressive prediction.

### Single-head attention is optimal (Exp42)
- HEAD_DIM=96 (2 heads) = 1.404 — much worse (+0.028)
- HEAD_DIM=128 (1 head) is strongly preferred
- Larger head dimension > more heads at this scale

### Architecture is fragile: VE and ReLU² are load-bearing (Exp43-44)
- No VE = 1.432 (+0.056): Value Embeddings are a core architectural feature, not optional
- Plain ReLU = 1.396 (+0.021): ReLU² squaring is critical for this architecture
- Both components are non-negotiable

## Current best state
- val_bpb: **1.375674** (Exp32, commit ece6e80, SCALAR_LR=0.7)
- Stuck here for 12 consecutive experiments

## Remaining exploration directions
- VE pattern: last-layer only (layer 2 only, fewer params), or all layers (add layer 1)
- Shorter sliding window (T/4 instead of T/2) for more steps in sliding layers
- Constant weight decay (no linear decay schedule)
- ns_steps reduction (3-4 instead of 5 iterations)
- Revisit EMBEDDING_LR/MATRIX_LR now that SCALAR_LR=0.7 is locked

## Meta-insight
The architecture has a stable core: DEPTH=3, ReLU², VE on alternating layers, SSL window, single large head. Most changes that reduce capacity (fewer VE, smaller head, less MLP, lower dim) hurt more than they help from extra steps. We may be at or near the Pareto frontier for this 5-minute compute budget.
