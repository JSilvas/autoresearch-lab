# 2026031796_attn_temp_half

**Hypothesis**: Exp95 showed 2× attention scale (sharper) is worse (+0.011). Testing 0.5× (softer) to bracket the optimum. Softer attention (logits ~5.65×cos(θ) vs default ~11.3×cos(θ)) makes the attention distribution more diffuse — each of the 64 window tokens contributes more equally. With a short S=64 window, all nearby tokens may be relevant for character-level/word-level patterns. Softer attention could allow the model to blend more context rather than laser-focusing on just 1-2 tokens.
**Target Metric**: val_bpb < 1.369316
**Code Change**: ATTN_TEMP_SCALE: 2.0 → 0.5.

---
**Result**: val_bpb=1.415616
**Git Hash**: (previous commit)
**Verdict**: DISCARD. Much worse (+0.046300). Softer attention (0.5×) is far more damaging than sharper (2.0×, +0.011). Attention temperature axis fully bracketed: 0.5×(+0.046) < 1.0×(best) < 2.0×(+0.011). Default scale 1/√d is unambiguously optimal. Selective attention matters; diffuse attention hurts badly.
