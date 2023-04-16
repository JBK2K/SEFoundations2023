from flask import Blueprint, render_template, request, redirect, url_for
from app.dynlottonr.models import Lottoresults, Main, Super, User, Usertickets
from app.extensions.database import db, CRUDMixin


blueprint = Blueprint('user_login', __name__)


@blueprint.get('/login')
def get_login():
    print('get login xxxDDD')
    return render_template('logsignup/login.html')


@blueprint.post('/login')
def post_login():
    print('logged in YYYYDDD')
    return "user logged in"


@blueprint.get('/logout')
def logout():
    return 'User logged out'

# register ab hier


@blueprint.get('/register')
def get_register():
    print('get register xxxDDD')
    return render_template('logsignup/signup.html')


@blueprint.post('/register')
def post_register():
    print(request.form)

    new_user = User(
        name=request.form['username'],
        mail=request.form['email'],
        password=request.form['password']
    )

    # check if user already exists
    user = User.query.filter_by(name=request.form['username']).first()
    if user:
        print('user already exists')
        return redirect(url_for('user_login.get_login'))

    new_user.save()
    print('success!')
    return 'User created'
