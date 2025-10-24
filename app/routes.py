from flask import render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, bcrypt
from app.forms import UserForm, LoginForm, ContatoForm, TransacaoForm
from app.models import User, Contato, Transacao
from datetime import datetime

# ------------------ HOME ------------------
@app.route("/", methods=["GET", "POST"])
def inicial():
    return render_template("paginaInicial.html")

# ------------------ LOGIN ------------------
@app.route("/login_page", methods=["GET", "POST"])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for("welcome"))

    form = LoginForm()
    if form.validate_on_submit():
        user = form.login()
        if user:
            login_user(user)
            flash(f"Login realizado com sucesso! Bem-vindo(a), {user.nome}.", "success")
            return redirect(url_for("welcome"))
        else:
            flash("E-mail ou senha incorretos.", "danger")

    return render_template("login.html", form=form)


# ------------------ WELCOME / DASHBOARD ------------------
@app.route("/welcome", methods=["GET", "POST"])
@login_required
def welcome():
    user = current_user
    destinatarios = User.query.filter(User.id != user.id).all()
    transacoes = Transacao.query.filter(
        (Transacao.remetente_id == user.id) | (Transacao.destinatario_id == user.id)
    ).order_by(Transacao.data.desc()).all()

    if request.method == "POST":
        destinatario_id = int(request.form.get("destinatario_id", 0))
        valor = float(request.form.get("valor", 0))
        descricao = request.form.get("descricao", "")

        destinatario = User.query.get(destinatario_id)

        if not destinatario:
            flash("Destinatário não encontrado.", "danger")
        elif destinatario.id == user.id:
            flash("Você não pode transferir para si mesmo.", "warning")
        elif valor <= 0:
            flash("Digite um valor válido para a transferência.", "warning")
        elif user.saldo < valor:
            flash("Saldo insuficiente!", "danger")
        else:
            user.saldo -= valor
            destinatario.saldo += valor
            transacao = Transacao(
                remetente_id=user.id,
                destinatario_id=destinatario.id,
                valor=valor,
                descricao=descricao
            )
            db.session.add(transacao)
            db.session.commit()
            flash(f"Transferência de {valor:.2f} HC enviada para {destinatario.nome}!", "success")
            return redirect(url_for("welcome"))

    return render_template("welcome.html", user=user, destinatarios=destinatarios, transacoes=transacoes)


# ------------------ CADASTRO ------------------
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if current_user.is_authenticated:
        return redirect(url_for("login_page"))

    form = UserForm()
    if request.method == "POST":
        tipo = request.form.get("tipo")
        # === Cadastro de Morador ===
        if tipo == "morador" and form.validate_on_submit():
            user = User(
                nome=form.nome.data,
                sobrenome=form.sobrenome.data,
                email=form.email.data,
                senha=bcrypt.generate_password_hash(form.senha.data).decode('utf-8'),
                saldo=0.0,
                is_comercio=False
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash("Cadastro realizado com sucesso! Faça login para continuar.", "success")
            return redirect(url_for("login_page"))        
        # === Cadastro de Comércio ===
        elif tipo == "comercio":
            nome = request.form.get("nome")
            proprietario = request.form.get("proprietario")
            email = request.form.get("email")
            comercio = User(
                nome=nome,
                sobrenome=proprietario,
                email=email,
                senha=bcrypt.generate_password_hash("123").decode('utf-8'),
                saldo=0.0,
                is_comercio=True
            )
            db.session.add(comercio)
            db.session.commit()
            flash("Comércio cadastrado com sucesso! Faça login para continuar.", "success")
            return redirect(url_for("login_page"))

        else:
            flash("Tipo de cadastro inválido ou dados incorretos.", "danger")

    return render_template("cadastro.html", form=form)


# ------------------ LOGOUT ------------------
@app.route("/sair")
@login_required
def logout():
    logout_user()
    session.clear()
    flash("Logout realizado com sucesso!", "info")
    return redirect(url_for("inicial"))


# ------------------ PÁGINA DE COMÉRCIOS ------------------
@app.route("/comercios", methods=["GET", "POST"])
def comercios_page():
    if request.method == "POST":
        nome = request.form.get("nome").strip()
        if User.query.filter_by(nome=nome, is_comercio=True).first():
            flash("Esse nome já está cadastrado!", "warning")
            return redirect(url_for("comercios_page"))

        email_fake = f"{nome.replace(' ', '').lower()}@comercio.com"
        senha_fake = bcrypt.generate_password_hash("123").decode('utf-8')
        comercio = User(
            nome=nome,
            email=email_fake,
            senha=senha_fake,
            saldo=0.0,
            is_comercio=True
        )
        db.session.add(comercio)
        db.session.commit()
        flash("Comércio cadastrado com sucesso!", "success")
        return redirect(url_for("comercios_page"))

    comercios = User.query.filter_by(is_comercio=True).all()
    return render_template("comercios.html", comercios=comercios)


# ------------------ BANCO SOCIAL ------------------
@app.route('/social', methods=['GET', 'POST'])
@login_required
def social():
    destinatarios = User.query.filter(User.id != current_user.id).all()  # todos exceto você
    transacoes = Transacao.query.filter(
        (Transacao.remetente_id == current_user.id) | 
        (Transacao.destinatario_id == current_user.id)
    ).order_by(Transacao.data.desc()).all()

    if request.method == 'POST':
        acao = request.form.get('acao')

        if acao == 'transferir':
            destinatario_id = int(request.form.get('destinatario'))
            valor = float(request.form.get('valor'))
            descricao = request.form.get('descricao', '')

            if valor > 0 and current_user.saldo >= valor:
                transacao = Transacao(
                    remetente_id=current_user.id,   # 🔹 corrigido
                    destinatario_id=destinatario_id,
                    valor=valor,
                    descricao=descricao,
                    data=datetime.utcnow()
                )
                current_user.saldo -= valor
                db.session.add(transacao)
                db.session.commit()
                flash("Transferência realizada com sucesso!", "success")
            else:
                flash("Saldo insuficiente ou valor inválido.", "danger")

        elif acao == 'adicionar':
            valor = float(request.form.get('quantidade'))
            descricao = request.form.get('descricao', '')
            current_user.saldo += valor
            transacao = Transacao(
                remetente_id=current_user.id,
                destinatario_id=current_user.id,
                valor=valor,
                descricao=descricao,
                data=datetime.utcnow()
            )
            db.session.add(transacao)
            db.session.commit()
            flash("Créditos adicionados com sucesso!", "success")

        # outros tipos (recarga, boleto) seguem a mesma lógica

        return redirect(url_for('social'))

    return render_template('social.html', user=current_user, destinatarios=destinatarios, transacoes=transacoes)

@app.route("/nova_transacao", methods=["GET", "POST"])
def nova_transacao():
    form = TransacaoForm()
    form.set_choices()  # MUITO IMPORTANTE: precisa ser chamado antes do validate_on_submit

    if form.validate_on_submit():
        form.save()
        flash("Transação registrada com sucesso!", "success")
        return redirect(url_for("dashboard"))  # ajuste conforme sua rota

    return render_template("nova_transacao.html", form=form)

# ------------------ CONTATO ------------------
@app.route("/contato", methods=["GET", "POST"])
def contato():
    form = ContatoForm()
    if form.validate_on_submit():
        form.save()
        flash("Mensagem enviada com sucesso!", "success")
        return redirect(url_for("login_page"))
    return render_template("contato.html", form=form)
