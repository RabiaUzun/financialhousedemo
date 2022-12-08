from flask_restx import Resource
from flask import request
from resources.v1.api import api as ns
from service.service_util import validate_schema
from service.reporting_service import reporting_service


class Client(Resource):
    schema = {
        "type": "object",
        "required": ["transactionId"],
        "additionalProperties": False,
        "properties": {
            "transactionId": {"type": "string"},
        },
    }

    @ns.doc(responses={400: "Bad Request", 200: "Success Result", 404: "Not Found"})
    def post(self):
        payload = request.json
        validate_schema(payload, self.schema)
        response = reporting_service.get_client(payload)
        return response.json(), response.status_code
