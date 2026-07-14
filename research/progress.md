# Research progress

## Checkpoint 1: research scaffold and cumulative validator

Date: 2026-07-13

### TDD evidence

Both production modules were absent when their tests were first run.

```text
$ python3 -m unittest tests.test_build_research_scaffold -v
ImportError: Failed to import test module: test_build_research_scaffold
ModuleNotFoundError: No module named 'scripts'
FAILED (errors=1)

$ python3 -m unittest tests.test_validate_repository -v
ImportError: Failed to import test module: test_validate_repository
ModuleNotFoundError: No module named 'scripts'
FAILED (errors=1)
```

After implementation, the focused suites passed. A later README exactness regression was also developed RED/GREEN. Final discovery passed 16 tests total: 3 scaffold tests and 13 cumulative-validator tests.

```text
$ python3 -m unittest discover -s tests -v
Ran 16 tests
OK
```

### Generated corpus scaffold

Command:

```bash
python3 scripts/build_research_scaffold.py \
  --corpus /Users/leopaz/dev/opensource/graham-essays/corpus \
  --output-root . \
  --batch-count 12
```

Result:

```text
generated research scaffold from 223 corpus files
```

The manifest contains 223 numerically sorted metadata records. The batch plan contains 12 explicit contiguous assignments: seven batches of 19 essays and five batches of 18 essays.

### QMD access and retrieval proof

Status command:

```bash
PATH=/Users/leopaz/.nvm/versions/node/v22.23.0/bin:$PATH \
  qmd --index graham-essays status
```

Status reported `223 files indexed`, `1582 embedded` vectors, and the `graham-essays` collection with 223 files.

BM25 example:

```bash
PATH=/Users/leopaz/.nvm/versions/node/v22.23.0/bin:$PATH \
  qmd --index graham-essays search \
  "talk to users launch startup" -c graham-essays -n 3 --format json
```

The top three results were articles 153, 069, and 222, with scores 0.79, 0.79, and 0.78.

Vector example:

```bash
PATH=/Users/leopaz/.nvm/versions/node/v22.23.0/bin:$PATH \
  qmd --index graham-essays vsearch \
  "founders learning directly from early users before scaling" \
  -c graham-essays -n 3 --format json
```

The top three results were articles 153, 169, and 039, with scores 0.64, 0.60, and 0.55.

Full-document retrieval proof:

```bash
PATH=/Users/leopaz/.nvm/versions/node/v22.23.0/bin:$PATH \
  qmd --index graham-essays get \
  qmd://graham-essays/153-do-things-that-don-t-scale.md | wc -l
```

The complete retrieval streamed successfully and contained 169 output lines. This was a retrieval-path check only; no essay was classified and no taxonomy was selected.

### Manifest gate

```bash
python3 scripts/validate_repository.py \
  --phase manifest \
  --repo . \
  --corpus /Users/leopaz/dev/opensource/graham-essays/corpus
```

```text
manifest validation passed: corpus_files=223 manifest_essays=223 unique_assignments=223 batches=12 gaps=0 overlaps=0
```

### Remaining work and blockers

- Remaining: independent review of all 12 non-overlapping essay batches, canonical audit assembly, taxonomy synthesis, per-skill baseline/forward evaluation, independent final review, and README catalog.
- Blockers: none.
