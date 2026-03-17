# 2026031775_warmdown60_retest

**Hypothesis**: WARMDOWN_RATIO=0.60 was 1.371320 at MATRIX_LR=0.095. Now at MATRIX_LR=0.080, check if this direction has also improved enough to challenge 0.65. 0.70 just retested and confirmed worse. Bracket the other side to confirm 0.65 is robustly optimal at new MATRIX_LR.
**Target Metric**: val_bpb < 1.369486
**Code Change**: WARMDOWN_RATIO = 0.65 → 0.60

---
**Result**: TBD
**Git Hash**: TBD
**Verdict**: TBD
