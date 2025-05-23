import os
from pathlib import Path

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
DRIVER = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)
