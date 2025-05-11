# backend/config.py

import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "chave_super_secreta")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt_super_secreta")
