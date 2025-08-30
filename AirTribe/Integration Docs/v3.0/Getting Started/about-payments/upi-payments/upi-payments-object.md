---
title: "Object"
slug: "upi-payments-object"
excerpt: "Overview of the UPI payment response object."
hidden: false
createdAt: "Thu Sep 12 2024 09:06:05 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Apr 09 2025 05:33:42 GMT+0000 (Coordinated Universal Time)"
---
Shown below is a sample response of a Create Payments API through payment method as `UPI`.

```json UPI Collect Response Object
{
  "data": {
    "order_id": "v1-240820090251-aa-xwuI7J",
    "merchant_order_reference": "8200c7f7-4490-4970-b6bb-40ffa05d47e5",
    "type": "CHARGE",
    "status": "PENDING",
    "challenge_url": "upi://pay?mode=04&pa=pinelabs.24092@hdfcbank&pn=Pine%20Test&mc=6012&cu=INR&am=1.00&tr=68706&tn=Payment%20for%20v1",
    "merchant_id": "110047",
    "order_amount": {
      "value": 100,
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
    "payments": [
      {
        "id": "v1-240820090251-aa-xwuI7J-up-6",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PENDING",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "UPI",
        "payment_option": {
          "upi_details": {
            "txn_mode": "COLLECT",
            "payer": {
              "vpa": "kevinbob@example"
            }
          },
          "acquirer_data": {
            "approval_code": "",
            "acquirer_reference": "",
            "rrn": "",
            "is_aggregator": true
          },
          "created_at": "2024-08-20T09:02:51.265Z",
          "updated_at": "2024-08-20T09:03:01.208Z"
        }
      }
    ],
    "created_at": "2024-08-20T09:02:51.265Z",
    "updated_at": "2024-08-20T09:03:01.208Z"
  }
}
```
```json UPI Intent Response Object
{
  "data": {
    "order_id": "v1-240820090251-aa-xwuI7J",
    "merchant_order_reference": "8200c7f7-4490-4970-b6bb-40ffa05d47e5",
    "type": "CHARGE",
    "status": "PENDING",
    "challenge_url": "upi://pay?mode=04&pa=pinelabs.24092@hdfcbank&pn=Pine%20Test&mc=6012&cu=INR&am=1.00&tr=68706&tn=Payment%20for%20v1",
    "merchant_id": "110047",
    "order_amount": {
      "value": 100,
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
    "payments": [
      {
        "id": "v1-240820090251-aa-xwuI7J-up-6",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PENDING",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "UPI",
        "payment_option": {
          "upi_details": {
            "txn_mode": "INTENT"
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2024-08-20T09:02:51.265Z",
        "updated_at": "2024-08-20T09:03:01.208Z"
      }
    ],
    "created_at": "2024-08-20T09:02:51.265Z",
    "updated_at": "2024-08-20T09:03:01.208Z"
  }
}
```
```json UPI Intent with QR Flow Response Object
{
  "data": {
    "order_id": "v1-250102053141-aa-TRBQR6",
    "merchant_order_reference": "f5cba4a4-1c46-4b23-b0a8-7fd6b8027f63",
    "type": "CHARGE",
    "status": "PENDING",
    "challenge_url": "upi://pay?mode=04&pa=pinelabs.1068@hdfcbank&pn=Saklani%20Bhai%20Upi&mc=6012&cu=INR&am=1.00&tr=3562571&tn=Payment%20for%20v1",
    "merchant_id": "110939",
    "order_amount": {
      "value": 100,
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
    "purchase_details": {
      "customer": {
        "email_id": "aayush.sam@gmail.com",
        "first_name": "joe",
        "last_name": "kumar",
        "customer_id": "192212",
        "mobile_number": "192192883",
        "billing_address": {
          "address1": "H.No 15, Sector 17",
          "pincode": "61232112",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        },
        "shipping_address": {
          "address1": "H.No 15, Sector 17",
          "address2": "string",
          "address3": "string",
          "pincode": "144001123",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        }
      },
      "merchant_metadata": {
        "key1": "value1",
        "key2": "value2"
      }
    },
    "payments": [
      {
        "id": "v1-250102053141-aa-TRBQR6-up-a",
        "merchant_payment_reference": "2c8f71b3-2eb0-47af-a18a-52699785f153",
        "status": "PENDING",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "UPI",
        "payment_option": {
          "upi_data": {
            "txn_mode": "INTENT"
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2025-01-02T05:32:08.847Z",
        "updated_at": "2025-01-02T05:32:11.798Z"
      }
    ],
    "created_at": "2025-01-02T05:31:41.687Z",
    "updated_at": "2025-01-02T05:32:11.799Z",
    "image_url": "https://upi-gateway-service-bucket.s3.ap-south-1.amazonaws.com/qr_images/110939/2025-01-02/3562571.png?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCmFwLXNvdXRoLTEiRzBFAiEAtxkyw5wTlnnU1YO%2FCCMoce1%2BK1MsaRStLaa8JcSywhcCIBmqqVHbdrmRaaTskcFJ2aQXvMoLWeXBRVcHgNu036P1Kp0FCM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMzA1NzE0MjgxODMwIgw%2FI8Yx5QqHlvdZSmUq8QS1o4FILej9eD96%2FSFv7vcS%2BxR8ink0aM5I0JT9TmDzgIZxAm0eszCWY%2BbLzffWlGDdtn806WJN2pieXpDuxOBmchQssqbcOP%2FIk%2BuQ5imve75JNCx7G%2FnVFnbKOYo4ct5LP%2BC5TIzzYxYC4IPid7xgehDKeVcu%2Bcvv03xwoqs19NHfVDqnGZ1lT%2Fqtj1EyP18zd1HqXI5AXGud2FvPqpwmno6%2F11i2JxytTHm%2B%2BhKVgSwYnUqygrOxjfDsb57EEWNwKQmnZ1a4%2BSTfk67PlQ%2FTpCWA61f72yzdFlIJ3ehQTkVI7vyBSX%2FnlyWN0mfI1VB3OhUHiPbjHlAMRKm5dKT6ewujM3q9jbip6a9XUk%2F3JR%2B%2BHxn0ygvGdP3VJhEIlCK7%2FRWmaozqKEKblkDGTokpqdA6ma4SS40GY4KQsWlkHnL8yjtz%2B1BtkToWy5W8S1%2BkpbmFP0Y745gYLE2U2wD3hVVDJdZUYskZjjCmUhbYa%2BiXOpjnWEulK795XKau3B7jovIoexKR%2Fnmw5FzsL9VhSuMsv75QWsqopztCSWWJN9DKaHZQ3asyjEZJj95Xz3H3cV%2FVRmcAxfD9YmtsdJ8EwBT36RJYr8mJo4fJOWswCQWa0NJ7gTzPWMK7aQhzMqDOeDGrzi72R3TQzkxNR7jYxoYggrHtsv%2BFY1XM3rhxn5ayVQ%2FfglQ1VaNmKDNPTK6CUzIILTg2csb%2FS5Xy0LyR2IR4r2S4%2BIqL66dUyRRlPVvXgv6Qv3kSivJ6YafhcSbDZAfxd3%2F%2BUcqVnJh3k7BnRoA5DnMzUtX5oN2SMyXOvwd5TcGVCVDF2AcoQRD%2ByatYMNvJ2LsGOpsBiR4DGjV%2FDkHj1IYcZTEm2STYa5v43ga5J7x%2BUfR9vPxlaYIAMqr4hc9sediH585AP%2FQ8Xfa9ynuZ9j210J6bMvIjycUjwzReD1jo%2B6rcDcOoZRF8tu3sqTjUuGFCDl5H0I5wqJ8XuAY1ZvYIliiA0szPwoazo%2BgRzUZjv7wCEkwk7bvyzSjM0P19SgAJYPewfmbPWabEhk7bWFI%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20250102T053211Z&X-Amz-SignedHeaders=host&X-Amz-Credential=ASIAUOLP5XVTC44HP7KZ%2F20250102%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Expires=1200&X-Amz-Signature=39ab101fb90f02314fdcf32d9786b2c78484dc729b80b186e84250400612933f",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Subscription UPI Collect Response Object
{
  "data": {
    "order_id": "v1-250408102515-aa-x2F8Qw",
    "merchant_order_reference": "8b5e2b5b-9fde-4010-af9c-281f9e2fa5af",
    "type": "CHARGE",
    "status": "PENDING",
    "challenge_url": "upi://mandate?pa=PinelabsUat1@icici&pn=PinelabsUat&tr=EZM2025032516184000196272&am=1000.00&cu=INR&orgid=400011&mc=5732&purpose=01&tn=remark&validitystart=25032025&validityend=21062025&amrule=EXACT&Recur=ONETIME&Rev=Y&Share=Y&Block=Y&txnType=CREATE&mode=13&sign=MEYCIQCHkSEsp0e+y2chLL5s+bvkY06b4NbA9gcl9fMykq4WaAIhAJEMQ9h5SOi6/Z+q/9gHGX4cH7RnwacTU5OpZ3nU3C3i",
    "callback_url": "www.google.com",
    "failure_callback_url": "www.example.com/failure",
    "merchant_id": "106639",
    "order_amount": {
      "value": 100000,
      "currency": "INR"
    },
    "pre_auth": false,
    "allowed_payment_methods": [
      "UPI"
    ],
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@gmail.com",
        "first_name": "kevin",
        "last_name": "bob",
        "mobile_number": "9667195458",
        "country_code": "91",
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
        },
        "is_edit_customer_details_allowed": false
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-250408102515-aa-x2F8Qw-up-c",
        "merchant_payment_reference": "6b4d003f-0918-45d3-aef0-e21af0f36771",
        "status": "PENDING",
        "payment_amount": {
          "value": 100000,
          "currency": "INR"
        },
        "payment_method": "UPI",
        "upi_details":{
            "txn_mode":"COLLECT",
            "payer":{
              "vpa":"kevin.bob@examplebank.com"
            }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2025-04-08T11:54:56.092Z",
        "updated_at": "2025-04-08T11:55:00.001Z",
        "mandate_info": {
          "request_type": "CREATE_MANDATE"
        }
      }
    ],
    "created_at": "2025-04-08T10:25:15.093Z",
    "updated_at": "2025-04-08T11:55:00.001Z",
    "integration_mode": "REDIRECT",
    "payment_retries_remaining": 7
  }
}
```
```json Subscription UPI Intent Response Object
{
  "data": {
    "order_id": "v1-250408102515-aa-x2F8Qw",
    "merchant_order_reference": "8b5e2b5b-9fde-4010-af9c-281f9e2fa5af",
    "type": "CHARGE",
    "status": "PENDING",
    "challenge_url": "upi://mandate?pa=PinelabsUat1@icici&pn=PinelabsUat&tr=EZM2025032516184000196272&am=1000.00&cu=INR&orgid=400011&mc=5732&purpose=01&tn=remark&validitystart=25032025&validityend=21062025&amrule=EXACT&Recur=ONETIME&Rev=Y&Share=Y&Block=Y&txnType=CREATE&mode=13&sign=MEYCIQCHkSEsp0e+y2chLL5s+bvkY06b4NbA9gcl9fMykq4WaAIhAJEMQ9h5SOi6/Z+q/9gHGX4cH7RnwacTU5OpZ3nU3C3i",
    "callback_url": "www.google.com",
    "failure_callback_url": "www.example.com/failure",
    "merchant_id": "106639",
    "order_amount": {
      "value": 100000,
      "currency": "INR"
    },
    "pre_auth": false,
    "allowed_payment_methods": [
      "UPI"
    ],
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@gmail.com",
        "first_name": "kevin",
        "last_name": "bob",
        "mobile_number": "9667195458",
        "country_code": "91",
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
        },
        "is_edit_customer_details_allowed": false
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-250408102515-aa-x2F8Qw-up-c",
        "merchant_payment_reference": "6b4d003f-0918-45d3-aef0-e21af0f36771",
        "status": "PENDING",
        "payment_amount": {
          "value": 100000,
          "currency": "INR"
        },
        "payment_method": "UPI",
        "payment_option": {
          "upi_data": {
            "txn_mode": "INTENT"
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2025-04-08T11:54:56.092Z",
        "updated_at": "2025-04-08T11:55:00.001Z",
        "mandate_info": {
          "request_type": "CREATE_MANDATE"
        }
      }
    ],
    "created_at": "2025-04-08T10:25:15.093Z",
    "updated_at": "2025-04-08T11:55:00.001Z",
    "integration_mode": "REDIRECT",
    "payment_retries_remaining": 7
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
    "6-2": "An object that contains the transaction amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/upi-payments-object#order-amount-child-object\" >Learn more about our `order_amount` child object</a>.",
    "7-0": "pre_auth",
    "7-1": "`boolean`",
    "7-2": "The pre-authorization type.<br><br>Possible values:<ul><li>`true`: When pre-authorization is needed.</li><li>`false`: When pre-authorization is not required.</ul></li>Example: `false`<br><br><a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/orders\" target=\"_blanck\">Learn more about our pre-authorization.</a>",
    "8-0": "allowed_payment_methods",
    "8-1": "`array of strings`",
    "8-2": "The type of payment methods you want to offer your customers to accept payments.  \n  \nAccepted values:<ul><li>`CARD`</li><li>`UPI`</li><li>`POINTS`</li><li>`NETBANKING`</li><li>`WALLET`</li><li>`CREDIT_EMI`</li><li>`DEBIT_EMI`</ul></li>Example: `CARD`  \n  \n**Note**: Before selecting a payment method, ensure it is configured for you.",
    "9-0": "notes",
    "9-1": "`string`",
    "9-2": "The note you want to show against an order.  \n  \nExample: `Order1`",
    "10-0": "callback_url",
    "10-1": "`string`",
    "10-2": "Use this URL to redirect your customers to specific success or failure pages based on the order or product details.  \n  \nExample: `https\\://sample-callback-url`",
    "11-0": "failure_callback_url",
    "11-1": "`string`",
    "11-2": "The URL specifically used to redirect customers to a failure page based on the order or product details.  \n  \nExample: `https://sample-failure-callback-url`  \n  \n**Note**:<ul><li>If the `failure_callback_url` is not provided, customers will be redirected to the `callback_url` for both successful and failed transactions.</li><li>If the `failure_callback_url` is provided, the `callback_url` will be used exclusively for successful transactions, while the `failure_callback_url` will be used for failed transactions.</li><li>If neither URL is provided, the default URL configured during merchant onboarding will be used.</ul></li>",
    "12-0": "purchase_details",
    "12-1": "`object`",
    "12-2": "An object that contains the purchase details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/upi-payments-object#purchase-details-child-object\" >Learn more about our `purchase_details` child object</a>.  \n  \n**Note**: The presence of the key-values pairs in this object depends on the Input request.",
    "13-0": "payments",
    "13-1": "`array of objects`",
    "13-2": "An array of object that contains the payment details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/upi-payments-object#payments-child-object\" >Learn more about our `payments` child object</a>.  \n  \n**Note**: Payments response object can vary based on the payment methods and payment status.",
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
    "5-2": "An object that contains the details of the billing address.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/upi-payments-object#billing-address-child-object\" >Learn more about our `billing_address` child object</a>.",
    "6-0": "shipping_address",
    "6-1": "`object`",
    "6-2": "An object that contains the shipping address details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/upi-payments-object#shipping-address-child-object\" >Learn more about our `shipping_address` child object</a>."
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
    "1-2": "A unique Payment Reference id sent by merchant. <br><br>Example:`008cf04b-a770-4777-854e-b1e6c1230609`",
    "2-0": "status",
    "2-1": "`string`",
    "2-2": "Payment status.<br><br>Possible values:<ul><li>`PENDING`: When the create payment API request is successfully received by Plural.</li><li>`AUTHORIZED`: **Only when `pre_auth` is `true`**. When the payment is ready for authorization.</li><li>`CANCELLED`: When the payment gets cancelled.</li><li>`PROCESSED`: When the payment is successfully received by Plural.</li><li>`FAILED`: When the payment fails, this can be for many reasons such as canceling payments, etc.</ul></li>Example: `PENDING`",
    "3-0": "payment_amount",
    "3-1": "`object`",
    "3-2": "An object that contains the details of the payment amount.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/upi-payments-object#payment-amount-child-object\" >Learn more about our `payment_amount` child object</a>.",
    "4-0": "payment_method",
    "4-1": "`string`",
    "4-2": "Type of payment method.<br><br>Accepted values:<ul><li>`CARD`</li><li>`UPI`</li><li>`POINTS`</ul></li>Example: `CARD`",
    "5-0": "payment_option",
    "5-1": "`object`",
    "5-2": "An object that contains the details of the payment options.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/upi-payments-object#payment-option-child-object\" >Learn more about our `payment_option` child object</a>.",
    "6-0": "acquirer_data",
    "6-1": "`object`",
    "6-2": "An object that contains the details of the acquirer data.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/upi-payments-object#acquirer-data-child-object\" >Learn more about our `acquirer_data` child object</a>.",
    "7-0": "error_detail",
    "7-1": "`object`",
    "7-2": "An object that contains the error details.<br><br><a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/upi-payments-object#error-detail-child-object\" >Learn more about our `error_detail` child object</a>.<br><br>**Note**: This object is returned only for the failed payment.",
    "8-0": "capture_data",
    "8-1": "`object`",
    "8-2": "An object that contains the details of the capture data.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/upi-payments-object#capture-data-child-object\" >Learn more about our `capture_data` child object</a>.  \n  \n**Note**: The presence of the key-value pairs against this object depends on the pre-authorization type.",
    "9-0": "created_at",
    "9-1": "`string`",
    "9-2": "The ISO 8601 UTC Timestamp, when the create order request was received by Plural.  \n  \nExample: `2024-08-20T09:02:51.265Z`",
    "10-0": "updated_at",
    "10-1": "`string`",
    "10-2": "The ISO 8601 UTC Timestamp, when the order response object is updated.  \n  \nExample: `2024-08-20T09:03:01.208Z`"
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
    "0-0": "upi_details",
    "0-1": "`object`",
    "0-2": "An object that contains the upi details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/upi-payments-object#upi-details-child-object\" >Learn more about our `upi_details` child object</a>."
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


#### UPI Details [Child Object]

The table below lists the various parameters in the `upi_details` child object. This object is part of the `payment_option` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "txn_mode",
    "0-1": "`string`",
    "0-2": "Type of UPI transaction.<br><br>Accepted values:<ul><li>`COLLECT`</li><li>`INTENT`</ul></li>Example: `COLLECT`",
    "1-0": "payer",
    "1-1": "`object`",
    "1-2": "An object that contains the payer details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/upi-payments-object#payer-child-object\" >Learn more about our `payer` child object</a>.  \n  \n**Note**: Mandatory for UPI collect only."
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


#### Payer [Child Object]

The table below lists the various parameters in the `payer` child object. This object is part of the `upi_details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "vpa",
    "0-1": "`string`",
    "0-2": "VPA handle of your customer from whom you want to accept payment.<ul><li>Minimum length: 2 characters.</li><li>Maximum length: 256 characters</ul></li>Example: `kevinbob@example`<br><br>Supported characters:<ul><li>`A-Z`</li><li>`a-z`</li><li>`0-9`</li><li>`@`</li><li>`$`</ul></li>"
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
    "1-2": "An object that contains the capture amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/v3.0/reference/upi-payments-object#capture-amount-child-object\" >Learn more about our `capture_amount` child object</a>.",
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
