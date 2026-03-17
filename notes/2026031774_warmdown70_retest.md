# 2026031774_warmdown70_retest

**Hypothesis**: WARMDOWN_RATIO=0.70 was a discard at MATRIX_LR=0.095 (Exp63: 1.371448 vs best 1.371208). But MATRIX_LR has since shifted to 0.080. With the Muon LR being lower, the model dynamics at the long warmdown tail have changed — maybe 0.70 now becomes optimal. The interaction between WARMDOWN_RATIO and MATRIX_LR may be significant.
**Target Metric**: val_bpb < 1.369486
**Code Change**: WARMDOWN_RATIO = 0.65 → 0.70

---
**Result**: TBD
**Git Hash**: TBD
**Verdict**: TBD
