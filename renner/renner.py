import json
from time import sleep

from config.settings import DRIVER
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def open_renner_website():
    try:
        DRIVER.get("https://www.lojasrenner.com.br/")
    except Exception as e:
        print(f"Houve um erro ao tentar se conectar ao site da Renner: {e}")


def login(email, psw):
    try:
        wait = WebDriverWait(DRIVER, timeout=30)
        user_nav_button = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "user-nav"))
        )
        user_nav_button.click()

        login_field = wait.until(EC.presence_of_element_located((By.NAME, "login")))

        login_field.send_keys(email)

        password_field = wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )

        password_field.send_keys(psw)

        login_button = wait.until(
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


def open_cart():
    cart_url = "https://www.lojasrenner.com.br/sacola#"
    try:
        DRIVER.get(cart_url)
        wait = WebDriverWait(DRIVER, timeout=30)
        loaded = wait.until(EC.url_to_be(cart_url))
        return loaded
    except Exception as e:
        print(f"Houve um erro ao abrir o carrinho: {e}")


def get_cart_items(email, psw):
    open_renner_website()
    login(email, psw)
    cart_loaded = open_cart()

    if cart_loaded:
        items_list = []
        wait = WebDriverWait(DRIVER, timeout=30)
        ok = False

        DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)

        while not ok:
            item_located = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "row_product"))
            )

            if item_located:
                ok = True

        items = DRIVER.find_elements(by=By.CLASS_NAME, value="row_product")

        for item in items:
            try:
                item_json = item.get_attribute("data-product-ga")
                item_data = dict()
                item_data = json.loads(item_json)
                item_id = item.get_attribute("id")
                link = wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, f'//*[@id="{item_id}"]/div[1]/a')
                    )
                )
                image = wait.until(
                    EC.presence_of_element_located(
                        (By.XPATH, f'//*[@id="{item_id}"]/div[1]/a/img')
                    )
                )
                item_data["product_link"] = link.get_attribute("href")
                item_data["product_image"] = image.get_attribute("src")
                items_list.append(item_data)
            except Exception as e:
                print(f"Erro: Item ID {item.get_attribute('id')}: {e}")

        close_driver()
        return items_list


def close_driver():
    DRIVER.close()
