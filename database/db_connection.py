# database/db_connection.py

import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

def connect_db():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT", 5432),
            cursor_factory=RealDictCursor
        )
        print("✅ Conectado ao banco de dados com sucesso.")
        return conn
    except Exception as e:
        print("❌ Erro na conexão com o banco:", e)
        return None
