---
title: "Native OTP"
slug: "card-payments-native-otp"
excerpt: "Learn how you can integrate with Plural APIs to start accepting payments on your website using OTP."
hidden: false
createdAt: "Tue Feb 18 2025 06:26:42 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Apr 23 2025 07:47:18 GMT+0000 (Coordinated Universal Time)"
---
Plural's 3D Secure Native OTP feature empowers you to manage the entire authentication process within your platform by eliminating the need to redirect users to the Access Control Server (ACS) page. By leveraging this feature, you can generate, resend, and verify One-Time Passwords (OTPs) through our APIs, ensuring a smooth authentication experience while maintaining complete control over the user interface.

## Key Benefits

**Seamless Authentication** – Your customers can complete the entire authentication flow on your platform without redirections.

**Brand Consistency**: This allows you to customize the OTP entry interface to align with your brand identity.

**Lower Drop-offs**: Reduce transaction abandonment due to redirection delays or network issues.

**Enhanced Insights**: Helps you to gain better visibility of your customer authentication behavior.

**Higher Conversion Rates**: Improve authentication success rates by 2-3%.

**Flexible Implementation**: Supports fallback to traditional ACS redirection when necessary.

## How It Works

Instead of directing your customers to an external 3D Secure page, the entire OTP-based authentication process happens within your website or application:

1. The customer initiates a payment on your platform.
2. The system triggers an OTP request via API.
3. The issuing bank sends the OTP to the customer.
4. The customer enters the OTP using your customized interface.
5. The OTP is submitted via API for verification.
6. The transaction is processed seamlessly without redirection.

This approach enhances user experience, reduces friction, and improves transaction success rates by keeping customers engaged within your platform.

## Supported Issuer Banks and Card Networks

[block:html]
{
  "html": "<!DOCTYPE html>\n<html>\n<head>\n    <title>Card Issuer Table</title>\n    <style>\n        table {\n            width: 100%;\n            border-collapse: collapse;\n        }\n        th, td {\n            border: 1px solid black;\n            padding: 10px;\n            text-align: center;\n        }        \n    </style>\n</head>\n<body>\n    <table>\n        <tr>\n            <th rowspan=\"2\">Card Issuer</th>\n            <th colspan=\"3\">NETWORK</th>\n        </tr>\n        <tr>\n            <th>VISA</th>\n            <th>MASTERCARD</th>\n            <th>RUPAY</th>\n        </tr>\n        <tr>\n            <td>ICICI Credit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td></td>\n        </tr>\n        <tr>\n            <td>ICICI Debit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td></td>\n        </tr>\n        <tr>\n            <td>HDFC Credit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n        </tr>\n        <tr>\n            <td>HDFC Debit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td></td>\n        </tr>\n        <tr>\n            <td>AXIS Credit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td></td>\n        </tr>\n        <tr>\n            <td>AXIS Debit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td></td>\n        </tr>\n        <tr>\n            <td>SBI Credit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n        </tr>\n        <tr>\n            <td>SBI Debit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td></td>\n        </tr>\n        <tr>\n            <td>KOTAK Credit Card</td>\n            <td>&#10004;</td>\n            <td></td>\n            <td></td>\n        </tr>\n        <tr>\n            <td>KOTAK Debit Card</td>\n            <td>&#10004;</td>\n            <td></td>\n            <td></td>\n        </tr>\n        <tr>\n            <td>YESBANK Credit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td></td>\n        </tr>\n    </table>\n</body>\n</html>\n"
}
[/block]


> 📘 Important
> 
> - The Native OTP flow enables you to cover `88.52%` of all transactions across all card issuers.

***

## Integration Steps

Follow the below steps to integrate with Plural Native OTP APIs in your application.

1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/3d-secure-authoriation#1-prerequisite-generate-token" >\[Prerequisite] Generate Token</a>
2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/3d-secure-authoriation#2-create-order" >Create Order</a>
3. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/3d-secure-authoriation#3-create-payment" >Create Payment</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/3d-secure-authoriation#31-get-card-details" >Get Card Details</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/3d-secure-authoriation#32-send-otp" >Generate OTP</a>
   3. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/3d-secure-authoriation#33-verify-otp" >Submit OTP</a>
   4. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/3d-secure-authoriation#34-resend-otp" >Resend OTP</a>
4. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/3d-secure-authoriation#4-handle-payment" >Handle Payment</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/3d-secure-authoriation#41-store-payment-details-on-your-server" >Store Payment Details on Your Server</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/3d-secure-authoriation#42-verify-payment-signature" >Verify Payment Signature</a>
5. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/3d-secure-authoriation#5-capture-order" >Capture Order</a>
6. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/3d-secure-authoriation#6-cancel-order" >Cancel Order</a>

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
  "merchant_order_reference": 112345,
  "order_amount": {
    "value": 1100,
    "currency": "INR"
  },
  "pre_auth": false,    
  "notes": "order1",
  "callback_url":"https://sample-callback-url",
  "failure_callback_url": "https://sample-failure-callback-url",
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
      "key1": "DD",
      "key2": "XOF"
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
  "merchant_order_reference": 112345,
  "order_amount": {
    "value": 1100,
    "currency": "INR"
  },
  "pre_auth": false,    
  "notes": "order1",
  "callback_url":"https://sample-callback-url",
  "failure_callback_url": "https://sample-failure-callback-url",
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
      "key1": "DD",
      "key2": "XOF"
    }
  }
}
'
```
```json Sample Response
{
  "data": {
    "order_id": "v1-4405071524-aa-qlAtAf",
    "merchant_order_reference": "112345",
    "type": "CHARGE",
    "status": "CREATED",
    "merchant_id": "104359",
    "order_amount": {
      "value": 1100,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
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
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [],
    "created_at": "2024-07-15T05:44:51.174Z",
    "updated_at": "2024-07-15T05:44:51.174Z"
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
      "merchant_payment_reference": "merchant-payment-reference-r4y",
      "payment_method": "CARD",
      "payment_amount": {
        "value": 35000,
        "currency": "INR"
      },
      "payment_option": {
        "card_details": {
          "name": "Kevin",
          "card_number": "2870-2870-2870-2870",
          "cvv": "235",
          "expiry_month": "03",
          "expiry_year": "30"
        }
      },
      "device_info": {
        "browser_accept_header": "*/*",
        "browser_user_agent": "mozilla/5.0+x11;+ubuntu;+linux+x86_64;+rv:72.0)+gecko/20100101+firefox/72.0",
        "browser_language": "en",
        "browser_screen_height": "768",
        "browser_screen_width": "1366",
        "browser_timezone": "-330",
        "browser_window_size": "1366x768",
        "browser_screen_color_depth": "24",
        "browser_java_enabled_val": "true",
        "browser_javascript_enabled_val": "true",
        "device_channel": "browser"
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
      "merchant_payment_reference": "merchant-payment-reference-r4y",
      "payment_method": "CARD",
      "payment_amount": {
        "value": 35000,
        "currency": "INR"
      },
      "payment_option": {
        "card_details": {
          "name": "Kevin",
          "card_number": "2870-2870-2870-2870",
          "cvv": "235",
          "expiry_month": "03",
          "expiry_year": "30"
        }
      },
      "device_info": {
        "browser_accept_header": "*/*",
        "browser_user_agent": "mozilla/5.0+x11;+ubuntu;+linux+x86_64;+rv:72.0)+gecko/20100101+firefox/72.0",
        "browser_language": "en",
        "browser_screen_height": "768",
        "browser_screen_width": "1366",
        "browser_timezone": "-330",
        "browser_window_size": "1366x768",
        "browser_screen_color_depth": "24",
        "browser_java_enabled_val": "true",
        "browser_javascript_enabled_val": "true",
        "device_channel": "browser"
      }
    }
  ]
}
'
```
```json Sample Response
{
  "data": {
    "order_id": "v1-5312042524-aa-0YO29z",
    "merchant_order_reference": "merchant-reference-r4y",
    "type": "CHARGE",
    "status": "CREATED",
    "challenge_url": "https://pluraluat.v2.pinepg.in/web/auth/landing/?token=S50w2VcwX9f3EQ%2B%2BYUb5lb%2FBp1TDpaXXuCSoyDmAfTQtxQFv09dv7LS4%2BApSGcMXFom",
    "merchant_id": "merchant-123",
    "order_amount": {
      "value": 35000,
      "currency": "INR"
    },
    "pre_auth": false,
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "payments": [
      {
        "id": "v1-0252192429-wa-0IOa9q",
        "merchant_payment_reference": "merchant-payment-reference-r4y",
        "status": "PENDING",
        "payment_amount": {
          "value": 35000,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "HDFC",
            "country_code": "IND"
          }
        },
        "convenience_fee_breakdown": {
          "fee_amount": {
            "value": 5000,
            "currency": "INR"
          },
          "tax_amount": {
            "value": 1080,
            "currency": "INR"
          },
          "additional_fee_amount": {
            "value": 1000,
            "currency": "INR"
          },
          "maximum_fee_amount": {
            "value": 4999,
            "currency": "INR"
          },
          "applicable_fee_amount": {
            "value": 4999,
            "currency": "INR"
          }
        },
        "created_at": "2024-04-30T08:01:32Z",
        "updated_at": "2024-04-30T08:01:32Z"
      }
    ],
    "created_at": "2024-04-30T08:01:32Z",
    "updated_at": "2024-04-30T08:01:32Z"
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/reference/card-payments-create" target="_blank">Create Payment API</a> documentation to learn more.

> 📘 Note:
> 
> - Follow the steps below to process the transaction using the native OTP flow. Or you can use the `chanllenge_url` to continue with the standard ACS [Access Control Server] flow.

### 3.1 Get Card Details

Use this API to fetch the card details.

Below are the sample requests and sample response for a Get Card Details API.

```curl cURL - UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/getCardDetails \
     --header 'Authorization: Bearer <access_token>' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "amount": "100",
  "card_details": [
    {
      "payment_identifier": "4012001037141112",
      "payment_reference_type": "CARD"
    }
  ]
}
'
```
```curl cURL - PROD
curl --request POST \
     --url https://api.pluralpay.in/api/pay/v1/getCardDetails \
     --header 'Authorization: Bearer <access_token>' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "amount": "100",
  "card_details": [
    {
      "payment_identifier": "4012001037141112",
      "payment_reference_type": "CARD"
    }
  ]
}
'
```
```json Sample Response
{
  "card_payment_details":[
    {
      "card_network":"VISA",
      "card_issuer":"INTL HDQTRS-CENTER OWNED",
      "card_type":"CREDIT",
      "card_category":"NONE",
      "is_international_card":false,
      "is_native_otp_supported":true,
      "country_code":"IND",
      "currency":"INR",
      "is_currency_supported":true
    }
  ]
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/reference/get-card-details" target="_blank">Get Card Details API</a> documentation to learn more.

### 3.2. Generate OTP

Use this API to generate and send an OTP to the registered mobile number.

Below are the sample requests and sample response for a Generate OTP API.

```curl cURL - UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/otp/generate \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "payment_id": "v1-250219120455-aa-Lc5FbR-cc-a"
}
'
```
```curl cURL - PROD
curl --request POST \
     --url https://api.pluralpay.in/api/pay/v1/otp/generate \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "payment_id": "v1-250219120455-aa-Lc5FbR-cc-a"
}
'
```
```json Sample Response
{
  "next": [
    "SUBMIT_OTP",
    "RESEND_OTP"
  ],
  "meta_data": {
    "resend_after": "180"
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/reference/card-payments-generate-otp" target="_blank">Send OTP API</a> documentation to learn more.

### 3.3. Submit OTP

Use this API to submit the OTP for verification.

Below are the sample requests and sample response for a Submit OTP API.

```curl cURL - UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/otp/submit \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "payment_id": "v1-250219120455-aa-Lc5FbR-cc-a",
  "otp": 1234
}
'
```
```curl cURL - PROD
curl --request POST \
     --url https://api.pluralpay.in/api/pay/v1/otp/submit \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "payment_id": "v1-250219120455-aa-Lc5FbR-cc-a",
  "otp": 1234
}
'
```
```json Sample Response
{
  "status": "SUCCESS"
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/reference/card-payments-submit-otp" target="_blank">Verify OTP API</a> documentation to learn more.

### 3.4. Resend OTP

Use this API to resend a OTP to the registered mobile number.

Below are the sample requests and sample response for a Resend OTP API.

```curl cURL - UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/otp/resend \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "payment_id": "v1-250219120455-aa-Lc5FbR-cc-a"
}
'
```
```curl cURL - PROD
curl --request POST \
     --url https://api.pluralpay.in/api/pay/v1/otp/resend \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --data '
{
  "payment_id": "v1-250219120455-aa-Lc5FbR-cc-a"
}
'
```
```json Sample Response
{
  "status": "SUCCESS",
  "next": [
    "SUBMIT_OTP",
    "RESEND_OTP"
  ],
  "meta_data": {
    "resend_after": "180"
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/reference/card-payments-resend-otp" target="_blank">Resend OTP API</a> documentation to learn more.

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

> 📘 Important:
> 
> - With pre-authorization set to true, you can capture or cancel a payment for an order.

## 5. Capture Order

Use this API to capture the payment against an order. On successful capture of an order the order status is updated as `processed`.

Shown below are the sample requests and sample response for a Capture Order API.

```curl cURL - UAT
curl --request PUT \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/orders/order_id/capture \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_capture_reference": "merchant-capture-ref-r4y",
  "capture_amount": {
    "value": 4000,
    "currency": "INR"
  }
}
'
```
```curl cURL - PROD
curl --request PUT \
     --url https://api.pluralpay.in/api/pay/v1/orders/order_id/capture \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_capture_reference": "merchant-capture-ref-r4y",
  "capture_amount": {
    "value": 4000,
    "currency": "INR"
  }
}
'
```
```json Sample Response
{
  "data": {
    "order_id": "v1-5757575757-aa-hU1rUd",
    "merchant_order_reference": "f4548bbf-a029-43d3-9209-e3385c80b1e9",
    "type": "CHARGE",
    "status": "PROCESSED",
    "merchant_id": "123456",
    "order_amount": {
      "value": 1100,
      "currency": "INR"
    },
    "pre_auth": true,    
    "notes": "order1",
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "232323",
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
          "address2": "string",
          "address3": "string",
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
        "id": "v1-1111071924-aa-zzSkOA-cc-G",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 1100,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "NONE",
            "card_category": "CONSUMER",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "000000",
          "acquirer_reference": "202456643801053",
          "rrn": "420145000226"
        },
        "capture_data": [
          {
            "merchant_capture_reference": "f31d8c60-0dc8-4788-a577-5ced930cc175",
            "capture_amount": {
              "value": 1100,
              "currency": "INR"
            },
            "created_at": "2024-07-19T11:13:21.523Z"
          }
        ],
        "created_at": "2024-07-19T11:11:48.944Z",
        "updated_at": "2024-07-19T11:13:23.962Z"
      }
    ],
    "created_at": "2024-07-19T11:11:48.944Z",
    "updated_at": "2024-07-19T11:13:23.962Z"
  }
}
```

Refer to our <a style="text-decoration:none;" href="https://developer.pluralonline.com/v3.0/reference/orders-capture" target="_blank">Capture Order API</a> documentation to learn more.

## 6. Cancel Order

Use this API to cancel the payment against an order.

Use the below endpoint to cancel the payment against the order.

```text Cancel Order Endpoint for UAT
PUT: https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/cancel
```
```text Cancel Order Endpoint for PROD
PUT: https://api.pluralpay.in/api/pay/v1/orders/{order_id}/cancel
```

Shown below is a sample request and sample response for a Cancel Order API.

```json Sample Response
{
  "data": {
    "order_id": "v1-5757575757-aa-hU1rUd",
    "merchant_order_reference": "2177120b-3be1-4330-a15f-53ce14d19841",
    "type": "CHARGE",
    "status": "CANCELLED",
    "merchant_id": "123456",
    "order_amount": {
      "value": 50000,
      "currency": "INR"
    },
    "pre_auth": true,    
    "notes": "order1",
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "232323",
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
        "id": "v1-2711071924-aa-VxIzq1-cc-Z",
        "status": "CANCELLED",
        "payment_amount": {
          "value": 1100,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "NONE",
            "card_category": "CONSUMER",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "000000",
          "acquirer_reference": "202456644249243",
          "rrn": "420123000239"
        },
        "created_at": "2024-07-19T11:27:55.664Z",
        "updated_at": "2024-07-19T11:28:52.487Z"
      }
    ],
    "created_at": "2024-07-19T11:27:55.664Z",
    "updated_at": "2024-07-19T11:28:52.487Z"
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/v3.0/reference/orders-cancel" target="_blank">Cancel Order API</a> documentation to learn more.
