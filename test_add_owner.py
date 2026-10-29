
from Controller.owner_controller import OwnerController


def test_add_owner():
    controller = OwnerController()

    owner_data = {
        "username": "test_owner_01",
        "password": "TestOwner@123",
        "full_name": "Test Property Owner",
        "email": "testowner01@example.com",
        "phone": None,
        "aadhar_no": None,
        "address": "Sonipat, Haryana"
    }

    result = controller.add_owner(owner_data)

    print("=== Add Owner Test ===")
    print(result["message"])


if __name__ == "__main__":
    test_add_owner()
