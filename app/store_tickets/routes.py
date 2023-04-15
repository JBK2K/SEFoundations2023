from flask import Blueprint, render_template, request
from app.dynlottonr.models import Lottoresults, Main, Super, User, Usertickets
from app.extensions.database import db


blueprint = Blueprint('ticket_form', __name__)


@blueprint.get('/tickets')
def get_tickets():
    print('get tickets')
    return render_template('user_ticket/usertickets.html')


@blueprint.post('/tickets')
def post_tickets():
    print('post tickets')
    # print the form data to the terminal
    print(request.form)
    print(request.form['playday'])
    print(request.form['main1'])

    main = Main(nr1=1, nr2=2, nr3=3, nr4=4, nr5=5)
    main.save()
    super = Super(nr1=1, nr2=2)
    super.save()
    User = Usertickets(playday=request.form['playday'], mainnr_id=main.id,
                       supernr_id=super.id)
    User.save()
    print('saved to backend')
    return render_template('user_ticket/usertickets.html')
    # print the form data to the terminal
