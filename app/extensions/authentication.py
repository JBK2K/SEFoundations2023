from flask_login import LoginManager
from app.dynlottonr.models import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    print("authentication = user_id", user_id)

    return User.query.get(user_id)