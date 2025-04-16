# Importação da construção do aplicativo para o arquivo rota
from app import app
from flask import Flask ,render_template,redirect, url_for
from app.models import Cadastro
from app import db
from app.form import Cadastroform, Loginform, RelatorioForm
from flask_login import login_user,logout_user,current_user

# Paginas Inicial
@app.route('/', methods=['GET','POST'])
def index():
    fomulario_login = Loginform()
    if fomulario_login.validate_on_submit():
        usuario = fomulario_login.login()
        login_user(usuario,remember=True)
        return redirect(url_for('dashboard'))
    
    return render_template('index.html',fomulario_login=fomulario_login)

# Rota para a Dashboard do usuario
@app.route('/dashboard', methods=['GET'])
def dashboard():
    nome = current_user.nome.capitalize()
    email = current_user.email.capitalize()
    matricula = current_user.matricula
    sexo = current_user.sexo.capitalize()
    cargo = current_user.cargo.capitalize()
    classe = current_user.classe[:-1].capitalize() + current_user.classe[-1].upper()
    
    # Verifica se o usuario esta logado
    return render_template('dashboard.html',nome=nome, email=email, matricula=matricula, sexo=sexo, cargo=cargo, classe=classe)

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
        print('deu certo')
    return render_template('relatorio.html', relatorio=relatorio)

# Rota exclusiva para cadastrar o usuario
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    formulario = Cadastroform()
    if formulario.validate_on_submit():
        novo_usuario = formulario.save()
        login_user(novo_usuario, remember=True)
        return redirect (url_for('dashboard'))
    return render_template('cadastro.html',formulario=formulario)
