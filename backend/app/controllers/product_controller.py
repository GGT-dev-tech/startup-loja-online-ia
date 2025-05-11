# backend/app/controllers/product_controller.py
from database.db_connection import connect_db
from flask import jsonify

def listar_produtos():
    conn = connect_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM produtos;")
            produtos = cur.fetchall()
            cur.close()
            conn.close()
            return jsonify(produtos)
        except Exception as e:
            return jsonify({"erro": str(e)}), 500
    else:
        return jsonify({"erro": "Erro de conexão com o banco"}), 500
