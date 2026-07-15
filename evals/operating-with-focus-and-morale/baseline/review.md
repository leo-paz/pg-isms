# Operating with focus and morale: RED baseline review

## Accepted result

The no-skill baseline is accepted at **14/30** (`0.466667`). The six vectors are `10000`, `11011`, `10000`, `10101`, `10000`, and `10111`. Every case misses at least one criterion, so the baseline is RED-valid.

## Chronology and blindness

1. The six canonical cases were frozen at `2026-07-15T22:41:04Z`, before response generation. The expected skill package did not exist.
2. Six distinct fresh-context generator tasks received only their exact scenario prompts. The generation contract hid criteria and disallowed skill files, source evidence, prior outputs, and repository context.
3. The first six completions were frozen without quality resampling. The attestation and manifest froze their hashes at `2026-07-15T22:46:31Z`, before scoring.
4. A distinct blind scorer, `/root/focus_baseline_scorer`, read the frozen cases, plan, attestation, manifest, and responses, then produced all 30 strict binary decisions. It did not read the taxonomy, skill, source material, prompt gate, intended answers, other evaluations, or generator history.
5. An independent reviewer completed Stage A before opening the scorer artifacts. Stage A was frozen at SHA-256 `c0c5b3dabb5cd9a018cd451c708b53ae0e9925db8f48f0a53ba41b475502844f`.
6. After the Stage-A freeze, the independent reviewer compared its 30 decisions with the scorer. Twenty-eight bits agreed. The two disagreements were both Stage-A undercalls in scenario 02; after line-level adjudication, the reviewer accepted the scorer's `1` decisions for criteria 4 and 5. No scorer bit required correction.
7. The accepted vectors, decisions, score, misses, and RED verdict are canonicalized in `summary.json` and the six files under `scorecards/`.

Historical properties such as fresh context and first-completion capture cannot be replayed from files. The integrity review establishes that the frozen plan, attestation, and manifest attest those properties consistently and contain no contradictory evidence.

## Integrity

| Frozen artifact | SHA-256 |
|---|---|
| Canonical cases | `f77e14ed626c40a49e051aa535feb5dd9dad4597a4761e5118feb1acea63c8c5` |
| Generation plan | `f84f0b565b617ea6e99b873edf7fdba8e171f2d178de0c649209f90ce414a8f9` |
| Generation attestation | `107c8cdf8aa0b3d9a09571fb2a70ec22b5063d939a32ae0382a13d4dbcdc5d96` |
| Manifest | `4d3af3395f316b5303188166821d053340ba0669495ecc4df0edee2b6a96802f` |
| Prompt-only aggregate | `5dcc5d515b9453ae4261017e10afd382ac03013cb7a9ab1061014c502d9d9a72` |
| Blind scorer JSON | `854d42b449fa785b22a9d563bbcf612715288cc7cf4965ff71ab72b8f69d221a` |
| Independent Stage A | `c0c5b3dabb5cd9a018cd451c708b53ae0e9925db8f48f0a53ba41b475502844f` |
| Independent final review | `e7729eb8f66920e0ce625e53703361f7be2c17d20ba0ee5d610ba58b53c14c5d` |

All six prompt files byte-match their canonical prompt projections. All six response hashes match the manifest, all response bodies are unique, all responses are below the 1,200-word limit, and response birth times equal modification times. The scorer is distinct from the six generator tasks. The skill package was absent both at freeze and scoring.

| Case | Response SHA-256 | Words | Final vector |
|---|---|---:|---:|
| 01 | `7a9188ee7dfd44861cec31cf01b68f3ac8ffc6063eaf96699a734c48d92c1f14` | 1015 | `10000` |
| 02 | `27805971e0593239d2d5bad66fce58961704cfdae1c7e24849948f7146ec50fa` | 809 | `11011` |
| 03 | `b97ef2b64f8f6cfd9ac1a707ed532579fcd58e3f573fa1568889093d58e6d625` | 804 | `10000` |
| 04 | `37d38d3a2151a786985fc5563d86a2837eed1acb68ed9b9d568bc755b1750f4a` | 578 | `10101` |
| 05 | `5ab8c95d267a53734af40599d9c94d96fd62aa134f76e41f5ddaebfc8e93128e` | 911 | `10000` |
| 06 | `3d6ffae0e37236382a0fdac3222ba3aea590f99d015656bae14b325b61da61c5` | 824 | `10111` |

## Scenario 02 Stage-A adjudication

Stage A scored scenario 02 as `11000`; the blind scorer scored it `11011`. The final vector is `11011`.

- **Criterion 4, `0 → 1`:** Stage A required a more formal recurring calendar than the criterion states. Days 6–15 explicitly schedule build/test work, unrelated features are frozen, clinic-user contact recurs across Days 1–5, 6–15, and 16–25, and the response explicitly restores a normal workweek with no mandatory nights. All conjuncts are present without inference.
- **Criterion 5, `0 → 1`:** Stage A over-required numeric precision. The response supplies functional owners, Days 1–5 baseline work, an explicit alert-open target from 22% to at least 50%, twice-weekly and end-week checkpoints, a Days 26–30 decision, and observable continue/adjust/pivot conditions. Role owners and relative day/week dates are valid because the prompt supplies neither personal names nor a calendar start date.

The correction changes the independent preliminary total from 12/30 to the accepted 14/30. It does not change the scoring contract; it applies the existing conjunctive rule without adding requirements absent from the criteria.

## Fairness and leakage

The prompts contain the canonical scenario text only: no criteria, rubric terms, taxonomy workflow names, skill content, or source evidence. Every criterion is answerable from the supplied scenario and requested operating decision. Literal taxonomy names are not required; semantic routing received credit in all six criterion-1 decisions. Role owners and relative dates also received credit consistently.

No integrity, prompt-leakage, contract-fairness, or arithmetic defect invalidates the RED result.
