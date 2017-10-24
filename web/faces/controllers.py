from flask import abort, Blueprint, current_app, send_file, render_template, url_for
from flask import make_response, redirect, request

from web.cache import cache

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
    return render_template('trial.html')

@faces.route('/response')
def response():
    # record response
    # redirect to trial
    return redirect(url_for('faces.trial'))
