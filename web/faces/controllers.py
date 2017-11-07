from flask import abort, Blueprint, current_app, send_file, render_template, url_for
from flask import make_response, redirect, request

from web.cache import cache
import web.connector as connector

import uuid

faces = Blueprint('faces', __name__, template_folder='templates')

@faces.route('/')
def index():
    # create a session ID here. use uuid.uuid4
    # store in cookie
    # redirect to route('/trial')
    return redirect(url_for('faces.trial'))

@faces.route('/trial')
def trial():
    # load session ID from cookie (do not modify it)
    # get remaining trials for session ID
    # if no remaining trials, redirect to mturk
    # else, randomly pick one, and return trial

    fakedb = []
    obj1 = {
        # experiment data
        'ProbeTime'             : 50,
        'idExperiments'         : 1,
        'idDataType_Probe'      : 1,
        'idDataType_Gallery'    : 1,

        # participant data
        'idParticipants'        : 1,
        'UUID'                  : str(uuid.uuid4()),

        # trial data
        'idTrials'              : 1,
        'ProbeID'               : 1,
        'ProbePath'             : 'http://www.saintsrescue.ca/new_site//wp-content/gallery/barn_animals_sponsorship/Brad-Pitt.jpg',
        'Gallery1ID'            : 1,
        'Gallery1Path'          : 'http://www.saintsrescue.ca/new_site//wp-content/gallery/barn_animals_sponsorship/Brad-Pitt.jpg',
        'Gallery2ID'            : 2,
        'Gallery2Path'          : 'https://images-na.ssl-images-amazon.com/images/I/91w1cLKbY-L._SX355_.jpg',
        'Gallery3ID'            : 3,
        'Gallery3Path'          : 'http://whitefencefarm-il.com/img/BarnAnimals_2.jpg'
    }

    obj2 = {
        # experiment data
        'ProbeTime'             : 50,
        'idExperiments'         : 1,
        'idDataType_Probe'      : 1,
        'idDataType_Gallery'    : 1,

        # participant data
        'idParticipants'        : 1,
        'UUID'                  : obj1['UUID'],

        # trial data
        'idTrials'              : 2,
        'ProbeID'               : 6,
        'ProbePath'             : 'http://s1.1zoom.me/big3/478/338769-sepik.jpg',
        'Gallery1ID'            : 4,
        'Gallery1Path'          : 'https://dncache-mauganscorp.netdna-ssl.com/thumbseg/1554/1554897-bigthumbnail.jpg',
        'Gallery2ID'            : 5,
        'Gallery2Path'          : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxukmqgr5IzjTfdPiyFwUamNI0QVrmq1lfgZCYO0BzF7iTU7iShA',
        'Gallery3ID'            : 6,
        'Gallery3Path'          : 'http://s1.1zoom.me/big3/478/338769-sepik.jpg'
    }
    fakedb.append(obj1)
    fakedb.append(obj2)



    return render_template('trial.html')

@faces.route('/response')
def response():
    # record response
    # redirect to trial
    return redirect(url_for('faces.trial'))
