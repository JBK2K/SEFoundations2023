from flask import Blueprint, render_template, request, redirect, url_for
from app.dynlottonr.models import Lottoresults, Main, Super, User, Usertickets
from app.extensions.database import db, CRUDMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user


blueprint = Blueprint('user_login', __name__)


@blueprint.get('/login')
def get_login():
    print('get login xxxDDD')
    return render_template('logsignup/login.html')


@blueprint.post('/login')
def post_login():
    print('logged in YYYYDDD')
    print(request.form)

    user = User.query.filter_by(mail=request.form['email']).first()

    if not user or not check_password_hash(user.password, request.form['password']):
        print('wrong email or password')
        return render_template('logsignup/login.html', error='Wrong email or password')
    else:
        print('success!')
        # reroute to other page.
    login_user(user)
    return redirect(url_for('ticket_form.get_tickets'))


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
        password=generate_password_hash(request.form.get('password')))

    # check if user already exists
    user = User.query.filter_by(mail=request.form['email']).first()
    if user:
        print('user already exists')
        # make alert that user exists already
        return render_template('logsignup/signup.html', error='The email address is already registered.')

    else:
        new_user.save()
        print('success!')

        login_user(new_user)
        return redirect(url_for('ticket_form.get_tickets'))
