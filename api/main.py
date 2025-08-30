import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))


from app import app, db

# Cria o banco de dados ao iniciar (executado uma vez)
with app.app_context():
    db.create_all()

# Função que o Vercel espera
def handler(request):
    return app(request.environ, lambda status, headers: (status, headers))


