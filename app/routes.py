from app import app, db
from flask import render_template, url_for, request, redirect #renderizar arquivo html
from flask_login import login_user, logout_user, current_user

from app.models import Contato
from app.forms import ContatoForm, UserForm, LoginForm


@app.route("/", methods = ["GET", "POST"])
def homepage():
   form = LoginForm()

   if form.validate_on_submit():
      user = form.login()
      login_user(user, remember=True)
      
   return render_template("index.html", form = form)


@app.route("/cadastro/", methods = ["GET", "POST"])
def cadastro():
   form = UserForm()
   if form.validate_on_submit():
      user = form.save()
      login_user(user, remember=True)
      return redirect(url_for("homepage"))
   return render_template("cadastro.html", form = form)


@app.route("/sair/")
def logout():
   logout_user()
   return redirect(url_for("homepage"))


@app.route("/contato/", methods = ["GET", "POST"])
def contato():
   form = ContatoForm()
   if form.validate_on_submit():
      form.save()
      return redirect(url_for("homepage"))

   return render_template("contato.html", form = form)

'''
@app.route("/contatoOld/", methods = ["GET", "POST"])
def contatoOld():
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

   return render_template("contatoOld.html", context = context)
'''