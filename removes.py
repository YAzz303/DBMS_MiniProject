import tk_delete
import tkinter as tk
from tkinter import ttk
from db import create_connection


def delete_customer():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Customer")

    tk.Label(delete_window, text="Customer ID:").grid(row=0, column=0)
    customer_id_entry = tk.Entry(delete_window)
    customer_id_entry.grid(row=0, column=1)

    def submit_delete():
        customer_id = int(customer_id_entry.get())
        tk_delete.delete_customer(customer_id)
        delete_window.destroy()

    tk.Button(delete_window, text="Submit", command=submit_delete).grid(row=1, column=0, columnspan=2)


def delete_supplier():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Supplier")

    tk.Label(delete_window, text="Supplier ID:").grid(row=0, column=0)
    supplier_id_entry = tk.Entry(delete_window)
    supplier_id_entry.grid(row=0, column=1)

    def submit_delete():
        supplier_id = int(supplier_id_entry.get())
        tk_delete.delete_supplier(supplier_id)
        delete_window.destroy()

    tk.Button(delete_window, text="Submit", command=submit_delete).grid(row=1, column=0, columnspan=2)


def delete_order():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Order")

    tk.Label(delete_window, text="Order ID:").grid(row=0, column=0)
    order_id_entry = tk.Entry(delete_window)
    order_id_entry.grid(row=0, column=1)

    def submit_delete():
        order_id = int(order_id_entry.get())
        tk_delete.delete_order(order_id)
        delete_window.destroy()

    tk.Button(delete_window, text="Submit", command=submit_delete).grid(row=1, column=0, columnspan=2)


def delete_product():
    delete_window = tk.Toplevel()
    delete_window.title("Delete Product")

    tk.Label(delete_window, text="Product ID:").grid(row=0, column=0)
    product_id_entry = tk.Entry(delete_window)
    product_id_entry.grid(row=0, column=1)

    def submit_delete():
        product_id = int(product_id_entry.get())
        tk_delete.delete_product(product_id)
        delete_window.destroy()

    tk.Button(delete_window, text="Submit", command=submit_delete).grid(row=1, column=0, columnspan=2)