# Six-week learning plan

## Learning record

**Assumed calendar:** Monday, July 20 through Sunday, August 30, 2026, with the decision review on Monday, August 31, 2026.

- **Product, stage, and segment:** Enterprise recruiting SaaS, pre-deployment and pre-revenue for this use case. The initial segment is mid-market recruiting teams that import candidates from the same source systems, have an active recruiter doing the import, and require a manager to authorize retries. Start with the two companies offering sandbox data and recruit four more matching teams. Six teams is a small but deliberately comparable behavioral sample; the 30 HR directors are useful leads, not evidence by themselves.
- **Primary claim:** When a recruiter imports candidates, failed imports plus manager approval for each retry interrupt the workflow long enough to cause abandonment; making recovery reliable and reducing repeated approval friction will cause the same team to complete imports and return to use the product.
- **Causal rivals:** Analytics may be hard to see or inadequate; the recruiter may lack authority independent of the product; failure notifications may not explain the remedy; source-data quality or integration defects may be the real cause; manager response time or another process delay may dominate. The primary claim is disconfirmed if teams still abandon after imports complete promptly, or if an analytics change alone produces repeated use while import recovery does not.
- **Evidence already observed:** Thirty directors requested a larger analytics dashboard, but in four screen shares recruiters could already see analytics and abandoned at failed imports and approval-gated retries. Two companies will incur the cost of sharing sandbox data. There is no deployment, repeated use, signed commitment, or payment. The request and observed behavior therefore conflict, and demand is not validated.
- **Sample and consent:** The learning lead owns inclusion and interpretation; the growth lead may recruit only to the inclusion rule above. Each session must include the recruiter who recently performed an import and, for the authority test, the approving manager. Obtain written permission for sandbox access, define retention/deletion dates, redact candidate personal data where possible, and record sessions only with consent. Exclude director-only conversations, teams without a candidate import in the last 30 days, non-comparable integrations, and prospects selected merely for enthusiasm or easy access.
- **Risks and confounders:** Sandbox behavior may not match production, manual help may create an operator effect, the two volunteers may be unusually motivated, customer approval policy may be immutable, and candidate data is sensitive. Cap concierge work at 90 minutes per company per week and log every manual action so custom service does not silently become the product.

## Weekly execution

1. **Week 1 — July 20–26: baseline and recruit.** Enroll the two sandbox partners and four additional qualifying teams. For each recruiter, reconstruct the most recent import event: source, sequence, failure, message seen, retry request, approver, elapsed time, workaround, and consequence. Instrument import attempts, completion, time-to-recovery, approvals, and subsequent product use. Do not demo a larger dashboard or ask whether participants like either solution.
2. **Week 2 — July 27–August 2: observe the failure.** Observe at least one unassisted sandbox import per team where safe. Reproduce and classify failures, measure the approval delay, and note whether analytics visibility interrupts the task. At the August 3 checkpoint, continue only if at least four teams reproduce materially the same failure-and-retry sequence; otherwise narrow the segment or revise the claim rather than pooling unlike problems.
3. **Week 3 — August 3–9: bounded comparison.** Give each reproducing team a reversible recovery path: explicit error diagnosis plus a concierge or prototype-assisted retry. In a separate attempt, test one authority change approved by the customer, such as one manager authorization covering retries for that import batch. Keep analytics unchanged. Compare completion and elapsed time with the team's baseline, and log all operator work.
4. **Week 4 — August 10–16: isolate rivals.** Repeat imports on new sandbox batches without researcher prompting. Where the authority change is not allowed, compare clearer notification plus the existing approval path; where it is allowed, compare approval-once with notification held constant. Ask about actual recent consequences and workarounds. If imports complete promptly but teams still stop, observe whether the unmet analytics job—not merely dashboard size—explains the stop.
5. **Week 5 — August 17–23: test costly behavior.** Remove avoidable concierge prompting and look for self-initiated return use. Ask teams that meet the workflow threshold to take the next appropriate enterprise step: approve a production security/integration review and sign a dated paid-pilot or deployment commitment. Record who can buy, procurement blockers, and refusals; do not count verbal enthusiasm, clicks, or continued subsidized testing as demand.
6. **Week 6 — August 24–30: repeat and decide.** Run the final import cycles, verify events with participants, document missing data and confounders, and stop prototype changes on August 28. The learning lead writes the decision record and holds the August 31 review against the precommitted thresholds.

## Thresholds and stop rules

The import claim passes only if at least four of the six qualifying teams each complete three import cycles across at least two weeks, at least 80% of assisted-path imports complete within 15 minutes, and at least three teams return for a later import without researcher prompting. Demand is validated for growth only when at least two of those teams also sign a dated paid-pilot/deployment commitment or pay; sandbox access alone does not qualify.

Pause a session immediately for unauthorized personal data, security risk, or customer harm. Stop the current segment test if fewer than four comparable teams reproduce the sequence by August 3, if the recovery path cannot be tested without overriding customer authority, or if the 90-minute concierge cap is repeatedly exceeded. Preserve the observations and revise the claim; do not quietly broaden the sample or change the threshold.

# Decision record

- **Decision now:** Do not build the requested larger analytics dashboard, and do not approve the $60,000 ad and landing-page budget. Investigate the observed import/retry bottleneck first. This is a learning decision, not a conclusion that analytics never matters.
- **Why:** The dashboard request is reported preference from directors, while four workflow observations point to a different abandonment cause. Sandbox-data access is a stronger signal than praise but remains below deployment, repeated use, commitment, or payment. Advertising would amplify an unvalidated workflow and confound product learning with acquisition quality.
- **Review date:** August 31, 2026.
- **Pass — workflow and demand:** If both thresholds pass, hand the tested recovery behavior and evidence to the shipping owner for the smallest production implementation. After the qualifying repeated use and paid/deployment commitments are verified, hand the narrow segment and evidence to growth for execution. Growth may then propose a staged acquisition test; the evidence does not automatically authorize all $60,000.
- **Workflow passes, demand does not:** Learning retains ownership for one explicitly bounded commitment/procurement test. Shipping may maintain only the reversible test path; growth still does not optimize channels.
- **Analytics rival wins:** If successful imports do not restore use and observed work shows a specific analytics job is blocking teams, send that preserved evidence to the opportunity-choice owner to compare a dashboard direction. Do not translate the original 30 requests directly into a build specification.
- **Claim fails or sample fragments:** Return the findings to opportunity choice for segment/problem selection. No silent pivot and no growth handoff.

# Ownership handoffs

| Phase or result | Accountable owner | Handoff artifact and boundary |
|---|---|---|
| Weeks 1–6 learning | Learning lead | Owns claim, sample, consent requirements, thresholds, stop rules, evidence log, and interpretation. |
| Participant recruitment | Growth lead, directed by learning | Recruits six matching teams; may not optimize ads, landing pages, or inclusion criteria. |
| Sandbox safety and access | Security/privacy owner plus each customer's data owner | Written access scope, redaction, retention/deletion date, and incident stop path before data use. |
| Reversible test path | Product/engineering test owner | Builds only the bounded recovery/notification/authorization test specified by learning and logs manual interventions. |
| Passed workflow claim | Shipping owner | Receives the falsifiable claim, comparison results, edge cases, and smallest validated behavior—not the directors' feature wording. |
| Validated demand | Growth lead | Receives the narrow segment, observed use, commitments/payment evidence, and acquisition assumptions for staged execution. |
| Unresolved pricing | Business-model owner | Receives willingness-to-pay and procurement evidence; learning does not infer a pricing model from pilot interest. |
| Failed claim or new direction | Opportunity-choice owner | Receives preserved observations, contradictions, confounders, and failed thresholds for explicit comparison or pivot. |
