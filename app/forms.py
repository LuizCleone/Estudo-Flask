from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

from app import db, bcrypt
from app.models import Contato, User

class UserForm(FlaskForm):
    nome = StringField("Nome:", validators=[DataRequired(), Length(min=1, max=50)])
    sobrenome = StringField("Sobrenome:", validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField("Email:", validators=[DataRequired('Por favor, digite seu e-mail'), Email('Formato de e-mail inválido')])
    senha = PasswordField("Senha:", validators=[DataRequired()])
    confirmacao_senha = PasswordField("Confirme a senha:", validators=[DataRequired(), EqualTo("senha")])
    btnSubmit = SubmitField("Cadastrar")

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Usuário já cadastrado com esse Email")
            
        
    def save(self):
        hashed_senha = bcrypt.generate_password_hash(self.senha.data.encode("utf-8"))
        user = User(
            nome = self.nome.data,
            sobrenome = self.sobrenome.data,
            email = self.email.data,
            senha = hashed_senha
        )
        db.session.add(user)
        db.session.commit()
        
        return user
    
class LoginForm(FlaskForm):
    
    email = StringField("Email", validators=[DataRequired('Por favor, digite seu e-mail'), Email('Formato de e-mail inválido')])
    senha = PasswordField("Senha", validators=[DataRequired()])
    btnSubmit = SubmitField("Login")

    def login(self):
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.senha, self.senha.data.encode("utf-8")):
                
                return user
            else:
                raise Exception("Senha incorreta")
        else:
            raise Exception("Usuário não encontrado")
"""     
            else:
                self.senha.errors.append("Senha incorreta")
                return None
        else:
            self.email.errors.append("Usuário não encontrado")
            return None
"""
    

class ContatoForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired(), Length(max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    assunto = StringField("Assunto", validators=[DataRequired(), Length(max=100)])
    mensagem = StringField("Mensagem", validators=[DataRequired(), Length(max=500)])
    btnSubmit = SubmitField("Enviar")

    def save(self):
        contato = Contato(
            nome = self.nome.data,
            email = self.email.data,
            assunto = self.assunto.data,
            mensagem = self.mensagem.data
        )

        db.session.add(contato)
        db.session.commit()












"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from wtforms import PasswordField 
from wtforms.validators import EqualTo, ValidationError

from app import db, bcrypt
from app.models import Contato, User




class UserForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired(), Length(min=1, max=50)])
    sobrenome = StringField("Sobrenome", validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha", validators=[DataRequired()])
    confirmacao_senha = PasswordField("Confirme a senha", validators=[DataRequired(), EqualTo("senha")])
    btnSubmit = SubmitField("Enviar")

    def validate(self, email):
        if User.query.filter_by(email=email.date).first():
            raise ValidationError("Usuário já cadastrado com esse Email")
    
    def save (self):
        hashed_senha = bcrypt.generate_password_hash(self.senha.data.encode("utf-8"))

        user = User (
            nome = self.nome.data,
            sobrenome = self.sobrenome.data,
            email = self.email.data,
            assunto = self.assunto.data,
            senha = hashed_senha
        )

        db.session.add(user)
        db.session.commit()

        return user
    
    class LoginForm(FlaskForm):
        email = StringField("Email", validators=[DataRequired(), Email()])
        senha = PasswordField("Senha", validators=[DataRequired()])
        btnSubmit = SubmitField("Login")

        def login(self):
            user = User.query.filter_by(email=self.email.data).first()
            if user:
                if bcrypt.check_password_hash(user.senha, self.senha.data.encode("utf-8")):
                    return user
                else:
                    raise Exception("Senha incorreta")
            else:
                raise Exception("Usuário não encontrado")


class ContatoForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired(), Length(min=1, max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    assunto = StringField("Assunto", validators=[DataRequired(), Length(min=2, max=100)])
    mensagem = StringField("Mensagem", validators=[DataRequired(), Length(min=4, max=500)])
    btnSubmit = SubmitField("Cadastrar")

    def save(self):
        contato = Contato(
            nome = self.nome.data,
            email = self.email.data,
            assunto = self.assunto.data,
            mensagem = self.mensagem.data
        )

        db.session.add(contato)
        db.session.commit()
"""