# Six-week learning plan

Treat the dashboard requests as a signal to investigate, not yet as validated demand. The observed bottleneck is activation: imports fail and retries require managerial approval. Do not buy ads until users can reliably complete the core workflow.

- **Week 1 — Establish the baseline.** Instrument import attempts, failure categories, retry counts, approval delays, successful-import rate, and time to first usable candidate record. Review the four recordings and run failure-focused interviews with the two sandbox partners. Record what users did, not only what they requested.
- **Week 2 — Test the bottleneck diagnosis.** Reproduce the dominant failures with partner data. Prototype the smallest changes that could remove them: preflight validation, actionable error messages, safe self-service retries, or a clearly defined approval path. Set a baseline for both partners before changing the flow.
- **Weeks 3–4 — Run paired workflow trials.** Have each partner complete representative imports in the sandbox using the current flow and the changed flow. Observe sessions and measure import completion, time to completion, approval touches, retries, subsequent recruiter activity, and return use. Keep analytics-dashboard work out of scope unless an analytics gap blocks a real post-import task.
- **Week 5 — Seek costly commitment.** If activation improves, ask each partner for a concrete next step: a dated deployment plan, security review, signed pilot, or payment. Document objections and which promised actions actually happen. If activation does not improve, isolate the remaining failure mechanism and run one narrower test.
- **Week 6 — Decide.** Continue product investment if both workflow evidence and commitment strengthen; run one bounded follow-up if results are mixed but a specific falsifiable blocker remains; stop or reconsider the segment/workflow if imports still fail or partners will not commit after the blocker is removed. Release growth spend only after a defined activation threshold and at least one credible deployment or paid-pilot commitment.

## Decision record

Maintain one dated log with: hypothesis, expected observation, test and cohort, baseline, result, disconfirming evidence, confidence, decision, owner, and next review date. Separate reported demand (“30 directors asked”) from observed behavior (four sessions), product reliability evidence, and commitment evidence (currently no deployment or payment). Predefine thresholds before each test—for example, successful representative imports, materially lower completion time and approval touches, return use, and a dated commercial commitment—then record whether each threshold was met.

## Ownership handoffs

- **Founder/product:** owns the learning question, partner selection, scope, interviews, weekly synthesis, and final continue/iterate/stop decision.
- **Engineering:** owns failure instrumentation, reproduction, narrow reliability changes, and a written handoff of known failure modes and unresolved risks.
- **Customer success/research:** schedules and observes trials, captures workflow evidence, and verifies partner follow-through without translating requests directly into requirements.
- **Growth:** pauses the $60,000 campaign; helps recruit test participants and preserves channel hypotheses. Growth receives ownership only after product sets an activation gate and commercial proof gate, then runs a small capped acquisition test before any broader spend.
- **Partners:** provide representative sandbox data, named operators, scheduled sessions, and—if the workflow succeeds—a dated deployment or pilot decision.
