from app import app, db
from flask import render_template, url_for, request #renderizar arquivo html
from app.models import Contato

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/contato/", methods = ["GET", "POST"])
def secondpage():
   context = {}
   if request.method == "GET":
      pesquisa = request.args.get("pesquisa")
      context.update({"pesquisa" : pesquisa})

   if request.method == "POST":
      nome = request.form["nome"]
      email = request.form["email"]
      assunto = request.form["assunto"]
      mensagem = request.form["mensagem"]

      contato = Contato(
         nome = nome,
         email = email,
         assunto = assunto,
         mensagem = mensagem
      )

      db.session.add(contato)
      db.session.commit()

   return render_template("contato.html", context = context)