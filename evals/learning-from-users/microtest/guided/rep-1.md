# Six-week learning plan

## Decision now

Do not build the larger dashboard and do not approve the $60,000 growth budget yet. Thirty requests are interest, not a diagnosis; the four observed sessions contradict the requested solution. The strongest evidence so far is workflow access from two companies, but sandbox access without repeated use, deployment, commitment, or payment does not validate demand.

For the next six weeks, the founder is the learning owner. Growth may recruit a bounded sample, but may not optimize channels. The test is whether import recovery and approval delay—not analytics visibility—cause abandonment.

## Learning record

| Field | Recorded decision |
|---|---|
| Product and stage | Enterprise recruiting SaaS; pre-demand-validation, with no deployment or payment yet. |
| Target segment | Recruiting teams evaluating the product that had a candidate-import failure in the last 30 days and require a manager to approve a retry. The unit of study is a recruiter plus that recruiter’s approving manager or budget owner. |
| Sample and rationale | Invite 12 of the 30 companies using a stratified list across team size and import source, seeking six qualified companies and a minimum of four with sandbox workflow access. Include the two current volunteers only if they meet the rule. This avoids treating the most available or enthusiastic prospects as the whole market. |
| Primary claim | For this segment, a failed candidate import followed by manager-gated retry creates enough delay that recruiters abandon evaluation; a pre-authorized, visible recovery path will produce faster successful imports and repeated use. |
| Causal rivals | Bad source data or mappings; repeated technical failure even after approval; poor retry notification; unclear ownership; general evaluation delay; analytics discoverability or missing reporting capability. |
| Disconfirming evidence | Recruiters still abandon after a successful pre-authorized retry; manager approval adds little time; the same files fail repeatedly for technical reasons; recruiters cannot complete real reporting tasks with the current analytics; or successful recovery does not lead to another import, a deployed pilot, or a paid commitment. |
| Evidence already observed | Thirty HR directors requested a larger dashboard. In four screen shares, recruiters could see analytics but abandoned when imports failed and every retry needed manager approval. Two companies offered sandbox data. Nobody has deployed or paid. The request and observed behavior conflict, and neither is yet validation. |
| Recruitment and consent | Growth sends neutral invitations from the founder’s inclusion list and schedules sessions. The founder obtains written consent for screen recording and sandbox-data use, states that participation is not a sales condition, and asks about a recent import event before describing a solution. |
| Risks and exclusions | Use synthetic or de-identified candidate data; exclude production PII, companies without a recent failure or approval gate, respondents who only offer opinions, and paid-ad leads. Stop for a privacy/security incident or production impact. Cap concierge work at 24 team-hours total so custom support does not silently become the product. |

## Calendar and test

Dates are assumed from July 15 through August 25, 2026.

| Week | Work and evidence |
|---|---|
| 1 — Jul 15–21 | Freeze dashboard and ad work. Instrument the sequence `import started → failure → approval requested → approval received → retry → successful import → next session`. Select the stratified invite list, collect consent, and capture each participant’s last real event, workaround, consequence, actor, approver, and buyer. |
| 2 — Jul 22–28 | Observe at least four recruiter-manager pairs reproduce a de-identified import and complete one real analytics task in the current product. Measure failure cause, approval latency, recovery time, assistance, abandonment, and analytics-task completion. Review the access gate on Jul 28. |
| 3 — Jul 29–Aug 4 | In sandbox only, run a within-company comparison with matched import files. Randomize the order of (A) the current manager-approved retry and (B) a concierge retry operating under written pre-authorization. Keep the dashboard unchanged. Log every manual step and confounder. |
| 4 — Aug 5–11 | Repeat the comparison on a second import cycle to distinguish novelty from repeated behavior. Observe whether the recruiter returns without prompting and whether the manager accepts the pre-authorization boundary. Review safety, causal rivals, and early repetitions on Aug 11. |
| 5 — Aug 12–18 | Run a third recovery/import where possible. After participants have experienced the workflow, ask the buyer for a 30-day deployed-pilot start date, named security/procurement step, and explicit paid price or budget—not general enthusiasm. Do not offer ad-subsidized usage. |
| 6 — Aug 19–25 | Analyze by company, preserve counterexamples, and separate workflow, analytics, and commercial evidence. On Aug 25, make one threshold-based decision and hand the record to the named next owner. |

### Thresholds and stop rules

- Access gate, July 28: at least four qualified companies provide de-identified sandbox workflow access and both recruiter and approver participation. If not, stop the comparison and return “insufficient behavioral access,” not “dashboard demand,” to opportunity choice.
- Causal threshold, August 18: in at least three of four observed companies, recruiters complete at least two separate imports; the pre-authorized condition succeeds within one business day at least 80% of the time, improves successful completion by at least 30 percentage points over the current path, and cuts median recovery time by at least half. At least 75% must also complete their real analytics task unaided; otherwise analytics remains a live rival.
- Demand threshold, August 25: at least three companies repeat the import workflow across two weeks, and either one pays for a deployed pilot or two sign paid-pilot commitments naming the user, buyer, price, start date within 30 days, and procurement/security next step. Sandbox activity alone does not pass.
- Stop immediately for material privacy, security, or production harm. Stop a company’s concierge test if recovery requires more than two staff-hours per import. Do not extend the six weeks merely because people remain positive.

## Ownership handoffs

| Result on Aug 25 | Next owner | Handoff |
|---|---|---|
| Access gate or causal threshold fails | Opportunity choice | Founder hands over the observations, failed claim, rivals, and segment limits. Reconsider the problem or segment; do not silently pivot to the dashboard. |
| Import-recovery claim passes, but repeated use and commercial threshold do not | Learning owner | Continue only a newly bounded deployment or willingness-to-pay test. Growth still does no channel optimization, and the $60,000 remains deferred. |
| Causal threshold passes and a minimal recovery specification is clear | Shipping/product owner | Build the smallest reversible import-recovery and approval change, with logging and rollback. Do not include a dashboard expansion unless separate behavior evidence passes. |
| Repeated use plus the demand threshold passes | Growth lead | Receive the exact segment, evidence, exclusions, buyer language, and observed conversion baseline. Growth now owns acquisition experiments; release budget incrementally rather than treating the original $60,000 request as pre-approved. |
| Analytics-task evidence defeats the primary claim | Opportunity choice, then learning | Compare analytics versus import-recovery directions explicitly and run a new falsifiable test. A feature request still does not authorize a build. |
| Material harm appears | Founder/security owner | Stop the test, contain the issue, document it, and require a safer sandbox protocol before any resumption. |
