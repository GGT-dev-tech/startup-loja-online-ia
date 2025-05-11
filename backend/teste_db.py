import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.db_connection import connect_db

def test_connection():
    try:
        # Obtém a conexão com o banco
        connection = connect_db()
        cursor = connection.cursor()
        print("Conexão com o PostgreSQL bem-sucedida!")

        # Teste: Executar uma query simples
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"Versão do PostgreSQL: {db_version[0]}")

        # Fechar cursor e conexão
        cursor.close()
        connection.close()
        print("Conexão fechada.")

    except Exception as error:
        print(f"Erro ao conectar ao PostgreSQL: {error}")

if __name__ == "__main__":
    test_connection()