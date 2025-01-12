from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class Addquote(FlaskForm):
    quote = StringField("Whats Your Quote: ")
    send = SubmitField("Submit")