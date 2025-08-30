---
title: "Create Customer"
slug: "create-customer-1"
excerpt: "Use the below endpoint to Create a Customer."
hidden: true
createdAt: "Tue Feb 08 2022 07:14:35 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:48:23 GMT+0000 (Coordinated Universal Time)"
---
**Request Body Parameters:**

[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Details",
    "0-0": "mobile_no\\*",
    "0-1": "string  \n(Length = 20 Characters)",
    "0-2": "valid user mobile number.",
    "1-0": "email_id\\*",
    "1-1": "string  \n(Length = 100 Characters)",
    "1-2": "valid user email id.",
    "2-0": "country_code\\*",
    "2-1": "string  \n(Length = 10 Characters)",
    "2-2": "vaild country code."
  },
  "cols": 3,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


**Response Payload:** 

```json 200 Success
{
    "country_code": "91",
    "mobile_no": "xxx",
    "status": "INACTIVE",
    "customer_token": "TsLrJUk0oqAwoqpKSYBflQ=="
}
```
