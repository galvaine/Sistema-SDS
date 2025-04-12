from app import db, lm
from flask_login import UserMixin

#função para controle de login
@lm.user_loader
def load_user(user_id):
    return Cadastro.query.get(user_id)

# Modelo para controle de usuario utilizando o userMixin
# para marca para o flask login que e utilizado como dados de login
class Cadastro(db.Model, UserMixin):
# Nome da tabela
    __tablename__ = 'cadastros'
    id = db.Column(db.Integer, primary_key=True)
    # Dados pessoais 
    nome = db.Column(db.String(30), unique=True, nullable=True)
    idade = db.Column(db.Integer)
    sexo = db.column(db.String(10))
    # Dados proficionais
    matricula = db.Column(db.Integer, unique=True, nullable=True)
    classe = db.Column(db.String(15))
    cargo = db.Column(db.String(15))
    # Dados de login
    email = db.Column(db.String,  nullable=True)
    senha = db.Column(db.String, nullable = True)
