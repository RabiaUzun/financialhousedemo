PYTHON_ENV = "local"

REPORTING_SERVICE = "https://sandbox-reporting.rpdpymnt.com"
MERCHANT_EMAIL = "demo@financialhouse.io"
MERCHANT_PASSWORD = "cjaiU8CV"

TOKEN_VALIDITY_SECONDS = 600

LOGIN_PATH = "/api/v3/merchant/user/login"  # Login with email and password.
TRANSACTION_REPORT_PATH = (
    "/api/v3/transactions/report"  # Request for list of transaction.
)
TRANSACTION_LIST_PATH = "/api/v3/transaction/list"  # Request for list of transaction.
TRANSACTION_PATH = "/api/v3/transaction"  # Request for all information of transaction.
CLIENT_PATH = "/api/v3/client"  # Request for information of client.
