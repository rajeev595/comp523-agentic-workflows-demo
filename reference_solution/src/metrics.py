"""Binary classification metrics. Labels are always 0 and 1."""


def _validate(y_true, y_pred):
    if not y_true:
        raise ValueError("At least one example is required")
    if len(y_true) != len(y_pred):
        raise ValueError("Labels and predictions must have equal lengths")
    if any(type(value) is not int or value not in (0, 1)
           for value in list(y_true) + list(y_pred)):
        raise ValueError("Labels and predictions must be integer 0 or 1")


def accuracy(y_true, y_pred):
    _validate(y_true, y_pred)
    return sum(actual == predicted for actual, predicted in zip(y_true, y_pred)) / len(y_true)


def macro_f1(y_true, y_pred):
    """Return the unweighted mean of F1 for labels 0 and 1.

    A class with a zero denominator contributes 0.0.
    """
    _validate(y_true, y_pred)
    scores = []
    for label in (0, 1):
        tp = sum(actual == label and predicted == label
                 for actual, predicted in zip(y_true, y_pred))
        fp = sum(actual != label and predicted == label
                 for actual, predicted in zip(y_true, y_pred))
        fn = sum(actual == label and predicted != label
                 for actual, predicted in zip(y_true, y_pred))
        denominator = 2 * tp + fp + fn
        scores.append(2 * tp / denominator if denominator else 0.0)
    return sum(scores) / len(scores)
