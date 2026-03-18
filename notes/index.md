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
| [2026031753_window_64th](2026031753_window_64th.md) | 6c71eb6 | 1.374682 | discard | SHORT_WINDOW_FRAC 32→64 (S=32 too small, 64 optimal) |
| [2026031754_matrixlr_retune](2026031754_matrixlr_retune.md) | 97c5209 | 1.374063 | discard | MATRIX_LR 0.095→0.10 (0.095 robust at S=64) |
| **[insight_06_exp45to54](insight_06_exp45to54.md)** | — | — | insight | Exp45-54: S=64 window is the biggest lever (Δ-0.004 total) |
| [2026031755_scalarlr_retune](2026031755_scalarlr_retune.md) | 43c172c | 1.373208 | discard | SCALAR_LR 0.7→0.8 (0.7 robust, no S=64 interaction) |
| [2026031756_depth4_ar48](2026031756_depth4_ar48.md) | 465ed41 | 1.384081 | discard | DEPTH=4 AR=48 (still too expensive vs DEPTH=3) |
| [2026031757_mlp4x_s64](2026031757_mlp4x_s64.md) | 179ddd4 | 1.373305 | discard | MLP 3x→4x at S=64 (3x still optimal, arch locked) |
| [2026031758_finallr12](2026031758_finallr12.md) | 10a3dad | 1.372820 | discard | FINAL_LR_FRAC 0.08→0.12 (overshoots, 0.08 optimal) |
| [2026031759_warmdown45](2026031759_warmdown45.md) | 2cfd433 | 1.372749 | discard | WARMDOWN_RATIO 0.50→0.45 (shorter warmdown, 0.50 optimal at S=64) |
| [2026031760_warmdown55](2026031760_warmdown55.md) | d20b7f8 | 1.371455 | keep | WARMDOWN_RATIO 0.50→0.55 ← NEW BEST |
| [2026031761_warmdown60](2026031761_warmdown60.md) | 3c283aa | 1.371320 | keep | WARMDOWN_RATIO 0.55→0.60 ← NEW BEST |
| [2026031762_warmdown65](2026031762_warmdown65.md) | ee42c4f | 1.371208 | keep | WARMDOWN_RATIO 0.60→0.65 ← NEW BEST |
| [2026031763_warmdown70](2026031763_warmdown70.md) | 4741a6f | 1.371448 | discard | WARMDOWN_RATIO 0.65→0.70 (inflection, 0.65 optimal) |
| **[insight_07_exp58to63](insight_07_exp58to63.md)** | — | — | insight | Exp58-63: WARMDOWN_RATIO=0.65 optimal (Δ-0.00055 total) |
| [2026031764_wd012](2026031764_wd012.md) | 8b156a5 | 1.371714 | discard | WEIGHT_DECAY 0.15→0.12 (too low, 0.15 robust) |
| [2026031765_wd018](2026031765_wd018.md) | 2944d4a | 1.372381 | discard | WEIGHT_DECAY 0.15→0.18 (too high, 0.15 confirmed optimal) |
| [2026031766_finallr06](2026031766_finallr06.md) | bd20a8f | 1.371321 | discard | FINAL_LR_FRAC 0.08→0.06 (0.08 optimal at WARMDOWN=0.65 too) |
| [2026031767_beta170](2026031767_beta170.md) | 9b34506 | 1.371243 | discard | ADAM beta1 0.75→0.70 (marginal, 0.75 optimal) |
| [2026031768_matrixlr090](2026031768_matrixlr090.md) | 850c314 | 1.370933 | keep | MATRIX_LR 0.095→0.090 ← NEW BEST |
| [2026031769_matrixlr085](2026031769_matrixlr085.md) | eb4d05a | 1.370791 | keep | MATRIX_LR 0.090→0.085 ← NEW BEST |
| [2026031770_matrixlr080](2026031770_matrixlr080.md) | 428f3a3 | 1.369486 | keep | MATRIX_LR 0.085→0.080 ← NEW BEST (Δ-0.0013!) |
| [2026031771_matrixlr075](2026031771_matrixlr075.md) | c5e9961 | 1.369538 | discard | MATRIX_LR 0.080→0.075 (0.080 confirmed optimal) |
| **[insight_08_exp64to71](insight_08_exp64to71.md)** | — | — | insight | Exp64-71: MATRIX_LR=0.080 new best (Δ-0.00172 at WARMDOWN=0.65) |
| [2026031772_emblr06](2026031772_emblr06.md) | f0e6efe | 1.370290 | discard | EMBEDDING_LR 0.7→0.6 (0.7 robust, no MATRIX_LR interaction) |
| [2026031773_scalarlr06](2026031773_scalarlr06.md) | a4c137c | 1.369900 | discard | SCALAR_LR 0.7→0.6 (0.7 robust, only MATRIX_LR needed recalibration) |
| [2026031774_warmdown70_retest](2026031774_warmdown70_retest.md) | 03254d8 | 1.369773 | discard | WARMDOWN_RATIO 0.65→0.70 retest (0.65 still optimal at new MATRIX_LR) |
| [2026031775_warmdown60_retest](2026031775_warmdown60_retest.md) | f67b8f4 | 1.369316 | keep | WARMDOWN_RATIO 0.65→0.60 retest ← NEW BEST (optimum shifted!) |
| [2026031776_warmdown55_retest](2026031776_warmdown55_retest.md) | 75e8376 | 1.369780 | discard | WARMDOWN_RATIO 0.60→0.55 (0.60 confirmed optimal at MATRIX_LR=0.080) |
| [2026031777_matrixlr075_wd60](2026031777_matrixlr075_wd60.md) | 14f8634 | 1.369366 | discard | MATRIX_LR 0.080→0.075 at WARMDOWN=0.60 (0.080 robust) |
| **[insight_09_exp72to77](insight_09_exp72to77.md)** | — | — | insight | Exp72-77: WARMDOWN×MATRIX_LR co-opt, joint best (0.080, 0.60)=1.369316 |
| [2026031778_unembedlr006](2026031778_unembedlr006.md) | 163e271 | 1.369852 | discard | UNEMBEDDING_LR 0.004→0.006 (0.004 robust at new config) |
| [2026031779_muonbeta2_90](2026031779_muonbeta2_90.md) | 0996160 | 1.369458 | discard | MUON_BETA2 0.95→0.90 (faster adapt worse, 0.95 optimal) |
| [2026031780_muonbeta2_99](2026031780_muonbeta2_99.md) | 5babaad | 1.370398 | discard | MUON_BETA2 0.95→0.99 (0.95 confirmed optimal, symmetric) |
| [2026031781_sll_window](2026031781_sll_window.md) | 422255c | 1.375563 | discard | WINDOW_PATTERN SSL→SLL (both S layers critical at S=64) |
| [2026031782_wd_constant](2026031782_wd_constant.md) | c95fee2 | 1.378674 | discard | WD constant (+0.009) — linear decay-to-zero is critical |
| [2026031783_velr01](2026031783_velr01.md) | 56d7933 | 1.377671 | discard | VE_LR=0.1 much worse (+0.008) — VE needs full EMBEDDING_LR |
| [2026031784_ns_steps5](2026031784_ns_steps5.md) | ae24fb6 | 1.370364 | discard | MUON_NS_STEPS=7→5 worse (+0.001), extra steps < orthogonalization quality |
| [2026031785_ns_steps9](2026031785_ns_steps9.md) | bc0e4f6 | 1.371058 | discard | MUON_NS_STEPS=9 worse (+0.002) — 7 is sweet spot (5→+0.001, 9→+0.002) |
| [2026031786_muon_mom90](2026031786_muon_mom90.md) | 5a26351 | 1.371226 | invalid | INVALID: get_muon_momentum() hardcodes 0.80, overrode param group — test was no-op |
| [2026031787_rope_base1000](2026031787_rope_base1000.md) | af41296 | 1.382689 | discard | RoPE base=1000 catastrophic (+0.013), 10000 well-calibrated for seq_len=2048 |
| [2026031788_muon_mom90_proper](2026031788_muon_mom90_proper.md) | 7c1e5ad | 1.374034 | discard | Muon momentum 0.80→0.90 much worse (+0.005), 0.80 confirmed optimal |
| [2026031789_cosine_warmdown](2026031789_cosine_warmdown.md) | 3b02172 | 1.373255 | discard | Cosine warmdown worse (+0.004), linear schedule confirmed better |
| [2026031790_wd_sqrt_decay](2026031790_wd_sqrt_decay.md) | 0ca90a0 | 1.372756 | discard | WD sqrt decay worse (+0.003), confirms linear WD is optimal |
| [2026031791_gelu](2026031791_gelu.md) | ea74421 | 1.375996 | discard | GELU worse (+0.007), activation rank: ReLU²>GELU>ReLU |
| [2026031792_ve_gate_full](2026031792_ve_gate_full.md) | 9f6f262 | 1.376281 | discard | VE gate 64→256 worse (+0.007), narrow gate is better |
| [2026031793_parallel_blocks](2026031793_parallel_blocks.md) | TBD | TBD | TBD | Parallel attn+MLP blocks (PaLM style, same residual add) |
