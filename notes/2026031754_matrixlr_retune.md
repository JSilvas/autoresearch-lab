# 2026031754_matrixlr_retune

**Hypothesis**: With SHORT_WINDOW_FRAC=32 (S=64) locked, the model is now MLP-dominant — first 2 layers do 64-token local attention (trivial cost) + MLP. Muon optimizer handles all matrix params (attention + MLP weights). With MLP being relatively more important in the compute budget, MATRIX_LR=0.095 may no longer be optimal. Try 0.10 (slightly higher).
**Target Metric**: val_bpb < 1.371759
**Code Change**: MATRIX_LR = 0.095 → 0.10

---
**Result**: val_bpb=1.374063
**Git Hash**: 97c5209
**Verdict**: DISCARD. MATRIX_LR=0.095 still optimal even in MLP-dominant S=64 regime. No interaction effect with window size.
