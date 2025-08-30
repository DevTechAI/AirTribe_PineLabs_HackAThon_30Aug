---
title: "Process Payment via Card Token"
slug: "emi-process-payment-via-card-token"
excerpt: "Use this API to process a tokenized card payment."
hidden: false
createdAt: "Mon Nov 25 2024 07:53:51 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Jan 31 2025 08:53:58 GMT+0000 (Coordinated Universal Time)"
---
## Environment

Use our UAT environment endpoint for testing and for integration utilize our production endpoint.

| Environment                   | Endpoint                                                     |
| :---------------------------- | :----------------------------------------------------------- |
| User Acceptance Testing [UAT] | `https://uat.pinepg.in/api/v2/process/payment/card/tokenize` |
| Production [PROD]             | `https://pinepg.in/api/v2/process/payment/card/tokenize`     |

> 📘 Note:
> 
> - Ensure that the paymode passed in the Accept Payment API is the CARD.
> - Use the generated link returned in our Process Payment via Card Token API to navigate your customers to the seamless checkout page to accept payment.
> - In the case of a Rupay card, token provision and processing will be done with actual card details and not with Alt Token.
