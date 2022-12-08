import json
import time
import requests


class ReportingService:
    def init_app(self, app):
        self.reporting_service = app.config["REPORTING_SERVICE"]
        self.merchant_email = app.config["MERCHANT_EMAIL"]
        self.merchant_password = app.config["MERCHANT_PASSWORD"]
        self.login_path = app.config["LOGIN_PATH"]
        self.transaction_report_path = app.config["TRANSACTION_REPORT_PATH"]
        self.transaction_list_path = app.config["TRANSACTION_LIST_PATH"]
        self.transaction_path = app.config["TRANSACTION_PATH"]
        self.client_path = app.config["CLIENT_PATH"]
        self.token = self.create_token()
        self.start_time = time.time()
        self.token_validity_seconds = app.config["TOKEN_VALIDITY_SECONDS"]

    def create_token(self):
        url = f"{self.reporting_service}{self.login_path}"

        payload = json.dumps(
            {
                "email": self.merchant_email,
                "password": self.merchant_password,
            }
        )
        headers = {"Content-Type": "application/json"}

        response = requests.request(
            "POST", url, headers=headers, data=payload, timeout=3
        )
        if response.status_code == 200:
            self.token = response.json()["token"]
            self.start_time = time.time()
            return self.token
        return None

    def check_token(self):
        finish_time = time.time()
        elapsed_time = finish_time - self.start_time
        if elapsed_time > self.token_validity_seconds:
            self.start_time = time.time()
            self.create_token()

    def get_transaction_report(self, payload):
        url = f"{self.reporting_service}{self.transaction_report_path}"
        self.check_token()
        headers = {"Authorization": self.token}
        response = requests.request(
            "POST", url, headers=headers, data=payload, timeout=3
        )
        return response

    def get_transaction_list(self, payload):
        url = f"{self.reporting_service}{self.transaction_list_path}"
        self.check_token()
        headers = {"Authorization": self.token}
        response = requests.request(
            "POST", url, headers=headers, data=payload, timeout=3
        )
        return response

    def get_transaction(self, payload):
        url = f"{self.reporting_service}{self.transaction_path}"
        self.check_token()
        headers = {"Authorization": self.token}
        response = requests.request(
            "POST", url, headers=headers, data=payload, timeout=3
        )
        return response

    def get_client(self, payload):
        url = f"{self.reporting_service}{self.client_path}"
        self.check_token()
        headers = {"Authorization": self.token}
        response = requests.request(
            "POST", url, headers=headers, data=payload, timeout=3
        )
        return response


reporting_service = ReportingService()
