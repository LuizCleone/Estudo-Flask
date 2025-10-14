from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db
from app.forms import UserForm, LoginForm, ContatoForm
from app.models import User, Contato
from app import bcrypt
from flask import session

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
    session.clear()  # 🔥 limpa mensagens e dados antigos
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