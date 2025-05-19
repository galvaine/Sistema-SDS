from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField,PasswordField,DateField,TextAreaField,TimeField
from wtforms.validators import DataRequired, Email,EqualTo,ValidationError
from flask_login import current_user

from app  import db, bcrypt
from app.models import Cadastro, Permuta

#  Formulario de cadastro
class Cadastroform(FlaskForm):
    # Dados pessoais 
    nome = StringField('Nome',validators=[DataRequired()])
    idade = DateField('Idade',validators=[DataRequired()])
    sexo = SelectField('Sexo',choices=[('masculino', 'Masculino'),('feminino', 'Feminino')],validators=[DataRequired()])
    # Dados proficionais
    matricula = IntegerField('Matricula',validators=[DataRequired()])
    classe = SelectField('Classe',choices=[
        ('classe III','Classe III'),
        ('classe II','Classe II'),
        ('classe I', 'Classe I')],validators=[DataRequired()])
    cargo = SelectField('Cargo',choices=[('guarda', 'Guarda'),('comandante','Comandante'),('subcomandante', 'Subcomandante')],validators=[DataRequired()])
    # Dados de login
    email = StringField('Email',validators=[DataRequired(),Email()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha')])
    # Botão para Cadastrar
    btnSubmit = SubmitField('Cadastrar')
    
    # Função para validar o email com unico
    #def validate_email(self, email):
    #    if Cadastro.query.filter(email=email.data).first():
    #        raise ValidationError('Usuario cadastrado')
        
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

# Formulario de Relatorio
class RelatorioForm(FlaskForm):
    data = DateField('Data', validators=[DataRequired()])
    comandante = StringField('Comandante', validators=[DataRequired()])
    motorista = StringField('Motorista', validators=[DataRequired()])
    patrulheiro = StringField('Patrulheiro')
    local = StringField('Local', validators=[DataRequired()])
    inspetor = StringField('Inspetor', validators=[DataRequired()])
    relatorio = TextAreaField('Relatorio', validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

# Formulario de Permuta
class PermutaForm(FlaskForm):
    data_solicitacao = DateField('Data da Solicitação',validators=[DataRequired()])
    solicitante = StringField('Solicitante', default= lambda: current_user.nome, validators=[DataRequired()])
    local_servico = StringField('Local de Serviço', validators=[DataRequired()])
    horario_inicio = TimeField('Data e Hora de Inicio', validators=[DataRequired()])
    horario_termino = TimeField('Data e Hora de Termino', validators=[DataRequired()])
    substituto = StringField('Subistituto',validators=[DataRequired()])
    btnSubmit = SubmitField('Enviar')

    def save(self):
        formata_data = str(self.data_solicitacao.data.strftime('%d/%m/%Y'))
        formata_horario_inicio = str(self.horario_inicio.data.strftime('%H:%M'))
        formata_horario_termino = str(self.horario_termino.data.strftime('%H:%M'))
        nova_permuta = Permuta(
            data_solicitacao = formata_data,
            solicitante = self.solicitante.data,
            local_servico = self.local_servico.data,
            horario_inicio = formata_horario_inicio,
            horario_termino = formata_horario_termino,
            substituto = self.substituto.data
        )
        db.session.add(nova_permuta)
        db.session.commit()
        return 'ok'