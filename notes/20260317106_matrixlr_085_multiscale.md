# 20260317106_matrixlr_085_multiscale

**Hypothesis**: MATRIX_LR=0.080 was tuned at uniform S=64. With S=32+S=128 multi-scale, the attention gradient dynamics change (smaller first-layer window, different gradient magnitudes). MATRIX_LR was the most sensitive hyperparameter (Δ-0.0013 at Exp70). Testing 0.085 to check if the optimum has shifted upward at the new config.
**Target Metric**: val_bpb < 1.368062
**Code Change**: MATRIX_LR 0.080→0.085. SHORT_WINDOW_FRAC=64 (S=32), SHORT_WINDOW_FRAC_2=16 (S=128).

---
**Result**: 1.372041 (Δ+0.004 vs S=32+S=128 best 1.368062)
**Git Hash**: 36744a8
**Verdict**: DISCARD — MATRIX_LR=0.085 much worse at multi-scale config. 0.080 confirmed as ceiling. Next: test 0.075 in case optimum shifted downward.
