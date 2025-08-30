---
title: "Create Payment via Pay by Points"
slug: "pay-by-point-payment-create"
excerpt: "Use this API to start accepting payment using Points."
hidden: false
createdAt: "Thu Sep 12 2024 05:58:12 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Mar 24 2025 11:47:26 GMT+0000 (Coordinated Universal Time)"
---
## Environment

Use our UAT environment endpoint for testing and for integration utilize our production endpoint.

| Environment                   | Endpoints                                                              |
| :---------------------------- | :--------------------------------------------------------------------- |
| User Acceptance Testing [UAT] | `https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/payments` |
| Production [PROD]             | `https://api.pluralpay.in/api/pay/v1/orders/{order_id}/payments`       |

> 📘 Important:
> 
> - We initiate a Points payment against a card transaction as a split payment.
> - You are required to create two different payments object one for a card payment and the other for a points payment.
