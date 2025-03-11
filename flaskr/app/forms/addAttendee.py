from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddAttendeeForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    submit = SubmitField("Add")