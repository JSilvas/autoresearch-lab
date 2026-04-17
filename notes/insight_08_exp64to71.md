# Insight 08: Exp64-71 — MATRIX_LR re-tune at WARMDOWN=0.65, new best 1.369486

## Summary
Major discovery: **MATRIX_LR needs complete re-tuning after WARMDOWN_RATIO change**. Previous optimum (0.095 at WARMDOWN=0.50) was far off — optimal is now **MATRIX_LR=0.080** at WARMDOWN=0.65, yielding a new best of **1.369486** (cumulative Δ=-0.002273 from session start at 1.371759).

## MATRIX_LR Sweep at WARMDOWN=0.65
| MATRIX_LR | val_bpb | Δ from 0.095 |
|-----------|---------|--------------|
| 0.095 (old) | 1.371208 | — |
| 0.090 (Exp68) | 1.370933 | -0.000275 |
| 0.085 (Exp69) | 1.370791 | -0.000417 |
| **0.080 (Exp70)** | **1.369486** | **-0.001722** |
| 0.075 (Exp71) | 1.369538 | -0.001670 |

## Why MATRIX_LR Shifted
- At WARMDOWN=0.50, the model spent 50% in decay. At WARMDOWN=0.65, it spends 65% in decay.
- Muon (matrix optimizer) runs many more steps in the decay phase.
- A lower base MATRIX_LR prevents overshooting in the extended decay regime.
- The jump from 0.085→0.080 was non-linear (+1305 improvement vs +142 for 0.090→0.085), suggesting a threshold effect.

## Other Results This Batch
- WEIGHT_DECAY: 0.12 and 0.18 both worse — 0.15 robust
- FINAL_LR_FRAC: 0.06 worse — 0.08 robust
- ADAM beta1: 0.70 marginally worse — 0.75 robust

## What's Next
- Re-tune EMBEDDING_LR, SCALAR_LR at new config (may have similar interaction)
- Re-check WARMDOWN_RATIO with new MATRIX_LR=0.080 (potential positive interaction)
