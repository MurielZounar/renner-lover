import logging
from time import sleep

from items.item import (
    delete_item,
    get_item_prices,
    get_user_items,
    item_exists,
    save_item,
    update_item_price,
)
from renner.renner import get_cart_items
from users.users import get_users
from utils.email import notify_user

logging.basicConfig(
    filename="renner_cart.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def cheaper_item(item, last_price, current_price, cheaper_items):
    logging.info("***** Redução de preço encontrada! *****")
    logging.info(
        f" - Produto: {item['name']}\n - Preço anterior: R${last_price}\n - Novo preço: R${current_price}"
    )

    cheaper_item = dict()
    cheaper_item["name"] = item["name"]
    cheaper_item["variant"] = item["variant"]
    cheaper_item["product_link"] = item["product_link"]
    cheaper_item["product_image"] = item["product_image"]
    cheaper_item["last_price"] = last_price
    cheaper_item["current_price"] = current_price
    cheaper_items.append(cheaper_item)


def check_item(item, user, cheaper_items):
    if not item_exists(item["id"]):
        save_item(item, user["id"])
    else:
        db_prices = get_item_prices(item["id"])

        if db_prices:
            if float(item["price"]) < db_prices["current_price"] > 0:
                last_price = db_prices["current_price"]
                current_price = item["price"]
                update_item_price(item["id"], current_price)
                cheaper_item(item, last_price, current_price, cheaper_items)


def delete_items(cart_items, user_id):
    db_items = get_user_items(user_id)

    if db_items:
        for db_item in db_items:
            exist = False

            for cart_item in cart_items:
                if cart_item["sku"] == db_item["sku"]:
                    exist = True
                    break

            if not exist:
                logging.info(
                    f"Excluindo produto ID: {db_item["sku"]} do BD, pois não está presente no carrinho"
                )
                delete_item(db_item["sku"])


def main():
    while True:
        users = get_users()

        if users:
            for user in users:
                cheaper_items = []
                print(f"Verificando carrinho do usuário {user['name']}...")

                renner_items = get_cart_items(user["email"], user["psw"])

                if renner_items:
                    for item in renner_items:
                        check_item(item, user, cheaper_items)

                    delete_items(renner_items, user["id"])

                if cheaper_items:
                    notify_user(cheaper_items, user["email"])
                else:
                    print("Nenhum desconto encontrado!")

                print("Fim da análise.")
                print("*" * 100)
        sleep(3600)


if __name__ == "__main__":
    main()
