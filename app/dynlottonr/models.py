from app.extensions.database import db
from datetime import datetime

from app.extensions.database import db, CRUDMixin


# User tickets table
class Usertickets(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    playday = db.Column(db.String(80))
    mainnr_id = db.Column(db.Integer, db.ForeignKey('main.id'))
    supernr_id = db.Column(db.Integer, db.ForeignKey('super.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# # User data table


class User(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    mail = db.Column(db.String(80))
    password = db.Column(db.String(6))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Lottoresults(db.Model, CRUDMixin,):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(80))
    mainnr_id = db.Column(db.Integer, db.ForeignKey('main.id'))
    supernr_id = db.Column(db.Integer, db.ForeignKey('super.id'))


class Main(db.Model, CRUDMixin,):
    id = db.Column(db.Integer, primary_key=True)
    nr1 = db.Column(db.Integer)
    nr2 = db.Column(db.Integer)
    nr3 = db.Column(db.Integer)
    nr4 = db.Column(db.Integer)
    nr5 = db.Column(db.Integer)


class Super(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    nr1 = db.Column(db.Integer)
    nr2 = db.Column(db.Integer)
