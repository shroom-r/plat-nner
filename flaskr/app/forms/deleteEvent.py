from flask_wtf import FlaskForm

class DeleteEventForm(FlaskForm):
    # Need form, even empty, to have csrf token
    pass