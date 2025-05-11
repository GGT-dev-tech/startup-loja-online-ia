# backend/app/routes/users.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.controllers.user_controller import listar_usuarios, criar_usuario

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
@jwt_required()
def get_usuarios():
    return listar_usuarios()

@users_bp.route('/', methods=['POST'])
@jwt_required()
def post_usuario():
    data = request.get_json()
    return criar_usuario(data)
