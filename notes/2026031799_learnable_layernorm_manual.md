# 2026031799_learnable_layernorm_manual

**Hypothesis**: Previous 3 attempts at learnable LayerNorm all showed identical "loss stall at 7.38" pattern despite different dtype fixes. Root cause: MPS F.layer_norm(x, ..., weight, bias) backward likely has a bug zeroing dL/dx when parameters are provided (stateless F.layer_norm works fine). Fix: implement LayerNorm manually using only mean/var/rsqrt — all standard MPS ops with working backward implementations. This avoids the F.layer_norm kernel entirely while preserving full learnable affine capability (gamma/beta per dimension).
**Target Metric**: val_bpb < 1.369316
**Code Change**: LearnableNorm.forward uses manual mean/var computation instead of F.layer_norm. Block adds ln1/ln2. GPT adds ln_emb/ln_out. setup_optimizer splits h.parameters() into 2D→Muon and 1D→AdamW (lr=scalar_lr*0.1=0.07).

---
**Result**: N/A — loss 7.37 at step 254 (58% through, lrm=0.72, deep into warmdown) — same broken pattern as all previous attempts
**Git Hash**: cef5777
**Verdict**: DISCARD — 4th consecutive LearnableNorm failure. Even manual mean/var/rsqrt ops can't fix the issue. The MPS backward bug appears to affect NOT F.layer_norm itself but the broader gradient computation chain through any learnable normalization on MPS bfloat16 embeddings. Permanently abandoning learnable norm.
