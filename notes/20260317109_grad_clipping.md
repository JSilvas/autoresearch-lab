# 20260317109_grad_clipping

**Hypothesis**: No gradient clipping has ever been used. Adding clip_grad_norm_=1.0 may stabilize training, especially during warmdown when LR is decaying and gradients could spike.
**Target Metric**: val_bpb < 1.368062
**Code Change**: `torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)` added before `optimizer.step()`.

---
**Result**: 1.378656 (Δ+0.011 vs best 1.368062)
**Git Hash**: db562b5
**Verdict**: DISCARD — MuonAdamW already normalizes gradients. Muon orthogonalizes (unit-norm updates), Adam divides by running mean squared gradient. External clip_grad_norm_ is redundant and interferes with both. Never add gradient clipping with this optimizer stack.
