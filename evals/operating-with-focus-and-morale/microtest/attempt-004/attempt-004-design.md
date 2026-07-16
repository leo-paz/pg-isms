# Microtest attempt 004: operating with focus and morale

Status: design only; no responses generated or scored.

## Frozen package surface

- Package-surface SHA-256: `7a997edc0a36cde7a51c57331896b6f11222615d391c8761afbb145ed8024654`
- Algorithm: SHA-256 of the bytewise concatenation, in this order, of:
  1. `skills/operating-with-focus-and-morale/SKILL.md` — `b6c338f2d9ce0b225e81f03ed1c1e4f8b15ab9731d53f343375a2008eedf0507`
  2. `skills/operating-with-focus-and-morale/references/runtime-contract.md` — `5d44db01c258ab81ad55a0479e49563dd8d2766be2d9f06144483db138d45cff`

Hypothesis: at this frozen package surface, fresh guided agents will more often produce a complete, owned, evidence-bound focus-and-morale operating artifact than otherwise identical fresh control agents.

## Exact prompt

```text
Today is July 15, 2026. You advise Common Chord, an 11-month-old Seattle startup running paid neighborhood choirs for adults. The team is founder Maya, music director Ellis, member coordinator Rowan, and three part-time conductors. It has 16 months of runway at current spend, payroll and venue bills are current, no financing process or buyer conversation is active, and no acute medical, safety, legal, privacy, or misconduct issue has been reported. Venue insurance and incident procedures are current.

Common Chord has 138 paying members across four choirs. Renewal opens August 10 and closes August 24. The attendance ledger shows 52 members attended fewer than three of the last six rehearsals. In 20 dated calls with recently lapsed members, 12 said they could not tell whether they were improving, five cited scheduling, and three cited price. One conductor tried a written song goal plus a closing rehearsal recording for two weeks: attendance among that choir's 28 members rose from 61% to 79%, but there was no control group and the same conductor ran both weeks. The team does not know whether that result repeats, whether it changes renewal, or whether the conductor rather than the tactic caused it.

The team has also announced an August 29 member showcase; venue deposits, performer communication, and contracted accompanists must be honored. Maya wants to open a fifth choir on August 20 because she says visible expansion will prove momentum and lift morale. A prospective sponsor says a professionally produced livestream of the showcase would create credibility. Maya also wants a full visual rebrand before renewal, and Rowan wants to pitch employer-sponsored memberships this month. No one has measured member demand or renewal effect for the fifth choir, livestream, rebrand, or employer plan. Ellis believes visible rehearsal progress is the renewal bottleneck. One conductor believes fatigue, not the member experience, explains the attendance decline.

Decision rights are written and accepted: Maya owns pricing and new locations, Ellis owns rehearsal standards and conductor assignment, and Rowan owns renewals and member communication. Nine routine rehearsal adjustments waited 24-36 hours in the last ten days after Maya inserted herself; no comparable queue existed before June 24, when she started carrying the expansion and showcase work.

For the last three weeks Maya worked 66 hours and Ellis 58; two conductors report no full day off in 14 days. The weekly anonymous morale pulse fell from 7/10 six weeks ago to 4/10 now. The team issued two erroneous song sheets and one member reply took 63 hours against its 24-hour standard. Current rehearsals, the 24-hour member-response promise, payroll, contracted showcase obligations, and incident coverage cannot be dropped.

What should Common Chord do from July 15 through the August 24 renewal decision? Return the actual operating artifact the team should use, not a pep talk or generic advice, in at most 1,200 words. Choose now, give dated checkpoints and decision branches, protect members and the team, and make unknowns explicit instead of inventing evidence or asking follow-up questions.
```

## Five strict binary conjunctive criteria

For every criterion, award `1` only when every clause passes. Any failed or unverifiable clause makes the criterion `0`; there is no partial credit and implicit fields do not count.

### C1 — Route and evidence integrity

1. Select `operating-with-focus-and-morale` as primary and use prompt facts to exclude survival, financing, buyer, structural-organization, and acute-risk primacy. Treat the recent approval queue as overload-related, with a dated persistence test that would switch to organization work.
2. Classify decision-relevant inputs without converting interpretations into facts or inventing evidence. Preserve separately as claims Maya's expansion-morale view, the sponsor's livestream-credibility view, Maya's rebrand preference, Rowan's employer-plan preference, Ellis's rehearsal-progress diagnosis, and the conductor's fatigue diagnosis.
3. Give each consequential unknown its own owner, method/artifact, due date, result threshold, and decision effect: trial repeatability, renewal effect, conductor-versus-tactic confounding, fatigue-versus-member-experience mechanism, and member demand or renewal effect for each of the fifth choir, livestream, rebrand, and employer plan.
4. Do not contradict or omit a numeric deadline, baseline, continuity fact, or workload signal used by the decision.

### C2 — One priority and competing work

1. Select exactly one state-changing outcome centered on the current four choirs' renewal/member value and exactly one current tactic or linked evidence loop; do not run a continuing portfolio comparison.
2. Include a dated baseline, dated target, affected members/work, accountable owner, proposed mechanism, at least one rival, honest evidence latency/checkpoint, falsifier, and final decision date.
3. Give separate `protect`, `cancel`, `delegate`, `defer`, or tightly `bound` dispositions with owner, effective date, and limit/reopen condition for the fifth choir, professional livestream, visual rebrand, employer-sponsored-membership pitch, and committed August 29 showcase.
4. Name current rehearsals, the 24-hour member response, payroll, contracted showcase obligations, and incident coverage as protected essentials; leave no named initiative undispositioned.

### C3 — Execution, recovery, and coverage

1. Protect recurring contiguous rehearsal-design/analysis time and recurring direct member contact for the accountable owner; bound meetings, notifications, status work, and availability.
2. For rehearsal delivery, member response, showcase/vendor commitments, incident response, payroll, and decision authority, name a primary owner, distinct backup decision owner, service block/level, escalation destination, and concrete response window.
3. Set a numeric sustainable weekly workload or availability limit, immediate dated recovery for overload, and an end date plus recovery for any exceptional push. Remove or delegate work before claiming protected capacity.
4. Diagnose morale from the observed pulse, hours, missed rest, errors, delayed reply, progress visibility, and ownership signal. Test progress and fatigue mechanisms without using raw hours, public pressure, compulsory nights, or continuous availability as determination.

### C4 — Owned cadence and goal/tactic separation

1. State the goal premise separately from the selected tactic and state the tactic selected now.
2. Include separate company-outcome, member/continuity, and workload/judgment measures; every measure has a dated baseline, target/limit, evidence source, owner, and review date.
3. Set at least one intermediate check at an honest evidence interval and a final decision on August 24 or another explicitly justified date tied to renewal evidence.
4. At checks, require recording observed result, confounders, safeguard status, and the precommitted branch. Do not use hours as a seriousness or morale success score.

### C5 — Complete branch matrix and compact contract

1. Provide separate `continue`, `adapt`, `reopen-goal`, and `stop` rows, each with its own observable threshold, next action, next owner, calendar date, primary route after the branch, and handoff/return condition and date.
2. `adapt` changes one material variable while the premise remains plausible; `reopen-goal` depends on repeated discriminating evidence or a changed hard constraint; `stop` depends on invalidation or a hard boundary, not low morale alone.
3. Record the decision now, a preserved option, and unresolved unknowns carried forward; do not move thresholds after results.
4. Stay at or below 1,200 words and use a filled compact record with no blank cells, `TBD`, "as needed," shared implicit owners/dates, or generic introductory/productivity prose. Include the one-line lineage treatment, saying once that runtime citations were not supplied if applicable.

## Fresh-agent paired run plan

Run ten one-shot calls: five control and five guided. Every repetition starts in a new context with no memory, prior output, evaluator notes, repository access, or eval artifacts. Randomly interleave the calls. Use the same model snapshot, base system message, decoding parameters, output-token limit, tool policy, and exact prompt in both arms. Disable repository and web access. Do not retry, repair, continue, or edit any output.

- Control, 5 reps: common base system message plus exact prompt only. Do not expose the skill name, metadata, package text, runtime contract, summaries, criteria, or eval context.
- Guided, 5 reps: identical base system message and exact prompt, plus the exact frozen contents of the two package files above as system-level skill guidance. Expose no other repository file.

Existing evals, cases, prompts, heldout material, microtests, responses, scores, cross-repetition history, and answer hints are forbidden in either arm.

## Blinded scoring

After all outputs are frozen, assign opaque random response IDs and keep the arm mapping inaccessible to the scorer. Show the scorer only the exact prompt, the five criteria in randomized order, and the ten responses in separately randomized order. Remove labels, filenames, package mentions, and metadata that reveal arm.

Score all 50 response-by-criterion judgments independently as binary, with a short evidence note. Lock them before unblinding. Then reveal the mapping once and compute:

`response_score = (C1 + C2 + C3 + C4 + C5) / 5`

`arm_score = mean(response_score for the five valid responses in that arm)`

`effect = guided_arm_score - control_arm_score`

Acceptance requires exactly five valid fresh-agent responses in each arm and `effect >= 0.20`. Otherwise reject or run a newly designed test; do not repair individual outputs.

## Novelty and non-overlap rationale

This is a performing-arts service case: paid adult neighborhood choirs must resolve whether visible rehearsal progress changes member renewal while preserving live rehearsals, a contracted showcase, member response, and humane workload. The evidence is embodied, cohort-based, and confounded by conductor effects. It is materially different from software delivery, calendar cleanup, fundraising, acquisition, and greenhouse/hardware trials.

The recent approval queue is deliberately bounded to an overload onset despite accepted decision rights, testing focus-versus-organization routing without making org design the main story. The expansion, livestream, rebrand, employer plan, rehearsal intervention, names, dates, and counts were created for this attempt. This design was authored without reading existing evals, prior cases, prompts, heldout items, microtests, responses, or scores.

The requested `research/taxonomy.md` path was absent in the working tree at design time; no substitute taxonomy artifact was opened. Routing and criteria use only the frozen skill surface above.
