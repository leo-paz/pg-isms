# Raw evaluation output

Case ID: scenario-05

Reviewer ID: engineering-forward-001

## Ownership and protected outcome

`engineering-for-leverage` owns the ingestion, replay, reconciliation, and transfer-safety machinery. `shipping-and-iterating-products` owns live exposure: cohort, release gates, monitoring, support, rollback decisions, incident response, and restitution. Because authorization policy is already settled, governance need not reopen it; engineering must faithfully enforce it at the trust boundary. Security, privacy, legal, and payroll-compliance reviewers must be current gate approvers before any exposure.

The protected outcome is that no duplicate, forged, malformed, stale, or reordered input can produce an unauthorized, incorrect, or duplicate transfer, and that interruption cannot leave an untraceable or silently inconsistent payroll. Availability matters, but an ambiguous event should stop for reconciliation or human review rather than guess with payroll funds.

## Technical sequence

1. **Authenticate and validate at ingress.** Verify the provider signature over the raw body, timestamp and replay window, expected account/tenant, schema, size, and allowed event type before the event can affect payroll. Support secret rotation and least-privilege credentials. Treat network allowlists as defense in depth, not identity. Retain a tamper-evident audit record of rejected malformed, replayed, and forged probes without exposing secrets.
2. **Make receipt durable before acknowledgment.** Append the raw event, provider/event identity, receipt time, content hash, and verification result to a durable inbox. Enforce a unique provider-plus-event key; a duplicate is an auditable no-op. Acknowledge only after this record commits.
3. **Derive state deterministically.** Process an employer/payroll aggregate through explicit monotonic states. Do not assume arrival order. State transitions require the complete evidence defined by the settled authorization policy; missing, conflicting, late, or impossible transitions enter a review queue. Keep enough immutable input and versioned transformation metadata to replay the result deterministically.
4. **Reconcile rather than infer.** Fetch authoritative employer/provider state at cutoffs and after gaps, and reconcile both the calculated payroll and bank state. Delayed events may update the inbox, but they must not blindly reopen a completed transfer. Record every divergence and its disposition.
5. **Separate calculation from money movement.** Commit the payroll calculation, internal ledger entry, and a single transfer intent transactionally. Dispatch through an outbox with a deterministic bank idempotency key. The executor uses transfer-only credentials and cannot alter payroll inputs. On timeout or crash, query/reconcile the bank before retrying; never create a new intent merely because the response is unknown.
6. **Make recovery ordinary.** Checkpoint processing, replay the inbox into a clean state, and reconcile the replayed ledger and bank results. Provide a kill switch that stops new transfer intents while preserving received events and reconciliation. An ambiguous already-sent transfer is frozen and investigated, not “rolled back” by sending an opposite transaction.

Code ownership must be end to end: a named ingestion owner can test, deploy, observe, replay, and repair the pipeline; a named transfer owner owns bank integration and reconciliation; and the release DRI is the incident commander once customers or funds are exposed. Handoffs and escalation are in the runbook.

## Assurance gates before funds

Date the initial record 2026-07-14 and set the first gate review for 2026-08-04. Before testing, record expected peak payroll volume, the earliest settlement cutoff, recovery objective, unequal-error policy, and exact pass/redesign thresholds. Then run:

- provider and bank sandbox/certification tests;
- historical representative replay plus generated duplicates, delays, reorderings, malformed fields, replay attacks, bad signatures, tenant mismatches, and identifier collisions;
- a crash or network interruption at every durable transition and before/after every external call;
- load at a precommitted multiple of expected payroll peak, with completion before the real settlement cutoff; and
- restore, credential-rotation, kill-switch, reconciliation, and incident drills by the people who will be on call.

The release is blocked unless the full fault matrix produces zero unauthorized or duplicate transfer intents, every accepted input remains recoverable and auditable, every deterministic replay converges to the same ledger state, every injected external ambiguity is reconciled or held for review, and operators meet the recorded recovery threshold. Known hostile inputs must never reach transfer creation. Measure false holds separately: they can delay payroll and therefore require monitoring and a staffed, time-bounded review path, but lowering them cannot weaken the money-safety invariants.

## Release sequence

Run the complete pipeline in shadow mode against representative payrolls with transfer credentials disabled, compare calculations and decisions to the current authoritative process, and clear every discrepancy. Next complete bank sandbox or zero-value validation where supported, current security/privacy/legal/compliance review, and an independent approval of the runbook and audit trail.

Only after those gates pass should shipping schedule a small, explicit first live cohort. Live funds are not the correctness experiment: use already-qualified low-volume employers, per-employer and per-batch caps, dual human confirmation of the reconciled payroll, staffed monitoring through settlement, and enough calendar margin to fall back to the established manual or legacy payroll path before employees are affected. Predeclare stop conditions for any invariant violation, unexplained reconciliation difference, audit gap, missed cutoff, or monitor failure. Stopping prevents new transfers; support then reconciles all in-flight states and follows the prewritten incident and restitution plan.

Expand only after complete settlement and reconciliation, a blameless review, and a dated shipping decision. Engineering keeps the technical rollback and replay path; shipping controls exposure and expansion. If a safety invariant fails at any stage, redesign and repeat the sandbox/shadow gates rather than learning from a larger live payroll cohort.
