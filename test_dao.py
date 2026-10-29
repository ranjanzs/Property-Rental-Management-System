
from DAO.admin_dao import AdminDAO
from DAO.owner_dao import OwnerDAO
from DAO.tenant_dao import TenantDAO
from DAO.property_dao import PropertyDAO
from DAO.rent_dao import RentDAO
from DAO.complaint_dao import ComplaintDAO


def test_dao_layer():
    print("Testing DAO Layer...")
    print("-" * 40)

    tests = [
        ("Admin", AdminDAO().get_all_admins),
        ("Owner", OwnerDAO().get_all_owners),
        ("Tenant", TenantDAO().get_all_tenants),
        ("Property", PropertyDAO().get_all_properties),
        ("Rent", RentDAO().get_all_rent_records),
        ("Complaint", ComplaintDAO().get_all_complaints),
    ]

    for name, method in tests:
        try:
            result = method()

            if isinstance(result, list):
                print(f"{name} DAO: SUCCESS - {len(result)} record(s) found")
            else:
                print(f"{name} DAO: CHECK RESULT - {result}")

        except Exception as error:
            print(f"{name} DAO: FAILED - {error}")


if __name__ == "__main__":
    test_dao_layer()
