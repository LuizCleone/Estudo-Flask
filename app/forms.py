
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, NumberRange, ValidationError
from app.models import User, Contato, Transacao
from datetime import datetime
from app import db, bcrypt

# ------------------ FORMULÁRIO DE CADASTRO ------------------
class UserForm(FlaskForm):
    tipo = SelectField(
        "Tipo de cadastro:",
        choices=[("morador", "Morador"), ("comercio", "Comércio")],
        validators=[DataRequired(message="Selecione o tipo de cadastro")]
    )

    nome = StringField("Nome:", validators=[DataRequired(), Length(max=50)])
    sobrenome = StringField("Sobrenome:", validators=[Optional(), Length(max=50)])
    endereco = StringField("Endereço:", validators=[DataRequired(), Length(max=100)])
    email = StringField("Email:", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha:", validators=[Optional(), Length(min=6)])
    confirmacao_senha = PasswordField("Confirme a senha:", validators=[Optional(), EqualTo("senha")])

    nomefantasia = StringField("Nome Fantasia:", validators=[Optional(), Length(max=100)])
    cnpj = StringField("CNPJ:", validators=[Optional(), Length(min=14, max=18)])
    proprietario = StringField("Proprietário:", validators=[Optional(), Length(max=100)])

    btnSubmit = SubmitField("Cadastrar")

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Já existe um usuário com esse e-mail.")

    def validate(self, extra_validators=None):
        rv = super().validate(extra_validators)
        if not rv:
            return False

        if self.tipo.data == "morador":
            if not self.sobrenome.data:
                self.sobrenome.errors.append("Sobrenome é obrigatório para moradores.")
                return False
            if not self.senha.data:
                self.senha.errors.append("Senha é obrigatória para moradores.")
                return False
            if not self.confirmacao_senha.data:
                self.confirmacao_senha.errors.append("Confirme sua senha.")
                return False
        elif self.tipo.data == "comercio":
            if not self.nomefantasia.data:
                self.nomefantasia.errors.append("Nome Fantasia é obrigatório para comércio.")
                return False
            if not self.proprietario.data:
                self.proprietario.errors.append("Proprietário é obrigatório para comércio.")
                return False
            if not self.cnpj.data:
                self.cnpj.errors.append("CNPJ é obrigatório para comércio.")
                return False
        return True

    def save(self):
        if self.tipo.data == "morador":
            senha = self.senha.data
            sobrenome = self.sobrenome.data
            is_comercio = False
        else:
            senha = "123"
            sobrenome = self.proprietario.data
            is_comercio = True

        hashed_senha = bcrypt.generate_password_hash(senha).decode("utf-8")
        user = User(
            nome=self.nome.data,
            sobrenome=sobrenome,
            email=self.email.data,
            senha=hashed_senha,
            saldo=0.0,
            is_comercio=is_comercio
        )
        db.session.add(user)
        db.session.commit()
        return user

# ------------------ FORMULÁRIO DE LOGIN ------------------
class LoginForm(FlaskForm):
    email = StringField("Email:", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha:", validators=[DataRequired()])
    btnSubmit = SubmitField("Login")

    def login(self):
        user = User.query.filter_by(email=self.email.data).first()
        if user and bcrypt.check_password_hash(user.senha, self.senha.data):
            return user
        return None

# ------------------ FORMULÁRIO DE TRANSAÇÃO ------------------
class TransacaoForm(FlaskForm):
    remetente = SelectField("Remetente:", coerce=int, validators=[DataRequired()])
    destinatario = SelectField("Destinatário:", coerce=int, validators=[DataRequired()])
    valor = FloatField("Valor:", validators=[DataRequired(), NumberRange(min=0.01)])
    descricao = StringField("Descrição:", validators=[Length(max=200)])
    btnSubmit = SubmitField("Registrar Transação")

    def set_choices(self):
        """Define as opções do select antes da validação do formulário"""
        usuarios = User.query.all()
        choices = [(u.id, f"{u.nome} {u.sobrenome or ''}") for u in usuarios]
        self.remetente.choices = choices
        self.destinatario.choices = choices

    def save(self):
        """Salva a transação no banco"""
        transacao = Transacao(
            remetente_id=self.remetente.data,
            destinatario_id=self.destinatario.data,
            valor=self.valor.data,
            descricao=self.descricao.data,
            data=datetime.utcnow()
        )
        db.session.add(transacao)
        db.session.commit()
        return transacao

# ------------------ FORMULÁRIO DE CONTATO ------------------
class ContatoForm(FlaskForm):
    nome = StringField("Nome:", validators=[DataRequired(), Length(max=100)])
    email = StringField("Email:", validators=[DataRequired(), Email(), Length(max=100)])
    assunto = StringField("Assunto:", validators=[DataRequired(), Length(max=150)])
    mensagem = StringField("Mensagem:", validators=[DataRequired(), Length(max=500)])
    btnSubmit = SubmitField("Enviar")

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


'''
------------------ IMPORTS ------------------
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional, NumberRange, ValidationError
from app.models import User, Contato, Transacao
from app import db, bcrypt
from datetime import datetime

# ------------------ FORMULÁRIO DE CADASTRO DE USUÁRIO ------------------

class UserForm(FlaskForm):
    # Campo de tipo (morador ou comércio)
    tipo = SelectField(
        "Tipo de cadastro:",
        choices=[("morador", "Morador"), ("comercio", "Comércio")],
        validators=[DataRequired(message="Selecione o tipo de cadastro")]
    )

    # Campos comuns
    nome = StringField("Nome:",
        validators=[DataRequired(message="Digite seu nome"), Length(min=1, max=50)]
    )
    sobrenome = StringField("Sobrenome:",
        validators=[Optional(), Length(max=50)]  # obrigatório só para moradores
    )
    endereco = StringField("Endereço:",
        validators=[DataRequired(message="Digite seu endereço"), Length(min=1, max=100)]
    )
    email = StringField("Email:",
        validators=[DataRequired(message="Digite seu e-mail"), Email(message="Formato de e-mail inválido")]
    )
    senha = PasswordField("Senha:",
        validators=[DataRequired(), Length(min=6, message="A senha deve ter pelo menos 6 caracteres")]  # comércio usa senha padrão
    )
    confirmacao_senha = PasswordField("Confirme a senha:",
        validators=[DataRequired(), EqualTo("senha", message="As senhas não coincidem")]
    )

    # Campos específicos de comércio
    nomefantasia = StringField("Nome Fantasia:",
        validators=[DataRequired(), Length(max=100, message="Máximo de 100 caracteres")]
    )
    cnpj = StringField("CNPJ:",
        validators=[DataRequired(), Length(min=14, max=18, message="Digite um CNPJ válido")]
    )
    proprietario = StringField("Proprietário:",
        validators=[DataRequired(), Length(max=100, message="Máximo de 100 caracteres")]
    )

    # Botão
    btnSubmit = SubmitField("Cadastrar")

    # Validação customizada para email único
    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Já existe um usuário com esse e-mail.")

    # Validação condicional dependendo do tipo
    def validate(self, extra_validators=None):
        # Executa validações padrões primeiro
        rv = super().validate(extra_validators=extra_validators)
        if not rv:
            return False

        # Valida campos obrigatórios conforme tipo
        if self.tipo.data == "morador":
            if not self.sobrenome.data:
                self.sobrenome.errors.append("Sobrenome é obrigatório para moradores.")
                return False
            if not self.senha.data:
                self.senha.errors.append("Senha é obrigatória para moradores.")
                return False
            if not self.confirmacao_senha.data:
                self.confirmacao_senha.errors.append("Confirme sua senha.")
                return False

        elif self.tipo.data == "comercio":
            if not self.nomefantasia.data:
                self.nomefantasia.errors.append("Nome Fantasia é obrigatório para comércio.")
                return False
            if not self.proprietario.data:
                self.proprietario.errors.append("Proprietário é obrigatório para comércio.")
                return False
            if not self.cnpj.data:
                self.cnpj.errors.append("CNPJ é obrigatório para comércio.")
                return False

        return True

    # Salvar usuário com senha hash
    def save(self):
        if self.tipo.data == "morador":
            senha = self.senha.data
            is_comercio = False
            sobrenome = self.sobrenome.data
        else:  # comércio
            senha = "123"
            is_comercio = True
            sobrenome = self.proprietario.data

        hashed_senha = bcrypt.generate_password_hash(senha).decode('utf-8')

        user = User(
            nome=self.nome.data,
            sobrenome=sobrenome,
            email=self.email.data,
            senha=hashed_senha,
            saldo=0.0,
            is_comercio=is_comercio
        )
        db.session.add(user)
        db.session.commit()
        return user

# ------------------ FORMULÁRIO DE LOGIN ------------------
class LoginForm(FlaskForm):
    email = StringField("Email:",
        validators=[DataRequired(message="Digite seu e-mail"), 
            Email(message="Formato de e-mail inválido")]
    )
    senha = PasswordField("Senha:",
        validators=[DataRequired(message="Digite sua senha")]
    )
    btnSubmit = SubmitField("Login")

    # Verifica login
    def login(self):
        user = User.query.filter_by(email=self.email.data).first()
        if user and bcrypt.check_password_hash(user.senha, self.senha.data):
            return user
        return None


# ------------------ FORMULÁRIO DE TRANSAÇÃO ------------------
class TransacaoForm(FlaskForm):
    remetente = SelectField("Remetente:", coerce=int, validators=[DataRequired()])
    destinatario = SelectField("Destinatário:", coerce=int, validators=[DataRequired()])
    valor = FloatField("Valor:", validators=[DataRequired(), NumberRange(min=0.01)])
    descricao = StringField("Descrição:", validators=[Length(max=200)])
    btnSubmit = SubmitField("Registrar Transação")

    def set_choices(self):
        usuarios = User.query.all()
        choices = [(u.id, f"{u.nome} {u.sobrenome or ''}") for u in usuarios]
        self.remetente.choices = choices
        self.destinatario.choices = choices

    def save(self):
        transacao = Transacao(
            remetente_id=self.remetente.data,
            destinatario_id=self.destinatario.data,
            valor=self.valor.data,
            descricao=self.descricao.data
        )
        db.session.add(transacao)
        db.session.commit()
        return transacao

class Transacao(db.Model):
    __tablename__ = 'transacao'
    id = db.Column(db.Integer, primary_key=True)
    remetente_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    destinatario_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(255))
    data = db.Column(db.DateTime, default=datetime.utcnow)

    remetente = db.relationship('User', foreign_keys=[remetente_id])
    destinatario = db.relationship('User', foreign_keys=[destinatario_id])



# ------------------ FORMULÁRIO DE CONTATO ------------------
class ContatoForm(FlaskForm):
    nome = StringField("Nome:",
        validators=[DataRequired(message="Digite seu nome"), Length(max=100)]
    )
    email = StringField("Email:",
        validators=[DataRequired(message="Digite seu e-mail"), Email(message="Formato inválido"), Length(max=100)]
    )
    assunto = StringField("Assunto:",
        validators=[DataRequired(message="Digite o assunto"), Length(max=150)]
    )
    mensagem = StringField("Mensagem:",
        validators=[DataRequired(message="Digite a mensagem"), Length(max=500)]
    )
    btnSubmit = SubmitField("Enviar")

    # Salvar mensagem no banco
    def save(self):
        contato = Contato(
            nome=self.nome.data,
            email=self.email.data,
            assunto=self.assunto.data,
            mensagem=self.mensagem.data,
            data_envio=datetime.utcnow()
        )
        db.session.add(contato)
        db.session.commit()
        return contato
'''
