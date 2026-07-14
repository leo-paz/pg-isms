# Baseline scorecard

Case ID: scenario-05

Reviewer ID: engineering-baseline-001

Independent scorer: engineering-baseline-scorer-001

Cases SHA-256: 8b57b50bc78649fac772fb3231373cc04b73926db43bd5f26bfae7701078979a

## Score

Score: 0/5

1. **0/1 — Primary workflow and invariant-first order are absent:** The response covers signature trust, ordering, idempotency, durable records, and recovery, but never makes `engineering-for-leverage` primary or states trust-boundary, authorization, ordering, idempotency, audit, and recovery invariants before selecting components.
2. **0/1 — Failure controls are incomplete:** It models adversarial and ordinary failures, validates input, bounds live transfers, and provides replay and reconciliation, but does not explicitly minimize processing privilege or require deterministic replay.
3. **0/1 — Test contract lacks precommitment:** It assigns end-to-end incident ownership and exercises a broad fault matrix and shadow replay, but does not choose the simplest design, explicitly use simulation and fault injection, or precommit a dated or quantitative pass-versus-redesign threshold.
4. **0/1 — Required reviews are incomplete:** It uses security review and shadow traffic before bounded exposure, but never requires current privacy and legal or compliance review before live payroll movement.
5. **0/1 — Workflow composition is incomplete:** It names technical and release owners plus monitoring, kill-switch, rollback, and incident mechanisms, but does not assign machinery and technical rollback to `engineering-for-leverage`, does not assign exposure to `shipping-and-iterating-products`, and omits explicit support and restitution ownership.
