# 2026031750_window_eighth

**Hypothesis**: SHORT_WINDOW_FRAC=4 (S=512) gave new best 1.373701. Continue shrinking: FRAC=8 → S=256 tokens. Even fewer S-layer FLOPs → even more optimizer steps. Risk: 256-token local context in first 2 layers may be too narrow for TinyStories text patterns.
**Target Metric**: val_bpb < 1.373701
**Code Change**: SHORT_WINDOW_FRAC = 4 → 8

---
**Result**: val_bpb=1.372684
**Git Hash**: 0257683
**Verdict**: KEEP. New best (1.373701→1.372684, Δ=-0.001017). Trend continues: smaller S window = more steps = better. Try S=128 (FRAC=16) next.
