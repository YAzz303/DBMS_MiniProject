# main.py
from insert_data import *
from read_data import *

def print_rows(rows):
    for row in rows:
        print(row)

def main():
    while True:
        print("\nInventory Management System")
        print("1. Insert Category")
        print("2. Insert Supplier")
        print("3. Insert Product")
        print("4. Insert Customer")
        print("5. Insert Order")
        print("6. Insert Order Item")
        print("7. Insert Stock Transaction")
        print("8. Read Categories")
        print("9. Read Suppliers")
        print("10. Read Products")
        print("11. Read Customers")
        print("12. Read Orders")
        print("13. Read Order Items")
        print("14. Read Stock Transactions")
        print("15. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter category name: ")
            description = input("Enter category description: ")
            insert_category(name, description)
        elif choice == '2':
            name = input("Enter supplier name: ")
            city = input("Enter city: ")
            country = input("Enter country: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            insert_supplier(name, city, country, phone, email)
        elif choice == '3':
            name = input("Enter product name: ")
            category_id = int(input("Enter category ID: "))
            supplier_id = int(input("Enter supplier ID: "))
            price = float(input("Enter price: "))
            quantity_in_stock = int(input("Enter quantity in stock: "))
            insert_product(name, category_id, supplier_id, price, quantity_in_stock)
        elif choice == '4':
            name = input("Enter customer name: ")
            city = input("Enter city: ")
            country = input("Enter country: ")
            email = input("Enter email: ")
            insert_customer(name, city, country, email)
        elif choice == '5':
            customer_id = int(input("Enter customer ID: "))
            shipping_date = input("Enter shipping date (YYYY-MM-DD HH:MM:SS): ")
            status = input("Enter status: ")
            total_amount = float(input("Enter total amount: "))
            insert_order(customer_id, shipping_date, status, total_amount)
        elif choice == '6':
            order_id = int(input("Enter order ID: "))
            product_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            insert_order_item(order_id, product_id, quantity, price)
        elif choice == '7':
            product_id = int(input("Enter product ID: "))
            transaction_type = input("Enter transaction type (in/out): ")
            quantity = int(input("Enter quantity: "))
            insert_stock_transaction(product_id, transaction_type, quantity)
        elif choice == '8':
            rows = read_categories()
            print_rows(rows)
        elif choice == '9':
            rows = read_suppliers()
            print_rows(rows)
        elif choice == '10':
            rows = read_products()
            print_rows(rows)
        elif choice == '11':
            rows = read_customers()
            print_rows(rows)
        elif choice == '12':
            rows = read_orders()
            print_rows(rows)
        elif choice == '13':
            rows = read_order_items()
            print_rows(rows)
        elif choice == '14':
            rows = read_stock_transactions()
            print_rows(rows)
        elif choice == '15':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
