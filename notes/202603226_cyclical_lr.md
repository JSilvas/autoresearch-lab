# 202603226_cyclical_lr

**Hypothesis**: SGDR-style two-cycle cosine LR gives the model a second warm-restart at 50% of training. The first cycle (0→50%) lets the model find a local minimum; the second (50→100%) re-heats and explores, potentially finding a better minimum. Mar17 Exp89 tested single cosine warmdown (worse), but two-cycle restarts are architecturally different. Schedule: lrm = max(0.5*(1+cos(π*(t*2 mod 1))), FINAL_LR_FRAC). At t=0: lrm=1.0; t=0.25: 0.5; t=0.5: restarts to 1.0; t=0.75: 0.5; t=1.0: 0.08.
**Target Metric**: val_bpb < 1.381845
**Code Change**: `import math`; `get_lr_multiplier` uses two-cycle cosine: `lrm = max(0.5*(1+cos(π*(adjusted*2%1))), FINAL_LR_FRAC)`. WARMDOWN_RATIO and the flat-top phase are removed (cosine handles entire schedule).

---
**Result**: 1.413364 (376 steps; Δ+0.032 vs baseline)
**Git Hash**: af931d3
**Verdict**: DISCARD — Worse than linear warmdown. The two cosine cycles remove the flat-top LR plateau (40% of training at peak LR in the baseline). That plateau is doing real exploration work. The cosine shape hurts because LR starts declining immediately from step 0, giving less time at peak. The warm-restart at 50% doesn't compensate — the model just gets destabilized and needs to re-converge. Confirms: our linear warmdown (flat top → linear decay) is better than any cosine variant.
