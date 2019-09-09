import unittest
from simplipy.xgboost.metric_utils import combine_metrics


class TestXgboost(unittest.TestCase):

    def test_custom_loss(self):
        assert True


class TestMetricUtils(unittest.TestCase):


    def test_combine_metrics(self):

        def metric_a(preds, dtrain):
            return 'a', 2

        def metric_b(preds, dtrain):
            return [('b1', 1), ('b2', 2)]


        metric = combine_metrics(metric_a, metric_b)

        self.assertListEqual(
            metric(None, None),
            [('a', 2), ('b1', 1), ('b2', 2)]
        )
