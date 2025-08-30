---
title: "Token's payment processing(Plural/Non Plural token requester)"
slug: "tokens-payment-processingpluralnon-plural-roken-requester"
excerpt: ""
hidden: true
createdAt: "Mon Jul 11 2022 12:40:58 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:54:16 GMT+0000 (Coordinated Universal Time)"
---
**Request Body** 

[block:parameters]
{
  "data": {
    "h-0": "Parameter Name",
    "h-1": "Fields",
    "h-2": "Type",
    "h-3": "Length",
    "h-4": "Description(M/O))",
    "0-0": "tokenize_card_data",
    "0-1": "",
    "0-2": "Complex object type",
    "0-3": "",
    "0-4": "",
    "1-0": "",
    "1-1": "token",
    "1-2": "string",
    "1-3": "",
    "1-4": "C- (Mandatory In case Merchant integrated token provisioning system other then Plural)",
    "2-0": "",
    "2-1": "cryptogram",
    "2-2": "string",
    "2-3": "",
    "2-4": "C- (Mandatory In case Merchant integrated token provisioning system other then Plural)",
    "3-0": "",
    "3-1": "expiration_month",
    "3-2": "string",
    "3-3": "Expiry month of Card. Like- 12, 08,01",
    "3-4": "M",
    "4-0": "",
    "4-1": "expiration_year",
    "4-2": "string",
    "4-3": "Expiry year of card. Like - 2024, 2025",
    "4-4": "M",
    "5-0": "",
    "5-1": "pine_token_identifier",
    "5-2": "string",
    "5-3": "Unique non-guessable Guid by using unique key generation algorithm (OpenJDK8 - Java.util.UUID – version 1 based on timestamp – 36 characters)/  \ncustom DB sequence Logic for each token reference.",
    "5-4": "C -( Mandatory In case Merchant integrated token provisioning via Plural only)",
    "6-0": "",
    "6-1": "cvv",
    "6-2": "string",
    "6-3": "Card verfication value",
    "6-4": "M",
    "7-0": "customer_data",
    "7-1": "",
    "7-2": "Complex object type",
    "7-3": "",
    "7-4": "O",
    "8-0": "",
    "8-1": "mobile_no",
    "8-2": "string",
    "8-3": "10 digits Customer mobile number",
    "8-4": "O",
    "9-0": "",
    "9-1": "email_id",
    "9-2": "string",
    "9-3": "Customer email id",
    "9-4": "O",
    "10-0": "",
    "10-1": "country_code",
    "10-2": "string",
    "10-3": "Country code of Indian country- 91",
    "10-4": "O",
    "11-0": "card_meta_data",
    "11-1": "",
    "11-2": "Complex object type",
    "11-3": "",
    "11-4": "O - This complex type parameter is optional",
    "12-0": "",
    "12-1": "issuer_name",
    "12-2": "string",
    "12-3": "",
    "12-4": "O",
    "13-0": "",
    "13-1": "scheme_name",
    "13-2": "string",
    "13-3": "",
    "13-4": "O",
    "14-0": "",
    "14-1": "card_type",
    "14-2": "string",
    "14-3": "",
    "14-4": "O"
  },
  "cols": 5,
  "rows": 15,
  "align": [
    "left",
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


**Response Body** 

| Parameter Name   | Type   | Description                                                                                                                                                             | M/O |
| :--------------- | :----- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-- |
| content          | string | HTML  form received from card host which browser will be render to get OTP authencation viewYespayment_idlongPlural unique transaction idYesorder_idlongPlural order id | M   |
| payment_id       | long   | Unique payment id.                                                                                                                                                      | M   |
| order_id         | long   | Unique order id.                                                                                                                                                        | M   |
| amount_in_paise  | long   | Amount paid in paise.                                                                                                                                                   | M   |
| response_code    | string | Response code.                                                                                                                                                          | M   |
| response_message | string | Short message about code.                                                                                                                                               | M   |

**Failure Response Body** 

[block:parameters]
{
  "data": {
    "h-0": "Parameter Name",
    "h-1": "Type",
    "h-2": "Description",
    "h-3": "M/O",
    "0-0": "response_code",
    "0-1": "int",
    "0-2": "Failure case approriate response code  like 6010,6020",
    "0-3": "M",
    "1-0": "response_message",
    "1-1": "string",
    "1-2": "Proper response message  \nExample- \"Oops, something went wrong!\"",
    "1-3": "M"
  },
  "cols": 4,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]
