---
title: "Object"
slug: "card-payments-object"
excerpt: "Overview of the card payment response object."
hidden: false
createdAt: "Thu Sep 12 2024 09:02:40 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed May 28 2025 11:16:16 GMT+0000 (Coordinated Universal Time)"
---
The table below lists the response objects received for the different Card Payment APIs.

[block:parameters]
{
  "data": {
    "h-0": "Token API",
    "h-1": "",
    "0-0": "Create Card Payment",
    "0-1": "<a href=\"https://developer.pluralonline.com/reference/card-payments-object#card-payment-response-object\" >Card Payment Response Object</a>",
    "1-0": "Generate OTP",
    "1-1": "<a href=\"https://developer.pluralonline.com/reference/card-payments-object#otp-response-objects\" >OTP Response Objects</a>",
    "2-0": "Resend OTP",
    "2-1": "<a href=\"https://developer.pluralonline.com/reference/card-payments-object#otp-response-objects\" >OTP Response Objects</a>",
    "3-0": "Submit OTP",
    "3-1": "<a href=\"https://developer.pluralonline.com/reference/card-payments-object#otp-response-objects\" >OTP Response Objects</a>",
    "4-0": "Get Card Details",
    "4-1": "<a href=\"https://developer.pluralonline.com/reference/card-payments-object#get-card-details-response-object\" >Get Card Details Response Object</a>"
  },
  "cols": 2,
  "rows": 5,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Card Payment Response Object

Shown below are the sample responses returned through our Create Payments API when the payment method is `CARD`.

```json Card Payment Object
{
  "data": {
    "order_id": "v1-5206071124-aa-mpLhF3",
    "merchant_order_reference": "0342ef1e-4606-4c11-8640-705f4d415b6d",
    "type": "CHARGE",
    "status": "PROCESSED",
    "challenge_url": "https://api.pluralpay.in/web/auth/landing/?token=S50xnInJvpcftOzmuGWUqnLpIe694YPGJiKL%2FdBh5Yl%2Bwb8giJrl6HoTvcKljRVZa3H",
    "merchant_id": "104359",
    "order_amount": {
      "value": 1000,
      "currency": "INR"
    },
    "pre_auth": false,
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],    
    "notes": "order1",
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "123456",
        "mobile_number": "9876543210",
        "billing_address": {
          "address1": "10 Downing Street Westminster London",
          "address2": "Oxford Street Westminster London",
          "address3": "Baker Street Westminster London",
          "pincode": "51524036",
          "city": "Westminster",
          "state": "Westminster",
          "country": "London"
        },
        "shipping_address": {
          "address1": "10 Downing Street Westminster London",
          "address2": "Oxford Street Westminster London",
          "address3": "Baker Street Westminster London",
          "pincode": "51524036",
          "city": "Westminster",
          "state": "Westminster",
          "country": "London"
        }
      },
      "merchant_metadata": {
        "key1": "value1",
        "key2": "value2"
      }
    },
    "payments": [
      {
        "id": "v1-5206071124-aa-mpLhF3-cc-l",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 1000,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "MASTERCARD",
            "issuer_name": "HDFC",
            "card_category": "NONE",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN",
            "last4_digit": "1091",
            "save": false,
            "is_native_otp_eligible": true
          }
        },
        "acquirer_data": {
          "approval_code": "030376",
          "acquirer_reference": "202455840588334",
          "rrn": "419335023601",
          "is_aggregator": true
        },
        "created_at": "2024-07-11T06:52:12.484Z",
        "updated_at": "2024-07-11T06:59:38.260Z"
      }
    ],
    "created_at": "2024-07-11T06:52:12.484Z",
    "updated_at": "2024-07-11T06:59:38.260Z"
  }
}
```
```json Tokenized Card Payment Object
{
  "data": {
    "order_id": "v1-5206071124-aa-mpLhF3",
    "merchant_order_reference": "0342ef1e-4606-4c11-8640-705f4d415b6d",
    "type": "CHARGE",
    "status": "PROCESSED",
    "challenge_url": "https://api.pluralpay.in/web/auth/landing/?token=S50xnInJvpcftOzmuGWUqnLpIe694YPGJiKL%2FdBh5Yl%2Bwb8giJrl6HoTvcKljRVZa3H",
    "merchant_id": "104359",
    "order_amount": {
      "value": 1000,
      "currency": "INR"
    },
    "pre_auth": false,
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],    
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "123456",
        "mobile_number": "9876543210",
        "billing_address": {
          "address1": "10 Downing Street Westminster London",
          "address2": "Oxford Street Westminster London",
          "address3": "Baker Street Westminster London",
          "pincode": "51524036",
          "city": "Westminster",
          "state": "Westminster",
          "country": "London"
        },
        "shipping_address": {
          "address1": "10 Downing Street Westminster London",
          "address2": "Oxford Street Westminster London",
          "address3": "Baker Street Westminster London",
          "pincode": "51524036",
          "city": "Westminster",
          "state": "Westminster",
          "country": "London"
        }
      },
      "merchant_metadata": {
        "key1": "value1",
        "key2": "value2"
      }
    },
    "payments": [
      {
        "id": "v1-5206071124-aa-mpLhF3-cc-l",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 1000,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_token_details": {
            "name": "Test",
            "last4_digit": "1091",
            "cvv": "123",
            "expiry_month": "01",
            "expiry_year": "2026",
            "token": "4000000000001091",
            "cryptogram": "wAAAAAAl9SX1HsAmWKSgqwAAAA",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "030376",
          "acquirer_reference": "202455840588334",
          "rrn": "419335023601",
          "is_aggregator": true
        },
        "created_at": "2024-07-11T06:52:12.484Z",
        "updated_at": "2024-07-11T06:59:38.260Z"
      }
    ],
    "created_at": "2024-07-11T06:52:12.484Z",
    "updated_at": "2024-07-11T06:59:38.260Z"
  }
}
```

The table below lists the various parameters returned in the payments response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "order_id",
    "0-1": "`string`",
    "0-2": "Unique identifier of the order in the Plural database.  \n  \nExample: `v1-5757575757-aa-hU1rUd`",
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
    "4-2": "Use the generated `challenge_url` URL to navigate your users the checkout page.",
    "5-0": "merchant_id",
    "5-1": "`string`",
    "5-2": "Unique identifier of the merchant in Plural database.  \n  \nExample: `123456`",
    "6-0": "order_amount",
    "6-1": "`object`",
    "6-2": "An object that contains the transaction amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/card-payments-object#order-amount-child-object\" >Learn more about our `order_amount` child object</a>.",
    "7-0": "pre_auth",
    "7-1": "`boolean`",
    "7-2": "The pre-authorization type.<br><br>Possible values:<ul><li>`true`: When pre-authorization is needed.</li><li>`false`: When pre-authorization is not required.</ul></li>Example: `false`<br><br><a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders\" target=\"_blanck\">Learn more about our pre-authorization.</a>.",
    "8-0": "allowed_payment_methods",
    "8-1": "`array of strings`",
    "8-2": "The type of payment methods you want to offer your customers to accept payments.  \n  \nAccepted values:<ul><li>`CARD`</li><li>`UPI`</li><li>`POINTS`</li><li>`NETBANKING`</li><li>`WALLET`</ul></li>Example: `CARD`  \n  \n**Note**: Before selecting a payment method, ensure it is configured for you.",
    "9-0": "notes",
    "9-1": "`string`",
    "9-2": "The note you want to show against an order.  \n  \nExample: `Order1`",
    "10-0": "callback_url",
    "10-1": "`string`",
    "10-2": "Use this URL to redirect your customers to specific success or failure pages based on the order or product details.  \n  \nExample: `https://sample-callback-url`",
    "11-0": "failure_callback_url",
    "11-1": "`string`",
    "11-2": "The URL specifically used to redirect customers to a failure page based on the order or product details.  \n  \nExample: `https://sample-failure-callback-url`  \n  \n**Note**:<ul><li>If the `failure_callback_url` is not provided, customers will be redirected to the `callback_url` for both successful and failed transactions.</li><li>If the `failure_callback_url` is provided, the `callback_url` will be used exclusively for successful transactions, while the `failure_callback_url` will be used for failed transactions.</li><li>If neither URL is provided, the default URL configured during merchant onboarding will be used.</ul></li>",
    "12-0": "purchase_details",
    "12-1": "`object`",
    "12-2": "An object that contains the purchase details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/card-payments-object#purchase-details-child-object\" >Learn more about our `purchase_details` child object</a>.  \n  \n**Note**: The presence of the key-values pairs in this object depends on the Input request.",
    "13-0": "payments",
    "13-1": "`array of objects`",
    "13-2": "An array of object that contains the payment details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/card-payments-object#payments-child-object\" >Learn more about our `payments` child object</a>.  \n  \n**Note**: Payments response object can vary based on the payment methods and payment status.",
    "14-0": "created_at",
    "14-1": "`string`",
    "14-2": "The ISO 8601 UTC Timestamp, when the create order request was received by Plural.  \n  \nExample: `2024-07-09T07:57:08.022Z`",
    "15-0": "updated_at",
    "15-1": "`string`",
    "15-2": "The ISO 8601 UTC Timestamp, when the order response object is updated.  \n  \nExample: `2024-07-09T07:57:08.022Z`"
  },
  "cols": 3,
  "rows": 16,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Order Amount [Child Object]

The table below lists the various parameters in the `order_amount` child object. This object is part of the payments sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value",
    "0-1": "`integer`",
    "0-2": "The transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
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

The table below lists the various parameters in the `purchase_details` child object. This object is part of the payments sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "customer",
    "0-1": "`Object`",
    "0-2": "An object that contains the customer details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/card-payments-object#customer-child-object\" >Learn more about our `customer` child object</a>.",
    "1-0": "merchant_metadata",
    "1-1": "`object`",
    "1-2": "An object of key-value pair that can be used to store additional information.  \n  \nExample: `\"key1\": \"DD\"`"
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
    "0-2": "Customer's email address.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 character.</ul></li>Example: `kevin.bob@example.com`",
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
    "4-2": "Customer's mobile number.<br><ul><li>Minimum length: `10` character.</li><li>Maximum length: `20` characters.</ul></li>Example: `9876543210`<br><br>Supported characters: `0-9`",
    "5-0": "billing_address",
    "5-1": "`object`",
    "5-2": "An object that contains the details of the billing address.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/card-payments-object#billing-address-child-object\" >Learn more about our `billing_address` child object</a>.",
    "6-0": "shipping_address",
    "6-1": "`object`",
    "6-2": "An object that contains the shipping address details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/card-payments-object#shipping-address-child-object\" >Learn more about our `shipping_address` child object</a>."
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
    "3-2": "Pincode of the billing address.<br><ul><li>Maximum length: 10 characters.</ul></li>Example: `51524036`",
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
    "3-2": "Pincode of the shipping address.<br><ul><li>Maximum length: 10 characters.</ul></li>Example: `51524036`",
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


## Payments [Child Object]

The table below lists the various parameters in the `payments` child object. This object is part of the payments sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "id",
    "0-1": "`string`",
    "0-2": "Unique identifier of the payment in the Plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `v1-5206071124-aa-mpLhF3-cc-l`",
    "1-0": "merchant_payment_reference",
    "1-1": "`string`",
    "1-2": "A unique Payment Reference id sent by merchant. <br><br> Example: `008cf04b-a770-4777-854e-b1e6c1230609`",
    "2-0": "status",
    "2-1": "`string`",
    "2-2": "Payment status.<br><br>Possible values:<ul><li>`PENDING`: When the create payment API request is successfully received by Plural.</li><li>`AUTHORIZED`: **Only when `pre_auth` is `true`**. When the payment is ready for authorization.</li><li>`CANCELLED`: When the payment gets cancelled.</li><li>`PROCESSED`: When the payment is successfully received by Plural.</li><li>`FAILED`: When the payment fails, this can be for many reasons such as canceling payments, etc.</ul></li>Example: `PENDING`",
    "3-0": "payment_amount",
    "3-1": "`object`",
    "3-2": "An object that contains the details of the payment amount.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/card-payments-object#payment-amount-child-object\" >Learn more about our `payment_amount` child object</a>.",
    "4-0": "payment_method",
    "4-1": "`string`",
    "4-2": "Type of payment method.<br><br>Accepted values:<ul><li>`CARD`</li><li>`UPI`</li><li>`POINTS`</ul></li>Example: `CARD`",
    "5-0": "payment_option",
    "5-1": "`object`",
    "5-2": "An object that contains the details of the payment options.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/card-payments-object#payment-option-child-object\" >Learn more about our `payment_option` child object</a>.",
    "6-0": "acquirer_data",
    "6-1": "`object`",
    "6-2": "An object that contains the details of the acquirer data.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/card-payments-object#acquirer-data-child-object\" >Learn more about our `acquirer_data` child object</a>.",
    "7-0": "error_detail",
    "7-1": "`object`",
    "7-2": "An object that contains the error details.<br><br><a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/card-payments-object#error-detail-child-object\" >Learn more about our `error_detail` child object</a>.<br><br>**Note**: This object is returned only for the failed payment.",
    "8-0": "capture_data",
    "8-1": "`object`",
    "8-2": "An object that contains the details of the capture data.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/card-payments-object#capture-data-child-object\" >Learn more about our `capture_data` child object</a>.  \n  \n**Note**: The presence of the key-value pairs against this object depends on the pre-authorization type.",
    "9-0": "created_at",
    "9-1": "`string`",
    "9-2": "The ISO 8601 UTC Timestamp, when the create payment request was received by Plural.  \n  \nExample: `2024-07-11T06:52:12.484Z`",
    "10-0": "updated_at",
    "10-1": "`string`",
    "10-2": "The ISO 8601 UTC Timestamp, when the payment response object is updated.  \n  \nExample: `2024-07-11T06:59:38.260Z`"
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


### Payment Amount [Child Object]

The table below lists the various parameters in the `payment_amount` child object. This object is part of the `payments` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value",
    "0-1": "`integer`",
    "0-2": "The transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1).</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
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


### Payment Option [Child Object]

The table below lists the various parameters in the `payment_option` child object. This object is part of the `payments` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "card_data",
    "0-1": "`object`",
    "0-2": "An object that contains the card details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/card-payments-object#card-data-child-object\" >Learn more about our `card_data` child object</a>."
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


#### Card Data [Child Object]

The table below lists the various parameters in the `card_data` child object. This object is part of the `payment_option` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "card_type",
    "0-1": "`string`",
    "0-2": "Type of card.<br><br>Possible values:<ul><li>`DEBIT`</li><li>`CREDIT`</ul></li>Example: `CREDIT`",
    "1-0": "network_name",
    "1-1": "`string`",
    "1-2": "Card network providers.  \n  \nExample: `VISA`",
    "2-0": "issuer_name",
    "2-1": "`string`",
    "2-2": "Card issuer entity.  \n  \nExample: `HDFC`",
    "3-0": "card_category",
    "3-1": "`string`",
    "3-2": "The card category type.<br><br>Possible values:<ul><li>`CONSUMER`</li><li>`COMMERCIAL`</li><li>`PREMIUM`</li><li>`SUPER_PREMIUM`</li><li>`PLATINUM`</li><li>`OTHER`</li><li>`BUSINESS`</li><li>`GOVERNMENT_NOTES`</li><li>`PAYOUTS`</li><li>`ELITE`</li><li>`STANDARD`</li></ul>",
    "4-0": "country_code",
    "4-1": "`string`",
    "4-2": "Card issuers Country.  \n  \nExample: `IND`",
    "5-0": "token_txn_type",
    "5-1": "`string`",
    "5-2": "Transaction token type.<br><br>Possible values:<ul><li>`ALT_TOKEN`</li><li>`NETWORK_TOKEN`</li><li>`ISSUER_TOKEN`</ul></li>Example: `ALT_TOKEN`",
    "6-0": "last4_digit",
    "6-1": "`string`",
    "6-2": "Card last four digits.  \n  \nExample: `1091`",
    "7-0": "save",
    "7-1": "`boolean`",
    "7-2": "Indicates the status of the customer's consent to save their card details for future transactions securely.  \n  \nPossible values:<ul><li>`true`: The customer's consent is received to save the card details securely..</li><li>`false`: The customer's consent is not received to save the card details.",
    "8-0": "is_native_otp_eligible",
    "8-1": "`boolean`",
    "8-2": "Status of Native OTP eligibility.  \n  \nPossible values:<ul><li>`true`: Card is eligible.</li><li>`false`: Card is not eligible."
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


### Acquirer Data [Child Object]

The table below lists the various parameters in the `acquirer_data` child object. This object is part of the `payments` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "approval_code",
    "0-1": "`string`",
    "0-2": "Authorization code returned from acquirer against the payment.  \n  \nExample: `030376`",
    "1-0": "acquirer_reference",
    "1-1": "`string`",
    "1-2": "Unique reference returned from acquirer for the payment.  \n  \nExample: `202455840588334`",
    "2-0": "rrn",
    "2-1": "`string`",
    "2-2": "Retrieval reference number returned from acquirer for the payment.  \n  \nExample: `419335023601`",
    "3-0": "is_aggregator",
    "3-1": "`boolean`",
    "3-2": "The selected aggregator model type.<br><br>Accepted values:<ul><li>`true`: Plural is responsible for settling funds related to this payment.</li><li>`false`: Plural is not responsible for settling funds related to this payment.</ul></li>**Note**:<ul><li>When the `is_aggregator` is set to true, Plural acts as the acquirer on behalf of merchants, receiving funds from banks into a designated \"Nodal Account\".</li><li>When the `is_aggregator` is set to false, the Merchant has a direct relationship with the bank and the responsibility for settlement of funds lies with both of those parties.</ul></li>"
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


### Error Detail [Child Object]

The table below lists the various parameters in the `error_detail` child object. This object is part of the `payments` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "code",
    "0-1": "`string`",
    "0-2": "The error short Code.  \n  \nExample: `PAYMENT_DECLINED`",
    "1-0": "message",
    "1-1": "`string`",
    "1-2": "Error description explaining the why the error occured.  \n  \nExample: `Transaction declined due to insufficient balance`"
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


### Capture Data [Child Object]

The table below lists the various parameters in the `capture_details` child object. This object is part of the `payments` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant_capture_reference",
    "0-1": "`string`",
    "0-2": "Unique identifier passed while creating the capture payment request.  \n  \nExample: `5742ef1e-4606-4c11-5757-705f4d415b6d`",
    "1-0": "capture_amount",
    "1-1": "`object`",
    "1-2": "An object that contains the capture amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/card-payments-object#capture-amount-child-object\" >Learn more about our `capture_amount` child object</a>.",
    "2-0": "created_at",
    "2-1": "`string`",
    "2-2": "The ISO 8601 UTC Timestamp, when the amount captured.  \n  \nExample: `2024-07-11T11:52:12.484105Z`"
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


#### Capture Amount [Child Object]

The table below lists the various parameters in the `capture_amount` child object. This object is part of the `capture_data` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value",
    "0-1": "`integer`",
    "0-2": "The transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1).</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
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


## OTP Response Objects

Shown below are the sample responses through our OTP APIs.

```json Generate OTP Response Object
{
  "next": [
    "SUBMIT_OTP",
    "RESEND_OTP"
  ],
  "meta_data": {
    "resend_after": "180"
  }
}
```
```json Submit OTP Response Object
{
  "status": "SUCCESS"
}
```
```json Resend OTP Response Object
{
  "status": "SUCCESS",
  "next": [
    "SUBMIT_OTP",
    "RESEND_OTP"
  ],
  "meta_data": {
    "resend_after": "180"
  }
}
```

The table below lists the various parameters returned in our OTP APIs response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "next",
    "0-1": "`array of strings`",
    "0-2": "An array of strings that contains the details of the next steps.  \n  \nPossible values:<ul><li>`SUBMIT_OTP`: Use our Submit OTP API to submit the OTP.</li><li>`RESEND_OTP`: Use our resend OTP API to resend OTP to the registered mobile number of your customer.</li><li>`NONE`: When OTP verification fails for reasons such as exceeding the maximum retry attempts or entering an invalid OTP.<br>**Note**: If the `next` parameter is returned as NONE, you must create a new payment for the existing order to proceed.</ul></li>",
    "1-0": "meta_data",
    "1-1": "`object`",
    "1-2": "An object that contains the metadata information.  \n  \n<a href=\"https://developer.pluralonline.com/reference/card-payments-object#metadata-child-object\" >Learn more about the `meta_data` child object</a>.",
    "2-0": "status",
    "2-1": "`string`",
    "2-2": "OTP Verification status.  \n  \nPossible values:<ul><li>`success`: When the OTP is successfully submitted and the payment is initiated.</ul></li>**Note**: The OTP submission status does not indicate the transaction status. To check the transaction status, use webhooks or the fetch order API."
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


### Metadata [Child Object]

The table below lists the various parameters in the `metadata` child object. This object is part of the `OTP APIs response` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "resend_after",
    "0-1": "`string`",
    "0-2": "The time after which you can initiate the Resend OTP API.  \n  \nTime in seconds.  \n  \nExample: `180`"
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


## Get Card Details Response Object

Shown below is a sample response returned through our Get Card Details API.

```json Get Card Details Response Object
{
  "card_payment_details":[
    {
      "card_network":"VISA",
      "card_issuer":"INTL HDQTRS-CENTER OWNED",
      "card_type":"CREDIT",
      "card_category":"NONE",
      "is_international_card":false,
      "is_native_otp_supported":true,
      "country_code":"IND",
      "currency":"INR",
      "is_currency_supported":true
    }
  ]
}
```

The table below lists the various parameters returned in our Get Card Details API response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "card_payment_details",
    "0-1": "`array of objects`",
    "0-2": "An array of objects that contains the card payment details.  \n  \nLearn more about our `card_payment_details` child object."
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


### Card Payment Details [Child Object]

The table below lists the various parameters in the `card_payment_details` child object. This object is part of the `Get Card Details API` response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "card_network",
    "0-1": "`string`",
    "0-2": "Card network providers.  \n  \nExample: `VISA`",
    "1-0": "card_issuer",
    "1-1": "`string`",
    "1-2": "Card Issuing entity.  \n  \nExample: `HDFC`",
    "2-0": "card_type",
    "2-1": "`string`",
    "2-2": "Type of card.  \n  \nPossible values:<ul><li>`NONE`</li><li>`DEBIT`</li><li>`CREDIT`</li><li>`PREPAID`</li><li>`CIRRUS`</li><li>`CHARGE_CARD`</li><li>`COMMERCIAL_PREPAID`</li><li>`COMMERCIAL_CREDIT`</li><li>`COMMERCIAL_DEBIT`</li><li>`CONSUMER`</li><li>`DEFERRED_DEBIT`</li><li>`OTHER`</ul></li>Example: `CREDIT`",
    "3-0": "card_category",
    "3-1": "`string`",
    "3-2": "The card category type.  \n  \nPossible values:<ul><li>`CONSUMER`</li><li>`COMMERCIAL`</li><li>`PREMIUM`</li><li>`SUPER_PREMIUM`</li><li>`PLATINUM`</li><li>`OTHER`</li><li>`BUSINESS`</li><li>`GOVERNMENT_NOTES`</li><li>`PAYOUTS`</li><li>`ELITE`</li><li>`STANDARD`</li><li>`NONE`</ul></li>",
    "4-0": "is_international_card",
    "4-1": "`boolean`",
    "4-2": "Status of the card classified as domestic or international.  \n  \nPossible values: <ul><li>`true`: The card is not issued from Indian Issuer Banks.[International Card]</li><li>`false`: The card is issued from the Indian Issuer Bank.[Domestic Card]</ul></li>",
    "5-0": "is_native_otp_supported",
    "5-1": "`boolean`",
    "5-2": "Native OTP supported status.  \n  \nPossible values: <ul><li>`true`: Card supports native OTP.</li><li>`false`: Card do not support native OTP.</ul></li>",
    "6-0": "country_code",
    "6-1": "`string`",
    "6-2": "Card issuers Country.  \n  \nExample: `IND`",
    "7-0": "currency",
    "7-1": "`string`",
    "7-2": "Type of currency.  \n  \nExample: `INR`",
    "8-0": "is_currency_supported",
    "8-1": "`boolean`",
    "8-2": "Currency support status.  \n  \nPossible values: <ul><li>`true`: Card supports dynamic currency conversion.</li><li>`false`: Card do not support dynamic currency conversion.</ul></li>"
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
