from db import create_connection    

def insert_customer(name, address, email):
    connection = create_connection()
    cursor = connection.cursor()
    query = "INSERT INTO Customer (name, address, email) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, address, email))
    connection.commit()
    print("Customer inserted successfully")
    cursor.close()
    connection.close()

def insert_supplier(name, address, email):
    connection = create_connection()
    cursor = connection.cursor()
    query = "INSERT INTO Supplier (name, address, email) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, address, email))
    connection.commit()
    print("Supplier inserted successfully")
    cursor.close()
    connection.close()

def insert_product(category, name, supplier_id, price, in_stock):
    connection = create_connection()
    cursor = connection.cursor()
    query = "INSERT INTO Product (category, name, supplier_id, price, in_stock) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (category, name, supplier_id, price, in_stock))
    connection.commit()
    print("Product inserted successfully")
    cursor.close()
    connection.close()

def insert_order(customer_id, product_id, quantity, status, shipping_date):
    connection = create_connection()
    cursor = connection.cursor()

    price_query = "SELECT price FROM Product WHERE product_id = %s"
    cursor.execute(price_query, (product_id,))
    product_price = cursor.fetchone()[0]
    amount = int(quantity) * int(product_price)

    query = "INSERT INTO `Order` (customer_id, product_id, quantity, status, amount, shipping_date) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (customer_id, product_id, quantity, status, amount, shipping_date))
    connection.commit()
    print("Order inserted successfully")
    cursor.close()
    connection.close()