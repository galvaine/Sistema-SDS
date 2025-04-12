from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField,PasswordField,DateField
from wtforms.validators import DataRequired, Email,EqualTo,ValidationError

from app  import db, bcrypt
from app.models import Cadastro

#  Formulario de cadastro
class Cadastroform(FlaskForm):
    # Dados pessoais 
    nome = StringField('Nome',validators=[DataRequired()])
    idade = DateField('Idade',validators=[DataRequired()])
    sexo = SelectField('Sexo',choices=[('masculino', 'Masculino'),('feminino', 'Feminino')],validators=[DataRequired()])
    # Dados proficionais
    matricula = IntegerField('Matricula',validators=[DataRequired()])
    classe = SelectField('Classe',choices=[('classe I','Classe III'),('classe II','Classe II'),('classe I', 'Classe I')],validators=[DataRequired()])
    cargo = SelectField('Cargo',choices=[('guarda', 'Guarda'),('comandante','Comandante'),('subcomandante', 'Subcomandante')],validators=[DataRequired()])
    # Dados de login
    email = StringField('Email',validators=[DataRequired(),Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha')])
    # Botão para Cadastrar
    btnSubmit = SubmitField('Cadastrar')
    
    # Função para validar o email com unico
    def validade_email(self, email):
        if Cadastro.query.filter(email=email.data).first():
            return ValidationError('Usuario cadastrado')
        
    def save(self):
        senha = bcrypt.generate_password_hash(self.senha.data.encode('utf-8'))
        novo_usuario = Cadastro(
            nome = self.nome.data,
            idade = self.idade.data,
            sexo = self.sexo.data,
            matricula = self.matricula.data,
            classe = self.classe.data,
            cargo = self.cargo.data,
            email = self.email.data,
            senha = senha 
        )
        db.session.add(novo_usuario)
        db.session.commit()
        return novo_usuario
    
# Formulario de login
class Loginform(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    btnSubimit = SubmitField('Login')
# Função que realiza a busca do email e senha no banco de dados para fazer o login
    def login(self):
        # Recuperar o usuario do email do banco de dados
        user = Cadastro.query.filter_by(email=self.email.data).first()
        # verificando senha e valida
        if user:
            # Descripitografia da senha usando o Bcrypt utilizando sistema do utf-8 para isso
            if bcrypt.check_password_hash(user.senha, self.senha.data.encode('utf-8')):
                # Retornando o Usuário logado 
                return user
            else:
                raise Exception('Senha incorreta!!!')
        else:
            raise Exception('Usuário não encontrado!!!')

# Formulario de Relatorio
#class RelatorioForm(FlaskForm):
#    data = DateField('Data', validators=[DataRequired()])
    