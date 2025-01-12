import os
from flask import Flask,redirect,render_template,url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from forms import  Addquote


app = Flask(__name__)

app.config['SECRET_KEY'] = 'idkwhattoputhere'


###
#dbstuff


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


class quotes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    quote = db.Column(db.Text)

    def __init__(self,quote):
        self.quote = quote

    def __repr__(self):
        return self.quote
    
#####

@app.route('/')
def index():
    quote = quotes.query.all()
    return render_template("home.html", quote=quote)


@app.route('/add',methods=['GET','POST'])
def add():
    form = Addquote()

    if form.validate_on_submit():
        quote = form.quote.data
        neq = quotes(quote)
        db.session.add(neq)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('add.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)