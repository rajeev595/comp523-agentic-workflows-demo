# COMP 523 evaluation demo

Read `ISSUE.md`. Work in this starter project, using Python's standard library.
Preserve the dataset, public evaluator interface, and test expectations.
Do not read or copy `../reference_solution/` during the live exercise.

Reproduce the failure with `bash scripts/check.sh`, diagnose the metric computation,
make a minimal fix, rerun checks, and generate `reports/evaluation.json`.
Request an independent read-only review if your agent environment supports it.
Report the observed tests and values, changed files, and remaining limitations.

The workflow is in `.agents/skills/repro-eval/SKILL.md`. The hook and named reviewer
under `.claude/` are Claude Code configuration; other agents must run checks explicitly.
