from app import app, db

with app.app_context():
    db.create_all()

application = app  # Vercel exige que o app seja chamado 'application'
