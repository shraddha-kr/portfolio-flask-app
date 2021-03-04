from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields.html5 import EmailField

class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [
            DataRequired(),
            Email(message=('* Not a valid email address.'))])
    subject = StringField('Subject', [DataRequired()])
    message = TextAreaField('Message', [
        DataRequired()])
    #recaptcha = RecaptchaField()
    submit = SubmitField('Send')
