"""
Some helpers to work with dicts.
"""


def merge(dict_a, dict_b):
    """
    Merges two dicts into one.

    Args:
        dict_a (dict): A dict
        dict_b (dict): A dict
    """

    # Check input
    assert type(dict_a) == dict and type(dict_b) == dict, "Input must be dicts"

    # Assert uniquze keys
    assert len(set(dict_a.keys()).intersection(dict_b.keys())) == 0, "Duplicate keys"

    return {**dict_a, **dict_b}
