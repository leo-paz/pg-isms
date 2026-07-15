# Strict held-out score: org-heldout-attempt-001

Scorer: `/root/org_heldout_scorer`
Role: fresh strict held-out scorer
Scored: 2026-07-15T20:38:06Z

## Scope

Only these four inputs were read:

- `evals/building-and-evolving-organizations/heldout/skill-freeze.json`
- `evals/building-and-evolving-organizations/heldout/case.json`
- `evals/building-and-evolving-organizations/heldout/generation-plan.json`
- `evals/building-and-evolving-organizations/heldout/response.md`

The skill/runtime contents, baseline/forward/microtest artifacts, sources, provenance, other skills, author/prompt-review notes, existing score/review files, git history/diff, and intended answers were not inspected. Scoring is strict binary: every pass-condition conjunct must appear; no generous inference.

## Integrity: PASS

| File | SHA-256 | Bytes | mtime UTC |
|---|---|---:|---|
| `skill-freeze.json` | `bcb1ca3b52709df747a76055d0d5c553930ce5c4a84d60d52482ab78e340c3e2` | 806 | 2026-07-15T20:20:22Z |
| `case.json` | `b2aa55d28c2d3f657896da59ccf9dc99d6e9cb390ae153dc06293e50251ceea9` | 5,716 | 2026-07-15T20:30:14Z |
| `generation-plan.json` | `017c6ad5d03bcdf3328b5d8df90194806a558dc52ce34b7dc279d1b8741eca9a` | 3,989 | 2026-07-15T20:31:11Z |
| `response.md` | `9c30c0cc1ccb4d8fc4783381f668aea0244a7d0b4640d451fa52e398d44a2020` | 19,914 | 2026-07-15T20:36:04Z |

- All three JSON files parse.
- The computed skill-freeze hash/bytes match the declarations in the case and generation plan.
- The computed case hash/bytes match the generation-plan declaration.
- The decoded prompt independently recomputes to `97cd9558af2c7793c752ad09eb039609124c198ce75d07f86a4efb1e65ec93a5`, 2,189 bytes, and 352 `wc -w` words, matching its declarations.
- The criteria array independently recomputes under the declared canonicalization to `661921dd17cee33481c0dcac2f4bbf309297cd0290b779827ca583e2ea9f9242`, 2,556 bytes, and five criteria, matching its declarations.
- The skill and runtime hashes/bytes agree across the three JSON declarations. Their contents were forbidden, so they were not independently hashed. Likewise, the declared context hash `690a3e0b755bc5860600e851e10b022cab0482a242fc0cfabd5a9b081b6a1279` and 17,988 bytes cannot be independently recomputed without those forbidden contents; the generation plan does declare the scoped input assembly, allowed/forbidden inputs, and `criteria_visible_during_generation=false`.
- The response's first two lines exactly match the required headers. It has no trailing spaces or tabs. Its final two bytes are `2e 0a`, proving exactly one file-final LF.
- Freeze chronology is consistent in both declarations and mtimes: skill freeze declared 20:20:15Z (mtime 20:20:22Z), case authored 20:22:55Z (mtime 20:30:14Z), generation frozen 20:30:42Z (plan mtime 20:31:11Z), response mtime 20:36:04Z.

## Score

Exact vector in C1-C5 order: **`[0, 0, 1, 1, 1]`**

### C1 — FAIL (0)

Present:

- The decision header explicitly selects `building-and-evolving-organizations` with `decision-rights` as primary route/branch.
- The survival state does not declare an emergency from the unstress-tested forecast.
- Finance owns an August 18 downside stress test.

Missing strict subcheck:

- No finance-test result or explicit switch condition says when `managing-runway-and-survival` would become primary. The response only makes the test a prerequisite for later hiring/capacity choices.

### C2 — FAIL (0)

Present:

- The ledger separates Observed, Claimed, and Unknown.
- Observed includes both dated delay and delegation records.
- Claimed includes the investor assertion, recruiter estimates, and finance forecast.
- Unknown includes sustainable operations-lead load.
- The conclusion supports an approval-queue mechanism, not a pilot gap, while retaining weather and other rivals.

Missing strict subchecks:

- The explicit Unknown rows do not place forecast robustness or the stress-test result in Unknown.
- The explicit Unknown rows do not place whether survival binds in Unknown.

### C3 — PASS (1)

The operations lead remains the named end-to-end campaign outcome owner and receives bounded inside-plan time-window and preapproved-envelope route authority. Founder exceptions, pre-execution notification/logging, next-business-day escalation, absence fallback, backup/succession work, and customer continuity are explicit. Flight-safety and security remain independently owned non-bypassable vetoes, and aviation-adviser/counsel review is required before go-live or protection changes.

### C4 — PASS (1)

The July 19-September 1 test is exactly 45 calendar days, with August 4/August 18 intermediate and September 2 final decisions. It names baseline-linked measures, artifacts, owners, and observable Continue/Adjust/Add-capacity/Reverse thresholds. Add capacity requires a sustained residual workload plus a service miss/latency gap after authority/interface fixes. Reversal covers protection bypass, harm, accountability-evidence loss, and continuity-impacting mishandled delay.

### C5 — PASS (1)

The record rejects a COO search because no current executive/capacity case is established and rejects a launch committee because it adds coordination without fixing ownership. It preserves a fully costed role-charter path only after the residual-gap predicate, retains unresolved unknowns and switch/eligibility conditions, and names next owners for every result branch.

## Threshold verdict

- Positive bits: **3/5**
- Required: **4/5**
- Threshold: **FAIL**
- Held-out transfer: **FAIL**
- Response: `9c30c0cc1ccb4d8fc4783381f668aea0244a7d0b4640d451fa52e398d44a2020`, **19,914 bytes**
