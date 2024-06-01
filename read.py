from db import create_connection

def read_table(table_name):
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    result = cursor.fetchall()

    widths = {
        'Customer': [12, 15, 20, 25, 25, 25],
        'Supplier': [12, 15, 20, 25],
        'Product': [12, 15, 15, 12, 10, 10],
        '`Order`': [12, 12, 12, 25, 25, 10, 15, 10]
    }
    
    # Define table headings
    headings = {
        'Customer': ["customer_id", "name", "address", "email", "created_at", "updated_at"],
        'Supplier': ["supplier_id", "name", "address", "email"],
        'Product': ["product_id", "supplier_id", "name", "category", "price", "in_stock"],
        '`Order`': ["order_id", "customer_id", "product_id", "quantity", "amount", "status", "created_at", "updated_at", "shipping_date"]
    }

    # Print table headings
    for heading, width in zip(headings[table_name], widths[table_name]):
        print(heading.ljust(width), end=' ')
    print()
    
    # Print rows of the table
    for row in result:
        for item, width in zip(row, widths[table_name]):
            print(str(item).ljust(width), end=' ')
        print()

    cursor.close()
    connection.close()