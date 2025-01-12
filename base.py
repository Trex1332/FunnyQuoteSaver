import os
from flask import Flask,redirect,render_template,url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRECT_KEY'] = 'idkwhattoputhere'

