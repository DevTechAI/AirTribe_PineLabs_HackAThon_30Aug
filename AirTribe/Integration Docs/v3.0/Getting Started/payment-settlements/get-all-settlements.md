---
title: "Get All Settlements"
slug: "get-all-settlements"
excerpt: "Use this API to fetch all the settlements against your account."
hidden: false
createdAt: "Thu Oct 24 2024 09:32:29 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Jan 08 2025 04:31:46 GMT+0000 (Coordinated Universal Time)"
---
## Environment

Use our UAT environment endpoint for testing and for integration utilize our production endpoint.

| Environment                   | Endpoints                                                 |
| :---------------------------- | :-------------------------------------------------------- |
| User Acceptance Testing [UAT] | `https://pluraluat.v2.pinepg.in//api/settlements/v1/list` |
| Production [PROD]             | `https://api.pluralpay.in/api/settlements/v1/list`        |

> 📘 Note:
> 
> 1. **Date Range**: Maximum date range for retrieving settlement data is 60 days.
> 2. **Page Size**: API supports a maximum of 10 records per page, one page at a time.
