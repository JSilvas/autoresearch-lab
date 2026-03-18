# 2026031798_learnable_layernorm

**Hypothesis**: Current norm() is stateless F.layer_norm with no learnable parameters (no gamma/beta). Every major modern transformer (GPT-2, Llama, Gemma, etc.) uses learnable affine LayerNorm. Without affine, the model cannot learn different feature scales per-dimension after normalization. Adding learnable gamma (init 1.0) and beta (init 0.0) to all 8 norms (ln1/ln2 per block × 3 blocks + ln_emb + ln_out) adds 8 × 2 × 256 = 4096 parameters (0.04% of total). These are given LR = scalar_lr × 0.1 = 0.07, conservative to prevent instability. Key benefit: each norm can learn to amplify/suppress specific feature dimensions, giving the model significantly more representational power.
**Target Metric**: val_bpb < 1.369316
**Code Change**: Block: add self.ln1/ln2 = nn.LayerNorm(n_embd). GPT: add self.ln_emb/ln_out = nn.LayerNorm(n_embd). setup_optimizer: split transformer.h params by ndim (2D→Muon, 1D→AdamW). TOTAL_BATCH_SIZE/DEVICE_BATCH_SIZE reverted.

---
**Result**: TBD
**Git Hash**: TBD
**Verdict**: TBD
