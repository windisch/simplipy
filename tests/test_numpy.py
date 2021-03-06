import unittest
import numpy as np
from simplipy.numpy_utils import reverse_cumsum
from simplipy.numpy_utils import get_change_points
from simplipy.numpy_utils import argmax


class TestNumpyUtils(unittest.TestCase):

    def test_reverse_cumsum(self):

        a = np.array([1, 2, 3, 4, 5])
        np.testing.assert_array_equal(
            reverse_cumsum(a),
            [15, 14, 12, 9, 5])

    def test_argmax_multidim(self):
        a = np.array([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 5],
        ])

        self.assertTupleEqual(
            argmax(a),
            (1, 3)
        )

    def test_get_change_points(self):

        a = np.array([1, 0, 0, 1, 1, 0, 1, 1, 0])

        np.testing.assert_array_equal(
            get_change_points(a),
            [1, 3, 5, 6, 8]
        )
