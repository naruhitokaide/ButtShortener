import os

from flask import Flask
from flask.ext.assets import Bundle, Environment
from flask.ext.login import LoginManager, current_user
from flask.ext.migrate import Migrate
from flask.ext.sqlalchemy import SQLAlchemy

from raven.contrib.flask import Sentry

app = Flask(__name__)
app.config.from_object('config')

# Load Flask Extensions
assets = Environment(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)
sentry = Sentry(app)

# Load blueprints
from ButtShortener.api import api
app.register_blueprint(api, url_prefix='/api')