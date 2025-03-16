from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, Optional

class NewEvent(FlaskForm):
    date = DateField("Date", validators=[DataRequired()], format='%Y-%m-%d')
    name = StringField("Nom de l'évènement", validators=[Optional()])
    submit = SubmitField("Créer")