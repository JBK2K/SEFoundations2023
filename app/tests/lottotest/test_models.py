from app.extensions.database import db
from app.dynlottonr.models import Lottoresults, Main, Super

def test_lottoresults():
    
    main = Main(nr1=3, nr2=8, nr3=24, nr4=21, nr5=22)
    super = Super(nr1=1, nr2=6)
    main.save()
    super.save()

    main_id = main.id
    super_id = super.id

    if main == Main.query.filter_by(id=main_id).first():
        print('main is in db')
    else:
        print('main is not in db')

    if super == Super.query.filter_by(id=super_id).first():
        print('super is in db')
    else:
        print('super is not in db')

    lotto = Lottoresults(day='monday', mainnr_id=main_id, supernr_id=super_id)
    lotto.save()
    
    lotto_id = lotto.id

    if lotto == Lottoresults.query.filter_by(id=lotto_id).first():
        print('lotto is in db')
    else:
        print('lotto is not in db')
    

    