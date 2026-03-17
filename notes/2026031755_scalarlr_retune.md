# 2026031755_scalarlr_retune

**Hypothesis**: SCALAR_LR=0.7 was optimized at S=1024 (Exp32-33). With S=64 now locked, the model dynamics shifted — S-layers are nearly free, MLP dominates. Scalars (resid_lambdas) behavior may differ. Try SCALAR_LR=0.8 (one step above the previous optimum).
**Target Metric**: val_bpb < 1.371759
**Code Change**: SCALAR_LR = 0.7 → 0.8

---
**Result**: TBD
**Git Hash**: TBD
**Verdict**: TBD
