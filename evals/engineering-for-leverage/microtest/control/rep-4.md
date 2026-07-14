# 30-day decision

Keep the Python/Postgres modular monolith for this launch. Do not introduce Rust, Kafka, per-connector microservices, or a universal plugin system in the next 30 days. The evidence currently shows one latency symptom, not a demonstrated throughput or architecture limit. A rewrite would add unfamiliar operations, dual-write/migration risk, and several new failure boundaries directly on the six-week critical path.

Treat that as a time-bounded decision, not a permanent rejection. Record it in an ADR with explicit revisit evidence: sustained arrival rate and burst shape, queue-age p95/p99, database saturation, recovery time after a representative outage, ordering violations, duplicate side effects, and operator toil. Kafka or service extraction becomes a candidate only if the measured workload cannot meet the contract and recovery objective after bounded improvements to the existing path, or if connector teams genuinely need independent deployment and scaling. Sales leads do not count as that evidence.

The 30-day outcome is a production-shaped third connector behind a flag, a measured and hardened ingestion path with launch gates, and two weeks of schedule buffer before the signed launch.

# Architecture for the launch

Use one ingress pipeline and make carrier-specific code a thin edge adapter:

1. A carrier route authenticates the webhook, captures receipt metadata, and stores the immutable raw payload.
2. In the same database transaction, write an inbox record with a database-enforced idempotency key and create the durable work item. Acknowledge only according to the carrier's documented retry contract; do not claim exactly-once delivery.
3. Existing workers process at-least-once. They normalize the carrier payload into the current internal event model, serialize work by the established business ordering key, apply state changes idempotently, and append an audit record.
4. Retry policy, dead-letter/quarantine state, replay tooling, metrics, and audit behavior belong to the shared pipeline. Parsing, authentication details, event mapping, and carrier API behavior belong to an adapter.

Prefer the existing, proven ordering mechanism unless tests disprove it. Before changing it, document exactly what is ordered: for example, per load or shipment rather than globally, how sequence-less events are handled, and what late events do. The correctness contract should be "at-least-once receipt plus idempotent effects and defined per-entity ordering," with duplicate and late-event outcomes visible in audit history.

Keep the durable queue in Postgres for this cycle. Instrument queue age separately from end-to-end ingestion latency so the four-second result can be attributed to ingress, lock contention, database work, worker capacity, or downstream calls. Likely low-risk levers include removing synchronous network work from the request path, query/index correction, bounded worker concurrency, connection-pool tuning, and batching where ordering permits. Apply only changes justified by profiles and query plans; do not assume all of them are needed.

# Abstraction boundary

Create a small, versioned `CarrierAdapter` contract from the common behavior already stable across the two live carriers. It should cover only:

- webhook verification and extraction of a stable carrier event identifier;
- parsing into a versioned normalized event or a typed rejection;
- identification of the business ordering key and any carrier sequence/time metadata;
- capability declarations for real differences such as event types or acknowledgement rules.

The adapter must not own queueing, retries, idempotency storage, audit persistence, customer feature flags, or observability. Those remain shared services called through normal in-process interfaces. Register adapters explicitly in code and deploy them with the monolith. Avoid runtime plugin loading, a connector SDK, or speculative hooks for the two sales leads.

Add contract tests that every adapter runs against shared fixtures: valid signature, invalid signature, duplicate delivery, reordered delivery, malformed and unknown events, retryable and terminal failures, audit completeness, and replay. Add golden fixtures for each carrier with secrets and customer data removed. The third connector is an implementation of this contract; refactor the two live connectors only enough to prove that the boundary describes current behavior without changing their customer-visible behavior.

# Evidence and gates

By day 10, replace the single load-test result with a production-shaped test matrix. Use observed payload sizes and burstiness, then test current peak, projected 40x steady state, and projected 40x bursts. Measure throughput, end-to-end and queue-age p95/p99, database CPU/IO/locks/connections, worker utilization, duplicate effects, and ordering violations.

The release gate is not merely p95 under two seconds. It requires all of the following in a production-like environment:

- p95 end-to-end ingestion delay below two seconds at the agreed 40x scenario, with documented safety margin and no unbounded queue growth;
- zero duplicate business effects and zero ordering-contract violations in duplicate/reordering tests;
- recovery from worker restart, database failover simulation, backlog, and poison messages within an agreed recovery objective;
- a successful replay that preserves auditability and does not repeat side effects;
- dashboards and alerts that let the on-call distinguish ingress errors, queue delay, processing failures, and carrier-specific failures;
- a rollback rehearsal that disables only the new carrier while leaving the two live connectors unchanged.

On day 2, the CTO, support lead, and engineering owner should set the missing numeric recovery objective, burst duration, acceptable error rate, and backlog-drain target. If they cannot agree, use the current customer contract as the latency ceiling and choose conservative internal targets, recording the open business decision rather than silently inventing one.

# Ownership

Assign one launch DRI with authority over scope and the go/no-go checklist. Split the eight-person team without creating component silos:

- One engineer owns the third carrier adapter and sanitized fixtures.
- One owns shared pipeline correctness, schema/index changes, and migration rollback.
- One owns load, fault, replay, and recovery testing plus dashboards.
- A second engineer reviews each area and can operate it; no critical subsystem has a single knower.
- The CTO is the architecture decision owner and removes scope, rather than adding platform work, if a gate is at risk.
- Support owns customer wording and escalation readiness, while engineering owns technical truth and incident response.

Keep one named incident commander and one release operator for launch, with a separate rollback decider. Document ownership in the runbook and code ownership rules. Schedule two short knowledge-transfer sessions and require the backup owners to execute one replay and one rollback rehearsal themselves.

# 30-day execution and handoff

**Days 1-3: baseline and decision lock.** Freeze new-platform work. Publish the ADR, current data flow, correctness contract, SLO definitions, known unknowns, and scope exclusions. Add correlation IDs and timestamps across receive, persist, claim, process, and complete stages. Capture a reproducible baseline, including the failing four-second scenario, before optimization.

**Days 4-10: characterize and design.** Run the load matrix and profile the bottleneck. Exercise duplicates, reordering, backlog, poison messages, restart, and replay. Specify the narrow adapter contract from the two live implementations. Produce the third carrier's mapping table and fixture set. Review any schema migration for lock duration and rollback.

At day 10, hold a decision checkpoint. Continue with Postgres if the bottleneck has a credible bounded fix and correctness tests pass. If evidence shows a hard database/queue limit, use the remaining time for the smallest proven isolation step, such as moving processing behind a durable boundary while retaining the monolith's domain logic; do not default to a full Rust/Kafka/microservice program. Any larger replatforming gets a separate plan and cannot displace the signed launch without an explicit business decision.

**Days 11-20: implement and harden.** Make the measured performance corrections, implement the adapter boundary and third connector, and add contract/integration tests. Ship observability and quarantine/replay controls with the code. Deploy database changes separately when possible, using expand/contract-compatible changes. Keep all third-carrier behavior off by default and preserve the live connectors' existing routes and flags.

**Days 21-26: production-shaped proving.** Run the full performance and failure suite on the release candidate. Shadow or replay sanitized traffic where legally and operationally safe, without customer side effects. Rehearse deploy, disable, rollback, backlog drain, replay, credential rotation, and incident escalation. Support validates screenshots, statuses, customer messaging, and the escalation tree.

**Days 27-30: release handoff.** Freeze connector scope and close or explicitly waive every gate with the CTO and launch DRI named on the decision. Deliver a versioned runbook containing dashboards, alert meanings, carrier contacts, feature-flag controls, common failure diagnosis, quarantine/replay steps, rollback thresholds, and audit queries. Conduct a game day led by the backup operators. Deploy the dormant connector code through normal production stages, verify no regression for the two live carriers, and leave enablement for the six-week launch behind a per-customer flag.

The handoff package includes the ADR, architecture and ordering contract, adapter contract, carrier mapping/fixtures, benchmark and recovery results, migration and rollback records, dashboard links, on-call ownership, support FAQ, and a signed go/no-go checklist. For the actual launch, use a canary: internal/test tenant, then the signed broker with a bounded subset if possible, then full enablement. Pause automatically or manually on contract latency, queue growth, audit gaps, duplicate effects, or unexplained ordering violations. Rollback means disabling the third adapter and draining or quarantining its work; it must not require rolling back unrelated fixes or changing customer commitments for the two existing connectors.
