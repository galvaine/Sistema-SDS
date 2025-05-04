#Importação da construção do aplicativo flask
from app import app
from app import db
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
