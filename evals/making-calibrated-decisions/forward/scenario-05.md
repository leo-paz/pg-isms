mode: cross-domain-decision  
primary_skill: making-calibrated-decisions  
reason: The tooling commitment couples patient harm, scientific evidence, regulation, manufacturing optionality, study timing, and cash survival; no single specialist owns the whole choice.

## Decision header — July 17, 2026

decision: Whether by August 15 to place the full non-refundable $700,000 tooling order, wait for independent and regulatory evidence, or obtain a bounded manufacturing option.  
owner and deadline: CEO, with board approval; August 15, 2026.  
state: Pre-revenue medical-device startup with $2.6 million cash and $260,000 monthly pre-tooling spend. Static runway is about 10 months before tooling and about 7.3 months immediately after a full order, excluding study and other new costs. The binding constraint is preserving enough cash to reach a fundable pivotal-study decision under a replication-failure case.  
product type: High-harm regulated hardware.  
error profile: A non-refundable order is irreversible. Maximum credible downsides include patient harm, unusable tooling, regulatory delay, and loss of cash needed for the study. Patients, study participants, employees, and owners bear the error. Protected obligations are safety, evidence integrity, regulatory control, and a board-defined cash floor.  
evidence clock: Independent replication finishes in October and the regulator meeting is in November. Waiting may delay the study three months; ordering now advances schedule but commits before the earliest trustworthy external evidence.

## Evidence ledger

**Observed**

- Cash is $2.6 million and monthly spend before tooling is $260,000.
- Eighteen bench-test units met the internal target.
- Independent replication is scheduled to finish in October and a regulator meeting is scheduled for November.
- Two nonbinding hospital letters exist; no purchase order exists.
- The proposed tooling order is $700,000 and non-refundable.

**Claimed**

- A famous surgeon says the design will become standard of care.
- The hospital letters express interest but do not establish purchasing commitment.
- The supplier says the manufacturing slot may disappear.
- Waiting could delay a pivotal study by three months.

**Inferred**

- Internal bench results justify continued investigation, but 18 internally tested units do not establish independent replication, clinical benefit, regulatory acceptability, manufacturability, or demand.
- Paying the full order would consume about 27% of current cash and reduce burn-only runway by about 2.7 months before study costs.
- The most valuable immediate action is to price and verify a manufacturing option that separates schedule preservation from the full irreversible exposure.

**Unknowns that can change the decision**

| Unknown | Owner | Artifact/source | Due | Threshold | Decision effect |
|---|---|---|---|---|---|
| Full downside cash need through study gate | Finance lead | Board-reviewed cash model including tooling, study, delays, and replication failure | Aug 1 | Protected cash floor funds obligations and the next evidence milestone without relying on uncommitted capital | Failure forbids full order and routes survival first |
| Supplier capacity and reservation alternatives | Operations lead | Written capacity evidence and binding quotes for reservation, staged tooling, transfer, cancellation, and refund terms | Jul 29 | A bounded option has defined cost, duration through November, capacity, milestones, and exit | Enables option instead of full order; absence weakens scarcity claim |
| Tooling usefulness under design change | Engineering/quality lead | Tool design review and change-cost analysis | Aug 5 | Qualified review shows specified tooling remains usable across credible replication/regulatory changes | Failure forbids irreversible tooling |
| Safety and replication risk | Scientific/quality lead | Independent lab protocol, blinded results when available, and qualified risk review | Protocol by Aug 1; results in October | No unresolved critical protocol defect now; independent result must meet predeclared acceptance criteria before full exposure | Protocol failure stops; result governs later commitment |
| Regulatory path | Regulatory lead | Current qualified regulatory strategy and November meeting record | Strategy by Aug 5; meeting in November | No known issue makes current tooling premature; regulator feedback later supports the intended path | Failure or material uncertainty favors option/wait |
| Study demand and procurement | Commercial/clinical lead | Buyer interviews, binding trial/site commitments, and budget authority | Aug 5 | Evidence identifies accountable buyers and concrete study/site commitments; letters alone do not pass | Distinguishes institutional demand from endorsement |

Rival explanations: internal success may reflect valid performance or internal protocol bias; hospital letters may signal real future demand or low-cost interest; supplier scarcity may be genuine or sales pressure; a three-month delay may matter greatly or be recoverable elsewhere in the study plan. Disconfirming observations are the absent independent replication, nonbinding demand, missing purchase orders, and undocumented capacity.

## Source calibration

The surgeon's reputation and clinical contact may justify careful investigation, but “standard of care” lacks a defined population, adoption threshold, evidence standard, and resolution date; it cannot pass a safety or cash gate. The supplier's scarcity forecast becomes decision-relevant only when capacity, expiration, and reservation alternatives are documented. Neither prestige nor urgency is proof.

## Options

| Option | Hard gates/survival | Users/payoff | Reversibility, options, evidence, delay |
|---|---|---|---|
| Full $700,000 order now | Independent, regulatory, design-stability, and cash-floor gates are unresolved | May avoid three-month delay if all later evidence passes; exposes future patients and study funding to premature design lock | Irreversible; destroys cash and design flexibility |
| Buy a documented reservation or staged option | Requires verified capacity, capped cost, milestone releases, and cash-floor approval | Preserves possible study timing while bounding premature exposure | Most reversible; carries option cost through October/November evidence |
| Wait without reservation | Preserves cash and design flexibility | Minimizes premature harm; may add three months if capacity is truly scarce | Fully preserves evidence response but may lose slot |

**Commitment:** do not authorize the full non-refundable order on current evidence. First seek a documented, capped reservation or staged commitment that lasts through the October replication and November regulator meeting. Any option price is acceptable only if the survival owner shows the protected study cash floor remains intact. If no credible option exists, default to waiting unless every high-harm and survival gate independently passes.

## Dated branches

- **proceed** — Predicate: by Aug 12 qualified safety, regulatory-prematurity, design-stability, demand, and cash-floor gates all pass, and supplier scarcity is documented. Owner/date/action: CEO and board, Aug 15; authorize only the approved staged or full order. Safeguard/preserved option: milestone releases, quality controls, and funded study reserve. Switch: any gate changes before payment → `defer` or `stop-or-route`. Handoffs: qualified regulatory, quality, clinical, manufacturing, and `managing-runway-and-survival` owners.
- **adapt** — Predicate: evidence supports preserving capacity but not full irreversible exposure. Owner/date/action: operations lead, Aug 15; purchase the capped reservation or staged tooling option. Preserved option: wait, modify design, or release the slot after October/November evidence. Switch: independent and regulatory gates pass → later `proceed`; fail → `stop-or-route`.
- **defer** — Predicate: material evidence is missing, no credible option is offered, and no gate has conclusively failed. Owner/date/action: CEO, Aug 15; place no non-refundable order and review after October replication and again after the November meeting. Preserved option: cash, redesign, alternate suppliers, and a later study. Switch: trustworthy evidence and a viable manufacturing path appear → reconsider.
- **stop-or-route** — Predicate: critical safety/protocol concern, design instability, unacceptable regulatory risk, or protected cash-floor failure. Owner/date/action: CEO, immediately; stop tooling commitment. Preserved option: investigation, redesign, and survival plan. Switch: the exact failed gate is resolved by qualified evidence. Handoffs: scientific/quality and regulatory specialists first; `managing-runway-and-survival` before any capital-dependent commitment.

This is a decision-process record, not medical, regulatory, legal, or investment advice.

Case ID: scenario-05
Reviewer ID: calibration-forward-generator-001
