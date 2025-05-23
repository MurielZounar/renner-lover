import sqlite3

from config.settings import SCHEMA_PATH
from database.connection import db_connect


def start_db():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as file:
        schema_sql = file.read()

    try:
        with db_connect() as conn:
            conn.isolation_level = None
            cursor = conn.cursor()
            cursor.execute("BEGIN")
            cursor.executescript(schema_sql)
            cursor.execute("COMMIT")
    except sqlite3.Error as e:
        if conn:
            cursor.execute("ROLLBACK")
        print(f"Erro ao inicializar o banco de dados: {e}")


if __name__ == "__main__":
    start_db()
