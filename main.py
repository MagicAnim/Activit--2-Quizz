# On importe Flask du module flask
from flask import Flask, render_template


# CREATION DE l'APP
# On crée une instance de Flask qui est donc notre app qu'on stocke dans la variable app
app = Flask("Mon Super Quizz")


# Route de notre page d'accueil qui est donc à la racine de notre app
@app.route("/")
def index():
    return render_template("index.html")

# Route seconde Page
@app.route("/question")
def seconde_page():
    return render_template("seconde_page.html", erreur = variable_à_injecter)

# Route permettant de compter les réponses de l'utilisateur
# @app.route("/reponse/<numero>")


# EXECUTION
# host = "0.0.0.0" -> app accessible par n'importe quelle adresse
# port = 81 -> port d'écoute du serveur de l'app
app.run(host = "0.0.0.0", port = 81)