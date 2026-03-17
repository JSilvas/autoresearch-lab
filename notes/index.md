# Experiment Index — autoresearch/mar17

| Note | Commit | val_bpb | Status | Description |
|------|--------|---------|--------|-------------|
| [202603171_baseline](202603171_baseline.md) | cb0a43f | 1.407007 | keep | baseline |
| [202603172_alternating_ve](202603172_alternating_ve.md) | cfeacbf | 1.393200 | keep | alternating VE layers 1,3 |
| [202603173_swiglu](202603173_swiglu.md) | 6edf0ba | 1.399548 | discard | SwiGLU iso-param MLP |
| [202603174_warmup](202603174_warmup.md) | 3f5636e | 1.443825 | discard | WARMUP_RATIO 0.0→0.03 |
| [202603175_mqa](202603175_mqa.md) | 6e2f68b | 1.402906 | discard | MQA n_kv_head=1 |
| [202603176_depth5](202603176_depth5.md) | 0327fa1 | 1.509948 | discard | DEPTH=5 ASPECT_RATIO=52 |
| [202603177_headdim64](202603177_headdim64.md) | ff0f6a2 | 1.491694 | discard | HEAD_DIM=64 (4 heads) |
| [202603178_wd015](202603178_wd015.md) | 32c2f3d | 1.388859 | keep | WEIGHT_DECAY 0.2→0.15 |
| [202603179_wd010](202603179_wd010.md) | 0a7bbde | 1.392744 | discard | WEIGHT_DECAY 0.15→0.10 |
| **[insight_01_exp1to5](insight_01_exp1to5.md)** | — | — | insight | Exp1-5 summary |
| [2026031710_finallr](2026031710_finallr.md) | 3ad49b8 | 1.389914 | discard | FINAL_LR_FRAC 0.08→0.04 |
| [2026031711_warmdown55](2026031711_warmdown55.md) | 67c52e7 | 1.389621 | discard | WARMDOWN_RATIO 0.50→0.55 |
| [2026031712_warmdown45](2026031712_warmdown45.md) | 0f477c6 | 1.389448 | discard | WARMDOWN_RATIO 0.50→0.45 |
| [2026031713_mlp6x](2026031713_mlp6x.md) | 986a927 | 1.398630 | discard | MLP 4x→6x width |
| [2026031714_mlp3x](2026031714_mlp3x.md) | d17078d | 1.387965 | keep | MLP 4x→3x width |
| [2026031715_mlp2x](2026031715_mlp2x.md) | 1c7cf81 | 1.396342 | discard | MLP 3x→2x width |
| [2026031716_depth3](2026031716_depth3.md) | 57f3251 | 1.380054 | keep | DEPTH=3 MLP 3x ← NEW BEST |
| [2026031717_depth2](2026031717_depth2.md) | 9b23684 | 1.444568 | discard | DEPTH=2 (too shallow) |
| **[insight_02_exp6to15](insight_02_exp6to15.md)** | — | — | insight | Exp6-15: step-starvation discovery |
| [2026031718_depth3_mlp4x](2026031718_depth3_mlp4x.md) | 43a3b31 | 1.383452 | discard | DEPTH=3 MLP 4x |
| [2026031719_depth3_wd020](2026031719_depth3_wd020.md) | b2536e1 | 1.383020 | discard | DEPTH=3 WD 0.15→0.20 |
| [2026031720_ssl_window](2026031720_ssl_window.md) | fbc3b42 | 1.378737 | keep | WINDOW_PATTERN SSL ← NEW BEST |
| [2026031721_halfbatch](2026031721_halfbatch.md) | fc79a75 | 1.387704 | discard | half batch BS=8 |
| [2026031722_matrixlr95](2026031722_matrixlr95.md) | 3742ab2 | 1.377378 | keep | MATRIX_LR 0.09→0.095 ← NEW BEST |
| [2026031723_matrixlr10](2026031723_matrixlr10.md) | 7718042 | 1.379157 | discard | MATRIX_LR 0.095→0.10 |
| [2026031724_momentum85](2026031724_momentum85.md) | a3587c5 | 1.378283 | discard | Muon momentum 0.80→0.85 |
| [2026031725_emblr07](2026031725_emblr07.md) | 4e9d975 | 1.376603 | keep | EMBEDDING_LR 0.6→0.7 ← NEW BEST |
| [2026031726_emblr08](2026031726_emblr08.md) | 80d7ce2 | 1.383802 | discard | EMBEDDING_LR 0.7→0.8 |
| **[insight_03_exp18to25](insight_03_exp18to25.md)** | — | — | insight | Exp18-25 summary |
| [2026031727_beta175](2026031727_beta175.md) | 384900d | 1.376361 | keep | ADAM beta1 0.7→0.75 ← NEW BEST |
| [2026031728_beta180](2026031728_beta180.md) | 4801ba8 | 1.378564 | discard | ADAM beta1 0.75→0.80 |
| [2026031729_sl_window](2026031729_sl_window.md) | bfb0c03 | 1.376968 | discard | WINDOW_PATTERN SL (1 sliding < 2 sliding) |
| [2026031730_depth2_retest](2026031730_depth2_retest.md) | 632fb05 | 1.437080 | discard | DEPTH=2 retest — still too shallow even with optimized params |
| [2026031731_scalarlr03](2026031731_scalarlr03.md) | a0bf157 | 1.381099 | discard | SCALAR_LR 0.5→0.3 (too low, hurts) |
| [2026031732_scalarlr07](2026031732_scalarlr07.md) | ece6e80 | 1.375674 | keep | SCALAR_LR 0.5→0.7 ← NEW BEST |
| [2026031733_scalarlr09](2026031733_scalarlr09.md) | 3340265 | 1.376563 | discard | SCALAR_LR 0.7→0.9 (overshoots, 0.7 optimal) |
| [2026031734_unembedlr008](2026031734_unembedlr008.md) | 8aec15b | 1.379705 | discard | UNEMBEDDING_LR 0.004→0.008 (too high) |
| [2026031735_unembedlr002](2026031735_unembedlr002.md) | 31a876b | 1.389440 | discard | UNEMBEDDING_LR 0.004→0.002 (too low, 0.004 optimal) |
| **[insight_04_exp30to35](insight_04_exp30to35.md)** | — | — | insight | Exp30-35: SCALAR_LR=0.7 new best, DEPTH=2 dead, UNEMBED_LR=0.004 optimal |
| [2026031736_beta2_99](2026031736_beta2_99.md) | b1cd8fa | 1.378974 | discard | ADAM beta2 0.95→0.99 (too slow) |
| [2026031737_beta2_90](2026031737_beta2_90.md) | 37bf0d5 | 1.377939 | discard | ADAM beta2 0.95→0.90 (faster also worse, 0.95 optimal) |
| [2026031738_mlp2x_depth3](2026031738_mlp2x_depth3.md) | a5e79ce | 1.382130 | discard | MLP 3x→2x at DEPTH=3 (capacity loss > step gain) |
| [2026031739_aspect56](2026031739_aspect56.md) | 2358e17 | 1.380076 | discard | ASPECT_RATIO 64→56 (dim 192→168, capacity loss) |
| [2026031740_muonmom75](2026031740_muonmom75.md) | 5b474ca | 1.381605 | discard | Muon momentum 0.80→0.75 (symmetric, 0.80 optimal) |
| [2026031741_lss_window](2026031741_lss_window.md) | d894078 | 1.380756 | discard | WINDOW_PATTERN SSL→LSS (last-layer global attn is key) |
| [2026031742_headdim96](2026031742_headdim96.md) | 1d8ad51 | 1.404089 | discard | HEAD_DIM 128→96 (2 heads much worse, 1 head preferred) |
| [2026031743_no_ve](2026031743_no_ve.md) | 3866f73 | 1.431874 | discard | No VE — catastrophic (+0.056), VE is architecturally critical |
| [2026031744_relu_plain](2026031744_relu_plain.md) | 386ae53 | 1.396303 | discard | ReLU²→ReLU (much worse, ReLU² is critical) |
| **[insight_05_exp36to44](insight_05_exp36to44.md)** | — | — | insight | Exp36-44: all hyperaxes exhausted, architecture confirmed stable |
| [2026031745_ve_lastonly](2026031745_ve_lastonly.md) | 18e1901 | 1.382688 | discard | VE last-layer only (layer 0 VE matters, 2/3 > 1/3) |
| [2026031746_ve_all](2026031746_ve_all.md) | 8dc32b8 | 1.386998 | discard | VE all 3 layers (inverted-U, 2/3 alternating is optimal) |
| [2026031747_emblr075](2026031747_emblr075.md) | 93cfb09 | 1.375955 | discard | EMBEDDING_LR 0.7→0.75 (marginal miss, 0.7 optimal) |
| [2026031748_emblr065](2026031748_emblr065.md) | c814390 | 1.377477 | discard | EMBEDDING_LR 0.75→0.65 (0.7 confirmed optimal) |
| [2026031749_window_quarter](2026031749_window_quarter.md) | ed9372d | 1.373701 | keep | SHORT_WINDOW_FRAC 2→4 (S=512, +16% steps) ← NEW BEST |
| [2026031750_window_eighth](2026031750_window_eighth.md) | 0257683 | 1.372684 | keep | SHORT_WINDOW_FRAC 4→8 (S=256) ← NEW BEST |
| [2026031751_window_16th](2026031751_window_16th.md) | 2304383 | 1.372200 | keep | SHORT_WINDOW_FRAC 8→16 (S=128) ← NEW BEST |
| [2026031752_window_32nd](2026031752_window_32nd.md) | 5bc773a | 1.371759 | keep | SHORT_WINDOW_FRAC 16→32 (S=64) ← NEW BEST |
| [2026031753_window_64th](2026031753_window_64th.md) | TBD | TBD | TBD | SHORT_WINDOW_FRAC 32→64 (S=32, near-causal) |
