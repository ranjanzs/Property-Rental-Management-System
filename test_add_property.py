
from Controller.property_controller import PropertyController


def test_add_property():
    controller = PropertyController()

    property_data = {
        "owner_id": 1,
        "property_name": "Test Rental House",
        "property_type": "Residential",
        "address": "Sector 15",
        "city": "Sonipat",
        "state": "Haryana",
        "pincode": "131001",
        "monthly_rent": 12000,
        "status": "Vacant"
    }

    result = controller.add_property(property_data)

    print("=== Add Property Test ===")
    print(result["message"])


if __name__ == "__main__":
    test_add_property()
