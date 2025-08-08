from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, Optional
import datetime

class NewEvent(FlaskForm):
    date = DateField("Date", validators=[DataRequired()], format='%Y-%m-%d', default=datetime.date.today)
    name = StringField("Nom de l'évènement", validators=[DataRequired()])
    submit = SubmitField("Créer")