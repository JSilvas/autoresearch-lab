# 2026031790_wd_sqrt_decay

**Hypothesis**: Current WD schedule is WD*(1-progress) (linear decay). Constant WD was catastrophically worse (Exp82, +0.009). Cosine LR warmdown just failed (Exp89, +0.004). The WD schedule shape controls how long regularization stays active. Square root decay — WD*(1-progress)^0.5 — keeps WD higher for longer (at progress=0.8: linear=0.20*WD, sqrt=0.447*WD). This means more sustained regularization during the warmdown phase. Whether this helps or hurts depends on the optimal regularization trajectory.
**Target Metric**: val_bpb < 1.369316
**Code Change**: get_weight_decay: WD*(1-progress) → WD*(1-progress)^0.5. LR schedule reverted to linear.

---
**Result**: val_bpb=1.372756
**Git Hash**: 0ca90a0
**Verdict**: DISCARD. Worse (+0.003440). Sqrt decay keeps WD too high for too long. WD shape confirmed: constant (+0.009), sqrt (+0.003), linear (best). Faster decay (beyond linear) untested but likely also worse.
