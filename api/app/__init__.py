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
from api.app.routes import index
from api.app.routes import dashboard
from api.app.routes import cadastro
from api.app.routes import relatorio
from api.app.routes import permuta
from api.app.routes import logoff

# importando o banco de Dados
from api.app.models import Cadastro