import time
from flask import abort, Blueprint, current_app, send_file, render_template, url_for
from flask import make_response, redirect, request

from web.cache import cache
import web.connector as connector

import uuid

faces = Blueprint('faces', __name__, template_folder='templates')

@faces.route('/')
def index():
    sid = connector.new_user(15) # TODO 15 needs to be the MTURK_ID
#    if sid is None:
#        return 'REDIRECT THIS TO MTURK1'
    response = make_response(redirect(url_for('faces.trial',sid=sid)))
    response.set_cookie('timer','1')
    return response

@faces.route('/trial/<sid>')
def trial(sid):
    trial = connector.get_trial(sid)
    if trial is None:
        return 'REDIRECT THIS TO MTURK2'
    return render_template('trial.html',trial=trial)

@faces.route('/response/<sid>/<tid>/<rid>')
def response(sid, tid, rid): # session id, trial id, response id
    check = connector.set_response(sid, tid, rid)
    timer = request.cookies.get('timer')
    print(str(timer))
    return redirect(url_for('faces.trial', sid=sid))
