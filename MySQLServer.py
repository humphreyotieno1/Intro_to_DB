import mysql.connector

def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Humphrey@18',
            ssl_disabled = True
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
            
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL server: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")
            
if __name__ == "__main__":
    create_database()