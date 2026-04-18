# 202603222_baseline_rope

**Hypothesis**: Establish mar22 session baseline with best-known RoPE config from mar17. Config: DEPTH=3, AR=64 (model_dim=256), SSL multi-scale windows S=32+S=128+L, MATRIX_LR=0.080, WARMDOWN=0.60, all other HPs from mar17 final state.
**Target Metric**: Establish baseline — mar17 best was 1.368062 (some MPS run-to-run variance expected)
**Code Change**: USE_ALIBI=False (restoring RoPE after Exp1 discard)

---
**Result**: 1.381845 (376 steps; mar17 best was 1.368062 — Δ+0.014 gap likely due to MPS non-determinism)
**Git Hash**: edb3cd2
**Verdict**: KEEP as session baseline. The ~0.014 gap from mar17 is within expected MPS variance. Session baseline = 1.381845; will try to beat this and ideally break below 1.368062.
