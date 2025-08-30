---
title: "Validate VPA Integration"
slug: "validate-vpa-integration"
excerpt: ""
hidden: true
createdAt: "Thu Jul 28 2022 14:10:03 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:54:41 GMT+0000 (Coordinated Universal Time)"
---
**Request Body Parameters:**

| Attribute   | Type   | Details                         |
| :---------- | :----- | :------------------------------ |
| merchant_id | int    | Merchant ID                     |
| vpa         | string | Valid UPI ID. eg.(john.doe@ybl) |

Request Payload

```json
{
  "merchant_data": {
    "merchant_id": "11573"
  },
  "upi_data": {
    "vpa": "xyz@ybl"
  }
}
```

**Response Payload:** 

```json 200 success
{
 "vpa": "john.doe@ybl",
 "response_code": 1,
 "response_message": "VPA is available"
}
```

**Failure Payload:** 

```json 400
{
 "vpa": "john.doee@ok",
 "response_code": 11011,
 "response_message": "Please enter a valid VPA ID"
}
```
