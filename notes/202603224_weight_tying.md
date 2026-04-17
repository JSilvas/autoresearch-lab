# 202603224_weight_tying

**Hypothesis**: Weight tying (lm_head.weight = wte.weight) reduces the model by ~2M params (8192×256) and forces input/output embeddings to be coherent. Standard in GPT-2 and most small LMs. With fewer params, the model might train faster (more throughput) and the shared embedding space may improve generalization. The EMBEDDING_LR=0.7 will now serve both roles.
**Target Metric**: val_bpb < 1.381845 (mar22 baseline)
**Code Change**: `self.lm_head.weight = self.transformer.wte.weight` in __init__; lm_head removed from optimizer (tied weight updated through embedding group at EMBEDDING_LR=0.7)

---
**Result**: CRASH (loss > 100 on step 1)
**Git Hash**: b1475c7
**Verdict**: DISCARD — Fundamental LR conflict. lm_head was tuned at UNEMBEDDING_LR=0.004 (dmodel_scaled ≈0.007). With weight tying, the shared weight inherits EMBEDDING_LR=0.7 (scaled ≈1.21) — ~170× larger. The combined gradient (sum of input-side and output-side gradients) applied at 1.21 causes immediate loss explosion. Weight tying requires matching LRs; our architecture has a hard constraint that output and input embeddings need very different learning dynamics. Permanently abandoned.
