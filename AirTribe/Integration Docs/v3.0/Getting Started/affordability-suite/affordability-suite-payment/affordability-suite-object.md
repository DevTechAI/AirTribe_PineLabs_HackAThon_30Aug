---
title: "Object"
slug: "affordability-suite-object"
excerpt: "Overview of the card payment response object."
hidden: false
createdAt: "Wed Jan 22 2025 17:58:19 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed May 28 2025 11:29:35 GMT+0000 (Coordinated Universal Time)"
---
Shown below is a sample response of a Create Payments API through payment method as `CARD`.

```json Credit EMI Payment Object
{
  "data": {
    "order_id": "v1-250124055307-aa-6OZ8sm",
    "merchant_order_reference": "53cf1451-4dfd-417d-a1c8-c8bd603d5200",
    "type": "CHARGE",
    "status": "PENDING",
    "challenge_url": "https://pluraluat.v2.pinepg.in/web/auth/landing/?token=S50f2FXi%2FYAGe2bLZEW%2FA2VHzXthz0m9igmtsP61ODtY5u4pR6RYB5IlJwK0%2Fuo%2FBs9",
    "merchant_id": "111163",
    "order_amount": {
      "value": 1600000,
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
    "allowed_payment_methods": [],
    "purchase_details": {
      "customer": {
        "country_code": "91",
        "billing_address": {},
        "shipping_address": {},
        "is_edit_customer_details_allowed": false
      }
    },
    "payments": [
      {
        "id": "v1-250124055307-aa-6OZ8sm-ce-a",
        "merchant_payment_reference": "c7a7f778-b68f-462b-a6af-50698df12a4a",
        "status": "FAILED",
        "payment_amount": {
          "value": 1550000,
          "currency": "INR"
        },
        "payment_method": "CREDIT_EMI",
        "offer_data": {
          "offer_details": {
            "id": "6",
            "name": "HDFC CC",
            "issuer_type": "CC_BANK",
            "priority": 1,
            "tenure": {
              "tenure_id": "1",
              "name": "3 Months",
              "tenure_type": "MONTH",
              "tenure_value": 3,
              "issuer_offer_parameters": [
                {
                  "program_type": "BANK_EMI",
                  "offer_id": "1803",
                  "offer_parameter_id": "72559"
                },
                {
                  "program_type": "MERCHANT_BANK_OFFER",
                  "offer_id": "1523",
                  "offer_parameter_id": "63566"
                }
              ],
              "details": [],
              "discount": {
                "discount_type": "INSTANT",
                "amount": {
                  "currency": "INR",
                  "value": 50000
                },
                "breakup": {
                  "merchant": {},
                  "issuer": {},
                  "brand": {},
                  "dealer": {}
                }
              },
              "loan_amount": {
                "currency": "INR",
                "value": 1550000
              },
              "total_discount_amount": {
                "currency": "INR",
                "value": 50000
              },
              "net_payment_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "monthly_emi_amount": {
                "currency": "INR",
                "value": 533984
              },
              "total_emi_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "interest_amount": {
                "currency": "INR",
                "value": 51952
              },
              "interest_rate_percentage": 20,
              "processing_fee_details": {
                "amount": {
                  "currency": "INR",
                  "value": 19900
                }
              },
              "processing_fee_amount": {
                "currency": "INR",
                "value": 19900
              },
              "emi_type": "STANDARD"
            }
          }
        },
        "error_detail": {
          "code": "INTERNAL_ERROR",
          "message": "Payment processor is unavailable"
        },
        "created_at": "2025-01-24T05:53:24.476Z",
        "updated_at": "2025-01-24T05:53:25.492Z"
      },
      {
        "id": "v1-250124055307-aa-6OZ8sm-ce-b",
        "merchant_payment_reference": "32e3ba62-bb95-41bb-be81-1b87ab96c0ed",
        "status": "PENDING",
        "payment_amount": {
          "value": 1550000,
          "currency": "INR"
        },
        "payment_method": "CREDIT_EMI",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "INTL HDQTRS-CENTER OWNED",
            "card_category": "Consumer",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN",
            "last4_digit": "1091",
            "save": false,
            "is_native_otp_eligible": true
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "",
          "rrn": "",
          "is_aggregator": true
        },
        "offer_data": {
          "offer_details": {
            "id": "6",
            "name": "HDFC CC",
            "issuer_type": "CC_BANK",
            "priority": 1,
            "tenure": {
              "tenure_id": "1",
              "name": "3 Months",
              "tenure_type": "MONTH",
              "tenure_value": 3,
              "issuer_offer_parameters": [
                {
                  "program_type": "BANK_EMI",
                  "offer_id": "1803",
                  "offer_parameter_id": "72559"
                },
                {
                  "program_type": "MERCHANT_BANK_OFFER",
                  "offer_id": "1523",
                  "offer_parameter_id": "63566"
                }
              ],
              "details": [],
              "discount": {
                "discount_type": "INSTANT",
                "amount": {
                  "currency": "INR",
                  "value": 50000
                },
                "breakup": {
                  "merchant": {},
                  "issuer": {},
                  "brand": {},
                  "dealer": {}
                }
              },
              "loan_amount": {
                "currency": "INR",
                "value": 1550000
              },
              "total_discount_amount": {
                "currency": "INR",
                "value": 50000
              },
              "net_payment_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "monthly_emi_amount": {
                "currency": "INR",
                "value": 533984
              },
              "total_emi_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "interest_amount": {
                "currency": "INR",
                "value": 51952
              },
              "interest_rate_percentage": 20,
              "processing_fee_details": {
                "amount": {
                  "currency": "INR",
                  "value": 19900
                }
              },
              "processing_fee_amount": {
                "currency": "INR",
                "value": 19900
              },
              "emi_type": "STANDARD"
            }
          }
        },
        "created_at": "2025-01-24T05:53:58.092Z",
        "updated_at": "2025-01-24T05:53:59.679Z"
      }
    ],
    "created_at": "2025-01-24T05:53:07.740Z",
    "updated_at": "2025-01-24T05:53:59.680Z",
    "integration_mode": "SEAMLESS",
    "payment_retries_remaining": 8
  }
}
```
```json Tokenized EMI Payment Object
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
    "6-2": "An object that contains the transaction amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#order-amount-child-object\" >Learn more about our `order_amount` child object</a>.",
    "7-0": "pre_auth",
    "7-1": "`boolean`",
    "7-2": "The pre-authorization type.<br><br>Possible values:<ul><li>`true`: When pre-authorization is needed.</li><li>`false`: When pre-authorization is not required.</ul></li>Example: `false`<br><br><a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders\" target=\"_blanck\">Learn more about our pre-authorization.</a>.",
    "8-0": "allowed_payment_methods",
    "8-1": "`array of strings`",
    "8-2": "The type of payment methods you want to offer your customers to accept payments.  \n  \nAccepted values:<ul><li>`CARD`</li><li>`UPI`</li><li>`POINTS`</li><li>`NETBANKING`</li><li>`WALLET`</li><li>`CREDIT_EMI`</li><li>`DEBIT_EMI`</ul></li>Example: `CARD`  \n  \n**Note**: Before selecting a payment method, ensure it is configured for you.",
    "9-0": "`notes`",
    "9-1": "`string`",
    "9-2": "The note you want to show against an order.  \n  \nExample: `Order1`",
    "10-0": "`callback_url`",
    "10-1": "`string`",
    "10-2": "Use this URL to redirect your customers to specific success or failure pages based on the order or product details.  \n  \nExample: `https://sample-callback-url`",
    "11-0": "purchase_details",
    "11-1": "`object`",
    "11-2": "An object that contains the purchase details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#purchase-details-child-object\" >Learn more about our `purchase_details` child object</a>.  \n  \n**Note**: The presence of the key-values pairs in this object depends on the Input request.",
    "12-0": "payments",
    "12-1": "`array of objects`",
    "12-2": "An array of object that contains the payment details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#payments-child-object\" >Learn more about our `payments` child object</a>.  \n  \n**Note**: Payments response object can vary based on the payment methods and payment status.",
    "13-0": "created_at",
    "13-1": "`string`",
    "13-2": "The ISO 8601 UTC Timestamp, when the create order request was received by Plural.  \n  \nExample: `2024-07-09T07:57:08.022Z`",
    "14-0": "updated_at",
    "14-1": "`string`",
    "14-2": "The ISO 8601 UTC Timestamp, when the order response object is updated.  \n  \nExample: `2024-07-09T07:57:08.022Z`",
    "15-0": "integration_mode",
    "15-1": "`string`",
    "15-2": "Type of integration mode you wish to integrate with.  \n  \nAccepted value: <ul><li>`REDIRECT`</li><li>`SEAMLESS`</li><li>`IFRAME`</li></ul>",
    "16-0": "payment_retries_remaining",
    "16-1": "`integer`",
    "16-2": "Payment attempts remaining on the order.  \n  \nExample: `9`"
  },
  "cols": 3,
  "rows": 17,
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
    "0-2": "An object that contains the customer details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#customer-child-object\" >Learn more about our `customer` child object</a>.",
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
    "5-2": "An object that contains the details of the billing address.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#billing-address-child-object\" >Learn more about our `billing_address` child object</a>.",
    "6-0": "shipping_address",
    "6-1": "`object`",
    "6-2": "An object that contains the shipping address details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#shipping-address-child-object\" >Learn more about our `shipping_address` child object</a>."
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
    "3-2": "An object that contains the details of the payment amount.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#payment-amount-child-object\" >Learn more about our `payment_amount` child object</a>.",
    "4-0": "payment_method",
    "4-1": "`string`",
    "4-2": "Type of payment method.<br><br>Accepted values:<ul><li>`CREDIT_EMI`</li><li>`DEBIT_EMI`</li><li>`CARDLESS_EMI`</ul></li>Example: `CREDIT_EMI`",
    "5-0": "payment_option",
    "5-1": "`object`",
    "5-2": "An object that contains the details of the payment options.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#payment-option-child-object\" >Learn more about our `payment_option` child object</a>.",
    "6-0": "acquirer_data",
    "6-1": "`object`",
    "6-2": "An object that contains the details of the acquirer data.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#acquirer-data-child-object\" >Learn more about our `acquirer_data` child object</a>.",
    "7-0": "error_detail",
    "7-1": "`object`",
    "7-2": "An object that contains the error details.<br><br><a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#error-detail-child-object\" >Learn more about our `error_detail` child object</a>.<br><br>**Note**: This object is returned only for the failed payment.",
    "8-0": "capture_data",
    "8-1": "`object`",
    "8-2": "An object that contains the details of the capture data.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#capture-data-child-object\" >Learn more about our `capture_data` child object</a>.  \n  \n**Note**: The presence of the key-value pairs against this object depends on the pre-authorization type.",
    "9-0": "offer_data",
    "9-1": "`object`",
    "9-2": "An object that contains the offer details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/affordability-suite-object#offer-data-child-object\" >Learn more about our `offer_data` child object</a>.",
    "10-0": "created_at",
    "10-1": "`string`",
    "10-2": "The ISO 8601 UTC Timestamp, when the create payment request was received by Plural.  \n  \nExample: `2024-07-11T06:52:12.484Z`",
    "11-0": "updated_at",
    "11-1": "`string`",
    "11-2": "The ISO 8601 UTC Timestamp, when the payment response object is updated.  \n  \nExample: `2024-07-11T06:59:38.260Z`"
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
    "1-2": "An object that contains the capture amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/payments-object#capture-amount-child-object\" >Learn more about our `capture_amount` child object</a>.",
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


### Offer Data [Child Object]

The table below lists the various parameters in the `offer_data` child object. This object is part of the `payments` object.

| Parameter     | Type     | Description                                |
| :------------ | :------- | :----------------------------------------- |
| offer_details | `object` | An object that contains the offer details. |

#### Offer Details [Child Object]

The table below lists the various parameters in the `offer_details` child object. This object is part of the `offer_data` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "id",
    "0-1": "`String`",
    "0-2": "Unique identifier of the issuer id in the Plural database.  \n  \nExample: `23`",
    "1-0": "name",
    "1-1": "`String`",
    "1-2": "Name of the Issuer.  \n  \nExample: `INDUSIND CC`",
    "2-0": "`display_name`",
    "2-1": "`string`",
    "2-2": "Name of the issuer offering the offer.  \n  \nExample: `INDUSIND`",
    "3-0": "issuer_type",
    "3-1": "`String`",
    "3-2": "The type of the Issuer offering the offer.  \n  \nAccepted values: <ul><li>`CC_BANK`</li><li>`DC_BANK`</ul></li>.",
    "4-0": "priority",
    "4-1": "`integer`",
    "4-2": "The priority of the issuer providing the offer.  \n  \nExample: `1`",
    "5-0": "tenures",
    "5-1": "`array of objects`",
    "5-2": "An array of objects that contains the tenures details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/affordability-suite-object#tenures-child-object\" >Learn more about the `tenures` child object.</a>"
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


### Tenures [Child Object]

The table below lists the various parameters in the `tenures` object. This is part of the offer discovery response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "tenure_id",
    "0-1": "`String`",
    "0-2": "Tenure id in the Plural database.  \n  \nExample: `1`",
    "1-0": "name",
    "1-1": "`String`",
    "1-2": "The name of the Issuer offering the offer..  \n  \nExample: `3 Months`",
    "2-0": "tenure_type",
    "2-1": "`String`",
    "2-2": "The type of the Tenure.  \n  \nAccepted values: <ul><li>`MONTH`</ul></li>.",
    "3-0": "tenure_value",
    "3-1": "`integer`",
    "3-2": "The value of the tenure.  \n  \nExample: `3`",
    "4-0": "issuer_offer_parameters",
    "4-1": "`array of objects`",
    "4-2": "An array of objects that contains the `issuer_offer_parameters` details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/affordability-suite-object#issuer-offer-parameters-child-object\" >Learn more about the `issuer_offer_parameters` child object.</a>",
    "5-0": "details",
    "5-1": "`array of objects`",
    "5-2": "An array of objects that contains the `product details`.  \n  \n<a href=\"https://developer.pluralonline.com/reference/affordability-suite-object#details-child-object\" >Learn more about the `details` child object.</a>",
    "6-0": "discount",
    "6-1": "`object`",
    "6-2": "An object that contains the discount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/affordability-suite-object#discount-child-object\" >Learn more about the `discount` child object.</a>",
    "7-0": "loan_amount",
    "7-1": "`object`",
    "7-2": "An object that contains the loan amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/affordability-suite-object#loan-amount-child-object\" >Learn more about the `loan_amount` child object.</a>",
    "8-0": "total_discount_amount",
    "8-1": "`object`",
    "8-2": "An object that contains the total discount amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/affordability-suite-object#total-discount-amount-child-object\" >Learn more about the `total_discount_amount` child object.</a>",
    "9-0": "net_payment_amount",
    "9-1": "`object`",
    "9-2": "An object that contains the net payment amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/affordability-suite-object#net-payment-amount-child-object\" >Learn more about the `net_payment_amount` child object.</a>",
    "10-0": "monthly_emi_amount",
    "10-1": "`object`",
    "10-2": "An object that contains the monthly EMI amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/affordability-suite-object#monthly-emi-amount-child-object\" >Learn more about the `monthly_emi_amount` child object.</a>",
    "11-0": "total_emi_amount",
    "11-1": "`object`",
    "11-2": "An object that contains the total EMI amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/affordability-suite-object#total-emi-amount-child-object\" >Learn more about the `total_emi_amount` child object.</a>",
    "12-0": "interest_amount",
    "12-1": "`object`",
    "12-2": "An object that contains the interest amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/affordability-suite-object#interest-amount-child-object\" >Learn more about the `interest_amount` child object.</a>",
    "13-0": "interest_rate_percentage",
    "13-1": "`float`",
    "13-2": "Interest rate percentage for the tenure.  \n  \nExample: `16.90`",
    "14-0": "processing_fee_details",
    "14-1": "`object`",
    "14-2": "An object that contains the processing fee details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/affordability-suite-object#processing-fee-details-child-object\" >Learn more about the `processing_fee_details` child object.</a>",
    "15-0": "emi_type",
    "15-1": "`strings`",
    "15-2": "Type of EMI.  \n  \nExample: `STANDARD`  \n  \nAccepted values: <ul><li>`LOW_COST`</li><li>`NO_COST`</li><li>`STANDARD`</ul></li>"
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


#### Issuer Offer Parameters [Child Object]

The table below lists the various parameters in the `issuer_offer_parameters` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "program_type",
    "0-1": "`String`",
    "0-2": "Unique identifier of the issuer id in the Plural database.  \n  \nExample: `23`",
    "1-0": "offer_id",
    "1-1": "`String`",
    "1-2": "Name of the Issuer.  \n  \nExample: `INDUSIND CC`",
    "2-0": "offer_parameter_id",
    "2-1": "`String`",
    "2-2": "The type of the Issuer offering the offer.  \n  \nAccepted values: <ul><li>`Credit`</li><li>`Debit`</li><li>`Cardless`</li><li>`NBFC`</ul></li>."
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


#### Details [Child Object]

The table below lists the various parameters in the `details` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "product_code",
    "0-1": "`String`",
    "0-2": "Unique Product identifier of the product.  \n  \nExample: `redmi_1`",
    "1-0": "brand_id",
    "1-1": "`String`",
    "1-2": "Unique brand identifier of the product.  \n  \nExample: `3`",
    "2-0": "product_offer_parameters",
    "2-1": "`array of objects`",
    "2-2": "An array of objects that contains the product offer schemes for the product EMI details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/affordability-suite-object#product-offer-parameters-child-object\" >Learn more about the `product_offer_parameters` child object.</a>",
    "3-0": "product_amount",
    "3-1": "`object`",
    "3-2": "An object that contains the product amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/affordability-suite-object#product-amount-child-object\" >Learn more about the `product_amount` child object.</a>",
    "4-0": "subvention",
    "4-1": "`object`",
    "4-2": "An object that contains the subvention details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/affordability-suite-object#subvention-child-object\" >Learn more about the `subvention` child object.</a>",
    "5-0": "discount",
    "5-1": "`object`",
    "5-2": "An object that contains the product discount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/affordability-suite-object#discount-child-object\" >Learn more about the `discount` child object.</a>"
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


##### Product Offer Parameters [Child Object]

The table below lists the various parameters in the `product_offer_parameters` child object. This is part of the `details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "program_type",
    "0-1": "`String`",
    "0-2": "Type of the Program.  \n  \nExample: `BRAND_EMI`  \n  \nAccepted values: <ul><li>`BRAND_EMI`</li><li>`BANK_EMI`</li><li>`MERCHANT_BRAND_OFFER`</li><li>`MERCHANT_BANK_OFFER`</li><li>`BRAND_OFFER`</li><li>`MY_EMI`</ul></li>",
    "1-0": "offer_id",
    "1-1": "`string`",
    "1-2": "Unique identifier of the offer.  \n  \nExample: `309`",
    "2-0": "offer_parameter_id",
    "2-1": "`string`",
    "2-2": "Unique offer parameter identifier.  \n  \nExample: `20` "
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


##### Product Amount [Child Object]

The table below lists the various parameters in the `product_amount` child object. This is part of the `details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
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


##### Subvention [Child Object]

The table below lists the various parameters in the `subvention` child object. This is part of the `details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "subvention_type",
    "0-1": "`String`",
    "0-2": "Type of subvention.  \n  \nExample: `INSTANT`  \n  \nAccepted values:<ul><li>`INSTANT`</li><li>`POST`</ul></li>",
    "1-0": "offer_type",
    "1-1": "`string`",
    "1-2": "Type of the offer.  \n  \nAccepted values: <ul><li>`LOW_COST`</li><li>`NO_COST`</li><li>`STANDARD`</ul></li>",
    "2-0": "percentage",
    "2-1": "`integer`",
    "2-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`",
    "3-0": "amount",
    "3-1": "`object`",
    "3-2": "An object that contains the subvention amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object\" >Learn more about the `amount` child object.</a>",
    "4-0": "breakup",
    "4-1": "`object`",
    "4-2": "An object that contains the subvention breakup details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#breakup-child-object\" >Learn more about the `breakup` child object.</a>"
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


###### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `subvention` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
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


###### Breakup [Child Object]

The table below lists the various parameters in the `breakup` child object. This is part of the `subvention` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "brand",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup details of the brand.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#brand-child-object\" >Learn more about the `brand` child object.</a>"
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


###### Brand [Child Object]

The table below lists the various parameters in the `brand` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup amount details of the brand.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object-1\" >Learn more about the `amount` child object.</a>"
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


###### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `brand` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
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


#### Discount [Child Object]

The table below lists the various parameters in the `discount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "discount_type",
    "0-1": "`String`",
    "0-2": "Type of discount.  \n  \nPossible values:<ul><li>`INSTANT`</li><li>`DEFERRED`</ul></li>",
    "1-0": "percentage",
    "1-1": "`Double`",
    "1-2": "The discount percentage provided by the offering entity.  \n  \nExample: `16.90`",
    "2-0": "amount",
    "2-1": "`string`",
    "2-2": "Discount amount.  \n  \nExample: `2000`",
    "3-0": "discount_deferred_duration_value",
    "3-1": "`integer`",
    "3-2": "The duration value for the deferred discount.  \n  \nExample: ",
    "4-0": "discount_deferred_duration_type",
    "4-1": "`string`",
    "4-2": "Discount duration type deferred.  \n  \nPossible values: <ul><li>`DAY`</li><li>`MONTH`</ul></li>",
    "5-0": "breakup",
    "5-1": "`object`",
    "5-2": "An object that contains the product offer details with breakup.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#breakup-child-object-1\" >Learn more about the `breakup` child object.</a>"
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


##### Breakup [Child Object]

The table below lists the various parameters in the `breakup` child object. This is part of the `discount` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant",
    "0-1": "`object`",
    "0-2": "An object that contains the merchant breakup details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#merchant-child-object\" >Learn more about the `breakup` child object.</a>",
    "1-0": "issuer",
    "1-1": "`object`",
    "1-2": "An object that contains the issure breakup details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#issuer-child-object\" >Learn more about the `breakup` child object.</a>",
    "2-0": "brand",
    "2-1": "`object`",
    "2-2": "An object that contains the brand breakup details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#brand-child-object-1\" >Learn more about the `breakup` child object.</a>",
    "3-0": "dealer",
    "3-1": "`object`",
    "3-2": "An object that contains the dealer breakup details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#dealer-child-object\" >Learn more about the `breakup` child object.</a>"
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


###### Merchant [Child Object]

The table below lists the various parameters in the `merchant` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object-2\" >Learn more about the amount child object.</a>"
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


###### Issuer [Child Object]

The table below lists the various parameters in the `issure` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object-2\" >Learn more about the amount child object.</a>"
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


###### Brand [Child Object]

The table below lists the various parameters in the `brand` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object-2\" >Learn more about the amount child object.</a>"
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


###### Dealer [Child Object]

The table below lists the various parameters in the `dealer` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object-2\" >Learn more about the amount child object.</a>"
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


#### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
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


#### Loan Amount [Child Object]

The table below lists the various parameters in the `loan_amount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
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


#### Total Discount Amount [Child Object]

The table below lists the various parameters in the `total_discount_amount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
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


#### Net Payment Amount [Child Object]

The table below lists the various parameters in the `net_payment_amount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
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


#### Monthly EMI Amount [Child Object]

The table below lists the various parameters in the `monthly_emi_amount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
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


#### Total EMI Amount [Child Object]

The table below lists the various parameters in the `total_emi_amount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
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


#### Interest Amount [Child Object]

The table below lists the various parameters in the `interest_amount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
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


#### Processing Fee Details [Child Object]

The table below lists the various parameters in the `processing_fee_details` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
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
