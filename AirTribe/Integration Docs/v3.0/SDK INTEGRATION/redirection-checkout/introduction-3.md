---
title: "Introduction"
slug: "introduction-3"
excerpt: "Integrate with Plural's hosted checkout to allow Plural to manage the checkout process on your site, providing your customers with a smooth and seamless experience."
hidden: true
createdAt: "Fri Sep 13 2024 08:05:35 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 12:53:02 GMT+0000 (Coordinated Universal Time)"
---
**Hosted/Redirect Checkout** allows you to hand over the entire checkout process to Plural, ensuring a seamless and secure experience. Customer payment information is safely stored with Plural, removing the need for **PCI **compliance implementation on your end. Customers are redirected to a **Plural-hosted page** to complete their payment, and their payment details are securely transmitted to Plural's servers, guaranteeing a smooth and protected transaction.

***

## Plural Hosted Checkout Flow

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0133f6c5ea07be39b73aade74083d860718019530d547592b89a4c41f0e279f1-Screenshot_2024-09-13_at_1.58.32_PM.png",
        "",
        "**Redirect Checkout Flow on Plural**"
      ],
      "align": "center",
      "caption": "**Redirect Checkout Flow on Plural**"
    }
  ]
}
[/block]


**How it works:**

1. Merchants integrate Plural’s payment gateway into their website.
2. Customers choose their preferred payment method and enter payment details on the form.
3. Upon clicking the "Pay" button, customers are redirected to a Plural-hosted payment page to complete the transaction.
4. Once the payment is successfully processed, customers are redirected back to the merchant's website, where they can view the payment confirmation.

***

## Features of Plural Hosted Checkout

- Plural handles the entire checkout process on your website, allowing customers to select their preferred payment option through a ready-made payment page hosted on Plural's server.
- After submitting their payment details, customers are directed to the appropriate payment options page for further authentication.
- **Supported payment options**: [Cards](https://developer.pluralonline.com/v3.0/docs/cards), [UPI](https://developer.pluralonline.com/v3.0/docs/upi-unified-payments-interface), [PBP](https://developer.pluralonline.com/v3.0/docs/pay-by-points). (Net-banking Coming Soon)
- Merchants can customize their checkout experience by setting up their own branding, including brand colors and logos, which can be easily managed through the Plural dashboard.
- Integration is simple and quick, requiring minimal technical knowledge, making it easy for merchants to get started.

***

## Plural Hosted Checkout Screens

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7c0d192ecdcd068f4957342dc6ec44aaad1483b3ff0b5b9f6f8ba19295889557-image.png",
        null,
        "Cards as a payment method"
      ],
      "align": "center",
      "sizing": "400px",
      "border": true,
      "caption": "Cards as a payment method"
    }
  ]
}
[/block]


***

<br />

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/79cc8cd6401dfcb14664cfb9418de3d3261f63a36eac43e6edda597fbb1c324a-image.png",
        null,
        "UPI as a payment method"
      ],
      "align": "center",
      "sizing": "400px",
      "caption": "UPI as a payment method"
    }
  ]
}
[/block]


***

<br />

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a30fb3ccf11eda836371fbdd018213e9d3551f9175c8266b22d55ef8fa74ea30-image.png",
        null,
        "PBP as a payment method"
      ],
      "align": "center",
      "sizing": "400px",
      "caption": "PBP as a payment method"
    }
  ]
}
[/block]


<br />

2. <br />

> 📘 Important:
> 
> - With pre-authorization set to true, you can capture or cancel a payment for an order.

## 5. Capture Order

Use this API to capture the payment against an order. On successful capture of an order the order status is updated as `processed`.

Use the below endpoint to capture the payment against the order.

```text Capture Order Endpoint for UAT
PUT: https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/capture
```
```text Capture Order Endpoint for PROD
PUT: https://api.pluralpay.in/api/pay/v1/orders/{order_id}/capture
```

Shown below is a sample request and sample response for a Capture Order API.

```json Sample Request
{
  "merchant_capture_reference": "merchant-capture-ref-r4y"
}
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
            "created_at": "2024-07-19T11:13:21.523516426Z"
          }
        ],
        "created_at": "2024-07-19T11:11:48.944147Z",
        "updated_at": "2024-07-19T11:13:23.962461Z"
      }
    ],
    "created_at": "2024-07-19T11:11:48.944147Z",
    "updated_at": "2024-07-19T11:13:23.962461Z"
  }
}
```

Refer to our <a href="https://developer.pluralonline.com/v3.0/reference/orders-capture" target="_blank">Capture Order API</a> documentation to learn more.

## 6. Cancel Order

Use this API to cancel the payment against an order.

Use the below endpoint to cancel the payment against the order.

```text Cancel Order Endpoint for UAT
PuT: https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/cancel
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
        "created_at": "2024-07-19T11:27:55.664651Z",
        "updated_at": "2024-07-19T11:28:52.487287Z"
      }
    ],
    "created_at": "2024-07-19T11:27:55.664651Z",
    "updated_at": "2024-07-19T11:28:52.487287Z"
  }
}
```

Refer to our <a href="https://developer.pluralonline.com/v3.0/reference/orders-cancel" target="_blank">Cancel Order API documentation to learn more.
