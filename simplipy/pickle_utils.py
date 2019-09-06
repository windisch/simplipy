import pickle
import os
import tempfile


def try_to_pickle(obj, filepath):

    tmpfile = tempfile.NamedTemporaryFile()
    try:
        pickle.dump(obj, open(tmpfile.name, 'wb'))
        os.rename(tmpfile.name, filepath)
    except Exception:
        raise


def try_to_unpickle(filepath):
    return pickle.load(open(filepath, 'rb'))
