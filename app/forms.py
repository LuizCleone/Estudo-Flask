
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app import db, bcrypt
from app.models import Contato, User

# ------------------ FORMULÁRIO DE CADASTRO ------------------
class UserForm(FlaskForm):
    nome = StringField(
        "Nome:",
        validators=[DataRequired(message="Por favor, digite seu nome"), Length(min=1, max=50)]
    )
    sobrenome = StringField(
        "Sobrenome:",
        validators=[DataRequired(message="Por favor, digite seu sobrenome"), Length(min=1, max=50)]
    )
    email = StringField(
        "Email:",
        validators=[DataRequired(message='Por favor, digite seu e-mail'), Email(message='Formato de e-mail inválido')]
    )
    senha = PasswordField(
        "Senha:",
        validators=[DataRequired(message="Por favor, digite sua senha")]
    )
    confirmacao_senha = PasswordField(
        "Confirme a senha:",
        validators=[DataRequired(message="Por favor, confirme sua senha"), EqualTo("senha", message="As senhas não coincidem")]
    )
    btnSubmit = SubmitField("Cadastrar")

    # Validação customizada para email já cadastrado
    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Usuário já cadastrado com esse Email")
            
    # Salva o usuário no banco com senha hash
    def save(self):
        hashed_senha = bcrypt.generate_password_hash(self.senha.data).decode('utf-8')
        user = User(
            nome=self.nome.data,
            sobrenome=self.sobrenome.data,
            email=self.email.data,
            senha=hashed_senha
        )
        db.session.add(user)
        db.session.commit()
        return user

# ------------------ FORMULÁRIO DE LOGIN ------------------
class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(message='Por favor, digite seu e-mail'), Email(message='Formato de e-mail inválido')]
    )
    senha = PasswordField(
        "Senha",
        validators=[DataRequired(message="Por favor, digite sua senha")]
    )
    btnSubmit = SubmitField("Login")

    # Valida login do usuário
    def login(self):
        user = User.query.filter_by(email=self.email.data).first()
        if not user:
            return None  # Usuário não encontrado
        if not bcrypt.check_password_hash(user.senha, self.senha.data):
            return None  # Senha incorreta
        return user

# ------------------ FORMULÁRIO DE CONTATO ------------------
class ContatoForm(FlaskForm):
    nome = StringField(
        "Nome",
        validators=[DataRequired(message="Por favor, digite seu nome"), Length(max=50)]
    )
    email = StringField(
        "Email",
        validators=[DataRequired(message="Por favor, digite seu e-mail"), Email(message="Formato de e-mail inválido")]
    )
    assunto = StringField(
        "Assunto",
        validators=[DataRequired(message="Por favor, digite o assunto"), Length(max=100)]
    )
    mensagem = TextAreaField(
        "Mensagem",
        validators=[DataRequired(message="Por favor, digite sua mensagem"), Length(max=500)]
    )
    btnSubmit = SubmitField("Enviar")

    # Salva o contato no banco
    def save(self):
        contato = Contato(
            nome=self.nome.data,
            email=self.email.data,
            assunto=self.assunto.data,
            mensagem=self.mensagem.data
        )
        db.session.add(contato)
        db.session.commit()
        return contato

