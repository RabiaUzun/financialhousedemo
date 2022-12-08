import pytest
from service.app import app


@pytest.fixture()
def initialize_app():
    return app


@pytest.fixture()
def schema_client():
    return {
        "type": "object",
        "required": ["transactionId"],
        "additionalProperties": False,
        "properties": {
            "transactionId": {"type": "string"},
        },
    }


@pytest.fixture()
def payload_client():
    return {"transactionId": "1030245-1606174013-1307"}


@pytest.fixture()
def schema_transaction():
    return {
        "type": "object",
        "required": ["transactionId"],
        "additionalProperties": False,
        "properties": {
            "transactionId": {"type": "string"},
        },
    }


@pytest.fixture()
def payload_transaction():
    return {"transactionId": "1030245-1606174013-1307"}


@pytest.fixture()
def schema_transaction_list():
    return {
        "type": "object",
        "required": [],
        "additionalProperties": False,
        "properties": {
            "fromDate": {"type": "string"},
            "toDate": {"type": "string"},
            "status": {
                "type": "string",
                "enum": ["APPROVED", "WAITING", "DECLINED", "ERROR"],
            },
            "operation": {
                "type": "string",
                "enum": ["DIRECT", "REFUND", "3D", "3DAUTH", "STORED"],
            },
            "merchantId": {"type": "integer"},
            "acquirerId": {"type": "integer"},
            "paymentMethod": {
                "type": "string",
                "enum": [
                    "CREDITCARD",
                    "CUP",
                    "IDEAL",
                    "GIROPAY",
                    "MISTERCASH",
                    "STORED",
                    "PAYTOCARD",
                    "CEPBANK",
                    "CITADEL",
                ],
            },
            "errorCode": {
                "type": "string",
                "enum": [
                    "Do not honor",
                    "Invalid Transaction",
                    "Invalid Card",
                    "Not sufficient funds",
                    "Incorrect PIN",
                    "Invalid country association",
                    "Currency not allowed",
                    "3-D Secure Transport Error",
                    "Transaction notpermitted to cardholder",
                ],
            },
            "filterField": {
                "type": "string",
                "enum": [
                    "Transaction UUID",
                    "Customer Email",
                    "Reference No",
                    "Custom Data",
                    "Card PAN",
                ],
            },
            "filterValue": {"type": "string"},
            "page": {"type": "integer"},
        },
    }


@pytest.fixture()
def payload_transaction_list():
    return {"fromDate": "2017-07-26", "toDate": "2017-08-01"}


@pytest.fixture()
def schema_transaction_report():
    return {
        "type": "object",
        "required": ["fromDate", "toDate"],
        "additionalProperties": False,
        "properties": {
            "fromDate": {"type": "string"},
            "toDate": {"type": "string"},
            "merchant": {"type": "integer"},
            "acquirer": {"type": "integer"},
        },
    }


@pytest.fixture()
def payload_transaction_report():
    return {"fromDate": "2015-07-01", "toDate": "2015-10-01"}
