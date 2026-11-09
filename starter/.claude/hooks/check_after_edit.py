#!/usr/bin/env python3
"""Run local checks after a Claude Edit/Write; report evidence without undoing edits."""
import json
from pathlib import Path
import subprocess
import sys


def main():
    # Claude supplies event JSON on stdin. No event field is executed as code.
    sys.stdin.read()
    project = Path(__file__).resolve().parents[2]
    try:
        result = subprocess.run(
            ["bash", "scripts/check.sh"], cwd=project,
            text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            timeout=25, check=False,
        )
        output, status = result.stdout, result.returncode
    except subprocess.TimeoutExpired:
        output, status = "Checks timed out after 25 seconds. Run bash scripts/check.sh manually.\n", 1
    reports = project / "reports"
    reports.mkdir(exist_ok=True)
    (reports / "hook-check.log").write_text(output, encoding="utf-8")
    if status:
        print("Post-edit checks failed; inspect reports/hook-check.log.\n" + output, file=sys.stderr)
        return 2
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext": "Post-edit checks passed. Evidence: reports/hook-check.log. Run the final check explicitly before finishing."
    }}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
