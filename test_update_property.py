
from Controller.property_controller import PropertyController


def test_update_property():
    controller = PropertyController()

    property_data = {
        "owner_id": 1,
        "property_name": "Green Valley Apartment",
        "property_type": "Residential",
        "address": "Flat 204, Green Valley Apartments",
        "city": "Sonipat",
        "state": "Haryana",
        "pincode": "131001",
        "monthly_rent": 15000,
        "status": "Vacant"
    }

    result = controller.update_property("P_001", property_data)

    print("=== Property Update Test ===")
    print(result["message"])

    # Verify the updated record
    verification = controller.get_property_by_id("P_001")

    if verification["success"]:
        print("Updated property details:")
        print(verification["data"])


if __name__ == "__main__":
    test_update_property()
