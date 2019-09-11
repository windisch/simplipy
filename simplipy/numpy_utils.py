import numpy as np


def get_random_state(seed):
    return np.random.RandomState(seed)


def shuffle_data(X, Y, seed=None):

    random = get_random_state(seed)

    indices = np.arange(X.shape[0])
    random.shuffle(indices)

    return X[indices], Y[indices]


def reverse_cumsum(x):
    return np.cumsum(x[::-1])[::-1]
