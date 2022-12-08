from service.service_util import validate_schema
from service.reporting_service import reporting_service


def test_transaction_with_fixture(payload_transaction, schema_transaction):
    assert validate_schema(payload_transaction, schema_transaction) is None
    assert reporting_service.get_transaction(payload_transaction) is not None
    assert reporting_service.get_transaction(payload_transaction).status_code == 200
    assert reporting_service.get_transaction(payload_transaction).json() == {
        "fx": {"merchant": {"originalAmount": 1000, "originalCurrency": "TRY"}},
        "transaction": {
            "merchant": {
                "referenceNo": "Test-Denem-Mongo-1",
                "merchantId": 1307,
                "status": "DECLINED",
                "channel": "API",
                "customData": None,
                "chainId": "5fbc453dd66dd",
                "type": "AUTH",
                "agentInfoId": 23234,
                "operation": "3D",
                "updated_at": "2020-11-23 23:26:54",
                "created_at": "2020-11-23 23:26:53",
                "id": 1030245,
                "fxTransactionId": 1418437,
                "acquirerTransactionId": 1033164,
                "code": "173",
                "message": "Decline",
                "transactionId": "1030245-1606174013-1307",
                "agent": {
                    "id": 23234,
                    "customerIp": "89.184.22.134",
                    "customerUserAgent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 Chrome/41.0.2228.0 Safari/537.36",
                    "merchantIp": "34.240.59.77",
                    "merchantUserAgent": "PostmanRuntime/7.6.1",
                    "created_at": "2020-11-23 23:21:45",
                    "updated_at": "2020-11-23 23:21:45",
                    "deleted_at": None,
                },
            }
        },
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
        },
        "merchant": {"name": "G-Merchant"},
    }
