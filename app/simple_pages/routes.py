from flask import Blueprint, render_template
blueprint = Blueprint('simple_pages', __name__)


@blueprint.route('/')
def landingpage():
    return render_template('simple_pages/home.html')


@blueprint.route('/about')
def about():
    return render_template('simple_pages/about.html')
