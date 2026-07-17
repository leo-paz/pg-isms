# Independent forward review — attempt 6

Auditor: `capital-forward6-auditor-001`  
Model: GPT-5 Codex  
Scoring: strict binary conjunctive; a criterion earns 1 only when every clause is explicit. No inference or generic-prose credit.

## Frozen result

| Case | Vector | Score |
|---|---:|---:|
| scenario-01 | `11111` | 5/5 |
| scenario-02 | `11111` | 5/5 |
| scenario-03 | `11011` | 4/5 |
| scenario-04 | `01111` | 4/5 |
| scenario-05 | `11111` | 5/5 |

Bit string: `1111111111110110111111111`  
Total: **23/25**

The vector was frozen before narrative review in `independent-vector-freeze.json`; its SHA-256 is `084adc10c2d76f106bf1c14246a6dfd407c4c3051309d090f4551bda448055c8`.

## Integrity

| Check | Result | Finding |
|---|---|---|
| Attempt | Pass | All four permitted forward manifests identify attempt 6. |
| Hash chain | Pass | Computed cases, plan, package-freeze, and generation-attestation hashes match every declared link. |
| Responses | Pass | All five computed response hashes match both frozen response records and are unique. |
| Counts | Pass | Words/bytes are 902/8853, 798/8134, 956/8717, 820/7947, and 929/9030; all match and remain at or below 1200 words. |
| Timestamps | Pass | Every response birth epoch equals mtime; responses follow the plan/package freeze and precede attestation/final generation freeze. |
| Isolation | Pass | No baseline, scorer artifact, prior-attempt directory, skill/source/provenance file, adjudication/review feedback, or git history was accessed. |

## Criterion judgments

| Criterion | Score | Evidence and judgment |
|---|---:|---|
| scenario-01.1 | 1 | Lines 5, 11–14, 24, 28–34, and 46 select the non-acute capital route, bound F0/S1, and count conversation interest as zero cash/demand. |
| scenario-01.2 | 1 | Lines 9–18 classify all supplied facts/statements and provide full controls for U1/U2. |
| scenario-01.3 | 1 | Lines 17 and 22–34 define the complete T1 thesis, ranges, envelope, alternative, adviser checks, and labeled assumptions. |
| scenario-01.4 | 1 | Lines 38–48 define the bounded batched process, tiers, calendar, controls, references, time cap, protected work, and truthful conduct. |
| scenario-01.5 | 1 | Lines 34 and 52–57 provide first-true branches plus G0/ZaR/ZaE/ZcR/ZcE closing gates and preserved options. |
| scenario-02.1 | 1 | Lines 5, 11–18, and 35–37 make terms primary, preserve unsigned/deadline/no-deal facts, and gate work through qualified owners. |
| scenario-02.2 | 1 | Lines 13, 15, 24, 27–31, and 42 give 11.11%/11.29% and explicitly model pool, participation, anti-dilution, and cap-table effects. |
| scenario-02.3 | 1 | Lines 11, 14–18, 27–31, and 39–46 separately compare all required economic, control, reference, certainty, and unknown-term dimensions. |
| scenario-02.4 | 1 | Lines 16, 24, and 39–46 establish the precommitted counter/walk envelope, including information/pro-rata and funding fit. |
| scenario-02.5 | 1 | Lines 25, 35, and 50–55 provide first-true branches, signed/completion evidence, consequences, synchronized facts, and preserved options. |
| scenario-03.1 | 1 | Lines 5, 11–16, 24–29, and 40 route from burn/flat revenue/churn/time-to-floor to survival and assign zero cash to financing indications. |
| scenario-03.2 | 1 | Lines 11–29, 35–40, and 46–49 provide the complete route-away handoff, cash floor/scenarios, H0, and early A5 switch. |
| scenario-03.3 | 0 | Lines 5 and 35–40 pause hires, sequence renewal/retention, protect customer support, and fully specify actions, but never explicitly protect **product continuity**. |
| scenario-03.4 | 1 | Lines 15, 18, 29, 40, and 46 bound materials/qualification/distraction, defer valuation/full launch, and provide the dated H0 handoff. |
| scenario-03.5 | 1 | Lines 18, 29, and 44–49 give separated survival branches, adviser gates, dates, options, and a conditional financing handoff. |
| scenario-04.1 | 0 | Lines 5, 15–17, and 24–30 choose the capital-heavy route, reject software-seed/$18m/next-summer claims, and count all interest as zero cash/demand, but never expressly reject **ramen-profitability or weekly-evidence defaults**. |
| scenario-04.2 | 1 | Lines 11–20, 26–36, and 40–42 build the dated model from all required capital/runway inputs and controlled unknowns. |
| scenario-04.3 | 1 | Lines 13–14, 17, 27–36, and 56–59 gate sizing on August 15 evidence and supply ranged/staged/no-raise/delay alternatives. |
| scenario-04.4 | 1 | Lines 16 and 44–50 segment all three investor types across every required fit, diligence, horizon, control, conflict, confidentiality/IP, exclusivity, and reference dimension. |
| scenario-04.5 | 1 | Lines 28, 42, 50, and 54–59 provide separated technical/financing branches, cash/route consequences, truthful communications, review gates, and preserved options. |
| scenario-05.1 | 1 | Lines 5, 12–13, 17–18, and 32–37 preserve the non-rescue, signature, expiry, freedom, pressure, and adviser facts. |
| scenario-05.2 | 1 | Lines 16, 25, 32, 39, 47, and 54–57 stop/verify/correct both funds, preserve the audit trail, gate acceptance, and branch on response. |
| scenario-05.3 | 1 | Lines 14–18, 24–28, and 41–48 compare every required offer, partner, control, certainty, confidentiality, unknown-term, and adviser dimension. |
| scenario-05.4 | 1 | Lines 25, 32, and 41–48 provide the weighted precommitment, protect operating work, and require references plus document/cap-table review. |
| scenario-05.5 | 1 | Lines 25 and 52–57 provide separated close/counter/decline branches with owners, dates, corrected disclosure, signed/cleared-funds evidence, consequences, and preserved options. |

The machine-readable review with the same frozen vector and per-criterion evidence is in `independent-review.json`.
