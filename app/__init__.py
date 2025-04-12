from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt



# Criação do aplicativo Flask
app = Flask(__name__)

# Criando e configurando o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '12456389'
db = SQLAlchemy(app)

# Configurando o flask login
#app.secret_key='12456389'
lm = LoginManager()
lm.init_app(app)
lm.login_view ='login'
bcrypt = Bcrypt(app)




# Configurando o Migrate
migrate = Migrate(app, db)

# Importação das rotas sempres posterior a criação do aplicativo 
from app.routes import index
from app.routes import dashboard
from app.routes import cadastro

# importando o banco de Dados
from app.models import Cadastro