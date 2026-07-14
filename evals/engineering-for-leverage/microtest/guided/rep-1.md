# 30-day technical decision

## Decision record

Choose the familiar Python/Postgres monolith for the third carrier and for the next 30 days. Harden the ingestion path, extract only the shared connector lifecycle, and test it under representative load and faults. Do not introduce Rust, Kafka, a universal plugin framework, or connector microservices in this launch.

This is a reversible decision, not a claim that the current design will scale. The four-second p95 is evidence of a problem, but one load test without throughput, resource, recovery, reordering, or operability data does not identify Python or Postgres as the limiting component. A six-week committed integration and an eight-person team make simultaneous language, broker, framework, and service-boundary migrations a larger delivery and reliability risk than the observed, still-undiagnosed latency.

Facts:

- The company has three paying B2B customers, two live connectors, one contracted launch in six weeks, and two uncommitted leads.
- Ordering, idempotency, and audit semantics have been shared and stable for eight months. That is enough evidence for a small common primitive, but not for a universal carrier platform.
- The known contract is p95 ingestion delay below two seconds. The only scale evidence is p95 of four seconds at projected 40x volume.
- The team can build, debug, deploy, observe, and operate Python/Postgres today.

Assumptions to confirm with the CTO, support, and the carrier by Day 2:

- The company is not in an acute cash-survival event that supersedes this work.
- “Ingestion delay” means webhook receipt through committed customer-visible state, not merely HTTP acknowledgement; the test and dashboard will use that end-to-end definition.
- The carrier supplies stable authentication and event/order identifiers or a documented reconciliation endpoint.
- Temporary recovery targets below do not weaken any existing customer or security commitment. If an existing commitment is stricter, it replaces the temporary target.

The binding constraint is reliable delivery of the signed connector with contractual latency, while the cause of the projected latency miss remains unknown. Evidence latency is days in a local replay environment and weeks for carrier sandbox/production behavior. A monolith change behind flags is relatively reversible; a new language, event platform, and service topology would add deployment, observability, security, migration, hiring, debugging, and on-call costs before showing product-specific advantage.

Candidates and leverage test:

| Candidate | Decision | What would justify it |
|---|---|---|
| Hardened Python/Postgres monolith | Choose now | It passes the predeclared load, invariant, recovery, and operability gates with the current team. |
| Kafka-backed ingestion | Reject for this launch | Reconsider only if the tuned baseline fails because durable queue work demonstrably contends with domain storage, or required retention/replay cannot be met, and a thin managed-Kafka spike passes the same tests including deployment and recovery. |
| Rust hot path | Reject for this launch | Reconsider only if profiling shows a CPU-bound Python stage is the binding constraint and a bounded Rust replacement behind that seam gives material end-to-end improvement after build, debugging, deployment, and on-call costs. |
| Universal plugin framework | Reject | Reconsider after several implemented carriers show repeated stable extension vocabulary; sales leads are not implementation evidence. |
| Microservice per connector | Reject | Reconsider when measured independent scaling or release cadence requires isolation and there is an owner able to deploy, observe, secure, and operate each boundary without added handoffs or incidents. |

No speculative Kafka or Rust branch will be maintained. The preserved option is the durable event log and a narrow claim/process boundary: a later worker or broker can consume the same versioned event envelope and conformance fixtures without changing connector payload parsing or domain semantics.

## Target architecture and abstraction

Keep one deployable and one operational surface:

`carrier HTTP adapter -> authentication/validation -> durable inbox -> ordered workers -> domain transaction -> transactional outbox/audit`

- Each carrier adapter owns signature or mTLS verification, request limits, payload parsing, carrier-specific mapping, and acknowledgement rules. It produces a small, versioned event envelope containing carrier, external event ID, domain ordering key, carrier sequence/time when available, received time, schema version, raw-payload reference/hash, and normalized command.
- The shared ingestion kernel owns the behavior proven common for eight months: durable receipt, idempotency, per-domain-key ordering, retry classification, quarantine, deterministic replay, and audit transitions. The third carrier is explicitly registered in code; there is no dynamic plugin loader, configuration language, or speculative “all carriers” schema.
- Postgres is the source of truth. Receipt and the unique idempotency key are committed atomically to an append-only inbox. Workers claim bounded batches; work for the same ordering key is serialized. Domain mutation and an outbox record for external side effects commit together, so a crash cannot create an unaudited half-effect. Notifications may wake workers but are never the durable mechanism.
- The ordering policy is explicit and connector-tested. If the carrier provides sequence numbers, gaps are held and reconciled. If it does not, retain the existing deterministic domain rule and reconcile against the carrier source of truth. Raw accepted events and processing versions support deterministic replay. Replays use the same idempotency and ordering checks as live traffic.
- Audit records receipt, authentication result, payload hash, processing version, state transitions, attempts, actor, error class, and final disposition. Sensitive payload access uses existing least-privilege service roles and retention policy. Invalid signatures, oversized/malformed payloads, and replay attempts are rejected or quarantined with metrics; one carrier's backlog is rate-limited so it cannot consume all workers or database connections.
- Existing live connectors move to the kernel one at a time behind per-carrier flags. Their current path stays available through the launch window. The third adapter uses the new kernel; if its processing is paused, accepted inbox events remain replayable.

The interface is accepted only with a conformance suite: golden carrier fixtures, duplicate delivery, concurrent delivery for one ordering key, out-of-order and missing sequences, worker interruption at every transaction boundary, database disconnect, poison payload, retry exhaustion, replay, and audit completeness. Carrier-specific exceptions remain in the adapter instead of weakening shared invariants.

Retreat from the abstraction if a connector needs bypasses for shared invariants, ordinary changes require edits across unrelated adapters, or adapter lead time, call sites, coordination, or incidents increase at the Day 30/Day 45 reviews. In that case keep the stable inbox primitive but return divergent mapping or workflow behavior to the carrier module. Do not preserve an abstraction merely to avoid duplication.

## Precommitted evaluation

The ingestion DRI owns a reproducible harness by Day 5 and records the keep/redesign decision on Day 10. Build a sanitized corpus from the last 30 days of both live carriers, preserving payload-size, duplicate, ordering-key hot spot, and burst distributions, plus third-carrier certification fixtures. Record phase timing, queue depth/age, rows and locks, query latency, connections, CPU, memory, worker utilization, retries, and external-call time.

Run these bounded tests against production-equivalent topology and data volume:

1. Sustain projected 40x peak for 60 minutes, then a 60x burst for 15 minutes. Pass only if receipt-to-committed-state p95 is at most 1.5 seconds at 40x, contractual p95 remains below two seconds during the burst, no backlog grows without bound, and database/worker capacity has observable headroom.
2. Inject the corpus's duplicates plus a 10% duplicate storm and shuffled events, including gaps and simultaneous events for one key. Pass only with zero duplicate business effects, zero invalid state reorderings, and an audit disposition for every accepted event.
3. Kill workers before and after each commit boundary, interrupt database connectivity for 60 seconds, restart the deployment, and poison one carrier's stream. Pass only with zero accepted-event loss, deterministic reconciliation/replay, isolation of the poisoned stream, and backlog drained within 15 minutes after restoration. The 15-minute target is provisional until Day 2 contract review.
4. Give the on-call engineer only dashboards, alerts, and the draft runbook. Pass only if queue-age or contract-risk alerts fire within five minutes, the engineer can identify the affected carrier and failure stage within ten minutes, and can pause, resume, quarantine, and replay without direct database edits.

Any idempotency, ordering, audit, or accepted-event-loss failure is an automatic release stop, regardless of latency. If the familiar baseline misses latency, first use measured evidence to change indexes, query shape, transaction scope, worker concurrency, connection allocation, batch size, backpressure, or database sizing and rerun the entire suite. By Day 10, if it still fails, write a short successor TDR naming the measured bottleneck. Only then run one bounded alternative spike targeted at that bottleneck; compare it on the same end-to-end and operability gates. Do not start a general replatform.

## 30-day execution and ownership

**Days 1–5 — establish truth.** The CTO is accountable for the decision and scope. One backend engineer is ingestion DRI and end-to-end code/incident owner; a second is named backup. They freeze unrelated ingestion refactors, confirm contracts and carrier certification steps with support, instrument phase timings, capture the corpus, document current data/invariant seams, and produce the failing baseline across load, recovery, reordering, and operability. Security review confirms webhook authentication, secret handling, payload retention, and least privilege. Support does not own technical correctness, but validates customer-visible timing and failure communications.

**Days 6–10 — decide with evidence.** The ingestion DRI profiles and tunes the familiar baseline, implements the minimal durable-inbox/worker seam if the current synchronous path causes queueing, and reruns all tests. On Day 10 the CTO signs the TDR: continue on Python/Postgres if every gate passes; otherwise authorize only the bottleneck-specific spike described above. Publish the measurements, rejected options, remaining uncertainty, and rollback seam.

**Days 11–20 — implement the signed carrier.** Build the third adapter and common conformance suite. Extract only shared lifecycle behavior as encountered. Migrate the first live connector to the kernel in shadow mode, comparing resulting commands, ordering decisions, and audit records without duplicating external effects; then canary it behind its flag. Carrier sandbox/certification is deployment evidence and is required—an undeployed spike is not enough. Add dashboards per carrier for receipt rate, phase latency, oldest inbox age, retries, quarantine, ordering gaps, duplicate suppression, and audit completion.

**Days 21–26 — prove recovery and supportability.** Migrate the second live connector only if the first remains clean. Run the full suite on the release candidate, conduct a game day with the backup/on-call engineer, and rehearse pause, flag rollback, backlog replay, reconciliation, and customer communication. Complete the carrier's security/procurement/integration checklist. Fix the release candidate after any invariant failure and rerun from the start.

**Days 27–30 — hand off release readiness.** Freeze the common kernel except for launch blockers. The ingestion DRI hands the release owner a signed evidence packet: TDR, test results, certification evidence, dashboards/alerts, known limits, data migration status, flags, rollback and replay commands, incident owners, and runbook. Support receives observable symptoms, customer wording, escalation paths, and status-update cadence. The release owner—not the architecture project—owns exposure, monitoring, support coordination, rollback gates, and incident response for the remaining two weeks.

Production exposure is staged inside the unchanged customer commitment: carrier sandbox/shadow, internal or agreed test loads, then a bounded canary, then full enablement. Any accepted-event loss, duplicate side effect, invalid ordering, missing audit record, authentication bypass, or unreconciled divergence stops exposure immediately. Two consecutive five-minute windows above the two-second p95 contract pause expansion; sustained backlog age or quarantine beyond the runbook threshold does the same. Roll back a migrated live connector with its per-carrier flag. For the new connector, pause processing while preserving durable receipts, reconcile, repair, and replay before resuming; do not discard or manually mutate events.

Review on Day 30 and again after the six-week launch. Record lead time, number of cross-module edits and handoffs, merge conflicts, incidents, latency/capacity, recovery time, and adapter exceptions. Keep the architecture if it passes and reduces change/operational cost. Redraw only the measured seam that fails. Kafka, Rust, and service extraction remain options with explicit switch conditions, not workstreams competing with the contracted launch.
