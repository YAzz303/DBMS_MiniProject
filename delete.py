from db import create_connection

def delete_customer(customer_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = "DELETE FROM Customer WHERE customer_id = %s"
    cursor.execute(query, (customer_id,))
    connection.commit()
    print("Customer deleted successfully")
    cursor.close()
    connection.close()

def delete_supplier(supplier_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = "DELETE FROM Supplier WHERE supplier_id = %s"
    cursor.execute(query, (supplier_id,))
    connection.commit()
    print("Supplier deleted successfully")
    cursor.close()
    connection.close()

def delete_product(product_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = "DELETE FROM Product WHERE product_id = %s"
    cursor.execute(query, (product_id,))
    connection.commit()
    print("Product deleted successfully")
    cursor.close()
    connection.close()

def delete_order(order_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = "DELETE FROM `Order` WHERE order_id = %s"
    cursor.execute(query, (order_id,))
    connection.commit()
    print("Order deleted successfully")
    cursor.close()
    connection.close()