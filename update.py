from db import create_connection

def update_customer_email(customer_id, new_email):
    connection = create_connection()
    cursor = connection.cursor()
    query = "UPDATE Customer SET email = %s WHERE customer_id = %s"
    cursor.execute(query, (new_email, customer_id))
    connection.commit()
    print("Customer email updated successfully")
    cursor.close()
    connection.close()

def update_product(product_id, new_price, new_category):
    connection = create_connection()
    cursor = connection.cursor()
    query = "UPDATE Product SET price = %s, category=%s WHERE product_id = %s"
    cursor.execute(query, (new_price, new_category, product_id))
    connection.commit()
    print("Product price and category updated successfully")
    cursor.close()
    connection.close()

def update_order_status(order_id, new_status):
    connection = create_connection()
    cursor = connection.cursor()
    query = "UPDATE `Order` SET status = %s WHERE order_id = %s"
    cursor.execute(query, (new_status, order_id))
    connection.commit()
    print("Order status updated successfully")
    cursor.close()
    connection.close()