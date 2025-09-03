from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import psycopg2



# Criação do aplicativo Flask
app = Flask(__name__)

# Criando e configurando o banco de dados



import tempfile

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:WyOXFVaYNLCf0pXt@db.fsnjmvfbkemdsrxolpgd.supabase.co:5432/postgres'
app.config['SECRET_KEY'] = '12456389'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



# Configurando o flask login
lm = LoginManager()
lm.init_app(app)
lm.login_view ='login'
bcrypt = Bcrypt(app)


# Importação das rotas sempres posterior a criação do aplicativo 
from app.routes import index
from app.routes import dashboard
from app.routes import cadastro
from app.routes import relatorio
from app.routes import permuta
from app.routes import logoff

# importando o banco de Dados
from app.models import Cadastro
