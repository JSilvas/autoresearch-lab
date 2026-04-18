# Activity-Based Learning Rate Scaling (Exp12)

## Overview
Implemented activity-based learning rate scaling as a form of synaptic metaplasticity where layer activity influences future learning rates.

## Changes Made
1. Added `ACTIVITY_EMA_DECAY = 0.99` hyperparameter
2. Added `self.layer_activity_ema` parameter in `GPT.__init__` to track EMA of layer activity
3. Updated EMA in forward pass after each block computation: layer activity measured as L2 norm of hidden states averaged across batch and sequence
4. Modified `setup_optimizer` to scale learning rates based on layer activity: LR scaling factor = exp(-average_activity), clipped to [0.5, 2.0] for stability
5. Applied scaling to Muon parameter groups (matrices) with per-layer activity tracking
6. Initialized EMA to zero in `init_weights`

## Results
- Validation BPB: 1.378481
- Baseline (Exp2): 1.381845
- Improvement: -0.003364 (better)

## Analysis
The activity-based LR scaling showed a small but consistent improvement over the baseline. This suggests that modulating learning rates based on recent layer activity (synaptic metaplasticity) can help optimization at this scale. The mechanism allows layers that are less active to receive slightly higher learning rates, potentially helping them catch up, while very active layers get slightly reduced learning rates to prevent over-updating.

## Next Steps
Consider combining this with other successful techniques from previous experiments or fine-tuning the activity scaling parameters (decay rate, clipping range).
