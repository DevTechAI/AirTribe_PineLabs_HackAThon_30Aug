---
title: "Create Card Payment"
slug: "card-payments-create"
excerpt: "Use this API to initiate a card payment."
hidden: true
createdAt: "Wed Sep 11 2024 11:56:50 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Mar 05 2025 12:04:18 GMT+0000 (Coordinated Universal Time)"
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
