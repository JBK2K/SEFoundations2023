from flask import Blueprint, render_template
blueprint = Blueprint('simple_pages', __name__)


@blueprint.route('/')
def landingpage():
    return render_template('simple_pages/home.html')

# if back to main page
@blueprint.route('/home')
def home():
    return redirect('http://127.0.0.1:5000/')

# route only login 
@blueprint.route('/login')
def login():
    return render_template('simple_pages/login.html')

#only underconstruktion
@blueprint.route('/contact')
def contact():
    return render_template('simple_pages/contact.html')

@blueprint.route('/about')
def about():
    return render_template('simple_pages/about.html')