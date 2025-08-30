---
title: "Integration Steps"
slug: "seamless-upi-integration-steps"
excerpt: "Learn how you can integrate with Plural APIs to start accepting payments on your website."
hidden: false
createdAt: "Tue Sep 10 2024 11:51:45 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Mar 24 2025 10:27:37 GMT+0000 (Coordinated Universal Time)"
---
Follow the below steps to integrate with Plural seamless checkout APIs in your application.

1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/seamless-upi-integration-steps#1-prerequisite-generate-token" >\[Prerequisite] Generate Token</a>
2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/seamless-upi-integration-steps#2-create-order" >Create Order</a>
3. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/seamless-upi-integration-steps#3-create-payment" >Create Payment</a>
4. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/seamless-upi-integration-steps#4-handle-payment" >Handle Payment</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/seamless-upi-integration-steps#41-store-payment-details-on-your-server" >Store Payment Details on Your Server</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/seamless-upi-integration-steps#42-verify-payment-signature" >Verify Payment Signature</a>

> 📘 Note
> 
> - Ensure you store your Client ID and Secret in your Backend securely.
> - Integrate our APIs on your backend system.
> - We strictly recommend not to call our APIs from the frontend.

## 1. [Prerequisite] Generate Token

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

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/v3.0/reference/generate-token" target="_blank">Generate Token API</a> documentation to learn more.

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
  "allowed_payment_methods":[
    "CARD",
    "UPI",
    "NETBANKING",
    "POINTS",
    "WALLET"
  ],
  "notes":"order1",
  "callback_url":"https://sample-callback-url",
  "failure_callback_url": "https://sample-failure-callback-url",
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
  "allowed_payment_methods":[
    "CARD",
    "UPI",
    "NETBANKING",
    "POINTS",
    "WALLET"
  ],
  "notes":"order1",
  "callback_url":"https://sample-callback-url",
  "failure_callback_url": "https://sample-failure-callback-url",
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
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
    "notes":"order1",
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
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

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/v3.0/reference/orders-create" target="_blank">Create Order API</a> documentation to learn more.

## 3. Create Payment

To create a payment, use our Create Payment API, use the `order_id` returned in the response of a Create Order API to link the payment against an order.

Below are the sample requests and sample response for a Create Payment API via Intent Flow.

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
      "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
      "payment_method": "UPI",
      "payment_amount": {
        "value": 1100,
        "currency": "INR"
      },
      "payment_option": {
        "upi_details": {
          "txn_mode": "INTENT"
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
      "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
      "payment_method": "UPI",
      "payment_amount": {
        "value": 1100,
        "currency": "INR"
      },
      "payment_option": {
        "upi_details": {
          "txn_mode": "INTENT"
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
    "order_id":"v1-240820090251-aa-xwuI7J",
    "merchant_order_reference":"8200c7f7-4490-4970-b6bb-40ffa05d47e5",
    "type":"CHARGE",
    "status":"PENDING",
    "challenge_url":"upi://pay?mode=04&pa=pinelabs.24092@hdfcbank&pn=Pine%20Test&mc=6012&cu=INR&am=1.00&tr=68706&tn=Payment%20for%20v1",
    "merchant_id":"110047",
    "order_amount":{
      "value":100,
      "currency":"INR"
    },
    "pre_auth":false,
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
    "notes":"order1",
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "purchase_details":{
      "customer":{
        "email_id":"kevin.bob@example.com",
        "first_name":"Kevin",
        "last_name":"Bob",
        "customer_id":"192212",
        "mobile_number":"9876543210",
        "billing_address":{
          "address1":"H.No 15, Sector 17",
          "address2":"",
          "address3":"",
          "pincode":"61232112",
          "city":"CHANDIGARH",
          "state":"PUNJAB",
          "country":"INDIA"
        },
        "shipping_address":{
          "address1":"H.No 15, Sector 17",
          "address2":"",
          "address3":"",
          "pincode":"144001123",
          "city":"CHANDIGARH",
          "state":"PUNJAB",
          "country":"INDIA"
        }
      },
      "merchant_metadata":{
        "key1":"DD",
        "key2":"XOF"
      }
    },
    "payments":[
      {
        "id":"v1-240820090251-aa-xwuI7J-up-6",
        "merchant_payment_reference":"008cf04b-a770-4777-854e-b1e6c1230609",
        "status":"PENDING",
        "payment_amount":{
          "value":100,
          "currency":"INR"
        },
        "payment_method":"UPI",
        "payment_option":{
          "upi_details":{
            "txn_mode":"INTENT"
          }
        },
        "acquirer_data":{
          "approval_code":"",
          "acquirer_reference":"",
          "rrn":"",
          "is_aggregator":true
        },
        "created_at":"2024-08-20T09:02:51.265Z",
        "updated_at":"2024-08-20T09:03:01.208Z"
      }
    ],
    "created_at":"2024-08-20T09:02:51.265Z",
    "updated_at":"2024-08-20T09:03:01.208Z"
  }
}
```

Below are the sample requests and sample response for a Create Payment API via Collect Flow.

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
      "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
      "payment_method": "UPI",
      "payment_amount": {
        "value": 100,
        "currency": "INR"
      },
      "payment_option": {
        "upi_details": {
          "txn_mode": "COLLECT",
          "payer": {
            "vpa": "kevin.bob@examplebank.com"
          }
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
      "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
      "payment_method": "UPI",
      "payment_amount": {
        "value": 100,
        "currency": "INR"
      },
      "payment_option": {
        "upi_details": {
          "txn_mode": "COLLECT",
          "payer": {
            "vpa": "kevin.bob@examplebank.com"
          }
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
    "order_id":"v1-240820090251-aa-xwuI7J",
    "merchant_order_reference":"8200c7f7-4490-4970-b6bb-40ffa05d47e5",
    "type":"CHARGE",
    "status":"PENDING",
    "challenge_url":"upi://pay?mode=04&pa=pinelabs.24092@hdfcbank&pn=Pine%20Test&mc=6012&cu=INR&am=1.00&tr=68706&tn=Payment%20for%20v1",
    "merchant_id":"110047",
    "order_amount":{
      "value":100,
      "currency":"INR"
    },
    "pre_auth":false,
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
    "notes":"order1",
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "purchase_details":{
      "customer":{
        "email_id":"kevin.bob@example.com",
        "first_name":"Kevin",
        "last_name":"Bob",
        "customer_id":"192212",
        "mobile_number":"9876543210",
        "billing_address":{
          "address1":"H.No 15, Sector 17",
          "address2":"",
          "address3":"",
          "pincode":"61232112",
          "city":"CHANDIGARH",
          "state":"PUNJAB",
          "country":"INDIA"
        },
        "shipping_address":{
          "address1":"H.No 15, Sector 17",
          "address2":"",
          "address3":"",
          "pincode":"144001123",
          "city":"CHANDIGARH",
          "state":"PUNJAB",
          "country":"INDIA"
        }
      },
      "merchant_metadata":{
        "key1":"DD",
        "key2":"XOF"
      }
    },
    "payments":[
      {
        "id":"v1-240820090251-aa-xwuI7J-up-6",
        "merchant_payment_reference":"008cf04b-a770-4777-854e-b1e6c1230609",
        "status":"PENDING",
        "payment_amount":{
          "value":100,
          "currency":"INR"
        },
        "payment_method":"UPI",
        "payment_option":{
          "upi_details":{
            "txn_mode":"COLLECT",
            "payer":{
              "vpa":"kevin.bob@examplebank.com"
            }
          },
          "acquirer_data":{
            "approval_code":"",
            "acquirer_reference":"",
            "rrn":"",
            "is_aggregator":true
          },
          "created_at":"2024-08-20T09:02:51.265Z",
          "updated_at":"2024-08-20T09:03:01.208Z"
        }
      }
    ],
    "created_at":"2024-08-20T09:02:51.265Z",
    "updated_at":"2024-08-20T09:03:01.208Z"
  }
}
```

Below are the sample requests and sample response for a Create Payment API via QR Flow.

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
      "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
      "payment_method": "UPI",
      "payment_amount": {
        "value": 100,
        "currency": "INR"
      },
      "payment_option": {
        "upi_details": {
          "txn_mode": "INTENT",
          "upi_qr": true
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
      "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
      "payment_method": "UPI",
      "payment_amount": {
        "value": 100,
        "currency": "INR"
      },
      "payment_option": {
        "upi_details": {
          "txn_mode": "INTENT",
          "upi_qr": true
        }
      }
    }
  ]
}
'
```
```json Sample Response
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

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/v3.0/reference/payments-create" target="_blank">Create Payment API</a> documentation to learn more.

> 📘 Note:
> 
> Use the [Cancel API ](https://developer.pluralonline.com/reference/orders-cancel)to cancel the payment against an order at any time.

## 4. Handle Payment

In create payment API response we return a `challenge_url`, use this challenge url to navigate your customers to the checkout page to accept payment.

> 📘 Note:
> 
> - On successful payment we send the webhook event `ORDER_AUTHORIZED` and the status of the payment is updated to `authorized`.
> - You can capture or cancel an order only when the order status is `authorized`.

### 4.1 Store Payment Details on Your Server

On a successful and failed payment we return the following fields to the return url.

- We recommend you to store the payment details on your server.
- You must validate the authenticity of the payment details returned. You can authenticate by verifying the signature.

```json Success Callback Response
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "status": "AUTHORIZED",
  "signature": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
}
```
```json Failure Callbak Response
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "status": "AUTHORIZED",
  "error_code": "USER_AUTHENTICATION_REQUIRED",
  "error_message": "Consumer Authentication Required",
  "signature": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
}
```

### 4.2 Verify Payment Signature

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
