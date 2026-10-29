
from Controller.owner_controller import OwnerController


def test_owner_controller():
    print("=== Owner Controller Test ===")

    controller = OwnerController()
    result = controller.get_all_owners()

    if result["success"]:
        owners = result["data"]
        print("Controller working successfully!")
        print("Total owners:", len(owners))
    else:
        print("Test failed:", result["message"])


if __name__ == "__main__":
    test_owner_controller()
