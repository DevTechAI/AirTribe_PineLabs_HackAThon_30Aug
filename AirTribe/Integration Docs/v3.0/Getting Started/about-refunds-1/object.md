---
title: "Object"
slug: "object"
excerpt: "Overview of the refunds response object."
hidden: true
createdAt: "Thu Sep 12 2024 15:49:45 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Oct 16 2024 12:55:25 GMT+0000 (Coordinated Universal Time)"
---
Shown below is a sample responses of a Create Refund API.

```json Refund Sample Response
{
  "data": {
    "order_id": "v1-5757575757-aa-hU1rUd",
    "refunds": [
      {
        "merchant_refund_reference": "23242324232423",
        "refund_id": "v1-3314042524-ga-0Y129h",
        "status": "PROCESSED",
        "merchant_id": "123456",
        "refund_amount": {
          "value": 1100,
          "currency": "INR"
        },
        "created_at": "2024-04-30T08:01:32Z",
        "updated_at": "2024-04-30T08:01:32Z"
      }
    ]
  }
}
```

The table below lists the various parameters returned in the refund response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "order_id",
    "0-1": "`string`",
    "0-2": "Unique identifier of the order in the Plural database.  \n  \nExample: `v1-5757575757-aa-hU1rUd`",
    "1-0": "refunds",
    "1-1": "`object`",
    "1-2": "An object that contains the refund details.  \n  \n<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#refunds-child-object\" >Learn more about our `refunds` child object</a>."
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Refunds [Child Object]

The table below lists the various parameters in the `refunds` child object. This object is part of the `refunds sample response` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant_refund_reference",
    "0-1": "`string`",
    "0-2": "Merchant unique identifier for the refund reference.<ul><li>Maximum length: 50 characters.</li><li>Minimum length: 1 characters.</ul></li>Example: `23242324232423`",
    "1-0": "refund_id",
    "1-1": "`string`",
    "1-2": "Unique identifier of the refund in the Plural database.  \n  \nExample: `v1-3314042524-ga-0Y129h`",
    "2-0": "status",
    "2-1": "`string`",
    "2-2": "Refund statuses.<br><br>Possible values:<ul><li>`CREATED`: When the refund is successfully created.</li><li>`PENDING`: We have processed the refund and waiting for the response from the acquirer.</li><li>`PROCESSED`: When the refund is successful.</li><li>`FAILED`: When the refund gets failed this could be for many reasons such refund time expiry etc.</ul></li>",
    "3-0": "merchant_id",
    "3-1": "`string`",
    "3-2": "Unique identifier of the merchant in the Plural database.  \n  \nExample: `123456`",
    "4-0": "refund_amount",
    "4-1": "`object`",
    "4-2": "An object that contains the refund amount details.  \n  \n<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#refund-amount-child-object\" >Learn more about our `refund_amount` child object</a>.",
    "5-0": "created_at",
    "5-1": "`string`",
    "5-2": "Unix timestamp when the create refund request was received by Plural.  \n  \nExample: `2024-07-09T07:57:08.022056Z`",
    "6-0": "updated_at",
    "6-1": "`string`",
    "6-2": "Unix timestamp when the refund response object is updated.  \n  \nExample: `2024-07-09T07:57:08.022065Z`"
  },
  "cols": 3,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Refund Amount [Child Object]

The table below lists the various parameters in the `refund_amount` child object. This object is part of the `refunds` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value",
    "0-1": "`integer`",
    "0-2": "Refund amount is Paisa.<ul><li>Minimum value: `100` (₹1).</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
    "1-0": "currency",
    "1-1": "`string`",
    "1-2": "Type of currency.  \n  \nExample: `INR`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]
