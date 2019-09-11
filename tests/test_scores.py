import unittest
import numpy as np
from simplipy.scores.base import compute_rates_and_thresholds

class TestScores(unittest.TestCase):

    def setUp(self):
        self.y_label = np.array(
            [1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0])
        self.y_proba = np.array(
            [0.9, 0.8, 0.6, 0.7, 0.8, 0.3, 0.1, 0.0, 1.0, 0.5, 0.8, 0.2])

        self.tps = [7, 7, 7, 7, 6, 5, 5, 5, 2 ,1]
        self.fps = [5, 4, 3, 2, 2, 2, 1, 0, 0, 0]
        self.thresholds = [0.0, 0.1, 0.2, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

    def test_rates_not_normalized(self):

        tpr, fpr, thresholds = compute_rates_and_thresholds(
            y_label=self.y_label,
            y_proba=self.y_proba,
            normalize=False)

        np.testing.assert_array_equal(tpr, self.tps)
        np.testing.assert_array_equal(fpr, self.fps)
        np.testing.assert_array_equal(thresholds, self.thresholds)

    def test_exchanged_positive_label(self):
        tpr, fpr, thresholds = compute_rates_and_thresholds(
            y_label=self.y_label,
            y_proba=self.y_proba,
            positive_label=0.0,
            normalize=False)

        np.testing.assert_array_equal(fpr, self.tps)
        np.testing.assert_array_equal(tpr, self.fps)

    def test_rates_normalized(self):
        tpr, fpr, thresholds = compute_rates_and_thresholds(
            y_label=self.y_label,
            y_proba=self.y_proba,
            normalize=True)

        n_pos = (self.y_label == 1.0).sum()
        n_neg = (self.y_label == 0.0).sum()

        np.testing.assert_array_equal(tpr, self.tps/n_pos)
        np.testing.assert_array_equal(fpr, self.fps/n_neg)
        np.testing.assert_array_equal(thresholds, self.thresholds)

    def test_without_zero(self):
        self.y_proba[np.where(self.y_proba == 0.0)] = 0.01
        _, _, thresholds = compute_rates_and_thresholds(
            y_label=self.y_label,
            y_proba=self.y_proba,
            normalize=True)
        self.assertEqual(thresholds[0], 0.0)

    def test_without_ones(self):
        self.y_proba[np.where(self.y_proba == 1.0)] = 0.999
        tpr, fpr, thresholds = compute_rates_and_thresholds(
            y_label=self.y_label,
            y_proba=self.y_proba,
            normalize=True)
        self.assertEqual(thresholds[-1], 1.0)
