import os
import sqlite3

from config.settings import DB_PATH


def db_connect():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Houve um erro ao se conectar com o BD: {e}")
