import os
import warnings

from flask import Flask, Markup, render_template, request
from flask_analytics import Analytics

from web.faces.controllers import faces
from web.cache import cache

# Build app
app = Flask(__name__)
# Analytics(app)
cache.init_app(app)

# Defaults
app.config['DEBUG'] = True
# app.config['OWNER_AUTHOR_KEY'] = 'bjrichardwebster'
# app.config['ANALYTICS']['GOOGLE_UNIVERSAL_ANALYTICS']['ACCOUNT'] = 'UA-80482679-1'

@app.errorhandler(404)
@cache.cached(300)
def page_not_found(error):
    app.logger.error('Page not found: %s', (request.path, error))
    return render_template('404.html'), 404

@app.errorhandler(500)
@cache.cached(300)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return render_template('500.html'), 500

app.register_blueprint(faces, url_prefix='/faces')
