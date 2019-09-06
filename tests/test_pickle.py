import unittest
import tempfile
import pickle
from simplipy.pickle_utils import (
    try_to_unpickle,
    try_to_pickle
)


class TestPickle(unittest.TestCase):

    def test_dict_saving(self):

        with tempfile.NamedTemporaryFile() as tmpfile:
            dict_orig = {'a': 1, 'b': 2.0}
            try_to_pickle(dict_orig, tmpfile.name)
            dict_loaded = pickle.load(open(tmpfile.name, 'rb'))
        self.assertDictEqual(dict_loaded, dict_orig)

    def test_dict_loading(self):
        with tempfile.NamedTemporaryFile() as tmpfile:
            dict_orig = {'a': 1, 'b': 2.0}
            pickle.dump(dict_orig, open(tmpfile.name, 'wb'))
            dict_loaded = try_to_unpickle(tmpfile.name)
        self.assertDictEqual(dict_loaded, dict_orig)
