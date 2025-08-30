---
title: "Test_Integration Steps"
slug: "test_integration-steps"
excerpt: ""
hidden: true
createdAt: "Fri Feb 28 2025 10:20:35 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Apr 14 2025 07:25:02 GMT+0000 (Coordinated Universal Time)"
---
Follow the below steps to integrate with Plural subscription APIs.

1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#1-prerequisite-generate-token" >\[Prerequisite] Generate Token</a>
2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#2-create-plan" >Create Plan</a>
3. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#3-get-all-plans" >Get All Plans</a>
4. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#4-create-subscription" >Create Subscription</a>
5. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#5-create-payment" >Create Payment</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#51-for-seamless-payment" >For Seamless Payment</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#52-redirect-payment" >Redirect Payment</a>
6. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#6-handle-payment" >Handle Payment</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#61-store-payment-details-on-your-server" >Store Payment Details on Your Server</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#62-verify-payment-signature" >Verify Payment Signature</a>
7. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#7-manage-subscription" >Manage Subscription</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#71-update-a-subscription" >Update a Subscription</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#73-pause-subscription" >Pause Subscription</a>
   3. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#74-resume-subscription" >Resume Subscription</a>
   4. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#75-retrieve-subscription-invoices" >Retrieve Subscription Invoices</a>
8. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#8-schedule-recurring-payment" >Schedule Recurring Payment</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#81-create-a-presentation" >Create a Presentation</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#82-retrieve-a-presentation" >Retrieve a Presentation</a>
   3. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#83-cancel-presentation" >Cancel Presentation</a>

## 1. [Prerequisite] Generate Token

Integrate our Generate Token API in your backend servers to generate the access token. Use the token generated to authenticate Plural APIs.

Below are the sample requests and response for the Generate Token API.

```curl cURL – UAT
curl --request POST \
--url https://pluraluat.v2.pinepg.in/api/auth/v1/token \
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
curl --request POST \
--url https://api.pluralpay.in/api/auth/v1/token \
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

## 2. Create Plan

Use this API to Create a Plan.

To authenticate this API, use the generated access token in the Authorization headers of the API request.

Below are the sample requests and response for the Create Plan API.

```curl cURL – UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/v1/public/plans \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "plan_name": "Monthly Plan",
  "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
  "notes": "string",
  "frequency_count": 1,
  "frequency": "Day",
  "amount": {
    "value": 100,
    "currency": "INR"
  },
  "max_limit_amount": {
    "value": 100,
    "currency": "INR"
  },
  "trial_period_in_days": 1,
  "start_date": "2022-02-01T17:32:28Z",
  "end_date": "2022-10-21T17:32:28Z",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "merchant_order_reference": "1234567890"
}
'
```
```curl cURL – PROD
curl --request POST \
     --url https://api.pluralpay.in/api/v1/public/plans \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "plan_name": "Monthly Plan",
  "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
  "notes": "string",
  "frequency_count": 1,
  "frequency": "Day",
  "amount": {
    "value": 100,
    "currency": "INR"
  },
  "max_limit_amount": {
    "value": 100,
    "currency": "INR"
  },
  "trial_period_in_days": 1,
  "start_date": "2022-02-01T17:32:28Z",
  "end_date": "2022-10-21T17:32:28Z",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "merchant_order_reference": "1234567890"
}
'
```
```json Sample Response
{
  "plan_id": "v1-plan-4405071524-aa-qlAtAf",
  "status": "ACTIVE",
  "plan_name": "Monthly Plan",
  "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
  "notes": "string",
  "frequency_count": 1,
  "frequency": "Day",
  "amount": {
    "value": 100,
    "currency": "INR"
  },
  "max_limit_amount": {
    "value": 100,
    "currency": "INR"
  },
  "trial_period_in_days": 1,
  "start_date": "2022-02-01T17:32:28Z",
  "end_date": "2022-10-21T17:32:28Z",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "merchant_order_reference": "1234567890",
  "created_at": "2022-10-21T17:32:28Z",
  "modified_at": "2022-10-21T17:32:28Z"
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/create-plan" target="_blank">Create Plan API</a> documentation to learn more.

## 3. Get All Plans

To fetch all Plan, use our Get All Plans API, for authentication use the generated access token in the headers of the API request.

Below are the sample requests and response for the Get All Plans API.

```curl cURL – UAT
curl --request GET \
     --url 'https://pluraluat.v2.pinepg.in/api/v1/public/plans?amount=' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json'\
     --data '
 {
  "start_date": "2022-02-01T17:32:28Z",
  "end_date": "2022-10-21T17:32:28Z",
  "amount": 1000,
  "amount_range": "",
  "frequency": "Day",
  "size": 10,
  "page": 5,
  "sort": "frequency_type,asc"
}
'
```
```curl cURL – PROD

```
```json Sample Response
{
  "links": {
    "first": {
      "href": "https://api.pluralpay.in/api/v1/public /{resource}/?size=10&page=0&sort=id,asc"
    },
    "self": {
      "href": "https://api.pluralpay.in/api/v1/public /{resource}/?size=10&page=0&sort=id,asc"
    },
    "next": {
      "href": "https://api.pluralpay.in/api/v1/public /{resource}/?size=10&page=0&sort=id,asc"
    },
    "last": {
      "href": "https://api.pluralpay.in/api/v1/public /{resource}/?size=10&page=0&sort=id,asc"
    }
  },
  "page": {
    "size": 10,
    "total_elements": 50,
    "total_pages": 5,
    "number": 1
  },
  "plans": [
    {
      "plan_id": "v1-plan-4405071524-aa-qlAtAf",
      "status": "ACTIVE",
      "plan_name": "Monthly Plan",
      "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
      "notes": "string",
      "frequency_count": 1,
      "frequency": "Day",
      "amount": {
        "value": 100,
        "currency": "INR"
      },
      "max_limit_amount": {
        "value": 100,
        "currency": "INR"
      },
      "trial_period_in_days": 1,
      "start_date": "2022-02-01T17:32:28Z",
      "end_date": "2022-10-21T17:32:28Z",
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      },
      "merchant_order_reference": "1234567890",
      "created_at": "2022-10-21T17:32:28Z",
      "modified_at": "2022-10-21T17:32:28Z"
    }
  ]
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/create-all-plan" target="_blank">Get All Plans API</a> documentation to learn more.

## 4. Create Subscription

To Create Subscription, use our Create subscription API, use the `plan_id `returned in the response of a Create Plan API to link the subscription with a plan.

For authentication use the generated access token in the headers of the API request.

Below are the sample requests and response for the Create subscription API.

```curl cURL – UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/v1/public/subscriptions \
     --header 'Authorization: Bearer https://pluraluat.v2.pinepg.in/api/v1/public/plans' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_order_reference": "1234567890",
  "enable_notification": true,
  "plan_id": "v1-plan-4405071524-aa-qlAtAf",
  "webhook_url": "https://www.subscription-url-webhook.com",
  "quantity": 1,
  "start_date": "2022-07-21T17:32:28Z",
  "end_date": "2022-09-21T17:32:28Z",
  "customer_id": "123456",
  "payment_mode": [
    "UPI"
  ],
  "integration_mode": "SEAMLESS",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "is_tpv_enabled": true,
  "bank_account": {
    "account_number": "123456789012345",
    "name": "Gaurav Kumar",
    "ifsc": "123456789012345"
  }
}
'
```
```curl cURL – PROD
curl --request POST \
     --url https://api.pluralpay.in/api/v1/public/subscriptions \
     --header 'Authorization: Bearer https://pluraluat.v2.pinepg.in/api/v1/public/plans' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_order_reference": "1234567890",
  "enable_notification": true,
  "plan_id": "v1-plan-4405071524-aa-qlAtAf",
  "webhook_url": "https://www.subscription-url-webhook.com",
  "quantity": 1,
  "start_date": "2022-07-21T17:32:28Z",
  "end_date": "2022-09-21T17:32:28Z",
  "customer_id": "123456",
  "payment_mode": [
    "UPI"
  ],
  "integration_mode": "SEAMLESS",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "is_tpv_enabled": true,
  "bank_account": {
    "account_number": "123456789012345",
    "name": "Gaurav Kumar",
    "ifsc": "123456789012345"
  }
}
'
```
```json Sample Response
{
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "merchant_order_reference": "1234567890",
  "enable_notification": true,
  "plan_details": {
    "plan_id": "v1-plan-4405071524-aa-qlAtAf",
    "status": "ACTIVE",
    "plan_name": "Monthly Plan",
    "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
    "notes": "string",
    "frequency_count": 1,
    "frequency": "Day",
    "amount": {
      "value": 100,
      "currency": "INR"
    },
    "max_limit_amount": {
      "value": 100,
      "currency": "INR"
    },
    "trial_period_in_days": 1,
    "start_date": "2022-02-01T17:32:28Z",
    "end_date": "2022-10-21T17:32:28Z",
    "merchant_metadata": {
      "key1": "DD",
      "key2": "XOF"
    },
    "merchant_order_reference": "1234567890",
    "created_at": "2022-10-21T17:32:28Z",
    "modified_at": "2022-10-21T17:32:28Z"
  },
  "quantity": 1,
  "start_date": "2022-07-21T17:32:28Z",
  "end_date": "2022-09-21T17:32:28Z",
  "customer_id": "123456",
  "payment_mode": [
    "UPI"
  ],
  "integration_mode": "SEAMLESS",
  "webhook_url": "https://www.subscription-url-webhook.com",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "status": "ACTIVE",
  "bank_account": {
    "account_number": "123456789012345",
    "name": "Gaurav Kumar",
    "ifsc": "123456789012345"
  },
  "is_tpv_enabled": true,
  "created_at": "2022-10-21T17:32:28Z",
  "modified_at": "2022-10-21T17:32:28Z",
  "order_id": "v1-4405071524-aa-qlAtAf",
  "redirect_url": "https://api-staging.pluralonline.com/api/v3/checkout-bff/redirect/checkout?token=V3_D7LwszJqF2XRiFq46uOXQr0sQn8XbObLh7WM9YF8OAxQDYRnCMbhYgHbgFf4vCjJ%22&subscription_id=v1-sub-4405071524-aa-qlAtAf"
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/create-subscription" target="_blank">Create subscription API</a> documentation to learn more.

## 5. Create Payment

### 5.1 For Seamless Payment

To create a payment, use our Create Payment API, use the `order_id` returned in the response of a Create Subscription API to link the payment against an order.

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
    "callback_url": "https://sample-callback-url",
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
    "callback_url": "https://sample-callback-url",
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

### 5.2 Redirect Payment

To initiate the payment process, Use the `redirect_url` provided in the response of `Create Subscription` to direct the customer to the payment page.

```json Example
https://api-staging.pluralonline.com/api/v3/checkout-bff/redirect/checkout?token=V3_D7LwszJqF2XRiFq46uOXQr0sQn8XbObLh7WM9YF8OAxQDYRnCMbhYgHbgFf4vCjJ&subscription_id=v1-sub-4405071524-aa-qlAtAf
```

The customer will be directed to the payment page to complete the transaction using their selected payment method.

## 6. Handle Payment

In create payment API response we return a `challenge_url`, use this challenge url to navigate your customers to the checkout page to accept payment.

> 📘 Note:
> 
> - On successful payment we send the webhook event `ORDER_AUTHORIZED` and the status of the payment is updated to `authorized`.
> - You can capture or cancel an order only when the order status is `authorized`.

### 6.1 Store Payment Details on Your Server

On a successful and failed payment, we return the following fields to the return url.

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

### 6.2 Verify Payment Signature

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

## 7. Manage Subscription

### 7.1 Update a Subscription

To Update a Subscription, use our Update Subscription API, use the `subscription_id` returned in the response of a Create subscription API.

For authentication use the generated access token in the headers of the API request.

Below are the sample requests and response for the Update a Subscription API.

```curl cURL – UAT
curl --request PATCH \
     --url https://pluraluat.v2.pinepg.in/api/v1/public/subscriptions/v1-sub-4405071524-aa-qlAtAf \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "plan_id": "v1-plan-4405071524-aa-qlAtAf",
  "enable_notification": "true",
  "quantity": 1,
  "merchant_order_reference": "1234567890",
  "webhook_url": "https://www.subscription-url-webhook.com",
  "end_date": "2022-09-21T17:32:28Z",
  "payment_mode": "UPI"

"merchant_metadata": {
    "key_1": "DD",
    "key_2": "DD"
  },
}
'
```
```curl cURL – PROD
curl --request PATCH \
     --url https://api.pluralpay.in/api/v1/public/subscriptions/v1-sub-4405071524-aa-qlAtAf \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "plan_id": "v1-plan-4405071524-aa-qlAtAf",
  "enable_notification": "true",
  "quantity": 1,
  "merchant_order_reference": "1234567890",
  "webhook_url": "https://www.subscription-url-webhook.com",
  "end_date": "2022-09-21T17:32:28Z",
  "payment_mode": "UPI"

"merchant_metadata": {
    "key_1": "DD",
    "key_2": "DD"
  },
}
'
```
```json Sample Response
{
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "merchant_order_reference": "1234567890",
  "enable_notification": true,
  "plan_details": {
    "plan_id": "v1-plan-4405071524-aa-qlAtAf",
    "status": "ACTIVE",
    "plan_name": "Monthly Plan",
    "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
    "notes": "string",
    "frequency_count": 1,
    "frequency": "Day",
    "amount": {
      "value": 100,
      "currency": "INR"
    },
    "max_limit_amount": {
      "value": 100,
      "currency": "INR"
    },
    "trial_period_in_days": 1,
    "start_date": "2022-02-01T17:32:28Z",
    "end_date": "2022-10-21T17:32:28Z",
    "merchant_metadata": {
      "key1": "DD",
      "key2": "XOF"
    },
    "merchant_order_reference": "1234567890",
    "created_at": "2022-10-21T17:32:28Z",
    "modified_at": "2022-10-21T17:32:28Z"
  },
  "quantity": 1,
  "start_date": "2022-07-21T17:32:28Z",
  "end_date": "2022-09-21T17:32:28Z",
  "customer_id": "123456",
  "payment_mode": [
    "UPI"
  ],
  "integration_mode": "SEAMLESS",
  "webhook_url": "https://www.subscription-url-webhook.com",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "status": "ACTIVE",
  "bank_account": {
    "account_number": "123456789012345",
    "name": "Gaurav Kumar",
    "ifsc": "123456789012345"
  },
  "is_tpv_enabled": true,
  "created_at": "2022-10-21T17:32:28Z",
  "modified_at": "2022-10-21T17:32:28Z"
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/update-subscription" target="_blank">Update Subscription API</a> documentation to learn more.

### 7.3 Pause Subscription

To Pause Subscription, use our Pause Subscription API, use the `subscription_id` returned in the response of a Create subscription API.

For authentication use the generated access token in the headers of the API request.

Below are the sample requests and response for the Pause Subscription API.

```curl cURL – UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/v1/public/subscriptions/v1-sub-4405071524-aa-qlAtAf/pause \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json'
```
```curl cURL – PROD
curl --request POST \
     --url https://api.pluralpay.in/api/v1/public/subscriptions/v1-sub-4405071524-aa-qlAtAf/pause \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json'
```
```json Sample Response
{
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "merchant_order_reference": "1234567890",
  "enable_notification": true,
  "plan_details": {
    "plan_id": "v1-plan-4405071524-aa-qlAtAf",
    "status": "ACTIVE",
    "plan_name": "Monthly Plan",
    "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
    "notes": "string",
    "frequency_count": 1,
    "frequency": "Day",
    "amount": {
      "value": 100,
      "currency": "INR"
    },
    "max_limit_amount": {
      "value": 100,
      "currency": "INR"
    },
    "trial_period_in_days": 1,
    "start_date": "2022-02-01T17:32:28Z",
    "end_date": "2022-10-21T17:32:28Z",
    "merchant_metadata": {
      "key1": "DD",
      "key2": "XOF"
    },
    "merchant_order_reference": "1234567890",
    "created_at": "2022-10-21T17:32:28Z",
    "modified_at": "2022-10-21T17:32:28Z"
  },
  "quantity": 1,
  "start_date": "2022-07-21T17:32:28Z",
  "end_date": "2022-09-21T17:32:28Z",
  "customer_id": "123456",
  "payment_mode": [
    "UPI"
  ],
  "integration_mode": "SEAMLESS",
  "webhook_url": "https://www.subscription-url-webhook.com",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "status": "ACTIVE",
  "bank_account": {
    "account_number": "123456789012345",
    "name": "Gaurav Kumar",
    "ifsc": "123456789012345"
  },
  "is_tpv_enabled": true,
  "created_at": "2022-10-21T17:32:28Z",
  "modified_at": "2022-10-21T17:32:28Z"
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/pause-subscription" target="_blank">Pause Subscription API</a> documentation to learn more.

### 7.4 Resume Subscription

To Resume Subscription, use our Resume Subscription API, use the `subscription_id` returned in the response of a Create subscription API.

For authentication use the generated access token in the headers of the API request.

Below are the sample requests and response for the Resume Subscription API.

```curl cURL – UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/v1/public/subscriptions/v1-sub-4405071524-aa-qlAtAf/resume \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json'
```
```curl cURL – PROD
curl --request POST \
     --url https://api.pluralpay.in/api/v1/public/subscriptions/v1-sub-4405071524-aa-qlAtAf/resume \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json'
```
```json Sample Response
{
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "merchant_order_reference": "1234567890",
  "enable_notification": true,
  "plan_details": {
    "plan_id": "v1-plan-4405071524-aa-qlAtAf",
    "status": "ACTIVE",
    "plan_name": "Monthly Plan",
    "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
    "notes": "string",
    "frequency_count": 1,
    "frequency": "Day",
    "amount": {
      "value": 100,
      "currency": "INR"
    },
    "max_limit_amount": {
      "value": 100,
      "currency": "INR"
    },
    "trial_period_in_days": 1,
    "start_date": "2022-02-01T17:32:28Z",
    "end_date": "2022-10-21T17:32:28Z",
    "merchant_metadata": {
      "key1": "DD",
      "key2": "XOF"
    },
    "merchant_order_reference": "1234567890",
    "created_at": "2022-10-21T17:32:28Z",
    "modified_at": "2022-10-21T17:32:28Z"
  },
  "quantity": 1,
  "start_date": "2022-07-21T17:32:28Z",
  "end_date": "2022-09-21T17:32:28Z",
  "customer_id": "123456",
  "payment_mode": [
    "UPI"
  ],
  "integration_mode": "SEAMLESS",
  "webhook_url": "https://www.subscription-url-webhook.com",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "status": "ACTIVE",
  "bank_account": {
    "account_number": "123456789012345",
    "name": "Gaurav Kumar",
    "ifsc": "123456789012345"
  },
  "is_tpv_enabled": true,
  "created_at": "2022-10-21T17:32:28Z",
  "modified_at": "2022-10-21T17:32:28Z"
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/resume-subscription" target="_blank">Resume Subscription API</a> documentation to learn more.

### 7.5 Retrieve Subscription Invoices

To Retrieve Subscription Invoices, use our Get Invoices of a Subscription API, use the `subscription_id` returned in the response of a Create subscription API.

For authentication use the generated access token in the headers of the API request.

Below are the sample requests and response for the Get Invoices of a Subscription API.

```curl cURL – UAT
curl --request GET \
     --url 'https://pluraluat.v2.pinepg.in/api/v1/public/subscriptions/v1-sub-4405071524-aa-qlAtAf/invoices?page=2&size=10&sort=frequency_type%2Casc' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json'
```
```curl cURL – PROD
curl --request GET \
     --url 'https://api.pluralpay.in/api/v1/public/subscriptions/v1-sub-4405071524-aa-qlAtAf/invoices?page=2&size=10&sort=frequency_type%2Casc' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json'
```
```json Sample Response
{
  "links": {
    "first": {
      "href": "https://api.pluralpay.in/api/v1/public /{resource}/?size=10&page=0&sort=id,asc"
    },
    "self": {
      "href": "https://api.pluralpay.in/api/v1/public /{resource}/?size=10&page=0&sort=id,asc"
    },
    "next": {
      "href": "https://api.pluralpay.in/api/v1/public /{resource}/?size=10&page=0&sort=id,asc"
    },
    "last": {
      "href": "https://api.pluralpay.in/api/v1/public /{resource}/?size=10&page=0&sort=id,asc"
    }
  },
  "page": {
    "size": 10,
    "total_elements": 50,
    "total_pages": 5,
    "number": 1
  },
  "invoices": [
    {
      "invoice_id": "v1-inv-4405071524-aa-qlAtAf",
      "status": "SUCCESS",
      "due_amount": {
        "value": 100,
        "currency": "INR"
      },
      "remaining_amount": {
        "value": 100,
        "currency": "INR"
      },
      "paid_amount": {
        "value": 100,
        "currency": "INR"
      },
      "created_at": "2022-09-21T17:32:28Z",
      "payment_mode": "UPI",
      "debit_date": "2022-09-21T17:32:28Z",
      "due_date": "2022-09-21T17:32:28Z",
      "customer_id": "123456",
      "issuer_name": null,
      "merchant_metadata": {},
      "invoice_pdf": "https://api.pluralpay.in/api/v1/public/invoice-pdf/v1-inv-4405071524-aa-qlAtAf.pdf"
    }
  ]
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/get-invoices-of-a-subscription" target="_blank">Get Invoices of a Subscription API</a> documentation to learn more.

## 8. Schedule Recurring Payment

### 8.1 Create Presentation

To Create Presentation, use our Create Presentation API, use the `subscription_id` returned in the response of a Create subscription API to link the payment against a subscription.

For authentication use the generated access token in the headers of the API request.

Below are the sample requests and response for the Create Presentation API.

```curl cURL – UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/v1/public/subscriptions/subscription_id/presentations \
     --header 'Authorization: Bearer https://pluraluat.v2.pinepg.in/api/v1/public/plans' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "due_date": "2022-09-21T17:32:28Z",
  "amount": {
    "value": 100,
    "currency": "INR"
  },
  "merchant_order_reference": "1234567890",
  "customer_id": "123456",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  }
}
'
```
```curl cURL – PROD
curl --request POST \
     --url https://api.pluralpay.in/api/v1/public/subscriptions/subscription_id/presentations \
     --header 'Authorization: Bearer https://pluraluat.v2.pinepg.in/api/v1/public/plans' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "due_date": "2022-09-21T17:32:28Z",
  "amount": {
    "value": 100,
    "currency": "INR"
  },
  "merchant_order_reference": "1234567890",
  "customer_id": "123456",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  }
}
'
```
```json Sample Response
{
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "presentation_id": "v1-pre-4405071524-aa-qlAtAf",
  "due_date": "2022-09-21T17:32:28Z",
  "amount": {
    "value": 100,
    "currency": "INR"
  },
  "merchant_order_reference": "1234567890",
  "customer_id": "123456",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  }
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/create-presentation" target="_blank">Create Presentation API</a> documentation to learn more.

### 8.2 Retrieve a Presentation

To Retrieve a Presentation, use our Get Presentation API, use the `presentation_id` returned in the response of a Create Presentation API.

For authentication use the generated access token in the headers of the API request.

Below are the sample requests and response for the Get Presentation API.

```curl cURL – UAT
curl --request GET \
     --url https://pluraluat.v2.pinepg.in/api/v1/public/presentations/v1-pre-4405071524-aa-qlAtAf \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json'
```
```curl cURL – PROD
curl --request GET \
     --url https://api.pluralpay.in/api/v1/public/presentations/v1-pre-4405071524-aa-qlAtAf \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json'
```
```json Sample Response
{
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "presentation_id": "v1-pre-4405071524-aa-qlAtAf",
  "due_date": "2022-09-21T17:32:28Z",
  "amount": {
    "value": 100,
    "currency": "INR"
  },
  "merchant_order_reference": "1234567890",
  "customer_id": "123456",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  }
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/get-presentation" target="_blank">Get Presentation API</a> documentation to learn more.

### 8.3 Cancel Presentation

To Cancel Presentation, use our Cancel Presentation API, use the `presentation_id` returned in the response of a Create Presentation API.

For authentication use the generated access token in the headers of the API request.

Below are the sample requests and response for the Cancel Presentation API.

```curl cURL – UAT
curl --request DELETE \
     --url https://pluraluat.v2.pinepg.in/api/v1/public/presentations/v1-pre-4405071524-aa-qlAtAf \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json'
```
```curl cURL – PROD
curl --request DELETE \
     --url https://api.pluralpay.in/api/v1/public/presentations/v1-pre-4405071524-aa-qlAtAf \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json'
```
```json Sample Response
"ok"
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/cancel-presentation" target="_blank">Cancel Presentation API</a> documentation to learn more.

## To Know Your Payment Status

To check your payment status, you can either rely on Webhook events or use our **Get Orders** APIs for real-time updates.

1. **Webhook Notification**: We send Webhook notifications on the successful payment or any changes to the payments object. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/developer-tools-webhook" target="_blank">Webhooks</a> documentation to learn more.

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>API Request Tabs</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n        }\n        .tabs {\n            display: flex;\n            border-bottom: 2px solid #ddd;\n        }\n        .tab {\n            padding: 10px 15px;\n            cursor: pointer;\n            font-weight: bold;\n            color: #666;\n        }\n        .tab.active {\n            color: #f5b301;\n            border-bottom: 3px solid #f5b301;\n        }\n        .code-container {\n            background-color: #1e1e1e;\n            color: #fff;\n            padding: 15px;\n            font-family: monospace;\n            border-radius: 5px;\n            margin-top: 10px;\n            overflow-x: auto;\n        }\n        pre {\n            margin: 0;\n            white-space: pre-wrap;\n            word-wrap: break-word;\n        }\n    </style>\n</head>\n<body>\n\n    <div class=\"tabs\">\n        <div class=\"tab active\" onclick=\"showCode('curl')\">Curl</div>\n        <div class=\"tab\" onclick=\"showCode('java')\">Java</div>\n        <div class=\"tab\" onclick=\"showCode('python')\">Python</div>\n        <div class=\"tab\" onclick=\"showCode('go')\">Go</div>\n        <div class=\"tab\" onclick=\"showCode('php')\">PHP</div>\n        <div class=\"tab\" onclick=\"showCode('ruby')\">Ruby</div>\n        <div class=\"tab\" onclick=\"showCode('node')\">Node.js</div>\n    </div>\n\n    <div class=\"code-container\">\n        <pre id=\"code-block\"></pre>\n    </div>\n\n    <script>\n        const codeSnippets = {\n            \"curl\": `curl --request GET \\\\\n  --url https://pluraluat.v2.pinepg.in/api/v1/public/presentations/v1-pre-4405071524-aa-qlAtAf \\\\\n  --header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \\\\\n  --header 'Content-Type: application/json' \\\\\n  --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \\\\\n  --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \\\\\n  --header 'accept: application/json'`,\n  \n            \"java\": `import java.net.HttpURLConnection;\nimport java.net.URL;\n\npublic class APIRequest {\n    public static void main(String[] args) throws Exception {\n        URL url = new URL(\"https://pluraluat.v2.pinepg.in/api/v1/public/presentations/v1-pre-4405071524-aa-qlAtAf\");\n        HttpURLConnection conn = (HttpURLConnection) url.openConnection();\n        conn.setRequestMethod(\"GET\");\n        conn.setRequestProperty(\"Authorization\", \"Bearer YOUR_ACCESS_TOKEN\");\n        conn.setRequestProperty(\"Content-Type\", \"application/json\");\n        System.out.println(\"Response Code: \" + conn.getResponseCode());\n    }\n}`,\n\n            \"python\": `import requests\n\nurl = \"https://pluraluat.v2.pinepg.in/api/v1/public/presentations/v1-pre-4405071524-aa-qlAtAf\"\nheaders = {\n    \"Authorization\": \"Bearer YOUR_ACCESS_TOKEN\",\n    \"Content-Type\": \"application/json\"\n}\n\nresponse = requests.get(url, headers=headers)\nprint(response.json())`,\n\n            \"go\": `package main\n\nimport (\n    \"fmt\"\n    \"net/http\"\n)\n\nfunc main() {\n    req, _ := http.NewRequest(\"GET\", \"https://pluraluat.v2.pinepg.in/api/v1/public/presentations/v1-pre-4405071524-aa-qlAtAf\", nil)\n    req.Header.Set(\"Authorization\", \"Bearer YOUR_ACCESS_TOKEN\")\n    req.Header.Set(\"Content-Type\", \"application/json\")\n\n    client := &http.Client{}\n    resp, _ := client.Do(req)\n    fmt.Println(resp.Status)\n}`,\n\n            \"php\": `<?php\n$ch = curl_init();\ncurl_setopt($ch, CURLOPT_URL, \"https://pluraluat.v2.pinepg.in/api/v1/public/presentations/v1-pre-4405071524-aa-qlAtAf\");\ncurl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);\ncurl_setopt($ch, CURLOPT_HTTPHEADER, [\n    \"Authorization: Bearer YOUR_ACCESS_TOKEN\",\n    \"Content-Type: application/json\"\n]);\n$response = curl_exec($ch);\ncurl_close($ch);\necho $response;\n?>`,\n\n            \"ruby\": `require 'net/http'\nrequire 'uri'\n\nuri = URI.parse(\"https://pluraluat.v2.pinepg.in/api/v1/public/presentations/v1-pre-4405071524-aa-qlAtAf\")\nrequest = Net::HTTP::Get.new(uri)\nrequest[\"Authorization\"] = \"Bearer YOUR_ACCESS_TOKEN\"\nrequest[\"Content-Type\"] = \"application/json\"\n\nresponse = Net::HTTP.start(uri.hostname, uri.port, use_ssl: true) do |http|\n  http.request(request)\nend\n\nputs response.body`,\n\n            \"node\": `const axios = require('axios');\n\nconst options = {\n  method: 'GET',\n  url: 'https://pluraluat.v2.pinepg.in/api/v1/public/presentations/v1-pre-4405071524-aa-qlAtAf',\n  headers: {\n    Authorization: 'Bearer YOUR_ACCESS_TOKEN',\n    'Content-Type': 'application/json'\n  }\n};\n\naxios.request(options).then(response => {\n  console.log(response.data);\n}).catch(error => {\n  console.error(error);\n});`\n        };\n\n        function showCode(language) {\n            document.getElementById(\"code-block\").textContent = codeSnippets[language];\n\n            // Highlight active tab\n            document.querySelectorAll(\".tab\").forEach(tab => {\n                tab.classList.remove(\"active\");\n            });\n            document.querySelector(`.tab[onclick=\"showCode('${language}')\"]`).classList.add(\"active\");\n        }\n\n        // Load Curl as default\n        showCode(\"curl\");\n    </script>\n\n</body>\n</html>\n"
}
[/block]
