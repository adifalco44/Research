# This was some seriously bad coding practices that
# I hacked together in a hurry.

from flask import abort, Blueprint, current_app, send_file, render_template
from flask import make_response, request

from ibio.cache import cache
from ibio.data.models import Experiment
from ibio import utils

import random, uuid, os

ecaldesi = Blueprint('ecaldesi', __name__, template_folder='templates')

@ecaldesi.route('/')
def index():
    trials = []

    trial = {}
    trial['id'] = 0
    trial['image'] = 'https://engineering.nd.edu/profiles/brichardwebster/@@images/81a1b34f-ee63-457b-864a-cb8eee7df648.jpeg'
    trial['options'] = ['Brandon RichardWebster', 'Kevin Bowyer', 'Walter Scheirer']
    trial['answer'] = [True, False, False]
    trials.append(trial)

    trial = {}
    trial['id'] = 1
    trial['image'] = 'https://engineering.nd.edu/profiles/kbowyer/@@images/fcc600ee-47e1-4c03-8ef4-ec2f657d0160.jpeg'
    trial['options'] = ['Brandon RichardWebster', 'Kevin Bowyer', 'Walter Scheirer']
    trial['answer'] = [False, True, False]
    trials.append(trial)

    return make_response(render_template('example.html', trials=trials))
