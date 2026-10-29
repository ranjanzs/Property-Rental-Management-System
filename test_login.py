
from getpass import getpass
from Controller.login_controller import LoginController


def test_login():
    print("=== Login Controller Test ===")

    username = input("Enter username: ").strip()
    password = getpass("Enter password: ")

    controller = LoginController()
    result = controller.login(username, password)

    if result["success"]:
        print("\nLogin successful!")
        print("Role:", result["role"])
        print("User ID:", result["user_id"])
        print("Full Name:", result["full_name"])
    else:
        print("\nLogin failed:", result["message"])


if __name__ == "__main__":
    test_login()
