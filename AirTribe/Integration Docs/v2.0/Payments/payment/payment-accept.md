---
title: "Accept Payment"
slug: "payment-accept"
excerpt: "Use this API to start accepting a payment."
hidden: false
createdAt: "Wed Aug 28 2024 11:58:58 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 20 2024 13:07:06 GMT+0000 (Coordinated Universal Time)"
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
