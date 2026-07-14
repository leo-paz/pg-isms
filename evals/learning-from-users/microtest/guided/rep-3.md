# Six-week learning plan

Assumed calendar: Monday, July 20 through Friday, August 28, 2026.

## Learning record

**Product, stage, and segment.** This is enterprise recruiting software in pre-validation discovery: there are feature requests and limited sandbox access, but no deployment, repeated production use, procurement, or payment. The initial segment is recruiting teams at companies that already use candidate imports and require a manager to authorize retries. Recruit eight companies: the two offering sandbox data plus six independent companies, not just the 30 dashboard requesters. Each company must provide an active recruiter who attempted an import in the last 30 days, the relevant approver, and either a redacted sandbox or a supervised screen-share. This sample tests the observed workflow across firms while avoiding an access-only or feature-request-only sample.

**Primary claim.** When a recruiter's candidate import fails, requiring a manager to approve every retry delays recovery enough that the recruiter abandons the product before analytics can create value. The actor is the recruiter, the workflow is import-failure recovery, and the consequence is abandonment before a useful analytics session.

**Causal rivals.** The dashboard may be too small or poorly organized; recruiters may lack authority for reasons beyond retry approval; error messages or notifications may hide the next action; bad mappings or source-data quality may make recovery impossible; an integration defect may be the real cause; or the manager's response time may matter more than the approval rule itself. Evidence would disconfirm the primary claim if recruiters still fail to return after imports are repaired and retries no longer wait on repeated approval, or if successful importers repeatedly fail real analytics tasks with the current dashboard but succeed with the larger version.

**Evidence already observed.** Thirty HR directors requested a larger dashboard, which is request evidence rather than evidence of use. In four screen-sharing sessions, recruiters could already see analytics, yet abandoned when imports failed and every retry needed manager approval. That behavior contradicts the stated dashboard diagnosis and raises the import-recovery claim. Two companies' willingness to share sandbox data is costly access and useful for learning, but neither it nor the four observations establishes demand because nobody has deployed or paid.

**Recruitment, consent, and risk.** The founder is the learning owner. The growth lead may recruit to the founder's inclusion rule but may not optimize channels or reinterpret results. Recruit the six additional companies across at least two company-size bands and two import sources; no more than half may come from the 30 requesters. Obtain separate consent from recruiter and approver rather than relying on the HR director alone. Use synthetic data first; for redacted candidate data, minimize fields, prohibit copying outside the sandbox, log access, name a deletion date, and let participants stop without affecting commercial treatment. Exclude companies without a recent import attempt, participants who only want to discuss features, and workflows that cannot be observed safely.

**Test and comparison.** Instrument the sequence `import started -> failure type -> retry requested -> approval requested/granted -> retry -> import completed -> analytics task -> return`. For qualified teams with a reproducible failure, run a reversible concierge recovery: diagnose the failure, show a precise next action, and let the manager give one bounded approval covering retries for that import. Compare each team's recovery time and downstream behavior with its most recent unassisted attempt. After a successful import, have the recruiter perform the same three recent analytics jobs first in the current dashboard and then in a larger clickable mockup; record completion, workaround, consequence, and subsequent voluntary return, not preference.

**Thresholds and stop rules.** Continue only if at least six qualified companies attempt an observed import by August 7 and at least four yield a reproducible failure; otherwise stop recruitment on August 7 and revisit the segment or claim. Hand the recovery specification to shipping if, by August 28, at least four of six failing teams complete an import, median time from failure to successful retry falls by at least 50%, and at least three of those teams return unprompted to use analytics on two separate days within 14 days. Build the larger dashboard only if, after successful imports, at least four of six recruiters cannot complete a named analytics job in the current view, can complete it in the larger mockup, and return to use it again. Stop custom recovery work after two assisted imports per company; do not let concierge support become an unpriced product.

Growth remains gated beyond that product-learning threshold. Release the $60,000 only after at least three companies deploy the workflow and use it weekly for two weeks and at least two of them either pay, sign a paid-pilot commitment, or enter procurement with a dated production launch. Sandbox access, clicks, signups, or praise cannot substitute. If fewer than three of six recovered teams return twice, preserve the findings and return the problem/segment to opportunity choice rather than silently pivoting.

## Weekly execution

| Week | Work and observable output |
|---|---|
| **1 — Jul 20–24** | Freeze the record and thresholds. Growth recruits to the inclusion rule. Product analytics adds the event sequence. The founder interviews recruiter and approver separately about the most recent import, exact sequence, workaround, delay, and consequence. Security approves the sandbox protocol. Output: eight scheduled companies, consent status, baseline event definitions, and no ad launch. |
| **2 — Jul 27–31** | Observe imports in the two offered sandboxes and at least two additional supervised sessions. Classify failure causes, approval waits, retries, and abandonment without pitching a solution. Reconstruct the most recent failed attempt for every participant. Output: evidence log with timestamps, source, actor, failure class, confounders, and harms. |
| **3 — Aug 3–7** | Run the first bounded concierge recoveries and one-import approvals. Capture baseline-versus-assisted recovery time. Test real analytics jobs after success using the existing dashboard before showing the larger mockup. At the August 7 review, enforce the minimum-sample stop rule. |
| **4 — Aug 10–14** | Repeat the recovery test across the remaining qualified teams and vary import source/company size. Product/design converts repeated recovery steps into a reversible specification, while learning retains interpretation. Record voluntary analytics returns; do not prompt people merely to manufacture retention. |
| **5 — Aug 17–21** | End concierge work at two assisted imports per company. Look for an unassisted repeat import and second analytics visit. Sales may ask for a concrete paid-pilot, procurement, or deployment commitment without discounting it into existence. Audit whether dashboard-mockup behavior actually beats the current view. |
| **6 — Aug 24–28** | Reconcile event data, observations, counterexamples, privacy issues, and commitments against the prewritten thresholds. On August 28, choose one of the recorded branches below and transfer the evidence, not an inflated conclusion. The ad budget remains on hold unless the separate growth gate has passed. |

# Decision record

- **Decision date:** July 20, 2026; interim review August 7; final review August 28.
- **Current decision:** Do not build the larger dashboard and do not spend the $60,000 yet. Run the import-recovery test because observed behavior currently outweighs feature-request volume.
- **Status of belief:** The import/approval claim is plausible but unvalidated. Four observations are narrow; two sandbox offers are meaningful access, not deployment or demand.
- **Unknowns to resolve:** failure mix, manager response time, approval policy, importer/source differences, downstream analytics task success, repeat use, procurement, and willingness to pay.
- **Evidence standard:** use event sequences, observed work, voluntary repeat behavior, deployment/procurement, and payment or signed commitment. Keep requests and qualitative explanations as context, not conversion metrics.
- **Branch A — recovery threshold passes:** learning hands a bounded problem statement, failure taxonomy, event data, security constraints, and acceptance thresholds to shipping. Dashboard work stays out unless its own behavioral threshold passes.
- **Branch B — dashboard rival passes:** learning hands the demonstrated analytics-task failure and tested mockup to shipping; the decision is based on completed tasks and repeat use, not the 30 requests.
- **Branch C — product threshold passes but growth gate does not:** shipping may implement the narrow reversible fix; learning continues deployment and willingness-to-pay tests. Growth may keep recruiting the sample but receives no optimization budget.
- **Branch D — growth gate passes:** the founder signs off on the evidence record; growth receives the validated segment, qualifying workflow, proof points, exclusions, and the $60,000 experiment budget. Growth then owns channel and landing-page execution with cost and conversion guardrails.
- **Branch E — recovery and dashboard thresholds both fail:** stop custom work, preserve counterevidence and segment boundaries, and return the unresolved direction to opportunity choice.

# Ownership handoffs

| State | Accountable owner | Handoff package |
|---|---|---|
| Uncertain through Aug 28 | Founder/learning lead | Question, sample, consent, thresholds, evidence log, confounders, and interpretation. |
| Recruitment during discovery | Growth lead, constrained by learning | Inclusion rule and outreach list; no ad or landing-page optimization mandate. |
| Safe test operations | Security/privacy owner plus support/data engineering | Data-minimization protocol, deletion log, incident/rollback path, and a two-import concierge cap. |
| Threshold-backed product work | Shipping/product lead | Narrow workflow specification, failure taxonomy, before/after behavior, acceptance criteria, and counterexamples. |
| Repeated use plus commercial gate | Growth lead | Validated segment, actual deployment/use evidence, paid or dated procurement commitments, exclusions, and approved budget. |
| Still uncertain | Founder/learning lead | Revised claim or sample and a new dated record; growth still only recruits. |
| Falsified direction | Opportunity-choice owner | Preserved negative evidence, tested rivals, remaining uncertainties, and explicit stop decision. |
