# 30-day plan

The 30-day goal is to learn whether the web notification flow reliably gets urgent exceptions acknowledged and resolved faster without disrupting the clerks’ high-frequency queue work. Do not block on the six-week rules-engine rewrite, run a broad campaign, or force all 600 clerks onto the new layout yet. Ship the smallest reversible version behind warehouse- and user-level flags, keep email as a fallback, and preserve the current queue layout and shortcuts wherever possible.

## Days 1–5: define the decision and protect the workflow

- Name one product manager as the accountable launch owner and agree on pre-launch success, expansion, pause, and rollback criteria.
- Capture baselines from the six warehouses: urgent exceptions created, missed or late acknowledgements, time to acknowledge, time to resolution, delivery failures, and the time/error rate for common keyboard-driven queue tasks.
- Observe a small sample of experienced clerks completing their top queue tasks. Treat shortcut behavior and task speed as compatibility requirements, not preferences.
- Split the web notification flow from the card-layout change if feasible. If they cannot be separated in this window, add a classic-layout option and make shortcut parity a release gate.
- Confirm event definitions and instrument exception created, notification sent/delivered/opened, acknowledged, assigned, resolved, email fallback, shortcut use, client errors, rollback, and support contacts.

## Days 6–10: make the thin release safe

- Productionize only the path already validated manually: urgent exception triggers, supervisor notification, acknowledgement, assignment, and a link into the existing queue. Use simple explicit rules for the paid-pilot use cases; record rules-engine gaps instead of rebuilding the platform first.
- Add per-warehouse and per-user feature flags, audit logs, idempotency, delivery monitoring, and a one-action rollback to email-only behavior.
- Run keyboard regression tests with representative clerks and browsers. The release cannot proceed if core shortcuts fail, focus order becomes unreliable, or common queue tasks materially slow down.
- Customer success confirms pilot contacts, escalation paths, training, and consent. Growth prepares pilot-specific material only; no broad campaign is scheduled.

## Days 11–17: paid-pilot release in parallel

- Launch to one paid-pilot warehouse first, during staffed hours, with email still active. Start with its supervisors and a small clerk cohort, then expand within that warehouse after 48 hours if delivery, acknowledgement, workflow, and error thresholds hold.
- Hold a daily 15-minute review of the funnel, incidents, clerk friction, and verbatim supervisor feedback. The engineering manager can pause or roll back immediately; no executive approval is required for safety actions.
- After two stable days, repeat with the other two paid pilots in staggered waves. Fix the smallest demonstrated blockers between waves.

## Days 18–24: test repeatability

- Offer the reversible web flow to the other three validating warehouses, still behind flags and still with email fallback. Expansion is based on pilot evidence, not the calendar.
- Compare each warehouse with its own manual-SMS and email baseline. Segment results by warehouse, role, urgency, browser, layout option, and new versus experienced users so aggregate gains do not hide clerk regressions.
- Interview at least one supervisor and two clerks per active warehouse. Ask about missed alerts, duplicate work, trust, shortcut failures, and cases where they reverted to email.
- Growth may draft a case study and narrow follow-up list, but publishes nothing until customers approve the claims and the evidence is repeatable.

## Days 25–30: decide and commit the next increment

Use a written review to choose one of three outcomes:

1. **Expand gradually** if urgent-alert acknowledgement and resolution improve meaningfully across warehouses, delivery is reliable, there are no severe incidents, and clerk task speed/error rates remain within the agreed compatibility bound.
2. **Iterate in place** if the alert value is clear but specific workflow or reliability issues remain. Keep successful cohorts enabled, fix the observed constraint, and run another measured wave.
3. **Roll back or stop** if alerts do not improve outcomes, trust is damaged, or the keyboard workflow regresses. Email remains intact, so stopping is cheap.

The rules-engine rewrite earns a separate proposal only if the month’s evidence shows that rule limitations—not delivery, adoption, or queue usability—are the binding constraint. A mandatory rollout to all 600 clerks is a later decision requiring demonstrated repeatability and shortcut/layout compatibility.

## Evidence and ownership

The primary outcome is the share of urgent exceptions acknowledged within the warehouse’s agreed response window. Supporting outcomes are median and tail time to acknowledge, time to resolution, missed exceptions, and repeated or duplicate work. Guardrails are notification delivery failures, severe incidents, false/duplicate alerts, email fallback use, support volume, clerk task completion time, shortcut failure rate, and queue error rate. Commercial evidence includes pilot activation, sustained weekly use, willingness to continue paying, and approval to serve as a reference. Set numeric thresholds from the captured baseline before the first release rather than choosing them after seeing results.

- **Product manager:** accountable for scope, success criteria, daily evidence review, and the day-30 recommendation.
- **Engineering manager:** owns release safety, feature flags, monitoring, incident response, and rollback authority.
- **Design/research:** owns clerk workflow observation, shortcut/layout compatibility, and structured interviews.
- **Data/analytics:** owns event quality, baseline comparison, segmentation, and the decision report.
- **Customer success:** owns warehouse readiness, training, feedback collection, and customer communications.
- **Pilot warehouse supervisor:** owns local escalation and confirms whether operational outcomes actually improved.
- **Growth:** owns only evidence-backed pilot messaging and a targeted expansion plan after the decision gate.
- **CEO:** resolves resource conflicts and accepts the agreed gates; does not override pause or rollback criteria during a live wave.
