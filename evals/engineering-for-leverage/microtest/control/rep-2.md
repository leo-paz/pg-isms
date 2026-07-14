# 30-day decision

Keep the Python/Postgres monolith for this launch and make the ingestion path measurable, bounded, and horizontally scalable inside it. Do not commit this month to Rust, Kafka, per-connector microservices, or a universal plugin framework.

The evidence does not support a rewrite. The team has one adverse latency result but has not isolated its cause or tested the other properties that matter. A six-week contractual launch also makes a simultaneous language, broker, deployment, and service-boundary migration an avoidable delivery risk. Kafka or Rust may eventually be justified, but only by a demonstrated bottleneck that simpler changes cannot fix. Microservices by connector would duplicate behavior that has been stable and shared for eight months and would add deployment and incident surfaces to an eight-person team.

This is a reversible decision with explicit exit criteria. Revisit the platform choice after the third carrier is stable, or earlier if tests show that a tuned Postgres queue cannot meet the contract with adequate headroom. Consider Kafka when durable replay across multiple independent consumers, retention beyond practical Postgres limits, or measured write/dispatch contention requires it. Consider extracting a service only when it has an independently scaling workload, ownership boundary, or reliability policy. Consider Rust only for a profiled CPU-bound component whose cost matters after algorithmic and operational fixes. Sales leads do not count as requirements.

The 30-day success gate is: at projected 40x traffic plus 50% headroom, p95 webhook-to-durable-acceptance latency is at most two seconds and p99 is documented; no accepted event is lost; duplicate delivery has no duplicate business effect; defined ordering is preserved; the system recovers from worker and database interruptions within agreed targets; and the on-call engineer can detect, drain, replay, and quarantine work using a runbook. If these gates cannot be met by day 20, the team uses the remaining time to choose the smallest evidence-backed architecture change and renegotiate scope rather than disguise uncertainty with a rewrite.

# Architecture for the next carrier

Use a modular ingestion pipeline within the monolith:

1. The HTTP edge authenticates the carrier, applies payload-size and rate limits, records a correlation ID, and durably stores the raw request plus essential headers in an append-only inbox transaction. It returns success only after that commit. Slow business processing is not on the request path.
2. A unique idempotency constraint uses `(carrier, carrier_event_id)` when the carrier supplies a stable identifier. The fallback is a documented carrier-specific key derived from stable fields, with a payload hash retained to detect conflicting reuse of a key. Duplicate receipts link to the original inbox record and do not repeat effects.
3. Workers claim rows in bounded batches using Postgres locking semantics such as `FOR UPDATE SKIP LOCKED`, normalize them into a versioned internal event, and invoke the existing shared ordering, idempotency, and audit pipeline. Worker count and batch size are configuration, not connector code.
4. Ordering is defined explicitly, not globally: events are serialized by the smallest business key whose order matters, such as carrier plus shipment/load identifier. Per-key sequence numbers are used when supplied; otherwise arrival order is recorded and late/out-of-order events are quarantined or reconciled according to a documented rule. Retries cannot overtake earlier work for the same key.
5. Business state changes and an outbox record are committed in one database transaction. External side effects are dispatched from the outbox with their own idempotency keys. Processing attempts, state transitions, actor/version, timestamps, and errors remain queryable for audit and replay.
6. Poison events move after a bounded retry policy to a quarantine state with reason, payload reference, and safe replay controls. Backoff has jitter and does not block unrelated ordering keys.

Before adding infrastructure, tune what measurements identify: indexes for claim and idempotency queries, short transactions, connection-pool limits, payload storage strategy, worker concurrency, and possibly time-based partitioning if table growth warrants it. Set database and worker saturation limits so increasing workers cannot overwhelm Postgres. Raw payload retention and redaction must match customer and compliance obligations.

# Abstraction policy

Build a narrow third-carrier adapter, not a universal plugin framework. The adapter contract should cover only observed variation:

- authenticate and validate a webhook;
- extract the stable event identity, ordering key, source timestamp, and event kind;
- translate the carrier payload into a versioned canonical event or a typed unsupported-event result;
- declare carrier-specific retry/acknowledgment constraints; and
- expose fixture-driven contract tests.

Keep durable receipt, deduplication, ordering, retry, quarantine, audit, metrics, and outbox behavior in the shared ingestion core. Carrier adapters must not own their own queues, database schemas, retry loops, or deployment units. Preserve the raw source payload so canonicalization bugs can be corrected and replayed.

Use the two current connectors and the signed third connector to test the seam. If implementing the third requires conditionals in shared code, first decide whether the difference is a legitimate adapter capability or a business rule common to all carriers. Do not design extension points for the two leads. Record proposed capabilities in a short deferred-requirements list and promote one only after a signed carrier demonstrates it.

# Ownership

Assign one directly responsible engineer for ingestion reliability and one for the third-carrier adapter, with a named backup for each. They may be a small working pair, but their acceptance criteria differ:

- The ingestion owner owns the inbox/outbox path, shared semantics, load and recovery harness, dashboards, SLOs, capacity model, and operational runbook.
- The connector owner owns mapping accuracy, carrier authentication, fixture coverage, sandbox/certification coordination, and carrier-specific release evidence.
- A product/support owner owns customer communications, rollout commitments, and the support decision tree. No date or behavior change is communicated without this owner.
- The CTO is the architecture decision owner and records the decision, alternatives, evidence, expiry/review date, and exit triggers. This prevents the rewrite proposal from remaining an unbounded parallel project.

Every production alert has an owning team member, a severity, and an action. During rollout, the primary ingestion owner is not also the only person able to replay or disable the connector.

# 30-day execution plan

## Days 1-3: establish facts and freeze scope

- Write the architecture decision record and define “ingestion delay” precisely: receipt-to-durable-acceptance and receipt-to-business-application should be separate measures.
- Capture current traffic shape, burstiness, payload sizes, database utilization, queue depth, slow queries, retry rates, duplicates, and event-key distribution. Reproduce the 40x result with a controlled workload and profiles.
- Agree on SLOs, recovery targets, ordering keys, retention, and the launch must-haves. Freeze the third-carrier event set. Put Rust/Kafka/framework work outside the launch scope.
- Add tracing/correlation from HTTP receipt through inbox, processing, state mutation, and outbox delivery. Dashboard queue age, throughput, error and retry rates, duplicate rate, quarantine count, worker saturation, connection-pool pressure, and database CPU/I/O/locks.

Deliverable: signed decision record, test matrix, baseline measurements, and named owners.

## Days 4-10: harden the shared path

- Implement or tighten the durable inbox, unique idempotency constraints, bounded worker claims, per-key ordering, retry/quarantine behavior, and transactional outbox.
- Add the narrow adapter interface and move the two existing connectors behind it without intentionally changing behavior. Golden fixtures must prove equivalent canonical events and acknowledgments.
- Build a deterministic test harness that can generate duplicates, conflicting IDs, delayed and reordered events, worker crashes, timeouts, malformed payloads, and database interruption.
- Profile and tune only observed bottlenecks. Document the capacity relationship among arrival rate, service rate, worker count, connections, and maximum queue age.

Deliverable: shared pipeline passing unit, integration, and adapter contract tests in a production-like environment.

## Days 11-17: implement carrier three and prove failure behavior

- Implement the third adapter from captured/sandbox fixtures, including signature verification, event identity, ordering key, mappings, unsupported events, and acknowledgment rules.
- Run sustained, burst, and soak tests at 40x and 60x projected traffic. Report p50/p95/p99 latency, throughput, database headroom, queue growth, and time to drain.
- Run recovery tests for process termination before and after commit, database unavailability, retry storms, poison messages, duplicated and reordered delivery, and outbox destination failure. Verify invariants from database records, not merely HTTP responses.
- Have someone other than the author execute quarantine and replay procedures from the draft runbook.

Deliverable: a signed test report with failures, fixes, remaining headroom, and an explicit go/no-go recommendation.

## Days 18-23: production shadow and operational readiness

- Deploy the shared changes with behavior-preserving flags. Start the third connector in receive-and-record/shadow mode where the carrier permits it: authenticate and normalize events, compare expected mutations, but suppress customer-visible effects.
- Use per-carrier and, if possible, per-customer kill switches. Make rollback stop new processing without deleting durable receipts; define how queued events will be resumed or replayed after a fix.
- Review dashboards and alerts with engineering and support. Complete runbooks for backlog growth, auth failure, mapping failure, duplicate conflict, ordering gap, quarantine, replay, carrier disablement, and escalation.
- Hold a launch-readiness review covering security, data retention, migrations, capacity, rollback, carrier certification, support copy, and ownership schedules.

Deliverable: operational sign-off and a release candidate. If the latency or correctness gate is still red, keep customer commitments unchanged only by narrowing internal scope or adding temporary capacity that testing proves safe; do not silently reduce reliability.

## Days 24-30: controlled release and handoff

- Enable the third connector for an internal/test account, then one low-risk customer, then the remaining contracted scope in timed cohorts. Advance only after a full observation window with latency, errors, duplicates, ordering gaps, quarantine, and support contacts within thresholds.
- Staff an engineering and support watch for each cohort. Use one incident channel and decision log. The ingestion owner has authority to pause rollout; support has a current status template but does not have to diagnose internals.
- Reconcile carrier counts against inbox, canonical events, business effects, and outbox deliveries after each cohort. Sample audit histories manually.
- At day 30, hand off dashboards, alert ownership, runbooks, replay permissions, known issues, capacity limits, and deferred requirements to the normal on-call rotation. Schedule a two-week post-launch review.

# Release gates and rollback

Promotion requires all automated correctness tests to pass; the 60x test to meet the two-second p95 target with stable queue depth and documented database headroom; recovery and reordering exercises to meet their targets; zero unexplained loss or duplicate business effects; no unresolved critical security or data-integrity issues; and successful runbook execution by the backup owner.

Pause a cohort on SLO breach, monotonically growing backlog, ordering or duplication invariant failure, unexplained reconciliation mismatch, or elevated customer errors. Roll back by disabling carrier processing at the feature flag while continuing safe durable receipt if possible. Drain or replay only after the defect and affected range are identified. A schema migration must be backward-compatible through the rollout window.

This plan preserves the current customer-visible commitment while changing its risk profile: the launch rests on measured capacity, explicit invariants, staged exposure, and operable recovery. It also leaves clean seams and decision evidence for a future broker or service extraction without paying that complexity before it is needed.
