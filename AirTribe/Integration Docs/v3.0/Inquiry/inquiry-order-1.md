---
title: "Inquiry Order"
slug: "inquiry-order-1"
excerpt: "This API Help to get Inquiry Order"
hidden: true
createdAt: "Fri Feb 04 2022 11:17:54 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:53:00 GMT+0000 (Coordinated Universal Time)"
---
**Response Payload:** 

```json 200 Success
{
    "merchant_data": {
        "merchant_id": 11573,
        "order_id": "2412I124E443611"
    },
    "order_data": {
        "order_status": "CHARGED",
        "plural_order_id": 33890,
        "amount": 200,
        "order_desc": "Test Order"
    }
}
```
```json Partial Refund
{
  "merchant_data": {
    "merchant_id": 11573,
    "order_id": "nbpay293279392667184"
  },
  "order_data": {
    "order_status": "PARTIAL_REFUNDED",
    "plural_order_id": 96874,
    "amount": 10000,
    "order_desc": null
  }
}
```

**Response Parameters** 

| Parameter Name  | Type   | Description             |
| :-------------- | :----- | :---------------------- |
| merchant_id     | string | unique merchant id.     |
| order_id        | string | unique order id.        |
| order_status    | string | status of the order.    |
| plural_order_id | string | unique plural order id. |
| amount          | long   | amount in paise.        |
| order_desc      | string | order arrangement.      |
