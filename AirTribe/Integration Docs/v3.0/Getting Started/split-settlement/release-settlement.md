---
title: "Release Settlement"
slug: "release-settlement"
excerpt: "Use this API to release a settlement against an order."
hidden: false
createdAt: "Fri Dec 06 2024 06:56:13 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed May 28 2025 11:11:46 GMT+0000 (Coordinated Universal Time)"
---
## Environment

Use our UAT environment endpoint for testing and for integration utilize our production endpoint.

| Environment                   | Endpoints                                                                                        |
| :---------------------------- | :----------------------------------------------------------------------------------------------- |
| User Acceptance Testing [UAT] | `https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{orderId}/settlementId/{settlementId}/release` |
| Production [PROD]             | `https://api.pluralpay.in/api/pay/v1/orders/{orderId}/settlementId/{settlementId}/release`       |

> 📘 Note:
> 
> - This API can only be used for orders with split settlements.
> - Use our <a href="https://developer.pluralonline.com/reference/orders-create" target="_blank">Create Orders API</a> to create a split settlement order.
