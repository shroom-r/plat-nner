from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired, Optional

class NewEvent(FlaskForm):
    date = DateField("date", validators=[DataRequired()], format='%Y-%m-%d')
    name = StringField("name", validators=[Optional()], render_kw={"placeholder": "Nom du poste"})
    # start_time = TimeField("start_time", validators=[Optional()], format='%H:%M')
    # end_time = TimeField("end_time", validators=[Optional()], format='%H:%M')
    submit = SubmitField("Add")