from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt



# Criação do aplicativo Flask
app = Flask(__name__)

# Criando e configurando o banco de dados
import os

basedir = os.path.abspath(os.path.dirname(__file__))
import tempfile

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(tempfile.gettempdir(), 'app.db')
app.config['SECRET_KEY'] = '12456389'
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
from api.app.models import Cadastro

# importando o banco de Dados
from api.app.models import Cadastro
