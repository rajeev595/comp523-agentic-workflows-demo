# COMP 523 evaluation demo

Work from this `starter/` directory. Read `ISSUE.md` before editing.

- Python standard library only; keep the public evaluator interface stable.
- Preserve the dataset and test expectations. Fix the implementation rather than weakening checks.
- Do not read or copy `../reference_solution/` during the live agent exercise.
- Run `bash scripts/check.sh` before the final answer and generate `reports/evaluation.json`.
- Use the `reviewer` subagent after the fix. Give it the check result and ask it to inspect the source, tests, and report independently.
- Show the changed files, test result, and both accuracy and macro-F1. Distinguish observed results from untested claims.

The `repro-eval` skill provides the workflow. The edit hook runs checks after `Edit` and `Write` calls; it reports failures but cannot undo an edit. Edits made through Bash do not trigger that matcher, so always run the final check explicitly.
