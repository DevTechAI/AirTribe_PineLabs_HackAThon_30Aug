---
title: "Process Payment Netbanking"
slug: "process-payment-netbanking-1"
excerpt: "Use the below endpoint to Process Payment Netbanking."
hidden: true
createdAt: "Thu Feb 03 2022 12:43:10 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:50:08 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

[block:parameters]
{
  "data": {
    "h-0": "Parameter Name",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "pay_code\\*",
    "0-1": "string",
    "0-2": "pay_code is the unique identifier of the bank on which net banking transaction is intended. pay_code can be taken from the codes table.",
    "1-0": "customer_data",
    "1-1": "()",
    "1-2": "",
    "2-0": "mobile_no",
    "2-1": "integer  \n(Length = 20 Characters)",
    "2-2": "Vaild mobile number",
    "3-0": "country_code",
    "3-1": "integer  \n(Length = 10 Characters)",
    "3-2": "Vaild country code.",
    "4-0": "email_id",
    "4-1": "string  \n(Length = 100 Characters)",
    "4-2": "Email of the user."
  },
  "cols": 3,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


**Request Body payload:** 

```json JSON
{
    "netbanking_data": {
        "pay_code": "NB1006"
    },
    "customer_data": {
        "country_code": "91",
        "mobile_number": "9121004027",
        "email_id": "test_customer@abc.com"
    }
}
```

**Response Payload:** 

```json 200 Success
{
  "content": "&lt;!DOCTYPE html>&lt;html>&lt;head>&lt;title> Redirecting ... &lt;/title>&lt;/head>&lt;body>&lt;script>var url = &#39;https://test.pinepg.in/pinepg/v2/process/payment?token=lRPM%2bQYBt%2f3QFrJt5VBAe4rSBIef9B8I5N5zEzmSwms%3d&#39;;window.location = url;&lt;/script>&lt;/body>&lt;/html>",
  "payment_id": 1623429,
  "order_id": 46882,
  "amount_in_paise": 300,
  "response_code": 1,
  "response_message": "Payment Successful!"
}
```
```json 400 Bad Request
{}
```

**Response Parameters** 

| Parameter Name   | Type   | Description                           |
| :--------------- | :----- | :------------------------------------ |
| content          | string | Html content to load the output data. |
| payment_id       | long   | Unique payment id.                    |
| order_id         | long   | Unique order id.                      |
| amount_in_paise  | long   | Amount paid in paise.                 |
| response_code    | string | Response code.                        |
| response_message | string | Short message about code.             |
