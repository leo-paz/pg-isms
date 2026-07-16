# Blind review — microtest attempt 005

- Scorer: `focus-micro5-blind-scorer`
- Locked: `2026-07-15T19:45:40-07:00`
- Status: locked before unblinding; no arm identities read or guessed
- Policy: strict binary conjunctive scoring; no inference and no partial credit
- Criterion order: `C1 C2 C3 C4 C5`

## Input hashes

| Input | SHA-256 |
|---|---|
| `microtest/prompt.txt` | `77d6384adc126690827efe4c5c8771e318ba88ee7c31a205a449e5e88d704638` |
| `microtest/rubric.json` | `678993e0559d0f40e18a51ec8a0559514085c8439b99c2f75573f739b4acb961` |
| `microtest/blind/slot-01.md` | `d8f36db46ba0a3f85830fec8185562e8186b9bb4b56a5177f1f9f50b0885b154` |
| `microtest/blind/slot-02.md` | `05f556fca64d1a45141f111b08dedc207835fb610f35595e620d203563bfd523` |
| `microtest/blind/slot-03.md` | `b65f47fd83e35918c7d51708fa6a4d16806ee05b5c28f7003e6e9963404f3fe9` |
| `microtest/blind/slot-04.md` | `173e1b29a3b59aace8b0b0e1838adc5d4f50927d714406d79d79a0e3ec824b2e` |
| `microtest/blind/slot-05.md` | `c54eab09d4521425ce6949c8576c15a6154cb724aedfe9b21ca3b3d018c21405` |
| `microtest/blind/slot-06.md` | `e7f3109f3d87a4f610b4f37a068bd8bb07d2cec860da08eb336062111b5fcb97` |
| `microtest/blind/slot-07.md` | `bf655687ce3c241378df938237ccc78e1b1c5026da211f6610f79ac5d30f574b` |
| `microtest/blind/slot-08.md` | `9d7b8f43777568bd477635c70cd672de1b745c780bce44de5c72e702fc2d8488` |
| `microtest/blind/slot-09.md` | `6a301504b84d1e22e99e08f1942644e201f64df73494c3f9ee82cbecb3304b13` |
| `microtest/blind/slot-10.md` | `5c8a32595307efea1deb88b2acfae056152b62ac030c238098d95922a2930adb` |

## Locked vectors and totals

| Slot | C1 | C2 | C3 | C4 | C5 | Vector | Total |
|---|---:|---:|---:|---:|---:|---|---:|
| slot-01 | 1 | 1 | 0 | 1 | 0 | `[1,1,0,1,0]` | 3 |
| slot-02 | 0 | 0 | 0 | 0 | 0 | `[0,0,0,0,0]` | 0 |
| slot-03 | 0 | 0 | 0 | 0 | 0 | `[0,0,0,0,0]` | 0 |
| slot-04 | 0 | 1 | 1 | 0 | 0 | `[0,1,1,0,0]` | 2 |
| slot-05 | 0 | 0 | 0 | 0 | 0 | `[0,0,0,0,0]` | 0 |
| slot-06 | 0 | 0 | 0 | 0 | 0 | `[0,0,0,0,0]` | 0 |
| slot-07 | 0 | 0 | 0 | 0 | 0 | `[0,0,0,0,0]` | 0 |
| slot-08 | 0 | 1 | 1 | 1 | 0 | `[0,1,1,1,0]` | 3 |
| slot-09 | 0 | 1 | 1 | 0 | 0 | `[0,1,1,0,0]` | 2 |
| slot-10 | 0 | 1 | 1 | 0 | 0 | `[0,1,1,0,0]` | 2 |

Total: `12/50`.

## Per-slot rationale

### slot-01 — `[1,1,0,1,0]` (3)

- C1 `1`: Concrete route gates exclude all alternate routes; observations and claims are classified; U1-U8 contain owner, method, date, threshold, and effect; no inputs remain unclassified.
- C2 `1`: One outcome and one tactic have every required field; all three initiatives are separately owned, dated, and bounded; essential services are separately protected; proxies are rejected.
- C3 `0`: The incident-only two-hour exceptional push has no calendar end date, which is an explicit required conjunct.
- C4 `1`: Multiple morale mechanisms and a rival are tested; premise and tactic are distinct; all three measure classes are complete; every checkpoint explicitly says results are not yet observed and supplies rival, safeguards, and branch.
- C5 `0`: The stop row promises a newly dated return after closure but supplies no handoff/return calendar date now.

### slot-02 — `[0,0,0,0,0]` (0)

- C1 `0`: No complete fact-based route exclusion, full input classification, or owner/method/date/threshold/effect unknown ledger.
- C2 `0`: Initiative-specific owner/date/reopen fields and parts of the outcome specification are missing or implicit.
- C3 `0`: No recurring contiguous product block, complete continuity escalations, or dated queue-relief test before organization redesign.
- C4 `0`: The three complete measure records and checkpoint state/rival/safeguard/branch records are absent.
- C5 `0`: Branches lack their own owner, route, calendar date, and dated handoff/return fields.

### slot-03 — `[0,0,0,0,0]` (0)

- C1 `0`: Alternate routes and consequential unknowns are not handled with the complete required structure.
- C2 `0`: The test lacks an explicit dated absolute target, and initiative dispositions lack complete owner/date/reopen fields.
- C3 `0`: No recurring contiguous product block, complete escalation destinations, or dated pre-redesign queue test.
- C4 `0`: Required measure and checkpoint ledgers are absent.
- C5 `0`: Branch-specific owners, routes, and dated handoff/return conditions are absent.

### slot-04 — `[0,1,1,0,0]` (2)

- C1 `0`: Expo reopen evidence has no complete unknown row; the exact September 10 event date is also not preserved.
- C2 `1`: One complete outcome/tactic, complete competing-work choices, protected essential obligations, and no proxy success evidence.
- C3 `1`: Recurring maker and teacher-contact cadence, complete supplied continuity, dated recovery, load removal, and a pre-redesign queue test are all explicit.
- C4 `0`: Future checkpoint result cells do not state an observed result or explicitly say `pending`.
- C5 `0`: The stop row has no return/handoff calendar date.

### slot-05 — `[0,0,0,0,0]` (0)

- C1 `0`: Alternate-route exclusion, full classification, and complete unknown records are missing.
- C2 `0`: Initiative dispositions do not each contain owner, date, and limit/reopen condition.
- C3 `0`: No recurring contiguous product block, complete continuity escalations, or dated pre-redesign relief test.
- C4 `0`: Complete three-class measures and checkpoint records are absent.
- C5 `0`: Branches omit per-row owner, route, and dated handoff/return fields.

### slot-06 — `[0,0,0,0,0]` (0)

- C1 `0`: Route exclusions and complete consequential-unknown records are missing.
- C2 `0`: Initiative dispositions and the consolidated outcome record are incomplete.
- C3 `0`: Continuity escalation destinations and a dated queue-relief test before organization redesign are absent.
- C4 `0`: Required measure and checkpoint records are absent.
- C5 `0`: Branch bullets lack dates, owners, routes, and dated handoff/return conditions.

### slot-07 — `[0,0,0,0,0]` (0)

- C1 `0`: No complete fact-based alternate-route exclusion or consequential-unknown ledger.
- C2 `0`: Dated baseline/target and initiative owner/date/reopen records are incomplete.
- C3 `0`: Product blocks, full escalation destinations, horizon-wide recovery, and a dated pre-redesign queue test are missing.
- C4 `0`: Complete measure and checkpoint records are absent.
- C5 `0`: Branch rows with all required fields are absent.

### slot-08 — `[0,1,1,1,0]` (3)

- C1 `0`: Investor diligence is omitted from classification, and the facilitator/teacher-mix rival has no complete unknown row.
- C2 `1`: Outcome/tactic, three initiative decisions, essential obligations, and proxy exclusions are complete.
- C3 `1`: Recurring product and teacher contact, supplied continuity, dated recovery with no exceptional push, load removal, and a pre-reroute queue test are explicit.
- C4 `1`: Mechanisms, premise/tactic split, complete measures, and explicitly pending checkpoints all satisfy the criterion.
- C5 `0`: The stop return is only to be dated later at routing, not given a calendar date.

### slot-09 — `[0,1,1,0,0]` (2)

- C1 `0`: The exact September 10 Expo date and Priya's catalog proposal are not explicitly preserved/classified.
- C2 `1`: The full outcome/tactic record, three dispositions, protected obligations, and proxy exclusions are present.
- C3 `1`: Recurring focus/contact, complete supplied continuity, dated recovery, removed load, and the July 21 queue test are present.
- C4 `0`: Checkpoints direct future recording but never explicitly label the results pending.
- C5 `0`: The stop row has no return/handoff calendar date.

### slot-10 — `[0,1,1,0,0]` (2)

- C1 `0`: Expo reopen economics has no complete unknown row, and the continuity gate cites nonexistent O29-O36 identifiers.
- C2 `1`: The outcome/tactic, initiative dispositions, essential obligations, and proxy handling are complete.
- C3 `1`: Recurring focus/contact, complete continuity, dated recovery without an exceptional push, load removal, and the July 23 queue test are explicit.
- C4 `0`: Checkpoint results are neither observed nor explicitly marked pending.
- C5 `0`: `owner-dated then` is not a return or handoff calendar date.

## Lock statement

These vectors and rationales were fixed from the anonymous slot texts and rubric before any arm mapping was viewed. No arm identity was inferred or recorded.
