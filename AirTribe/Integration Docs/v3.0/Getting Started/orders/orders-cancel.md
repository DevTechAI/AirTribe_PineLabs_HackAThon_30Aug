---
title: "Cancel Order"
slug: "orders-cancel"
excerpt: "Use this API to cancel the Payment against an order."
hidden: false
createdAt: "Fri Jul 12 2024 12:41:44 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed May 28 2025 10:59:01 GMT+0000 (Coordinated Universal Time)"
---
> 📘 Note:
> 
> - You can use this API only when the `pre_auth` parameter is set to true and the payment is created against an order request.

## Environment

Use our UAT environment endpoint for testing and for integration utilize our production endpoint.

| Environment                   | Endpoints                                                            |
| :---------------------------- | :------------------------------------------------------------------- |
| User Acceptance Testing [UAT] | `https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/cancel` |
| Production [PROD]             | `https://api.pluralpay.in/api/pay/v1/orders/{order_id}/cancel`       |
