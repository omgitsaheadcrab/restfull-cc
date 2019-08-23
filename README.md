# Customer Credit Card Service

## Register new customer

**Definition**

`PUT /api/customer`

**Arguments**

- `"first_name":string` a globally unique identifier for this device
- `"email":string` a friendly name for this device
- `"trailing_digits":number` last four digits of credit card
- `"leading_digits":number` `OPTIONAL` first four digits of credit card
- `"card_type":string` `OPTIONAL` card issuer name
- `"start_date":string` `OPTIONAL` issue date of credit card
- `"end_date":string` `OPTIONAL` expiry date of credit card

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
- `"start_date":string` `OPTIONAL` issue date of credit card
- `"end_date":string` `OPTIONAL` expiry date of credit card

**Response**

- `404 Not Found` if customer not found
- `200 OK` on success

```json
{
    "matches": [{
        "first_name": "richard",
        "email": "richard.branson@virgin.com"
    }, {
        "first_name": "john",
        "email": "john.smith@gmail.com"
    }],
	"message": "Possible customers found"
}
```
