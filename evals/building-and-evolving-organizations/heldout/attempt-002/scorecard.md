# Held-out attempt 002 strict score

Scorer: `/root/org_heldout2_scorer`  
Case: `org-heldout-attempt-002`  
Scored: `2026-07-15T21:05:58Z`  
Policy: every conjunct must be explicit; no generous inference.

## Scope

I read only the authorized `skill-freeze.json`, `case.json`, `generation-plan.json`, `prompt.txt`, and `response.md`. I did not inspect attempt 001; skill/runtime contents; baseline, forward, or microtest artifacts; sources/provenance; other skills; author/prompt-review notes; existing score/review files; git history/diffs; or intended answers. No canonical file was edited.

## Integrity: PASS

| Authorized whole file | SHA-256 | Bytes |
|---|---|---:|
| `skill-freeze.json` | `e542c6c6851be2a658bf52e93153324ef7d772f2ecc00f20a99053bdd4ed1cc1` | 747 |
| `case.json` | `905f08d79020052395cc8c97f037078ed8710042a953cb78fed701dce6e305fc` | 9485 |
| `generation-plan.json` | `3081252bde4374020e22b30bf87b438efcabf44cd64a7824d8fb4c9fbe66f088` | 4025 |
| `prompt.txt` | `0bbf1d70b9dd670c9ca23b7495da58b0144275933c289b7638133da4bc55299f` | 4509 |
| `response.md` | `56876ecb2325a221b76d228fe2573caded5e5a4a72e27e915eabc61a86146885` | 22353 |

Accessible scoped declarations also verify:

- Decoded prompt: `6ddde934d4f7d12994ffea10121f675e7826780d15208794e0787adba85fc457`, 4508 bytes, 720 words.
- Minified hidden-criteria JSON: `b86eeacc7d30787429808c76e0a17fc7b3c64290afc216a40669bdcfc9cf6dc8`, 3963 bytes.
- `prompt.txt` is byte-identical to the decoded case prompt plus exactly one LF.
- Skill declaration is consistently `2a1e0a27562aa3cfac61ce280a833bd538e4ad633267e238d8cf7bed695e572a`, 3718 bytes, across the authorized freeze/case/plan. Runtime declaration is consistently `6fc8f66eb3b3aea79b1bab9b67602887e0bbb17a00e302e6982fb48378e7bd5b`, 12033 bytes. Their canonical contents were intentionally not inspected.
- The first two response lines exactly match the required headers. There are no trailing spaces/tabs, no CR bytes, and the final two bytes are `2e0a`, proving exactly one file-final LF.
- Declared chronology is skill freeze `20:40:32Z`, case authoring `20:48:17Z`, and generation freeze `20:55:33Z`. Authorized-file mtimes are strictly ordered freeze `<` case `<` prompt `<` plan `<` response, and the response birth/mtime is `21:03:19Z`. Freeze-before-response passes.

## Strict vector: `[1, 0, 0, 0, 0]`

| Criterion | Bit | Strict evidence and missing conjuncts |
|---|---:|---|
| C1 | 1 | Lines 9-11 make Leah's role evolution the primary eight-week test before either search. Line 18 rejects survival as binding; lines 48 and 70 reject stage/investor precedent and coach/leave as primary causal routes. |
| C2 | 0 | Lines 18-42 substantially separate records, claims, and unknowns. However, line 40 leaves candidate ability/fit to a later selection process without a complete owner/date-by-final-review/threshold/effect contract. It also dates the residual role decision September 21, after the September 14 final review stated at line 76 and using the September 18 release afterward. |
| C3 | 0 | Lines 56-66 preserve one owner and define retained decisions, delegation, escalation, backup, absence handling, and artifacts without a new layer. But recruiting is 5% in the observed baseline (line 29) and remains at or below 5% in the target (line 68), so the allocation does not materially increase recruiting as required. |
| C4 | 0 | The response defines the bounded test and all four decision outcomes with substantial numeric controls. Yet recruiting latency appears only as the 13-day historical baseline at line 32; no forward artifact, target, or success/failure threshold measures recruiting latency during the pilot. |
| C5 | 0 | Current access/customer protections, qualified reviewers, a job-relevant scorecard, accessible structured assessment, and independent ratings are present. A later search still lacks an explicit bias review and does not expressly prohibit polish or protected-trait proxies; rejecting pedigree and charisma alone is insufficient. |

## Threshold and transfer verdict

Positive bits: **1/5**. Required: **4/5**. Threshold: **not met**. Transfer verdict: **FAIL**.
