# Financial House Demo Flask Proxy Project

To be able to run the application in your local environment 
without any problem please follow the steps below:

`virtualenv --python=PATH-TO-PYTHON-3.7 .venv`

`source .venv/bin/activate`

`make install`

With the steps above, your local environment is successfully prepared to 
run the application.

Run the below command to start the application

`make start`

The curl request of the endpoints are stated below:

**Client**
```
curl --location --request POST 'http://localhost:5000/v1/client' \
--header 'Content-Type: application/json' \
--data-raw '{
    "transactionId": "1030245-1606174013-1307"
}'
```
****
**Transaction**
```
curl --location --request POST 'http://localhost:5000/v1/transaction' \
--header 'Content-Type: application/json' \
--data-raw '{
    "transactionId": "1030245-1606174013-1307"
}'
```
****
**Transaction List**
```
curl --location --request POST 'http://localhost:5000/v1/transaction-list' \
--header 'Content-Type: application/json' \
--data-raw '{
    "fromDate": "2017-07-26",
    "toDate": "2017-08-01"
}'
```
****
**Transaction Report**
```
curl --location --request POST 'http://localhost:5000/v1/transaction-report' \
--header 'Content-Type: application/json' \
--data-raw '{
        "fromDate": "2015-07-01",
        "toDate": "2015-10-01"
    }'
```

# Test

You can run the unit tests with the command below.

`make test`