# backend/app/routes/products.py
from flask import Blueprint, jsonify
from app.controllers.product_controller import listar_produtos
from flask_jwt_extended import jwt_required

products_bp = Blueprint('products', __name__)

@products_bp.route('/', methods=['GET'])
@jwt_required()
def get_produtos():
    return listar_produtos()
