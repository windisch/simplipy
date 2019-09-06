import unittest
from simplipy.dicts import merge


class TestDicts(unittest.TestCase):

    def test_merge_dicts(self):
        A = {'a': 0, 'b': 1}
        B = {'c': 2, 'd': 3, 'e': 4}

        self.assertDictEqual(
            merge(A, B),
            {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
        )

    def test_exception_on_duplicates(self):
        with self.assertRaises(AssertionError):
            merge(
                {'a': 10, 'b': 3},
                {'b': 70, 'c': 4}
            )

    def test_wrong_type(self):

        with self.assertRaises(AssertionError):
            merge(1, {'a': 1})

        with self.assertRaises(AssertionError):
            merge({'a': 1}, 1)
