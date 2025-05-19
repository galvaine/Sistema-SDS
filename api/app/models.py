from app import db, lm
from flask_login import UserMixin

#função para controle de login
@lm.user_loader
def load_user(user_id):
    return Cadastro.query.get(user_id)

# Modelo do banco de dados de usuario utilizando o userMixin
# para marca para o flask login que e utilizado como dados de login
class Cadastro(db.Model, UserMixin):
# Nome da tabela
    __tablename__ = 'cadastros'
    id = db.Column(db.Integer, primary_key=True)
    # Dados pessoais 
    nome = db.Column(db.String(30), unique=True, nullable=True)
    idade = db.Column(db.String(20))
    sexo = db.Column(db.String(15), nullable=True)
    # Dados proficionais
    matricula = db.Column(db.Integer, unique=True, nullable=True)
    classe = db.Column(db.String(15))
    cargo = db.Column(db.String(15))
    # Dados de login
    email = db.Column(db.String,  nullable=True, unique=True)
    senha = db.Column(db.LargeBinary, nullable = True)

# Tabela de permuta
class Permuta(db.Model):
    __tablename__ = 'permutas'
    id = db.Column(db.Integer, primary_key=True)
    data_solicitacao = db.Column(db.String(20), nullable=True)
    solicitante = db.Column(db.String(30), nullable=True)
    local_servico = db.Column(db.String(30), nullable=True)
    horario_inicio = db.Column(db.String(20), nullable=True)
    horario_termino = db.Column(db.String(20), nullable=True)
    substituto = db.Column(db.String(30), nullable=True)
    altorizacao = db.Column(db.Integer, default=0)
    
