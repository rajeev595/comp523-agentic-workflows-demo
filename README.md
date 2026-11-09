# Agentic Workflows with Coding Agents

Runnable COMP 523 presentation demo: repair an evaluation bug using repository instructions, a reusable skill, an edit hook, and an independent reviewer.

This kit was recreated from the prior demo specification because the original ChatGPT ZIP was unavailable in this workspace. It is not a byte-for-byte copy of that ZIP.

## Start the live demo

Requires Git, Python 3.9+, and Bash. No Python packages or API keys are needed for the tests. The live agent portion requires an installed, signed-in Claude Code.

```bash
git clone https://github.com/rajeev595/comp523-agentic-workflows-demo.git
cd comp523-agentic-workflows-demo/starter
bash scripts/check.sh
```

The first check is **supposed to fail** (4 failures out of 12 tests): the starter incorrectly returns accuracy as macro-F1. Continue with:

```bash
claude
```

At the Claude Code prompt:

```text
/repro-eval Fix the evaluation issue in ISSUE.md.
```

Start Claude from `starter/` so its project instructions and configuration are discovered. Review the folder trust prompt if one appears. Use `/hooks` and `/agents` to inspect the configured hook and reviewer. If the skill is absent, restart Claude in this directory.

After the agent finishes, exit to the same terminal and verify:

```bash
bash scripts/check.sh
python3 -m src.evaluate --output reports/evaluation.json
cat reports/evaluation.json
git diff -- src
```

Expected metrics: **accuracy = 0.8**, **macro-F1 = 0.4444444444444444**. The ten examples contain eight negative and two positive labels; predictions are all negative. Negative-class F1 is 8/9, positive-class F1 is 0, and their unweighted mean is 4/9.

## Six-minute presentation

| Time | Show | Point to explain |
|---|---|---|
| 0:00–0:45 | `ISSUE.md`, failing check | Establish evidence before editing. |
| 0:45–1:30 | `CLAUDE.md`, skill, hook, reviewer | Instructions, reusable workflow, deterministic check, independent review. |
| 1:30–4:30 | Invoke `/repro-eval` | Watch the agent inspect, fix, check, and request review. |
| 4:30–5:30 | Passing check and JSON report | Verify the outcome yourself. |
| 5:30–6:00 | Diff and reviewer findings | Small change, reproducible evidence, explicit limitations. |

Agent response time varies. Use the backup below if time runs short.

## Backup without a live agent

From `starter/`, run the prepared solution in its own directory:

```bash
cd ../reference_solution
bash scripts/check.sh
python3 -m src.evaluate --output reports/evaluation.json
cat reports/evaluation.json
diff -u ../starter/src/metrics.py src/metrics.py || true
```

This leaves the starter untouched so you can rehearse again. Explain that this is the prepared reference solution, not a live agent result.

## Included materials

- `starter/`: deliberately broken implementation, dataset, issue, and tests.
- `starter/CLAUDE.md` and `starter/AGENTS.md`: project instructions.
- `starter/.claude/skills/repro-eval/SKILL.md`: Claude's reusable workflow.
- `starter/.agents/skills/repro-eval/SKILL.md`: portable workflow for other compatible agents.
- `starter/.claude/settings.json` and `.claude/hooks/check_after_edit.py`: checks after Claude `Edit` or `Write` calls.
- `starter/.claude/agents/reviewer.md`: reviewer restricted to `Read`, `Grep`, and `Glob`.
- `reference_solution/`: working implementation for the fallback demonstration.

The hook writes `reports/hook-check.log`. A failing post-edit hook reports the problem to Claude; it does not undo edits or prevent completion. Bash-based edits do not match this hook. Always run the final check manually. The reviewer reads evidence and cannot run commands itself.

## Verification scope

Preparation checks: the reference solution passed all 12 tests and produced the expected JSON metrics. The configured hook command was exercised on broken and fixed copies, including a directory with spaces: failures returned exit 2 and a log; success returned valid `PostToolUse` JSON and a log. A full authenticated Claude Code session—including skill discovery, automatic hook invocation, and reviewer delegation—has not been rehearsed as part of preparing this kit. Do not present it as already verified end to end.

Configuration follows the official [skills](https://code.claude.com/docs/en/skills), [hooks](https://code.claude.com/docs/en/hooks), and [subagent](https://code.claude.com/docs/en/sub-agents) documentation. The hook and named reviewer are Claude-specific; other agents must run checks explicitly and use their own review capability.
