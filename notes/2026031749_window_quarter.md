# 2026031749_window_quarter

**Hypothesis**: "S" sliding window currently = seq_len//2 = 1024. Reducing to seq_len//4 = 512 saves attention FLOPs in the 2 sliding layers: ~16% fewer total ops per step → ~16% more optimizer steps. Risk: shallower local context (512 vs 1024 tokens) in layers 0-1. Last layer always stays at full 2048. Added SHORT_WINDOW_FRAC=4 param to control this.
**Target Metric**: val_bpb < 1.375674
**Code Change**: SHORT_WINDOW_FRAC = 2 → 4 (new configurable param; was hardcoded //2)

---
**Result**: TBD
**Git Hash**: TBD
**Verdict**: TBD
