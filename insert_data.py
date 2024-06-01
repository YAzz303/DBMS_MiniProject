from db import get_db_connection

def insert_category(name, description):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO Category (name, description) VALUES (%s, %s)"
    cursor.execute(query, (name, description))
    connection.commit()
    cursor.close()
    connection.close()

def insert_supplier(name, city, country, phone, email):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO Supplier (name, city, country, phone, email) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (name, city, country, phone, email))
    connection.commit()
    cursor.close()
    connection.close()

def insert_product(name, category_id, supplier_id, price, quantity_in_stock):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO Product (name, category_id, supplier_id, price, quantity_in_stock) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (name, category_id, supplier_id, price, quantity_in_stock))
    connection.commit()
    cursor.close()
    connection.close()

def insert_customer(name, city, country, email):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO Customer (name, city, country, email) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, city, country, email))
    connection.commit()
    cursor.close()
    connection.close()

def insert_order(customer_id, shipping_date, status, total_amount):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO `Order` (customer_id, shipping_date, status, total_amount) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (customer_id, shipping_date, status, total_amount))
    connection.commit()
    cursor.close()
    connection.close()

def insert_order_item(order_id, product_id, quantity, price):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO OrderItem (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (order_id, product_id, quantity, price))
    connection.commit()
    cursor.close()
    connection.close()

def insert_stock_transaction(product_id, transaction_type, quantity):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "INSERT INTO StockTransaction (product_id, transaction_type, quantity) VALUES (%s, %s, %s)"
    cursor.execute(query, (product_id, transaction_type, quantity))
    connection.commit()
    cursor.close()
    connection.close()
