from flask import abort, Blueprint, current_app, send_file, render_template, url_for
from flask import make_response, redirect, request

from web.cache import cache
import web.connector as connector

import uuid

faces = Blueprint('faces', __name__, template_folder='templates')

@faces.route('/')
def index():
    sid = connector.new_user(15) # TODO 15 needs to be the MTURK_ID
    if sid is None:
        return 'REDIRECT THIS TO MTURK'
    return redirect(url_for('faces.trial', sid=sid))

@faces.route('/trial/<sid>')
def trial(sid):
    trial = connector.get_trial(1)
    if trial is None:
        return 'REDIRECT THIS TO MTURK'
    return render_template('trial.html', trial=trial)

@faces.route('/response/<sid>/<tid>/<rid>')
def response(sid, tid, rid): # session id, trial id, response id
    check = connector.set_response(sid, tid, rid)
    if check is None:
        return 'REDIRECT THIS TO MTURK'
    return redirect(url_for('faces.trial', sid=sid))
