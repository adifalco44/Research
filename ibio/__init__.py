import os
import warnings

from flask import Flask, Markup, render_template, request
from flask_analytics import Analytics

from ibio.pamiexp.controllers import pamiexp
from ibio.ecaldesi.controllers import ecaldesi
from ibio.cache import cache
import utils


# Build app
app = Flask(__name__,
            instance_path=utils.get_instance_folder_path(),
            instance_relative_config=True)
Analytics(app)
cache.init_app(app)

# Defaults
app.config['DEBUG'] = True
app.config['OWNER_AUTHOR_KEY'] = 'bjrichardwebster'
app.config['ANALYTICS']['GOOGLE_UNIVERSAL_ANALYTICS']['ACCOUNT'] = 'UA-80482679-1'

# Instance values
app.config.from_pyfile('config.cfg', silent=True)


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

app.register_blueprint(pamiexp, url_prefix='/pamiexp')
app.register_blueprint(ecaldesi, url_prefix='/ecaldesi')
