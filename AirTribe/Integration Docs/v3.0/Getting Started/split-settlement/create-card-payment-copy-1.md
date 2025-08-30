---
title: "Create Payment"
slug: "create-card-payment-copy-1"
excerpt: "Use this API to initiate a payment."
hidden: true
createdAt: "Thu Jan 02 2025 11:04:11 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Jan 09 2025 14:04:06 GMT+0000 (Coordinated Universal Time)"
---
## Environment

Use our UAT environment endpoint for testing and for integration utilize our production endpoint.

| Environment                   | Endpoints                                                              |
| :---------------------------- | :--------------------------------------------------------------------- |
| User Acceptance Testing [UAT] | `https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/payments` |
| Production [PROD]             | `https://api.pluralpay.in/api/pay/v1/orders/{order_id}/payments`       |

> 📘 NOTE:
> 
> - CVV-Less feature is only supported for seamless card transactions.
> - You can implement a CVV-less flow for processing payments on your systems, provided that the token type used is `NETWORK_TOKEN`.
