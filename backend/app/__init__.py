# backend/app/__init__.py
from flask_jwt_extended import JWTManager
from backend.config import Config
from flask import Flask
from app.routes.auth import auth_bp


def create_app():
    app = Flask(__name__)

    # Registro de rotas
    from app.routes.products import products_bp
    app.register_blueprint(products_bp, url_prefix='/produtos')
    
    

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    jwt = JWTManager(app)

    ...

    

    return app
