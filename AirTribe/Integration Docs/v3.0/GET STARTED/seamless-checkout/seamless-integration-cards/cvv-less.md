---
title: "CVV Less Flow"
slug: "cvv-less"
excerpt: "Learn how you can save card details as tokens and enable CVV-less payment flow for customers via Plural."
hidden: false
createdAt: "Fri Oct 18 2024 06:02:06 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Mar 24 2025 10:25:20 GMT+0000 (Coordinated Universal Time)"
---
A CVV-less transaction allows your customers to process a payment without requiring their card's CVV [Card Verification Value]. This can be used for saved cards as tokens, where CVV is not necessary for repeated transactions, such as tokenized payments or card-on-file services.

CVV-less transactions enhance customer convenience by simplifying the payment process for recurring or saved card transactions. This improves the customer experience by reducing friction during checkout. While still maintaining security through tokenization and other robust verification methods. This balance enhances convenience without compromising safety.

## Supported Networks:

- Visa
- Mastercard

> 📘 NOTE:
> 
> - This feature is only supported for seamless card transactions.
> - You can implement a CVV-less flow for processing payments on your systems, provided that the token type used is `NETWORK_TOKEN`.
> - For Visa and Mastercard tokenized transactions, the cvv parameter can be omitted.

## Tokenized Card Payment without CVV

Use our [Payment via Card Token API](https://developer.pluralonline.com/reference/card-payments-create) to process a tokenized card payment without CVV[Card Verification Value].

Shown below is a sample request and sample response for a Tokenized Card Payment.

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
        "value": 1100,
        "currency": "INR"
      },
      "payment_option": {
        "card_token_details": {
          "name": "Kevin",
          "last4_digit": "1234",
          "expiry_month": "03",
          "expiry_year": "30",
          "cvv":"123", // cvv parameter can be omitted for Visa and Mastercard tokenized payments
          "token": "4000000000001091",
          "cryptogram": "/wAAAAAAl9SX1HsAmWKSgqwAAAA=",
          "token_txn_type": "NETWORK_TOKEN",
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
      "payment_method": "CARD",
      "payment_amount": {
        "value": 1100,
        "currency": "INR"
      },
      "payment_option": {
        "card_token_details": {
          "name": "Kevin",
          "last4_digit": "1234",
          "expiry_month": "03",
          "expiry_year": "30",
          "cvv":"123", // cvv parameter can be omitted for Visa and Mastercard tokenized payments
          "token": "4000000000001091",
          "cryptogram": "/wAAAAAAl9SX1HsAmWKSgqwAAAA=",
          "token_txn_type": "NETWORK_TOKEN",
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
  "data": {
    "order_id": "v1-241007052351-aa-uXmn5S",
    "merchant_order_reference": "ab4756d5-bcaa-419e-a13c-dcf8c8410b60",
    "type": "CHARGE",
    "status": "PENDING",
    "challenge_url": "https://pluraluat.v2.pinepg.in/web/auth/landing/?token=S50TpKleRC1badrnan295BUX0VQ3tDWZC922nXnhPO%2BKHKegMc1RDKvPWs6BwHWR%2FHw",
    "merchant_id": "108272",
    "order_amount": {
      "value": 1100,
      "currency": "INR"
    },
    "pre_auth": false,
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
        "id": "v1-241007052351-aa-uXmn5S-cc-x",
        "status": "PENDING",
        "payment_amount": {
          "value": 1100,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "DEBIT",
            "network_name": "Visa",
            "issuer_name": "INTL HDQTRS-CENTER OWNED",
            "card_category": "Commercial",
            "country_code": "IND",
            "token_txn_type": "NETOWRK_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "7282786475376849903955",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2024-10-07T05:24:04.757Z",
        "updated_at": "2024-10-07T05:24:08.193Z"
      }
    ],
    "created_at": "2024-10-07T05:23:51.175Z",
    "updated_at": "2024-10-07T05:24:08.193Z"
  }
}
```

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/card-payments-create" target="_blank">Create Card Payment API</a> to learn more.

> 📘 Note:
> 
> CVV-less can only be tested on Production environment.
