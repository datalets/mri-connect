from flask import Flask, Markup
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import flask_admin as admin
import click

# Create application
app = FlaskAPI(__name__)
from .config import Config
app.logger.info('>>> {}'.format(Config.FLASK_ENV))

if Config.SQLALCHEMY_DATABASE_URI.startswith("sqlite"):
    app.logger.info('Warning: temporary database, changes will not persist.')
    app.logger.info('>>> {}'.format(Config.SQLALCHEMY_DATABASE_URI))

db = SQLAlchemy(app)

from .models import *
migrate = Migrate(app, db)

# Create admin
adminlink = Config.ADMIN_PATH
app.logger.info('Admin access at /%s' % adminlink)
admin = admin.Admin(app, url='/'+adminlink, name='GMBA Connect', template_mode='bootstrap3')

from .views import *
