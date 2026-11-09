# Fix the evaluation metric

The classifier predicts negative for every example. Its accuracy is 0.8,
but our report incorrectly says macro-F1 is also 0.8.

Implement `macro_f1` in `src/metrics.py`. Evaluate both labels, 0 and 1,
and average their F1 scores equally. Use `2*TP / (2*TP + FP + FN)`;
if a class denominator is zero, its F1 is 0.0. Preserve validation.

Acceptance criteria:

- All 12 existing tests pass without weakening or deleting them.
- For the provided fixture: accuracy = 0.8 and macro-F1 = 4/9 (about 0.4444).
- `bash scripts/check.sh` passes and writes `reports/evaluation.json`.
- Explain the bug, show the diff, and ask the read-only reviewer to inspect it.
- Keep the change small; do not add dependencies or read the reference solution.
