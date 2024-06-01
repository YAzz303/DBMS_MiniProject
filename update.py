from db import create_connection

def update_customer(customer_id, field, new_value):
    connection = create_connection()
    cursor = connection.cursor()

    if field == "name":
        query = "UPDATE Customer SET name = %s WHERE customer_id = %s"
    elif field == "address":
        query = "UPDATE Customer SET address = %s WHERE customer_id = %s"
    elif field == "email":
        query = "UPDATE Customer SET email = %s WHERE customer_id = %s"

    cursor.execute(query, (new_value, customer_id))
    connection.commit()
    print(f"Customer {field} updated successfully")
    cursor.close()
    connection.close()

def update_supplier(supplier_id, field, new_value):
    connection = create_connection()
    cursor = connection.cursor()
    if field == "name":
        query = "UPDATE Supplier SET name = %s WHERE supplier_id = %s"
    elif field == "address":
        query = "UPDATE Supplier SET address = %s WHERE supplier_id = %s"
    elif field == "email":
        query = "UPDATE Supplier SET email = %s WHERE supplier_id = %s"
    cursor.execute(query, (new_value, supplier_id))
    connection.commit()
    print(f"Supplier {field} updated successfully")
    cursor.close()
    connection.close()

def update_order_status(order_id, field, new_value):
    connection = create_connection()
    cursor = connection.cursor()
    if field == "status":
        if new_value == "shipped":
            query = "UPDATE `Order` SET status=%s WHERE order_id = %s"
            cursor.execute(query, (new_value, order_id))
            # Fetch the product_id
            product_id_query = "SELECT product_id FROM `Order` WHERE order_id = %s"
            cursor.execute(product_id_query, (order_id,))
            product_id = cursor.fetchone()[0]

            # Decrease the stock by one
            decrease_stock_query = "UPDATE Product SET stock = stock - 1 WHERE product_id = %s"
            cursor.execute(decrease_stock_query, (product_id,))
        else: 
            query = "UPDATE `Order` SET status=%s WHERE order_id = %s"
            cursor.execute(query, (new_value, order_id))
    elif field == "quantity":
        price_query = "SELECT price FROM Product WHERE product_id IN (SELECT product_id FROM `Order` WHERE order_id = %s)"
        cursor.execute(price_query, (order_id,))
        product_price = cursor.fetchone()[0]
        amount = new_value * product_price        

        query = "UPDATE `Order` SET quantity=%s, amount=%s WHERE order_id=%s"
        cursor.execute(query, (new_value, amount, order_id))

    connection.commit()
    print(f"Order {field} updated successfully")
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

