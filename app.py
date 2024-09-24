from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

app = Flask(__name__)

# Configurações do banco de dados PostgreSQL a partir do .env
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o banco de dados
db = SQLAlchemy(app)

# Importa os models
from models import *  

if __name__ == '__main__':
    app.run(debug=True)

