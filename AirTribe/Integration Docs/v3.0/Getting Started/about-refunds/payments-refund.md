---
title: "Create Refund"
slug: "payments-refund"
excerpt: "Use this API to initiate a refund against an order."
hidden: false
createdAt: "Tue Oct 15 2024 08:11:50 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon May 19 2025 07:33:05 GMT+0000 (Coordinated Universal Time)"
---
> 📘 Note:
> 
> - For a full refund, all IMEI numbers associated with the products are automatically blocked. For a partial refund, you must specify the IMEI number that needs to be blocked.

## Environment

Use our UAT environment endpoint for testing and for integration utilize our production endpoint.

| Environment                   | Endpoints                                                      |
| :---------------------------- | :------------------------------------------------------------- |
| User Acceptance Testing [UAT] | `https://pluraluat.v2.pinepg.in/api/pay/v1/refunds/{order_id}` |
| Production [PROD]             | `https://api.pluralpay.in/api/pay/v1/refunds/{order_id}`       |
