from flask_wtf import FlaskForm
from wtforms import StringField

class Addquote(FlaskForm):
    quote = StringField("Whats Your Quote: ")