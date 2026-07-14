# Six-week learning plan

Treat the request for a larger dashboard as a hypothesis, not the roadmap. The observed failure is earlier in the journey: imports fail, retries require approval, and nobody has reached deployment or payment. Pause the $60,000 acquisition spend until the team can reliably activate sandbox users.

## Weeks 1–2: establish the failure and the baseline

- Product owns one learning question: “If importing and retrying become reliable, will a customer complete setup, return, and commit to a pilot?”
- Engineering instruments import attempts, failure causes, retry requests, approval latency, successful completion, dashboard use, and return sessions. Record time from first import attempt to usable candidate data.
- Customer success schedules observed sandbox sessions with the two data-sharing companies and invites a small, varied subset of the other directors. Watch users import real-shaped data and narrate their expectations; do not lead with dashboard concepts.
- Product and engineering reproduce every observed failure and separate data-quality errors, integration defects, and approval-policy delays.

## Weeks 3–4: run the smallest useful experiment

- Engineering ships a sandbox-only slice: preflight validation with actionable errors, safe resumable imports, and automatic retry for low-risk failures. Preserve an auditable escalation path for failures that truly require approval.
- Customer success gives each partner the same short import task and support window. Product compares the result with the week-one baseline.
- Success measures are import completion rate, median time to usable data, retry recovery rate and latency, completion without staff rescue, a second independent session, and willingness to schedule a deployment/pilot conversation.
- The growth lead may interview prospects and improve message clarity, but should not buy traffic during this experiment.

## Weeks 5–6: test commitment and decide

- Repeat the flow with fresh datasets and at least two additional willing prospects if available. Ask for a concrete next step: named implementation owner, deployment date, security review, or paid/time-bounded pilot.
- Interview dashboard requesters only after a successful import. Ask what decision they cannot make with the current analytics, then prototype only the most repeated decision-critical gap.
- At the end of week six, choose one outcome: scale the reliability fix and begin a small acquisition test; continue a narrowly defined reliability experiment; or stop and reassess the customer/problem if reliable activation still produces no commitment.

## Decision record

Maintain one dated record with: decision owner, hypothesis, observation or dataset, baseline, change tested, participant and dataset characteristics, quantitative results, direct behavioral evidence, confounders, and next decision. Precommit to these thresholds:

- Proceed to a small paid-acquisition test only if both sandbox partners complete imports without staff intervention, recovery is materially faster than baseline, at least one repeats the workflow, and at least one makes a concrete deployment or pilot commitment.
- Extend the reliability experiment only when failures are understood and the next test is smaller and diagnostic.
- Do not enlarge the dashboard unless successful users repeatedly identify the same missing decision and use a prototype to make it.

Record contrary evidence as prominently as positive evidence. Ads remain a separate, later test; an acquisition test must have its own budget cap, channel hypothesis, activation metric, and stop date.

## Ownership handoffs

- **Product lead:** owns the learning question, participant mix, experiment protocol, decision log, and week-six go/no-go decision.
- **Engineering lead:** owns instrumentation, failure taxonomy, sandbox fix, data safeguards, and a written readiness handoff to customer success.
- **Customer success/research:** owns recruiting, consent and data handling, observed sessions, support notes, and commitment follow-up; hands coded observations to product within one business day.
- **Growth lead:** owns prospect interviews now and receives an acquisition-readiness handoff only after the activation threshold passes; then proposes the capped channel test instead of receiving the full $60,000 by default.
- **Executive sponsor:** resolves cross-functional blockers and approves any spend, but does not override the precommitted evidence thresholds without documenting why.
