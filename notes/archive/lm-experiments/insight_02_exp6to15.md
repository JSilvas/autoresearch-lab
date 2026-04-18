# Insight Note 02 — Experiments 6–17

## Summary

Starting best: **1.393200** (Exp1, alternating VE).
Best after Exp6–17: **1.380054** (Exp15, DEPTH=3 + MLP 3x).

## The Big Discovery: Step-Starvation

The dominant theme of this cycle is **step-starvation**. The model trains for a fixed 5-minute wall-clock budget. Any change that increases compute per step reduces the number of optimizer steps, hurting convergence. Conversely, reducing compute per step dramatically helps.

Evidence chain:
- MLP 6x (Exp12): 1.398630 — worse (fewer steps)
- MLP 4x (baseline): 1.393200
- MLP 3x (Exp13): 1.387965 — better (+0.005)
- MLP 2x (Exp14): 1.396342 — worse (too narrow)
- DEPTH=5 (Exp5): 1.509948 — much worse
- DEPTH=4 baseline: 1.393200
- DEPTH=3 + 3x MLP (Exp15): **1.380054** — massive win (+0.014)
- DEPTH=2 (Exp16): 1.444568 — too shallow

**Key principle**: 3 layers + 3x MLP ≈ 500 steps vs 4 layers + 4x MLP ≈ 333 steps. The ~50% more steps is worth more than the lost depth/capacity.

## Secondary Findings
- WEIGHT_DECAY=0.15 (Exp7): confirmed better than 0.20 or 0.10
- WARMDOWN_RATIO=0.50: confirmed (0.45, 0.55 both worse)
- FINAL_LR_FRAC=0.08: confirmed (0.04 worse)
- HEAD_DIM=128 (2 heads): confirmed (64-head worse)
- SwiGLU, MQA, warmup: all hurt at this scale

## Current Architecture (DEPTH=3 + MLP 3x)
- DEPTH=3, dim=256 (2 heads, HEAD_DIM=128)
- MLP: 3x = 768 hidden, ReLU²
- VE on layers 0,2 (alternating, 64-channel gate)
- x0 skip, resid_lambdas, RoPE base=10000, QK-norm
- WD=0.15, MATRIX_LR=0.09, EMBEDDING_LR=0.6, WARMDOWN=0.50

## Next Direction
Tune hyperparameters specifically for DEPTH=3+3x. LR tuning, WD, VE configuration. Also explore wider dim at fewer layers.
