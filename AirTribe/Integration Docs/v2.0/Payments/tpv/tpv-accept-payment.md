---
title: "Accept Payment"
slug: "tpv-accept-payment"
excerpt: "Use this API to accept a payment."
hidden: false
createdAt: "Mon Jun 24 2024 11:55:05 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Aug 22 2024 08:44:12 GMT+0000 (Coordinated Universal Time)"
---
> 📘 Note:
> 
> - Plural accept payment API use Base64 Encode as an input request. And uses HashMap secret to authorise the payment. To learn more about Base64 Encode and HashMap secret key generation <a href="https://developer.pluralonline.com/v2.0/reference/prerequisite" target="_blanck">refer to our Pre-requisite</a>.

## Environment

Use our UAT environment endpoint for testing and for integration utilize our production endpoint.

| Environment                   | Endpoint                                      |
| :---------------------------- | :-------------------------------------------- |
| User Acceptance Testing [UAT] | `https://uat.pinepg.in/api/v2/accept/payment` |
| Production [PROD]             | `https://pinepg.in/api/v2/accept/payment`     |
