from flask_wtf import FlaskForm

class DeletePostForm(FlaskForm):
    # Need form, even empty, to have csrf token
    pass