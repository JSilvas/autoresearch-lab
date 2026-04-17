# 2026032210_muon_momentum_ramp

**Hypothesis**: Muon momentum warm ramp (0.70 → 0.80 over training) may improve optimization stability vs constant 0.80. Similar to the linear weight decay schedule, starting lower allows larger initial steps (less inertia) and increasing momentum later helps converge to a sharper minimum. Untested in mar17 (only constant 0.80, 0.75, 0.85, 0.90, 0.95 tried).
**Target Metval**: val_bpb < 1.381845 (mar22 baseline)
**Code Change**: Replace `get_muon_momentum` to return `0.70 + 0.10 * progress` (clamped to [0.70, 0.80]).

---
