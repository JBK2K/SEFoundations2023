from app.app import create_app
from app.dynlottonr.models import Lottoresults, Main, Super, User, Usertickets
from app.extensions.database import db

from werkzeug.security import generate_password_hash, check_password_hash

if __name__ == '__main__':
    app = create_app()
    app.app_context().push()

# lottonr = {
#     'monday': {'main': [3, 8, 24, 21, 22], 'super': [1, 6]},
#     'tuesday': {'main': [3, 8, 24, 19, 21], 'super': [1, 9]},
#     'wednesday': {'main': [3, 4, 8, 19, 20], 'super': [5, 6]},
#     'thursday': {'main': [2, 7, 17, 14, 20], 'super': [2, 9]},
#     'friday': {'main': [1, 7, 12, 15, 20], 'super': [2, 10]},
#     'saturday': {'main': [3, 7, 16, 19, 29], 'super': [9, 12]},
#     'sunday': {'main': [3, 7, 16, 19, 29], 'super': [9, 12]}, }
# print(lottonr)
# print('Hello World')


# hashed_password = 'pbkdf2:sha256:260000$qDhowSZPOtKIyHEg$f39726e0d6a1f149de76355bf3f583c760dbce1e82927ac1ccb6a5c8a65123c0'
# password_to_check = 'super secret'

# is_password_valid = check_password_hash(hashed_password, 'super secret')

# print(is_password_valid)
# True / False


# def seed():
#     for day, numbers in lottonr.items():
#         main = Main(nr1=numbers['main'][0], nr2=numbers['main'][1],
#                     nr3=numbers['main'][2], nr4=numbers['main'][3], nr5=numbers['main'][4])
#         super = Super(nr1=numbers['super'][0], nr2=numbers['super'][1])
#         main.save()
#         super.save()
#         lotto = Lottoresults(day=day, mainnr_id=main.id, supernr_id=super.id)

#         lotto.save()
#         print('saved to backend')


# seed()


# # delete all entries in lottoresults
# def delete():
#     up = Lottoresults.query.all()
#     for item in up:
#         item.delete()
#     print('success!')

#     main = Main.query.all()
#     for item in main:
#         item.delete()
#     print('success!')

#     super = Super.query.all()
#     for item in super:
#         item.delete()
#     print('success!')


# delete()


# def delete_x():
#     # delete day monday with main and super id

#     up = Lottoresults.query.filter_by(day='tuesday').first()
#     print(up)
#     # print all content of monday
#     print(up.day, up.mainnr_id, up.supernr_id)

#     # delete main and super id with up.mainnr_id and up.supernr_id
#     main = Main.query.filter_by(id=up.mainnr_id).first()
#     super = Super.query.filter_by(id=up.supernr_id).first()
#     print(main.id, main.nr1, main.nr2, main.nr3, main.nr4, main.nr5)
#     print(super.id, super.nr1, super.nr2)
#     main.delete()
#     super.delete()
#     up.delete()

#     print('success!')


# delete_x()


# def x_delete():
#     one = Lottoresults.query.all()
#     for item in one:
#         item.delete()
#     # one.delete()
#     print(one)
#     two = Main.query.all()
#     for item in two:
#         item.delete()
#     # two.delete()
#     print(two)
#     three = Super.query.all()
#     for item in three:
#         item.delete()
#     # three.delete()
#     print(three)
#     four = User.query.all()
#     for item in four:
#         item.delete()
#     # four.delete()
#     print(four)
#     five = Usertickets.query.all()
#     for item in five:
#         item.delete()
#     # five.delete()
#     print(five)
#     print('success!')


# x_delete()
# def delete_alluser():
#     up = User.query.all()
#     print(up)
#     for item in up:
#         item.delete()


# delete_alluser()


# function with arg  usertickets.id

# test()

# def update():
#     up = Lottoresults().query.filter_by(day='monday').all()
#     print(up)
#     for day in up:
#         day.day = 'montag'
#         day.save()


# update()

# def delete():
#     # up = Lottoresults.query.all()
#     # print(up)
#     # for x in range(len(up)):
#     #     Haupt = Main().query.filter_by(id=up[x].mainnr_id).first()

#     #     if Haupt:
#     #         Haupt.delete()

#     #     extra = Super().query.filter_by(id=up[x].supernr_id).first()

#     #     if extra:
#     #         extra.delete()

#     # for day in up:
#     #     day.delete()
#     main = Main.query.all()
#     for item in main:
#         item.delete()
#     super = Super.query.all()
#     for item in super:
#         item.delete()

# user = Usertickets.query.all()
# for item in user:
#      item.delete()


# delete()
