"""
Multinomial Models should be comparable.
"""

from model_base import *


class H2OMultinomialModel(ModelBase):

    def __init__(self, dest_key, model_json):
        super(H2OMultinomialModel, self).__init__(dest_key, model_json,H2OMultinomialModelMetrics)

class H2OMultinomialModelMetrics(object):
  def __init__(self, metric_json):
    self._metric_json = metric_json