---
title: "Refunds"
slug: "payment-refund"
excerpt: "Learn how you can refund a payments accepted using Plural."
hidden: false
createdAt: "Thu Aug 22 2024 10:34:57 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Mar 20 2025 09:18:20 GMT+0000 (Coordinated Universal Time)"
---
A refund is a process when a receiver returns money back to a customer for a canceled or disputed transaction. This typically happens when a customer returns a product, cancels a service, or faces an issue with their purchase. The purpose is to reverse the original transaction and return the funds to the customer.

Plural processes refund directly to the customer's original payment method to prevent chargebacks. For example, if a credit card was used for the payment, the refund will be returned to that same credit card.

You can use the below API to Create a Refund.

## 1. Create Refund

Use this API to initiate a refund against an order. You can use this API only when the order status is `processed`.

Shown below are the sample requests and sample response for a Create Refund API.

```curl cURL – UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/refunds/order_id \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_order_reference": "232343434344",
  "order_amount": {
    "value": 1100,
    "currency": "INR"
  },
  "merchant_metadata": {
    "key1": "DD",
    "key_2": "XOF"
  }
}
'
```
```curl cURL – PROD
curl --request POST \
     --url https://api.pluralpay.in/api/pay/v1/refunds/order_id \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_order_reference": "232343434344",
  "order_amount": {
    "value": 1100,
    "currency": "INR"
  },
  "merchant_metadata": {
    "key1": "DD",
    "key_2": "XOF"
  }
}
'
```
```json Sample Response
{
  "data": {
    "order_id": "v1-5757575757-aa-hU1rUd",
    "refunds": [
      {
        "merchant_refund_reference": "merchant-reference-r4n",
        "refund_id": "v1-3314042524-ga-0Y129h",
        "status": "PROCESSED",
        "merchant_id": "merchant-123",
        "refund_amount": {
          "value": 1100,
          "currency": "INR"
        },
        "created_at": "2024-04-30T08:01:321Z",
        "updated_at": "2024-04-30T08:01:321Z"
      }
    ]
  }
}
```

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/v3.0/reference/payments-refund" target="_blank">Create Refund API</a> documentation for more information.
