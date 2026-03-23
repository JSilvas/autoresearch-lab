# 202603224_weight_tying

**Hypothesis**: Weight tying (lm_head.weight = wte.weight) reduces the model by ~2M params (8192×256) and forces input/output embeddings to be coherent. Standard in GPT-2 and most small LMs. With fewer params, the model might train faster (more throughput) and the shared embedding space may improve generalization. The EMBEDDING_LR=0.7 will now serve both roles.
**Target Metric**: val_bpb < 1.381845 (mar22 baseline)
**Code Change**: `self.lm_head.weight = self.transformer.wte.weight` in __init__; lm_head removed from optimizer (tied weight updated through embedding group at EMBEDDING_LR=0.7)

---
