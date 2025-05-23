import sqlite3

from database.connection import db_connect


def db_get_one(query: str, data=()):
    with db_connect() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query, data)
            result = cursor.fetchone()
            return result
        except sqlite3.Error as e:
            print(f"Houve um erro ao executar a consulta: {e}")


def db_get_many(query: str, data=()):
    with db_connect() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(query, data)
            result = cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print(f"Houve um erro ao executar a consulta: {e}")


def db_execute(operation_string: str, data=()):
    with db_connect() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(operation_string, data)
            conn.commit()
        except sqlite3.Error as e:
            if conn:
                conn.rollback()
            print(f"Houve um erro ao inserir os dados: {e}")
