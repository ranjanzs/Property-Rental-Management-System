
from Database.connection import get_connection

connection = get_connection()

if connection:
    cursor = connection.cursor()

    cursor.execute("SELECT DATABASE(), @@hostname, @@port")
    print("Python connection:", cursor.fetchone())

    cursor.execute("SHOW TABLES")
    print("Tables:", cursor.fetchall())

    cursor.close()
    connection.close()

