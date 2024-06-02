from db import create_connection

def read_customers(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Customer")
    return cursor.fetchall()

def read_suppliers(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Supplier")
    return cursor.fetchall()

def read_products(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Product")
    return cursor.fetchall()

def read_orders(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `Order`")
    return cursor.fetchall()
