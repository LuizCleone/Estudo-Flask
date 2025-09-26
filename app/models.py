from app import db
from datetime import datetime
from app import login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=True)
    sobrenome = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    senha = db.Column(db.String, nullable=True)

class Contato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_envio = db.Column(db.DateTime, default=datetime.now())
    nome = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=True)
    assunto = db.Column(db.String, nullable=True)
    mensagem = db.Column(db.String, nullable=True)
    respondido = db.Column(db.Integer, default=0)




'''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# modelo do usuário
class Usuario(BaseModel):
    id: int
    nome: str
    email: str

# simulando um "banco de dados"
usuarios = []

# criar usuário (CREATE)
@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    for u in usuarios:
        if u.id == usuario.id:
            raise HTTPException(status_code=400, detail="ID já existe")
    usuarios.append(usuario)
    return {"mensagem": "Usuário criado com sucesso"}

# listar todos os usuários (READ)
@app.get("/usuarios")
def listar_usuarios():
    return usuarios

# buscar usuário por ID (READ)
@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int):
    for u in usuarios:
        if u.id == usuario_id:
            return u
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# atualizar usuário (UPDATE)
@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: int, dados: Usuario):
    for i in range(len(usuarios)):
        if usuarios[i].id == usuario_id:
            usuarios[i] = dados
            return {"mensagem": "Usuário atualizado"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

# deletar usuário (DELETE)
@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    for u in usuarios:
        if u.id == usuario_id:
            usuarios.remove(u)
            return {"mensagem": "Usuário removido"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
'''