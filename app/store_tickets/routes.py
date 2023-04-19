from flask import Blueprint, render_template, request, redirect, url_for
from app.dynlottonr.models import Lottoresults, Main, Super, User, Usertickets
from app.extensions.database import db
from flask_login import login_required, current_user


blueprint = Blueprint('ticket_form', __name__)


# jinja templating first example
@blueprint.route('/eurojackpot')
def lotto():
    page_number = request.args.get('page', 1, type=int)
    # import von config klappt nicht.
    per_page = current_app.config.get('LOTTODAYS_PER_PAGE', 3)
    # lottonr = Lottoresults.query.all()
    lottonr_paginated = Lottoresults.query.paginate(
        page=page_number, per_page=per_page)
    return render_template('lottonum/eurojackpot.html', lottonr_paginated=lottonr_paginated)


@blueprint.get('/tickets')
@login_required
def get_tickets():
    print('get tickets')
    tickets = Usertickets.query.filter_by(user_id=current_user.id).all()
    print(tickets)
    if not tickets:
        print('no tickets')
        return render_template('user_ticket/usertickets.html')
    else:
        print('tickets available')
        for ticket in tickets:
            print(f"Ticket id: {ticket.id}")
            print(f"Playday: {ticket.playday}")
            print(f'Mainnr id:{ticket.mainnr_id}')
            print(f'supernr id:{ticket.supernr_id}')
            print(f'userid:{ticket.user_id}')
            main = Main.query.filter_by(id=ticket.mainnr_id).all()

            for m in main:
                print(
                    f"Main: nr 1{m.nr1} nr2 {m.nr2} nr3 {m.nr3} nr4 {m.nr4} nr5 {m.nr5}")
            super = Super.query.filter_by(id=ticket.supernr_id).all()

            for s in super:
                print(f"Super: s1{s.nr1} s2{s.nr2}")

            maint = Main.query.all()
            supert = Super.query.all()
            print('maint', maint)
            print('supert', supert)
            page_number = request.args.get('page', 1, type=int)

            return render_template('user_ticket/usertickets.html', tickets=tickets, Main=Main, Super=Super)
            # sending main and super does not really work to frondend.


@blueprint.post('/tickets')
@login_required
def post_tickets():
    print('post tickets')
    # print the form data to the terminal
    print(request.form)

    # assign user_id to the current user logged in

    main = Main(nr1=request.form['main1'], nr2=request.form['main2'],
                nr3=request.form['main3'], nr4=request.form['main4'], nr5=request.form['main5'])
    main.save()
    super = Super(nr1=request.form['super1'], nr2=request.form['super2'])
    super.save()

    user_atm = current_user.id
    print(user_atm)
    user_new = Usertickets(playday=request.form['playday'], mainnr_id=main.id,
                           supernr_id=super.id, user_id=user_atm)
    user_new.save()
    print('saved to backend')
    return redirect(url_for('ticket_form.get_tickets'))


@blueprint.put('/tickets/<int:id>')
@login_required
def update_ticket(id):
    # retrieve the existing ticket by id
    existing_ticket = Usertickets.query.filter_by(
        id=id, user_id=current_user.id).first()

    # check if the ticket exists
    if not existing_ticket:
        abort(404)

    # update the ticket with the new form data
    existing_ticket.playday = request.form['playday']
    existing_ticket.mainnr.nr1 = request.form['main1']
    existing_ticket.mainnr.nr2 = request.form['main2']
    existing_ticket.mainnr.nr3 = request.form['main3']
    existing_ticket.mainnr.nr4 = request.form['main4']
    existing_ticket.mainnr.nr5 = request.form['main5']
    existing_ticket.supernr.nr1 = request.form['super1']
    existing_ticket.supernr.nr2 = request.form['super2']

    # commit the changes to the database

    print('updated ticket')
    # return redirect(url_for('ticket_form.get_tickets'))
