---
title: "Object (COPY)"
slug: "object-copy-2"
excerpt: "Overview of the split settlement object."
hidden: true
createdAt: "Thu Jan 02 2025 11:45:48 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Jan 03 2025 04:38:03 GMT+0000 (Coordinated Universal Time)"
---
Shown below is a sample response of a Create Orders API.

```json Split Order Response
{
  "data": {
    "order_id": "v1-241118074845-aa-wduUQF",
    "merchant_order_reference": "3595f435-b1c5-4a60-a98c-9cf39ee3dc07",
    "type": "CHARGE",
    "status": "CREATED",
    "merchant_id": "108272",
    "order_amount": {
      "value": 50000,
      "currency": "INR"
    },
    "pre_auth": false,
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
        "mobile_number": "9876543210",
        "billing_address": {},
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
      },
      "split_info": {
        "split_type": "AMOUNT",
        "split_details": [
          {
            "split_merchant_id": "1324",
            "split_settlement_id": "v1-241118074845-aa-wduUQF-ss-b",
            "merchant_settlement_reference": "kshjhfk",
            "amount": {
              "value": 30000,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2024-11-18T07:48:45.324Z"
          },
          {
            "split_merchant_id": "1233",
            "split_settlement_id": "v1-241118074845-aa-wduUQF-ss-r",
            "amount": {
              "value": 20000,
              "currency": "INR"
            },
            "on_hold": false,
            "status": "RELEASED",
            "updated_at": "2024-11-18T07:48:45.324Z"
          }
        ]
      }
    },
    "created_at": "2024-11-18T07:48:45.324336Z",
    "updated_at": "2024-11-18T07:48:45.324348Z",
    "integration_mode": "SEAMLESS"
  }
}
```

Shown below is a sample response of a Create Payments API.

```json Create Payment Object
{
  "data": {
    "order_id": "v1-4405071524-aa-qlAtAf",
    "merchant_order_reference": "112345",
    "type": "CHARGE",
    "status": "PENDING",
    "challenge_url": "https://api.pluralpay.in/web/auth/landing/?token=S50%2B0lOoYHlA03j3y8Of4%2BZEzhD8MuFFLKP6NXx9uiaBBXlNhpCRA4wqkPd%2Bs9eRz7H",
    "merchant_id": "123456",
    "order_amount": {
      "value": 1100,
      "currency": "INR"
    },
    "pre_auth": false,
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
      },
      "split_info": {
        "split_type": "AMOUNT",
        "split_details": [
          {
            "split_merchant_id": "123456",
            "split_settlement_id": "v1-241118174248-aa-81BMcH-ss-b",
            "merchant_settlement_reference": "kshjhfk",
            "amount": {
              "value": 20000,
              "currency": "INR"
            },
            "on_hold": false,
            "status": "RELEASED",
            "updated_at": "2024-11-18T07:49:38.212311Z"
          },
          {
            "split_merchant_id": "234567",
            "split_settlement_id": "v1-241118174248-aa-81BMcH-ss-r",
            "amount": {
              "value": 30000,
              "currency": "INR"
            },
            "on_hold": false,
            "status": "RELEASED",
            "updated_at": "2024-11-18T07:48:45.324348Z"
          }
        ]
      }
    },
    "payments": [
      {
        "id": "v1-5307071124-aa-dmkVNf-cc-c",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PENDING",
        "payment_amount": {
          "value": 1100,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "KOTAK",
            "card_category": "CONSUMER",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "created_at": "2024-07-11T07:53:43.358Z",
        "updated_at": "2024-07-11T07:56:18.044Z"
      }
    ],
    "created_at": "2024-07-11T07:53:43.358Z",
    "updated_at": "2024-07-11T07:56:18.044Z"
  }
}
```

Shown below is a sample response of a Release Settlement Fee API.

```json Release Settlement Object
{
  "data": {
    "order_id": "v1-241118174248-aa-81BMcH",
    "merchant_order_reference": "76d3327d-4aa2-4303-be51-e051180f3b99",
    "type": "CHARGE",
    "status": "PROCESSED",
    "merchant_id": "108272",
    "order_amount": {
      "value": 50000,
      "currency": "INR"
    },
    "pre_auth": false,
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.sam@gmail.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
        "mobile_number": "9876543210",
        "billing_address": {},
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
      },
      "split_info": {
        "split_type": "AMOUNT",
        "split_details": [
          {
            "split_merchant_id": "123456",
            "split_settlement_id": "v1-241118174248-aa-81BMcH-ss-b",
            "merchant_settlement_reference": "kshjhfk",
            "amount": {
              "value": 20000,
              "currency": "INR"
            },
            "on_hold": false,
            "status": "RELEASED",
            "updated_at": "2024-11-18T07:49:38.212311Z"
          },
          {
            "split_merchant_id": "234567",
            "split_settlement_id": "v1-241118174248-aa-81BMcH-ss-r",
            "amount": {
              "value": 30000,
              "currency": "INR"
            },
            "on_hold": false,
            "status": "RELEASED",
            "updated_at": "2024-11-18T07:48:45.324348Z"
          }
        ]
      }
    },
    "payments": [
      {
        "id": "v1-241118174248-aa-81BMcH-cc-v",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 50000,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "U.S. REGION",
            "card_category": "Consumer",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "000000",
          "acquirer_reference": "202467869455141",
          "rrn": "431323000215",
          "is_aggregator": true
        },
        "created_at": "2024-11-18T07:48:48.233526Z",
        "updated_at": "2024-11-18T07:48:56.352361Z"
      }
    ],
    "created_at": "2024-11-18T07:48:45.324336Z",
    "updated_at": "2024-11-18T07:48:45.324348Z",
    "integration_mode": "SEAMLESS"
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
    "6-2": "An object that contains the transaction amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders-object#order-amount-child-object\" >Learn more about the `order_amount` child object.</a>",
    "7-0": "notes",
    "7-1": "`string`",
    "7-2": "The note you want to show against an order.  \n  \nExample: `Order1`",
    "8-0": "pre_auth",
    "8-1": "`boolean`",
    "8-2": "The pre-authorization type.  \n  \nPossible values:<ul><li>`true`: When pre-authorization is needed.</li><li>`false`: When pre-authorization is not required.</ul></li>Example: `false`<br><br><a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders\" target=\"_block\">Learn more about our pre authorization</a>.",
    "9-0": "callback_url",
    "9-1": "`string`",
    "9-2": "Use this URL to redirect your customers to specific success or failure pages based on the order or product details.  \n  \nExample: `https\\://sample-callback-url`",
    "10-0": "purchase_details",
    "10-1": "`object`",
    "10-2": "An object that contains the purchase details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders-object#purchase-details-child-object\" >Learn more about the `purchase_details` child object.</a><br><br>**Note**: The presence of the object key-values depends on the Input request.",
    "11-0": "payments",
    "11-1": "`array of objects`",
    "11-2": "An array of objects that contains the payment details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders-object#payments-child-object\" >Learn more about the `payments` child object.</a><br><br>**Note**: Payment object is returned only for the orders linked with a payment.",
    "12-0": "created_at",
    "12-1": "`string`",
    "12-2": "The ISO 8601 UTC Timestamp, when the create order request was received by Plural.  \n  \nExample: `2024-07-09T07:57:08.022Z`",
    "13-0": "updated_at",
    "13-1": "`string`",
    "13-2": "The ISO 8601 UTC Timestamp, when the order object is updated.  \n  \nExample: `2024-07-09T07:57:08.022Z`"
  },
  "cols": 3,
  "rows": 14,
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
    "2-2": "An object that contains the split information details."
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
    "0-2": "Type of split.<br><br>Example: `Amount`",
    "1-0": "split_details",
    "1-1": "`array of objects`",
    "1-2": "An array of objects that contains the split details."
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
    "0-0": "split_merchant_id",
    "0-1": "`string`",
    "0-2": "Partner merchant ID.  \n  \nExample: `123456`",
    "1-0": "merchant_settlement_reference",
    "1-1": "`string`",
    "1-2": "Unique identifier entered while creating a order in split.<ul><li>Maximum length: 50 characters.</ul></li>Example: `5206071124-aa-mpLhF3-cc-l`",
    "2-0": "split_settlement_id",
    "2-1": "`string`",
    "2-2": "Unique identifier of the split settlement in the Plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `71124-aa-mpLhF3-cc-l`<br><br>**Note**: Use this Settlement ID to initiate a release a settlement using our Release Settlement API.",
    "3-0": "amount",
    "3-1": "`object`",
    "3-2": "An object that contains the split amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/split-settlement-object#amount-child-object\" >Learn more about the `amount` child object.</a>",
    "4-0": "on_hold",
    "4-1": "`boolean`",
    "4-2": "Indicate whether the settlement is on hold for future release.  \n  \nAccepted values:<ul><li>`true`: The settlement is placed on hold.</li><li>`false`: The settlement is processed immediately.",
    "5-0": "status",
    "5-1": "`string`",
    "5-2": "Split Settlement status.<br><br>Possible values:<ul><li>`RELEASED`</li><li>`HOLD`</ul></li>",
    "6-0": "updated_at",
    "6-1": "`string`",
    "6-2": "The ISO 8601 UTC Timestamp, when the split order was created by Plural.  \n  \nExample: `2024-07-09T07:57:08.022Z`"
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


### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This object is part of the `split_details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value",
    "0-1": "`integer`",
    "0-2": "The split amount is Paisa.<ul><li>Minimum value: `100` (₹1).</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
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
    "4-0": "payment_option",
    "4-1": "`object`",
    "4-2": "An object that contains the details of the payment options.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#payment-option-child-object\" >Learn more about our `payment_option` child object</a>.",
    "5-0": "acquirer_data",
    "5-1": "`object`",
    "5-2": "An object that contains the details of the acquirer data.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#acquirer-data-child-object\" >Learn more about our `acquirer_data` child object</a>.",
    "6-0": "error_detail",
    "6-1": "`object`",
    "6-2": "An object that contains the error details.<br><br><a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#error-detail-child-object\" >Learn more about our `error_detail` child object</a>.<br><br>**Note**: This object is returned only for the failed payment.",
    "7-0": "capture_data",
    "7-1": "`object`",
    "7-2": "An object that contains the details of the capture data.  \n  \n<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#capture-data-child-object\" >Learn more about our `capture_data` child object</a>.  \n  \n**Note**: The presence of the key-value pairs against this object depends on the pre-authorization type.",
    "8-0": "additional_detail",
    "8-1": "`object`",
    "8-2": "An object that contains the additional details related to the payment.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders-object#additional-detail-child-object\" >Learn more about our `capture_data` child object</a>.",
    "9-0": "created_at",
    "9-1": "`string`",
    "9-2": "The ISO 8601 UTC Timestamp, when the create payment request was received by Plural.  \n  \nExample: `2024-07-09T07:57:08.022Z`",
    "10-0": "updated_at",
    "10-1": "`string`",
    "10-2": "The ISO 8601 UTC Timestamp, when the payment object is updated.  \n  \nExample: `2024-07-09T07:57:08.022Z`"
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
    "0-2": "An object that contains the card details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#card-data-child-object\" >Learn more about our `card_data` child object</a>."
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
    "1-2": "Error description. This parameter tells you why the error occurred.  \n  \nExample: `Transaction declined due to insufficient balance`"
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

The table below lists the various parameters in the `capture_data` child object. This object is part of the `payments` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant_capture_reference",
    "0-1": "`string`",
    "0-2": "Unique identifier passed while creating the capture payment request.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `5742ef1e-4606-4c11-5757-705f4d415b6d`",
    "1-0": "capture_amount",
    "1-1": "`object`",
    "1-2": "An object that contains the capture amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#capture-amount-child-object\" >Learn more about our `capture_amount` child object</a>.",
    "2-0": "created_at",
    "2-1": "`string`",
    "2-2": "The ISO 8601 UTC Timestamp, when the amount is captured.  \n  \nExample: `2024-07-11T11:52:12.484105Z`"
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


### Additional Detail [Child Object]

The table below lists the various parameters in the `additional_detail` child object. This object is part of the `payments` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "source_ip",
    "0-1": "`string`",
    "0-2": "The IP Address of the merchant.  \n  \nExample: `52.66.76.63`"
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
