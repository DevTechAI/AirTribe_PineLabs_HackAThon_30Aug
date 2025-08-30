---
title: "Integration Steps"
slug: "subscription-integration-steps"
excerpt: "Learn how to integrate subscription APIs to automate plan creation, subscription management, and scheduled payments."
hidden: false
createdAt: "Thu Feb 27 2025 05:56:44 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Apr 14 2025 07:25:31 GMT+0000 (Coordinated Universal Time)"
---
# Auto-debit flow

Follow the below steps to integrate with Plural subscription APIs for Auto-debit flow.

1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/subscription-integration-steps#1-prerequisite-generate-token" >\[Prerequisite] Generate Token</a>
2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/subscription-integration-steps#2-create-plan" >Create Plan</a>
3. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/subscription-integration-steps#3-create-subscription" >Create Subscription</a>
4. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/subscription-integration-steps#4-create-payment" >Create Payment</a>
5. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/subscription-integration-steps#5-handle-payment" >Handle Payment</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/subscription-integration-steps#51-store-payment-details-on-your-server" >Store Payment Details on Your Server</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/subscription-integration-steps#52-verify-payment-signature" >Verify Payment Signature</a>

> 📘 Note
> 
> - Ensure you store your Client ID and Secret in your Backend securely.
> - Integrate our APIs on your backend system.
> - We strictly recommend not to call our APIs from the frontend.
> - Failure to adhere to the above guidelines may result in legal implications. In such cases, you will be held responsible for any damage or loss arising from non-compliance.

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
  "merchant_plan_reference": "1234567890"
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
  "merchant_plan_reference": "1234567890"
}
'
```
```json Sample Response
{
  "plan_id": "v1-plan-4405071524-aa-qlAtAf",
  "status": "ACTIVE",
  "plan_name": "Monthly Plan",
  "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
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
  "merchant_plan_reference": "1234567890",
  "created_at": "2022-10-21T17:32:28Z",
  "modified_at": "2022-10-21T17:32:28Z"
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/create-plan" target="_blank">Create Plan API</a> documentation to learn more.

## 3. Create Subscription

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
  "merchant_subscription_reference": "1234567890",
  "enable_notification": true,
  "plan_id": "1",
  "quantity": 1,
  "start_date": "2022-07-21T17:32:28Z",
  "end_date": "2022-09-21T17:32:28Z",
  "customer_id": "123456",
  "allowed_payment_methods": [
    "UPI"
  ],
  "integration_mode": "SEAMLESS",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "is_tpv_enabled": false,
  "bank_account": {
    "account_number": "123456789012345",
    "name": "Gaurav Kumar",
    "ifsc": "123456789012345"
  },
  "callback_url": "https://www.example.com",
  "failure_callback_url": "https://www.example.com"
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
  "merchant_subscription_reference": "1234567890",
  "enable_notification": true,
  "plan_id": "1",
  "quantity": 1,
  "start_date": "2022-07-21T17:32:28Z",
  "end_date": "2022-09-21T17:32:28Z",
  "customer_id": "123456",
  "allowed_payment_methods": [
    "UPI"
  ],
  "integration_mode": "SEAMLESS",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "is_tpv_enabled": false,
  "bank_account": {
    "account_number": "123456789012345",
    "name": "Gaurav Kumar",
    "ifsc": "123456789012345"
  },
  "callback_url": "https://www.example.com",
  "failure_callback_url": "https://www.example.com"
}
'
```
```json Sample Response
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "merchant_subscription_reference": "1234567890",
  "enable_notification": true,
  "plan_details": {
    "plan_id": "v1-plan-4405071524-aa-qlAtAf",
    "status": "ACTIVE",
    "plan_name": "Monthly Plan",
    "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
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
    "merchant_plan_reference": "1234567890",
    "created_at": "2022-10-21T17:32:28Z",
    "modified_at": "2022-10-21T17:32:28Z"
  },
  "quantity": 1,
  "start_date": "2022-07-21T17:32:28Z",
  "end_date": "2022-09-21T17:32:28Z",
  "customer_id": "123456",
  "payment_mode": "UPI",
  "allowed_payment_methods": [
    "UPI"
  ],
  "integration_mode": "SEAMLESS",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "status": "ACTIVE",
  "is_tpv_enabled": true,
  "bank_account": {
    "account_number": "123456789012345",
    "name": "Gaurav Kumar",
    "ifsc": "123456789012345"
  },
  "created_at": "2022-10-21T17:32:28Z",
  "modified_at": "2022-10-21T17:32:28Z",
  "callback_url": "https://www.example.com",
  "failure_callback_url": "https://www.example.com",
  "redirect_url": "https://api-staging.pluralonline.com/api/v3/checkout-bff/redirect/checkout?token=V3_D7LwszJqF2XRiFq46uOXQr0sQn8XbObLh7WM9YF8OAxQDYRnCMbhYgHbgFf4vCjJ%22&subscription_id=v1-sub-4405071524-aa-qlAtAf"
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/create-subscription" target="_blank">Create subscription API</a> documentation to learn more.

## 4. Create Payment

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
  "payments": [
    {
      "payment_method": "UPI",
      "merchant_payment_reference": "108cf506-c6a1-4535-9e7f-3af9c6d3d90c",
      "payment_amount": {
        "value": 100,
        "currency": "INR"
      },
      "payment_option": {
        "upi_details": {
          "txn_mode": "INTENT"
        }
      },
      "mandate_info": {
        "request_type": "CREATE_MANDATE"
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
      "payment_method": "UPI",
      "merchant_payment_reference": "108cf506-c6a1-4535-9e7f-3af9c6d3d90c",
      "payment_amount": {
        "value": 100,
        "currency": "INR"
      },
      "payment_option": {
        "upi_details": {
          "txn_mode": "INTENT"
        }
      },
      "mandate_info": {
        "request_type": "CREATE_MANDATE"
      }
    }
  ]
}
'
```
```json Sample Response
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
            "payment_method": "UPI",
            "merchant_payment_reference": "56d3cd91-9bb1-459c-8358-d92ef62d38ee",
            "payment_amount": {
                "value": 100,
                "currency": "INR"
            },
            "payment_option": {
                "upi_details": {
                    "txn_mode": "COLLECT",
                    "payer": {
                        "vpa": "9280850298@oksbi"
                    }
                }
            },
            "mandate_info": {
                "request_type": "CREATE_MANDATE"
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
            "payment_method": "UPI",
            "merchant_payment_reference": "56d3cd91-9bb1-459c-8358-d92ef62d38ee",
            "payment_amount": {
                "value": 100,
                "currency": "INR"
            },
            "payment_option": {
                "upi_details": {
                    "txn_mode": "COLLECT",
                    "payer": {
                        "vpa": "9280850298@oksbi"
                    }
                }
            },
            "mandate_info": {
                "request_type": "CREATE_MANDATE"
            }
        }
    ]
}
'
```
```json Sample Response
{
  "data": {
    "order_id": "v1-250408102515-aa-x2F8Qw",
    "merchant_order_reference": "8b5e2b5b-9fde-4010-af9c-281f9e2fa5af",
    "type": "CHARGE",
    "status": "PENDING",
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

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/v3.0/reference/payments-create" target="_blank">Create Payment API</a> documentation to learn more.

## 5. Handle Payment

In create payment API response we return a `challenge_url`, use this challenge url to navigate your customers to the checkout page to accept payment.

> 📘 Note:
> 
> - This `challenge_url` is applicable only for UPI Intent flow.
> - For UPI Collect flow, the customer will receive a notification in their UPI app to authorize the payment.

> 📘 Note:
> 
> - On successful payment we send the webhook event `ORDER_AUTHORIZED` and the status of the payment is updated to `authorized`.
> - You can capture or cancel an order only when the order status is `authorized`.

### 5.1 Store Payment Details on Your Server

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

## To Know Your Payment Status and Manage subscription

To check your payment status, you can rely on Webhook events.

1. **Webhook Notification**: We send Webhook notifications on the successful payment or any changes to the payments object. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/developer-tools-webhook" target="_blank">Webhooks</a> documentation to learn more.
2. **Manage Plan**: To manage the Plan, refer to below APIs to learn more.
   1. `Update Plan`: To Update Plan details, use our <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/reference/update-plan" >Update Plan API</a>.
   2. `Delete Plan`: To Delete a plan, use our <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/reference/delete-plan" >Delete Plan API</a>.
3. **Manage Subscription**: To manage the subscription, refer to below APIs to learn more.
   1. `Pause Subscription`: To Pause a Subscription, use our <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/reference/pause-subscription" >Pause Subscription API</a>.
   2. `Resume Subscription`: To Resume a Subscription, use our <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/reference/resume-subscription" >Resume Subscription API</a>.

> 📘 **NOTE: **
> 
> If the Auto Debit payment is disabled, follow the steps to create a scheduled recurring payment manually.

## Schedule Recurring Payment

### Create Presentation

To Schedule Recurring Payment, use our Create Presentation API, use the `subscription_id` returned in the response of a Create subscription API to link the payment against a subscription.

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
  "merchant_presentation_reference": "1234567890"
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
  "merchant_presentation_reference": "1234567890"
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
  "merchant_presentation_reference": "1234567890"
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/create-presentation" target="_blank">Create Presentation API</a> documentation to learn more.
