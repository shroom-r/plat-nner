from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField
from wtforms.validators import DataRequired, Optional

class NewEventPost(FlaskForm):
    name = StringField("name", validators=[DataRequired()], render_kw={"placeholder": "Nom du poste"})
    start_time = TimeField("start_time", validators=[Optional()], format='%H:%M')
    end_time = TimeField("end_time", validators=[Optional()], format='%H:%M')
    submit = SubmitField("Add")