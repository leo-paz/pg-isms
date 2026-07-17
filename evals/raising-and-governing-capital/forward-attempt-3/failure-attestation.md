# Forward attempt 3 failure

Attempt 3 is invalid under its frozen generation contract and was not scored. The first written completions for scenarios 2 and 3 contain 1,496 and 1,246 words, exceeding the 1,200-word ceiling. Scenario 1 is within the ceiling at 1,157 words, but a valid evaluation requires all five cases.

All three dispatched response bodies remain byte-for-byte frozen. Their hashes, byte counts, and equal birth/modify timestamps are recorded in `failure-attestation.json`. Scenarios 4 and 5 were not dispatched, no criteria were exposed to generators, and scoring did not start.

This failure is not a license to replace or resample a response. The next attempt requires a material package-level compaction change, new package hashes, and five new fresh-context generators.
