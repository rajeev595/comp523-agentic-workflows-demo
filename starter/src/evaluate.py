"""Evaluate a JSON fixture and write a deterministic JSON report."""

import argparse
import json
from pathlib import Path

from .metrics import accuracy, macro_f1

DEFAULT_DATA = Path(__file__).resolve().parents[1] / "data" / "predictions.json"


def evaluate(dataset):
    y_true = dataset["y_true"]
    y_pred = dataset["y_pred"]
    return {
        "schema_version": 1,
        "n_examples": len(y_true),
        "labels": [0, 1],
        "accuracy": accuracy(y_true, y_pred),
        "macro_f1": macro_f1(y_true, y_pred),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA)
    parser.add_argument("--output", type=Path, default=Path("reports/evaluation.json"))
    args = parser.parse_args()
    with args.data.open(encoding="utf-8") as handle:
        report = evaluate(json.load(handle))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n"
    args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
