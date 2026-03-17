# 202603172_alternating_ve

**Hypothesis**: VE on alternating layers (1,3) was the mar15 best config. All-layer VE (master baseline) may be redundant or harmful — alternating gives more unique per-layer signal.
**Target Metric**: val_bpb < 1.407007
**Code Change**: `has_ve` returns True only for even-indexed layers from the end (i.e., layers 1 and 3 for DEPTH=4).

---
**Result**: val_bpb=1.393200
**Git Hash**: cfeacbf
**Verdict**: KEEP. Clear win — +0.013807 improvement. Alternating VE is better than all-layer VE.
