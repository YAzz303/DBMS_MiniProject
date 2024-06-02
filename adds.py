import tk_insert
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
        tk_insert.insert_product(category, name, supplier_id, price, in_stock)
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
    shipping_date_entry = tk.Entry(add_window)
    shipping_date_entry.grid(row=4, column=1)

    def submit_order():
        customer_id = customer_id_entry.get()
        product_id = product_id_entry.get()
        quantity = quantity_entry.get()
        status = status_entry.get()
        shipping_date = shipping_date_entry.get()
        tk_insert.insert_order(customer_id, product_id, quantity, status, shipping_date)
        add_window.destroy()

    tk.Button(add_window, text="Submit", command=submit_order).grid(row=5, column=0, columnspan=2)