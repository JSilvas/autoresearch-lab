# 20260317101_multiscale_reversed

**Hypothesis**: Exp100 showed S=64→S=128→L=2048 (fine-to-coarse) beats uniform S=64. Does layer order matter? Testing reversed S=128→S=64→L=2048 (coarse-to-fine). The intuition: layer 0 scans wider context first to identify relevant spans, then layer 1 refines with local attention. Or: coarse-to-fine may interfere with attention because residual x already has medium-range info that the next local layer must de-noise.
**Target Metric**: val_bpb < 1.368544
**Code Change**: SHORT_WINDOW_FRAC=16 (S=128 first), SHORT_WINDOW_FRAC_2=32 (S=64 second). Layer 0: S=128, Layer 1: S=64, Layer 2: L=2048.

---
**Result**: 1.370738 (Δ+0.002194 vs Exp100 best 1.368544)
**Git Hash**: 94556e6
**Verdict**: DISCARD — fine-to-coarse order (S=64 first, S=128 second) is significantly better than coarse-to-fine. Confirms Exp100 finding: local attention first, medium-range second is the correct hierarchy. Likely because layer 0 needs to extract local patterns before layer 1 can use them in broader context.
