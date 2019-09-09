"""
"""

from simplipy.list_utils import flatten


def _make_iterable(obj):

    if type(obj) == tuple:
        return [obj]
    else:
        return obj


def combine_metrics(*callables):
    """
    Combines a list of metrics to a single metric
    """

    def metric_fn(preds, dtrain):

        metrics = [_make_iterable(m(preds, dtrain)) for m in callables]
        return flatten(metrics)
    return metric_fn
