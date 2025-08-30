---
title: "Fetch Customer with Mobile"
slug: "fetch-customer-with-mobile"
excerpt: "Use the below endpoint to Fetch customers with Mobile numbers."
hidden: true
createdAt: "Thu Feb 03 2022 07:32:01 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:49:12 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:**

[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Details",
    "0-0": "country_code\\*",
    "0-1": "string  \n(Length = 10 Characters)",
    "0-2": "vaild country code.",
    "1-0": "mobile_no\\*",
    "1-1": "string  \n(Length = 20 Characters)",
    "1-2": "valid user mobile number"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


**Request Query Param:** 

```json JSON
country_code=91&mobile_no=9791121672
```

**Response Payload:** 

```json 200 Success
{
    "country_code": "91",
    "mobile_no": "9791121672",
    "status": "INACTIVE",
    "customer_token": "TsLrJUk0oqAwoqpKSYBflQ=="
}
```
```json 400 Bad Request
{
  "error_code": "16250",
  "error_message": "INVALID_CUSTOMER_TOKEN"
}
{
  "error_code": "16050",
  "error_message": "CUSTOMER_NOT_FOUND"
}
```
```json 500 Internal Server Error
{
  "error_code": "16010",
  "error_message": "Oops, something went wrong!"
}
```
