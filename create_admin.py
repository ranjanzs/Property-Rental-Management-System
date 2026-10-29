
import bcrypt
from getpass import getpass

from Database.connection import get_connection


def create_admin():
    print("\n=== Create Admin Account ===")

    username = input("Enter username: ").strip()
    password = getpass("Enter password: ")
    full_name = input("Enter full name: ").strip()
    email = input("Enter email (optional): ").strip() or None
    phone = input("Enter phone (optional): ").strip() or None

    if not username or not password or not full_name:
        print("Username, password, and full name are required.")
        return

    # Securely hash the password using bcrypt
    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    connection = get_connection()

    if connection is None:
        print("Database connection failed.")
        return

    cursor = None

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO Admin
                (Username, Password_Hash, Full_Name, Email, Phone)
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            username,
            password_hash,
            full_name,
            email,
            phone
        )

        cursor.execute(query, values)
        connection.commit()

        print("Admin account created successfully!")

    except Exception as error:
        connection.rollback()
        print("Could not create admin:", error)

    finally:
        if cursor is not None:
            cursor.close()
        connection.close()


if __name__ == "__main__":
    create_admin()
