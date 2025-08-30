---
title: "Process Payment"
slug: "emi-process-payment"
excerpt: "Use this API to generate a payment link and process the payment."
hidden: false
createdAt: "Mon Nov 25 2024 07:44:20 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Jan 31 2025 07:10:41 GMT+0000 (Coordinated Universal Time)"
---
## Environment

Use our UAT environment endpoint for testing and for integration utilize our production endpoint.

| Environment                   | Endpoint                                       |
| :---------------------------- | :--------------------------------------------- |
| User Acceptance Testing [UAT] | `https://uat.pinepg.in/api/v2/process/payment` |
| Production [PROD]             | `https://pinepg.in/api/v2/process/payment`     |

> 📘 Note:
> 
> - Ensure that the paymode passed in the Accept Payment API is `CARD`.
