from database.queries import db_execute, db_get_many, db_get_one


def item_exists(sku):
    exist = False
    item = db_get_one("SELECT id FROM items WHERE sku=?", (sku,))

    if item:
        exist = True

    return exist


def save_item(item, user_id):
    insert_string = "INSERT INTO items (user_id, sku, brand, name, variant, current_price, last_price, product_link, product_image) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    data = (
        user_id,
        item["id"],
        item["brand"],
        item["name"],
        item["variant"],
        item["price"],
        item["price"],
        item["product_link"],
        item["product_image"],
    )
    db_execute(insert_string, data)


def update_item_price(sku, price):
    update_string = "UPDATE items SET current_price=?, last_price=? WHERE sku=?"
    data = (
        price,
        price,
        sku,
    )
    db_execute(update_string, data)


def delete_item(sku):
    delete_string = "DELETE FROM items WHERE sku = ?"
    data = (sku,)
    db_execute(delete_string, data)


def get_item_prices(sku):
    item = db_get_one("SELECT current_price, last_price FROM items WHERE sku=?", (sku,))

    if item:
        prices = dict()
        prices["current_price"] = item["current_price"]
        prices["last_price"] = item["last_price"]
        return prices


def get_user_items(user_id):
    items = db_get_many("SELECT sku FROM items WHERE user_id=?", (user_id,))

    if items:
        return items
