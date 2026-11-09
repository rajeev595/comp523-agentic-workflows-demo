import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from src.evaluate import DEFAULT_DATA, evaluate
from src.metrics import accuracy, macro_f1


class EvaluationTests(unittest.TestCase):
    def setUp(self):
        self.actual = [0] * 8 + [1] * 2
        self.predicted = [0] * 10

    def test_accuracy_baseline(self):
        self.assertAlmostEqual(accuracy(self.actual, self.predicted), 0.8)

    def test_accuracy_perfect(self):
        self.assertEqual(accuracy([0, 1], [0, 1]), 1.0)

    def test_macro_f1_imbalanced(self):
        self.assertAlmostEqual(macro_f1(self.actual, self.predicted), 4 / 9)

    def test_macro_f1_perfect_both_classes(self):
        self.assertEqual(macro_f1([0, 1], [0, 1]), 1.0)

    def test_macro_f1_all_incorrect(self):
        self.assertEqual(macro_f1([0, 1], [1, 0]), 0.0)

    def test_macro_f1_absent_class_contributes_zero(self):
        self.assertEqual(macro_f1([0, 0], [0, 0]), 0.5)

    def test_macro_f1_all_positive_predictions(self):
        self.assertAlmostEqual(macro_f1([0, 0, 0, 1], [1, 1, 1, 1]), 0.2)

    def test_mismatched_lengths_rejected(self):
        for metric in (accuracy, macro_f1):
            with self.subTest(metric=metric.__name__), self.assertRaises(ValueError):
                metric([0, 1], [0])

    def test_empty_inputs_rejected(self):
        for metric in (accuracy, macro_f1):
            with self.subTest(metric=metric.__name__), self.assertRaises(ValueError):
                metric([], [])

    def test_nonbinary_labels_rejected(self):
        for metric in (accuracy, macro_f1):
            for actual, predicted in (([2], [0]), ([0], [-1]), (["0"], [0])):
                with self.subTest(metric=metric.__name__, actual=actual, predicted=predicted):
                    with self.assertRaises(ValueError):
                        metric(actual, predicted)

    def test_report_schema_and_values(self):
        report = evaluate(json.loads(DEFAULT_DATA.read_text(encoding="utf-8")))
        self.assertEqual(set(report), {"schema_version", "n_examples", "labels", "accuracy", "macro_f1"})
        self.assertEqual(report["schema_version"], 1)
        self.assertEqual(report["n_examples"], 10)
        self.assertEqual(report["labels"], [0, 1])
        self.assertAlmostEqual(report["accuracy"], 0.8)
        self.assertAlmostEqual(report["macro_f1"], 4 / 9)

    def test_cli_writes_deterministic_json(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "nested" / "report.json"
            command = [sys.executable, "-m", "src.evaluate", "--output", str(output)]
            first = subprocess.run(command, check=True, capture_output=True, text=True)
            first_bytes = output.read_bytes()
            second = subprocess.run(command, check=True, capture_output=True, text=True)
            self.assertEqual(first_bytes, output.read_bytes())
            self.assertEqual(first.stdout, second.stdout)
            self.assertEqual(json.loads(first.stdout), json.loads(first_bytes))


if __name__ == "__main__":
    unittest.main()
