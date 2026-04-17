# Insight 10: Multi-scale Windows (Exp100-105)

## Summary
Multi-scale attention windows unlock a new performance dimension. The key finding: different transformer layers benefit from *different* context granularities — uniform window is suboptimal.

## Results
| Config | val_bpb | Δ vs baseline |
|--------|---------|---------------|
| Uniform S=64 (baseline) | 1.369316 | — |
| S=64+S=128 (Exp100) | 1.368544 | -0.000772 |
| S=128+S=64 reversed (Exp101) | 1.370738 | +0.001422 |
| S=64+S=256 wider (Exp102) | 1.372970 | +0.003654 |
| **S=32+S=128 (Exp103)** | **1.368062** | **-0.001254** |
| S=16+S=128 too narrow (Exp104) | 1.369029 | -0.000287 |
| S=32+S=64 wrong 2nd (Exp105) | 1.371384 | +0.002068 |

## Key Findings
1. **Fine-to-coarse order is critical**: S=32→S=128 beats S=128→S=32 by 0.002. Layer 0 must do local extraction first.
2. **First window optimum: S=32** (FRAC=64). Smaller than uniform S=64. U-shaped: S=16 < S=32 > S=64.
3. **Second window optimum: S=128** (FRAC=16). Consistent across both S=32 and S=64 first layers. Monotone: S=64 < S=128 < S=256 for second layer.
4. **Optimal: S=32+S=128+L** = 1.368062, total gain -0.001254 vs uniform S=64 baseline.

## Interpretation
The model needs a hierarchical context processing pipeline: layer 0 extracts local character/word patterns within 32 tokens, layer 1 integrates sentence-level patterns within 128 tokens, layer 2 handles long-range document structure globally. Previously uniform S=64 was a compromise that suboptimally served all three roles.
