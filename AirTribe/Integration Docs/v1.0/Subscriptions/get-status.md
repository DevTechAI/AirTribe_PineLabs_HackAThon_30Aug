---
title: "Get Status"
slug: "get-status"
excerpt: ""
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Wed Jul 26 2023 10:29:46 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Jul 26 2023 11:44:48 GMT+0000 (Coordinated Universal Time)"
---
**Authorization**  
For Authorization use Basic Auth, where:

- _Username:_ Plural MerchantId
- _Password:_ Merchant Access token

**Query Parameters**  
At least one query parameter (from pluralTransactionId/transactionId/orderId) is required. 

[block:parameters]
{
  "data": {
    "h-0": "Parameter Name",
    "h-1": "Type",
    "h-2": "Description",
    "h-3": "",
    "h-4": "",
    "0-0": "pluralTransactionId",
    "0-1": "string",
    "0-2": "generated after successful process payment API execution",
    "0-3": "",
    "0-4": "",
    "1-0": "requestType",
    "1-1": "string",
    "1-2": "Request Type Enum",
    "1-3": "C/E/N/R",
    "1-4": "**C:** Create Mandate  \n**E:** Execute Mandate  \n**N: **Predebit Notification  \n**R:** Revoke Mandate",
    "2-0": "transactionId",
    "2-1": "string",
    "2-2": "Merchant Transaction Id, generated for each Create Mandate/ Execute Mandate/ Predebit Notification/ Revoke Mandate",
    "2-3": "",
    "2-4": "",
    "3-0": "orderId",
    "3-1": "string",
    "3-2": "OrderId is generated for each subscription.",
    "3-3": "",
    "3-4": ""
  },
  "cols": 5,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]
