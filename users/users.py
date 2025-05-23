from config.settings import ALLOWED_FIELDS
from database.queries import db_execute, db_get_many, db_get_one


def get_users():
    return db_get_many("SELECT id, name, email, psw FROM users")


def save_user(name, email, psw):
    insert_string = "INSERT INTO users (name, email, psw) VALUES (?, ?, ?)"
    data = (
        name,
        email,
        psw,
    )
    db_execute(insert_string, data)


def user_exists(email):
    exist = False
    user = db_get_one("SELECT id, email FROM users WHERE email = ?", (email,))

    if user:
        exist = True

    return exist


def new_id(self, ref):
    last_id = 0
    users = ref.get()
    if users:
        for user in users:
            last_id += 1

    if last_id == 0:
        last_id = 1
    return last_id


def update_user(email, field, value):
    if field not in ALLOWED_FIELDS:
        raise ValueError("Campo não permitido.")

    update_string = f"UPDATE users SET {field} = ? WHERE email = ?"
    data = (
        value,
        email,
    )
    db_execute(update_string, data)


def delete_user(id):
    db_execute("DELETE FROM users WHERE id = ?", (id,))


def get_user(email):
    user = db_get_one("SELECT id, name, email FROM users WHERE email = ?", (email,))

    if user:
        return user
