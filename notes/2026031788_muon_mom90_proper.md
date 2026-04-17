# 2026031788_muon_mom90_proper

**Hypothesis**: Discovered bug in Exp86 — `get_muon_momentum()` hardcodes 0.80 and overrides `group["momentum"]` each step, making Exp86's MUON_MOMENTUM param change a near-no-op (only affected step 0). Now fixing the wire: get_muon_momentum returns MUON_MOMENTUM. Baseline is momentum=0.80. Previously tried 0.75 (Exp40, discard) and 0.85 (Exp24, discard) at earlier eras. Now at optimum 1.369316 with lower MATRIX_LR=0.080, trying 0.90 properly. Higher momentum + lower LR = larger effective update. Also reverting ROPE_BASE=1000 disaster (Exp87 was +0.013).
**Target Metric**: val_bpb < 1.369316
**Code Change**: get_muon_momentum returns MUON_MOMENTUM=0.90 (was hardcoded 0.80). ROPE_BASE=10000 (restored). Exp87/Exp86 bugs documented.

---
**Result**: val_bpb=1.374034
**Git Hash**: 7c1e5ad
**Verdict**: DISCARD. Much worse (+0.004718). Muon momentum axis at current optimum: 0.75 worse (Exp40), 0.80 BEST, 0.85 worse (Exp24), 0.90 much worse. 0.80 is confirmed optimal, don't try again.
