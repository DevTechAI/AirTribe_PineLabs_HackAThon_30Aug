---
title: "Seamless Checkout Integration Steps"
slug: "split-settlements-integration-steps-1"
excerpt: "Learn how you can integrate with Plural APIs to start accepting payments and distributing settlements to your merchants."
hidden: true
createdAt: "Mon Dec 09 2024 05:17:30 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon May 19 2025 07:25:01 GMT+0000 (Coordinated Universal Time)"
---
Follow the below steps to integrate Split Settlements with Plural seamless checkout APIs in your application.

1. <a href="https://developer.pluralonline.com/docs/integration-steps-1#1-prerequisite-generate-token" >\[Prerequisite] Generate Token</a>
2. <a href="https://developer.pluralonline.com/docs/integration-steps-1#2-create-order" >Create Order</a>
3. <a href="https://developer.pluralonline.com/docs/integration-steps-1#3-create-payment" >Create Payment</a>
4. <a href="https://developer.pluralonline.com/docs/split-settlements-integration-steps#4-manage-settlement" >Manage Settlement</a>
   1. <a href="https://developer.pluralonline.com/docs/split-settlements-integration-steps#41-release-settlement-api" >Release Settlement</a>
   2. <a href="https://developer.pluralonline.com/docs/split-settlements-integration-steps#42-cancel-settlement-api" >Cancel Settlement</a>
5. <a href="https://developer.pluralonline.com/docs/integration-steps-1#5-handle-payment" >Handle Payment</a>
   1. <a href="https://developer.pluralonline.com/docs/integration-steps-1#51-store-payment-details-on-your-server" >Store Payment Details on Your Server</a>
   2. <a href="https://developer.pluralonline.com/docs/integration-steps-1#52-verify-payment-signature" >Verify Payment Signature</a>

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
  "merchant_order_reference":"1578609owyihy",
  "order_amount":{
    "value":50000,
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
    "customer":{
      "email_id":"kevin.bob@example.com",
      "first_name":"Kevin",
      "last_name":"Bob",
      "customer_id":"192212",
      "mobile_number":"9876543210",
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
    },
    "split_info":{
      "split_type":"AMOUNT",
      "split_details":[
        {
          "split_merchant_id":"1324",
          "merchant_settlement_reference":"kshjhfk",
          "amount":{
            "value":30000,
            "currency":"INR"
          },
          "on_hold":true
        },
        {
          "split_merchant_id":"1233",
          "amount":{
            "value":20000,
            "currency":"INR"
          },
          "on_hold":false
        }
      ]
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
  "merchant_order_reference":"1578609owyihy",
  "order_amount":{
    "value":50000,
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
    "customer":{
      "email_id":"kevin.bob@example.com",
      "first_name":"Kevin",
      "last_name":"Bob",
      "customer_id":"192212",
      "mobile_number":"9876543210",
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
    },
    "split_info":{
      "split_type":"AMOUNT",
      "split_details":[
        {
          "split_merchant_id":"1324",
          "merchant_settlement_reference":"kshjhfk",
          "amount":{
            "value":30000,
            "currency":"INR"
          },
          "on_hold":true
        },
        {
          "split_merchant_id":"1233",
          "amount":{
            "value":20000,
            "currency":"INR"
          },
          "on_hold":false
        }
      ]
    }
  }
}
'
```
```json Sample Response
{
  "data":{
    "order_id":"v1-241118074845-aa-wduUQF",
    "merchant_order_reference":"3595f435-b1c5-4a60-a98c-9cf39ee3dc07",
    "type":"CHARGE",
    "status":"CREATED",
    "merchant_id":"108272",
    "order_amount":{
      "value":50000,
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
      "customer":{
        "email_id":"kevin.bob@example.com",
        "first_name":"Kevin",
        "last_name":"Bob",
        "customer_id":"192212",
        "mobile_number":"9876543210",
        "billing_address":{
          
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
      },
      "split_info":{
        "split_type":"AMOUNT",
        "split_details":[
          {
            "split_merchant_id":"1324",
            "split_settlement_id":"v1-241118074845-aa-wduUQF-ss-b",
            "merchant_settlement_reference":"kshjhfk",
            "amount":{
              "value":30000,
              "currency":"INR"
            },
            "on_hold":true,
            "status":"HOLD",
            "updated_at":"2024-11-18T07:48:45.324Z"
          },
          {
            "split_merchant_id":"1233",
            "split_settlement_id":"v1-241118074845-aa-wduUQF-ss-r",
            "amount":{
              "value":20000,
              "currency":"INR"
            },
            "on_hold":false,
            "status":"RELEASED",
            "updated_at":"2024-11-18T07:48:45.324Z"
          }
        ]
      }
    },
    "created_at":"2024-11-18T07:48:45.324336Z",
    "updated_at":"2024-11-18T07:48:45.324348Z",
    "integration_mode":"SEAMLESS"
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/v3.0/reference/orders-create" target="_blank">Create Order API</a> documentation to learn more.

## 3. Create Payment

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
      "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
      "payment_method": "CARD",
      "payment_amount": {
        "value": 1100,
        "currency": "INR"
      },
      "payment_option": {
        "card_details": {
          "name": "Anil Reddy",
          "card_number": "4111111111111111",
          "cvv": "272",
          "expiry_month": "04",
          "expiry_year": "2029",
          "registered_mobile_number": "9876543210"
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
      "payment_method": "CARD",
      "payment_amount": {
        "value": 1100,
        "currency": "INR"
      },
      "payment_option": {
        "card_details": {
          "name": "Anil Reddy",
          "card_number": "4111111111111111",
          "cvv": "272",
          "expiry_month": "04",
          "expiry_year": "2029",
          "registered_mobile_number": "9876543210"
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
    "order_id":"v1-4405071524-aa-qlAtAf",
    "merchant_order_reference":"112345",
    "type":"CHARGE",
    "status":"PENDING",
    "challenge_url":"https://api.pluralpay.in/web/auth/landing/?token=S50%2B0lOoYHlA03j3y8Of4%2BZEzhD8MuFFLKP6NXx9uiaBBXlNhpCRA4wqkPd%2Bs9eRz7H",
    "merchant_id":"123456",
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
        "key1":"value1",
        "key2":"value2"
      },
      "split_info":{
        "split_type":"AMOUNT",
        "split_details":[
          {
            "split_merchant_id":"123456",
            "split_settlement_id":"v1-241118174248-aa-81BMcH-ss-b",
            "merchant_settlement_reference":"kshjhfk",
            "amount":{
              "value":20000,
              "currency":"INR"
            },
            "on_hold":false,
            "status":"RELEASED",
            "updated_at":"2024-11-18T07:49:38.212311Z"
          },
          {
            "split_merchant_id":"234567",
            "split_settlement_id":"v1-241118174248-aa-81BMcH-ss-r",
            "amount":{
              "value":30000,
              "currency":"INR"
            },
            "on_hold":false,
            "status":"RELEASED",
            "updated_at":"2024-11-18T07:48:45.324348Z"
          }
        ]
      }
    },
    "payments":[
      {
        "id":"v1-5307071124-aa-dmkVNf-cc-c",
        "merchant_payment_reference":"008cf04b-a770-4777-854e-b1e6c1230609",
        "status":"PENDING",
        "payment_amount":{
          "value":1100,
          "currency":"INR"
        },
        "payment_method":"CARD",
        "payment_option":{
          "card_data":{
            "card_type":"CREDIT",
            "network_name":"VISA",
            "issuer_name":"KOTAK",
            "card_category":"CONSUMER",
            "country_code":"IND",
            "token_txn_type":"ALT_TOKEN"
          }
        },
        "created_at":"2024-07-11T07:53:43.358Z",
        "updated_at":"2024-07-11T07:56:18.044Z"
      }
    ],
    "created_at":"2024-07-11T07:53:43.358Z",
    "updated_at":"2024-07-11T07:56:18.044Z"
  }
}
```

Refer to our <a style="text-decoration:none" href="<https://developer.pluralonline.com/v3.0/reference/payments-create>" target="_blank">Create Payment API</a> documentation to learn more.

> 📘 Note:
> 
> - To manage settlements effectively, use the Release Settlement API to hold or release settlements for an order based on your requirements.
> - You can only Release a Settlement when the order status is `PROCESSED`.

## 4. Manage Settlement

### 4.1. Release Settlement

Use this API to initiate a full or partial settlement against an order. For partial settlements, specify the desired settlement amount in the `release_amount` object.

Below is a sample requests and response for Release Settlement API.

```curl cURL - UAT
curl --request PATCH \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/orders/orderId/settlementId/settlementId/release \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "release_amount": {
    "value": 20000,
    "currency": "INR"
  }
}
'
```
```curl cURL - PROD
curl --request PATCH \
     --url https://api.pluralpay.in/api/pay/v1/orders/orderId/settlementId/settlementId/release \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "release_amount": {
    "value": 20000,
    "currency": "INR"
  }
}
'
```
```json Sample Response
{
  "data": {
    "order_id": "v1-250513055632-aa-rjIIWX",
    "merchant_order_reference": "bc2ddc75-eebb-452c-a034-ba9a836ddf17",
    "type": "CHARGE",
    "status": "PROCESSED",
    "merchant_id": "111370",
    "order_amount": {
      "value": 21000,
      "currency": "INR"
    },
    "pre_auth": false,
    "allowed_payment_methods": [
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.sam@gmail.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
        "country_code": "91",
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
        },
        "is_edit_customer_details_allowed": false
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      },
      "split_info": {
        "split_type": "AMOUNT",
        "split_details": [
          {
            "split_merchant_id": "111370",
            "split_settlement_id": "v1-250513055632-aa-rjIIWX-ss-f",
            "amount": {
              "value": 10000,
              "currency": "INR"
            },
            "on_hold": false,
            "status": "RELEASED",
            "updated_at": "2025-05-13T05:58:15.960Z",
            "release_amount": {
              "value": 10000,
              "currency": "INR"
            }
          },
          {
            "split_merchant_id": "111370",
            "split_settlement_id": "v1-250513055632-aa-rjIIWX-ss-g",
            "amount": {
              "value": 2000,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-13T05:56:32.655Z"
          },
          {
            "split_merchant_id": "111370",
            "split_settlement_id": "v1-250513055632-aa-rjIIWX-ss-h",
            "amount": {
              "value": 8000,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-13T05:56:32.655Z"
          },
          {
            "split_merchant_id": "111370",
            "split_settlement_id": "v1-250513055632-aa-rjIIWX-ss-i",
            "amount": {
              "value": 500,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-13T05:56:32.655Z"
          },
          {
            "split_merchant_id": "111370",
            "split_settlement_id": "v1-250513055632-aa-rjIIWX-ss-j",
            "amount": {
              "value": 500,
              "currency": "INR"
            },
            "on_hold": false,
            "status": "RELEASED",
            "updated_at": "2025-05-13T05:56:32.655Z"
          }
        ]
      }
    },
    "payments": [
      {
        "id": "v1-250513055632-aa-rjIIWX-cc-a",
        "merchant_payment_reference": "d1ec1a52-45fb-47be-bd7a-0e0d930f26b8",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 21000,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "HDFC",
            "card_category": "",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN",
            "last4_digit": "1091",
            "is_native_otp_eligible": true
          }
        },
        "acquirer_data": {
          "approval_code": "831000",
          "acquirer_reference": "7471158294616880303814",
          "rrn": "513205569234",
          "is_aggregator": true
        },
        "created_at": "2025-05-13T05:56:56.703Z",
        "updated_at": "2025-05-13T05:57:10.422Z"
      }
    ],
    "created_at": "2025-05-13T05:56:32.655Z",
    "updated_at": "2025-05-13T05:58:15.963Z",
    "integration_mode": "SEAMLESS",
    "payment_retries_remaining": 9
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/reference/release-settlement" target="_blank">Release Settlement API</a> documentation to learn more.

### 4.2. Cancel Settlement

Use this API to cancel a settlement against an order.

Below is a sample requests and response for Cancel Settlement API.

```curl cURL - UAT
curl --request PATCH \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/orders/orderId/settlementId/settlementId/cancel \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json'
```
```curl cURL - PROD
curl --request PATCH \
     --url https://api.pluralpay.in/api/pay/v1/orders/orderId/settlementId/settlementId/cancel \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json'
```
```json Sample Response
{
  "data": {
    "order_id": "v1-250513090438-aa-WoJ9px",
    "merchant_order_reference": "a4df17c9-a37c-4b24-b825-04c6f28b9145",
    "type": "CHARGE",
    "status": "PARTIALLY_CAPTURED",
    "merchant_id": "112434",
    "order_amount": {
      "value": 21000,
      "currency": "INR"
    },
    "pre_auth": true,
    "purchase_details": {
      "customer": {
        "country_code": "91",
        "billing_address": {},
        "shipping_address": {},
        "is_edit_customer_details_allowed": false
      },
      "split_info": {
        "split_type": "AMOUNT",
        "split_details": [
          {
            "split_merchant_id": "112434",
            "split_settlement_id": "v1-250513090438-aa-WoJ9px-ss-f",
            "amount": {
              "value": 10000,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-13T09:04:38.495Z"
          },
          {
            "split_merchant_id": "112434",
            "split_settlement_id": "v1-250513090438-aa-WoJ9px-ss-g",
            "amount": {
              "value": 2000,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-13T09:04:38.495Z"
          },
          {
            "split_merchant_id": "112434",
            "split_settlement_id": "v1-250513090438-aa-WoJ9px-ss-h",
            "amount": {
              "value": 8000,
              "currency": "INR"
            },
            "on_hold": false,
            "status": "CANCELLED",
            "updated_at": "2025-05-13T09:16:36.890Z"
          },
          {
            "split_merchant_id": "112434",
            "split_settlement_id": "v1-250513090438-aa-WoJ9px-ss-i",
            "amount": {
              "value": 500,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-13T09:04:38.495Z"
          },
          {
            "split_merchant_id": "112434",
            "split_settlement_id": "v1-250513090438-aa-WoJ9px-ss-j",
            "amount": {
              "value": 500,
              "currency": "INR"
            },
            "on_hold": false,
            "status": "RELEASED",
            "updated_at": "2025-05-13T09:04:38.495Z"
          }
        ]
      }
    },
    "payments": [
      {
        "id": "v1-250513090438-aa-WoJ9px-cc-a",
        "merchant_payment_reference": "ce2e7dd6-b6b0-4763-8650-44637dc7fee1",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 21000,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "HDFC",
            "card_category": "",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN",
            "last4_digit": "1091",
            "is_native_otp_eligible": true
          }
        },
        "acquirer_data": {
          "approval_code": "831000",
          "acquirer_reference": "7471271731696698003813",
          "rrn": "513309573407",
          "is_aggregator": false
        },
        "capture_data": [
          {
            "merchant_capture_reference": "6fb491a4-a22e-4a11-a1e6-94a442e27721",
            "capture_amount": {
              "value": 20000,
              "currency": "INR"
            },
            "created_at": "2025-05-13T09:06:11.865Z"
          }
        ],
        "created_at": "2025-05-13T09:05:08.764Z",
        "updated_at": "2025-05-13T09:06:13.915Z"
      }
    ],
    "created_at": "2025-05-13T09:04:38.495Z",
    "updated_at": "2025-05-13T09:16:36.893Z",
    "integration_mode": "SEAMLESS",
    "payment_retries_remaining": 9
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/reference/cancel-settlement" target="_blank">Cancel Settlement API</a> documentation to learn more.

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

### To Know Your Payment Status

To check your payment status, you can either rely on Webhook events or use our **Get Orders** APIs for real-time updates.

1. **Webhook Notification**: We send Webhook notifications on the successful payment or any changes to the payments object. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/developer-tools-webhook" target="_blank">Webhooks</a> documentation to learn more.
2. **Get Orders API**: Use our Get Orders API to know the real time status of the payment. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/order-manage#3-get-order-by-order-id" target="_blank">Manage Orders</a> documentation to learn more.

### Refunds

Plural processes refund directly to the customer's original payment method to prevent chargebacks.

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/payment-refund" target="_blank">Refunds</a> documentation to learn more.
