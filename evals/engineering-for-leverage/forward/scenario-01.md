# Raw evaluation output

Case ID: scenario-01

Reviewer ID: engineering-forward-001

## Decision

Keep TypeScript and Postgres as the default foundation for now, and put the real-time transport behind a narrow replaceable boundary. Do not adopt the actor runtime on the strength of architectural fit alone. The product target is real, but neither option has yet been demonstrated at 50,000 connections: the familiar prototype is under-tested, while the actor option carries unmeasured proficiency, operations, ecosystem, hiring, and exit costs.

This is an early, reversible software decision with short evidence latency. The binding constraint is scale uncertainty, not current proof that the familiar stack is incapable. I assume no acute survival constraint and that a two-week technical trial is affordable; if either assumption is false, record it and choose the smallest path that preserves delivery.

## Bounded comparison

The technical owner should date this decision 2026-07-14 and run one production-shaped comparison by 2026-07-28:

- Harden the TypeScript prototype into a capable familiar baseline rather than benchmarking a toy. Keep Postgres as the durable system of record and isolate connection/fanout mechanics behind a small interface.
- Build only enough of the actor candidate to exercise that same interface. Do not port the product or create a general framework.
- Replay the same representative workload: 50,000 persistent connections, the expected distribution of room sizes, realistic message sizes and fanout, connection churn, slow clients, and a reconnect surge. Sustain the run long enough to expose leaks and degradation rather than reporting a brief peak.
- Define “sub-100 ms” before the run as an end-to-end percentile and measurement point; use p99 unless the product requirement specifies otherwise. Also precommit limits for accepted-message loss or duplication, recovery after a killed instance, deployment time, and monthly infrastructure cost at the target and at the next plausible scale.
- Fault-inject node loss, dependency latency, reconnect storms, and a deploy. Require a founder to diagnose the failure from normal logs, metrics, and traces and restore service from a runbook. Record the time and any specialist knowledge needed.

The record must compare more than throughput: implementation and debugging time, concepts and moving parts, managed-service maturity, library interoperability, observability, security patching, deployment, local development, on-call recovery, hiring and training, procurement, maintenance, migration, and vendor lock-in. For the actor candidate, preserve an exit seam at the transport boundary and verify how durable state can be exported or replayed.

## Precommitted branches

- If the familiar baseline meets the 50,000-connection and p99 fanout target with agreed recovery and cost headroom, keep it. When both candidates are capable, familiarity and ecosystem strength are net leverage.
- Switch the transport component—not the whole product—to the actor runtime only if the familiar baseline misses a binding threshold after one bounded, ordinary optimization and the actor candidate passes it with a material margin, while its operational drill and lifecycle-cost estimate remain acceptable. The decision record must name the specific capability or reduction in delivery/operating cost that pays for the new runtime.
- If the actor runtime wins only a synthetic peak but requires opaque operations, scarce expertise, or a costly migration, reject it.
- If neither candidate passes, do not disguise that result as a technology preference. Revisit the connection topology, workload assumptions, or product SLO and test the next smallest candidate.

The founder responsible for real-time infrastructure owns the trial, the runbook, and the recommendation. Preserve both the benchmark harness and the transport seam. Review again at 10,000 real connections, at the first material SLO breach, or on 2026-10-14, whichever comes first, using production fanout, incident, recovery, and cost data rather than the original benchmark alone.
