from .models import Lottoresults, Main, Super
from flask import Blueprint, render_template, request, current_app, redirect, url_for
from app.simple_pages import routes


blueprint = Blueprint('eurojackpot', __name__)


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


# das klappt aber nicht innerhalb eine page...
@blueprint.route('/eurojackpot/<day>')
def eurojackpot(day):
    dayresult = Lottoresults.query.filter_by(day=day).first_or_404()
    mainres = Main.query.filter_by(id=dayresult.mainnr_id).first()

    superres = Super.query.filter_by(id=dayresult.supernr_id).first()
    return render_template(
        'lottonum/eurojackpotresult.html',
        mainnr=[mainres.nr1, mainres.nr2,
                mainres.nr3, mainres.nr4, mainres.nr5],
        supernr=[superres.nr1, superres.nr2],
        day=dayresult.day
    )


# store data in db.
@blueprint.route('/run-seed')
def run_seed():
    if not Lottoresults.query.filter_by(day='monday').first():
        import app.scripts.seeds
        print('stored data to db')
        return 'Database seed completed!'
    else:
        print('already in db')
        return redirect(url_for('simple_pages.landingpage'))
