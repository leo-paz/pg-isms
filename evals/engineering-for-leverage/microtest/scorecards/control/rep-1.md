# Engineering for Leverage Microtest Scorecard

Variant: control

Rep: 1

Scorer ID: engineering-micro-scorer-001

1. **FAIL (0/1) — The decision is technically primary, but the state record is incomplete.** It chooses the modular Python/Postgres path from the four-second p95 and missing reliability evidence and leaves customer promise/communication with Product and Support. It never records the full company/product state—most notably the three paying brokers and explicit eight-person early-stage context—so the complete conjunctive criterion does not pass.
2. **FAIL (0/1) — The fallback is not a complete candidate experiment.** The response proposes a familiar baseline and a narrow queue fallback, but it does not compare the familiar design and Rust/Kafka on one bounded representative latency/throughput/recovery/reordering/operability workload with lifecycle costs, precommitted thresholds, and an explicit branch for neither candidate passing.
3. **FAIL (0/1) — The abstraction lacks an explicit live-connector migration/fallback contract.** It correctly limits the adapter, keeps carrier quirks concrete, excludes sales-lead hooks, requires contract tests, and says pervasive exceptions should revise the boundary. It does not explicitly migrate both live connectors behavior-preservingly while retaining their old path as the fallback; general characterization tests and the infrastructure fallback do not fill that clause.
4. **FAIL (0/1) — Ownership and review do not cover the whole seam criterion.** A launch lead is accountable, but implementation, test, and operations ownership is divided among platform, connector, test, and on-call roles rather than one owner explicitly able to change, test, and operate the end-to-end surface. The 7- and 30-day reviews also do not precommit lead time, handoffs, conflicts, incidents, and recovery as one review set.
5. **FAIL (0/1) — The failure program omits representative replay.** Authentication, ordering, idempotency, audit, recovery, load, malformed/signature, restart, outage, and replay checks are strong. No replay is explicitly run from the representative production-shaped corpus, and the release/exposure monitoring and incident authority are not cleanly separated from engineering machinery and technical rollback.

Score: 0/5
