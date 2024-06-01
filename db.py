import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Yrtking$123',
            database='inventory_manage'
        )
        if connection.is_connected():
            print('Connected to MySql database')
            return connection
    except:
        print('Error while connecting to MySQL')
        return None
        