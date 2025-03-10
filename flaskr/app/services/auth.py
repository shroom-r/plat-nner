from flask_login import  login_user

def logUser(user):
    user.is_authenticated = True
    login_user(user,remember=True)