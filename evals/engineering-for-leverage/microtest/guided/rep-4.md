# 30-day decision: prove and harden the monolith

## Decision

For the next 30 days, keep Python, Postgres, and one deployable monolith. Build the third carrier as a thin adapter to a shared ingestion kernel, and fix the measured bottleneck only after a representative baseline identifies it. Do not start the Rust rewrite, Kafka migration, per-connector microservices, or a universal plugin framework.

This preserves the six-week carrier date and the two existing connectors while testing the actual risk: whether the familiar stack can ingest correctly and recover at projected load. The one four-second p95 result is evidence of a problem, but not evidence that language, broker, or service boundaries caused it.

The choice is reversible. The normalized event envelope and deterministic worker contract form a future transport seam; they do not require a generic queue API or dynamic plugin system now. Keep the current processing path behind a feature flag until the hardened path passes staged exposure.

## Technical decision record

**Facts.** This is an eight-person, early enterprise-integration product with three paying brokers, two connectors that have shared stable semantics for eight months, and one contracted connector due in six weeks. Two further connectors are leads, not evidence. Errors have high operational cost: loss, duplicate effects, reordering, or an incomplete audit trail can corrupt customer workflows. Internal changes are reversible; customer exposure is not equally cheap. The current team is proficient in Python/Postgres. The binding constraint is a correct, supportable launch that meets the two-second p95 contract at 40x projected volume.

**Assumptions to close by July 15.** No acute default-dead condition was supplied; the CTO confirms runway before architecture work. If survival is binding, scope narrows further to the signed connector and contractual reliability. Product and Support define exactly when the ingestion-delay clock starts and stops. Engineering records the real 30-day peak, event-size distribution, carrier mix, burst shape, ordering keys, retry rules, and each carrier's authoritative event identifier/sequence. Security confirms payload retention and redaction rules. These are decision inputs, not reasons to delay the first baseline.

| Candidate | Limitation it could remove | Lifecycle judgment |
|---|---|---|
| Profile and harden Python/Postgres | Slow queries, lock contention, insufficient worker concurrency, connection pressure, or missing batching/indexes | First choice: existing proficiency, deployment, debugging, libraries, observability, hiring pool, and one security/backup surface; smallest migration and exit cost |
| Postgres durable inbox plus partitioned workers | Request-coupled processing, unsafe retries, and uncontrolled concurrency | Adopt if not already present; familiar operations and transactional audit/idempotency outweigh an additional platform |
| Managed Kafka | A demonstrated Postgres transport ceiling or need for independently retained, partitioned replay | Deferred: adds procurement, IAM, monitoring, incident modes, dual-store reconciliation, specialist knowledge, migration, and vendor/exit cost before a transport ceiling is known |
| Rust hot path | A demonstrated CPU-bound parser/validator ceiling | Deferred: no CPU profile exists; a rewrite adds build, debugging, deployment, library, maintenance, and hiring cost without addressing database or queue delay |
| Service per connector / universal plugins | Independently changing, independently operated connector domains | Rejected now: ordering, idempotency, and audit are shared; separate services duplicate those invariants and multiply deploys, calls, handoffs, and incidents. Sales leads do not justify speculative extension points |

The falsifiable leverage claim is that the familiar design can meet the workload gates below, let the third connector reuse invariant code rather than reimplement it, and remain operable by one on-call engineer. If it does not, the measurements identify which narrower option earns its cost.

## Architecture and abstraction boundary

Use one deployable with three explicit in-process boundaries:

1. **Carrier adapter.** Authenticate the webhook and map the carrier payload to a versioned canonical envelope containing carrier, external event ID, business-object ordering key, carrier sequence when one exists, event type/version, source time, receipt time, payload hash, and trace ID. Carrier-specific acknowledgement and reconciliation calls also live here.
2. **Shared ingestion kernel.** In one short Postgres transaction, persist the immutable receipt and audit transition and enforce a unique idempotency identity such as `(carrier, external_event_id)`. The exact fallback when a carrier lacks a stable ID must be documented per carrier and tested; do not silently guess from timestamps. Claim work in bounded batches with `FOR UPDATE SKIP LOCKED` or the already-proven equivalent, partitioned by the business-object ordering key. Hold or quarantine gaps and ambiguous order rather than applying them out of order. Make state transitions and customer-visible database effects atomic where possible; where an external side effect prevents that, use a transactional outbox and an idempotent delivery key.
3. **Operations path.** Record received, authenticated, deduplicated, waiting-for-gap, processing, applied, quarantined, and failed transitions with actor/version/reason. Provide bounded retry, dead-letter quarantine, reconciliation against the carrier's supported source of truth, and deterministic replay from immutable receipts. Metrics cover receipt-to-durable, receipt-to-applied, queue age/depth, duplicate rate, gap age, retries, quarantines, reconciliation differences, and per-carrier errors.

Extract only this stable vocabulary. The adapter may parse, authenticate, normalize, acknowledge, and reconcile; it may not override idempotency, ordering, audit, retry, or replay rules. A carrier conformance suite runs the same duplicate, out-of-order, gap, malformed-signature, retry, replay, and audit fixtures against all three adapters. There is no runtime plugin loader, connector-owned database, network call between connector and kernel, or connector microservice.

One named ingestion DRI owns the adapters, kernel, schema, conformance tests, dashboards, deployment, on-call runbook, replay tooling, and technical rollback end to end. Connector contributors remain reviewers/implementers, not separate operational owners. A release captain owns customer exposure, rollout monitoring, Support coordination, exposure rollback, and incident command. This is a code and incident boundary, not a team reorganization.

## Precommitted workload and gates

By July 16, freeze a sanitized or synthetic workload derived from the last 30 days: observed carrier mix and payload-size distribution, 40x the observed peak arrival rate for two hours, plus a two-minute 2x burst. Report throughput separately from latency; no offered-load collapse or hidden producer throttling is allowed. If Product has not clarified the contract clock, use receipt at the public endpoint through durable, ordered application as the conservative default.

The same harness must inject duplicates, reversals within an ordering key, sequence gaps, malformed authentication, worker termination, database disconnect/reconnect, and a five-minute loss of half the workers while 40x traffic continues. A 24-hour staging soak follows. The release candidate passes only if:

- contractual ingestion p95 is at most 2.0 seconds at 40x, with an internal target of 1.5 seconds for margin; p99 and maximum are reported, not hidden;
- every acknowledged receipt is accounted for, with zero lost accepted events, zero duplicate customer-visible effects, zero ordering violations within a key, and a complete audit chain;
- after the five-minute worker impairment, backlog drains within 15 minutes while 40x arrivals continue, and restart/replay produces the same final state;
- alerts identify the affected carrier and failure class within two minutes, and an on-call engineer using only the runbook can quarantine, replay, reconcile, and roll back the candidate within 15 minutes; and
- the existing two connectors produce no conformance or shadow-replay regression, security review confirms signature validation, least-privilege database access, payload redaction/retention, and bounded replay permissions, and Support accepts the diagnostic fields and runbook.

Store the workload, seed, configuration, raw results, query plans/profiles, and build SHA. Engineering may correct an unrealistic workload with Product and Support, but may not relax a threshold after seeing a failing candidate without recording a new decision and contract consequence.

## 30-day execution and decision branches

**July 14-16 (days 1-3): contract and instrumentation.** Name the ingestion DRI and release captain. Close the assumptions above, draw the existing request/data path, inventory shared invariants and trust boundaries, add end-to-end timestamps and queue/database metrics, and freeze the workload and gates. Support's customer dates remain unchanged.

**July 17-21 (days 4-8): failing baseline and diagnosis.** Run latency, throughput, duplicate/reordering, interruption, recovery, replay, and operator drills on the unchanged system. Profile Python CPU, database waits/locks, query plans, connections, queue age, serialization, and downstream calls. Publish the baseline even if it reproduces only the known four-second p95.

**July 22 (day 9): choose the narrow fix.** If time is in queries/locks, fix indexes, query shape, transaction scope, contention, or batching. If it is worker capacity, add bounded concurrency and ordering-key partitioning. If request coupling is the problem, add/harden the Postgres inbox. If an external dependency dominates, decouple acknowledgement from processing only if the carrier contract permits it and retain the end-to-end contract metric. Do not combine branches without evidence.

**July 23-30 (days 10-17): implement and preserve behavior.** Land the shared kernel, adapter contract, audit/replay path, and third adapter behind flags. First run conformance against the two live adapters, then compare deterministic shadow replay of sanitized production-shaped receipts before switching any path. Keep schema changes backward compatible and the old path available through the soak.

**July 31-August 4 (days 18-22): destructive verification.** Run the full 40x suite, fault injection, reconciliation, security/privacy review, restore drill, and 24-hour soak. Fix the observed failure; do not substitute an undeployed spike for deployment evidence.

**August 5-8 (days 23-26): release rehearsal.** In the signed carrier's sandbox, run authenticated end-to-end traffic and shadow processing. Rehearse enable, pause, quarantine, replay, reconciliation, and rollback with Engineering, Support, and the release captain. Produce the customer-specific integration checklist and evidence pack.

**August 9-12 (days 27-30): handoff and dated review.** The ingestion DRI signs the technical gates; Security signs the trust-boundary checks; Support signs diagnostics and customer messaging; the release captain alone authorizes staged exposure. Record results, remaining uncertainty, and the six-week launch plan in the TDR. Review on August 12, 2026, and again one week after the third carrier's launch.

## Release handoff and fallback

The third connector remains off by default and is enabled by carrier and broker: sandbox/shadow, internal or test tenant, one consenting broker, then broader rollout. Each stage has a named observer, a minimum observation window agreed with Support, and automatic pause on any threshold breach, audit gap, unexplained reconciliation difference, or sustained queue-age rise. Technical rollback disables the new adapter/worker path without deleting receipts; exposure rollback stops acknowledgements or routes them according to the carrier's documented retry contract. Reconcile every receipt accepted during a rollback before resuming. Existing connectors stay on their proven path until their shadow comparison and gates pass.

This plan does not move the current customer commitment. It removes the speculative rewrite from its critical path and surfaces launch risk on days 9 and 22. A gate failure is escalated immediately rather than concealed by exposing unsafe behavior.

Kafka earns a bounded prototype only if the optimized Postgres design still fails the workload and evidence attributes the ceiling to transport/locking/WAL limits at an agreed operating budget. The prototype must pass the same gates and include dual-write reconciliation, migration, security, on-call, and exit drills. Rust earns an isolated benchmark only if profiling shows parsing/validation consuming more than half of service time and the system still misses capacity after ordinary Python optimization. Per-connector services are reconsidered only after production data shows connectors changing, scaling, or failing independently and reduced lead time outweighs added handoffs and incidents. Otherwise retain the monolith and delete unused abstraction. At each review, compare connector lead time, handoffs, merge conflicts, incidents, recovery time, conceptual surface, and on-call load; redraw or retreat if coordination or operational cost rises.
