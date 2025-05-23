CREATE TABLE IF NOT EXISTS
    users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(10),
        email VARCHAR(150) UNIQUE,
        psw VARCHAR(50)
    )

     
CREATE TABLE IF NOT EXISTS
   items (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_id INTEGER REFERENCES users(id),
      sku VARCHAR(20) UNIQUE,
      brand VARCHAR(30),
      name VARCHAR(100),
      variant VARCHAR(50),
      current_price DECIMAL,
      last_price DECIMAL,
      product_link VARCHAR(255),
      product_image VARCHAR(255)
   )