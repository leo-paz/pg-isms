# Baseline scorecard

Case ID: scenario-02

Reviewer ID: engineering-baseline-001

Independent scorer: engineering-baseline-scorer-001

Cases SHA-256: 8b57b50bc78649fac772fb3231373cc04b73926db43bd5f26bfae7701078979a

## Score

Score: 2/5

1. **1/1 — Abstracts evidence, not speculation:** It treats the nine-month repeated protocol as a candidate abstraction, rejects the universal framework, and refuses to design for the speculative fourth provider.
2. **1/1 — Extracts only the stable primitive:** It creates a narrow retry, idempotency, and audit protocol while leaving authentication, settlement, provider state, mapping, reconciliation, and unusual failures concrete.
3. **0/1 — The migration contract is incomplete:** It requires conformance tests, but names no accountable owner, no explicit invariant set, and no behavioral-parity gate for migrating the existing connectors.
4. **0/1 — Gates and retreat path are incomplete:** Repeated implementations, stable common behavior, and recurring coordination cost are revisit signals, but simpler call sites and reduced duplication are not gates, and there is no removal or retreat path if the abstraction increases complexity.
5. **0/1 — Revisit is not dated:** It protects current delivery and waits for the third real connector while excluding the fourth, but the revisit is event-based rather than assigned a date after the third connector supplies evidence.
