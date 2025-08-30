---
title: "Object"
slug: "customer-token-object"
excerpt: "Overview of the customer token response object."
hidden: true
createdAt: "Wed Feb 12 2025 10:20:05 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Feb 17 2025 08:09:15 GMT+0000 (Coordinated Universal Time)"
---
Shown below are the sample response returned through our customer token APIs.

```json Tokens Response Object
{
  "customer_id": "cust-v1-0811030624-aa-RBDgpR",
  "tokens": [
    {
      "token_id": "token-v1-0811030624-aa-RBDgpR",
      "merchant_token_reference": "",
      "status": "ACTIVE",
      "payment_method": "CARD",
      "expired_at": "2024-10-04T13:11:29.645591Z",
      "created_at": "2024-10-04T13:11:29.645591Z",
      "updated_at": "2024-10-04T13:11:29.645657Z",
      "status_reason": null,
      "merchant_metadata": {
        "key1": "XX",
        "key2": "DOF"
      },
      "card_data": {
        "last4_digit": "2363",
        "card_type": "CREDIT",
        "network_name": "VISA",
        "issuer_name": "HDFC",
        "card_category": "Consumer",
        "country_code": "IND",
        "international": false,
        "emi": true,
        "cvv_required": false
      },
      "is_compliant": true
    }
  ]
}
```

The table below lists the various parameters returned in the orders response objects.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "customer_id",
    "0-1": "`string`",
    "0-2": "Unique identifier of the customer in the Plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `cust-v1-0811030624-aa-RBDgpR`",
    "1-0": "tokens",
    "1-1": "`array of objects`",
    "1-2": "An array of object that contains the token information details."
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


### Tokens [Child Object]

The table below lists the various parameters in the `tokens` child object. This is part of the `tokens` response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "token_id",
    "0-1": "`string`",
    "0-2": "Unique identifier of the token in the Plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `token-v1-0811030624-aa-RBDgpR`",
    "1-0": "merchant_token_reference",
    "1-1": "`string`",
    "1-2": "Unique identifier entered while creating a token.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `82d57572-057c-4826-5775-385a52150554`",
    "2-0": "status",
    "2-1": "`string`",
    "2-2": "",
    "3-0": "payment_method",
    "3-1": "`string`",
    "3-2": "Type of payment method.  \n  \nAccepted values:<ul><li>`CARD`</li><li>`UPI`</li><li>`POINTS`</ul></li>Example: `CARD`",
    "4-0": "expired_at",
    "4-1": "`string`",
    "4-2": "The ISO 8601 UTC Timestamp, when the token get expired.  \n  \nExample: `2024-10-04T13:11:29.645591Z`",
    "5-0": "created_at",
    "5-1": "`string`",
    "5-2": "The ISO 8601 UTC Timestamp, when the create token was received by Plural.  \n  \nExample: `2024-10-04T13:11:29.655592Z`",
    "6-0": "updated_at",
    "6-1": "`string`",
    "6-2": "The ISO 8601 UTC Timestamp, when the token is updated.  \n  \nExample: `2024-10-04T13:11:29.645657Z`",
    "7-0": "status_reason",
    "7-1": "",
    "7-2": "",
    "8-0": "merchant_metadata",
    "8-1": "`object`",
    "8-2": "An object of key-value pair that can be used to store additional information.  \n  \nExample: \"key1\": \"DD\"",
    "9-0": "card_data",
    "9-1": "`object`",
    "9-2": "An object that contains the card details.",
    "10-0": "is_compliant",
    "10-1": "`boolean`",
    "10-2": ""
  },
  "cols": 3,
  "rows": 11,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Card Data [Child Object]

The table below lists the various parameters in the `card_data` child object. This is part of the `tokens` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "last4_digit",
    "0-1": "`string`",
    "0-2": "The last four digits of your card number.  \n  \nHas to be 4 digits.  \n  \nExample: `1234`  \n  \nSupported characters: `0-9`",
    "1-0": "card_type",
    "1-1": "`string`",
    "1-2": "Type of card.  \n  \nPossible values:<ul><li>`DEBIT`</li><li>`CREDIT`</ul></li>Example: `CREDIT`",
    "2-0": "network_name",
    "2-1": "`string`",
    "2-2": "Card network providers.  \n  \nExample: `VISA`",
    "3-0": "issuer_name",
    "3-1": "`string`",
    "3-2": "Card issuer entity.  \n  \nExample: `HDFC`",
    "4-0": "card_category",
    "4-1": "`string`",
    "4-2": "The card category type.  \n  \nPossible values:<ul><li>`CONSUMER`</li><li>`COMMERCIAL`</li><li>`PREMIUM`</li><li>`SUPER_PREMIUM`</li><li>`PLATINUM`</li><li>`OTHER`</li><li>`BUSINESS`</li><li>`GOVERNMENT_NOTES`</li><li>`PAYOUTS`</li><li>`ELITE`</li><li>`STANDARD`</ul></li>Example: `CONSUMER`",
    "5-0": "country_code",
    "5-1": "`string`",
    "5-2": "Card issuers Country.  \n  \nExample: `IND`",
    "6-0": "international",
    "6-1": "`boolean`",
    "6-2": "",
    "7-0": "emi",
    "7-1": "`boolean`",
    "7-2": "",
    "8-0": "cvv_required",
    "8-1": "`boolean`",
    "8-2": ""
  },
  "cols": 3,
  "rows": 9,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]
