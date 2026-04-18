# Insight Note 01 — Experiments 1–5

## Summary

Starting baseline: **1.407007** (master train.py, all-layer VE).
Best after Exp1–5: **1.388859** (Exp7, WEIGHT_DECAY=0.15).

## Key Findings

### What Worked
- **Alternating VE (Exp1)**: Restoring VE to layers 1,3 only improved by 0.013807. All-layer VE is redundant — alternating gives richer per-layer signal.
- **WEIGHT_DECAY=0.15 (Exp7)**: Reduced WD from 0.20 improved by 0.004341. This confirms the decaying WD schedule benefits from a lower peak.

### What Failed (2026 Research Ideas vs Reality)
- **SwiGLU (Exp2)**: +0.006 worse. ReLU² wins at dim=256, 333 steps. SwiGLU benefits don't materialize at this tiny scale/budget.
- **LR Warmup 3% (Exp3)**: +0.051 worse. Catastrophic! With only ~333 steps, warmup wastes too many full-LR steps. WARMUP_RATIO=0.0 is non-negotiable.
- **MQA n_kv_head=1 (Exp4)**: +0.010 worse. With only 2 Q heads, halving KV heads removes too much representational capacity.
- **DEPTH=5 (Exp5)**: +0.117 worse. Extra layer reduces step count by ~20% — model doesn't converge.
- **HEAD_DIM=64 (Exp6)**: +0.099 worse. Smaller heads with more of them is worse at this scale.

## Principles Confirmed
1. This model is step-starved: any change that reduces optimizer steps is very costly.
2. Architectural changes from large-model literature (SwiGLU, MQA, more heads, more depth) all hurt at this tiny scale.
3. The current DEPTH=4, HEAD_DIM=128, ReLU² MLP is near-optimal for the 5-min budget.
4. Hyperparameter tuning (WD, LR schedules) is where gains remain.

## Next Direction
Focus on: WD fine-tuning, WARMDOWN_RATIO, MATRIX_LR, MLP width changes, EMBEDDING_LR.
