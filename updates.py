import tk_update
import tkinter as tk
from tkinter import ttk
from db import create_connection

def update_customer():
    update_window = tk.Toplevel()
    update_window.title("Update Customer")

    tk.Label(update_window, text="Customer ID:").grid(row=0, column=0)
    customer_id_entry = tk.Entry(update_window)
    customer_id_entry.grid(row=0, column=1)

    tk.Label(update_window, text="Field to update:").grid(row=1, column=0)
    field_combobox = ttk.Combobox(update_window, values=["name", "address", "email"])
    field_combobox.grid(row=1, column=1)

    tk.Label(update_window, text="New Value:").grid(row=2, column=0)
    new_value_entry = tk.Entry(update_window)
    new_value_entry.grid(row=2, column=1)

    def submit_update():
        customer_id = customer_id_entry.get()
        field = field_combobox.get()
        new_value = new_value_entry.get()
        tk_update.update_customer(customer_id, field, new_value)
        update_window.destroy()

    tk.Button(update_window, text="Submit", command=submit_update).grid(row=3, column=0, columnspan=2)

def update_supplier():
    update_window = tk.Toplevel()
    update_window.title("Update Supplier")

    tk.Label(update_window, text="Supplier ID:").grid(row=0, column=0)
    supplier_id_entry = tk.Entry(update_window)
    supplier_id_entry.grid(row=0, column=1)

    tk.Label(update_window, text="Field to update:").grid(row=1, column=0)
    field_combobox = ttk.Combobox(update_window, values=["name", "address", "email"])
    field_combobox.grid(row=1, column=1)

    tk.Label(update_window, text="New Value:").grid(row=2, column=0)
    new_value_entry = tk.Entry(update_window)
    new_value_entry.grid(row=2, column=1)

    def submit_update():
        supplier_id = supplier_id_entry.get()
        field = field_combobox.get()
        new_value = new_value_entry.get()
        tk_update.update_supplier(supplier_id, field, new_value)
        update_window.destroy()

    tk.Button(update_window, text="Submit", command=submit_update).grid(row=3, column=0, columnspan=2)


def update_product():
    update_window = tk.Toplevel()
    update_window.title("Update Product")

    tk.Label(update_window, text="Product ID:").grid(row=0, column=0)
    product_id_entry = tk.Entry(update_window)
    product_id_entry.grid(row=0, column=1)

    tk.Label(update_window, text="Field to update:").grid(row=1, column=0)
    field_combobox = ttk.Combobox(update_window, values=["name", "category", "price", "in_stock"])
    field_combobox.grid(row=1, column=1)

    tk.Label(update_window, text="New Value:").grid(row=2, column=0)
    new_value_entry = tk.Entry(update_window)
    new_value_entry.grid(row=2, column=1)

    def submit_update():
        product_id = product_id_entry.get()
        field = field_combobox.get()
        new_value = new_value_entry.get()
        tk_update.update_product(product_id, field, new_value)
        update_window.destroy()

    tk.Button(update_window, text="Submit", command=submit_update).grid(row=3, column=0, columnspan=2)

def update_order():
    update_window = tk.Toplevel()
    update_window.title("Update Order")

    tk.Label(update_window, text="Order ID:").grid(row=0, column=0)
    order_id_entry = tk.Entry(update_window)
    order_id_entry.grid(row=0, column=1)

    tk.Label(update_window, text="Field to update:").grid(row=1, column=0)
    field_combobox = ttk.Combobox(update_window, values=["status", "quantity", "shipping_date"])
    field_combobox.grid(row=1, column=1)

    tk.Label(update_window, text="New Value:").grid(row=2, column=0)
    new_value_entry = tk.Entry(update_window)
    new_value_entry.grid(row=2, column=1)

    def submit_update():
        order_id = order_id_entry.get()
        field = field_combobox.get()
        new_value = new_value_entry.get()
        tk_update.update_order(order_id, field, new_value)
        update_window.destroy()

    tk.Button(update_window, text="Submit", command=submit_update).grid(row=3, column=0, columnspan=2)

