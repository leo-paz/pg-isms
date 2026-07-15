# Organization paired-microtest design gate

**Verdict: PASS**  
**Blockers: none**  
**Review date: 2026-07-15**  
**Mode: blind independent review of the three authorized artifacts only**

## Snapshot hashes

| Authorized input | SHA-256 |
|---|---|
| `.superpowers/sdd/org-micro-draft/rubric.json` | `637702d2cc20c2c1a20cd1c190b9a1f7fac43e020732e6682873a7f43fd6aa75` |
| `skills/building-and-evolving-organizations/SKILL.md` | `2a1e0a27562aa3cfac61ce280a833bd538e4ad633267e238d8cf7bed695e572a` |
| `skills/building-and-evolving-organizations/references/runtime-contract.md` | `6fc8f66eb3b3aea79b1bab9b67602887e0bbb17a00e302e6982fb48378e7bd5b` |

Derived fingerprints: decoded prompt via `jq -r` plus its trailing LF is `375c5d6d4c905177150b206e7c65fb960cde374c99cb22f7ac4abd49662fa4be`; compact criteria JSON via `jq -c` plus its trailing LF is `5a12e2133053c6b53f2d0bd1a3771ddaf2b21e8d1f24ed886647154634d4ce19`.

No external digest manifest was authorized. These hashes bind this verdict to the reviewed snapshots.

## Checks

| Check | Result | Finding |
|---|---|---|
| JSON and shape | PASS | The rubric parses; schema version and skill name match; the prompt is a nonempty string; all criteria are nonempty strings. |
| Exact prompt length | PASS | The decoded prompt is exactly **365** whitespace-delimited words (`jq -r .prompt` piped to an `awk` field count). |
| Five criteria | PASS | Exactly five pass/fail criteria are present. |
| Naturalness and leakage | PASS | This is a plausible executive memo request. It naturally asks for a current decision, six-week operation, deferred alternatives, and a later decision without exposing branch labels, the evidence taxonomy, operating-contract checklist, result taxonomy, scoring, or intended answer. |
| Chronology | PASS | Jan 1-Mar 31 evidence, the March queue attempt, Apr 6-17 shadow exercise, and May 4 memo date are consistently ordered. Six weeks after May 4 is derivable. |
| Arithmetic | PASS | `15 + 4 + 1 = 20` delayed requests and `16 + 2 = 18` shadow decisions. Other counts may overlap and create no contradiction. |
| Feasibility and alignment | PASS | The prompt supplies enough evidence to make the organizational decision and design a reversible test without assuming historical facts. The five constructs align to the skill/runtime contract and are feasible within 1,500 words. |
| Evidence taxonomy | PASS | Criterion 2 correctly separates records and verified exercise results from stakeholder claims and unresolved causality, sustainable load, boundary quality, and future effects; it also requires a causal rival. |
| Criterion independence | PASS | C1 scores present diagnosis/choice; C2 epistemic discipline; C3 the operating contract; C4 pilot execution; C5 closure branching. Shared continuity and security terms have scope-specific roles and are not independent pass evidence by themselves. |
| Semantic grading | PASS | Semantic equivalents are accepted. The rubric grades substance, observable limits, owners, safeguards, and actions, not exact headings or phrase matches. |
| Generic-advice resistance | PASS | Generic delegation advice cannot satisfy the company-specific taxonomy, decision boundaries, interface, escalation, coverage, audit, dated test, safeguards, and four thresholded closure results. |
| Predeclared 5 + 5 design | PASS | Five fresh no-skill and five fresh guided responses meet the five-repetition minimum. Independent contexts and hidden criteria reduce contamination and coaching. The identical prompt isolates the guidance condition. |
| Normalized threshold | PASS | With five criteria across five responses, `guided mean - no-skill mean >= 0.20` requires five net criterion-pass gains across 25 arm-level criterion decisions: one additional criterion per response on average. That is a clear material-effect gate for this microtest. |

## Criterion separation

1. Present problem diagnosis, intervention, and rejected/deferred structure.
2. Evidence discipline and causal uncertainty.
3. Target decision-rights operating contract.
4. Time-bounded pilot execution and safeguards.
5. End-of-pilot decision closure with result-specific thresholds, owners, and actions.

Continuity and qualified security/contract review appear in both C3 and C4 because one tests durable ownership/review and the other tests pilot safeguards. A context-free mention must not receive both credits. Likewise, C4's measures establish what the pilot observes; C5 separately requires branch thresholds and next actions.

## Grading guardrails

- Generate every response in fresh context with no rubric criteria, prior outputs, or intended answer visible.
- Read each response and make every criterion judgment semantically; do not use keyword counts.
- Do not infer omitted dates, owners, limits, thresholds, or actions.
- Score C3 on operating design, C4 on pilot design, and C5 on closure logic.
- Normalize each response as criteria passed divided by five, compare arm means, and require a guided-minus-control difference of at least `0.20`.

## Nonblocking cautions

- Five samples per arm are sufficient for a wording microtest, not a precise population-effect estimate. Retain raw outputs and per-criterion judgments to inspect variance.
- The criteria are intentionally conjunctive. Sensible prose does not earn a pass when a required owner, date, limit, safeguard, threshold, or next action is absent.

## Final verdict

**PASS.** The rubric is mechanically valid, chronologically and arithmetically coherent, natural, answer-leakage resistant, construct-aligned, semantically gradable, and resistant to generic advice. The predeclared independent `5 no-skill + 5 guided` design with hidden criteria and a normalized improvement threshold of `>= 0.20` is sound for the intended paired-prompt wording microtest.
