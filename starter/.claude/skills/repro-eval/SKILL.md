---
name: repro-eval
description: Reproduce and fix the COMP 523 evaluation bug, verify metric behavior, save a JSON report, and request an independent review.
---

Complete the evaluation task in `ISSUE.md`. Additional request: $ARGUMENTS

1. Read the issue, source, dataset, and tests. Run `bash scripts/check.sh` to establish the failing baseline.
2. Explain the discrepancy between accuracy and macro-F1 using the class counts. Make a small source change that satisfies the documented metric contract. Preserve test expectations and data; do not consult the reference solution.
3. Run `bash scripts/check.sh` explicitly. If it fails, inspect the failure and continue fixing. Then run `python3 -m src.evaluate --output reports/evaluation.json`.
4. Ask the `reviewer` subagent to read the implementation, tests, and JSON report. Supply the actual check result. It has read-only tools and should return findings, not edit files.
5. Resolve actionable findings and rerun checks if source changes. Present the diff summary, test results, accuracy, macro-F1, report path, and review outcome. Never claim a test or review happened without evidence.
