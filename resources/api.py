from flask_restx import Api
from resources.v1.transaction_resource import Transaction
from resources.v1.transaction_list_resource import TransactionList
from resources.v1.transaction_report_resource import TransactionReport
from resources.v1.client_resource import Client

api = Api(default="v1", prefix="/v1")

api.add_resource(Transaction, "/transaction")
api.add_resource(TransactionList, "/transaction-list")
api.add_resource(TransactionReport, "/transaction-report")
api.add_resource(Client, "/client")
