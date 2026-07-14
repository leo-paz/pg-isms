# Raw forward output
Case ID: scenario-05
Reviewer ID: shipping-forward-001

## Ownership and current gate

The need has enough evidence to enter product shipping: twelve firms supplied workflow data, four completed two manual-service cycles, and two made a paid-pilot commitment. Learning should preserve the unresolved hypotheses and predefined interpretation thresholds, but shipping now owns the user-visible artifact, pilot exposure, monitoring, support, and fallback.

Engineering for leverage owns the internal event bus and any migration machinery. Replacing it is not the primary workflow and should not block the pilot unless a bounded reliability test shows the current bus cannot meet the notification’s delivery, isolation, audit, or data-integrity gate. If a narrow adapter, retry queue, or idempotency guard meets that gate, build that and defer the broad replacement.

Growth may recruit the already-defined wholesaler segment into the bounded pilot under the existing evidence plan. It should not run a broad lead-generation campaign before the released workflow demonstrates use: manual service and paid intent validate the problem and willingness, but not yet activation, retention, or reliable delivery of the product. Pricing, packaging, payer, and sales-economics decisions belong with business-model design.

## Smallest useful release

Release one complete job: when an already-defined time-sensitive invoice exception occurs, notify the designated approver in time to act and take them directly to the existing approval action.

The first version should include:

- ingestion of only the validated exception type from the existing system;
- one configured approver and one channel, assumed to be email unless pilot data identifies another required channel;
- invoice identity, exception reason, deadline, and a secure link to the existing approval screen;
- delivery status, bounded retry, deduplication, and an operator-visible audit trail;
- acknowledgement or approval-state feedback so the team can tell whether the alert led to action;
- a manual resend/escalation and a documented return to the manual notification service.

Defer a rules builder, multiple channels, broad analytics, generalized workflow automation, and wholesale event-bus replacement. Before release, verify recipient authorization, tenant isolation, link security, privacy, idempotency, deadline/time-zone handling, and that duplicate, stale, or misdirected alerts cannot silently create approval errors.

## Pilot and evidence loop

Start with the two paid-pilot firms, supervised by a named release owner and support owner. Shadow the first exceptions against the manual service, then send live notifications with the manual process available as fallback. After one clean cycle, add the other two firms that used the manual service. Because the workflow is monthly, use two monthly cycles as the minimum trustworthy evidence window rather than imposing an arbitrary weekly success decision; inspect delivery and incidents continuously and review outcomes after each cycle.

Track eligible exceptions, alerts generated, delivery latency, delivery failures, duplicates, wrong recipients, acknowledgement, approval before deadline, exceptions still missed, manual fallback, repeated use, support effort, and any privacy or authorization harm. Compare each firm with its manual-service baseline and account for exception volume, approver absence, holidays, and changes in invoice mix.

Proposed thresholds, explicitly assumptions to agree with the pilot firms before launch:

- **Operational pass:** every eligible exception is either delivered within five minutes or visibly escalated to the operator; zero wrong-tenant or wrong-recipient alerts; zero unbounded duplicates; and all failures are recoverable through the manual fallback.
- **Use/outcome pass:** across two monthly cycles, at least three of four firms repeatedly use the workflow and at least 80% of notified exceptions are acknowledged or resolved before their deadline, with a clear improvement over each firm’s manual baseline.
- **Change:** alerts arrive but are not acted on, or failures cluster in one step. Test the smallest discriminating change—recipient mapping, message content, timing, or action-link friction—without broadening the product.
- **Pause/rollback:** any cross-tenant disclosure, unauthorized approval path, silent missed exception, unreconciled duplicate, or failure that could cause material invoice loss. Stop live alerts for the affected firm, resume the manual service, investigate, and re-pass the relevant gate.
- **Stop/return to learning:** reliable alerts are delivered but firms still do not act or repeat use after two cycles. Return the named uncertainty about whether notification changes approval outcomes; do not answer weak use with more channels or a lead campaign.

## Handoff gates

Shipping remains owner through the bounded release. The bus replacement stays with engineering for leverage and is justified only by measured constraints or broader internal leverage, not by the desire to postpone user evidence. Once one defined wholesaler segment passes the product-use/outcome threshold and the paid commitment persists, hand channel acquisition, activation, retention, and expansion to growth while shipping continues to own visible rollout. Broader acquisition is gated on released-workflow evidence, and broader rollout is separately gated on the operational, privacy, and harm thresholds above.
