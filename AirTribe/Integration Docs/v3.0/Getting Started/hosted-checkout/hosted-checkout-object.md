---
title: "Object"
slug: "hosted-checkout-object"
excerpt: "Overview of the hosted checkout API response object."
hidden: false
createdAt: "Fri Sep 13 2024 08:08:19 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 20 2024 10:37:50 GMT+0000 (Coordinated Universal Time)"
---
Shown below is a sample responses of a Hosted Checkout API.

```json Generate Checkout Link Sample Response
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
  "order_id": "v1-5757575757-aa-hU1rUd",
  "redirect_url": "https://api.pluralonline.com/api/v3/checkout-bff/redirect/checkout?token=<<Redirect Token>>",
  "response_code": 200,
  "response_message": "Order Creation Successful."
}
```

The table below lists the various parameters returned in the Hosted checkout response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "token",
    "0-1": "`string`",
    "0-2": "Token generate by our system for Plural Hosted Checkout.  \n  \nExample: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`",
    "1-0": "order_id",
    "1-1": "`string`",
    "1-2": "Unique identifier of the order in the Plural database.  \n  \nExample: `v1-5757575757-aa-hU1rUd`",
    "2-0": "redirect_url",
    "2-1": "`string`",
    "2-2": "The checkout link generate on our system.  \n  \nExample: `<https://api.pluralonline.com/api/v3/checkout-bff/redirect/checkout?token=><<Redirect Token>`",
    "3-0": "response_code",
    "3-1": "`integer`",
    "3-2": "Response code of the request.  \n  \nExample: `200`",
    "4-0": "response_message",
    "4-1": "`string`",
    "4-2": "Corresponding message to the response code.  \n  \nExample: `Order Creation Successful`"
  },
  "cols": 3,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]
