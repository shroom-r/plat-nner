from flask_wtf import FlaskForm

class DeleteAttendeeForm(FlaskForm):
    # Need form, even empty, to have csrf token
    pass