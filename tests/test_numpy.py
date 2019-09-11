import unittest
import numpy as np
from simplipy.numpy_utils import reverse_cumsum


class TestNumpyUtils(unittest.TestCase):

    def test_reverse_cumsum(self):

        a = np.array([1, 2, 3, 4, 5])
        np.testing.assert_array_equal(
            reverse_cumsum(a),
            [15, 14, 12, 9, 5])
