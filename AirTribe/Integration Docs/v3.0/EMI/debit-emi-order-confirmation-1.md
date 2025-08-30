---
title: "Debit EMI: Order Confirmation"
slug: "debit-emi-order-confirmation-1"
excerpt: "This API Help to get Debit EMI: Order Confirmation"
hidden: true
metadata: 
  image: []
  robots: "index"
createdAt: "Mon Feb 07 2022 04:43:24 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Feb 09 2022 11:54:03 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

| Attribute | Type   | Details                             |
| :-------- | :----- | :---------------------------------- |
| token\*   | string | valid token to check for the order. |

**Response Payload:** 

```json 200 Success
{
    "order_confirmation_response": {
        "merchant_id": "11607",
        "payment_status_code": "4",
        "payment_status": "CAPTURED",
        "payment_id": "438471",
        "plural_order_id": "106801"
    },
    "response_code": 14010,
    "response_message": "SUCCESS"
}
```
```json 400 Bad Request
{
  "error_code": "14110",
  "error_message": "Your order could not be confirmed. Please try again"
}
```
