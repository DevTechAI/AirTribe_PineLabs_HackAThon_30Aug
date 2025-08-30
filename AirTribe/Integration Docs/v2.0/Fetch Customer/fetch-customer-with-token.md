---
title: "Fetch Customer with Token"
slug: "fetch-customer-with-token"
excerpt: "Use the below endpoint to Fetch Customer with Token"
hidden: true
createdAt: "Thu Feb 03 2022 07:03:38 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:49:20 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:**

| Attribute        | Type   | Details                                 |
| :--------------- | :----- | :-------------------------------------- |
| customer_token\* | string | vaild Token to be set for the customer. |

**Request Query Param:** 

```less JSON
customer_token=TsLrJUk0oqAwoqpKSYBflQ==
```

**Response Payload:** 

```json 200 Success
{
    "country_code": "91",
    "mobile_no": "xxx",
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
