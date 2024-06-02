import tk_insert
import update
import delete
import views
import tkinter as tk
from tkinter import ttk
from db import create_connection


def add_customer():
    add_window = tk.Toplevel()
    add_window.title("Add Customer")
    # Add entry widgets and a submit button
    tk.Label(add_window, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=0, column=1)

    tk.Label(add_window, text="Address:").grid(row=1, column=0)
    address_entry = tk.Entry(add_window)
    address_entry.grid(row=1, column=1)

    tk.Label(add_window, text="Email:").grid(row=2, column=0)
    email_entry = tk.Entry(add_window)
    email_entry.grid(row=2, column=1)

    def submit_customer():
        name = name_entry.get()
        address = address_entry.get()
        email = email_entry.get()
        tk_insert.insert_customer(name, address, email)
        add_window.destroy()

    tk.Button(add_window, text="Submit", command=submit_customer).grid(row=3, column=0, columnspan=2)

def add_supplier():
    add_window = tk.Toplevel()
    add_window.title("Add Supplier")
    # Add entry widgets and a submit button
    tk.Label(add_window, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=0, column=1)

    tk.Label(add_window, text="Address:").grid(row=1, column=0)
    address_entry = tk.Entry(add_window)
    address_entry.grid(row=1, column=1)

    tk.Label(add_window, text="Email:").grid(row=2, column=0)
    email_entry = tk.Entry(add_window)
    email_entry.grid(row=2, column=1)

    def submit_supplier():
        name = name_entry.get()
        address = address_entry.get()
        email = email_entry.get()
        tk_insert.insert_supplier(name, address, email)
        add_window.destroy()

    tk.Button(add_window, text="Submit", command=submit_supplier).grid(row=3, column=0, columnspan=2)

def add_product():
    add_window = tk.Toplevel()
    add_window.title("Add Product")

    tk.Label(add_window, text="Supplier ID:").grid(row=2, column=0)
    supplier_id_entry = tk.Entry(add_window)
    supplier_id_entry.grid(row=2, column=1)

    tk.Label(add_window, text="Name:").grid(row=1, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=1, column=1)

    tk.Label(add_window, text="Category:").grid(row=0, column=0)
    category_entry = tk.Entry(add_window)
    category_entry.grid(row=0, column=1)

    tk.Label(add_window, text="Price:").grid(row=3, column=0)
    price_entry = tk.Entry(add_window)
    price_entry.grid(row=3, column=1)

    tk.Label(add_window, text="In Stock:").grid(row=4, column=0)
    in_stock_entry = tk.Entry(add_window)
    in_stock_entry.grid(row=4, column=1)

    def submit_product():
        category = category_entry.get()
        name = name_entry.get()
        supplier_id = supplier_id_entry.get()
        price = price_entry.get()
        in_stock = in_stock_entry.get()
        insert_product(category, name, supplier_id, price, in_stock)
        add_window.destroy()
    tk.Button(add_window, text="Submit", command=submit_product).grid(row=5, column=0, columnspan=2)

def add_order():
    add_window = tk.Toplevel()
    add_window.title("Add Order")

    tk.Label(add_window, text="Customer ID:").grid(row=0, column=0)
    customer_id_entry = tk.Entry(add_window)
    customer_id_entry.grid(row=0, column=1)

    tk.Label(add_window, text="Product ID:").grid(row=1, column=0)
    product_id_entry = tk.Entry(add_window)
    product_id_entry.grid(row=1, column=1)

    tk.Label(add_window, text="Quantity:").grid(row=2, column=0)
    quantity_entry = tk.Entry(add_window)
    quantity_entry.grid(row=2, column=1)

    tk.Label(add_window, text="Status:").grid(row=3, column=0)
    status_entry = tk.Entry(add_window)
    status_entry.grid(row=3, column=1)

    tk.Label(add_window, text="Shipping Date:").grid(row=4, column=0)
    shipping_date_entry = DateEntry(add_window, date_pattern='y-mm-dd')
    shipping_date_entry.grid(row=4, column=1)

    def submit_order():
        customer_id = customer_id_entry.get()
        product_id = product_id_entry.get()
        quantity = quantity_entry.get()
        status = status_entry.get()
        shipping_date = shipping_date_entry.get()
        insert_order(customer_id, product_id, quantity, status, shipping_date)
        add_window.destroy()

    tk.Button(add_window, text="Submit", command=submit_order).grid(row=5, column=0, columnspan=2)




def update_customer():
    # Function to update a customer
    update_window = tk.Toplevel()
    update_window.title("Update Customer")
    # Add fields and logic to update customer

def delete_customer():
    # Function to delete a customer
    delete_window = tk.Toplevel()
    delete_window.title("Delete Customer")
    # Add fields and logic to delete customer




def main_window():
    root = tk.Tk()
    root.title("Inventory Management System")

    customer_frame = ttk.Frame(root)
    customer_frame.grid(row=0, column=0, padx=10, pady=10)

    # Customer Management
    ttk.Label(customer_frame, text="Customer Management").grid(row=0, column=0, columnspan=2)
    ttk.Button(customer_frame, text="Add Customer", command=add_customer).grid(row=1, column=0)
    ttk.Button(customer_frame, text="View Customers", command=views.view_customers).grid(row=1, column=1)
    ttk.Button(customer_frame, text="Update Customer", command=update_customer).grid(row=2, column=0)
    ttk.Button(customer_frame, text="Delete Customer", command=delete_customer).grid(row=2, column=1)

     #Supplier Management
    supplier_frame = ttk.Frame(root)
    supplier_frame.grid(row=1, column=0, padx=10, pady=10)

    ttk.Label(supplier_frame, text="Supplier Management").grid(row=0, column=0, columnspan=2)
    ttk.Button(supplier_frame, text="Add Supplier", command=add_supplier).grid(row=1, column=0) 
    ttk.Button(supplier_frame, text="View Suppliers", command=views.view_suppliers).grid(row=1, column=1) 
    ttk.Button(supplier_frame, text="Update Supplier", command=None).grid(row=2, column=0) 
    ttk.Button(supplier_frame, text="Delete Supplier", command=None).grid(row=2, column=1) 

    # Product Management
    product_frame = ttk.Frame(root)
    product_frame.grid(row=2, column=0, padx=10, pady=10)

    ttk.Label(product_frame, text="Product Management").grid(row=0, column=0, columnspan=2)
    ttk.Button(product_frame, text="Add Product", command=add_product).grid(row=1, column=0) 
    ttk.Button(product_frame, text="View Products", command=views.view_products).grid(row=1, column=1) 
    ttk.Button(product_frame, text="Update Product", command=None).grid(row=2, column=0) 
    ttk.Button(product_frame, text="Delete Product", command=None).grid(row=2, column=1) 

    # Order Management
    order_frame = ttk.Frame(root)
    order_frame.grid(row=3, column=0, padx=10, pady=10)

    ttk.Label(order_frame, text="Order Management").grid(row=0, column=0, columnspan=2)
    ttk.Button(order_frame, text="Add Order", command=add_order).grid(row=1, column=0) 
    ttk.Button(order_frame, text="View Orders", command=views.view_orders).grid(row=1, column=1) 
    ttk.Button(order_frame, text="Update Order", command=None).grid(row=2, column=0) 
    ttk.Button(order_frame, text="Delete Order", command=None).grid(row=2, column=1) 

    root.mainloop()

if __name__=="__main__":
    main_window()