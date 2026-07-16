# Attempt 005 paired microtest design

Status: design only; no generation or scoring has been run.

Pinned skill package:

- Combined SHA-256: `1b2be7ce738d64d623e026c4ced88bd7f415b0d3296196590a7d7a5145b16678`
- Definition: `sha256(SKILL.md bytes || 0x00 || runtime-contract.md bytes)`
- `SKILL.md`: `8cb42d33741e49adfb6412bcedb88106491f0041324486115aa4ffdf362245cc`
- `runtime-contract.md`: `24ec2d982c69da54dc1c6474032e898ee4da22e3f10a8b0bd2a7c4dadeeb2336`

Repository-source boundary: only the current `skills/operating-with-focus-and-morale/SKILL.md` and `skills/operating-with-focus-and-morale/references/runtime-contract.md` were read. No existing eval, previous design, prompt, response, score, heldout test, forward test, or microtest content was reviewed.

## Domain

Early-stage educational card-game publishing. This physical educational publishing scenario is materially distinct from software, marine or greenhouse hardware, choir or performing arts, local news, financing, and acquisition.

## Exact prompt

Use this prompt byte-for-byte for every control and guided run:

```text
Today is July 15, 2026. I am Lena, founder and product lead of Mosaic Minute, a five-person company publishing a classroom card game for public middle-school teachers. We are early-stage, have nine months of runway, and the next three payrolls are funded. There is no fundraising, investor diligence, buyer conversation, sale process, lawsuit, safety event, security issue, or active customer incident.

Decision rights are written down: I own product decisions, Mateo owns sales, Priya owns design, Eli owns operations, and Mina owns teacher success. Before June, approvals normally cleared within four working hours. In the last two weeks, six product or design approvals waited two to three days, all after my workload rose; no one disputes the written rights.

Fourteen teachers new to the game ran a first session using the current core deck. Five completed setup without help; nine stalled at the instruction sequence. Seven of those nine separately said the quick-start order was unclear. Four of the five who completed setup requested a school quote. No revised quick-start insert has been tested. Our printer can make test inserts in two business days. Twelve new-teacher sessions are already booked for July 22, 24, and 28.

We are also carrying three proposed initiatives. Mateo wants a booth at the September 10 National Teaching Expo; a non-refundable $8,000 deposit is due July 17 and preparation is estimated at 90 team-hours. He says it will "put us on the map" and produce 300 leads. At our last comparable event, 41 badge scans led to two demos and no orders. A competitor announced an AI-literacy expansion deck; I said we must ship a response in three weeks or become irrelevant, but no teacher or buyer has asked us for one. Priya proposes a wholesale-catalog redesign; three bookstores have asked only for a current price sheet, and none has asked for a redesign.

The team reports morale at 3/10 versus 7/10 on June 1. In the last 12 days we skipped two scheduled teacher calls, reversed two print-file decisions, and stopped the Friday peer critique twice. I have averaged 67 hours a week for three weeks, worked six late nights, taken no full day off, and attended none of the teacher sessions. I proposed a 72-hour week through August 1. Mateo says visible hours prove we are serious.

Confirmed continuity coverage is: teacher messages and session changes, Mina primary and Mateo backup, one-business-day response via the shared CRM; printer and fulfillment exceptions, Eli primary and Priya backup, four-working-hour response via the vendor log; product decision authority while I am offline, me primary and Mateo backup, same-working-day response via the decision log; payroll, Eli primary and our external bookkeeper Dana backup, one-business-day response via the payroll checklist. Every named backup has agreed and is available through July 31.

Choose our one company-changing priority and one current tactic for the next three weeks. Give me a compact, dated operating decision I can execute: deal with all named initiatives, the approval slowdown, user contact, continuity, workload, morale, evidence checks, and the conditions to continue, change tactics, reconsider the goal, or stop. Distinguish facts, interpretations, and unknowns; do not invent missing facts. Keep the answer at or below 1,200 words.
```

## Paired run protocol

Run five pairs (`pair-01` through `pair-05`), for ten generation agents total.

- Use ten separate fresh agents: one user turn, one final answer, no prior or follow-up turns, and no access to another output.
- Use one fixed model snapshot and identical baseline system, temperature `0.7`, top-p `1.0`, maximum output-token budget, tool policy, and timeout. Record execution values.
- Disable repository browsing, web access, inter-agent communication, and rubric or evaluation-artifact access.
- Interleave or randomize arms within each pair.
- On a technical failure before an answer, replace both agents in that pair and record the replacement. Never selectively rerun a low score.

Control, five fresh agents: default system baseline plus the exact prompt only. Do not expose the skill name, skill files, skill catalog, repository, or rubric.

Guided, five fresh agents: the identical default system baseline and exact prompt, with only the pinned `SKILL.md` and `runtime-contract.md` loaded as the applicable skill package. Do not expose the rubric, hashes, evaluation purpose, or other repository material.

## Five strict binary conjunctive criteria

Score each criterion `1` only if every clause is explicit and internally consistent. Any missing, implied, merged, invented, or contradictory clause makes that criterion `0`. No partial or style credit.

### C1 — Route and evidence integrity

Pass only if all are true:

1. Makes focus, attention allocation, degraded judgment, and morale the current primary operating problem, while excluding survival, financing, buyer, organization-redesign, and acute-risk routes with prompt facts rather than assertion.
2. Preserves the dated teacher behavior, event history, workload and judgment signals, approval timing, coverage facts, and every quoted stakeholder interpretation as observed facts or claims without promoting a claim to fact.
3. Gives every consequential unknown on which the selected priority, a named initiative, approval-queue route, or later branch depends its own owner, artifact or method, due date, observable result threshold, and decision effect; invents neither a result nor backup.
4. Leaves no decision-relevant prompt input unclassified.

### C2 — One state-changing priority and complete competing-work choices

Pass only if all are true:

1. Selects exactly one user or company outcome and exactly one current tactic or evidence plan, with dated baseline and target, affected users or work, owner, mechanism, rival explanation, honest latency and checkpoint, falsifier, and final decision date.
2. Gives the Teaching Expo booth, competitor-response expansion, and wholesale-catalog redesign separate `cancel`, `delegate`, `defer`, or tightly `bound` dispositions, each with owner, effective date, and limit or reopen condition.
3. Separately protects essential teacher, production or fulfillment, decision-authority, and payroll obligations instead of treating them as parallel priorities.
4. Does not use hours, morale, prestige, competitor activity, or generic visibility as outcome evidence.

### C3 — Executable attention, continuity, and recovery envelope

Pass only if all are true:

1. Creates recurring contiguous product or analysis time and recurring direct teacher contact for Lena at dates or cadences compatible with July 22, 24, and 28; teacher-success delegation does not replace Lena's decision-relevant contact.
2. For teacher communications, printer or fulfillment exceptions, product decision authority, and payroll, states the supplied primary, distinct supplied backup, service or protected block, escalation destination, response window, and handoff artifact without inventing replacements.
3. Sets a concrete sustainable weekly workload or availability limit, recovery, and an end date for any bounded exceptional push; explicitly rejects or replaces the proposed open-ended 72-hour push and visible-hours proxy.
4. Removes, delegates, or bounds load before claiming focus time, and gives the acute-overload approval queue a dated relief test before escalating it to organization redesign.

### C4 — Morale diagnosis and owned evidence cadence

Pass only if all are true:

1. Treats morale as an operating signal by naming the rating change, skipped teacher calls, print-file reversals, missed peer critiques, or approval waits and tests at least two plausible mechanisms instead of treating morale as a verdict.
2. States the durable goal premise separately from the selected tactic and ties recovery to controllable progress, teacher evidence, ownership or peer support, realistic duration, and recovery rather than pressure or hours.
3. Includes separate company-outcome, teacher or continuity, and workload or judgment measures, each with dated baseline, observable target or limit, source, owner, and review date.
4. For every named intermediate and final check, records the observed result or pending state, confounder or rival status, safeguard status, and precommitted branch.

### C5 — Distinct persistence and stopping decisions

Pass only if all are true:

1. Provides separate `continue`, `adapt`, `reopen-goal`, and `stop` rows; every row has its own observable threshold, action, owner, calendar date, primary route after the branch, and handoff or return condition and date.
2. Continue requires outcome evidence and safeguards; adapt changes one material tactic variable while the premise remains plausible; reopen-goal requires repeated discriminating evidence or a changed hard constraint; stop uses invalidation or a hard survival, safety, legal, harm, or preserved-option boundary.
3. Commits now to a selected tactic, honest final decision date, and non-moving logic while carrying unresolved unknowns forward.
4. Does not treat a competitor announcement, low morale, effort, or a single miss as sufficient proof to persist, reopen, or stop.

Response score: `(C1 + C2 + C3 + C4 + C5) / 5`.

## Blind scoring

1. Freeze all ten raw answers. Assign opaque IDs independently of arm and pair; keep the key with a non-scoring coordinator.
2. Randomize answer order separately for two fresh independent scorers. Give each only the exact prompt, criteria, and anonymized answers. Hide arm, pair, skill text, hashes, run order, and expected effect.
3. Require `0` or `1` for each criterion plus a short excerpt or precise missing-clause note. Do not infer absent fields.
4. Send disagreements to a third fresh blind adjudicator with only the disputed answer, prompt, criterion, and randomized scorer notes.
5. Freeze the adjudicated matrix before revealing arms.

Compute each arm's five-answer mean, paired differences, and criterion pass rates. Acceptance is:

```text
mean_guided_score - mean_control_score >= 0.20
```

No other acceptance gate is substituted for this threshold.

## Fairness self-audit

- The prompt is byte-identical across arms; only the pinned guidance exposure differs.
- All scorable facts are in the prompt; no research, specialist domain knowledge, or essay citation is required.
- Criteria are threshold-neutral: they require observable, precommitted, date-consistent consequential thresholds, not preferred numeric values.
- Criteria are separated by surface: routing/evidence, priority/alternatives, execution/continuity, morale/cadence, and branch logic. A fact is reused only when it has a distinct consequence.
- Every clause affects routing, evidence integrity, priority, continuity, sustainable judgment, morale diagnosis, or a decision branch. No points depend on polish, headings, citation form, or table aesthetics.
- Supplied owners, backups, artifacts, windows, dates, and evidence latency avoid forcing invention.
- Compact tables can satisfy all criteria in an estimated 850–1,100 words, leaving margin under 1,200.
- Pairwise technical replacement and blind scoring prevent selective reruns, truncation handling, or order from favoring an arm.

## Novelty self-audit

- The educational card-game publishing domain is outside every excluded domain.
- The design derives only from the two pinned current skill files; no existing evaluation material was reviewed.
- The scenario's combination of physical publishing latency, booked teacher sessions, a documented-rights overload queue, confirmed backup coverage, event and competitor pressure, and morale signals is independently constructed.
- Neither arm sees expected answer text or the scoring rubric.
