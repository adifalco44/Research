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
    return redirect(url_for('faces.trial', sid=sid))

@faces.route('/trial/<sid>')
def trial(sid):
    trial = connector.get_trial(sid)
    if trial is None:
        return 'REDIRECT THIS TO MTURK2'
    response = make_response(render_template('trial.html',trial=trial))
    response.set_cookie('timer',str(time.time()))
    response.set_cookie('sid',sid)
    return response

@faces.route('/response/<sid>/<tid>/<rid>')
def response(sid, tid, rid): # session id, trial id, response id
    check = connector.set_response(sid, tid, rid)
#if check is None:
 #       return 'REDIRECT THIS TO MTURK3'

    user = request.cookies.get('sid')
    if (user==sid):
        last = float(request.cookies.get('timer'))
        timer = time.time() - last
        print(str(timer))
        return redirect(url_for('faces.trial', sid=sid))
    return render_template("404.html")
