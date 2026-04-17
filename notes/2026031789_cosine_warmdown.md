# 2026031789_cosine_warmdown

**Hypothesis**: Current LR warmdown is linear (cooldown * 1.0 + (1-cooldown) * FINAL_LR_FRAC). Cosine warmdown is used in many SOTA recipes (GPT-4, etc.) — it decays more slowly at the start (preserving peak LR longer) and more steeply toward the end, reaching the same FINAL_LR_FRAC. With WARMDOWN_RATIO=0.60 (60% of training in decay), the shape of the decay matters a lot. Try: cosine_scale = 0.5*(1+cos(π*(1-cooldown))), LR = cosine_scale*(1-FINAL_LR_FRAC) + FINAL_LR_FRAC.
**Target Metric**: val_bpb < 1.369316
**Code Change**: get_lr_multiplier: linear warmdown → cosine warmdown. Also MUON_MOMENTUM reverted to 0.80.

---
**Result**: val_bpb=1.373255
**Git Hash**: 3b02172
**Verdict**: DISCARD. Worse (+0.003939). Cosine schedule decays LR faster in early warmdown, hurting convergence. Linear warmdown is confirmed better — the gradual linear decay matches the training dynamics better.
