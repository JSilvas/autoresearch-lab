# 2026031793_parallel_blocks

**Hypothesis**: Current blocks are sequential: x = x + attn(norm(x)); x = x + mlp(norm(x)). Parallel blocks (PaLM/GPT-J style): x = x + attn(norm(x)) + mlp(norm(x)). Both attn and MLP process the same pre-norm input, gradient flows more directly through both paths, and the attn doesn't need to "fix up" for the MLP to see. For small models, parallel blocks can be equally or more effective while having the same parameter count. Changes gradient flow and loss landscape.
**Target Metric**: val_bpb < 1.369316
**Code Change**: Block.forward: sequential attn+mlp → parallel (both on norm(x), single residual add). VE gate channels reverted to 64.

---
**Result**: val_bpb=1.387348
**Git Hash**: 83ba44f
**Verdict**: DISCARD. Much worse (+0.018032). Parallel blocks failed badly — high training loss (~3.89-3.93 vs baseline ~3.84-3.87) throughout, and clear degradation on val_bpb. The sequential residual path is critical: attn must "fix up" the representation before MLP sees it. Parallel form removes this information flow.
