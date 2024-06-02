import tk_read
import tkinter as tk
from tkinter import ttk
from db import create_connection

def view_customers():
    view_window = tk.Toplevel()
    view_window.title("View Customers")

    tree = ttk.Treeview(view_window, columns=("ID", "Name", "Address", "Email", "Created At", "Updated At"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Address", text="Address")
    tree.heading("Email", text="Email")
    tree.heading("Created At", text="Created At")
    tree.heading("Updated At", text="Updated At")
    tree.pack(fill=tk.BOTH, expand=True)

    connection = create_connection()
    customers = tk_read.read_customers(connection)
    connection.close()

    for customer in customers:
        tree.insert("", tk.END, values=customer)

def view_suppliers():
    view_window = tk.Toplevel()
    view_window.title("View Suppliers")

    tree = ttk.Treeview(view_window, columns=("ID", "Name", "Address", "Email", "Created At", "Updated At"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Address", text="Address")
    tree.heading("Email", text="Email")
    tree.heading("Created At", text="Created At")
    tree.heading("Updated At", text="Updated At")
    tree.pack(fill=tk.BOTH, expand=True)

    connection = create_connection()
    suppliers = tk_read.read_suppliers(connection)
    connection.close()

    for supplier in suppliers:
        tree.insert("", tk.END, values=supplier)

def view_products():
    view_window = tk.Toplevel()
    view_window.title("View Products")

    tree = ttk.Treeview(view_window, columns=("ID", "Supplier ID", "Name", "Category", "Price", "In Stock", "Created At", "Updated At"), show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Supplier ID", text="Supplier ID")
    tree.heading("Name", text="Name")
    tree.heading("Category", text="Category")
    tree.heading("Price", text="Price")
    tree.heading("In Stock", text="In Stock")
    tree.heading("Created At", text="Created At")
    tree.heading("Updated At", text="Updated At")
    tree.pack(fill=tk.BOTH, expand=True)

    connection = create_connection()
    products = tk_read.read_products(connection)
    connection.close()

    for product in products:
        tree.insert("", tk.END, values=product)

def view_orders():
    view_window = tk.Toplevel()
    view_window.title("View Orders")

    columns = ("ID", "Customer ID", "Product ID", "Quantity", "Amount", "Status", "Created At", "Updated At", "Shipping Date")
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
