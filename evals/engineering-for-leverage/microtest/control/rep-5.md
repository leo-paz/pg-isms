# 30-day decision

Keep the Python/Postgres monolith for this launch. Do not start the Rust rewrite, Kafka adoption, connector microservices, or a universal plugin system in this 30-day window. One failing latency result is a reason to instrument and test the current system, not evidence that all four changes are needed. The team has six weeks, knows this stack, and has eight months of stable shared behavior; a platform migration would put the signed carrier and existing commitments on the same critical path.

Record that choice in a short ADR on day 3. It is a time-bounded decision, not a declaration that the current architecture will scale forever. Reconsider components independently only when evidence supplies a reason:

- consider Kafka if a representative, tuned Postgres design cannot meet the sustained rate and recovery target, or if multiple independent consumers create a demonstrated durable-fan-out need;
- consider Rust only if profiling identifies CPU-bound code that cannot economically meet the target in Python;
- split a connector into a service only when it needs an independent reliability boundary, deploy cadence, or owning team;
- expand the adapter API into a plugin platform only after real carrier implementations reveal more stable commonality and an actual third-party extensibility requirement.

The two sales leads do not count as requirements. Capture their known differences as notes, but do not design to hypothetical integrations.

# Target architecture for the launch

Use one shared ingestion pipeline with narrow carrier adapters:

1. The HTTP endpoint authenticates the carrier, applies request-size limits, derives a carrier-scoped idempotency key and ordering key, and commits the raw payload plus metadata to a durable Postgres inbox. It acknowledges only after that commit. A duplicate key returns the same successful acknowledgement without repeating downstream effects.
2. Workers claim inbox records in bounded batches. Parallelism is allowed across ordering keys; events for the same agreed business stream are applied serially. Prefer a carrier sequence number when available. Define the fallback and gap policy with the carrier rather than silently sorting by arrival time.
3. A carrier adapter verifies signatures and converts the payload into a versioned canonical event. The existing shared application service owns ordering, idempotency, state transitions, retries, and audit writes. Adapters do not implement those policies.
4. Processing status, attempt count, timestamps, last error, and a trace/correlation ID stay with the inbox record. Successful domain changes and the immutable audit entry commit in one transaction. Permanent failures go to a visible quarantine state that operators can inspect and replay; they are not discarded.
5. Scale by tuning indexes and transaction scope, eliminating measured query or lock hotspots, batching safe work, and adding Python worker processes before introducing another runtime or broker.

First verify whether the two-second contract measures acknowledgement latency or receipt-to-application latency. Instrument and report both: `received -> durable` and `received -> applied`. That prevents an artificially fast acknowledgement from hiding a growing backlog.

The adapter seam should be a small internal Python protocol: `verify`, `dedupe_key`, `ordering_key/sequence`, and `normalize`. Put carrier registration and credentials in configuration and keep transport, retries, persistence, observability, and business rules out of adapters. Extract this seam from the two live connectors, then implement the third against it. Add a new method only when a concrete carrier requires it; use an explicit carrier capability flag for a real variation rather than a generic hook system.

# Acceptance gates

By day 5, convert the contract and operational expectations into agreed numbers. If stakeholders have not supplied stricter values, use these launch gates:

- a production-shaped 40x load, including bursts and realistic payload/key skew, sustains arrival rate for 60 minutes with p95 contract latency at or below 1.5 seconds, no loss, no incorrect duplicate effects, and no continuously growing backlog;
- the same run leaves at least 20% measured capacity headroom in the constrained resource;
- duplicate, concurrent, delayed, out-of-order, and sequence-gap fixtures preserve the documented per-key semantics;
- killing and restarting workers, dropping database connections, and replaying a backlog produces no loss or double application and drains within an agreed recovery objective;
- dashboards expose rate, both latency measures, backlog age/depth, duplicate rate, retry/quarantine count, worker and database saturation, and errors by carrier; alerts and the runbook are exercised by someone other than the author;
- the third adapter passes the shared contract suite plus carrier signature, fixture, sandbox, rate-limit, timeout, and malformed-payload tests.

If the 40x gate still fails, profile before changing architecture. Make the narrowest measured improvement and repeat the entire suite. If the tuned design cannot pass by day 20, preserve the customer rollout commitments by reducing internal scope, negotiating a controlled ramp or capacity limit with the business, and presenting the measured bottleneck plus the smallest alternative experiment. Do not attempt a six-week rewrite as a rescue plan.

# 30-day execution plan

## Days 1-3: decide and establish the baseline

- The technical lead owns the ADR and architecture boundary. The ingestion owner maps the current request path, queries, locks, retries, and audit behavior.
- Product/support and engineering clarify the two-second metric, projected traffic shape, rollout cohort, and recovery objective. The third-carrier owner confirms documentation, credentials, sandbox access, rate limits, signature rules, event IDs, ordering guarantees, and escalation contacts. Missing access is escalated on day 1.
- Add correlation IDs and timing spans, then reproduce the 40x result with a production-shaped fixture set. Record throughput, backlog growth, CPU, memory, database connections, query time, lock time, and I/O. Save the test configuration so results are comparable.
- Publish the ADR: current-stack decision, rejected scope, assumptions, evidence still needed, acceptance gates, and explicit reconsideration triggers.

## Days 4-10: create safety rails

- Build the repeatable capacity test and the duplicate/reordering/recovery matrix before changing the pipeline. Run them against the current implementation and retain the failing baseline.
- Add the narrow adapter contract and shared contract tests around the two live connectors without changing their external behavior. Golden fixtures should prove normalization, idempotency, ordering, audit output, and error classification.
- Add dashboards and alerts for both latency measures and backlog age. Create operator commands or an admin path to inspect, quarantine, and safely replay an event with an audit trail.
- Profile the baseline and rank bottlenecks by measured contribution. The technical lead approves only changes tied to one of those measurements.

## Days 11-20: remove the measured bottleneck and build carrier three

- Implement the durable inbox/worker separation only if the current path lacks it or the measurements show it is needed. Add or change indexes, batch sizes, worker concurrency, and transaction boundaries one at a time, rerunning the same tests after each material change.
- In parallel within the team, the carrier owner implements carrier three using the frozen narrow adapter contract and captured/sandbox fixtures. Changes to shared semantics require review from the ingestion owner and new contract tests; carrier-specific exceptions stay explicit in the adapter.
- By day 15, run the first end-to-end carrier sandbox flow. By day 18, run 40x capacity, ordering, recovery, and replay tests with all three connector mixes. By day 20, hold the evidence-based architecture checkpoint and either pass, continue with one bounded optimization, or invoke the scoped fallback above.

## Days 21-26: harden a releasable candidate

- Freeze architecture changes. Run a longer soak with traffic skew, duplicate storms, slow carrier responses where applicable, worker loss, database reconnects, and a deploy during backlog processing.
- Security-review signature verification and secret handling. Verify schema changes are backward compatible and that old and new application versions can coexist during deployment.
- Put carrier three behind a carrier-and-customer feature flag. Rehearse disablement, deployment rollback, and forward recovery from retained raw events. Rollback must not delete inbox or audit data.
- Have the on-call engineer who did not author the feature follow the draft runbook during a game day. Fix unclear alerts, permissions, and replay steps.

## Days 27-30: hand off and approve the controlled rollout

- Cut a release candidate and stop feature work. Rerun the complete acceptance suite from a clean environment and attach results, dashboard links, known limits, schema steps, and fixture versions to the release record.
- Hold a go/no-go review with the technical lead, ingestion owner, carrier owner, on-call owner, and product/support representative. A failed correctness, recovery, or latency gate is a no-go, not an on-call exception.
- Deploy dormant code first, validate existing connectors, then enable carrier three for an internal/test account and the smallest agreed broker cohort. Expand only after a full observation window with gates green. The launch at six weeks uses the same staged sequence; the remaining two weeks are contingency and controlled ramp, not new platform work.
- Support receives the rollout schedule, customer-visible behavior, status wording, known limitations, and escalation path. No internal architecture work changes an existing external commitment without product/support approval.

# Ownership and durable handoff

Use named people in the actual release record, with one accountable owner per line below:

- **Technical lead:** ADR, scope control, day-20 checkpoint, and go/no-go chair.
- **Ingestion owner:** shared pipeline, database behavior, idempotency/ordering/audit invariants, capacity results, and post-launch health.
- **Carrier-three owner:** adapter, carrier coordination, sandbox evidence, fixtures, and carrier-specific runbook notes.
- **On-call owner:** dashboards, alerts, recovery game day, replay permissions, deployment and rollback runbooks, and the first-week support rota.
- **Product/support owner:** contract interpretation, cohort/ramp approval, existing customer commitments, communications, and escalation coordination.

Required handoff artifacts are the ADR; concise architecture and event-state diagrams; adapter contract and fixture guide; benchmark scripts and before/after results; migration, deploy, disable, replay, and rollback instructions; dashboards and alert thresholds; carrier escalation contacts; and a risk/known-limit list. Schedule a 24-hour and seven-day post-enable review. The ingestion owner remains accountable after release; the carrier owner does not throw the connector over the wall at merge time.
