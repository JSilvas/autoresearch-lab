# 202603229_gated_attnres

**Hypothesis**: AttnRes Exp3 failed because zero-init query produced uniform mixing (far from optimal resid_lambdas=1.0, x0_lambdas=0.1 baseline). Gated version: keep resid_lambdas/x0_lambdas AS the baseline path, ADD a per-layer scalar gate (init=0) that gates an AttnRes correction: x = x_base + gate[i] * (x_attn - x_base). gate=0 → exactly baseline (no risk from init). Model can learn gate>0 if cross-layer attention helps. gradient to gate is (x_attn - x_base) · dL/dx — nonzero when AttnRes provides different signal. This is the safest AttnRes test.
**Target Metric**: val_bpb < 1.381845
**Code Change**: Add self.attn_res_queries [n_layer, n_embd] (zero init), self.attn_res_gate [n_layer] scalar (zero init). Forward: keep baseline mixing, compute x_attn, blend: x = x_base + gate * (x_attn - x_base). Add both to optimizer at SCALAR_LR.

---
