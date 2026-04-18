# 20260317107_matrixlr_075_multiscale

**Hypothesis**: After 0.085 was worse at multi-scale, test if optimum shifted downward to 0.075.
**Target Metric**: val_bpb < 1.368062
**Code Change**: MATRIX_LR 0.080→0.075. SHORT_WINDOW_FRAC=64 (S=32), SHORT_WINDOW_FRAC_2=16 (S=128).

---
**Result**: 1.370853 (Δ+0.003 vs best 1.368062)
**Git Hash**: ba7d6f4
**Verdict**: DISCARD — 0.080 confirmed optimal at S=32+S=128 config. Both 0.075 and 0.085 worse. MATRIX_LR=0.080 is robust across configs.
