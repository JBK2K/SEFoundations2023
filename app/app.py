from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from app.config import *
from app.extensions.database import db, migrate

from . import dynlottonr
from . import simple_pages
from . import store_tickets

# fragen wie das mit env./ config.py und sql url laeuft ..


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_blueprints(app)
    register_extensions(app)

    return app

# Blueprints


def register_blueprints(app: Flask):
    app.register_blueprint(dynlottonr.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)
    app.register_blueprint(store_tickets.routes.blueprint)


def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)


if __name__ == '__main__':
    app.run()
