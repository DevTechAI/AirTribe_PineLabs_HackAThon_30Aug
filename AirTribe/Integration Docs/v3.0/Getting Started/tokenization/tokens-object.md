---
title: "Object"
slug: "tokens-object"
excerpt: "Overview of the token APIs response object."
hidden: false
createdAt: "Thu Feb 13 2025 07:17:07 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Mar 06 2025 14:56:08 GMT+0000 (Coordinated Universal Time)"
---
The table below lists the response objects received for the different Tokens APIs.

| Token API           |                       |
| :------------------ | :-------------------- |
| Generate Card Token | Card Token Object     |
| Generate Cryptogram | Cryptogram Object     |
| Get Customer Token  | Customer Token Object |
| Delete Token        | Delete Token Object   |

## Card Token Object

Shown below is a sample response returned through our Generate Card Token API.

```json Card Token Response Object
{
  "token_id": "token-v1-0811030624-aa-RBDgpR",
  "customer_id": "cust-786cdrexrt",
  "merchant_token_reference": "ec71b52e-c21f-4ac5-8624-385d6b6bdccc",
  "status": "ACTIVE",
  "created_at": "2024-10-04T13:11:29.645657Z",
  "updated_at": "2024-10-04T13:11:29.645657Z"
}
```

The table below lists the various parameters returned in the Generate Card Token API response.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "token_id",
    "0-1": "`string`",
    "0-2": "Unique identifier of the token in the Plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `token-v1-0811030624-aa-RBDgpR`",
    "1-0": "customer_id",
    "1-1": "`string`",
    "1-2": "Unique identifier of the customer in the Plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `cust-v1-0811030624-aa-RBDgpR`",
    "2-0": "merchant_token_reference",
    "2-1": "`string`",
    "2-2": "Unique identifier entered while creating a token.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `82d57572-057c-4826-5775-385a52150554`",
    "3-0": "status",
    "3-1": "`string`",
    "3-2": "Token status.<br><br>Possible values:<ul><li>`Initiated`: It's a token's initial state, indicating that Plural is working with token service providers to generate it.</li><li>`Active`: It's a token's active state, achieved when the service_provider_token status is marked as active by the network token service providers.</li><li>`Suspended`: The token status changes to suspended when it is not active for any token service provider or is marked as suspended by network token service providers.</li><li>`Failed`: The token status changes to failed if it is marked as failed by all service providers.</li><li>`Deactivated`:  The status will be deactivated if it is neither active nor suspended for all token service providers or if the token is deactivated by network token service providers.</ul></li>",
    "4-0": "created_at",
    "4-1": "`string`",
    "4-2": "The ISO 8601 UTC Timestamp, when the create token was received by Plural.  \n  \nExample: `2024-10-04T13:11:29.655592Z`",
    "5-0": "updated_at",
    "5-1": "`string`",
    "5-2": "The ISO 8601 UTC Timestamp, when the token is updated.  \n  \nExample: `2024-10-04T13:11:29.645657Z`"
  },
  "cols": 3,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Cryptogram

Shown below is a sample response returned through our Generate Cryptogram API.

```json Cryptogram Response Object
{
  "token_id": "token-v1-0811030624-aa-RBDgpR",
  "merchant_token_reference": "ec71b52e-c21f-4ac5-8624-385d6b6bdccc",
  "service_provider_token_id": "tp-v1-0811030624-aa-RBDgpR",
  "token_data": {
    "cryptogram": "/wAAAAAAl9SX1HsAmWKSgqwAAAA=",
    "token_reference": "sas7wqaoidasdfssdjjk",
    "payment_account_reference": "8324ssdas7wqaoidassdjjk",
    "token_expiry_month": 5,
    "token_expiry_year": 2030
  }
}
```

The table below lists the various parameters returned in the Generate Cryptogram API response.

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
    "2-0": "service_provider_token_id",
    "2-1": "`string`",
    "2-2": "Unique service provider reference in the Plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `tp-v1-0811030624-aa-RBDgpR`",
    "3-0": "token_data",
    "3-1": "`object`",
    "3-2": "An object that contains the token details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/tokens-object#token-data-child-object\" >Learn more about the `token_data` child object.</a>"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Token Data [Child Object]

The table below lists the various parameters in the `token_data` child object. This is part of the `cryptogram` response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "cryptogram",
    "0-1": "`string`",
    "0-2": "Dynamically generated encrypted value to authenticate and protect card-not-present (CNP) transactions.  \n  \nExample: `AFV5JWsTN01sAAPKVx01AAADFA==`",
    "1-0": "token_reference",
    "1-1": "`string`",
    "1-2": "Unique identifier entered while creating a token.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `82d57572-057c-4826-5775-385a52150554`",
    "2-0": "payment_account_reference",
    "2-1": "`string`",
    "2-2": "Unique identifier of a payment account which is independent of the card number.  \n  \nExample: `500167T12CBJM1WXT8C7WSENYDYSY`",
    "3-0": "token_expiry_month",
    "3-1": "`string`",
    "3-2": "The month when the payment token expires.  \n  \nExample: `02`",
    "4-0": "token_expiry_year",
    "4-1": "`string`",
    "4-2": "The year when the payment token expires.  \n  \nExample: `2025`"
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


## Customer Token

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
    "1-2": "An array of object that contains the token information details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/tokens-object#tokens-child-object\" >Learn more about the `tokens` child object.</a>"
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
    "2-2": "Token status.<br><br>Possible values:<ul><li>`Initiated`: It's a token's initial state, indicating that Plural is working with token service providers to generate it.</li><li>`Active`: It's a token's active state, achieved when the service_provider_token status is marked as active by the network token service providers.</li><li>`Suspended`: The token status changes to suspended when it is not active for any token service provider or is marked as suspended by network token service providers.</li><li>`Failed`: The token status changes to failed if it is marked as failed by all service providers.</li><li>`Deactivated`:  The status will be deactivated if it is neither active nor suspended for all token service providers or if the token is deactivated by network token service providers.</ul></li>",
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
    "7-1": "`string`",
    "7-2": "Reason corresponding to the payment token status.  \n  \nExample: `payment token expired`",
    "8-0": "merchant_metadata",
    "8-1": "`object`",
    "8-2": "An object of key-value pair that can be used to store additional information.  \n  \nExample: \"key1\": \"DD\"",
    "9-0": "card_data",
    "9-1": "`object`",
    "9-2": "An object that contains the card details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/tokens-object#card-data-child-object\" >Learn more about the `card_data` child object.</a>",
    "10-0": "is_compliant",
    "10-1": "`boolean`",
    "10-2": "Status of the token compliant as per Reserve Bank Of India (RBI) regulations.  \n  \nExample: `true`"
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


#### Card Data [Child Object]

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
    "6-2": "International transaction support status.  \n  \nPossible values:<ul><li>`true`: Supports international transaction.</li><li>`false`: Do not support international transactions.</ul></li>",
    "7-0": "emi",
    "7-1": "`boolean`",
    "7-2": "EMI Transaction support status.  \n  \nPossible values:<ul><li>`true`: Supports EMI transactions.</li><li>`false`: Do not support EMI transactions.</ul></li>",
    "8-0": "cvv_required",
    "8-1": "`boolean`",
    "8-2": "Is CVV required for the transaction.  \n  \nPossible values:<ul><li>`true`: CVV is required for the transaction.</li><li>`false`: CVV is not required for the transaction.</ul></li>"
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


## Delete Token

Shown below is a sample response returned through our Delete Token API.

```json Delete Token Response Object
{
  "customer_id": "cust-786cdrexrt",
  "token-id": "ec71b52e-c21f-4ac5-8624-385d6b6bdccc",
  "status": "DELETED",
  "merchant_unique_reference": "dx98b63e-c74g-5ac4-632e-346d6c7bdwka"
}
```

The table below lists the various parameters returned in the Delete Token API response.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "token_id",
    "0-1": "`string`",
    "0-2": "Unique identifier of the token in the Plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: \\`ec71b52e-c21f-4ac5-8624-385d6b6bdccc",
    "1-0": "customer_id",
    "1-1": "`string`",
    "1-2": "Unique identifier of the customer in the Plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `cust-v1-0811030624-aa-RBDgpR`",
    "2-0": "merchant_token_reference",
    "2-1": "`string`",
    "2-2": "Unique identifier entered while creating a token.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `82d57572-057c-4826-5775-385a52150554`",
    "3-0": "status",
    "3-1": "`string`",
    "3-2": "Token status.<br><br>Possible values:<ul><li>`Initiated`: It's a token's initial state, indicating that Plural is working with token service providers to generate it.</li><li>`Active`: It's a token's active state, achieved when the service_provider_token status is marked as active by the network token service providers.</li><li>`Suspended`: The token status changes to suspended when it is not active for any token service provider or is marked as suspended by network token service providers.</li><li>`Failed`: The token status changes to failed if it is marked as failed by all service providers.</li><li>`Deactivated`:  The status will be deactivated if it is neither active nor suspended for all token service providers or if the token is deactivated by network token service providers.</ul></li>",
    "4-0": "created_at",
    "4-1": "`string`",
    "4-2": "The ISO 8601 UTC Timestamp, when the create token was received by Plural.  \n  \nExample: `2024-10-04T13:11:29.655592Z`",
    "5-0": "updated_at",
    "5-1": "`string`",
    "5-2": "The ISO 8601 UTC Timestamp, when the token is updated.  \n  \nExample: `2024-10-04T13:11:29.645657Z`"
  },
  "cols": 3,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]
