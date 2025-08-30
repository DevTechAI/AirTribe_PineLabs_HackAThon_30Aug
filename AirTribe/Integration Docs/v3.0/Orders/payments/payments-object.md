---
title: "Object"
slug: "payments-object"
excerpt: "Overview of the payments/refund response object."
hidden: true
createdAt: "Thu Jul 11 2024 09:23:02 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Sep 12 2024 16:22:00 GMT+0000 (Coordinated Universal Time)"
---
# Payments Object

Shown below is a sample responses of a Create Payments API.

```json Card Payments Object
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
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "030376",
          "acquirer_reference": "202455840588334",
          "rrn": "419335023601"
        },
        "capture_data": []
      }
    ],
    "created_at": "2024-07-11T06:52:12.484105Z",
    "updated_at": "2024-07-11T06:59:38.260145Z"
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
    "6-2": "An object that contains the transaction amount details.  \n  \n<a href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#order-amount-child-object\" >Learn more about our `order_amount` child object</a>.",
    "7-0": "pre_auth",
    "7-1": "`boolean`",
    "7-2": "The pre-authorization type.<br><br>Possible values:<ul><li>`true`: When pre-authorization is needed.</li><li>`false`: When pre-authorization is not required.</ul></li>Example: `false`<br><br><a href=\"https://developer.pluralonline.com/v3.0/reference/orders\" target=\"_blanck\">Learn more about our pre-authorization.</a>.",
    "8-0": "purchase_details",
    "8-1": "`object`",
    "8-2": "An object that contains the purchase details.  \n  \n<a href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#purchase-details-child-object\" >Learn more about our `purchase_details` child object</a>.  \n  \n**Note**: The presence of the key-values pairs in this object depends on the Input request.",
    "9-0": "payments",
    "9-1": "`array of objects`",
    "9-2": "An array of object that contains the payment details.  \n  \n<a href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#payments-child-object\" >Learn more about our `payments` child object</a>.  \n  \n**Note**: Payments response object can vary based on the payment methods and payment status.",
    "10-0": "created_at",
    "10-1": "`string`",
    "10-2": "The ISO 8601 UTC Timestamp, when the create payment request was received by Plural.  \n  \nExample: `2024-07-09T07:57:08.022056Z`",
    "11-0": "updated_at",
    "11-1": "`string`",
    "11-2": "The ISO 8601 UTC Timestamp, when the payment response object is updated.  \n  \nExample: `2024-07-09T07:57:08.022065Z`"
  },
  "cols": 3,
  "rows": 12,
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
    "0-2": "An object that contains the customer details.  \n  \n<a href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#customer-child-object\" >Learn more about our `customer` child object</a>.",
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
    "4-2": "Customer's mobile number.<br><ul><li>Minimum length: 9 character.</li><li>Maximum length: 20 characters.</ul></li>Example: `9876543210`",
    "5-0": "billing_address",
    "5-1": "`object`",
    "5-2": "An object that contains the details of the billing address.  \n  \n<a href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#billing-address-child-object\" >Learn more about our `customer` child object</a>.",
    "6-0": "shipping_address",
    "6-1": "`object`",
    "6-2": "An object that contains the shipping address details.  \n  \n<a href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#shipping-address-child-object\" >Learn more about our `customer` child object</a>."
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
    "1-0": "status",
    "1-1": "`string`",
    "1-2": "Payment status.<br><br>Possible values:<ul><li>`PENDING`: When the create payment API request is successfully received by Plural.</li><li>`AUTHORIZED`: **Only when `pre_auth` is `true`**. When the payment is ready for authorization.</li><li>`CANCELLED`: When the payment gets cancelled.</li><li>`PROCESSED`: When the payment is successfully received by Plural.</li><li>`FAILED`: When the payment fails, this can be for many reasons such as canceling payments, etc.</ul></li>Example: `PENDING`",
    "2-0": "payment_amount",
    "2-1": "`object`",
    "2-2": "An object that contains the details of the payment amount.  \n  \n<a href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#payment-amount-child-object\" >Learn more about our `payment_amount` child object</a>.",
    "3-0": "payment_method",
    "3-1": "`string`",
    "3-2": "Type of payment method.<br><br>Accepted values:<ul><li>`CARD`</li><li>`UPI`</li><li>`POINTS`</ul></li>Example: `CARD`",
    "4-0": "payment_option",
    "4-1": "`object`",
    "4-2": "An object that contains the details of the payment options.  \n  \n<a href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#payment-option-child-object\" >Learn more about our `payment_option` child object</a>.",
    "5-0": "acquirer_data",
    "5-1": "`object`",
    "5-2": "An object that contains the details of the acquirer data.  \n  \n<a href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#acquirer-data-child-object\" >Learn more about our `acquirer_data` child object</a>.",
    "6-0": "error_detail",
    "6-1": "`object`",
    "6-2": "An object that contains the error details.<br><br><a href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#error-detail-child-object\" >Learn more about our `error_detail` child object</a>.<br><br>**Note**: This object is returned only for the failed payment.",
    "7-0": "capture_data",
    "7-1": "`object`",
    "7-2": "An object that contains the details of the capture data.  \n  \n<a href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#capture-data-child-object\" >Learn more about our `capture_data` child object</a>.  \n  \n**Note**: The presence of the key-value pairs against this object depends on the pre-authorization type."
  },
  "cols": 3,
  "rows": 8,
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
    "0-2": "An object that contains the card details.  \n  \n<a href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#card-data-child-object\" >Learn more about our `card_data` child object</a>."
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
    "3-0": "product_name",
    "3-1": "`string`",
    "3-2": "Card name.  \n  \nExample: `Visa Platinum`",
    "4-0": "card_category",
    "4-1": "`string`",
    "4-2": "The card category type.<br><br>Possible values:<ul><li>`CONSUMER`</li><li>`COMMERCIAL`</li><li>`PREMIUM`</li><li>`SUPER_PREMIUM`</li><li>`PLATINUM`</li><li>`OTHER`</li><li>`BUSINESS`</li><li>`GOVERNMENT_NOTES`</li><li>`PAYOUTS`</li><li>`ELITE`</li><li>`STANDARD`</li></ul>",
    "5-0": "country_code",
    "5-1": "`string`",
    "5-2": "Card issuers Country.  \n  \nExample: `IND`",
    "6-0": "token_txn_type",
    "6-1": "`string`",
    "6-2": "Transaction token type.<br><br>Possible values:<ul><li>`ALT_TOKEN`</li><li>`NETWORK_TOKEN`</li><li>`ISSUER_TOKEN`</ul></li>Example: `ALT_TOKEN`"
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
    "2-2": "Retrieval reference number returned from acquirer for the payment.  \n  \nExample: `419335023601`"
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
    "1-2": "An object that contains the capture amount details.  \n  \n<a href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#capture-amount-child-object\" >Learn more about our `capture_amount` child object</a>.",
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


# Refund Object

Overview of the refunds response object.

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
    "1-2": "An object that contains the refund details.  \n  \n<a href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#refunds-child-object\" >Learn more about our `refunds` child object</a>."
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
    "4-2": "An object that contains the refund amount details.  \n  \n<a href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#refund-amount-child-object\" >Learn more about our `refund_amount` child object</a>.",
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
