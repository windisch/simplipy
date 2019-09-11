import numpy as np


def get_random_state(seed):
    return np.random.RandomState(seed)


def shuffle_data(X, Y, seed=None):

    random = get_random_state(seed)

    indices = np.arange(X.shape[0])
    random.shuffle(indices)

    return X[indices], Y[indices]


def reverse_cumsum(x):
    """
    Returns an array where the i-th position is the sum of all values in the original array having
    index larger or equal than :code:`i`
    """
    return np.cumsum(x[::-1])[::-1]
