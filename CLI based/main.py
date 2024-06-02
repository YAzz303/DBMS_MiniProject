import insert
from read import read_table
import update
import delete
import tkinter as tk
from tkinter import ttk


def main():
    while True:
        print("\nInventory Management System")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Delete")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            handle_create()
        elif choice == '2':
            handle_read()
        elif choice == '3':
            handle_update()
        elif choice == '4':
            handle_delete()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def handle_create():
    print("\nCreate Menu")
    print("1. Create Customer")
    print("2. Create Supplier")
    print("3. Create Product")
    print("4. Create Order")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter customer name: ")
        address = input("Enter customer address: ")
        email = input("Enter customer email: ")
        insert.insert_customer(name, address, email)
    elif choice == '2':
        name = input("Enter supplier name: ")
        address = input("Enter supplier address: ")
        email = input("Enter supplier email: ")
        insert.insert_supplier(name, address, email)
    elif choice == '3':
        category = input("Enter product category: ")
        name = input("Enter product name: ")
        supplier_id = int(input("Enter supplier ID: "))
        price = int(input("Enter product price: "))
        in_stock = int(input("Enter quantity in stock: "))
        insert.insert_product(category, name, supplier_id, price, in_stock)
    elif choice == '4':
        customer_id = int(input("Enter customer ID: "))
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))
        status = input("Enter order status: ")
        shipping_date = input("Enter shipping date (YYYY-MM-DD HH:MM:SS) or leave empty: ")
        if shipping_date == "":
            shipping_date = None
        print(customer_id, product_id, quantity, status, shipping_date)
        insert.insert_order(customer_id, product_id, quantity, status, shipping_date)
    else:
        print("Invalid choice. Please try again.")

def handle_read():
    print('Tables avalaible: Customer   Supplier   Product   `Order`\n')
    table_name = input('Enter the table name to read from: ')
    read_table(table_name)

def handle_update():
    print("\nUpdate Menu")
    print("1. Update Customer")
    print("2. Update Supplier")
    print("3. Update Product")
    print("4. Update Order")
    
    
    choice = input("Enter your choice: ")

    if choice == '1':
        customer_id = int(input("Enter customer ID: "))
        field = input("Enter field to update (name/address/email): ").lower()
        if field not in ["name", "address", "email"]:
            print("Invalid field")
            return
        new_value = input(f"Enter new {field}: ")
        update.update_customer(customer_id, field, new_value)
    elif choice == '2':
        supplier_id = int(input("Enter supplier ID: "))
        field = input("Enter field to update (name/address/email): ").lower()
        if field not in ["name", "address", "email"]:
            print("Invalid field")
            return
        new_value = input(f"Enter new {field}: ")
        update.update_supplier(supplier_id, field, new_value)
    elif choice == '3':
        product_id = int(input("Enter product ID: "))
        new_price = int(input("Enter new price: "))
        new_category = input("Enter category: ")
        update.update_product(product_id, new_price, new_category)
    elif choice == '4':
        order_id = int(input("Enter order ID: "))
        field = input("Enter field to update (status/quantity): ").lower()
        new_value = input(f"Enter new {field}")
        update.update_order_status(order_id, field, new_value)
    else:
        print("Invalid choice. Please try again.")

def handle_delete():
    print("\nDelete Menu")
    print("1. Delete Customer")
    print("2. Delete Supplier")
    print("3. Delete Product")
    print("4. Delete Order")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        customer_id = int(input("Enter customer ID: "))
        delete.delete_customer(customer_id)
    elif choice == '2':
        supplier_id = int(input("Enter supplier ID: "))
        delete.delete_supplier(supplier_id)
    elif choice == '3':
        product_id = int(input("Enter product ID: "))
        delete.delete_product(product_id)
    elif choice == '4':
        order_id = int(input("Enter order ID: "))
        delete.delete_order(order_id)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
