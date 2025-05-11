# backend/app/controllers/auth_controller.py

from database.db_connection import connect_db
from passlib.hash import pbkdf2_sha256

def autenticar_usuario(usuario, senha):
    conn = connect_db()
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT senha_hash FROM usuarios WHERE usuario = %s", (usuario,))
        resultado = cur.fetchone()
        cur.close()
        conn.close()

        if resultado:
            return pbkdf2_sha256.verify(senha, resultado['senha_hash'])
    return False
