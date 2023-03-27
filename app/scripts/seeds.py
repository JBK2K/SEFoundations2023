from app.app import create_app
from app.dynlottonr.models import Lottoresults, Main, Super
from app.extensions.database import db


if __name__ == '__main__':
    app = create_app()
    app.app_context().push()


lottonr = {
    'monday': {'main': [3, 8, 24, 21, 22], 'super': [1, 6]},
    'tuesday': {'main': [3, 8, 24, 19, 21], 'super': [1, 9]},
    'wednesday': {'main': [3, 4, 8, 19, 20], 'super': [5, 6]},
    'thursday': {'main': [2, 7, 17, 14, 20], 'super': [2, 9]},
    'friday': {'main': [1, 7, 12, 15, 20], 'super': [2, 10]},
    'saturday': {'main': [3, 7, 16, 19, 29], 'super': [9, 12]},
    'sunday': {'main': [3, 7, 16, 19, 29], 'super': [9, 12]}, }


def seed():
    for day, numbers in lottonr.items():
        main = Main(nr1=numbers['main'][0], nr2=numbers['main'][1],
                    nr3=numbers['main'][2], nr4=numbers['main'][3], nr5=numbers['main'][4])
        super = Super(nr1=numbers['super'][0], nr2=numbers['super'][1])
        main.save()
        super.save()
        print(main.id)
        lotto = Lottoresults(day=day, mainnr_id=main.id, supernr_id=super.id)

        lotto.save()


def update():
    up = Lottoresults().query.filter_by(day='monday').all()
    print(up)
    for day in up:
        day.day = 'montag'
        day.save()


def delete():
    up = Lottoresults().query.filter_by(day='sunday').all()
    print(up)
    for x in range(len(up)):
      Haupt = Main().query.filter_by(id=up[x].mainnr_id).first()

      if Haupt:
        Haupt.delete()

      extra = Super().query.filter_by(id=up[x].supernr_id).first()
      
      if extra:
        extra.delete()

    for day in up:
        day.delete()


delete()
