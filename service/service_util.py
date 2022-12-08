from jsonschema import Draft7Validator, exceptions
from jsonschema.validators import validator_for
from werkzeug.exceptions import BadRequest


def validate_schema(instance, schema):
    try:
        validator = validator_for(schema, Draft7Validator)
        validator = validator(schema=schema)
        validator.validate(instance)
    except exceptions.ValidationError as err:
        msg = str(err)
        msg = msg[: msg.index("\n")]
        raise BadRequest(msg) from err
