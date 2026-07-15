# Held-out scorecard — forming-founder-partnerships attempt 028

## Verdict

- Vector: **[1, 1, 1, 1, 0]**
- Strict criteria: **4/5**
- Integrity: **PASS**
- Prompt naturalness and no leakage: **PASS**
- Threshold: **PASS** (`4/5`, with both required auxiliary verdicts passing)
- Held-out transfer: **PASS**

## Integrity reproduction

All values below were independently recomputed from only the permitted frozen files.

| Domain | SHA-256 | Bytes | Result |
|---|---|---:|---|
| Whole `skill-freeze.json` | `3412d690deb77e9d2033408516669908a040a7a2d6a61b36095690e8995978b2` | 791 | matches case/plan |
| Whole `case.json` | `402133067e51bea31fb5fca46694f3ff1d341463a1ca852b6d5f07f9d8c0ea1a` | 7,018 | matches plan |
| Whole `generation-plan.json` | `24ab506c8fad2ca77b182e9293f5eb18dbde9b5d54e128558951e3e06d4d86e8` | 5,520 | frozen input inspected |
| Whole `response.md` | `b863b61d340af302b745be460b404fa99ca67f3b45c5ad9c6f15a0af8f94471f` | 14,767 | frozen response inspected |
| Whole `SKILL.md` | `a1bd8c331837d5e8a1177ab774b7d4f3e6a7a6d2d11b4293333fed445d77d584` | 3,762 | matches freeze/plan |
| Whole `runtime-contract.md` | `9fef3fe9b7e3ef19dba864698046322b50cdf83aa61178934e5476aa17fb3a38` | 11,011 | matches freeze/plan |
| Decoded prompt, no added final LF | `77e5827ab9a60917f8d7ce35611060760c9e638e7f7f863e7512aa2421fa9a8c` | 2,058 | matches plan |
| Canonical hidden criteria | `28836b4f6f6c4b39a54869afe1c95964a874bb05fd67bcd44ea5ba80bbefcd07` | 3,938 | matches plan |
| Exact assembled context | `dae9317209d2ee9fdc25cd1349fbfcc17c612a172d525f6aa87ed94a754b239d` | 16,879 | matches plan |
| Response-body hash domain | `097f68fa0629c54f74bd1b2b56b0aa016e7e4c793747476bf67ab4787c9d54fa` | 14,458 | matches header |

The context was reproduced exactly as specified: `# Skill`, the skill without its final LF, `# Runtime contract`, the runtime contract without its final LF, `# User request`, the decoded prompt without an added terminal LF, the specified blank-line separators, and one context-final LF.

The response envelope has exactly eight headers in the required order and exact fixed values. Both timestamps are UTC RFC3339; dispatch at `2026-07-15T13:49:49Z` precedes completion at `2026-07-15T13:53:47Z`. There is exactly one separating empty line, no body-leading or body-trailing blank line, no trailing spaces or tabs, and exactly one file-final LF.

Chronology is valid: pre-author freeze (`13:46:31Z`) → case authorship (`13:46:49Z`) → separate prompt gate (`13:48:25Z`) → plan frozen before response (`13:49:06Z`) → separate generation (`13:49:49Z`–`13:53:47Z`) → separate strict scoring (`13:55:53Z`). Prompt reviewer `/root/founder_heldout_prompt_gate_028`, generator `/root/founder_heldout_generator_028`, scorer `/root/founder_heldout_scorer_028`, and planned independent reviewer `/root/founder_heldout_independent_review_028` are identity-separated.

## Prompt naturalness and no leakage — PASS

The independently recomputed whitespace word count is 340, matching metadata. The prompt is a coherent first-person CEO financing request containing plausible dates, roles, alternatives, economics, and governance facts. It contains no `C1`–`C5` identifiers, pass/fail or threshold language, skill-route names, response-envelope instructions, or references to hidden criteria, scores, reviews, or evaluation artifacts. Its density reflects a detailed financing brief, not rubric-shaped instructions.

## Strict binary scoring

### C1 — PASS (1)

- Response line 16: “**Primary route:** `raising-and-governing-capital`” and “not an unsettled founder relationship.”
- Response line 24: “`partnership-primary` is not active,” the July 11 note and absence of a trust/commitment dispute settle the current question, and no candidate, existing-team, ownership, or work-trial branch is opened.
- Response line 100 reopens founder-partnership work only if founder status, relative control, departure, trust, commitment, ownership intent, or a founder-to-founder role agreement affecting continuation becomes genuinely unsettled.

Misses: none.

### C2 — PASS (1)

- Response line 34: “**Observed, July 14:** Erin completed a financing model.”
- Response line 39 records management review on July 17 and counsel review on July 18 as scheduled and says every result remains `unknown` until its dated event.
- Response line 55 makes Priya the owner of the still-unknown July 18 “legal effect and actual terms” review; line 82 expressly requires review of both complete document sets.

Misses: none.

### C3 — PASS (1)

- Response lines 16, 38, and 95 name Erin as financing-process owner; lines 14 and 94 give July 21 as the decision date.
- Response lines 14, 35, and 36 preserve the July 24 equity expiry and July 25 debt expiry.
- Response lines 39, 59, and 87 record Nadia and Luis’s September 1 joint financing review.
- Response lines 40, 60, and 88 assign Erin the November 28 cash test and state that cash below $1.7 million causes Erin to reopen external financing on December 1.

Misses: none.

### C4 — PASS (1)

- Response lines 16, 20, 83, and 94 keep the financing business choice with Nadia alone.
- Response line 22 names Priya Desai in the qualified-current-counsel lane and assigns her legal effect, actual terms, and document/legal questions. Lines 55, 82, 84, 90, and 96 keep her work to document review, legal verification, and advice on legal effect and actual terms.
- No passage makes Priya, Erin, or Luis the financing decision maker. No passage makes Nadia the owner of counsel’s legal review.

Misses: none.

### C5 — FAIL (0)

Carried accurately:

- Response lines 37, 44, 72, and 97 carry $3.6 million cash, $180,000 monthly burn, 20 months’ runway, the live decline-both option, and unchanged current ownership/board if both are declined.
- Response lines 35 and 45 carry all required equity economics, runway outputs, five-seat/exactly-one-investor-seat structure, and consent rights.
- Response lines 36 and 46 carry the debt amount, 24-month tenor, 10% rate, $180,000 annual interest, $36,000 fee, 1% fully diluted warrant, $1 million minimum-cash covenant, no board seat, and 10 gross/30 total months before costs.
- Response line 47 carries the supplied static illustration: $5.4 million post-funding cash, $4.32 million 24-month burn, $360,000 two-year interest, $36,000 fee, and $684,000 remaining before principal.

Strict conjunctive miss:

- The response never states that the $36,000 debt fee is **2%**. Line 36 says only “a $36,000 fee,” and line 47 again supplies only the dollar amount. C5 requires both the percentage and dollar amount.

Derived-output audit:

- Per the scoring instruction, every numeric output explicitly supplied by the prompt—including the whole static illustration—is treated as a supplied fact, not a new calculation.
- The only new derived numeric economic output is line 47’s statement that $684,000 is `$316,000 below` the $1 million covenant. The qualitative reconciliation statements introduce no new numeric output. Thus the response remains within the maximum of two additional derived economic calculations and does not build or demand an exhaustive replacement model.

No other C5 misses were found.
