import updates
import removes
import views
import adds
import tkinter as tk
from tkinter import ttk
from db import create_connection

def main_window():
    root = tk.Tk()
    root.title("Inventory Management System")

    customer_frame = ttk.Frame(root)
    customer_frame.grid(row=0, column=0, padx=10, pady=10)

    # Customer Management
    ttk.Label(customer_frame, text="Customer Management").grid(row=0, column=0, columnspan=2)
    ttk.Button(customer_frame, text="Add Customer", command=adds.add_customer).grid(row=1, column=0)
    ttk.Button(customer_frame, text="View Customers", command=views.view_customers).grid(row=1, column=1)
    ttk.Button(customer_frame, text="Update Customer", command=updates.update_customer).grid(row=2, column=0)
    ttk.Button(customer_frame, text="Delete Customer", command=removes.delete_customer).grid(row=2, column=1)

     #Supplier Management
    supplier_frame = ttk.Frame(root)
    supplier_frame.grid(row=1, column=0, padx=10, pady=10)

    ttk.Label(supplier_frame, text="Supplier Management").grid(row=0, column=0, columnspan=2)
    ttk.Button(supplier_frame, text="Add Supplier", command=adds.add_supplier).grid(row=1, column=0) 
    ttk.Button(supplier_frame, text="View Suppliers", command=views.view_suppliers).grid(row=1, column=1) 
    ttk.Button(supplier_frame, text="Update Supplier", command=updates.update_supplier).grid(row=2, column=0) 
    ttk.Button(supplier_frame, text="Delete Supplier", command=removes.delete_supplier).grid(row=2, column=1) 

    # Product Management
    product_frame = ttk.Frame(root)
    product_frame.grid(row=2, column=0, padx=10, pady=10)

    ttk.Label(product_frame, text="Product Management").grid(row=0, column=0, columnspan=2)
    ttk.Button(product_frame, text="Add Product", command=adds.add_product).grid(row=1, column=0) 
    ttk.Button(product_frame, text="View Products", command=views.view_products).grid(row=1, column=1) 
    ttk.Button(product_frame, text="Update Product", command=updates.update_product).grid(row=2, column=0) 
    ttk.Button(product_frame, text="Delete Product", command=removes.delete_product).grid(row=2, column=1) 

    # Order Management
    order_frame = ttk.Frame(root)
    order_frame.grid(row=3, column=0, padx=10, pady=10)

    ttk.Label(order_frame, text="Order Management").grid(row=0, column=0, columnspan=2)
    ttk.Button(order_frame, text="Add Order", command=adds.add_order).grid(row=1, column=0) 
    ttk.Button(order_frame, text="View Orders", command=views.view_orders).grid(row=1, column=1) 
    ttk.Button(order_frame, text="Update Order", command=updates.update_order).grid(row=2, column=0) 
    ttk.Button(order_frame, text="Delete Order", command=removes.delete_order).grid(row=2, column=1) 

    root.mainloop()

if __name__=="__main__":
    main_window()