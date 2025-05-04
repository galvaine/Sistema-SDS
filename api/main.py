from api.app import app, db
import os
import sys
sys.path.append('/caminho/para/seu/modulo')

with app.app_context():
    db.create_all()

application = app  # Vercel exige que o app seja chamado 'application'
