---
name: repro-eval
description: Reproduce and fix the COMP 523 evaluation bug, verify metric behavior, save a JSON report, and request an independent review.
---

Read `ISSUE.md`, source, dataset, and tests. Run `bash scripts/check.sh` to establish
the failing baseline. Explain the difference between accuracy and macro-F1 using
the class counts, then make a minimal implementation fix. Preserve data and test
expectations; do not consult `../reference_solution/` during the exercise.

Run `bash scripts/check.sh` explicitly and resolve failures. Generate the report
with `python3 -m src.evaluate --output reports/evaluation.json`. Request an independent
read-only review if the environment supports subagents; otherwise say that the
independent review was not run. Address findings and rerun checks after any source change.

Return the change summary, actual check result, both metrics, report path, and review
outcome. The `.claude/` hook and named reviewer are Claude-specific; this skill does
not install or promise equivalent automation in other agents.
