# 2026031750_window_eighth

**Hypothesis**: SHORT_WINDOW_FRAC=4 (S=512) gave new best 1.373701. Continue shrinking: FRAC=8 → S=256 tokens. Even fewer S-layer FLOPs → even more optimizer steps. Risk: 256-token local context in first 2 layers may be too narrow for TinyStories text patterns.
**Target Metric**: val_bpb < 1.373701
**Code Change**: SHORT_WINDOW_FRAC = 4 → 8

---
**Result**: TBD
**Git Hash**: TBD
**Verdict**: TBD
