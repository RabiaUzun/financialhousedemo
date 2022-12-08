from flask_restx import Resource
from flask import request
from resources.v1.api import api as ns
from service.service_util import validate_schema
from service.reporting_service import reporting_service


class TransactionList(Resource):
    schema = {
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

    @ns.doc(responses={400: "Bad Request", 200: "Success Result", 404: "Not Found"})
    def post(self):
        payload = request.json
        validate_schema(payload, self.schema)
        response = reporting_service.get_transaction_list(payload)
        return response.json(), response.status_code
