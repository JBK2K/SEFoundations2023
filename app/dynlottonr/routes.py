from flask import Blueprint, render_template
blueprint = Blueprint('eurojackpot', __name__)
from .models import Lottoresults, Main, Super

# lottonr = {
#   'monday' : {'main':[3,8,24,21,22 ] , 'super': [1,6]},
#   'tuesday' : {'main':[3,8,24,19,21 ] , 'super': [1,9]},
#   'wednesday' : {'main':[3,4,8,19,20 ] , 'super': [5,6]},
#   'thursday' : {'main':[2,7,17,14,20 ] , 'super': [2,9]},
#   'friday' : {'main':[1,7,12,15,20 ] , 'super': [2,10]},
#   'saturday' : {'main':[3,7,16,19,29 ] , 'super': [9,12]},
#   'sunday' : {'main':[3,7,16,19,29 ] , 'super': [9,12]},}


# jinja templating first example
@blueprint.route('/eurojackpot')
def lotto():
    lottonr = Lottoresults.query.all()
    return render_template('lottonum/eurojackpot.html', lottonr=lottonr)
    
# das klappt aber nicht innerhalb eine page...
@blueprint.route('/eurojackpot/<day>')
def eurojackpot(day): 
    dayresult = Lottoresults.query.filter_by(day=day).first_or_404()
    mainres = Main.query.filter_by(id=dayresult.mainnr_id).first()

    superres = Super.query.filter_by(id=dayresult.supernr_id).first()
    return render_template(
        'lottonum/eurojackpotresult.html', 
        mainnr=[mainres.nr1, mainres.nr2, mainres.nr3, mainres.nr4,mainres.nr5],
        supernr=[superres.nr1, superres.nr2],
        day=dayresult.day
        )