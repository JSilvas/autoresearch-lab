# Insight 09: Exp72-77 — WARMDOWN×MATRIX_LR co-optimization, joint optimum found

## Summary
Discovered strong **co-optimization interaction** between WARMDOWN_RATIO and MATRIX_LR. Joint optimum is **(MATRIX_LR=0.080, WARMDOWN_RATIO=0.60)** at val_bpb=**1.369316** (cumulative Δ=-0.002443 from session start 1.371759).

## Co-optimization Path
1. WARMDOWN=0.50, MATRIX_LR=0.095 → 1.371759 (session start)
2. WARMDOWN=0.65, MATRIX_LR=0.095 → 1.371208 (warmdown discovery)
3. WARMDOWN=0.65, MATRIX_LR=0.080 → 1.369486 (MATRIX_LR discovery, Δ=-0.001722!)
4. WARMDOWN=0.60, MATRIX_LR=0.080 → **1.369316** (warmdown re-tune, Δ=-0.000170)

## WARMDOWN sweep at MATRIX_LR=0.080
| WARMDOWN | val_bpb |
|----------|---------|
| 0.55 | 1.369780 |
| **0.60** | **1.369316** |
| 0.65 | 1.369486 |
| 0.70 | 1.369773 |

## Why the Co-dependency
- MATRIX_LR governs Muon update magnitude per step
- WARMDOWN_RATIO governs how many steps are spent in the decay phase
- Lower MATRIX_LR (0.080 vs 0.095) pairs better with moderate warmdown (0.60) vs long warmdown (0.65)
- At lower MATRIX_LR, less warmdown time is needed to converge → optimum shifts from 0.65 to 0.60

## Other Axes Confirmed Robust
- EMBEDDING_LR=0.7, SCALAR_LR=0.7, WEIGHT_DECAY=0.15, FINAL_LR_FRAC=0.08
- Only MATRIX_LR needed recalibration after WARMDOWN change

## What's Next
- UNEMBEDDING_LR retest at new joint config
- Muon Nesterov/polar_express params (rarely tried)
- Consider if any architecture tweaks are worth retrying at final config
