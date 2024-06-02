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
    else:
        print("Invalid field")
        return
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
    else:
        print("Invalid field")
        return
    cursor.execute(query, (new_value, supplier_id))
    connection.commit()
    print(f"Supplier {field} updated successfully")
    cursor.close()
    connection.close()

def update_order(order_id, field, new_value):
    connection = create_connection()
    cursor = connection.cursor()
    if field == "status":
        if new_value == "shipped":
            query = "UPDATE `Order` SET status=%s WHERE order_id = %s"
            cursor.execute(query, (new_value, order_id))
            # Fetch the product_id and quantity
            order_query = "SELECT product_id, quantity FROM `Order` WHERE order_id = %s"
            cursor.execute(order_query, (order_id,))
            result = cursor.fetchone()
            product_id = result[0]
            quantity = result[1]

            # Decrease the stock by the order quantity
            decrease_stock_query = "UPDATE Product SET in_stock = in_stock - %s WHERE product_id = %s"
            cursor.execute(decrease_stock_query, (quantity, product_id))
        else: 
            query = "UPDATE `Order` SET status=%s WHERE order_id = %s"
            cursor.execute(query, (new_value, order_id))
    elif field == "quantity":
        price_query = "SELECT price FROM Product WHERE product_id IN (SELECT product_id FROM `Order` WHERE order_id = %s)"
        cursor.execute(price_query, (order_id,))
        product_price = cursor.fetchone()[0]
        amount = int(new_value) * int(product_price)        
        query = "UPDATE `Order` SET quantity=%s, amount=%s WHERE order_id=%s"
        cursor.execute(query, (new_value, amount, order_id))
    elif field == "shipping_date":
        query = "UPDATE `Order` SET shipping_date=%s WHERE order_id=%s"
        cursor.execute(query, (new_value, order_id))
    else:
        print("Invalid field")
        return
    connection.commit()
    print(f"Order {field} updated successfully")
    cursor.close()
    connection.close()

def update_product(product_id, field, new_value):
    connection = create_connection()
    cursor = connection.cursor()

    if field == "name":
        query = "UPDATE Product SET name = %s WHERE product_id = %s"
    elif field == "category":
        query = "UPDATE Product SET category = %s WHERE product_id = %s"
    elif field == "price":
        query = "UPDATE Product SET price = %s WHERE product_id = %s"
    elif field == "in_stock":
        query = "UPDATE Product SET in_stock = %s WHERE product_id = %s"
    else:
        print("Invalid field")
        return
    cursor.execute(query, (new_value, product_id))
    connection.commit()
    print(f"Product {field} updated successfully")
    cursor.close()
    connection.close()


