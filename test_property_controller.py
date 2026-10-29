from Controller.property_controller import PropertyController


def test_property_controller():
    print("=== Property Controller Test ===")

    controller = PropertyController()
    result = controller.get_all_properties()

    if result["success"]:
        properties = result["data"]

        print("Controller working successfully!")
        print("Total properties:", len(properties))

        for property_data in properties:
            print(property_data)
    else:
        print("Test failed:", result["message"])


if __name__ == "__main__":
    test_property_controller()