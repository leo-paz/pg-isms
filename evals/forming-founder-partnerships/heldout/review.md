# Independent held-out review — attempt 028

Reviewer: `/root/founder_heldout_independent_review_028`

## Stage A — blind record (fixed before score-artifact access)

Stage A read only canonical `skill-freeze.json`, `case.json`, `generation-plan.json`, `response.md`, `skills/forming-founder-partnerships/SKILL.md`, and `skills/forming-founder-partnerships/references/runtime-contract.md`. No prior attempt, baseline, forward test, microtest, unrelated evaluation, `score.json`, `scorecard.md`, or prompt-review content was opened before this record was fixed.

### Independently reproduced hashes and byte counts

| Hash domain | Bytes | SHA-256 |
|---|---:|---|
| whole `skill-freeze.json` | 791 | `3412d690deb77e9d2033408516669908a040a7a2d6a61b36095690e8995978b2` |
| whole `case.json` | 7,018 | `402133067e51bea31fb5fca46694f3ff1d341463a1ca852b6d5f07f9d8c0ea1a` |
| whole `generation-plan.json` | 5,520 | `24ab506c8fad2ca77b182e9293f5eb18dbde9b5d54e128558951e3e06d4d86e8` |
| whole `response.md` | 14,767 | `b863b61d340af302b745be460b404fa99ca67f3b45c5ad9c6f15a0af8f94471f` |
| whole `SKILL.md` | 3,762 | `a1bd8c331837d5e8a1177ab774b7d4f3e6a7a6d2d11b4293333fed445d77d584` |
| whole `runtime-contract.md` | 11,011 | `9fef3fe9b7e3ef19dba864698046322b50cdf83aa61178934e5476aa17fb3a38` |
| decoded prompt UTF-8, no added LF | 2,058 | `77e5827ab9a60917f8d7ce35611060760c9e638e7f7f863e7512aa2421fa9a8c` |
| canonical hidden-criteria array: recursive key sort, compact JSON, array order preserved, no LF | 3,938 | `28836b4f6f6c4b39a54869afe1c95964a874bb05fd67bcd44ea5ba80bbefcd07` |
| exact assembled generation context | 16,879 | `dae9317209d2ee9fdc25cd1349fbfcc17c612a172d525f6aa87ed94a754b239d` |
| response-body domain, excluding envelope, separator, and file-final LF | 14,458 | `097f68fa0629c54f74bd1b2b56b0aa016e7e4c793747476bf67ab4787c9d54fa` |

The prompt has 340 whitespace-delimited words and no terminal LF. Both frozen skill inputs have exactly one terminal LF. Reassembling `# Skill\n\n<skill without final LF>\n\n# Runtime contract\n\n<runtime without final LF>\n\n# User request\n\n<prompt>\n` reproduces the declared context exactly. Every Stage A hash and byte declaration in the freeze, case, and plan matches independent recomputation.

### Envelope, body, and whitespace

The response has exactly eight headers, in this order: `canonical_task`, `sample_id`, `arm`, `context_id`, `dispatched_at`, `completed_at`, `response_sha256`, `response_bytes`. The four fixed values match the plan. One empty line separates the envelope from the body. The declared body hash and 14,458-byte count match independent extraction. The body has zero leading blank lines, zero trailing blank lines, zero lines ending in spaces or tabs, zero CR bytes, and the file has exactly one final LF.

### Chronology and identity separation

The declared chronology is valid and monotonic: pre-author skill freeze `2026-07-15T13:46:31Z`; case authorship `13:46:49Z`; independent prompt review `13:48:25Z`; generation-plan creation and freeze `13:49:06Z`; dispatch `13:49:49Z`; completion `13:53:47Z`. Plan creation equals plan freeze as declared, and all other transitions are strictly later.

The named roles are distinct: case author `/root`; prompt reviewer `/root/founder_heldout_prompt_gate_028`; generator `/root/founder_heldout_generator_028`; scorer `/root/founder_heldout_scorer_028`; final reviewer `/root/founder_heldout_independent_review_028`. The prompt-review result recorded in the frozen plan is PASS with no findings; its underlying artifact is reserved for Stage B verification.

### Prompt naturalness and leakage

Blind verdict: **PASS**. The prompt is a plausible first-person financing/governance request with concrete offer terms, accountable people, pending reviews, and dated decisions. It contains no criterion labels, scoring language, answer template, evaluation instructions, expected verdict, or reference to hidden artifacts. Its density is justified by the requested comparison and governance decision rather than leaked rubric structure.

### Strict conjunctive criterion vector

Blind vector: **`[C1=1, C2=1, C3=1, C4=1, C5=0]` = 4/5**.

- **C1 PASS.** The response makes `raising-and-governing-capital` primary, explicitly treats the July 11 founder agreement and absence of trust/commitment dispute as settling the partnership question, opens no candidate/existing-team/ownership/work-trial branch, and supplies the correct future switch across founder status, relative founder control, departure, trust, commitment, ownership intent, and a founder-to-founder role agreement affecting continuation.
- **C2 PASS.** It records Erin's July 14 completion of the model, the July 17 management review, and Priya's July 18 document/legal-effect/actual-terms review; the dated events are scheduled while each result is explicitly unknown pending completion.
- **C3 PASS.** It names Erin as financing-process owner, gives Nadia's July 21 decision date, preserves the July 24 equity and July 25 debt expiries, assigns Erin the November 28 cash test and the below-$1.7-million December 1 reopening rule, and records Nadia and Luis's joint September 1 financing review.
- **C4 PASS.** Nadia alone owns the business decision. Priya is identified within the qualified-current-counsel route and is limited to document review, legal effect, actual terms, legal verification, and related legal questions. Erin and Luis are not made decision makers, and Nadia is not assigned Priya's legal review.
- **C5 FAIL.** The response accurately carries the remaining current-state, equity, debt, control, runway, and static-illustration facts, and adds only a bounded derived comparison. But strict C5 is conjunctive: the response states the debt fee only as `$36,000` and nowhere carries the stated `2%` fee term. Dollar equivalence does not satisfy the requirement to carry both `2%/$36,000`.

### Blind threshold and transfer verdict

The strict score is **4/5**, meeting the predeclared minimum of 4 positive bits. With independently verified integrity PASS and prompt-naturalness/no-leakage PASS, the blind held-out transfer verdict is **PASS**. This verdict is fixed before Stage B comparison; any score-artifact disagreement, hash discrepancy, chronology conflict, or integrity problem will change the final independent verdict to FAIL.

## Stage B — score-artifact comparison

Stage A above was fixed before these artifacts were opened.

### Stage B artifact hashes

| Whole artifact | Bytes | SHA-256 |
|---|---:|---|
| `score.json` | 9,737 | `ec7e9fbc1023dbd29e3f4e429e3ff495c5af5c628232a10b730878c65adec0c4` |
| `scorecard.md` | 7,264 | `d1514d688c6d8759310e62774815dc47d69807e30aa9fc1c0d2899b603817eab` |
| current `prompt-review.json` | 5,254 | `cbd7fb98d3308734faea6cfd9e0d2b9cff26685394cc082cdf5deeb0ca9a62c5` |

The prompt-review artifact hash exactly matches the hash frozen into `generation-plan.json`. Its declared case, freeze, skill, and runtime hashes and byte counts match the Stage A recomputations. All ten prompt-gate checks are PASS, `blockers` is empty, and `strict_verdict` is PASS. Its naturalness, arithmetic, chronology, no-leakage, isolated-criteria, C1 route-away, and C5 calculation-cap rationales are consistent with the blind analysis.

### Field-by-field comparison

- **Integrity:** `score.json` and `scorecard.md` reproduce every whole-file and scoped-domain hash and byte count in Stage A. They agree on the exact eight-line response envelope, body domain, timestamp order, separator, blank-line counts, trailing-whitespace result, and single final LF. No hash or integrity disagreement exists.
- **C1:** both score artifacts assign PASS for the capital route, settled partnership, omitted partnership branches, and complete future founder-specific switch. This exactly matches blind C1.
- **C2:** both assign PASS for model completion and the scheduled-but-unknown July 17 and July 18 reviews, including Priya's document/legal-effect/actual-terms scope. This exactly matches blind C2.
- **C3:** both assign PASS for Erin's process ownership, July 21 decision date, both expiries, September 1 joint review, and the November 28/December 1 cash trigger. This exactly matches blind C3.
- **C4:** both assign PASS because Nadia alone retains the business choice while Priya remains in the qualified-current-counsel document/legal lane. This exactly matches blind C4.
- **C5:** both assign FAIL solely because the response carries `$36,000` but omits the required `2%` fee term. Both otherwise find the required economics/control/model outputs accurate and find only one new derived numeric output, `$316,000 below`. This exactly matches blind C5 and its rationale.
- **Auxiliary verdicts and threshold:** both artifacts report vector `[1, 1, 1, 1, 0]`, 4/5 positive bits, minimum 4, threshold met, integrity PASS, naturalness/no-leakage PASS, overall PASS, and held-out transfer PASS. Every verdict agrees with Stage A.

### Completed chronology

`score.json` adds strict scoring by `/root/founder_heldout_scorer_028` at `2026-07-15T13:55:53Z`, after response completion at `13:53:47Z`. This independent review completed at `2026-07-15T14:02:43Z`, after scoring. The full sequence remains monotonic, and the prompt reviewer, generator, scorer, and final reviewer remain identity-separated.

## Final independent verdict — PASS

There is no Stage A/Stage B disagreement, hash discrepancy, chronology conflict, identity-separation failure, envelope/whitespace defect, prompt leakage, or other integrity problem. The canonical attempt earns 4/5 strict bits, meets the 4-bit threshold, passes both required auxiliary gates, and therefore independently passes held-out transfer.
