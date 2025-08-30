---
title: "Manage Subscription"
slug: "manage-subscription"
excerpt: "Learn how to manage the subscriptions."
hidden: true
createdAt: "Wed Mar 05 2025 06:40:28 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Apr 14 2025 07:25:09 GMT+0000 (Coordinated Universal Time)"
---
Integrate the Below APIs to Efficiently Manage Subscriptions and Payments.

## 1. Update a Subscription

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

## 2. Pause Subscription

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

## 3. Resume Subscription

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

## 4. Retrieve Subscription Invoices

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
