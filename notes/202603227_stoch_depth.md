# 202603227_stoch_depth

**Hypothesis**: Stochastic depth (layer drop) regularizes the 3-layer model by randomly skipping entire block computations during training (with probability p=0.10). Each step, the model trains a different depth-2 or depth-3 sub-network, creating an implicit ensemble. At eval, all 3 layers active. Can help generalization when model capacity > data complexity. With depth=3, skipping one layer 10% of the time means 10% of gradient updates are computed on a 2-layer network.
**Target Metric**: val_bpb < 1.381845
**Code Change**: Add STOCHASTIC_DEPTH_RATE=0.10 hyperparameter. In GPT.forward: each block (non-last) has 10% chance of being skipped (output = mixed input, no attn/mlp). Block is never skipped at eval. VE lookup moved inside non-skip branch.

---
