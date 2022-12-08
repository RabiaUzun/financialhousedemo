from service.service_util import validate_schema
from service.reporting_service import reporting_service


def test_transaction_list_with_fixture(
    payload_transaction_list, schema_transaction_list
):
    assert validate_schema(payload_transaction_list, schema_transaction_list) is None
    assert reporting_service.get_transaction_list(payload_transaction_list) is not None
    assert (
        reporting_service.get_transaction_list(payload_transaction_list).status_code
        == 200
    )
    assert reporting_service.get_transaction_list(payload_transaction_list).json() == {
        "per_page": 50,
        "current_page": 1,
        "next_page_url": None,
        "prev_page_url": None,
        "from": 1,
        "to": 4,
        "data": [
            {
                "customerInfo": {
                    "number": "0000000000000000",
                    "email": "joe.doe@example.com",
                    "billingFirstName": "John",
                    "billingLastName": "Doe",
                },
                "updated_at": "2017-07-26 17:02:35",
                "created_at": "2017-07-26 17:02:29",
                "fx": {
                    "merchant": {
                        "originalAmount": 50000,
                        "originalCurrency": "TRY",
                        "convertedAmount": 50000,
                        "convertedCurrency": "TRY",
                    }
                },
                "acquirer": {
                    "id": 31,
                    "name": "Mergen Bank",
                    "code": "MB",
                    "type": "CITADEL",
                },
                "transaction": {
                    "merchant": {
                        "referenceNo": "cpg_5978ca4987b86",
                        "status": "APPROVED",
                        "operation": "3DAUTH",
                        "type": "AUTH",
                        "message": "Approved",
                        "customData": "1773-1501088340-1",
                        "created_at": "2017-07-26 17:02:34",
                        "transactionId": "981964-1501088554-3",
                    }
                },
                "merchant": {
                    "id": 3,
                    "name": "Dev-Merchant",
                    "allowPartialRefund": True,
                    "allowPartialCapture": True,
                },
            },
            {
                "customerInfo": {
                    "billingFirstName": "John",
                    "billingLastName": "Doe",
                    "email": "joe.doe@example.com",
                },
                "updated_at": "2017-07-26 16:57:31",
                "created_at": "2017-07-26 16:57:30",
                "fx": {
                    "merchant": {
                        "originalAmount": 50000,
                        "originalCurrency": "TRY",
                        "convertedAmount": 50000,
                        "convertedCurrency": "TRY",
                    }
                },
                "acquirer": {
                    "id": 31,
                    "name": "Mergen Bank",
                    "code": "MB",
                    "type": "CITADEL",
                },
                "transaction": {
                    "merchant": {
                        "referenceNo": "cpg_5978c9f1490f8",
                        "status": "WAITING",
                        "customData": "1772-1501088249-1",
                        "type": "AUTH",
                        "operation": "3D",
                        "created_at": "2017-07-26 16:57:30",
                        "message": "Waiting",
                        "transactionId": "981962-1501088250-3",
                    }
                },
                "merchant": {
                    "id": 3,
                    "name": "Dev-Merchant",
                    "allowPartialRefund": True,
                    "allowPartialCapture": True,
                },
            },
            {
                "customerInfo": {
                    "billingFirstName": "John",
                    "billingLastName": "Doe",
                    "email": "joe.doe@example.com",
                },
                "updated_at": "2017-07-26 16:57:02",
                "created_at": "2017-07-26 16:57:02",
                "fx": {
                    "merchant": {
                        "originalAmount": 50000,
                        "originalCurrency": "TRY",
                        "convertedAmount": 50000,
                        "convertedCurrency": "TRY",
                    }
                },
                "acquirer": {
                    "id": 31,
                    "name": "Mergen Bank",
                    "code": "MB",
                    "type": "CITADEL",
                },
                "transaction": {
                    "merchant": {
                        "referenceNo": "cpg_5978c9d46e117",
                        "status": "WAITING",
                        "customData": "1771-1501088220-1",
                        "type": "AUTH",
                        "operation": "3D",
                        "created_at": "2017-07-26 16:57:02",
                        "message": "Waiting",
                        "transactionId": "981961-1501088222-3",
                    }
                },
                "merchant": {
                    "id": 3,
                    "name": "Dev-Merchant",
                    "allowPartialRefund": True,
                    "allowPartialCapture": True,
                },
            },
            {
                "customerInfo": {
                    "billingFirstName": "John",
                    "billingLastName": "O'Connor",
                    "email": "oconnor@bumin.com.tr",
                },
                "updated_at": "2017-07-26 14:47:06",
                "created_at": "2017-07-26 14:47:05",
                "fx": {
                    "merchant": {
                        "originalAmount": 100,
                        "originalCurrency": "EUR",
                        "convertedAmount": 100,
                        "convertedCurrency": "EUR",
                    }
                },
                "acquirer": {
                    "id": 31,
                    "name": "Mergen Bank",
                    "code": "MB",
                    "type": "CITADEL",
                },
                "transaction": {
                    "merchant": {
                        "referenceNo": "api_5978ab63f4217",
                        "status": "WAITING",
                        "customData": None,
                        "type": "AUTH",
                        "operation": "3D",
                        "created_at": "2017-07-26 14:47:05",
                        "message": "Waiting",
                        "transactionId": "981930-1501080425-3",
                    }
                },
                "merchant": {
                    "id": 3,
                    "name": "Dev-Merchant",
                    "allowPartialRefund": False,
                    "allowPartialCapture": True,
                },
            },
        ],
    }
