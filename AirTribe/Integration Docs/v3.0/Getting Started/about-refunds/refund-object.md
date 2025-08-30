---
title: "Object"
slug: "refund-object"
excerpt: "Overview of the refunds response object."
hidden: false
createdAt: "Tue Oct 15 2024 08:11:33 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon May 19 2025 07:41:53 GMT+0000 (Coordinated Universal Time)"
---
Shown below is a sample response returned through our Refund API.

```json Refund
{
  "data": {
    "order_id": "v1-241010071949-aa-vcqtJY",
    "parent_order_id": "v1-241010055924-aa-AHbN0s",
    "merchant_order_reference": "e436fefa-f0e9-4b36-ac01-3d158c31726c",
    "type": "REFUND",
    "status": "PROCESSED",
    "merchant_id": "108272",
    "order_amount": {
      "value": 400,
      "currency": "INR"
    },
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
        "key1": "XX",
        "key2": "DOF"
      }
    },
    "payments": [
      {
        "id": "v1-241010071949-aa-vcqtJY-cc-b",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 400,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "7285447904236780703954",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2024-10-10T07:19:49.423Z",
        "updated_at": "2024-10-10T07:19:51.205Z"
      }
    ],
    "created_at": "2024-10-10T07:19:49.424Z",
    "updated_at": "2024-10-10T07:19:51.205Z"
  }
}
```
```json Split Refund
{
  "data": {
    "order_id": "v1-250226115026-aa-JO3YTv",
    "parent_order_id": "v1-250226114507-aa-tDpkuP",
    "merchant_order_reference": "merchant-reference-r4y",
    "type": "REFUND",
    "status": "PROCESSED",
    "merchant_id": "122743",
    "order_amount": {
      "value": 21000,
      "currency": "INR"
    },
    "purchase_details": {
      "customer": {
        "country_code": "91",
        "billing_address": {},
        "shipping_address": {},
        "is_edit_customer_details_allowed": false
      },
      "merchant_metadata": {
        "key1": "value1",
        "key2": "value2"
      },
      "split_info": {
        "split_type": "AMOUNT",
        "split_details": [
          {
            "parent_order_split_settlement_id": "v1-250513063000-aa-UBAnaE-ss-g",
            "split_merchant_id": 117230,
            "split_settlement_id": "v1-5312042524-aa-0YO29z-ss-a",
            "merchant_settlement_reference": "ref1",
            "amount": {
              "value": 21000,
              "currency": "INR"
            },
            "status": "DO_NOT_RECOVER"
          }
        ]
      }
    },
    "payments": [
      {
        "id": "v1-250226115026-aa-JO3YTv-cc-a",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 21000,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "7405706270796283203814",
          "rrn": "",
          "is_aggregator": true,
          "acquirer_name": "Cyber_Source_AXIS"
        },
        "offer_data": {},
        "created_at": "2025-02-26T11:50:26.351Z",
        "updated_at": "2025-02-26T11:50:27.718Z"
      }
    ],
    "created_at": "2025-02-26T11:50:26.352Z",
    "updated_at": "2025-02-26T11:50:27.718Z",
    "integration_mode": "SEAMLESS",
    "payment_retries_remaining": 10
  }
}
```
```json Multiple Split Refund
{
  "data": {
    "order_id": "v1-250513063438-aa-83Pcx8",
    "parent_order_id": "v1-250513063000-aa-UBAnaE",
    "merchant_order_reference": "0a049dd9-74eb-4a84-9d77-f639d9d889bc",
    "type": "REFUND",
    "status": "PROCESSED",
    "merchant_id": "111370",
    "order_amount": {
      "value": 8800,
      "currency": "INR"
    },
    "purchase_details": {
      "customer": {
        "country_code": "91",
        "billing_address": {},
        "shipping_address": {},
        "is_edit_customer_details_allowed": false
      },
      "merchant_metadata": {
        "key1": "value1",
        "key2": "value2"
      },
      "split_info": {
        "split_type": "AMOUNT",
        "split_details": [
          {
            "parent_order_split_settlement_id": "v1-250513063000-aa-UBAnaE-ss-g",
            "split_merchant_id": "111370",
            "split_settlement_id": "v1-250513063438-aa-83Pcx8-ss-c",
            "amount": {
              "value": 800,
              "currency": "INR"
            },
            "status": "DO_NOT_RECOVER",
            "updated_at": "2025-05-13T06:34:38.036Z"
          },
          {
            "parent_order_split_settlement_id": "v1-250513063000-aa-UBAnaE-ss-h",
            "split_merchant_id": "111370",
            "split_settlement_id": "v1-250513063438-aa-83Pcx8-ss-d",
            "amount": {
              "value": 8000,
              "currency": "INR"
            },
            "status": "DO_NOT_RECOVER",
            "updated_at": "2025-05-13T06:34:38.036Z"
          }
        ]
      }
    },
    "payments": [
      {
        "id": "v1-250513063438-aa-83Pcx8-cc-a",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 8800,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "7471180795846584503814",
          "rrn": "",
          "is_aggregator": true
        },
        "offer_data": {},
        "created_at": "2025-05-13T06:34:38.036Z",
        "updated_at": "2025-05-13T06:34:40.256Z"
      }
    ],
    "created_at": "2025-05-13T06:34:38.036Z",
    "updated_at": "2025-05-13T06:34:40.256Z",
    "integration_mode": "SEAMLESS",
    "payment_retries_remaining": 10
  }
}
```

The table below lists the various parameters returned in the orders response objects.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "order_id",
    "0-1": "`string`",
    "0-2": "Unique identifier of the order in the Plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `v1-5757575757-aa-hU1rUd`",
    "1-0": "parent_order_id",
    "1-1": "`string`",
    "1-2": "Unique identifier of the parent order in the Plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `v1-5757575757-aa-hU1rUd`",
    "2-0": "merchant_order_reference",
    "2-1": "`string`",
    "2-2": "Unique identifier entered while creating a refund.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `82d57572-057c-4826-5775-385a52150554`",
    "3-0": "type",
    "3-1": "`string`",
    "3-2": "Payment type.  \n  \nPossible values:<ul><li>`CHARGE`</li><li>`REFUND`</ul></li>",
    "4-0": "status",
    "4-1": "`string`",
    "4-2": "Order status.<br><br>Possible values:<ul><li>`CREATED`: When the order is successfully created.</li><li>`PENDING`: When the order is linked against a refund request.</li><li>`PROCESSED`: When the refund is received successfully.</li><li>`FAILED`: Refund acceptance failed for reasons such as cancel transactions, maximum retries for OTP verification etc.</ul></li>",
    "5-0": "merchant_id",
    "5-1": "`string`",
    "5-2": "Unique identifier of the merchant in the Plural database.  \n  \nExample: `123456`",
    "6-0": "order_amount",
    "6-1": "`object`",
    "6-2": "An object that contains the transaction amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders-object#order-amount-child-object\" >Learn more about the `order_amount` child object.</a>",
    "7-0": "purchase_details",
    "7-1": "`object`",
    "7-2": "An object that contains the purchase details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders-object#purchase-details-child-object\" >Learn more about the `purchase_details` child object.</a><br><br>**Note**: The presence of the object key-values depends on the Input request.",
    "8-0": "payments",
    "8-1": "`array of objects`",
    "8-2": "An array of objects that contains the payment details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders-object#payments-child-object\" >Learn more about the `payments` child object.</a><br><br>**Note**: Payment object is returned only for the orders linked with a payment.",
    "9-0": "created_at",
    "9-1": "`string`",
    "9-2": "The ISO 8601 UTC Timestamp, when the create refund request was received by Plural.  \n  \nExample: `2024-07-09T07:57:08.022Z`",
    "10-0": "updated_at",
    "10-1": "`string`",
    "10-2": "The ISO 8601 UTC Timestamp, when the refund object is updated.  \n  \nExample: `2024-07-09T07:57:08.022Z`"
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
    "0-0": "customer",
    "0-1": "`Object`",
    "0-2": "An object that contains the customer details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders-object#customer-child-object\" >Learn more about the `customer` child object.</a>",
    "1-0": "merchant_metadata",
    "1-1": "`object`",
    "1-2": "An object of key-value pair that can be used to store additional information.  \n  \nExample: `\"key1\": \"DD\"`",
    "2-0": "split_info",
    "2-1": "`object`",
    "2-2": "An object that contains the split information details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/refund-object#split-info-child-object\" >Learn more about the `split_info` child object.</a>"
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


## Customer [Child Object]

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
    "4-2": "Customer's mobile number.<br><ul><li>Minimum length: `10` character.</li><li>Maximum length: `20` characters.</ul></li>Example: `9876543210`<br><br>Supported characters: <ul><li>`0-9`</ul></li>",
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


### Billing Address [Child Object]

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


### Shipping Address [Child Object]

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


### Split Info [Child Object]

The table below lists the various parameters in the `split_info` child object. This is part of the `purchase_details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "split_type",
    "0-1": "`string`",
    "0-2": "Type of split.  \n  \nExample: `Amount`",
    "1-0": "split_details",
    "1-1": "`array of objects`",
    "1-2": "An array of objects that contains the split details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/refund-object#split-details-child-object\" >Learn more about the `split_details` child object.</a>"
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


#### Split Details [Child Object]

The table below lists the various parameters in the `split_details` child object. This is part of the `split_info` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "parent_order_split_settlement_id",
    "0-1": "`string`",
    "0-2": "Unique identifier of the split settlement in the Plural database.  \n  \nExample: `v1-5757575757-aa-hU1rUd`",
    "1-0": "split_merchant_id",
    "1-1": "`string`",
    "1-2": "Unique identifier of your partner merchant in the Plural database.  \n  \nExample: `123456`",
    "2-0": "amount",
    "2-1": "`object`",
    "2-2": "An object that contains the split amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/orders-object#amount-child-object\" >Learn more about the `amount` child object.</a>",
    "3-0": "status",
    "3-1": "`string`",
    "3-2": "Split Settlement recovery status.<br><br>Possible values:<ul><li>`DO_NOT_RECOVER`</li><li>`BLANK`</ul></li>"
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
    "2-2": "An object that contains the details of the payment amount.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#payment-amount-child-object\" >Learn more about our `payment_amount` child object</a>.",
    "3-0": "payment_method",
    "3-1": "`string`",
    "3-2": "Type of payment method.<br><br>Accepted values:<ul><li>`CARD`</li><li>`UPI`</li><li>`POINTS`</ul></li>Example: `CARD`",
    "4-0": "acquirer_data",
    "4-1": "`object`",
    "4-2": "An object that contains the details of the acquirer data.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#acquirer-data-child-object\" >Learn more about our `acquirer_data` child object</a>.",
    "5-0": "created_at",
    "5-1": "`string`",
    "5-2": "The ISO 8601 UTC Timestamp, when the create payment request was received by Plural.  \n  \nExample: `2024-07-09T07:57:08.022Z`",
    "6-0": "updated_at",
    "6-1": "`string`",
    "6-2": "The ISO 8601 UTC Timestamp, when the payment object is updated.  \n  \nExample: `2024-07-09T07:57:08.022Z`"
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
    "0-2": "Authorization code returned from acquirer against the payment.<ul><li>Maximum length: 50 characters.</ul></li>Example: `030376`",
    "1-0": "acquirer_reference",
    "1-1": "`string`",
    "1-2": "Unique reference returned from acquirer for the payment.<ul><li>Maximum length: 50 characters.</ul></li>Example: `202455840588334`",
    "2-0": "rrn",
    "2-1": "`string`",
    "2-2": "Retrieval reference number returned from acquirer for the payment.<ul><li>Maximum length: 50 characters.</ul></li>Example: `419335023601`",
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
