from pathlib import Path

from cryptography.fernet import Fernet

SECRET_KEY_PATH = Path(Path(__file__).parent.parent / "config" / "secret_key.key")


def create_key() -> None:
    key = Fernet.generate_key()
    with open(SECRET_KEY_PATH, "wb") as key_file:
        key_file.write(key)


def get_key() -> str:
    with open(SECRET_KEY_PATH, "rb") as key_file:
        key = key_file.read()
    return key


def encrypt(password: str) -> str:
    fernet = Fernet(get_key())
    return fernet.encrypt(password.encode()).decode()


def decrypt(password: str) -> str:
    fernet = Fernet(get_key())
    return fernet.decrypt(password.encode()).decode()


if __name__ == "__main__":
    create_key()
