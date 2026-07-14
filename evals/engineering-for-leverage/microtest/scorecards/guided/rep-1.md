# Engineering for Leverage Microtest Scorecard

Variant: guided

Rep: 1

Scorer ID: engineering-micro-scorer-001

1. **PASS (1/1) — The responsibility boundary and state record are explicit.** The decision records team/customer/connector/lead state, stable history, four-second versus two-second evidence, and assumptions; engineering owns the internal structure while the release owner owns later exposure, monitoring, Support coordination, rollback gates, and incident response.
2. **FAIL (0/1) — The neither-candidate-passes branch is absent.** Familiar Python/Postgres, Kafka, and Rust have lifecycle comparisons; the 60-minute 40x/15-minute 60x workload covers all five dimensions with thresholds, a Day-10 decision, a transport seam, and current security/procurement checks. If the baseline fails, however, the response authorizes one targeted alternative but never explicitly states the architecture/release decision if that alternative also fails latency or operability; generic rollout stops do not supply that candidate branch.
3. **PASS (1/1) — The abstraction contract is complete.** Only stable lifecycle invariants are shared; carrier quirks and leads stay concrete; conformance tests are extensive; live connectors migrate one at a time in shadow comparison with their old path retained; and explicit lead-time/call-site/coordination/incident triggers cause retreat.
4. **PASS (1/1) — One DRI owns the mapped surface with a measured review.** The plan maps data and invariant seams, uses observed stability/change cost, assigns an end-to-end ingestion DRI and backup, makes the smallest flag-reversible change, protects the launch, and reviews on Day 30/Day 45 using lead time, edits/handoffs, conflicts, incidents, and recovery.
5. **PASS (1/1) — Invariants, destructive evidence, and release ownership are operational.** Authorization, ordering, idempotency, audit, and recovery are defined; a last-30-days corpus plus third-carrier fixtures drives simulation, fault injection, and replay against numeric pass/redesign gates; engineering owns machinery/technical rollback and the release owner owns exposure, monitoring, Support, rollback gates, and incident response.

Score: 4/5
