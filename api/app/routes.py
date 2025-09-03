# Importação da construção do aplicativo para o arquivo rota
from api.app import app
from flask import Flask ,render_template,redirect, url_for,request
from api.app.models import Cadastro, Permuta
from api.app import db
from api.app.form import Cadastroform, Loginform, RelatorioForm, PermutaForm
from flask_login import login_user,logout_user,current_user
from datetime import datetime

# Paginas Inicial
@app.route('/', methods=['GET','POST'])
def index():
    fomulario_login = Loginform()
    if fomulario_login.validate_on_submit():
        usuario = fomulario_login.login()
        login_user(usuario,remember=True)
        return redirect(url_for('dashboard'))
    else:   
        return render_template('index.html',fomulario_login=fomulario_login)

# Rota para a Dashboard do usuario
@app.route('/dashboard', methods=['GET'])
def dashboard():
    nome = current_user.nome.capitalize()
    
    mensagem = "teste de mensagem"

    # Verifica se o usuario esta logado
    return render_template('dashboard.html',nome=nome, mensagem=mensagem)

# Rota para sair 
@app.route('/logoff')
def logoff():
    # Função destinada a realiza a saida do usuario
    logout_user()
    return redirect(url_for('index'))

# pagina destinado ao relatorio
@app.route('/relatorio', methods=['GET', 'POST'])
def relatorio():
    relatorio = RelatorioForm()
    if relatorio.validate_on_submit():
        pass
    return render_template('relatorio.html', relatorio=relatorio)

# Rota para a pagina e cadastro de permutas
@app.route('/permuta', methods = ['GET', 'POST'])
def permuta():
    # Pega os dados do formulario de permuta
    formulario_permuta = PermutaForm()
    print(formulario_permuta.data_solicitacao.data)
    print(formulario_permuta.solicitante.data)
    # Verifica se os Dados do formualrio foram validados
    if request.method == 'POST' and formulario_permuta.validate_on_submit():
        nova_permuta = formulario_permuta.save()
        return redirect(url_for('dashboard'))
    if formulario_permuta.errors:
        return "Erro a cadastrar a permuta"

    return render_template('permuta.html', formulario_permuta=formulario_permuta)
    
    

# Rota exclusiva para cadastrar o usuario
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    formulario = Cadastroform()
    if request.method == 'POST' and formulario.validate_on_submit():
        novo_usuario = formulario.save()
        login_user(novo_usuario, remember=True)
        return redirect (url_for('dashboard'))
    return render_template('cadastro.html',formulario=formulario)

# Rota para o historico de permutas
@app.route('/historicopermuta', methods=['GET'])
def historico_permuta():
    # Pega o usuario logado
    current_user_nome = current_user.nome
    # Realiza a busca no banco de dados das permutas do usuario logado
    historico_nome = Permuta.query.filter_by(solicitante=current_user_nome).first()
    # Verifica se o usuario ja fez alguma permuta
    if historico_nome and historico_nome.substituto:
        # Se ja fez permuta traz todo o historico
        historico = Permuta.query.all()
    else:
        # Se nao fez permuta traz o valor 0
        historico = 0
    return render_template('historico_permuta.html', historico=historico)
