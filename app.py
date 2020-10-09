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


@app.route('/', methods=['GET', 'POST'])  # méthodes autorisées sur ma route
def index():  # Vue dans laquel on traite les données du formulaire
    if request.method == 'POST':  # indiquer au paramètre 'methods' routes autorisées
        name = request.form.get('name')  # récup infos du formulaire grâce à request
        task = Task(name=name)  # créer tâche ds ma bdd en passant par Model Task
        db.session.add(task)  # ajouter objet 'task' à la session
        db.session.commit()  # enregistrer objet à la session
        return redirect(url_for('index'))  # rediriger l'utilisateur vers page 'index' grâce à url_for qui envoie vers vue
    else:
        tasks = Task.query.order_by(Task.created_at).all()
    return render_template('index.html', tasks=tasks)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Task.query.get_or_404(id)  # on récupère la tâche dans notre bdd grâce à l'id
    if request.method == 'POST':
        task.name = request.form.get('name')  # on màj le nom de la tâche avec les données reçues du formulaire
        db.session.commit()
        return redirect(url_for('index'))
    else:
        return render_template('update.html', task=task)


@app.route('/delete/<int:id>')
def delete(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))


