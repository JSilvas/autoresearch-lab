# 20260317110_mixed_head_windows

**Hypothesis**: Current setup is inter-layer multi-scale (layer 0=S=32, layer 1=S=128). Testing intra-layer multi-scale: within every S attention layer, head 0 attends locally (S=32) while head 1 attends at medium range (S=128). Each layer simultaneously captures both granularities, potentially allowing richer per-layer representations.
**Target Metric**: val_bpb < 1.368062
**Code Change**: MIXED_HEAD_WINDOWS=True. Added `mixed_head_windows` field to GPTConfig and 4D per-head mask in CausalSelfAttention when w_h1 > 0. Every S layer now returns (32, 128) window tuple.

---
**Result**: 1.380770 (Δ+0.013 vs best 1.368062)
**Git Hash**: 98b31bf
**Verdict**: DISCARD — Inter-layer hierarchy wins. Intra-layer multi-scale fails because mixed heads see the same un-processed input at different scales, losing the compositional stack (local features → medium integration). Layer specialization is more powerful than head specialization.
