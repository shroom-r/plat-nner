from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class DeleteAttendeeForm(FlaskForm):
    # Need form, even empty, to have csrf token
    pass
    # submit = SubmitField("x")