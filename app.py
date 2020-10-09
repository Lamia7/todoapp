from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)  # Crée un instance de la classe Flask, c'est notre app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'  # Nom de la bdd
db = SQLAlchemy(app)  # Lie notre app à SQLAlchemy


class Task(db.Model):  # Modèle pour une tâche
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)


@app.route('/', methods=['GET', 'POST'])
def index():  # Vue dans laquel on traite les données du formulaire
    if request.method == 'POST':
        name = request.form.get('name')
        task = Task(name=name)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))
    else:
        tasks = Task.query.order_by(Task.created_at).all()
    return render_template('index.html', tasks=tasks)
