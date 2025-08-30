---
title: "Card registration via tokenization"
slug: "getting-started-with-your-api-1"
excerpt: "When customer give consent for card provisioning in any case  of Iframe/Redirect & Seamless. Customer's consent would be a pass as Process Payment API request payload.\n\nFirst Time card tokenization- New is_card_to_be_saved field introduced which need to be pass with other card's details in Process payment API call. Card must be tokenized after successful capture transaction.\n\nNote: Merchant first need to call customer creation API along with customer activation process."
hidden: true
metadata: 
  image: []
  robots: "index"
createdAt: "Mon Jul 11 2022 10:08:57 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Oct 04 2022 14:38:21 GMT+0000 (Coordinated Universal Time)"
---
**Request Body** 

[block:parameters]
{
  "data": {
    "h-0": "Parameter Name",
    "h-1": "",
    "h-2": "Type",
    "h-3": "Description",
    "h-4": "M/O",
    "0-0": "card_data",
    "0-1": "",
    "0-2": "Complex type",
    "0-3": "",
    "0-4": "M",
    "1-0": "",
    "1-1": "card_number",
    "1-2": "string",
    "1-3": "16-19 digits card number",
    "1-4": "M",
    "2-0": "",
    "2-1": "card_expiry_month",
    "2-2": "string",
    "2-3": "Expiry month of Card",
    "2-4": "M",
    "3-0": "",
    "3-1": "card_expiry_year",
    "3-2": "string",
    "3-3": "Expiry year of card",
    "3-4": "M",
    "4-0": "",
    "4-1": "card_holder_name",
    "4-2": "string",
    "4-3": "Card holder name mentioned on card",
    "4-4": "o",
    "5-0": "",
    "5-1": "cvv",
    "5-2": "string",
    "5-3": "Card verification value",
    "5-4": "M",
    "6-0": "",
    "6-1": "is_card_to_be_saved",
    "6-2": "boolean",
    "6-3": "true/false",
    "6-4": "M -\"In case customer wants to tokenized card with us\".  \nvalue is true in case customer wants to tokenized card for future transactions via Plural",
    "7-0": "customer_data",
    "7-1": "",
    "7-2": "Complex type",
    "7-3": "",
    "7-4": "",
    "8-0": "",
    "8-1": "customer_token",
    "8-2": "string",
    "8-3": "Customer tokan generated on customer creation  \nValue like - vQ7ssVqGlcfEUpGdzycwnQ",
    "8-4": "M-\"In case customer wants to tokenize card with us then customer token is mandatory field\"",
    "9-0": "",
    "9-1": "mobile_no",
    "9-2": "string",
    "9-3": "10 digits Customer mobile number",
    "9-4": "O",
    "10-0": "",
    "10-1": "country_code",
    "10-2": "string",
    "10-3": "Country code for India is 91",
    "10-4": "O",
    "11-0": "",
    "11-1": "email_id",
    "11-2": "string",
    "11-3": "Customer email id",
    "11-4": "O"
  },
  "cols": 5,
  "rows": 12,
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

[block:parameters]
{
  "data": {
    "h-0": "Parameter Name",
    "h-1": "Type",
    "h-2": "Description",
    "h-3": "M/O",
    "0-0": "content",
    "0-1": "string",
    "0-2": "HTML form received from card host which browser will be render to get OTP authencation view",
    "0-3": "M",
    "1-0": "payment_id",
    "1-1": "long",
    "1-2": "Unique payment id.",
    "1-3": "M",
    "2-0": "order_id",
    "2-1": "long",
    "2-2": "Unique order id.",
    "2-3": "M",
    "3-0": "amount_in_paise",
    "3-1": "long",
    "3-2": "Amount paid in paise.",
    "3-3": "M",
    "4-0": "response_code",
    "4-1": "string",
    "4-2": "Success value is 1  \nFailure case approriate response code  like 6010,6020",
    "4-3": "M",
    "5-0": "response_message",
    "5-1": "string",
    "5-2": "Short message about code.",
    "5-3": "M"
  },
  "cols": 4,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]
