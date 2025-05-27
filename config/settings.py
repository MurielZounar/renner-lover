import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
ROOT_PATH = Path(__file__).parent.parent
DB_PATH = Path(ROOT_PATH / "data" / "renner_cart.db")
SCHEMA_PATH = Path(ROOT_PATH / "database" / "schema.sql")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
ALLOWED_FIELDS = {
    "id",
    "name",
    "email",
    "psw",
    "user_id",
    "sku",
    "brand",
    "name",
    "variant",
    "current_price",
    "last_price",
    "product_link",
    "product_image",
}
SLEEP_TIME = 10
