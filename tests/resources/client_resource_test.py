from service.service_util import validate_schema
from service.reporting_service import reporting_service


def test_client_with_fixture(payload_client, schema_client):
    assert validate_schema(payload_client, schema_client) is None
    assert reporting_service.get_client(payload_client) is not None
    assert reporting_service.get_client(payload_client).status_code == 200
    assert reporting_service.get_client(payload_client).json() == {
        "customerInfo": {
            "billingFirstName": "CEM",
            "billingLastName": "VAROL",
            "issueNumber": None,
            "email": "cem@freelancer.run",
            "billingCompany": "BT",
            "billingCity": "876b3170-075a-4632-b3e2-91e9650f5991",
            "updated_at": "2020-11-23 23:26:53",
            "created_at": "2020-11-23 23:26:53",
            "id": 721148,
        }
    }
