# Raw held-out output
Case ID: enterprise-factory-edge-foundation
Generator ID: engineering-heldout-generator-002

## Decision memo: foundation for the first factory deployment

**To:** CTO and deployment team
**Decision date:** July 14, 2026
**Decision:** Build the first deployment as a single-node, on-premises package using Docker and Postgres, with a narrow, optional cloud bridge. Do not commit four engineers for five months to Kubernetes or a general-purpose synchronization layer now.

### Why this is the right constraint to solve

The current evidence is a cloud prototype on synthetic data and one contracted partner offering limited staging access. The second prospect has supplied neither systems access nor deployment evidence, so it is not evidence of a repeated architecture need. The binding constraint is proving that the product can be approved, installed, operated, and useful inside one manufacturer's actual workflow despite data-residency rules, intermittent connectivity, and quarterly maintenance windows. A Kubernetes foundation does not remove that constraint.

The proposed Kubernetes project would consume 20 engineer-months before the team has observed a production-shaped workload, plant operating model, or second deployment. It also introduces orchestration and custom distributed-state failure modes. The familiar Docker/Postgres baseline can test the product-specific risks sooner and with fewer concepts. An undeployed spike, even if technically successful, will not count as field evidence.

Known facts are those stated above. Assumptions to confirm with the partner by August 14 are that it can provide a supported Linux host or VM, permits the proposed container and Postgres versions, and will initially use the product for observation or recommendations rather than autonomous equipment actuation. Company survival state, exact workload, availability target, host specification, Kubernetes proficiency, plant identity integration, and allowable outbound data are unknown. If acute survival is binding, reduce this plan to the shortest deployable proof rather than fund either foundation project.

### Bounded foundation

The package will contain the local ingest, optimization, operator-facing functions, and durable state required to remain useful with no cloud connection. It will use OCI containers on one host, a pinned Postgres release, versioned configuration and schemas, and scripted install, backup, restore, upgrade, and rollback. Kubernetes-specific APIs will not appear in application code.

The cloud bridge will be a separately replaceable adapter, disabled by default until the partner approves its data-flow inventory. It will send only explicitly allowlisted records or aggregates over outbound mutual TLS. A local durable outbox, immutable event identifiers, idempotent cloud consumers, transactional acknowledgement, checkpoints, bounded retries, and deterministic replay will make disconnect, duplication, interruption, and reordering ordinary test cases. The bridge will not be a generic bidirectional synchronization platform, and local product operation will not wait on it.

Preserve a portability seam through standard container images, a documented health contract, versioned event envelopes, database migrations that work independently of the orchestrator, and exportable Postgres backups. That leaves open a later move to Kubernetes, another on-premises runtime, or a fully disconnected package without paying for those branches now. There will be one end-to-end technical owner for install through recovery; ownership will not be split by service until field evidence reveals a stable seam.

The initial engineering budget is capped at two engineers for eight weeks to produce the deployable package, bridge, failure-test harness, security artifacts, and runbooks. This is a scope limit, not a delivery forecast; procurement can proceed in parallel and may still determine the calendar.

### Assurance and deployment gates

Before staging, obtain the partner's written acceptance of the architecture, host and network requirements, data-flow and residency map, identity model, support path, and update process. Supply an SBOM, dependency and vulnerability policy, signed artifacts, encryption-at-rest plan, least-privilege service accounts, secrets handling, audit logs, backup/restore procedure, patch policy, and a rollback package that does not require internet access. Security review and procurement approval are gates, not post-deployment chores.

Measure a representative staging workload using real, permitted plant data. Before the run, the partner and engineering owner will record the actual peak ingest rate and local response-time SLO. The package passes only if it:

- sustains twice the observed peak rate while meeting that local SLO, without an external network;
- survives a seven-day simulated outage and at least 100 forced disconnect/reorder/duplicate cycles with zero acknowledged-event loss and zero duplicate business effects;
- catches up within four hours of reconnection without impairing local operation;
- completes backup restore and previous-version rollback within 60 minutes each, performed from the runbook by an engineer who did not author it;
- operates for 30 consecutive staging days with at least 99.5% availability excluding partner-planned downtime, no severity-1 incident, and no residency-policy violation; and
- can be installed, diagnosed, updated, and rolled back within an approved maintenance window using the customer's supported tooling.

If seven days is shorter than the partner's documented worst credible isolation period, replace it before testing with that period plus 50%. Fault injection must include power loss during database writes, disk pressure, certificate expiry, corrupt or hostile input, clock skew, process restart, bridge replay, and an unavailable cloud endpoint. Log recovery time, manual steps, data loss, duplicate effects, and operator confusion, not only throughput.

This memo assumes the software does not directly command physical equipment. If that assumption is false, staging remains sandboxed or shadow-only until qualified plant-safety, security, privacy, and current legal/compliance reviewers approve it. Commands must be authorized, bounded, auditable, idempotent where possible, fail safe on disconnect, and require human confirmation until a separately approved safety case exists. The plant retains an immediate local disable path. The engineering owner owns the machinery and technical rollback; the shipping/product owner owns exposure gates, monitoring, customer support, incident coordination, and remedy for credible harm.

### Precommitted decision branches

**Keep and harden the single-node foundation** if the security and procurement gates pass and all staging thresholds pass. Continue it through the first production deployment, prioritizing operational defects and documented customer-stack fit. Review the decision on August 14, 2026 for environment confirmation, on January 15, 2027 for approval and deployment readiness, and after 30 staging operating days for measured results.

**Expand it without changing foundations** if the first site reveals additional connectors, data rules, or packaging variants but retains adequate single-node headroom. Add only capabilities demanded by an accessed workflow. Abstract shared behavior only after at least two deployed factories exhibit the same stable vocabulary and invariant; until then, tolerate small, explicit duplication.

**Evaluate Kubernetes or a multi-node design** only after two independent factories are deployed and measurement shows that the single-node design cannot meet a required availability, capacity, isolation, or independently deployable-service need. Start with a two-week, time-boxed comparison against the current baseline using the same workload and recovery suite. Adopt it only if it clears the existing gates and removes the observed limitation while reducing total delivery, support, and recovery cost after training, security review, observability, upgrades, and customer-cluster compatibility are included. Prospect interest alone is not a trigger.

**Reverse or replatform** if the partner rejects Docker or Postgres, the security review rejects the trust boundary, the package misses capacity or recovery thresholds after one bounded remediation cycle, or quarterly windows make the tested install/rollback procedure infeasible. Choose the smallest response supported by evidence: a partner-approved VM/appliance format for packaging constraints, a local-only mode for bridge constraints, or a measured HA design for availability constraints. Exportable data, versioned contracts, and standard containers are the retreat path.

Rejected for now are the cloud-only prototype, because it conflicts with connectivity and residency constraints, and the proposed Kubernetes/custom-sync foundation, because no deployed evidence shows a product-specific net advantage over the familiar baseline. This decision buys field evidence while preserving the option to change architecture once a real limitation—not an imagined future factory—earns the added machinery.
