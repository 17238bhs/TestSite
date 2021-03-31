from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db' #tell where database is, old connection methods not needed, URI is Universal Resource Index
db = SQLAlchemy(app) #does everything for us in the background

class Pizza (db.Model):
    __tablename__ = "Pizza" #if your class name is same as table name, this isnt needed, but good to do*
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    photo = db.Column(db.String())

class Topping (db.Model):
    __tablename__ = "Topping"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())

toppings = db.Table ('toppings', db.Column('pid', db.Integer, db.ForeignKey('Pizza.id'), primary_key=True), db.Column('tid', db.Integer, db.ForeignKey('Topping.id'), primary_key=True))


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/pizza/<int:id>')
def pizza(id):
    pizza = Pizza.query.filter_by(id=id).first_or_404() #get first result else 404
    return render_template ('pizza.html', pizza = pizza)

if __name__ == "__main__":
    app.run(port=3000)