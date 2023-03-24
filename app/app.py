from flask import Flask, redirect, url_for, render_template

from . import dynlottonr
# from . import simple_pages


def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config')

  register_blueprints(app)

  return app

# Blueprints
def register_blueprints(app: Flask):
  # app.register_blueprint(dynlottonr.routes.blueprint)
  app.register_blueprint(simple_pages.routes.blueprint)


if __name__ == '__main__':
    app.run()


