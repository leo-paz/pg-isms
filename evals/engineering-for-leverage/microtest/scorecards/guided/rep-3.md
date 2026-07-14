# Engineering for Leverage Microtest Scorecard

Variant: guided

Rep: 3

Scorer ID: engineering-micro-scorer-001

1. **PASS (1/1) — The decision record and later release ownership are explicit.** Facts, assumptions, stage, measured constraint, and evidence latency are recorded; the ingestion DRI owns the binding internal surface while the release owner owns customer exposure, coordination, monitoring window, pause, and exposure rollback.
2. **FAIL (0/1) — The alternative-failure branch is not stated.** Familiar, Kafka/queue, and Rust receive lifecycle comparisons and the bounded 40x/burst suite covers all five workload dimensions with thresholds, a Day-10 decision, a transport seam, and current security/customer checks. The response says to evaluate an alternative after bounded tuning fails but never explicitly says what decision follows if that alternative also fails.
3. **FAIL (0/1) — Behavior-preserving live-connector migration is not required.** The adapter is narrow, provider specifics and leads stay concrete, all adapters get a conformance suite, the previous compatible path is retained, and retreat triggers are explicit. But the plan never says to migrate the two live connectors through characterization/shadow equivalence without changing behavior; conformance alone and a fallback path do not satisfy that migration clause.
4. **PASS (1/1) — The mapped boundary, owner, and reviews meet the full criterion.** It maps the shared data/invariant seam and change-frequency triggers, assigns an ingestion DRI who can change, test, deploy, operate, and roll back the end-to-end surface, preserves delivery with the smallest reversible path, and uses Day 10/14-days-post-launch reviews covering lead time, handoffs, conflicts, incidents, drain/recovery time, and operator cost.
5. **PASS (1/1) — Validation and release responsibility are fully separated.** The response defines authorization, ordering, idempotency, audit, and recovery; uses representative workload simulation, explicit interruption/failover fault injection, and signed-sample replay with numeric pass/redesign gates; and separates the engineering DRI/technical fallback from release exposure, monitoring, Support, exposure rollback, and incident coordination.

Score: 3/5
