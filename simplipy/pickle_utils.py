import pickle
import os
import tempfile


def try_to_pickle(obj, filepath):
    """
    Pickels the object under the given filepath in secure manner.

    Args:
        obj (object): A python object
        filepath (string): Path to the outfile
    """

    tmpfile = tempfile.NamedTemporaryFile()
    try:
        pickle.dump(obj, open(tmpfile.name, 'wb'))
        os.rename(tmpfile.name, filepath)
    except Exception:
        raise


def try_to_unpickle(filepath):
    """
    Loads the python object from the pickle file.
    """
    return pickle.load(open(filepath, 'rb'))
