---
title: "Object"
slug: "tpv-objects"
excerpt: "Overview of Plural TPV APIs response."
hidden: true
createdAt: "Thu Nov 14 2024 10:42:42 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Nov 14 2024 12:17:34 GMT+0000 (Coordinated Universal Time)"
---
Shown below is a sample response returned for our Orders APIs against a TPV payment.

```json Orders Object
{
  "order_id": "v1-5757575757-aa-hU1rUd",
  "merchant_order_reference": "82d57572-057c-4826-5775-385a52150554",
  "type": "CHARGE",
  "status": "CREATED",
  "order_amount": {
    "value": 100,
    "currency": "INR"
  },
  "pre_auth": true,
  "purchase_details": {
    "account_details": {
      "bank_details": {
        "account_number": "103101532234",
        "ifsc_code": "",
        "bank_name": ""
      }
    },
    "customer": {
      "email_id": "kevin.bob@example.com",
      "first_name": "Kevin",
      "last_name": "Bob",
      "customer_id": "192212",
      "mobile_number": "9876543210",
      "billing_address": {
        "address1": "H.No 15, Sector 17",
        "address2": "",
        "address3": "",
        "pincode": "61232112",
        "city": "CHANDIGARH",
        "state": "PUNJAB",
        "country": "INDIA"
      },
      "shipping_address": {
        "address1": "H.No 15, Sector 17",
        "address2": "",
        "address3": "",
        "pincode": "144001123",
        "city": "CHANDIGARH",
        "state": "PUNJAB",
        "country": "INDIA"
      }
    },
    "merchant_metadata": {
      "key1": "DD",
      "key2": "XOF"
    }
  },
  "created_at": "2024-11-08T06:53:17.603070Z",
  "updated_at": "2024-11-08T06:53:17.603085Z"
}
```

The table below lists the various parameters returned in the orders response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "order_id",
    "0-1": "`string`",
    "0-2": "Unique identifier of the order in the Plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `v1-5757575757-aa-hU1rUd`",
    "1-0": "merchant_order_reference",
    "1-1": "`string`",
    "1-2": "Unique identifier entered while creating a order.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `82d57572-057c-4826-5775-385a52150554`",
    "2-0": "type",
    "2-1": "`string`",
    "2-2": "Payment type.  \n  \nPossible values:<ul><li>`CHARGE`</li><li>`REFUND`</ul></li>",
    "3-0": "status",
    "3-1": "`string`",
    "3-2": "Order status.<br><br>Possible values:<ul><li>`CREATED`: When the order is successfully created.</li><li>`PENDING`: When the order is linked against a payment request.</li><li>`PROCESSED`: When the payment is received successfully.</li><li>`AUTHORIZED`: **Only when `pre_auth` is `true`**. When the payment is ready for authorization.</li><li>`CANCELLED`: When the payment gets cancelled.</li><li>`ATTEMPTED`: When the payment is unsuccessful due to incorrect OTP. You can retry OTP verification until the payment gets failed.</li><li>`FAILED`: Payment acceptance failed for reasons such as cancel transactions, maximum retries for OTP verification etc.</li><li>`FULLY_REFUNDED`: When the payment is completely refunded.</li><li>`PARTIALLY_REFUNDED`: When the partial refund is successful.</ul></li>",
    "4-0": "challenge_url",
    "4-1": "`string`",
    "4-2": "Use the generated `challenge_url` to accept payment.<br><br>**Note**: This parameter is returned only after the payment is linked against the `order_id`.",
    "5-0": "merchant_id",
    "5-1": "`string`",
    "5-2": "Unique identifier of the merchant in the Plural database.  \n  \nExample: `123456`",
    "6-0": "order_amount",
    "6-1": "`object`",
    "6-2": "An object that contains the transaction amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/tpv-objects#order-amount-child-object\" >Learn more about the `order_amount` child object.</a>",
    "7-0": "notes",
    "7-1": "`string`",
    "7-2": "The note you want to show against an order.  \n  \nExample: `Electricity Bill`",
    "8-0": "pre_auth",
    "8-1": "`boolean`",
    "8-2": "The pre-authorization type.  \n  \nPossible values:<ul><li>`true`: When pre-authorization is needed.</li><li>`false`: When pre-authorization is not required.</ul></li>Example: `false`<br><br><a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders\" target=\"_block\">Learn more about our pre authorization</a>.",
    "9-0": "purchase_details",
    "9-1": "`object`",
    "9-2": "An object that contains the purchase details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/tpv-objects#purchase-details-child-object\" >Learn more about the `purchase_details` child object.</a><br><br>**Note**: The presence of the object key-values depends on the Input request.",
    "10-0": "payments",
    "10-1": "`array of objects`",
    "10-2": "An array of objects that contains the payment details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders-object#payments-child-object\" >Learn more about the `payments` child object.</a><br><br>**Note**: Payment object is returned only for the orders linked with a payment.",
    "11-0": "created_at",
    "11-1": "`string`",
    "11-2": "The ISO 8601 UTC Timestamp, when the create order request was received by Plural.  \n  \nExample: `2024-07-09T07:57:08.022056Z`",
    "12-0": "updated_at",
    "12-1": "`string`",
    "12-2": "The ISO 8601 UTC Timestamp, when the order object is updated.  \n  \nExample: `2024-07-09T07:57:08.022065Z`"
  },
  "cols": 3,
  "rows": 13,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Order Amount [Child Object]

The table below lists the various parameters in the `order_amount` child object. This object is part of the orders sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value",
    "0-1": "`integer`",
    "0-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`",
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


## Purchase Details [Child Object]

The table below lists the various parameters in the `purchase_details` child object. This object is part of the orders sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "account_details",
    "0-1": "`object`",
    "0-2": "An object that contains the account details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders-object#customer-child-object\" >Learn more about the `account_details` child object</a>.",
    "1-0": "customer",
    "1-1": "`object`",
    "1-2": "An object that contains the customer details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders-object#customer-child-object\" >Learn more about the `customer` child object</a>.",
    "2-0": "merchant_metadata",
    "2-1": "`object`",
    "2-2": "An object of key-value pair that can be used to store additional information.  \n  \nExample: `\"key1\": \"DD\"`"
  },
  "cols": 3,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Bank Details [Child Object]

The table below lists the various parameters in the `bank_details` child object. This is part of the `purchase_details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "bank_details",
    "0-1": "`object`",
    "0-2": "An object that contains the bank account details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders-object#customer-child-object\" >Learn more about the `bank_details` child object</a>."
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Bank Details [Child Object]

The table below lists the various parameters in the `bank_details` child object. This is part of the `account_details` object.

### Customer [Child Object]

The table below lists the various parameters in the `customer` child object. This is part of the `purchase_details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "email_id",
    "0-1": "`string`",
    "0-2": "Customer's email address.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `kevin.bob@example.com`",
    "1-0": "first_name",
    "1-1": "`string`",
    "1-2": "Customer's first name.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `Kevin`",
    "2-0": "last_name",
    "2-1": "`string`",
    "2-2": "Customer's last name.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `Bob`",
    "3-0": "customer_id",
    "3-1": "`string`",
    "3-2": "Unique identifier of the customer in the Plural database.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 19 characters.</ul></li>Example: `123456`",
    "4-0": "mobile_number",
    "4-1": "`string`",
    "4-2": "Customer's mobile number.<br><ul><li>Minimum length: 9 character.</li><li>Maximum length: 20 characters.</ul></li>Example: `9876543210`<br><br>Supported characters: <ul><li>`0-9`</li><li>`+`</ul></li>",
    "5-0": "billing_address",
    "5-1": "`object`",
    "5-2": "An object that contains the details of the billing address.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders-object#billing-address-child-object\" >Learn more about the `billing_address` child object.</a>",
    "6-0": "shipping_address",
    "6-1": "`object`",
    "6-2": "An object that contains the shipping address details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders-object#shipping-address-child-object\" >Learn more about the `shipping_address` child object.</a>"
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


#### Billing Address [Child Object]

The table below lists the various parameters in the `billing_address` child object. This is part of the `customer` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "address1",
    "0-1": "`string`",
    "0-2": "Customer's billing address1.<br><ul><li>Maximum length: 100 characters.</ul></li>Example: `10 Downing Street Westminster London`",
    "1-0": "address2",
    "1-1": "`string`",
    "1-2": "Customer's billing address2.<br><ul><li>Maximum length: 100 characters.</ul></li>Example: `Oxford Street Westminster London`",
    "2-0": "address3",
    "2-1": "`string`",
    "2-2": "Customer's billing address3.<br><ul><li>Maximum length: 100 characters.</ul></li>Example: `Baker Street Westminster London`",
    "3-0": "pincode",
    "3-1": "`string`",
    "3-2": "Pincode of the billing address.<ul><li>Minimum length: 6 characters.</li><li>Maximum length: 10 characters.</ul></li>Example: `51524036`<br><br>Supported characters: <ul><li>`0-9`</ul></li>",
    "4-0": "city",
    "4-1": "`string`",
    "4-2": "City of the billing address.<br><ul><li>Maximum length: 50 characters.</ul></li>Example: `Westminster`",
    "5-0": "state",
    "5-1": "`string`",
    "5-2": "State of the billing address.<br><ul><li>Maximum length: 50 characters.</ul></li>Example: `Westminster`",
    "6-0": "country",
    "6-1": "`string`",
    "6-2": "Country of the billing address.<br><ul><li>Maximum length: 50 characters.</ul></li>Example: `London`"
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


#### Shipping Address [Child Object]

The table below lists the various parameters in the `shipping_address` child object. This is part of the `customer` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "address1",
    "0-1": "`string`",
    "0-2": "Customer's shipping address1.<br><ul><li>Maximum length: 100 characters.</ul></li>Example: `10 Downing Street Westminster London`",
    "1-0": "address2",
    "1-1": "`string`",
    "1-2": "Customer's shipping address2.<br><ul><li>Maximum length: 100 characters.</ul></li>Example: `Oxford Street Westminster London`",
    "2-0": "address3",
    "2-1": "`string`",
    "2-2": "Customer's shipping address3.<br><ul><li>Maximum length: 100 characters.</ul></li>Example: `Baker Street Westminster London`",
    "3-0": "pincode",
    "3-1": "`string`",
    "3-2": "Pincode of the shipping address.<ul><li>Minimum length: 6 characters.</li><li>Maximum length: 10 characters.</ul></li>Example: `51524036`<br><br>Supported characters: <ul><li>`0-9`</ul></li>",
    "4-0": "city",
    "4-1": "`string`",
    "4-2": "City of the shipping address.<br><ul><li>Maximum length: 50 characters.</ul></li>Example: `Westminster`",
    "5-0": "state",
    "5-1": "`string`",
    "5-2": "State of the shipping address.<br><ul><li>Maximum length: 50 characters.</ul></li>Example: `Westminster`",
    "6-0": "country",
    "6-1": "`string`",
    "6-2": "Country of the shipping address.<br><ul><li>Maximum length: 50 characters.</ul></li>Example: `London`"
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
