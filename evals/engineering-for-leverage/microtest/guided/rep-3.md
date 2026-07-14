# 30-day technical decision

## Decision record

**Facts.** This is an eight-person, early-revenue integration SaaS with three paying brokers, two live carrier connectors, a third signed carrier due in six weeks, and two uncommitted leads. Ordering, idempotency, and audit behavior have been shared and stable for eight months. The only capacity evidence is one 40x load test with p95 ingestion delay of four seconds versus a two-second contract. Throughput, recovery, reordering, and operability remain untested.

**Assumptions to verify on day 1.** The company is not in acute survival mode; “ingestion delay” means webhook receipt to committed customer-visible state; 40x is a credible projected peak rather than a sustained average; and the third carrier can provide a sandbox, signed sample payloads, and a launch contact. If survival is binding, the CTO should freeze architecture work beyond the minimum launch and reliability fixes.

**Binding constraint.** The constraint is missing evidence about the familiar pipeline under representative load and failure, not a demonstrated Python, Postgres, or team-topology limit. Errors are costly: loss, duplication, reordering, or an incomplete audit trail can corrupt broker workflows. Most proposed changes are technically reversible, but the carrier integration and customer rollout have long evidence latency and contractual consequences.

**Choice through launch.** Keep a modular Python/Postgres monolith. Profile and tune the measured bottleneck, add bounded worker capacity or a durable Postgres-backed inbox only if the tests require it, and implement carrier three behind the same shared ingestion core. Do not adopt Rust, Kafka, connector microservices, or a universal plugin framework in this launch window.

This preserves a valuable option: the ingress-to-canonical-event boundary can later feed Kafka or another queue without changing carrier adapters or domain processing. That option is not exercised unless the familiar baseline fails precommitted tests after bounded tuning, or production evidence shows a need for independent retention, fan-out, replay, or scaling that Postgres cannot meet economically.

**Why the alternatives lose now.** Rust may help only if profiling proves CPU or memory safety is the bottleneck; today it adds proficiency, hiring, debugging, build, deployment, observability, security-patching, and migration costs without solving ordering or recovery by itself. Kafka supplies durable-log capabilities, but adds procurement, operations, partition-key semantics, dual-system observability, incident modes, and exit costs before those capabilities are shown necessary. Per-connector services would duplicate shared invariants and increase deployments, handoffs, and incidents for an eight-person team. A universal plugin framework speculates from two leads; three real connectors justify a narrow adapter contract, not a general extension platform.

Review this decision on day 10 and again 14 days after carrier-three launch. The CTO is decision owner; the ingestion DRI supplies evidence. Record measured p50/p95/p99, maximum sustainable rate, backlog age and drain time, invariant failures, recovery time, operator steps, engineering time, defects, and lifecycle cost estimates for each branch.

## Target architecture and abstraction boundary

Use one end-to-end ingestion path:

`authenticated webhook -> carrier adapter -> durable receipt -> shared ordered/idempotent processor -> domain transaction + audit -> customer-visible state`

- Each carrier adapter owns only authentication/signature verification, schema validation, and translation into a versioned canonical event. Preserve the raw payload or a compliant reference plus carrier, tenant, event ID, ordering key, received time, schema version, and trace ID.
- The shared core owns deduplication keys, per-business-key ordering, transaction boundaries, retry policy, audit records, reconciliation, and deterministic replay. Those are the repeated, stable semantics; they must not be reimplemented in adapters.
- Define an adapter interface no broader than `verify`, `parse/validate`, and `normalize`. Carrier three must pass the same conformance suite as the two live connectors: valid samples, malformed and unauthorized input, duplicate delivery, out-of-order delivery, retry, interruption, replay, and audit completeness.
- Keep the interface in-process. Do not make a network boundary where the product/data seam is not yet independently changing or scaling.
- Prefer the current synchronous/durable path if it passes. If profiling shows coupling between request handling and processing causes the latency failure, introduce a Postgres inbox with a unique idempotency constraint, explicit state transitions, bounded retries, dead-letter/quarantine state, and workers claiming rows safely. Acknowledge only after durable receipt. Partition work by the real ordering key; never assume global ordering.
- Make replay idempotent and scopeable by tenant, carrier, time range, and ordering key. Reconciliation compares durable receipts with processed/audited outcomes and reports gaps rather than silently repairing them.

Retreat from the adapter abstraction if carrier three repeatedly needs exceptions in the shared interface, call-site count or concepts rise, or conformance logic becomes more complex than explicit connector code. Redraw or separate a runtime boundary only if measured lead time, merge conflicts, independent scaling, failure isolation, or incidents improve enough to exceed the new coordination and operational cost.

## Precommitted evidence gate

By day 3, freeze a representative workload from production distributions: request rate, payload sizes, carrier mix, tenant skew, ordering-key cardinality, duplicate/retry rate, and burst shape. Remove or synthesize sensitive data. Run at projected 40x peak for 60 minutes, plus a 2x-peak 10-minute burst, against a production-like database and deployment shape.

Pass thresholds, agreed before tuning:

- receipt-to-committed-visible-state p95 at or below 1.5 seconds and p99 at or below 2 seconds at 40x, leaving contract margin;
- sustained processing at or above offered 40x load with no unbounded backlog, and the burst backlog drained within 10 minutes;
- zero lost events, duplicate domain effects, per-key ordering violations, or audit gaps across duplicates, delayed delivery, and randomized reordering;
- process restart, mid-transaction kill, database failover/reconnect, and deployment interruption recover automatically with no invariant violation; normal service resumes within five minutes;
- an on-call engineer can detect a stuck key or growing backlog, identify the carrier/tenant, quarantine safely, and replay/reconcile it from the runbook within 15 minutes;
- dashboards and alerts cover ingress rate/errors, oldest backlog age, processing latency, retry/quarantine counts, invariant failures, and reconciliation gaps.

If the baseline passes, stop architectural work. If it misses, profile query time, locks, connection pools, transaction scope, indexes, serialization, and worker saturation; make the smallest change and rerun the identical suite. If bounded Python/Postgres tuning still cannot pass by day 10, evaluate a managed queue/Kafka behind the preserved seam with the same tests and a written migration/rollback cost. Consider Rust only after a profile attributes the miss to code execution and a representative spike demonstrates material end-to-end advantage, including deployment and debugging time. No candidate wins on an undeployed benchmark alone.

## Ownership

- **Ingestion DRI:** owns the HTTP edge, adapter contract, shared invariants, storage, conformance/load/fault tests, dashboards, runbook, replay tooling, and ingestion incidents end to end. This is one accountable surface, not ownership split by connector.
- **Carrier-three implementer:** owns its translation and fixtures, works inside the adapter boundary, and cannot fork ordering, idempotency, audit, or retry behavior. The ingestion DRI reviews and operates the result.
- **Platform/operations partner:** validates production-like deployment, database capacity, secrets, alerts, restore/failover behavior, and vendor/procurement implications. With eight people, this may be a role rather than a separate team.
- **Security/privacy reviewer:** signs off on webhook authentication, secret rotation, input limits, tenant isolation, raw-payload retention/redaction, least-privilege database access, audit access, and denial-of-service blast radius.
- **Release owner:** owns customer exposure, carrier coordination, monitoring window, support staffing, customer communication, rollout pause, and exposure rollback. Engineering owns the technical fallback. Support owns neither architectural acceptance nor an unsupported promise.

## 30-day execution and release handoff

**Days 1-3 — contract and observability.** Confirm survival state, the contractual latency clock, projected traffic model, carrier-three workflow, security/procurement needs, and current rollout commitments. Name the ingestion DRI and release owner. Capture the architecture/data seams and current failure behavior. Add missing trace IDs and measurements without changing customer behavior; freeze the workload and thresholds above.

**Days 4-7 — baseline and failure evidence.** Run load, duplicate, reorder, replay, restart, database interruption, and operator drills on the current monolith. Profile the four-second path. Produce a short evidence table and select only the smallest corrective branch: query/index/transaction/worker tuning, or durable inbox if request/processing coupling is proven.

**Days 8-10 — decision gate.** Implement the bounded fix, rerun the same suite, and hold the CTO gate. Passing means architecture freeze through launch. Failure means a time-boxed alternative spike behind the seam; it does not authorize a universal framework, connector services, or a language rewrite. Publish the decision, rejected alternatives, remaining uncertainty, rollback, and owner.

**Days 11-18 — carrier three.** Build the narrow adapter and fixtures. Run the complete conformance suite and representative replay with signed carrier samples. Exercise reconciliation and deterministic replay. Perform security/privacy review and validate sandbox workflow, rate limits, error responses, secret rotation, supportability, and customer-stack fit.

**Days 19-23 — production-like release candidate.** Deploy dark with the connector disabled. Run the 40x and fault suite in the release topology, verify dashboards/alerts and database headroom, restore from backup where feasible, and have a second engineer execute the runbook. Fix only launch blockers; keep architecture frozen.

**Days 24-27 — controlled exposure rehearsal.** In the carrier sandbox or an approved shadow mode, process end-to-end traffic without updating customer-visible state, compare normalized results and audit records, and reconcile every receipt. Then run a tightly scoped canary with the signed carrier and an approved broker account if contractual and privacy terms allow. Any loss, duplicate effect, ordering violation, audit gap, p99 breach, or unrecoverable backlog is an automatic pause.

**Days 28-30 — handoff.** Release owner, ingestion DRI, support, security, and the carrier contact sign one checklist: thresholds passed on the release build; carrier conformance passed; secrets and contacts current; dashboards and paging live; capacity and database limits documented; reconciliation clean; runbook exercised; feature flag tested; schema change backward-compatible; and incident roles scheduled.

The technical rollback is to disable carrier-three exposure while continuing to durably retain or explicitly reject receipts according to the carrier contract, then replay after correction. Do not silently accept and drop. The exposure rollback is owned by the release owner, who pauses the canary, informs support/carrier/customer contacts, and preserves current commitments for the two existing connectors. Keep the previous compatible code path deployable until reconciliation is clean and the monitoring window closes.

Fourteen days after launch, review latency, backlog, invariant failures, incidents, operator load, connector lead time, handoffs, and change conflicts. Keep the modular monolith and narrow seam unless measured evidence crosses the recorded switch condition; delete unused framework scaffolding and retreat from abstractions that increased concepts or coordination without leverage.
