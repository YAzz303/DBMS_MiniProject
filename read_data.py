# read_data.py
from db import get_db_connection

def read_categories():
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Category"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def read_suppliers():
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Supplier"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def read_products():
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Product"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def read_customers():
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM Customer"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def read_orders():
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM `Order`"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def read_order_items():
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM OrderItem"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def read_stock_transactions():
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM StockTransaction"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows
