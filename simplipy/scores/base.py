import numpy as np
from simplipy.numpy_utils import reverse_cumsum


def _remove_redundant_thresholds(tp, fp, thresholds):
    """
    Removes thresholds where neither the nunber of true positive nor the number of false
    positive change and hence can be omitted

    Args:
        tp (numpy.ndarray): List of integers representing the number of true positives
        fp (numpy.ndarray): List of integers representing the number of false positives
        thresholds (numpy.ndarray): List of thresholds

    Returns:
        tuple: Tuple consisting of cleaned true positives, false positives, and thresholds

    """
    corners_threshold = np.diff(thresholds, prepend=-1) != 0.0
    thresholds = thresholds[corners_threshold]
    tp = tp[corners_threshold]
    fp = fp[corners_threshold]

    corner_positions = np.logical_or(
        np.diff(tp, prepend=tp[0]+1) != 0.0,
        np.diff(fp, prepend=fp[0]+1) != 0.0)

    tp = tp[corner_positions]
    fp = fp[corner_positions]
    thresholds = thresholds[corner_positions]

    return tp, fp, thresholds


def compute_rates_and_thresholds(y_label, y_proba, positive_label=1.0, normalize=True):
    """
    Computes the true positive and false positive rate for the given labels and probbilities as the
    discrimination thresholds varies. This method is slow, but correct!

    Args:
        y_label (numpy.ndarray): The true labels
        y_proba (numpy.ndarray): The predicted probabilitites
        positive_label (obj): The positive label
        normalize (bool): Whether rates or absolute numbers should be returned

    Returns:
        tuple: Tuple consisting of true positive rate, false positive rate, and thresholds
        Here, :code:`tpr[i]` is the true positive rate of a classifier that let points with
        probability larger or equal than :code:`thresholds[i]` as positive

    """

    p = np.argsort(y_proba)
    y_proba = y_proba[p]
    y_label = y_label[p]
    thresholds = y_proba

    y_label_pos = y_label == positive_label
    y_label_neg = y_label != positive_label

    n_pos = y_label_pos.sum()
    n_neg = y_label_neg.sum()

    # Compute fully fletched tpr and fpr rates
    tp = reverse_cumsum(y_label_pos)
    fp = reverse_cumsum(y_label_neg)

    # Append rates for 1 and 0
    if thresholds[0] != 0.0:
        thresholds = np.append(0.0, thresholds)
        tp = np.append(n_pos, tp)
        fp = np.append(n_neg, fp)

    if thresholds[-1] != 1.0:
        thresholds = np.append(thresholds, 1.0)
        # If 1.0 is not a threshold, then its not a probability which meas no point gets this
        # probability assigned . Hence, both rates must be zero
        tp = np.append(tp, 0.0)
        fp = np.append(fp, 0.0)

    tp, fp, thresholds = _remove_redundant_thresholds(tp, fp, thresholds)

    if normalize:
        return tp/n_pos, fp/n_neg, thresholds
    else:
        return tp, fp, thresholds
