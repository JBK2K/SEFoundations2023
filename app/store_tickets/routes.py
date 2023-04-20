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


@blueprint.route('/tickets')
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


@blueprint.post('/tickets/delete')
@login_required
def delete_tickets():
    print("Delete tickets")
    mainnr_id = request.form['mainnr_id']
    supernr_id = request.form['supernr_id']
    ticket_id = request.form['ticket_id']

    print(mainnr_id, supernr_id, ticket_id)
    up = Usertickets.query.filter_by(id=ticket_id).first()

    print(up)
    print(up.id, up.user_id, up.playday, up.mainnr_id, up.supernr_id)
    # delete main and super id with up.mainnr_id and up.supernr_id
    main = Main.query.filter_by(id=up.mainnr_id).first()
    super = Super.query.filter_by(id=up.supernr_id).first()
    print(main.id, main.nr1, main.nr2, main.nr3, main.nr4, main.nr5)
    print(super.id, super.nr1, super.nr2)
    main.delete()
    super.delete()
    up.delete()
    print('deleted from backend')

    return redirect(url_for('ticket_form.get_tickets'))

# create an edit function that looks like the delete function


@blueprint.post('/tickets/edit')
@login_required
def edit_tickets():
    print('edit tickets')
    playday = request.form['playday']
    mainnr_id = request.form['mainnr_id']
    supernr_id = request.form['supernr_id']
    ticket_id = request.form['ticket_id']
    mainr_1 = request.form['main1']
    mainr_2 = request.form['main2']
    mainr_3 = request.form['main3']
    mainr_4 = request.form['main4']
    mainr_5 = request.form['main5']
    superr_1 = request.form['super1']
    superr_2 = request.form['super2']
    print(playday)
    print(mainnr_id, supernr_id, ticket_id)
    print(mainr_1, mainr_2, mainr_3, mainr_4, mainr_5)
    print(superr_1, superr_2)

    up = Usertickets.query.filter_by(id=ticket_id).first()
    # updated playday
    up.playday = playday
    # update main and super table based on mainnr_id and supernr_id
    main = Main.query.filter_by(id=up.mainnr_id).first()
    super = Super.query.filter_by(id=up.supernr_id).first()

    main.nr1 = mainr_1
    main.nr2 = mainr_2
    main.nr3 = mainr_3
    main.nr4 = mainr_4
    main.nr5 = mainr_5
    super.nr1 = superr_1
    super.nr2 = superr_2

    main.save()
    super.save()
    up.save()

    print('success!')

    return redirect(url_for('ticket_form.get_tickets'))
