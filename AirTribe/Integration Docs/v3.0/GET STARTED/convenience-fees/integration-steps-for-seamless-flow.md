---
title: "Integration Steps"
slug: "integration-steps-for-seamless-flow"
excerpt: "Learn how you can integrate with Plural APIs to start accepting payments including convenience fee."
hidden: false
createdAt: "Fri Dec 13 2024 06:07:24 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Mar 24 2025 10:37:09 GMT+0000 (Coordinated Universal Time)"
---
Follow the below steps to integrate with Plural seamless checkout APIs in your application.

1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-for-seamless-flow#1-prerequisite-generate-token" >\[Prerequisite] Generate Token</a>
2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-for-seamless-flow#2-create-order" >Create Order</a>
3. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-for-seamless-flow#3-calculate-convenience-fee" >Calculate Convenience Fee</a>
4. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-for-seamless-flow#4-create-payment" >Create Payment</a>
5. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-for-seamless-flow#5-handle-payment" >Handle Payment</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-for-seamless-flow#51-store-payment-details-on-your-server" >Store Payment Details on Your Server</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-for-seamless-flow#52-verify-payment-signature" >Verify Payment Signature</a>

> 📘 Note
> 
> - Ensure you store your Client ID and Secret in your Backend securely.
> - Integrate our APIs on your backend system.
> - We strictly recommend not to call our APIs from the frontend.

## 1. [Prerequisite] Generate Token

> 🚧 Watch Out
> 
> - To Integrate with Plural seamless checkout flow you must have a PCI compliance certificate.

Integrate our Generate Token API in your backend servers to generate the access token. Use the token generated to authenticate Plural APIs.

Below are the sample requests and response for the Generate Token API.

```curl cURL – UAT
curl --location 'https://pluraluat.v2.pinepg.in/api/auth/v1/token' \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--data '
{
  "client_id": "a17ce30e-f88e-4f81-ada1-c3b4909ed232",
  "client_secret": "fgwei7egyhuggwp39w8rh",
  "grant_type": "client_credentials"
}
'
```
```curl cURL – PROD
curl --location 'https://api.pluralpay.in/api/auth/v1/token' \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--data '
{
  "client_id": "a17ce30e-f88e-4f81-ada1-c3b4909ed232",
  "client_secret": "fgwei7egyhuggwp39w8rh",
  "grant_type": "client_credentials"
}
'
```
```json Sample Response
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
  "expires_in": 3600
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/v3.0/reference/generate-token" target="_blank">Generate Token API</a> documentation to learn more.

## 2. Create Order

To create an Order, use our Create Order API, for authentication use the generated access token in the headers of the API request.

Below are the sample requests and response for a Create Order API.

```curl cURL - UAT
curl --location 'https://pluraluat.v2.pinepg.in/api/pay/v1/orders' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
--header 'Content-Type: application/json' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'accept: application/json' \
--data '
{
  "merchant_order_reference":112345,
  "order_amount":{
    "value":1100,
    "currency":"INR"
  },
  "pre_auth":false,
  "callback_url":"https://sample-callback-url",
  "failure_callback_url": "https://sample-failure-callback-url",
  "allowed_payment_methods":[
    "CARD",
    "UPI",
    "NETBANKING",
    "POINTS",
    "WALLET"
  ],
  "notes":"order1",
  "callback_url":"https://sample-callback-url",
  "purchase_details":{
    "customer":{
      "email_id":"kevin.bob@example.com",
      "first_name":"Kevin",
      "last_name":"Bob",
      "customer_id":"123456",
      "mobile_number":"9876543210",
      "billing_address":{
        "address1":"10 Downing Street Westminster London",
        "address2":"Oxford Street Westminster London",
        "address3":"Baker Street Westminster London",
        "pincode":"51524036",
        "city":"Westminster",
        "state":"Westminster",
        "country":"London"
      },
      "shipping_address":{
        "address1":"10 Downing Street Westminster London",
        "address2":"Oxford Street Westminster London",
        "address3":"Baker Street Westminster London",
        "pincode":"51524036",
        "city":"Westminster",
        "state":"Westminster",
        "country":"London"
      }
    },
    "merchant_metadata":{
      "key1":"DD",
      "key2":"XOF"
    }
  }
}
'
```
```curl cURL - PROD
curl --location 'https://api.pluralpay.in/api/pay/v1/orders' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
--header 'Content-Type: application/json' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'accept: application/json' \
--data '
{
  "merchant_order_reference":112345,
  "order_amount":{
    "value":1100,
    "currency":"INR"
  },
  "pre_auth":false,
  "callback_url":"https://sample-callback-url",
  "failure_callback_url": "https://sample-failure-callback-url",
  "allowed_payment_methods":[
    "CARD",
    "UPI",
    "NETBANKING",
    "POINTS",
    "WALLET"
  ],
  "notes":"order1",
  "callback_url":"https://sample-callback-url",
  "purchase_details":{
    "customer":{
      "email_id":"kevin.bob@example.com",
      "first_name":"Kevin",
      "last_name":"Bob",
      "customer_id":"123456",
      "mobile_number":"9876543210",
      "billing_address":{
        "address1":"10 Downing Street Westminster London",
        "address2":"Oxford Street Westminster London",
        "address3":"Baker Street Westminster London",
        "pincode":"51524036",
        "city":"Westminster",
        "state":"Westminster",
        "country":"London"
      },
      "shipping_address":{
        "address1":"10 Downing Street Westminster London",
        "address2":"Oxford Street Westminster London",
        "address3":"Baker Street Westminster London",
        "pincode":"51524036",
        "city":"Westminster",
        "state":"Westminster",
        "country":"London"
      }
    },
    "merchant_metadata":{
      "key1":"DD",
      "key2":"XOF"
    }
  }
}
'

```
```json Sample Response
{
  "data":{
    "order_id":"v1-4405071524-aa-qlAtAf",
    "merchant_order_reference":"112345",
    "type":"CHARGE",
    "status":"CREATED",
    "merchant_id":"104359",
    "order_amount":{
      "value":1100,
      "currency":"INR"
    },
    "pre_auth":false,
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
    "notes":"order1",
    "purchase_details":{
      "customer":{
        "email_id":"kevin.bob@example.com",
        "first_name":"Kevin",
        "last_name":"Bob",
        "customer_id":"123456",
        "mobile_number":"9876543210",
        "billing_address":{
          "address1":"10 Downing Street Westminster London",
          "address2":"Oxford Street Westminster London",
          "address3":"Baker Street Westminster London",
          "pincode":"51524036",
          "city":"Westminster",
          "state":"Westminster",
          "country":"London"
        },
        "shipping_address":{
          "address1":"10 Downing Street Westminster London",
          "address2":"Oxford Street Westminster London",
          "address3":"Baker Street Westminster London",
          "pincode":"51524036",
          "city":"Westminster",
          "state":"Westminster",
          "country":"London"
        }
      },
      "merchant_metadata":{
        "key1":"DD",
        "key2":"XOF"
      }
    },
    "payments":[
      
    ],
    "created_at":"2024-07-15T05:44:51.174Z",
    "updated_at":"2024-07-15T05:44:51.174Z"
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/reference/orders-create" target="_blank">Create Order API</a> documentation to learn more.

## 3. Calculate Convenience Fee

Use this API to Calculate the convenience fee for the payment against an order.

Below are the sample requests and sample response for Calculate Convenience Fee API.

```curl cURL - UAT
curl --location 'https://pluraluat.v2.pinepg.in/api/pay/v1/fees' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
--header 'Content-Type: application/json' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'accept: application/json' \
--data '
{
  "amount": {
    "value":10000,
    "currency":"INR"
  },
  "payment_method":"CARD",
  "network_type":"VISA"
}
'
```
```curl cURL - PROD
curl --location 'https://api.pluralpay.in/api/pay/v1/fees' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
--header 'Content-Type: application/json' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'accept: application/json' \
--data '
{
  "amount": {
    "value":10000,
    "currency":"INR"
  },
  "payment_method":"CARD",
  "network_type":"VISA"
}
'
```
```json Sample Response
{
  "data": [
    {
      "payment_method": "CARD",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 300,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 57,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 20,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 377,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 10377,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "UNKNOWN",
        "card_type": "CREDIT"
      }
    },
    {
      "payment_method": "CARD",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 360,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 101,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 205,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 666,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 10666,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "VISA",
        "card_type": "CREDIT"
      }
    },
    {
      "payment_method": "CARD",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 480,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 122,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 201,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 803,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 10803,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "MASTERCARD",
        "card_type": "CREDIT"
      }
    },
    {
      "payment_method": "NETBANKING",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 400,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 77,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 30,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 507,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 10507,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "UNKNOWN"
      }
    },
    {
      "payment_method": "UPI",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 600,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 117,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 50,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 767,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 10767,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "UNKNOWN"
      }
    },
    {
      "payment_method": "WALLET",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 700,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 136,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 60,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 896,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 10896,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "UNKNOWN"
      }
    },
    {
      "payment_method": "CARD",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 900,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 176,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 80,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 1156,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 11156,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "UNKNOWN",
        "card_type": "DEBIT"
      }
    },
    {
      "payment_method": "CARD",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 1100,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 351,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 850,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 2301,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 12301,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "MASTERCARD",
        "card_type": "DEBIT"
      }
    }
  ]
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/v3.0/reference/payments-create" target="_blank">Calculate Convenience Fee API</a> documentation to learn more.

## 4. Create Payment

To create a payment, use our Create Payment API, use the `order_id` returned in the response of a Create Order API to link the payment against an order.

Below are the sample requests and sample response for Card Payment API.

```curl cURL - UAT
curl --location 'https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/payments' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
--header 'Content-Type: application/json' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'accept: application/json' \
--data '
{
  "payments": [
    {
      "payment_method": "CARD",
      "payment_amount": {
        "value": 10666,
        "currency": "INR"
      },
      "payment_option": {
        "card_details": {
          "name": "INDRANI DUTTA",
          "card_number": "4012000000001097",
          "cvv": "123",
          "expiry_month": "01",
          "expiry_year": "2026"
        }
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 360,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 101,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 205,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 666,
          "currency": "INR"
        }
      }
    }
  ]
}
'
```
```curl cURL - PROD
curl --location 'https://api.pluralpay.in/api/pay/v1/orders/{order_id}/payments' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
--header 'Content-Type: application/json' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'accept: application/json' \
--data '
{
  "payments": [
    {
      "payment_method": "CARD",
      "payment_amount": {
        "value": 10666,
        "currency": "INR"
      },
      "payment_option": {
        "card_details": {
          "name": "INDRANI DUTTA",
          "card_number": "4012000000001097",
          "cvv": "123",
          "expiry_month": "01",
          "expiry_year": "2026"
        }
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 360,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 101,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 205,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 666,
          "currency": "INR"
        }
      }
    }
  ]
}
'
```
```json Sample Response
{
  "data":{
    "order_id":"v1-241202053455-aa-GQT2Ss",
    "merchant_order_reference":"8939be73-6acb-4bb1-a6a9-43bf4b6a01d0",
    "type":"CHARGE",
    "status":"PENDING",
    "challenge_url":"https://pluraluat.v2.pinepg.in/web/auth/landing/?token=S503%2BwhWUyqWEBDEg2lPgkejhHti4ejP1x21CYZFm2zlfHavE8ketvC%2Bi7px6hmYIcd",
    "merchant_id":"106696",
    "order_amount":{
      "value":10000,
      "currency":"INR"
    },
    "pre_auth":false,
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
    "purchase_details":{
      
    },
    "payments":[
      {
        "id":"v1-241202053455-aa-GQT2Ss-cc-s",
        "status":"PENDING",
        "payment_amount":{
          "value":10666,
          "currency":"INR"
        },
        "payment_method":"CARD",
        "payment_option":{
          "card_data":{
            "card_type":"CREDIT",
            "network_name":"VISA",
            "issuer_name":"VISA PRODUCTION SUPPORT CLIENT BID 1",
            "card_category":"Consumer",
            "country_code":"IND",
            "token_txn_type":"ALT_TOKEN"
          }
        },
        "convenience_fee_breakdown":{
          "fee_amount":{
            "value":360,
            "currency":"INR"
          },
          "tax_amount":{
            "value":101,
            "currency":"INR"
          },
          "additional_fee_amount":{
            "value":205,
            "currency":"INR"
          },
          "maximum_fee_amount":{
            "value":1500000,
            "currency":"INR"
          },
          "applicable_fee_amount":{
            "value":666,
            "currency":"INR"
          }
        },
        "acquirer_data":{
          "approval_code":"",
          "acquirer_reference":"7331177473836261303954",
          "rrn":"",
          "is_aggregator":true
        },
        "created_at":"2024-12-02T05:35:45.541Z",
        "updated_at":"2024-12-02T05:35:47.970Z"
      }
    ],
    "created_at":"2024-12-02T05:34:55.591Z",
    "updated_at":"2024-12-02T05:35:47.971Z",
    "integration_mode":"SEAMLESS"
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/v3.0/reference/payments-create" target="_blank">Create Payment API</a> documentation to learn more.

> 📘 Note:
> 
> When the pre-authorization is set to true you can capture the payment after successful delivery or service.

## 5. Handle Payment

In create payment API response we return a `challenge_url`, use this challenge url to navigate your customers to the checkout page to accept payment.

> 📘 Note:
> 
> - On successful payment we send the webhook event `ORDER_AUTHORIZED` and the status of the payment is updated to `authorized`.
> - You can capture or cancel an order only when the order status is `authorized`.

### 5.1 Store Payment Details on Your Server

On a successful and failed payment we return the following fields to the return url.

- We recommend you to store the payment details on your server.
- You must validate the authenticity of the payment details returned. You can authenticate by verifying the signature.

```json Success Callback Response
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "payment_status": "AUTHORIZED",
  "signature": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
}
```
```json Failure Callbak Response
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "payment_status": "AUTHORIZED",
  "error_code": "USER_AUTHENTICATION_REQUIRED",
  "error_message": "Consumer Authentication Required",
  "signature": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
}
```

### 5.2 Verify Payment Signature

Ensure you follow this as a mandatory step to verify the authenticity of the details returned to the checkout form for successful payments.

Follow the below steps to verify the signature.

1. Create a signature on your server using the following parameters using the SHA256 algorithm.
   1. `order_id`: Unique Identifier generated for an order request on Plural database.
   2. `payment_status`: Payment status.
   3. `error_code`: Short code for the error returned.
   4. `error_message`: Corresponding error message for the code.
   5. `secret_key`: The Onboarding team has provided you with this information as part of the onboarding process.

Use the below sample code to construct HashMap signature using the SHA256 algorithm.

```java Java
import java.io.UnsupportedEncodingException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
 
public class hash {
    public static void main(String[] args) {
        // Test the GenerateHash method
        String input = "<string>";
        String secretKey = "<secret_key>";  // Example key in hex
 
        String hash = GenerateHash(input, secretKey);
        System.out.println("Generated Hash: " + hash);
    }
    public static String GenerateHash(String input, String strSecretKey) {
        String strHash = "";
        try {
            if (!isValidString(input) || !isValidString(strSecretKey)) {
                return strHash;
            }
            byte[] convertedHashKey = new byte[strSecretKey.length() / 2];
 
            for (int i = 0; i < strSecretKey.length() / 2; i++) {
                convertedHashKey[i] =
                        (byte)Integer.parseInt(strSecretKey.substring(i * 2, (i*2)+2),16); //hexNumber radix
            }
            strHash = hmacDigest(input.toString(), convertedHashKey,
                    "HmacSHA256");
        } catch (Exception ex) {
            strHash = "";
        }
        return strHash.toUpperCase();
    }
    private static String hmacDigest(String msg, byte[] keyString, String algo) {
        String digest = null;
        try {
            SecretKeySpec key = new SecretKeySpec(keyString, algo);
            Mac mac = Mac.getInstance(algo);
            mac.init(key);
            byte[] bytes = mac.doFinal(msg.getBytes("UTF-8"));
            StringBuffer hash = new StringBuffer();
            for (int i = 0; i < bytes.length; i++) {
                String hex = Integer.toHexString(0xFF & bytes[i]);
                if (hex.length() == 1) {
                    hash.append('0');
                }
                hash.append(hex);
            }
            digest = hash.toString();
        } catch (UnsupportedEncodingException e) {
// logger.error("Exception occured in hashing the pine payment gateway request"+e);
        } catch (InvalidKeyException e) {
// logger.error("Exception occured in hashing the pine payment gateway request"+e);
        } catch (NoSuchAlgorithmException e) {
// logger.error("Exception occured in hashing the pine payment gateway request"+e);
        }
        return digest;
    }
    public static boolean isValidString(String str){
        if(str != null && !"".equals(str.trim())){
            return true;
        }
        return false;
    }
}
```

> 📘 Note:
> 
> To create a request string, format the key-value pairs of data returned to the return URL. The pairs are separated by `&` and arranged in ascending order based on a lexicographical comparison of the keys.

Shown below is a example to create a request string.

```text Success
"key1=value1&key2=value2", ["order_id=random_order_id&status=AUTHORIZED"]
```
```text Failed
"key1=value1&key2=value2&key3=value3&key4=value4", ["error_code=USER_AUTHENTICATION_FAILED&error_message=Consumer Authentication required&order_id=<order_id>&status=FAILED"]
```

2. If the signature generated on your server matches the Plural signature returned in the return URL, it confirms that the payment details are from Plural.
3. Capture the status returned on your database. Once the payment status is `AUTHORIZED` you can either capture or cancel an order.

> 📘 Important:
> 
> - With pre-authorization set to true, you can capture or cancel a payment for an order.
