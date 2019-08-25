# Customer Credit Card Service

## Usage

**Install dependencies:**

```bash
$ python2 -m virtualenv env
$ source env/bin/activate
$ # dependencies for local testing
$ pip install -r requirements.txt 
$ # dependencies for dev_appserver
$ pip install -r requirements.txt -t lib/
```

**Prepare storage:**

Either initialise an instance of [cloud_sql_proxy](https://cloud.google.com/sql/docs/mysql/sql-proxy) or create a local database named 'restfulcc'


```bash
$ mysql -h 127.0.0.1 -u root -p
mysql> CREATE DATABASE restfulcc;
mysql> QUIT;
```

**Run the application in GAE dev_appserver:**

```bash
$ dev_appserver app.yaml
```

**Run the application locally:**

```bash
$ python2 main.py
```

**Run tests locally:**

```bash
$ pytest -v main_test.py
```

## Register new customer

**Definition**

`PUT /api/customer`

**Arguments**

- `"first_name":string` a globally unique identifier for this device
- `"email":string` a friendly name for this device
- `"trailing_digits":number` last four digits of credit card
- `"leading_digits":number` `OPTIONAL` first four digits of credit card
- `"card_type":string` `OPTIONAL` card issuer name
- `"start_date":string` `OPTIONAL` issue date of credit card (MM.YYYY)
- `"end_date":string` `OPTIONAL` expiry date of credit card (MM.YYYY)

**Response**

- `201 Created` on success
- `201 Bad Request` on fail to due missing required fields

```json
{
    "data": {
		"card_type": null,
        "email": "john@gmail.com",
		"end_date": null,
        "first_name": "john",
		"leading_digits": null,
        "start_date": "08.2012",
        "trailing_digits": 3456
    },
    "message": "Customer registered"
}
```

`OPTIONAL` arguments null if not provided

## Retrieve customer matches

**Definition**

`GET /api/customer`

**Arguments**

- `"trailing_digits":number` last four digits of credit card
- `"leading_digits":number` `OPTIONAL` first four digits of credit card
- `"card_type":string` `OPTIONAL` card issuer name
- `"start_date":string` `OPTIONAL` issue date of credit card (MM.YYYY)
- `"end_date":string` `OPTIONAL` expiry date of credit card (MM.YYYY)

**Response**

- `404 Not Found` if customer not found
- `200 OK` on success

```json
{
    "matches": {
        "richard.branson@virgin.com": "richard",
		"john.smith@gmail.com": "john"
    },
	"message": "Possible customers found"
}
```
