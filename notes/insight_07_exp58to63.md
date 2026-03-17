# Insight 07: Exp58-63 — WARMDOWN_RATIO sweep, optimal at 0.65

## Summary
Exp58 (FINAL_LR_FRAC=0.12) was a dead end. The main discovery in this batch is that **WARMDOWN_RATIO=0.65 is optimal**, yielding a new best of **1.371208** (total Δ=-0.000551 from 0.50 baseline).

## WARMDOWN_RATIO Sweep Results
| Ratio | val_bpb | Δ |
|-------|---------|---|
| 0.45 (Exp59) | 1.372749 | +0.000990 |
| 0.50 (baseline) | 1.371759 | — |
| 0.55 (Exp60) | 1.371455 | -0.000304 |
| 0.60 (Exp61) | 1.371320 | -0.000439 |
| 0.65 (Exp62) | **1.371208** | **-0.000551** |
| 0.70 (Exp63) | 1.371448 | -0.000311 |

## Interpretation
- WARMDOWN_RATIO=0.65 is optimal: U-shaped response centered around 0.65
- Shorter warmdown (0.45) is strictly worse — too little time for LR descent
- Longer warmdown (0.65) is better than 0.50, likely because S=64's extra steps benefit from a more gradual decay that maintains learning late
- This is an S=64-specific effect: at S=1024, Exp11 (0.55) was a marginal discard vs 0.50

## What's Next
- WEIGHT_DECAY re-tune at S=64 with WARMDOWN_RATIO=0.65
- FINAL_LR_FRAC at new warmdown setting (potential interaction)
- Other LR schedule parameters confirmed optimal: WARMUP=0.0, FINAL_LR_FRAC=0.08
