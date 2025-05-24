import mysql.connector
from mysql.connector import Error
 
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password@123",  # Replace with your MySQL root password
            database="employee1_db"
        )
        return connection
    except Error as e:
        print("Error connecting to MySQL", e)
        return None
