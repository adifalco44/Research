import copy
import json
import os
from ibio import utils

class Experiment(object):
    def __init__(self):
        pass

    @staticmethod
    @utils.static_vars_(data=None)
    def get_all():
        if Experiment.get_all.data is None:
            with open(utils.get_experiment_data_path(), 'r') as f:
                data = json.load(f)
                Experiment.get_all.data = data
        return Experiment.get_all.data
