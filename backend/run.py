import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# backend/run.py
from flask import Flask
from app import create_app

# Criação da aplicação usando a função modular
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
