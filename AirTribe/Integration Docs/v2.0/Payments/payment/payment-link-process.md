---
title: "Process Payment"
slug: "payment-link-process"
excerpt: "Use this API to generate a payment link and process the payment."
hidden: false
createdAt: "Tue Sep 17 2024 07:03:28 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jan 21 2025 09:12:44 GMT+0000 (Coordinated Universal Time)"
---
## Environment

Use our UAT environment endpoint for testing and for integration utilize our production endpoint.

| Environment                   | Endpoint                                       |
| :---------------------------- | :--------------------------------------------- |
| User Acceptance Testing [UAT] | `https://uat.pinepg.in/api/v2/process/payment` |
| Production [PROD]             | `https://pinepg.in/api/v2/process/payment`     |

> 📘 Note:
> 
> - Ensure that the paymode passed in the Accept Payment API is the same as the one used in the Process Payment request payload.
> - Use the generated link returned in our Generate Payment Link API to navigate your customers to the seamless checkout page to accept payment.
