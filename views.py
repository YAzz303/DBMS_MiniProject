import tk_read
import tkinter as tk
from tkinter import ttk
from db import create_connection

def view_customers():
    view_window = tk.Toplevel()
    view_window.title("View Customers")

    columns = ("ID", "Name", "Address", "Email", "Created At", "Updated At")
    tree = ttk.Treeview(view_window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)  # Set the column width to ensure all columns are visible
    tree.pack(fill=tk.BOTH, expand=True)
    connection = create_connection()
    customers = tk_read.read_customers(connection)
    connection.close()
    for customer in customers:
        tree.insert("", tk.END, values=customer)

def view_suppliers():
    view_window = tk.Toplevel()
    view_window.title("View Suppliers")

    columns = ("ID", "Name", "Address", "Email", "Created At", "Updated At")
    tree = ttk.Treeview(view_window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)  # Set the column width to ensure all columns are visible
    tree.pack(fill=tk.BOTH, expand=True)
    connection = create_connection()
    suppliers = tk_read.read_suppliers(connection)
    connection.close()

    for supplier in suppliers:
        tree.insert("", tk.END, values=supplier)


def view_products():
    view_window = tk.Toplevel()
    view_window.title("View Products")

    columns = ("Product ID", "Supplier ID", "Name", "Category", "Price", "In Stock", "Created At", "Updated At")
    tree = ttk.Treeview(view_window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)  # Set the column width to ensure all columns are visible
    tree.pack(fill=tk.BOTH, expand=True)
    connection = create_connection()
    products = tk_read.read_products(connection)
    connection.close()

    for product in products:
        # print(product)  # Debug print to ensure the data includes all columns
        tree.insert("", tk.END, values=product)


def view_orders():
    view_window = tk.Toplevel()
    view_window.title("View Orders")

    columns = ("Order ID", "Customer ID", "Product ID", "Quantity", "Amount", "Status", "Created At", "Updated At", "Shipping Date")
    tree = ttk.Treeview(view_window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)  # Set the column width to ensure all columns are visible
    tree.pack(fill=tk.BOTH, expand=True)
    connection = create_connection()
    orders = tk_read.read_orders(connection)
    connection.close()

    for order in orders:
        # print(order)  # Debug print to ensure the data includes shipping_date
        tree.insert("", tk.END, values=order)
