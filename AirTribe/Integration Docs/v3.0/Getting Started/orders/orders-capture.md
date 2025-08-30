---
title: "Capture Order"
slug: "orders-capture"
excerpt: "Use this API to capture the Payment against an order."
hidden: false
createdAt: "Fri Jul 12 2024 12:36:25 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed May 28 2025 10:57:55 GMT+0000 (Coordinated Universal Time)"
---
> 📘 Note:
> 
> - You can use this API only when the `pre_auth` parameter is set to true and the payment is created against an order request.
> - You can capture a partial amount against an order. Currently, the system supports only one partial capture per order. Any remaining amount will be auto-reversed to your customer’s account.

## Environment

Use our UAT environment endpoint for testing and for integration utilize our production endpoint.

| Environment                   | Endpoints                                                             |
| :---------------------------- | :-------------------------------------------------------------------- |
| User Acceptance Testing [UAT] | `https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/capture` |
| Production [PROD]             | `https://api.pluralpay.in/api/pay/v1/orders/{order_id}/capture`       |
