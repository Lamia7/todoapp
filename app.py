from flask import Flask

app = Flask(__name__)  # Création d'instance de Flask : notre app


@app.route('/')
def index():  # Méthode appelée depuis la route /
    return "Hello World!"


if __name__ == "__main__":
    app.run()
