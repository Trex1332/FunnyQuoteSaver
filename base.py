import os
from flask import Flask,redirect,render_template,url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRECT_KEY'] = 'idkwhattoputhere'


###
#dbstuff


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


class quotes(db.Model):
    id = db.Column(db.Integer, primay_key = True)
    quote = db.Column(db.Text)

    def __init__(self,quote):
        self.quote = quote

    def __repr__(self):
        return self.quote