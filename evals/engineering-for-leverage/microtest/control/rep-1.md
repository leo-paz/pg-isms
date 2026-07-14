# 30-day decision and delivery plan

## Decision

For this 30-day window, keep the Python/Postgres monolith and make ingestion a well-defined module inside it. Do not begin a Rust rewrite, adopt Kafka, split services by carrier, or build a universal plugin framework. Those changes add three unfamiliar operating surfaces while the evidence shows one latency symptom, not a demonstrated architectural limit. They also consume the six-week launch window without directly improving the signed carrier's outcome.

Record this as a reversible architecture decision with a review date after the third connector has run at production volume. The decision is not that Kafka, Rust, or services are always wrong; it is that the team lacks the throughput, recovery, ordering, staffing, and operability evidence needed to justify them now.

The 30-day exit criteria are:

- the third connector is production-ready behind a per-customer feature flag;
- the projected 40x workload meets p95 ingestion delay below 2 seconds with agreed headroom, and ordering, idempotency, recovery, and audit tests pass;
- dashboards, alerts, replay controls, and a support runbook exist;
- the launch has a named owner, staged rollout and rollback criteria, and a 12-day buffer before the six-week commitment.

If the existing design cannot meet those criteria after measured tuning, the fallback is a narrow durable work queue or managed streaming component behind the same internal interface—not a simultaneous language, broker, and service rewrite.

## Target architecture

Keep webhook receipt, durable storage, processing, and connector code in one deployable, but separate their responsibilities:

1. The HTTP edge authenticates the carrier, applies request-size limits, assigns a correlation ID, and stores the immutable raw payload in a Postgres `inbox` record. It acknowledges only after that transaction commits.
2. A database uniqueness constraint on `(carrier, carrier_event_id)`—or a documented carrier-specific deduplication key—provides the primary idempotency barrier. Duplicate receipt is observable and harmless.
3. Workers claim inbox rows in bounded batches. Events that require ordering are partitioned by the carrier's true ordering key, such as shipment or load ID, so work for different keys can run concurrently without reordering one key.
4. A small carrier adapter validates and normalizes the payload into the existing domain command. The shared ingestion service owns deduplication, ordering, retries, audit records, state transitions, and terminal failure handling.
5. Processing and its audit/state transition commit atomically where possible. Retries use capped exponential backoff; poison events move to an inspectable failed state rather than blocking unrelated keys. Replay is an explicit, authorized operation with an audit entry.

This creates a seam that could later be backed by Kafka or moved into another process without changing connector behavior. Postgres remains the source of truth during the launch; there is no dual-write path.

Before tuning, instrument timestamps for received, durably accepted, claimed, processed, and completed. Break the four-second p95 into queue wait, database time, external calls, and application time. Likely remedies—worker concurrency, shorter transactions, indexes, batch size, connection limits, and removal of synchronous work from receipt—must be selected from measurements, not guesses. Capacity testing must also verify database CPU, I/O, locks, connection saturation, table growth, and backlog drain time.

## Abstraction boundary

Extract only the stable behavior demonstrated by the two live connectors over eight months. Define a narrow in-process `CarrierAdapter` contract with operations equivalent to:

- verify/authenticate the webhook using carrier-specific rules;
- derive the event ID, event type, event time, and ordering key;
- parse and normalize the payload into typed domain input;
- classify malformed, retryable, and permanent carrier-specific failures.

Adapters do not own persistence, threads, retries, audit formatting, deployment, or customer rollout. Shared contract tests run unchanged against every adapter, with carrier fixtures covering duplicates, out-of-order delivery, malformed events, signature failure, retry, and replay. Carrier-specific code can remain explicit when behavior differs; no configuration language, dynamic discovery, third-party plugin API, or speculative hooks are added for the two sales leads.

The interface should be versioned only when a second real implementation need proves the change. The third adapter is the test of whether the boundary is useful; if it requires pervasive exceptions, revise the boundary rather than hiding differences in flags.

## Thirty-day execution

### Days 1–5: establish facts and freeze scope

- Name the launch DRI and write the architecture decision, non-goals, two-second SLO definition, traffic model, and rollback rules.
- Add end-to-end timing, backlog, retry, duplicate, failure, and per-carrier metrics. Trace several representative events.
- Reproduce the 40x test with a documented payload mix, ordering-key distribution, arrival shape, database size, and infrastructure. Capture a baseline rather than relying on the single prior result.
- Add failing tests for sustained throughput, burst behavior, duplicate storms, reordering, worker crash/restart, poison events, database interruption, replay, and backlog recovery. Define success thresholds, including zero incorrect state transitions and a bounded drain time.
- Freeze the third connector's required event set with the carrier and product. Sales leads do not enter this scope.

Decision gate on day 5: publish the measured bottleneck and choose the smallest remediation. Escalate immediately if the signed carrier cannot provide fixtures, credentials, or certification access.

### Days 6–12: harden the shared ingestion path

- Implement the durable inbox lifecycle and database-enforced deduplication where the current system lacks them; preserve existing behavior with characterization tests.
- Add safe worker concurrency by ordering key, explicit retry/failure states, replay tooling, and complete audit correlation.
- Tune only the measured constraint. Review migrations for lock duration and rehearse them on production-sized data.
- Run the full workload and failure suite after every material change. Compare latency distributions and resource ceilings, not only averages.

Decision gate on day 12: proceed if the system meets the SLO with headroom and drains a defined backlog after failure. If not, spend at most three days prototyping one narrow queue alternative against the same tests. The CTO approves any expansion only with benchmark evidence, migration/rollback cost, and an owner for operations.

### Days 13–20: build the signed connector

- Finalize the adapter contract from the two existing implementations, then implement the third with recorded/synthetic fixtures and carrier sandbox traffic.
- Run the shared contract suite plus carrier-specific signature, schema, rate-limit, and error cases.
- Put enablement behind carrier, customer, and event-type flags. Default all new flags off.
- Conduct an audit review: each incoming event must be traceable from raw receipt through deduplication, normalized action, retries, final state, and replay.

### Days 21–26: production rehearsal

- Deploy dark with receipt disabled or sandbox-only, then run the production-like 40x workload for long enough to expose connection, storage, and backlog trends.
- Rehearse worker termination, deploy interruption, database failover/interruption, bad payload flood, carrier retry storm, and rollback. Verify that restart causes neither loss nor double application.
- Validate dashboards and alerts with support: p50/p95/p99 ingestion delay, receive and completion rate, oldest pending age, queue depth, duplicates, retry rate, terminal failures, replay count, and per-carrier/customer health.
- Run a game day in which someone other than the author diagnoses and recovers a failed event using only the runbook.

### Days 27–30: release handoff

- Produce a release candidate, migration/rollback checklist, evidence packet, known-limitations list, capacity result, and carrier certification status.
- Hold a go/no-go review against written criteria. Unresolved correctness, recovery, audit, or SLO failures are no-go; the date alone is not a go criterion.
- Deploy shared-path changes independently first if safe, observe them on the two existing carriers, and keep the new connector dark.
- Hand the remaining 12-day launch buffer to the release owner for carrier certification, staged customer enablement, and observation. Do not change customer-visible commitments unless a no-go condition is reached.

## Ownership and operating model

One engineering lead is accountable for the launch and scope. A platform/reliability engineer owns ingestion behavior, capacity tests, dashboards, migrations, and rollback. A connector engineer owns the third adapter, fixtures, and carrier certification. A second engineer owns independent contract and failure testing. The engineer on call owns production response only after completing the game day; feature authors remain escalation contacts through launch.

Product owns the event scope and customer promise. Support owns customer communication and validates the troubleshooting guide, but does not decide technical readiness. The CTO reviews the day-5 and day-12 evidence and decides only on exceptional scope or platform changes, avoiding day-to-day design churn. Every deliverable has one directly responsible owner in the tracker, with a backup named for launch week.

## Release and handoff contract

Enable the third carrier in stages: internal/sandbox traffic, one low-risk broker or a controlled traffic slice, then the remaining signed scope. Hold each stage through an agreed observation window. Promotion requires p95 below two seconds, no unexplained backlog growth, no incorrect ordering or duplicate application, acceptable database headroom, and zero unresolved high-severity audit gaps.

Rollback means disabling new event intake with the feature flag and reverting compatible application code; it must not delete accepted inbox records. Accepted events remain visible and can be drained or replayed after correction. Database changes must be backward compatible through the observation period.

The handoff package contains the architecture decision, adapter contract, test and capacity evidence, dashboards, alert thresholds, on-call and support runbooks, replay authorization procedure, schema migration plan, rollback commands, feature-flag matrix, carrier contacts, and customer communication templates. Schedule a review 7 and 30 days after enablement. At that review, reconsider Kafka or service extraction only if measurements show sustained database/queue limits, materially different scaling or deployment needs, or operational ownership that a separate service would improve. Consider a broader plugin framework only after multiple signed carriers demonstrate repeated variation that the narrow adapter cannot express.
