from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os

# ===== Carrega variáveis do .env =====
load_dotenv(".env")

# ===== Inicializa app =====
app = Flask(__name__)

# ===== Configurações =====
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI", "sqlite:///database.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "chave_secreta_padrao")

# ===== Extensões =====
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"  # ajustar para o endpoint correto de login
login_manager.login_message_category = "info"

# ===== Importa modelos =====
from app.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ===== Importa rotas =====
from app import routes

# ===== Rodar servidor =====
if __name__ == "__main__":
    app.run(debug=True)
