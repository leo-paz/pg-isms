# 30-day decision

Keep the Python/Postgres monolith for the six-week carrier launch. Do not start a Rust rewrite, Kafka adoption, connector microservices, or a universal plugin framework in this window. The single four-second result is evidence of a performance risk, not evidence that the language, database, or deployment shape is the cause. Changing all four would put a small team onto unfamiliar operational ground while consuming the launch margin.

Record this as a 30-day, evidence-contingent decision rather than a permanent ban. First make the ingestion path measurable, reproduce the failure, and test the failure modes that matter. Optimize the demonstrated bottleneck inside the current system. Reconsider a broker only if the tuned Postgres path cannot meet the agreed load, latency, recovery, and operability gates, or if measured requirements emerge for retention, fan-out, or isolation that Postgres cannot reasonably provide. Reconsider service extraction only when a module needs independent scaling or deployment and the team can own another production boundary. Sales leads are not architecture requirements.

The launch scope is the signed carrier plus ingestion reliability. Preserve current customer-visible commitments by cutting speculative platform work, not by weakening release gates.

# Target architecture

Keep one deployable with explicit internal modules:

1. The webhook edge authenticates and minimally validates a request, assigns a correlation ID, and atomically stores the raw event, its carrier/account identity, its idempotency key, and a work record before acknowledging it.
2. Horizontally scalable Python workers claim work in bounded batches from Postgres, using the existing queue mechanism or a simple locked-work-table pattern. Backpressure must be visible, and interactive database work must not be starved by ingestion workers.
3. A carrier adapter performs only carrier-specific verification, parsing, and mapping into a versioned canonical event. Shared code owns ordering, idempotency, retry classification, domain mutation, and audit behavior.
4. A transaction applies the domain effect and records the processing outcome consistently. A unique database constraint enforces idempotency; an application-side check alone is insufficient. Ordering is serialized by the smallest real business stream, such as carrier account plus load, using carrier sequence data where available and explicitly handling stale or unsequenced events.
5. Raw inputs and append-only attempt/outcome records support diagnosis and controlled replay. Permanent failures go to a visible failed-event state; transient failures use bounded exponential retry with jitter. Replay uses the same processing path and cannot bypass idempotency.

Instrument both receipt-to-durable-acceptance and receipt-to-completed-domain-effect. On day 1, confirm which one the two-second contract governs; improving the acknowledgment alone must not disguise a growing processing backlog. Dashboards should show latency percentiles by carrier and stage, arrival and completion rates, backlog age and depth, retry and duplicate rates, ordering conflicts, permanent failures, worker/database saturation, and replay results.

# Abstraction policy

Extract a narrow `CarrierAdapter` boundary from the behavior already proven by the two live connectors. Its contract should cover authentication/verification, parsing, canonical mapping, idempotency-key derivation, ordering metadata, and error classification. It should not expose arbitrary lifecycle hooks, dynamic loading, connector-owned queues, or connector-owned audit logic.

Add the third connector as an in-repository adapter selected from an explicit registry and deployed with the monolith. Give every adapter the same conformance suite: signed fixture verification, schema variants, duplicates, out-of-order delivery, missing sequence data, malformed payloads, retryable and permanent errors, and replay. Allow a capability flag only for a demonstrated carrier difference, with shared defaults. After the third connector has production evidence, review the three implementations for another extraction; do not design for the two unsigned leads.

# Thirty-day execution plan

## Days 1-5: define and measure

- Write a one-page decision record containing the decision, rejected changes, revisit triggers, and owners. Freeze unrelated ingestion refactors for 30 days.
- Define the contract boundary, canonical event, ordering key, duplicate semantics, data-retention rules, and a recovery objective with product and support.
- Add stage-level timestamps, correlation IDs, database/worker metrics, and a production-shaped load generator with scrubbed or synthetic payload distributions.
- Reproduce the four-second result. Profile CPU, database waits, locks, queries, connection use, worker concurrency, payload size, and external calls. Produce a latency budget by stage rather than guessing at the cause.
- Establish the failing baseline at steady 40x load and short bursts. Also run duplicate storms, out-of-order streams, poison events, worker termination mid-event, deploy/restart, database interruption, backlog drain, and replay tests.

## Days 6-12: remove the measured bottleneck

- Make the smallest fixes supported by the profile: likely candidates include query/index changes, shorter transactions, elimination of synchronous network work, bounded worker concurrency, batch claiming, or separation of worker and request connection budgets.
- Run the complete harness after each material change and retain comparable results. Check domain correctness and database impact, not latency alone.
- At day 12, hold a go/no-go review. If the current stack meets the gates with headroom, lock the architecture for launch. If not, identify the remaining measured constraint and escalate the launch risk. Do not begin a wholesale rewrite. A transport experiment is justified only as a narrowly isolated, harness-tested fallback with a named owner and explicit stop date.

## Days 13-20: build the signed connector

- Implement the adapter, fixtures, signature/auth handling, canonical mapping, capability declarations, and conformance tests. Keep shared invariants out of connector code.
- Test against the carrier sandbox and recorded contract examples. Resolve undocumented payload or ordering behavior with the carrier while there is still schedule margin.
- Put enablement behind a carrier-and-broker feature flag. Add a kill switch that stops new processing without deleting durable inputs, and make replay after re-enable an exercised path.

## Days 21-26: prove production readiness

- Repeat steady, burst, recovery, reordering, duplicate, and replay tests with all three adapters enabled and production-like data volumes.
- Exercise deploys during load, worker crashes, database failover/interruption behavior, backlog alarms, and drain time. Verify that one connector's poison traffic cannot consume all workers or connections; use bounded per-carrier admission/concurrency if the test demonstrates that need.
- Run a game day with the actual on-call engineer and support liaison. They must detect a stalled carrier, identify affected brokers/events, disable the connector, inspect audit evidence, and safely replay it using the runbook.

## Days 27-30: release handoff

- Freeze the release candidate and collect the decision record, benchmark report, test evidence, dashboards, alerts, carrier contacts, data mapping, known limitations, and rollback/replay runbook in one handoff packet.
- Hold an engineering, product, and support readiness review against explicit gates. Record every exception with an owner and deadline; no silent waivers.
- In a sandbox or non-effecting production mode, validate authentication, event receipt, mapping, metrics, and flags. Schedule the remaining two weeks as a controlled rollout: internal traffic first, then one broker/load cohort, then staged expansion while watching each gate.

# Release gates and rollback

The release candidate must demonstrate, on a documented production-shaped workload:

- p95 end-to-end ingestion below two seconds at 40x projected load, with an internal target below 1.5 seconds for headroom, plus reported p99 and worst-case backlog age;
- zero lost acknowledged events, exactly one domain effect for duplicates, and conformance to the agreed per-stream ordering rule;
- recovery from tested worker, deploy, and database interruptions within the agreed recovery objective, followed by successful backlog drain and replay;
- no starvation of normal application traffic and no unbounded retry, worker, connection, or queue growth;
- actionable alerts and a game-day-proven disable, diagnosis, rollback, and replay procedure; and
- passing adapter conformance and carrier sandbox tests.

Rollback is configuration-first: stop cohort expansion, disable the third adapter, retain durable inputs, and continue the two proven connectors. A code rollback follows only if shared-path health is affected. Support gets a prewritten status template, the affected-event lookup, the escalation roster, and update intervals. Customer enablement never outruns the ability to identify and replay every accepted event.

# Ownership for an eight-person team

Assign one accountable technical lead for the decision and release, not a committee. Staff the month as follows, with the lead also contributing code: two engineers on instrumentation/performance and the shared ingestion path; two on the carrier adapter and carrier coordination; one on database/observability and capacity safety; one on the reliability harness and game day; and one release/support liaison on flags, runbooks, cohort state, and communications. Pair across these tracks at the conformance suite and game day so knowledge is not trapped with one person.

After launch, the shared-ingestion owner owns the adapter contract and invariants; the named connector owner owns carrier-specific mapping and relationship changes; the database/observability owner owns capacity thresholds and dashboards; and the weekly on-call owns incident command using the shared runbook. Connector ownership does not imply a separate service, deployment pipeline, or on-call rotation.
