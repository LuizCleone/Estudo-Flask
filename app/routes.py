from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from app.forms import UserForm, LoginForm, ContatoForm
from app.models import User, Contato
from app import bcrypt

# ------------------ HOME / LOGIN ------------------
@app.route("/", methods=["GET", "POST"])
def homepage():
    if current_user.is_authenticated:
        return redirect(url_for("welcome"))

    form = LoginForm()
    
    if form.validate_on_submit():
        user = form.login()
        if user:
            login_user(user)  # Loga o usuário com Flask-Login
            flash(f"Bem-vindo, {user.nome}!", "success")
            return redirect(url_for("welcome"))
        else:
            flash("E-mail ou senha incorretos.", "danger")
    
    return render_template("index.html", form=form)


# ------------------ WELCOME / DASHBOARD ------------------
@app.route("/welcome")
@login_required
def welcome():
    return render_template("welcome.html", user=current_user)


# ------------------ CADASTRO ------------------
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if current_user.is_authenticated:
        return redirect(url_for("welcome"))

    form = UserForm()
    if form.validate_on_submit():
        user = form.save()
        login_user(user)  # Faz login automático após cadastro
        flash(f"Usuário {user.nome} cadastrado com sucesso!", "success")
        return redirect(url_for("welcome"))

    return render_template("cadastro.html", form=form)


# ------------------ LOGOUT ------------------
@app.route("/sair")
@login_required
def logout():
    logout_user()
    flash("Logout realizado com sucesso!", "success")
    return redirect(url_for("homepage"))


# ------------------ CONTATO ------------------
@app.route("/contato", methods=["GET", "POST"])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        form.save()
        flash("Mensagem enviada com sucesso!", "success")
        return redirect(url_for("homepage"))
    
    return render_template("contato.html", form=form)


# ------------------ CONTATO ANTIGO (Exemplo de GET/POST manual) ------------------
@app.route("/contatoOld", methods=["GET", "POST"])
def contatoOld():
    context = {}
    
    if request.method == "GET":
        pesquisa = request.args.get("pesquisa")
        context.update({"pesquisa": pesquisa})
    
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        assunto = request.form.get("assunto")
        mensagem = request.form.get("mensagem")

        contato = Contato(
            nome=nome,
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )

        db.session.add(contato)
        db.session.commit()
        flash("Mensagem enviada com sucesso!", "success")
        return redirect(url_for("contatoOld"))

    return render_template("contatoOld.html", context=context)




"""
from app import app, db
from flask import render_template, url_for, request, redirect, flash, session
from flask_login import login_user, logout_user, current_user

from app.models import Contato
from app.forms import ContatoForm, UserForm, LoginForm


@app.route("/", methods = ["GET", "POST"])
def homepage():
    form = LoginForm()
    
    if form.validate_on_submit():  # Verifica se o formulário foi enviado e validado
        user = form.login()
        
        if user:
            # Login bem-sucedido
            session["user_id"] = user.id  # Armazena o ID do usuário na sessão
            flash(f"Bem-vindo, {user.email}!", "success")
            return redirect(url_for("welcome"))
        else:
            # Usuário ou senha incorretos
            flash("E-mail ou senha incorretos.", "danger")
    
    return render_template("index.html", form=form)

def homepage():
   form = LoginForm()

   if form.validate_on_submit():
      user = form.login()
      login_user(user, remember=True)
      return redirect(url_for('welcome'))
      
   return render_template("index.html", form = form)


   from flask import render_template, redirect, url_for, flash, session
from app import app, db, bcrypt
from app.forms import UserForm, LoginForm, ContatoForm
from app.models import User, Contato

# ------------------ HOME / LOGIN ------------------
@app.route("/", methods=["GET", "POST"])
def homepage():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = form.login()
        if user:
            session["user_id"] = user.id
            flash(f"Bem-vindo, {user.nome}!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("E-mail ou senha incorretos.", "danger")
    
    return render_template("index.html", form=form)


# ------------------ DASHBOARD ------------------
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Você precisa fazer login primeiro.", "warning")
        return redirect(url_for("homepage"))
    
    user = User.query.get(session["user_id"])
    return render_template("dashboard.html", user=user)


# ------------------ CADASTRO ------------------
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    form = UserForm()
    
    if form.validate_on_submit():
        user = form.save()
        flash(f"Usuário {user.nome} cadastrado com sucesso!", "success")
        return redirect(url_for("homepage"))
    
    return render_template("cadastro.html", form=form)


# ------------------ CONTATO ------------------
@app.route("/contato", methods=["GET", "POST"])
def contato():
    form = ContatoForm()
    
    if form.validate_on_submit():
        form.save()
        flash("Mensagem enviada com sucesso!", "success")
        return redirect(url_for("homepage"))
    
    return render_template("contato.html", form=form)


# ------------------ LOGOUT ------------------
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    flash("Logout realizado com sucesso!", "success")
    return redirect(url_for("homepage"))



@app.route('/welcome')
def welcome():
    return render_template('welcome.html')



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
"""