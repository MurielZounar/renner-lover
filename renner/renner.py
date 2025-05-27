import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.password import decrypt
from webdriver_manager.chrome import ChromeDriverManager


class Driver:
    def __init__(self, email, psw):
        self._email = email
        self._psw = psw
        self.driver = None
        self.wait = None

    def get_driver(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_experimental_option(
                "excludeSwitches", ["enable-automation"]
            )
            chrome_options.add_experimental_option("useAutomationExtension", False)
            chrome_options.add_argument("--remote-debugging-port=9222")
            chrome_options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            )

            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), options=chrome_options
            )
            self.wait = WebDriverWait(self.driver, timeout=30)
        except Exception as e:
            print(f"Erro ao criar driver: {e}")

    def get_cart_items(self):
        self.get_driver()
        self.renner_home_page()
        self.login()
        cart_loaded = self.open_cart()

        if cart_loaded:
            items_list = []
            ok = False

            self.scroll()

            while not ok:
                item_located = self.wait.until(
                    EC.presence_of_element_located((By.CLASS_NAME, "row_product"))
                )

                if item_located:
                    ok = True

            items = self.driver.find_elements(by=By.CLASS_NAME, value="row_product")

            for item in items:
                try:
                    item_json = item.get_attribute("data-product-ga")
                    item_data = dict()
                    item_data = json.loads(item_json)
                    item_id = item.get_attribute("id")
                    link = self.wait.until(
                        EC.presence_of_element_located(
                            (By.XPATH, f'//*[@id="{item_id}"]/div[1]/a')
                        )
                    )
                    image = self.wait.until(
                        EC.presence_of_element_located(
                            (By.XPATH, f'//*[@id="{item_id}"]/div[1]/a/img')
                        )
                    )
                    item_data["product_link"] = link.get_attribute("href")
                    item_data["product_image"] = image.get_attribute("src")
                    items_list.append(item_data)
                except Exception as e:
                    print(f"Erro: Item ID {item.get_attribute('id')}: {e}")

            self.logout()
            return items_list

    def renner_home_page(self):
        try:
            url = "https://www.lojasrenner.com.br/"
            self.driver.get(url)
        except Exception as e:
            print(f"Houve um erro ao tentar se conectar ao site da Renner: {e}")

    def login(self):
        try:
            user_nav_button = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "user-nav"))
            )
            user_nav_button.click()

            login_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "login"))
            )

            login_field.send_keys(self._email)

            password_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "password"))
            )

            password_field.send_keys(decrypt(self._psw))

            login_button = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="__next"]/div/div[1]/div[1]/div[1]/div/div/main/div/div[1]/div/div/div[2]/button',
                    )
                )
            )

            login_button.click()
        except Exception as e:
            print(f"Houve um erro ao tentar fazer o login: {e}")

    def open_cart(self):
        cart_url = "https://www.lojasrenner.com.br/sacola#"
        try:
            self.driver.get(cart_url)
            loaded = self.wait.until(EC.url_to_be(cart_url))
            return loaded
        except Exception as e:
            print(f"Houve um erro ao abrir o carrinho: {e}")

    def logout(self):
        try:
            self.driver.close()
        except Exception as e:
            print(f"Houve um erro ao tentar fazer o logout: {e}")

    def scroll(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
