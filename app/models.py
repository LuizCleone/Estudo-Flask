from app import db, login_manager, bcrypt
from datetime import datetime
from flask_login import UserMixin

# ------------------ FUNÇÃO DE LOGIN ------------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ------------------ USUÁRIO ------------------
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    sobrenome = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    saldo = db.Column(db.Float, default=0.0)
    is_comercio = db.Column(db.Boolean, default=False)

    # Método para criar hash da senha
    def set_senha(self, senha_plain):
        self.senha = bcrypt.generate_password_hash(senha_plain).decode('utf-8')


# ------------------ CONTATO ------------------
class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow)
    nome = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    assunto = db.Column(db.String(150), nullable=True)
    mensagem = db.Column(db.String(500), nullable=True)
    respondido = db.Column(db.Integer, default=0)


# ------------------ TRANSAÇÃO ------------------
class Transacao(db.Model):
    __tablename__ = "transacao"
    id = db.Column(db.Integer, primary_key=True)
    remetente_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    destinatario_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(255))
    data = db.Column(db.DateTime, default=datetime.utcnow)

    remetente = db.relationship("User", foreign_keys=[remetente_id])
    destinatario = db.relationship("User", foreign_keys=[destinatario_id])


'''
from app import db, login_manager, bcrypt
from datetime import datetime
from flask_login import UserMixin

------------------ FUNÇÃO DE LOGIN ------------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


------------------ USUÁRIO ------------------
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    sobrenome = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    saldo = db.Column(db.Float, default=0.0)
    is_comercio = db.Column(db.Boolean, default=False)

Método para criar hash da senha
    def set_senha(self, senha_plain):
        self.senha = bcrypt.generate_password_hash(senha_plain).decode('utf-8')


 ------------------ CONTATO ------------------
class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.utcnow)
    nome = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    assunto = db.Column(db.String(100), nullable=True)
    mensagem = db.Column(db.String(500), nullable=True)
    respondido = db.Column(db.Integer, default=0)


  ------------------ TRANSAÇÃO ------------------
class Transacao(db.Model):
    __tablename__ = "transacao"
    id = db.Column(db.Integer, primary_key=True)
    remetente_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    destinatario_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(200), nullable=True)          novo campo
    data = db.Column(db.DateTime, default=datetime.utcnow)       novo campo
'''