# Insight Note 03 — Experiments 18–25

## Summary

Starting best: **1.380054** (DEPTH=3, MLP 3x).
Best after Exp18–25: **1.376603** (EMBEDDING_LR=0.7).

## Confirmed for DEPTH=3+SSL Architecture

| Parameter | Optimal | Tried | Notes |
|---|---|---|---|
| WEIGHT_DECAY | 0.15 | 0.10, 0.15✓, 0.20 | Same as DEPTH=4 |
| WINDOW_PATTERN | "SSL" | "L", "SSL"✓ | Sliding saves attn FLOPs |
| MATRIX_LR | 0.095 | 0.09, 0.095✓, 0.10 | Slightly higher than DEPTH=4 |
| EMBEDDING_LR | 0.7 | 0.6, 0.7✓, 0.8 | Higher than DEPTH=4 (0.6) |
| Muon momentum | 0.80 | 0.80✓, 0.85 | Same as DEPTH=4 |
| Batch size | 32768 | 32768✓, 16384 | Larger batch wins (less noise) |

## What Failed
- WD=0.20: 1.383020 — more regularization not needed
- SSL confirmed good, but "SL" not yet tested
- Half batch (BS=8): 1.387704 — 2x steps but gradient noise hurts

## Key Principle Still Active
More optimizer steps = better, but only if gradient quality is maintained. This limits:
- Smaller batch (too noisy)
- Larger dim (too few steps)
- More depth (too few steps)

## Current Configuration (Best Known: 1.376603)
- DEPTH=3, ASPECT_RATIO=64, dim=256 (2 heads, HEAD_DIM=128)
- MLP: 3x = 768 hidden, ReLU²
- WINDOW_PATTERN="SSL"
- WD=0.15, MATRIX_LR=0.095, EMBEDDING_LR=0.7
- ADAM_BETAS=(0.7, 0.95), momentum=0.80
- WARMDOWN=0.50, FINAL_LR_FRAC=0.08

## Next Direction
Fine-tune remaining knobs: ADAM_BETAS beta1, WARMDOWN_RATIO with new config, UNEMBEDDING_LR. Also consider removing resid_lambdas or x0 skip (simplification check).
