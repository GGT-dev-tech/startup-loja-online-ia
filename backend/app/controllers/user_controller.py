# backend/app/controllers/user_controller.py

from database.db_connection import connect_db
from passlib.hash import pbkdf2_sha256
from flask import jsonify

def listar_usuarios():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT id, nome, usuario, tipo FROM usuarios;")
    usuarios = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(usuarios)

def criar_usuario(data):
    nome = data.get("nome")
    usuario = data.get("usuario")
    senha = data.get("senha")
    tipo = data.get("tipo", "funcionario")  # padrão

    senha_hash = pbkdf2_sha256.hash(senha)

    conn = connect_db()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO usuarios (nome, usuario, senha_hash, tipo) VALUES (%s, %s, %s, %s);",
            (nome, usuario, senha_hash, tipo)
        )
        conn.commit()
        return jsonify({"mensagem": "Usuário criado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    finally:
        cur.close()
        conn.close()
