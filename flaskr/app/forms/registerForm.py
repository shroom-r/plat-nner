from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    secretCode = StringField("Secret code", validators=[DataRequired()])
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Register")
    message = ""
