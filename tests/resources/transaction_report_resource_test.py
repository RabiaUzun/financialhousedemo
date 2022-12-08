from service.service_util import validate_schema
from service.reporting_service import reporting_service


def test_transaction_report_with_fixture(
    payload_transaction_report, schema_transaction_report
):
    assert (
        validate_schema(payload_transaction_report, schema_transaction_report) is None
    )
    assert (
        reporting_service.get_transaction_report(payload_transaction_report) is not None
    )
    assert (
        reporting_service.get_transaction_report(payload_transaction_report).status_code
        == 500
    )
    assert reporting_service.get_transaction_report(
        payload_transaction_report
    ).json() == {
        "code": 9,
        "status": "DECLINED",
        "message": "10.72.23.66:27017: The 'cursor' option is required, except for aggregate with the explain argument",
    }
