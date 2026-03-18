# 2026031799_learnable_layernorm_manual

**Hypothesis**: Previous 3 attempts at learnable LayerNorm all showed identical "loss stall at 7.38" pattern despite different dtype fixes. Root cause: MPS F.layer_norm(x, ..., weight, bias) backward likely has a bug zeroing dL/dx when parameters are provided (stateless F.layer_norm works fine). Fix: implement LayerNorm manually using only mean/var/rsqrt — all standard MPS ops with working backward implementations. This avoids the F.layer_norm kernel entirely while preserving full learnable affine capability (gamma/beta per dimension).
**Target Metric**: val_bpb < 1.369316
**Code Change**: LearnableNorm.forward uses manual mean/var computation instead of F.layer_norm. Block adds ln1/ln2. GPT adds ln_emb/ln_out. setup_optimizer splits h.parameters() into 2D→Muon and 1D→AdamW (lr=scalar_lr*0.1=0.07).

---
**Result**: TBD
**Git Hash**: TBD
**Verdict**: TBD
