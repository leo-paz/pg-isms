# 30-day decision

Keep the Python/Postgres monolith for the third-carrier launch. Do not introduce Rust, Kafka, a universal plugin framework, or per-connector microservices in this release. The single four-second result proves that the current path misses the latency contract in one test; it does not identify Python, Postgres, process boundaries, or queueing as the cause. Replacing the stack now would add unfamiliar deployment, debugging, observability, migration, and incident modes inside a six-week integration window.

Harden the existing ingestion path, measure it under a representative workload, and add one narrow carrier-adapter interface over the ordering, idempotency, and audit semantics that have been shared for eight months. Preserve an event-envelope seam so a broker can be inserted later without rewriting connectors, but do not operate that broker unless the familiar baseline fails a precommitted gate for a diagnosed reason.

This keeps the current customer-visible commitments as the planning baseline. It does not turn the date into permission to ship through a failed safety or contract gate; the release owner must escalate a failed gate rather than silently accepting it.

## Technical decision record

**Facts.** The company has eight people, three paying brokers, two live connectors, a signed third connector due in six weeks, and two uncommitted leads. The live connectors have shared ordering, idempotency, and audit behavior for eight months. One projected-40x test reported p95 delay of four seconds against a two-second contract. There is no controlled throughput, recovery, reordering, or operability evidence yet. The team is proficient in the current stack.

**Assumptions to verify by Day 3.** The company is not default-dead or in an acute survival event; the two-second measure is receipt-to-durable-domain-effect rather than HTTP acknowledgement; the carrier can provide sandbox traffic, signatures, retry rules, sequence semantics, and representative payloads; and durable raw-payload retention is permitted by current customer, security, privacy, and compliance requirements. If survival is binding, that decision takes precedence over this architecture work. If the contractual timer or data-retention rules differ, the workload and storage design change, not the release gate's authority.

**Stage and constraint.** This is early, revenue-bearing enterprise integration work with weeks-long deployment evidence, meaningful duplicate/out-of-order error cost, and a reversible software change. The binding technical constraint is an unexplained ingestion-delay failure plus missing reliability evidence, under a six-week delivery constraint. It is not a demonstrated need for a new language, broker, or service boundary.

**Falsifiable leverage claim.** A profiled and tuned Python/Postgres path should process the representative 40x mix below the contract, preserve all shared invariants through interruption and reordering, and remain operable by the current team. It should deliver the signed connector within six weeks with fewer concepts, deployment units, handoffs, and failure modes than the proposed rewrite.

**Candidate comparison.**

| Candidate | Limitation it would remove | Lifecycle cost and decision |
|---|---|---|
| Profile and harden Python/Postgres | Known query, lock, worker, or indexing bottlenecks; missing durable replay/visibility | Uses current proficiency, deployment, libraries, security controls, and on-call knowledge; lowest migration and exit cost. Choose now. |
| Python plus Kafka | Postgres-backed dispatch cannot meet measured sustained throughput/recovery after bounded tuning | Adds procurement/hosting, partitions and ordering keys, schema compatibility, dual-system observability, replay controls, and broker operations. Keep as a conditional branch, not a Day-1 dependency. |
| Rust on the hot path | Profiling shows parsing/validation CPU is the dominant bound and a production-shaped prototype materially improves it | Adds language proficiency, build/debug, hiring, deployment, library, security, and maintenance costs. Reject without that evidence. |
| Per-connector microservices and universal plugins | Repeated independent deployment or isolation needs overwhelm shared ownership | Duplicates shared invariants and multiplies network calls, deployments, dashboards, incident surfaces, and coordination. Two leads are not requirements. Reject for this launch. |

The Day-12 branch is precommitted: stay on Postgres if the tuned baseline meets the performance and fault gates. If Postgres dispatch remains the measured bottleneck after query-plan, index, batching, lock-contention, and worker-concurrency work, run a time-boxed Python/Kafka spike against the identical harness while the release path continues. Adopt it only if it passes every gate with material headroom and the team can deploy, observe, recover, and remove it. If Python CPU is instead the dominant bound, profile a bounded Rust worker; do not combine that experiment with Kafka or service decomposition. No candidate earns adoption merely by improving an undeployed microbenchmark.

Record the final evidence and ratify or amend this choice on Day 30. Review again 30 days after the third carrier reaches production, using p95/p99 delay, backlog age, recovery time, incidents, connector lead time, handoffs, conflicts, and on-call load. That review may keep, redraw, separate, or retreat from the seam.

## Architecture and abstraction

Use one deployable and one Postgres ownership boundary:

1. The carrier endpoint validates request size, signature, schema version, and required identifiers. In one transaction it stores an immutable inbound envelope and receipt audit record before acknowledgement. The envelope includes carrier, external event ID, ordering key/sequence when available, receive time, schema version, payload location/hash, and trace ID.
2. Existing monolith workers claim envelopes in bounded batches, call the carrier adapter, and apply the normalized domain operation plus processing audit state transactionally. A unique carrier/event identity prevents duplicate domain effects. Where a carrier lacks a trustworthy event ID or sequence, the adapter must declare and test the existing deterministic fallback; a content hash must not be treated as universally collision-free.
3. Ordering is scoped to the existing business ordering key, not made global. Missing predecessors are parked for bounded retry/reconciliation. Duplicate, delayed, reordered, and interrupted delivery must converge to the same domain state and complete audit trail. Poison events enter a visible quarantine rather than blocking unrelated keys.
4. Raw envelopes and state transitions support deterministic replay and reconciliation after a crash or pause. Replay uses the same idempotent processing path; operators do not patch business tables manually.

If the current system already provides an equivalent durable inbox, extend it rather than replacing it. Otherwise add the schema and worker changes with backward-compatible migrations. Tune from profiles: query plans and indexes first, then batch size, connection use, worker concurrency, and hot-key contention. Do not acknowledge receipt before the durability point assumed by the carrier retry contract.

The only new abstraction is a statically registered `CarrierAdapter` with pure, typed operations equivalent to `verify`, `decode`, `event_identity`, `ordering_metadata`, and `normalize`. Connector code owns signature and payload quirks and returns normalized events; the shared engine alone owns durable receipt, idempotent effects, ordering, retry/quarantine, audit, replay, and metrics. Characterization tests for the two live connectors freeze current behavior before extraction, and the signed third connector supplies the third concrete use. There is no dynamic loading, plugin discovery, connector-owned queue, separate database, or connector service.

Every adapter must pass one conformance suite covering valid fixtures, authentication failure, malformed and oversized input, identity collisions, duplicate delivery, all relevant reorderings, missing predecessors, retry, interruption, replay, quarantine, and audit completeness. Permit localized duplication if a carrier does not share a stable concept. Retreat from the interface if it causes expanding conditionals, additional call-site concepts, cross-adapter coordination, or slower connector delivery without reducing defects.

## Bounded evidence gate

By Day 4, freeze a versioned workload from redacted/reviewed live fixtures plus third-carrier sandbox fixtures, with the projected carrier/event mix and payload-size distribution. Run a 60-minute 40x sustained test and a 15-minute 80x burst on production-shaped infrastructure. Measure from durable receipt to durable domain effect, as well as acknowledgement latency, throughput, queue age, DB CPU/IO, locks, connections, worker CPU/memory, retries, and per-ordering-key skew.

The ingestion technical owner owns the harness and signs the results on Days 8, 12, and 26. Day-30 release readiness requires all of the following precommitted thresholds:

- At 40x, p95 receipt-to-effect is at most 1.5 seconds, leaving margin below the two-second contract; at the 80x burst it remains below two seconds, backlog stays bounded, and it drains within ten minutes after returning to 40x.
- There is zero lost accepted envelope, zero duplicate domain effect, deterministic final state for the enumerated reorder/duplicate permutations, and a complete, queryable audit trail.
- Worker termination, mid-batch termination, deploy interruption, and a ten-minute database outage recover through replay without manual data edits. After service restoration, 40x traffic is accepted within two minutes and the backlog drains within 15 minutes.
- Malformed, oversized, unauthenticated, replayed, and poison inputs remain within their ordering key/tenant blast radius; secrets and database roles are least-privileged; quarantine and replay actions are authenticated and audited.
- A second engineer, using only dashboards and the runbook, can identify a stuck or hot key, distinguish carrier rejection from internal backlog, quarantine one event, replay safely, and reconcile counts within 15 minutes.

Run the load test once before optimization to preserve the failing baseline, then after each material change. Fault injection must include duplicates, delay, reorder, missing sequence, worker kill, deploy, connection exhaustion, database outage, and carrier retry storms. Reconcile accepted carrier IDs, envelope IDs, normalized operations, domain effects, and audit rows after every run. A staging or carrier sandbox run is necessary but not sufficient; before exposure, replay a reviewed production-shaped sample and complete current security, privacy, compliance, and customer-stack checks. A spike that has not been deployed and operated on production-shaped infrastructure is not field evidence.

## 30-day execution and ownership

**Days 1-3 — decide and map.** Name one third-carrier launch DRI who can change, test, deploy, operate, and roll back the entire endpoint-to-domain-effect surface. Document the contract timer, current data flow, ordering keys, transactional boundaries, idempotency keys, audit states, carrier retry behavior, sensitive fields, and all downstream effects. Obtain carrier sandbox/workflow access and fixtures. Product/Support confirm the unchanged external commitment and name the release owner; they do not redefine technical pass criteria.

**Days 4-8 — establish evidence.** Add trace IDs, delay/backlog/error metrics, query/lock profiling, and the versioned harness. Run and retain the failing baseline, throughput test, reorder simulation, recovery faults, and operator exercise. On Day 8, publish the diagnosed bottleneck and the smallest change expected to remove it.

**Days 9-15 — harden the familiar baseline.** Make the profiled index/query/batch/concurrency changes and add or complete durable inbox, idempotency, audit, quarantine, and replay behavior. Run the Day-12 branch gate. Do not let a Kafka or Rust spike consume the connector's critical path. Use backward-compatible schema expansion and rehearse migration and rollback.

**Days 16-21 — extract only proven sameness.** Add characterization tests, extract the narrow adapter, migrate the two live connectors behavior-preservingly, and implement the third adapter behind a per-carrier processing flag. Run all three through the same conformance and representative-replay suites. If extraction changes live outputs, revert it and ship the third adapter with localized code rather than force the framework.

**Days 22-26 — production-shaped assurance.** Shadow or sandbox the third connector without customer-visible effects, compare normalized output and audit records, repeat load and fault gates, rotate secrets, verify least privilege, and have the secondary engineer execute the runbook. Finish dashboards, alerts, migration timing, capacity estimate, and reconciliation tooling.

**Days 27-30 — decision and handoff.** Freeze nonessential changes, run the complete gate on the release candidate, record candidate results and rejected alternatives in the decision record, and hold a go/no-go handoff with engineering, Product, and Support. Deliver a release-ready build and a staged Days 31-42 exposure plan; do not introduce another architecture migration during that window.

The launch DRI owns code, schemas, invariant/conformance tests, technical monitoring, replay tooling, and technical rollback. A named secondary reviews changes and proves the runbook, avoiding a single-person operating surface. The on-call incident lead owns diagnosis and recovery once exposed. Product/Support's release owner owns customer-visible exposure, customer communications, canary progression, support coverage, exposure rollback, and incident/restitution workflow; engineering supplies the gates and executes technical rollback. This assigns end-to-end responsibilities without inventing new teams or reporting lines.

## Release handoff and rollback

The handoff packet contains the signed decision record; fixture and workload versions; test results; capacity envelope; schema and application deployment order; carrier configuration and secret-rotation record; dashboards and alert thresholds; conformance report; open risks; carrier contact/escalation path; reconciliation report; and a timestamped runbook for pause, replay, quarantine, rollback, and recovery.

The release sequence is expand schema, deploy compatible readers/writers, enable durable intake with effects disabled for the third carrier, shadow and reconcile, then enable effects for the smallest carrier-approved account/event slice. Increase exposure only after a full observation window with passing latency, invariant, and audit metrics. If carrier traffic cannot be safely segmented, use sandbox/shadow assurance followed by a single feature-gated activation with staffed monitoring and immediate pause capability.

Pause third-carrier effects immediately on any lost accepted envelope, duplicate domain effect, irreconcilable ordering divergence, audit gap, authentication bypass, or cross-tenant effect. Pause progression when p95 exceeds two seconds for five minutes, backlog drain exceeds the tested bound, quarantine grows unexpectedly, or operators cannot reconcile the stream. Technical rollback disables processing for that carrier while retaining durable envelopes, rolls workers back to the last compatible version, and replays through the idempotent path after remediation. Exposure rollback and customer communication belong to the release owner. Existing live connectors remain on their last characterized path unless the release candidate has passed behavior-preserving replay and rollback rehearsal for them.

This plan preserves the useful option: if measured Postgres dispatch, Python CPU, or connector coupling later becomes the proven predecessor limitation, the durable envelope, typed adapter, conformance suite, and replay harness let the team evaluate Kafka, Rust, or a service boundary one at a time against the same evidence without committing the launch to all three bets.
