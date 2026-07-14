# Baseline scorecard

Case ID: scenario-04

Reviewer ID: engineering-baseline-001

Independent scorer: engineering-baseline-scorer-001

Cases SHA-256: 8b57b50bc78649fac772fb3231373cc04b73926db43bd5f26bfae7701078979a

## Score

Score: 0/5

1. **0/1 — Shared invariants are not diagnosed:** It identifies overlapping ownership, layer-based responsibility, file contention, and coordination symptoms before rejecting microservices, but does not identify the shared business or data invariants causing the coupling.
2. **0/1 — Seam mapping is incomplete:** It sketches outcome seams and assigns responsible teams, but does not map data seams and change frequency before choosing boundaries or explicitly require each owner to understand, test, operate, and change its full surface.
3. **0/1 — Governance is incomplete:** It supplies interfaces, tests, data ownership, on-call routing, and incident responsibility, but no explicit invariant set or decision log.
4. **0/1 — Product-delivery preservation is unstated:** It rejects the full rewrite and later proposes one-capability extraction with a strangler interface and rollback, but never commits the initial boundary or ownership change to preserving ongoing product delivery.
5. **0/1 — Review contract is incomplete:** It proposes observation over several release cycles and measures contention, cross-team changes, incident handoffs, deploy coupling, scaling, and reliability, but gives no review date, lead-time or recovery measure, or explicit keep, redraw, or further-separate decision branch.
