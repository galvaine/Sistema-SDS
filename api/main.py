from app import app, db

# Cria as tabelas ao importar (opcional, dependendo do seu fluxo)
with app.app_context():
    db.create_all()

# Vercel precisa encontrar essa variável
app = app