from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__) # Crée un instance de la classe Flask, c'est notre app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' # Nom de la bdd
db = SQLAlchemy(app) # Lie notre app à SQLAlchemy


class Task(db.Model): # Modèle
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)


@app.route('/')
def index(): # Méthode appelée lorsqu'on se rend sur la route '/'
    return 'Hello World!'
