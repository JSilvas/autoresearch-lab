# 20260317100_multiscale_windows

**Hypothesis**: Both S layers currently use identical S=64 window. Creating a hierarchy (S=64 local → S=128 medium → L=2048 global) might let the model capture patterns at multiple scales simultaneously: layer 0 attends to local n-grams/word-level (64 tokens), layer 1 attends to sentence-level (128 tokens), layer 2 attends globally. Uniform S=64 forces both local layers to the same granularity; multi-scale exploits the sequential processing structure. S=128 alone was worse than S=64 (Exp51 vs Exp52: 1.372200 vs 1.371759), but combining S=64+S=128 in different layers has not been tried.
**Target Metric**: val_bpb < 1.369316
**Code Change**: Add SHORT_WINDOW_FRAC_2=16 (S2=128). Modify _compute_window_sizes to alternate S layers between frac_1 (S=64) and frac_2 (S=128). Layer 0: S=64, Layer 1: S=128, Layer 2: L=2048.

---
**Result**: TBD
**Git Hash**: TBD
**Verdict**: TBD
