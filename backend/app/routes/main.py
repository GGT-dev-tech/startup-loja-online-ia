# backend/app/routes/main.py

from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return "API da Loja Online + IA está funcionando! ✅"
