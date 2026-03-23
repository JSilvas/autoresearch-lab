# 202603229_gated_attnres

**Hypothesis**: AttnRes Exp3 failed because zero-init query produced uniform mixing (far from optimal resid_lambdas=1.0, x0_lambdas=0.1 baseline). Gated version: keep resid_lambdas/x0_lambdas AS the baseline path, ADD a per-layer scalar gate (init=0) that gates an AttnRes correction: x = x_base + gate[i] * (x_attn - x_base). gate=0 → exactly baseline (no risk from init). Model can learn gate>0 if cross-layer attention helps. gradient to gate is (x_attn - x_base) · dL/dx — nonzero when AttnRes provides different signal. This is the safest AttnRes test.
**Target Metric**: val_bpb < 1.381845
**Code Change**: Add self.attn_res_queries [n_layer, n_embd] (zero init), self.attn_res_gate [n_layer] scalar (zero init). Forward: keep baseline mixing, compute x_attn, blend: x = x_base + gate * (x_attn - x_base). Add both to optimizer at SCALAR_LR.

---
**Result**: 1.450376 (387 steps; Δ+0.068 vs baseline)
**Git Hash**: 354d5b1
**Verdict**: DISCARD — Gated AttnRes with zero gate and small learned corrections did not help; worse than baseline. The model apparently does not benefit from adding a content-dependent cross-layer term to the residual stream at this scale and time budget. This confirms that the baseline's fixed resid/x0 scalars are already near-optimal for depth=3 with the given window pattern and learning rates.
