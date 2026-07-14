The current evidence points to an activation failure, not a discovery or acquisition problem. I would freeze the dashboard and ad proposals for six weeks and use the two sandbox partners to learn whether reliable imports and fewer approval loops get recruiters to a first successful workflow.

## Six-week learning plan

**Week 1 — establish the funnel and reproduce the failure.** Define the learning question: “If candidate imports succeed without repeated manager intervention, will a recruiting team complete a useful workflow and return?” Instrument import start, import failure reason, retry request, approval wait, successful import, first completed recruiter task, and return use. Replay the four sessions with logs, reproduce the dominant failures, and interview the two sandbox partners about what data they can safely share and what a successful trial would mean.

**Week 2 — remove the narrowest blocker.** Fix the most common import failure and create a safe self-service retry for recoverable errors, with an audit trail and escalation for risky cases. Do not broaden analytics. Confirm in internal tests that representative files import and retries do not corrupt or duplicate records.

**Weeks 3–4 — run two observed sandbox pilots.** Give each partner a defined dataset and task. Observe the first import live, then let recruiters work without coaching. Review logs and conduct short follow-ups after 24 hours and one week. Record where they stop, who must intervene, whether they complete the intended task, and whether they return. Ship only fixes tied to observed blockers.

**Week 5 — test the next constraint.** If imports are reliable but use still stops, investigate the next observed bottleneck. Show a lightweight analytics sketch only if recruiters complete the core workflow and still cannot make a decision because specific information is missing; do not treat the thirty feature requests as proof of priority.

**Week 6 — decide.** Continue investing in import/retry reliability if both partners can import successfully, complete the target workflow, and return with materially less support. Test a narrowly specified analytics change only if the activation path works and repeated observation ties a missing metric to a blocked decision. Revisit acquisition only after activation is repeatable; otherwise stop the ad spend and document the unresolved failure.

## Decision record

Create one dated record with: decision owner; question being tested; current observations; assumptions; instrumentation and pilot design; success, failure, and safety thresholds; decision date; outcome; and links to session notes and logs. Initial entry: defer the $60,000 ad purchase and large-dashboard build; prioritize import reliability and self-service retry. Evidence: users can already reach analytics, but imports and approval waits stop them; no deployment or payment yet. Confidence is moderate because the pattern appeared in four sessions but only two sandbox pilots are available. Reopen the decision after week six or sooner if both pilots hit a safety problem.

## Ownership handoffs

- The founder owns the learning question, partner commitments, weekly synthesis, and the week-six product decision.
- The growth lead owns funnel instrumentation and reporting, but keeps the ad budget uncommitted until the activation threshold is met.
- Engineering owns import diagnostics, the recoverable-retry path, auditability, and incident response; it hands a tested pilot build and known-limitations note to customer success.
- Customer success or the founder owns pilot setup, consent and data-handling checks, observation, and follow-up notes; issues are handed back to engineering with logs and reproduction steps.
- The manager or security owner at each partner approves the sandbox scope and risky exceptions, not every recoverable retry.
- At the end of each week, the founder records what changed, assigns the next owner and due date, and explicitly accepts, rejects, or defers new dashboard requests.
