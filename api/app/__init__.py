from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
lm = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)

    # Configurações
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:WyOXFVaYNLCf0pXt@db.fsnjmvfbkemdsrxolpgd.supabase.co:5432/postgres'
    app.config['SECRET_KEY'] = '12456389'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicialização dos módulos
    db.init_app(app)
    lm.init_app(app)
    lm.login_view = 'login'
    bcrypt.init_app(app)

    # Importações internas (dentro do contexto da app)
    with app.app_context():
        from app.routes import index, dashboard, cadastro, relatorio, permuta, logoff
        from app.models import Cadastro
        db.create_all()

    return app