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
