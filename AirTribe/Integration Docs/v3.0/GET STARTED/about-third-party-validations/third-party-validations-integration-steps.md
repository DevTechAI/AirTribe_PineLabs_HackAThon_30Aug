---
title: "Integration Steps"
slug: "third-party-validations-integration-steps"
excerpt: "Learn how to use Plural APIs to validate your customer account and start accepting payments after successful account validation."
hidden: false
createdAt: "Thu Sep 19 2024 11:31:31 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Mar 24 2025 10:33:55 GMT+0000 (Coordinated Universal Time)"
---
Follow the below steps to integrate with Plural Third Party Validation APIs in your application.

1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/third-party-validations-integration-flow#1-prerequisite-generate-token" >\[Prerequisite] Generate Token</a>
2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/third-party-validations-integration-flow#2-create-order" >Create Order</a>
3. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/third-party-validations-integration-flow#3-create-payment" >Create Payment</a>
4. <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/third-party-validations-integration-flow#4-handle-payment" >Handle Payment</a>
   1. <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/third-party-validations-integration-flow#41-store-payment-details-on-your-server" >Store Payment Details on Your Server</a>
   2. <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/third-party-validations-integration-flow#42-verify-payment-signature" >Verify Payment Signature</a>

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
    "account_details":{
      "bank_details":{
        "account_number":"103101532234",
        "ifsc_code":"",
        "bank_name":""
      }
    },
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
  "purchase_details":{
    "account_details":{
      "bank_details":{
        "account_number":"103101532234",
        "ifsc_code":"",
        "bank_name":""
      }
    },
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

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/v3.0/reference/orders-create" target="_blank">Create Order API</a> documentation to learn more.

> 🚧 Watch Out:
> 
> - For PNB accounts, pass 16-digit account numbers with a prefix zero.  
>   Example: If the account number is 123456789012345, pass it as 0123456789012345.
> - For PSBI, Canara, CITI and SBI accounts, pass 17-digit account numbers with a prefix zero.  
>   Example: If the account number is 1234567890123456, pass it as 01234567890123456.
> - For all other banks, pass the account number as is.

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
    "order_id":"v1-240821055834-aa-ksDPRb",
    "merchant_order_reference":"8edb181b-0359-4191-b5ad-f630cafc0733",
    "type":"CHARGE",
    "status":"PENDING",
    "merchant_id":"110047",
    "order_amount":{
      "value":100,
      "currency":"INR"
    },
    "notes":"some order",
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
        "id":"v1-240821055834-aa-ksDPRb-up-Y",
        "merchant_payment_reference":"008cf04b-a770-4777-854e-b1e6c1230609",
        "status":"PENDING",
        "payment_amount":{
          "value":100,
          "currency":"INR"
        },
        "payment_method":"UPI",
        "acquirer_data":{
          "approval_code":"",
          "acquirer_reference":"",
          "rrn":""
        },
        "created_at":"2024-08-21T05:58:34.771Z",
        "updated_at":"2024-08-21T05:58:59.851Z"
      }
    ],
    "created_at":"2024-08-21T05:58:34.771Z",
    "updated_at":"2024-08-21T05:58:59.851Z"
  }
}
```

Below are the sample requests and sample response for a Create Payment API via Netbanking Flow

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
           "merchant_payment_reference": "4301dc85-da77-4bd5-b865-23f12c84cd05",
           "payment_method": "NETBANKING",
           "payment_amount": {
               "value": 100,
               "currency": "INR"
           },
           "payment_option": {
               "netbanking_details": {
                   "pay_code": "NB1531",
                   "registered_mobile_number": "918612300789"
               }
           },
           "device_info" : {
               "device_type" : "WEB",
               "browser_user_agent" : "Mozilla/5.0 (WindowsNT 10.0; WOW64; rv:51.0)"
           },
           "customer_account_details": {
               "account_number": "1234567890",
               "ifsc_code": "SBIN0006393"
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
           "merchant_payment_reference": "4301dc85-da77-4bd5-b865-23f12c84cd05",
           "payment_method": "NETBANKING",
           "payment_amount": {
               "value": 100,
               "currency": "INR"
           },
           "payment_option": {
               "netbanking_details": {
                   "pay_code": "NB1531",
                   "registered_mobile_number": "918612300789"
               }
           },
           "device_info" : {
               "device_type" : "WEB",
               "browser_type": "CHROME",
               "source_ip_address" : "10.10.10.10",
               "browser_user_agent" : "Mozilla/5.0 (WindowsNT 10.0; WOW64; rv:51.0)"
           },
           "customer_account_details": {
               "account_number": "1234567890",
               "ifsc_code": "SBIN0006393"
           }
       }
   ]
}
'
```
```json Sample Response
{
  "data":{
    "order_id":"v1-250129121449-aa-QhZSto",
    "merchant_order_reference":"152f124e-17a1-aa5680ed14b393-SUCCESS",
    "type":"CHARGE",
    "status":"PENDING",
    "merchant_id":"111267",
    "order_amount":{
      "value":100,
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
        "email_id":"aayush.sam@gmail.com",
        "first_name":"joe",
        "last_name":"kumar",
        "customer_id":"192212",
        "mobile_number":"192192883",
        "country_code":"91",
        "billing_address":{
          "address1":"H.No 15, Sector 17",
          "pincode":"61232112",
          "city":"CHANDIGARH",
          "state":"PUNJAB",
          "country":"INDIA"
        },
        "shipping_address":{
          "address1":"H.No 15, Sector 17",
          "address2":"string",
          "address3":"string",
          "pincode":"144001123",
          "city":"CHANDIGARH",
          "state":"PUNJAB",
          "country":"INDIA"
        },
        "is_edit_customer_details_allowed":false
      },
      "merchant_metadata":{
        "key1":"value1",
        "key2":"value2"
      }
    },
    "payments":[
      {
        "id":"v1-250129121449-aa-QhZSto-nb-a",
        "merchant_payment_reference":"c149ad6e-5f83-4da2-ba44-5504a3e3434c",
        "status":"PENDING",
        "payment_amount":{
          "value":100,
          "currency":"INR"
        },
        "payment_method":"NETBANKING",
        "payment_option":{
          "netbanking_data":{
            "pay_code":"NB1531",
            "registered_mobile_number":"918612300789"
          }
        },
        "acquirer_data":{
          "approval_code":"TRP0000",
          "acquirer_reference":"USBILZU0002C5T",
          "rrn":"",
          "is_aggregator":true
        },
        "created_at":"2025-01-29T12:14:53.564Z",
        "updated_at":"2025-01-29T12:14:55.150Z"
      }
    ],
    "created_at":"2025-01-29T12:14:49.766Z",
    "updated_at":"2025-01-29T12:14:55.150Z",
    "integration_mode":"SEAMLESS",
    "payment_retries_remaining":9
  }
}
```

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/v3.0/reference/payments-create" target="_blank">Create Payment API</a> documentation to learn more.

## 4. Handle Payment

In create payment API response we return a `challenge_url`, use this challenge url to navigate your customers to the checkout page to accept payment.

> 📘 Note:
> 
> - On successful payment we send the webhook event `ORDER_AUTHORIZED` and the status of the payment is updated to `authorized`.
> - You can capture or cancel an order only when the order status is `authorized`.

### 4.1 Store Payment Details on Your Server

On a successful and failed payment, we return the following fields to the return url.

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
