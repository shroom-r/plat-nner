from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    secretCode = StringField("Secret code", validators=[DataRequired()], render_kw={'autofocus': True})
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Register")
    message = ""
