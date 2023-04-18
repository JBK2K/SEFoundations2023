from flask import Blueprint, render_template, request
from app.dynlottonr.models import Lottoresults, Main, Super, User, Usertickets
from app.extensions.database import db
from flask_login import login_required


blueprint = Blueprint('ticket_form', __name__)

# user_dict = {
#     'name': 'Max',
#     'mail': 'max.meier@gmail.com',
#     'password': '56789000'
# }


@blueprint.get('/tickets')
@login_required
def get_tickets():
    print('get tickets')
    return render_template('user_ticket/usertickets.html')


@blueprint.post('/tickets')
@login_required
def post_tickets():
    print('post tickets')
    # print the form data to the terminal
    print(request.form)

    # user = User(
    #     name=user_dict['name'], mail=user_dict['mail'], password=user_dict['password'])
    # user.save()

    main = Main(nr1=request.form['main1'], nr2=request.form['main2'],
                nr3=request.form['main3'], nr4=request.form['main4'], nr5=request.form['main5'])
    main.save()
    super = Super(nr1=request.form['super1'], nr2=request.form['super2'])
    super.save()

    user_new = Usertickets(playday=request.form['playday'], mainnr_id=main.id,
                           supernr_id=super.id, user_id=user.id)
    user_new.save()
    print('saved to backend')
    return render_template('user_ticket/usertickets.html')
    # print the form data to the terminal
