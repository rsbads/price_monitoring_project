import sqlite3


def create_table():
    conn = sqlite3.connect('price_monitoring.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        Product_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Product_name TEXT NOT NULL,
        Product_type TEXT NOT NULL,
        Price REAL,
        URL TEXT                                 
    )
    """)
    conn.commit()
    conn.close()



def create_compras_table():
    conn = sqlite3.connect('price_monitoring.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABEL IF NOT EXISTS purchase (
        Purchase_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Product_ID INTEGER NOT NULL,
        Purchase_date TEXT NOT NULL,
        Purchase_price) REAL NOT NULL,
        FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID)
""")
    conn.commit()
    conn.close()



def create_favorite_table():
    conn = sqlite3.connect('price_monitoring.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABEL IF NOT EXISTS favorites(
    Favorite_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Product_ID INTEGER NOT NULL
    Favorite_data TEXT NOT NULL
    FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID))
""")
    conn.commit()
    conn.close()



def insert_row(product_name, product_type, price, url):
    conn = sqlite3.connect('price_monitoring.db')
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO Products (Product_name, Product_type, Price, URL)
    VALUES (?, ?, ?, ?)
    """, (product_name, product_type, price, url))
    conn.commit()
    conn.close()



def insert_purchase(product_id, purchase_date, purchase_price):
    conn = sqlite3.connect('price_monitoring.db')
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO purchases (Product_ID, Purchase_date, Purchase_price)
    VALUES (?, ?, ?)
""",(product_id, purchase_date, purchase_date))
    conn.commit()
    conn.close()



def insert_favorite(product_id, favorite_date):
    conn = sqlite3.connect('price_monitoring.db')
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO favorites(Product_ID, Favorite_date)
        VALUES (?, ?)
""", (product_id, favorite_date))
    conn.commit()
    conn.close()



def update_row(product_id, product_name, product_type, price, url):
    conn = sqlite3.connect('price_monitoring.db')
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE Products SET Product_name = ?, Product_type = ?, Price = ?, URL = ?
    WHERE Product_ID = ?
    """, (product_name, product_type, price, url, product_id))
    conn.commit()
    conn.close()



def delete_row(product_id):
    conn = sqlite3.connect('price_monitoring.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Products WHERE Product_ID = ?", (product_id,))
    conn.commit()
    conn.close()



def get_all_products():
    conn = sqlite3.connect('price_monitoring.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    records = cursor.fetchall()
    conn.close()
    return records
