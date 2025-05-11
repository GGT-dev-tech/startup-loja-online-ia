# backend/app/routes/auth.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.controllers.auth_controller import autenticar_usuario

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    senha = data.get('senha')

    if autenticar_usuario(usuario, senha):
        token = create_access_token(identity=usuario)
        return jsonify(access_token=token), 200
    else:
        return jsonify({"erro": "Usuário ou senha inválidos"}), 401
