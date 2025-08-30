---
title: "Available Events"
slug: "webhook-available-events"
excerpt: "Webhook events available on Plural."
hidden: false
createdAt: "Fri Sep 27 2024 08:51:59 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon May 19 2025 07:57:49 GMT+0000 (Coordinated Universal Time)"
---
The table below list the available webhook events on Plural with descriptions.

[block:parameters]
{
  "data": {
    "h-0": "Webhook",
    "h-1": "Description",
    "0-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#customer_activated\" >`CUSTOMER_ACTIVATED`</a>",
    "0-1": "When the customer is activated on Plural's platform.",
    "1-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#customer_deleted\" >`CUSTOMER_DELETED`</a>",
    "1-1": "When the customer is removed from Plural's system.",
    "2-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#customer_suspended\" >`CUSTOMER_SUSPENDED`</a>",
    "2-1": "When the customer is temporarily suspended on the Plural platform through the portal.",
    "3-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#customer_creation_failed\" >`CUSTOMER_CREATION_FAILED`</a>",
    "3-1": "When the customer creation is failed.",
    "4-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#order_authorized\" >`ORDER_AUTHORIZED`</a>",
    "4-1": "When the order is ready for authorization.",
    "5-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#order_processed\" >`ORDER_PROCESSED`</a>",
    "5-1": "When the payment is successfully received.",
    "6-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#order_cancelled\" >`ORDER_CANCELLED`</a>",
    "6-1": "When the order is cancelled.",
    "7-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#payment_failed\" >`PAYMENT_FAILED`</a>",
    "7-1": "When the payment against an order get failed.",
    "8-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#order_failed\" >`ORDER_FAILED`</a>",
    "8-1": "When the order is failed.",
    "9-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#refund_processed\" >`REFUND_PROCESSED`</a>",
    "9-1": "When the refund is successful.",
    "10-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#refund_failed\" >`REFUND_FAILED`</a>",
    "10-1": "When the refund against an order get failed.",
    "11-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#token_activated\" >`TOKEN_ACTIVATED`</a>",
    "11-1": "When the token is activated via the network.",
    "12-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#token_deactivated\" >`TOKEN_DEACTIVATED`</a>",
    "12-1": "When the token is deactivated.",
    "13-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#token_suspended\" >`TOKEN_SUSPENDED`</a>",
    "13-1": "When the token is suspended.",
    "14-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#token_provision_failed\" >`TOKEN_PROVISION_FAILED`</a>",
    "14-1": "When the token provisioning is failed.",
    "15-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#subscription_activated\" >`SUBSCRIPTION_ACTIVATED`</a>",
    "15-1": "When the subscription is activated.",
    "16-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#subscription_pending\" >`SUBSCRIPTION_PENDING`</a>",
    "16-1": "When the subscription is pending.",
    "17-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#subscription_paused\" >`SUBSCRIPTION_PAUSED`</a>",
    "17-1": "When the subscription is paused.",
    "18-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#subscription_resumed\" >`SUBSCRIPTION_RESUMED`</a>",
    "18-1": "When the subscription is resumed.",
    "19-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#subscription_completed\" >`SUBSCRIPTION_COMPLETED`</a>",
    "19-1": "When the subscription is completed.",
    "20-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#subscription_charged\" >`SUBSCRIPTION_CHARGED`</a>",
    "20-1": "When the successful charge is made on the subscription.",
    "21-0": "<a href=\"https://developer.pluralonline.com/docs/webhook-available-events#subscription_halted\" >`SUBSCRIPTION_HALTED`</a>",
    "21-1": "When all retries have been exhausted and the subscription moves from the `PENDING `state to the `Halted `state."
  },
  "cols": 2,
  "rows": 22,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Sample Payload

### CUSTOMER_ACTIVATED

Triggered when the customer is activated at Plural's end. Shown below is the sample payload returned for customer activation scenario.

```json Customer Activated
{
  "event_type": "CUSTOMER_ACTIVATED",
  "data": {
    "customer": {
      "customer_id": "cust-v1-0811030624-aa-RBDgpR",
      "merchant_customer_reference": "12345ABC",
      "first_name": "Kevin",
      "last_name": "Bob",
      "country_code": "91",
      "mobile_number": "9876543210",
      "email_id": "kevin.bob@example.com",
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
      "gstin": "27ABCDE1234F2Z5",
      "merchant_metadata": {
        "key1": "XX",
        "key2": "DOF"
      },
      "status": "ACTIVE",
      "created_at": "2024-10-04T13:11:29.645591Z",
      "updated_at": "2024-10-04T13:11:29.645657Z"
    }
  }
}
```

### CUSTOMER_DELETED

Triggered when the customer is deleted at the Plural end. Shown below is the sample payload returned for Customer Deleted event.

```json Customer Deleted
{
  "event_type": "CUSTOMER_DELETED",
  "data": {
    "customer": {
      "customer_id": "cust-v1-0811030624-aa-RBDgpR",
      "merchant_customer_reference": "12345ABC",
      "first_name": "Kevin",
      "last_name": "Bob",
      "country_code": "91",
      "mobile_number": "9876543210",
      "email_id": "kevin.bob@example.com",
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
      "gstin": "27ABCDE1234F2Z5",
      "merchant_metadata": {
        "key1": "XX",
        "key2": "DOF"
      },
      "status": "DELETED",
      "status_reason": "customer deleted via plural customer dashboard",
      "created_at": "2024-10-04T13:11:29.645591Z",
      "updated_at": "2024-10-04T13:11:29.645657Z"
    }
  }
}
```

### CUSTOMER_SUSPENDED

Triggered when the customer is temporarily suspended at Plural’s end via the portal. Shown below is the sample payload returned for Customer Suspended event.

```json Customer Suspended
{
  "event_type": "CUSTOMER_SUSPENDED",
  "data": {
    "customer": {
      "customer_id": "cust-v1-0811030624-aa-RBDgpR",
      "merchant_customer_reference": "12345ABC",
      "first_name": "Kevin",
      "last_name": "Bob",
      "country_code": "91",
      "mobile_number": "9876543210",
      "email_id": "kevin.bob@example.com",
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
      "gstin": "27ABCDE1234F2Z5",
      "merchant_metadata": {
        "key1": "XX",
        "key2": "DOF"
      },
      "status": "SUSPENDED",
      "status_reason": "customer suspended",
      "created_at": "2024-10-04T13:11:29.645591Z",
      "updated_at": "2024-10-04T13:11:29.645657Z"
    }
  }
}
```

### CUSTOMER_CREATION_FAILED

Triggered when customer creation fails. Shown below is the sample payload returned for Customer Creation Failure scenarios.

```json Customer Creation Failed
{
  "event_type": "CUSTOMER_CREATION_FAILED",
  "data": {
    "customer": {
      "customer_id": "cust-v1-0811030624-aa-RBDgpR",
      "merchant_customer_reference": "12345ABC",
      "first_name": "Kevin",
      "last_name": "Bob",
      "country_code": "91",
      "mobile_number": "9876543210",
      "email_id": "kevin.bob@example.com",
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
      "gstin": "27ABCDE1234F2Z5",
      "merchant_metadata": {
        "key1": "XX",
        "key2": "DOF"
      },
      "status": "FAILED",
      "status_reason": "invalid_data",
      "failure_reason": {
        "code": "INVALID_REQUEST",
        "message": "Request is not well-formed, syntactically incorrect, or violates schema",
        "additional_error_details": {
          "source": "internal",
          "step": "creation",
          "reason": "invalid_data",
          "metadata": {}
        }
      },
      "created_at": "2024-10-04T13:11:29.645591Z",
      "updated_at": "2024-10-04T13:11:29.645657Z"
    }
  }
}
```

### ORDER_AUTHORIZED

Triggered when the order is ready for authorization. Shown below are the sample payloads returned against different payment method.

```json Card Payload
{
  "event_type": "ORDER_AUTHORIZED",
  "data": {
    "order_id": "v1-240828181232-aa-7cGcgo",
    "merchant_order_reference": "8e9b80ea-49c3-4d3e-860b-057890d2fd73",
    "type": "CHARGE",
    "status": "AUTHORIZED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "109500",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": true,    
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
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
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-240828181232-aa-7cGcgo-cc-h",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "AUTHORIZED",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "NONE",
            "product_name": "",
            "card_category": "CONSUMER",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "831000",
          "acquirer_reference": "7248687871426329503954",
          "rrn": "424118053313",
          "is_aggregator": true
        },
        "created_at": "2024-08-28T18:12:32.152Z",
        "updated_at": "2024-08-28T18:13:08.418Z"
      }
    ],
    "created_at": "2024-08-28T18:12:32.152Z",
    "updated_at": "2024-08-28T18:13:08.418Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Tokenized Card Payload
{
  "event_type": "ORDER_AUTHORIZED",
  "data": {
    "order_id": "v1-240828181232-aa-7cGcgo",
    "merchant_order_reference": "8e9b80ea-49c3-4d3e-860b-057890d2fd73",
    "type": "CHARGE",
    "status": "AUTHORIZED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "109500",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": true,    
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
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
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-240828181232-aa-7cGcgo-cc-h",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "AUTHORIZED",
        "payment_amount": {
          "value": 100,
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
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "831000",
          "acquirer_reference": "7248687871426329503954",
          "rrn": "424118053313",
          "is_aggregator": true
        },
        "created_at": "2024-08-28T18:12:32.152Z",
        "updated_at": "2024-08-28T18:13:08.418Z"
      }
    ],
    "created_at": "2024-08-28T18:12:32.152Z",
    "updated_at": "2024-08-28T18:13:08.418Z",
    "integration_mode": "SEAMLESS"
  }
} }
}
```
```json Pay by Points
{
  "eventType": "ORDER_AUTHORIZED",
  "data": {
    "orderId": "v1-240813114804-aa-tgiDMn",
    "merchantOrderReference": "bf53f2c1-0334-43fc-9ca1-3a6f8a2cc35a",
    "type": "CHARGE",
    "status": "AUTHORIZED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchantId": "109968",
    "orderAmount": {
      "value": 200,
      "currency": "INR"
    },
    "notes": "order1",
    "preAuth": true,
    "purchaseDetails": {
      "customer": {
        "emailId": "john.doe@gmail.com",
        "firstName": "John",
        "lastName": "Doe",
        "customerId": "192212",
        "mobileNumber": "192192883",
        "billingAddress": {
          "address1": "H.No 15, Sector 17",
          "address2": "",
          "address3": "",
          "pincode": "61232112",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        },
        "shippingAddress": {
          "address1": "H.No 15, Sector 17",
          "address2": "string",
          "address3": "string",
          "pincode": "144001123",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        }
      },
      "merchantMetadata": {}
    },
    "payments": [
      {
        "id": "v1-240813114804-aa-tgiDMn-cc-W",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "AUTHORIZED",
        "paymentAmount": {
          "value": 100,
          "currency": "INR"
        },
        "paymentMethod": "CARD",
        "paymentOption": {
          "cardData": {
            "cardType": "CREDIT",
            "networkName": "VISA",
            "issuerName": "NONE",
            "productName": "",
            "cardCategory": "CONSUMER",
            "countryCode": "IND"
          }
        },
        "captureData": []
      },
      {
        "id": "v1-240813114804-aa-tgiDMn-pt-9",
        "status": "AUTHORIZED",
        "paymentAmount": {
          "value": 100,
          "currency": "INR"
        },
        "paymentMethod": "POINTS",
        "paymentOption": {
          "cardData": {
            "cardType": "",
            "networkName": "",
            "issuerName": "",
            "productName": "",
            "cardCategory": "",
            "countryCode": ""
          }
        },
        "captureData": []
      }
    ],
    "createdAt": "2024-08-28T18:12:32.152Z",
    "updatedAt": "2024-08-28T18:13:32.252Z",
    "integration_mode": "SEAMLESS"
  }
}
```

### ORDER_PROCESSED

Triggered when the payment is successfully received. Shown below are the sample payloads returned against different payment method.

```json Card Payload with Pre-authorization True
{
  "event_type": "ORDER_PROCESSED",
  "data": {
    "order_id": "v1-240909084141-aa-O2oJwd",
    "merchant_order_reference": "a51688bd-34bb-4714-b40d-5fbbf381ba87",
    "type": "CHARGE",
    "status": "PROCESSED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "109500",
    "order_amount": {
      "value": 200,
      "currency": "INR"
    },
    "pre_auth": true,    
    "notes": "order1",
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
      }
    },
    "payments": [
      {
        "id": "v1-240909084141-aa-O2oJwd-cc-N",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 200,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "NONE",
            "product_name": "",
            "card_category": "CONSUMER",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "831000",
          "acquirer_reference": "7258713154996001403955",
          "rrn": "425308234545",
          "is_aggregator": true
        },
        "capture_data": [
          {
            "merchant_capture_reference": "2a2ef9cd-6edd-4df0-8c26-d2e81249ac4d",
            "capture_amount": {
              "value": 200,
              "currency": "INR"
            },
            "created_at": "2024-09-09T08:50:41.082Z"
          }
        ],
        "created_at": "2024-08-28T18:12:32.152Z",
        "updated_at": "2024-08-28T18:13:08.418Z"
      }
    ],
    "created_at": "2024-09-09T08:41:41.026Z",
    "updated_at": "2024-09-09T08:50:41.082Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Tokenized Card Payload
{
  "event_type": "ORDER_PROCESSED",
  "data": {
    "order_id": "v1-240909084141-aa-O2oJwd",
    "merchant_order_reference": "a51688bd-34bb-4714-b40d-5fbbf381ba87",
    "type": "CHARGE",
    "status": "PROCESSED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "109500",
    "order_amount": {
      "value": 200,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
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
      }
    },
    "payments": [
      {
        "id": "v1-240909084141-aa-O2oJwd-cc-N",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 200,
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
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "831000",
          "acquirer_reference": "7258713154996001403955",
          "rrn": "425308234545",
          "is_aggregator": true
        },
        "capture_data": [
          {
            "merchant_capture_reference": "2a2ef9cd-6edd-4df0-8c26-d2e81249ac4d",
            "capture_amount": {
              "value": 200,
              "currency": "INR"
            },
            "created_at": "2024-09-09T08:50:41.082Z"
          }
        ],
        "created_at": "2024-08-28T18:12:32.152Z",
        "updated_at": "2024-08-28T18:13:08.418Z"
      }
    ],
    "created_at": "2024-09-09T08:41:41.026Z",
    "updated_at": "2024-09-09T08:50:41.082Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Purchase Card Payload
{
  "event_type": "ORDER_PROCESSED",
  "data": {
    "order_id": "v1-240909084141-aa-O2oJwd",
    "merchant_order_reference": "a51688bd-34bb-4714-b40d-5fbbf381ba87",
    "type": "CHARGE",
    "status": "PROCESSED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "109500",
    "order_amount": {
      "value": 200,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
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
      }
    },
    "payments": [
      {
        "id": "v1-240909084141-aa-O2oJwd-cc-N",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 200,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "NONE",
            "product_name": "",
            "card_category": "CONSUMER",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "831000",
          "acquirer_reference": "7258713154996001403955",
          "rrn": "425308234545",
          "is_aggregator": true
        },
        "created_at": "2024-08-28T18:12:32.152Z",
        "updated_at": "2024-08-28T18:13:08.418Z"
      }
    ],
    "created_at": "2024-09-09T08:41:41.026Z",
    "updated_at": "2024-09-09T08:50:41.082Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Partially Capture Payload
{
  "event_type": "ORDER_PROCESSED",
  "data": {
    "order_id": "v1-241011063254-aa-eAX0xI",
    "merchant_order_reference": "c1cab20c-eace-4f53-8201-87bc8bc208b1",
    "type": "CHARGE",
    "status": "PARTIALLY_CAPTURED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "108272",
    "order_amount": {
      "value": 2000,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
    "payments": [
      {
        "id": "v1-241011063254-aa-eAX0xI-cc-r",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 2000,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "DEBIT",
            "network_name": "VISA",
            "issuer_name": "VISA PRODUCTION SUPPORT CLIENT BID 1",
            "card_category": "Commercial",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "831000",
          "acquirer_reference": "7286284540236614603955",
          "rrn": "428406565162",
          "is_aggregator": true
        },
        "capture_data": [
          {
            "merchant_capture_reference": "242c60f7-4068-4fc3-ab93-4ab92afea129",
            "capture_amount": {
              "value": 1200,
              "currency": "INR"
            },
            "created_at": "2024-10-11T06:34:12.366Z"
          }
        ],
        "created_at": "2024-10-11T06:33:00.321Z",
        "updated_at": "2024-10-11T06:34:14.583Z"
      }
    ],
    "created_at": "2024-10-11T06:32:54.188Z",
    "updated_at": "2024-10-11T06:34:14.584Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Pay by Points
{
  "eventType": "ORDER_PROCESSED",
  "data": {
    "orderId": "v1-240813114804-aa-tgiDMn",
    "merchantOrderReference": "bf53f2c1-0334-43fc-9ca1-3a6f8a2cc35a",
    "type": "CHARGE",
    "status": "PROCESSED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchantId": "109968",
    "orderAmount": {
      "value": 200,
      "currency": "INR"
    },
    "notes": "order1",
    "preAuth": false,
    "purchaseDetails": {
      "customer": {
        "emailId": "john.doe@gmail.com",
        "firstName": "John",
        "lastName": "Doe",
        "customerId": "192212",
        "mobileNumber": "192192883",
        "billingAddress": {
          "address1": "H.No 15, Sector 17",
          "address2": "",
          "address3": "",
          "pincode": "61232112",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        },
        "shippingAddress": {
          "address1": "H.No 15, Sector 17",
          "address2": "string",
          "address3": "string",
          "pincode": "144001123",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        }
      },
      "merchantMetadata": {}
    },
    "payments": [
      {
        "id": "v1-240813114804-aa-tgiDMn-cc-W",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "paymentAmount": {
          "value": 100,
          "currency": "INR"
        },
        "paymentMethod": "CARD",
        "paymentOption": {
          "cardData": {
            "cardType": "CREDIT",
            "networkName": "VISA",
            "issuerName": "NONE",
            "productName": "",
            "cardCategory": "CONSUMER",
            "countryCode": "IND"
          }
        },
        "captureData": [
          {
            "merchantCaptureReference": "138e4a3f-1792-4f79-8f87-862b47231fd2",
            "captureAmount": {
              "value": 100,
              "currency": "INR"
            },
            "createdAt": "2024-08-28T18:12:32.152Z"
          }
        ]
      },
      {
        "id": "v1-240813114804-aa-tgiDMn-pt-9",
        "status": "PROCESSED",
        "paymentAmount": {
          "value": 100,
          "currency": "INR"
        },
        "paymentMethod": "POINTS",
        "paymentOption": {
          "cardData": {
            "cardType": "",
            "networkName": "",
            "issuerName": "",
            "productName": "",
            "cardCategory": "",
            "countryCode": ""
          }
        },
        "captureData": [
          {
            "merchantCaptureReference": "138e4a3f-1792-4f79-8f87-862b47231fd2",
            "captureAmount": {
              "value": 100,
              "currency": "INR"
            },
            "createdAt": "2024-08-28T18:12:32.152Z"
          }
        ]
      }
    ],
    "createdAt": "2024-08-28T18:12:32.152Z",
    "updatedAt": "2024-08-28T18:13:32.252Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json UPI Intent Payload
{
  "event_type": "ORDER_PROCESSED",
  "data": {
    "order_id": "v1-240912090202-aa-LAKYlA",
    "merchant_order_reference": "6c59c3e2-3cc8-4207-bdf5-49b976cb8077",
    "type": "CHARGE",
    "status": "PROCESSED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "110047",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
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
        "id": "v1-240912090202-aa-LAKYlA-up-s",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "UPI",
        "payment_option": {
          "upi_data": {
            "txn_mode": "INTENT",
            "payee": {
              "reference_id": "174425",
              "reference_type": "MERCHANT",
              "vpa": "pinelabs.24092@hdfcbank",
              "acquirer_name": "HDFC"
            },
            "payer": {
              "vpa": "saklania8-2@okicici",
              "phone_number": "918979279800",
              "account_type": "SAVINGS"
            }
          }
        },
        "acquirer_data": {
          "approval_code": "00",
          "acquirer_reference": "462274903205",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2024-09-12T09:02:02.024Z",
        "updated_at": "2024-09-12T09:04:41.960Z"
      }
    ],
    "created_at": "2024-09-12T09:02:02.024Z",
    "updated_at": "2024-09-12T09:04:41.960Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Netbanking Payload
{
  "event_type": "ORDER_PROCESSED",
  "data": {
    "order_id": "v1-241108070043-aa-Sys3RJ",
    "merchant_order_reference": "3ebf9a69-ac36-4a66-9f35-01f339c4486c",
    "type": "CHARGE",
    "status": "PROCESSED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "110553",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
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
        "id": "v1-241108070043-aa-Sys3RJ-nb-7",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "NETBANKING",
        "acquirer_data": {
          "approval_code": "0300",
          "acquirer_reference": "USBI0001265269",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2024-11-08T07:00:54.043Z",
        "updated_at": "2024-11-08T07:01:51.687Z"
      }
    ],
    "created_at": "2024-11-08T07:00:43.756Z",
    "updated_at": "2024-11-08T07:01:51.687Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Dynamic Currency Conversion Payment
{
  "event_type": "ORDER_PROCESSED",
  "data": {
    "order_id": "v1-240909084141-aa-O2oJwd",
    "merchant_order_reference": "a51688bd-34bb-4714-b40d-5fbbf381ba87",
    "type": "CHARGE",
    "status": "PROCESSED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "109500",
    "order_amount": {
      "value": 10000,
      "currency": "INR"
    },
    "pre_auth": false,
    "allowed_payment_methods": [],    
    "notes": "order1",
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
      }
    },
    "payments": [
      {
        "id": "v1-240909084141-aa-O2oJwd-cc-N",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 123,
          "currency": "USD"
        },
        "base_amount": {
         "value": 10000,
         "currency": "INR"
        },
        "conversion_rate": 0.0123,
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "NONE",
            "product_name": "",
            "card_category": "CONSUMER",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "831000",
          "acquirer_reference": "7258713154996001403955",
          "rrn": "425308234545",
          "is_aggregator": true
        },
        "created_at": "2024-08-28T18:12:32.152Z",
        "updated_at": "2024-08-28T18:13:08.418Z"
      }
    ],
    "created_at": "2024-09-09T08:41:41.026Z",
    "updated_at": "2024-09-09T08:50:41.082Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Credit EMI
{
  "event_type": "ORDER_PROCESSED",
  "data": {
    "order_id": "v1-250414093519-aa-0ySFy5",
    "merchant_order_reference": "39b6b551-320d-4935-bb71-a337e83898f4",
    "type": "CHARGE",
    "status": "PROCESSED",
    "merchant_id": "111077",
    "order_amount": {
      "value": 2100000,
      "currency": "INR"
    },
    "pre_auth": false,
    "allowed_payment_methods": [
      "CARD",
      "NETBANKING",
      "CREDIT_EMI",
      "UPI",
      "DEBIT_EMI",
      "CARDLESS_EMI",
      "POINTS"
    ],
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "cust-v1-250414071055-aa-lj5Omz",
        "mobile_number": "9876543210",
        "country_code": "91",
        "billing_address": {
          "address1": "H.No 15, Sector 17",
          "pincode": "61232112",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        },
        "shipping_address": {
          "address1": "H.No 15, Sector 17",
          "pincode": "160036",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        },
        "is_edit_customer_details_allowed": false
      }
    },
    "payments": [
      {
        "id": "v1-250414093519-aa-0ySFy5-ce-a",
        "merchant_payment_reference": "b67211ae-7190-4b84-8787-5036a5515e84",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 1800000,
          "currency": "INR"
        },
        "payment_method": "CREDIT_EMI",
        "payment_option": {},
        "acquirer_data": {
          "approval_code": "831000",
          "acquirer_reference": "7446233403796371303002",
          "rrn": "710409149533",
          "is_aggregator": true
        },
        "offer_data": {
          "offer_details": {
            "id": "6",
            "name": "HDFC CC",
            "issuer_type": "CC_BANK",
            "priority": 1,
            "tenure": {
              "tenure_id": "7",
              "name": "No EMI Only Cashback",
              "tenure_type": "MONTH",
              "tenure_value": 0,
              "issuer_offer_parameters": [
                {
                  "program_type": "BRAND_EMI",
                  "offer_id": "3722",
                  "offer_parameter_id": "204140"
                }
              ],
              "details": [
                {
                  "product_code": "Apple_test_1",
                  "product_display_name": "",
                  "brand_id": "1",
                  "brand_name": "Apple",
                  "product_offer_parameters": [
                    {
                      "program_type": "BRAND_OFFER",
                      "offer_id": "3722",
                      "offer_parameter_id": "204140"
                    }
                  ],
                  "product_amount": {
                    "currency": "INR",
                    "value": 2100000
                  },
                  "interest_rate": 0,
                  "discount": {
                    "discount_type": "INSTANT",
                    "percentage": 0,
                    "amount": {
                      "currency": "INR",
                      "value": 300000
                    },
                    "discount_deferred_duration_value": 0,
                    "breakup": {
                      "merchant": {}
                    }
                  },
                  "product_imei": ""
                }
              ],
              "discount": {
                "discount_type": "INSTANT",
                "percentage": 0,
                "amount": {
                  "currency": "INR",
                  "value": 300000
                },
                "discount_deferred_duration_value": 0,
                "breakup": {
                  "merchant": {}
                }
              },
              "loan_amount": {
                "currency": "INR",
                "value": 1800000
              },
              "total_discount_amount": {
                "currency": "INR",
                "value": 300000
              },
              "net_payment_amount": {
                "currency": "INR",
                "value": 1800000
              },
              "monthly_emi_amount": {
                "currency": "INR",
                "value": 1800000
              },
              "total_emi_amount": {
                "currency": "INR",
                "value": 1800000
              },
              "split_emi_percentage": 0,
              "interest_rate_percentage": 0,
              "dealer_charges_percentage": 0,
              "emi_type": "STANDARD"
            }
          }
        },
        "created_at": "2025-04-14T09:35:27.420Z",
        "updated_at": "2025-04-14T09:35:43.223Z"
      }
    ],
    "refunds": [],
    "created_at": "2025-04-14T09:35:19.742Z",
    "updated_at": "2025-04-14T09:35:43.223Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```Text Split Settlement
{
  "event_type": "ORDER_PROCESSED",
  "data": {
    "order_id": "v1-250515094053-aa-oXnK19",
    "merchant_order_reference": "1d600467-7ce2-4c15-884e-87a32d4a17d5",
    "type": "CHARGE",
    "status": "PROCESSED",
    "merchant_id": "111302",
    "order_amount": {
      "value": 21000,
      "currency": "INR"
    },
    "pre_auth": false,
    "allowed_payment_methods": [
      "CARD",
      "NETBANKING",
      "UPI"
    ],
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
            "split_merchant_id": "111302",
            "split_settlement_id": "v1-250515094053-aa-oXnK19-ss-f",
            "amount": {
              "value": 10000,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-15T09:40:53.878Z"
          },
          {
            "split_merchant_id": "111302",
            "split_settlement_id": "v1-250515094053-aa-oXnK19-ss-g",
            "amount": {
              "value": 2000,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-15T09:40:53.878Z"
          },
          {
            "split_merchant_id": "111302",
            "split_settlement_id": "v1-250515094053-aa-oXnK19-ss-h",
            "amount": {
              "value": 8000,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-15T09:40:53.878Z"
          },
          {
            "split_merchant_id": "111302",
            "split_settlement_id": "v1-250515094053-aa-oXnK19-ss-i",
            "amount": {
              "value": 500,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-15T09:40:53.878Z"
          },
          {
            "split_merchant_id": "111302",
            "split_settlement_id": "v1-250515094053-aa-oXnK19-ss-j",
            "amount": {
              "value": 500,
              "currency": "INR"
            },
            "on_hold": false,
            "status": "RELEASED",
            "updated_at": "2025-05-15T09:40:53.878Z"
          }
        ]
      }
    },
    "payments": [
      {
        "id": "v1-250515094053-aa-oXnK19-cc-a",
        "merchant_payment_reference": "832f9d6a-c9d9-4707-9ae5-e02bfce18bdb",
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
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN",
            "last4_digit": "1091",
            "save": false
          }
        },
        "acquirer_data": {
          "approval_code": "831000",
          "acquirer_reference": "7473021240916837003813",
          "rrn": "513509578842",
          "is_aggregator": true
        },
        "created_at": "2025-05-15T09:41:44.421Z",
        "updated_at": "2025-05-15T09:42:05.112Z"
      }
    ],
    "refunds": [],
    "created_at": "2025-05-15T09:40:53.878Z",
    "updated_at": "2025-05-15T09:42:05.112Z",
    "integration_mode": "SEAMLESS"
  }
}
```

### ORDER_CANCELLED

Triggered when the order is cancelled. Shown below are the sample payloads returned against different payment method.

```json Card Payload
{
  "event_type": "ORDER_CANCELLED",
  "data": {
    "order_id": "v1-240828181232-aa-7cGcgo",
    "merchant_order_reference": "8e9b80ea-49c3-4d3e-860b-057890d2fd73",
    "type": "CHARGE",
    "status": "CANCELLED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "109500",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
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
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-240828181232-aa-7cGcgo-cc-h",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "CANCELLED",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "NONE",
            "product_name": "",
            "card_category": "CONSUMER",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "831000",
          "acquirer_reference": "7248688579796775203955",
          "rrn": "424118053313",
          "is_aggregator": true
        },
        "created_at": "2024-08-28T18:12:32.152Z",
        "updated_at": "2024-08-28T18:14:18.965Z"
      }
    ],
    "created_at": "2024-08-28T18:12:32.152Z",
    "updated_at": "2024-08-28T18:14:18.965Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Tokenized Card Payload
{
  "event_type": "ORDER_CANCELLED",
  "data": {
    "order_id": "v1-240828181232-aa-7cGcgo",
    "merchant_order_reference": "8e9b80ea-49c3-4d3e-860b-057890d2fd73",
    "type": "CHARGE",
    "status": "CANCELLED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "109500",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
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
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-240828181232-aa-7cGcgo-cc-h",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "CANCELLED",
        "payment_amount": {
          "value": 100,
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
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "831000",
          "acquirer_reference": "7248688579796775203955",
          "rrn": "424118053313",
          "is_aggregator": true
        },
        "created_at": "2024-08-28T18:12:32.152Z",
        "updated_at": "2024-08-28T18:14:18.965Z"
      }
    ],
    "created_at": "2024-08-28T18:12:32.152Z",
    "updated_at": "2024-08-28T18:14:18.965Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Pay by Points
{
  "eventType": "ORDER_CANCELLED",
  "data": {
    "orderId": "v1-240813104001-aa-NV193P",
    "merchantOrderReference": "merchant-reference-42",
    "type": "CHARGE",
    "status": "CANCELLED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchantId": "109968",
    "orderAmount": {
      "value": 1000,
      "currency": "INR"
    },
    "notes": "order1",
    "preAuth": false,
    "purchaseDetails": {
      "customer": {
        "emailId": "john.doe@gmail.com",
        "firstName": "John",
        "lastName": "Doe",
        "customerId": "192212",
        "mobileNumber": "192192883",
        "billingAddress": {
          "address1": "H.No 15, Sector 17",
          "address2": "",
          "address3": "",
          "pincode": "61232112",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        },
        "shippingAddress": {
          "address1": "H.No 15, Sector 17",
          "address2": "string",
          "address3": "string",
          "pincode": "144001123",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        }
      },
      "merchantMetadata": {}
    },
    "payments": [
      {
        "id": "v1-240813104001-aa-NV193P-cc-9",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "paymentAmount": {
          "value": 500,
          "currency": "INR"
        },
        "paymentMethod": "CARD",
        "paymentOption": {
          "cardData": {
            "cardType": "CREDIT",
            "networkName": "VISA",
            "issuerName": "NONE",
            "productName": "",
            "cardCategory": "CONSUMER",
            "countryCode": "IND"
          }
        },
        "captureData": []
      },
      {
        "id": "v1-240813104001-aa-NV193P-pt-S",
        "status": "PROCESSED",
        "paymentAmount": {
          "value": 500,
          "currency": "INR"
        },
        "paymentMethod": "POINTS",
        "paymentOption": {
          "cardData": {
            "cardType": "",
            "networkName": "",
            "issuerName": "",
            "productName": "",
            "cardCategory": "",
            "countryCode": ""
          }
        },
        "captureData": []
      }
    ],
    "createdAt": "2024-08-28T18:12:32.152Z",
    "updatedAt": "2024-08-28T18:13:32.252Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Split Settlement
{
  "event_type": "ORDER_CANCELLED",
  "data": {
    "order_id": "v1-250515102814-aa-FP1ezF",
    "merchant_order_reference": "8cb7f1ad-c150-4c5c-92ff-0e83e51fcc7c",
    "type": "CHARGE",
    "status": "CANCELLED",
    "merchant_id": "111302",
    "order_amount": {
      "value": 21000,
      "currency": "INR"
    },
    "pre_auth": false,
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
            "split_merchant_id": "111302",
            "split_settlement_id": "v1-250515102814-aa-FP1ezF-ss-f",
            "amount": {
              "value": 10000,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-15T10:28:14.477Z"
          },
          {
            "split_merchant_id": "111302",
            "split_settlement_id": "v1-250515102814-aa-FP1ezF-ss-g",
            "amount": {
              "value": 2000,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-15T10:28:14.477Z"
          },
          {
            "split_merchant_id": "111302",
            "split_settlement_id": "v1-250515102814-aa-FP1ezF-ss-h",
            "amount": {
              "value": 8000,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-15T10:28:14.477Z"
          },
          {
            "split_merchant_id": "111302",
            "split_settlement_id": "v1-250515102814-aa-FP1ezF-ss-i",
            "amount": {
              "value": 500,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-15T10:28:14.477Z"
          },
          {
            "split_merchant_id": "111302",
            "split_settlement_id": "v1-250515102814-aa-FP1ezF-ss-j",
            "amount": {
              "value": 500,
              "currency": "INR"
            },
            "on_hold": false,
            "status": "RELEASED",
            "updated_at": "2025-05-15T10:28:14.477Z"
          }
        ]
      }
    },
    "payments": [],
    "refunds": [],
    "created_at": "2025-05-15T10:28:14.477Z",
    "updated_at": "2025-05-15T10:28:45.137Z",
    "integration_mode": "SEAMLESS"
  }
}
```

### PAYMENT_FAILED

Triggered when the payment against an order gets failed. Shown below are the sample payloads returned against different payment method.

```json Capture Failure Payload
{
  "event_type": "PAYMENT_FAILED",
  "data": {
    "order_id": "v1-240828180835-aa-IKvddb",
    "merchant_order_reference": "4de00e1f-4855-4454-bf50-c0f7dd680e27",
    "type": "CHARGE",
    "status": "FAILED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "109500",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": true,    
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
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
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-240828180835-aa-IKvddb-cc-2",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "FAILED",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "NONE",
            "product_name": "",
            "card_category": "CONSUMER",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "7248685878696292803954",
          "rrn": "",
          "is_aggregator": true
        },
        "error_detail": {
          "code": "PAYMENT_DECLINED",
          "message": "Transaction declined by Acquirer due to unknown reason"
        },
        "created_at": "2024-08-28T18:08:35.651Z",
        "updated_at": "2024-08-28T18:10:15.584Z"
      }
    ],
    "created_at": "2024-08-28T18:08:35.651Z",
    "updated_at": "2024-08-28T18:10:15.584Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Card OTP Failure
{
  "event_type": "PAYMENT_FAILED",
  "data": {
    "order_id": "v1-240828180835-aa-IKvddb",
    "merchant_order_reference": "4de00e1f-4855-4454-bf50-c0f7dd680e27",
    "type": "CHARGE",
    "status": "ATTEMPTED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "109500",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
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
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-240828180835-aa-IKvddb-cc-2",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "FAILED",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "NONE",
            "product_name": "",
            "card_category": "CONSUMER",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "7248685878696292803954",
          "rrn": "",
          "is_aggregator": true
        },
        "error_detail": {
          "code": "USER_AUTHENTICATION_FAILED",
          "message": "Consumer Authentication failed"
        },
        "created_at": "2024-08-28T18:08:35.651Z",
        "updated_at": "2024-08-28T18:10:15.584Z"
      }
    ],
    "created_at": "2024-08-28T18:08:35.651Z",
    "updated_at": "2024-08-28T18:10:15.584Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Tokenized Card Payload
{
  "event_type": "PAYMENT_FAILED",
  "data": {
    "order_id": "v1-240828180835-aa-IKvddb",
    "merchant_order_reference": "4de00e1f-4855-4454-bf50-c0f7dd680e27",
    "type": "CHARGE",
    "status": "ATTEMPTED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "109500",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": true,    
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
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
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-240828180835-aa-IKvddb-cc-2",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "FAILED",
        "payment_amount": {
          "value": 100,
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
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "7248685878696292803954",
          "rrn": "",
          "is_aggregator": true
        },
        "error_detail": {
          "code": "PAYMENT_DECLINED",
          "message": "Transaction declined by Acquirer due to unknown reason"
        },
        "created_at": "2024-08-28T18:08:35.651Z",
        "updated_at": "2024-08-28T18:10:15.584Z"
      }
    ],
    "created_at": "2024-08-28T18:08:35.651Z",
    "updated_at": "2024-08-28T18:10:15.584Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Pay by Points
{
  "eventType": "PAYMENT_FAILED",
  "data": {
    "orderId": "v1-240816104837-aa-ewN96Q",
    "merchantOrderReference": "merchant-reference-49",
    "type": "CHARGE",
    "status": "ATTEMPTED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchantId": "109968",
    "orderAmount": {
      "value": 10000,
      "currency": "INR"
    },   
    "notes": "order1",
    "preAuth": false,
    "purchaseDetails": {
      "customer": {
        "emailId": "john.doe@gmail.com",
        "firstName": "John",
        "lastName": "Doe",
        "customerId": "192212",
        "mobileNumber": "192192883",
        "billingAddress": {
          "address1": "H.No 15, Sector 17",
          "address2": "",
          "address3": "",
          "pincode": "61232112",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        },
        "shippingAddress": {
          "address1": "H.No 15, Sector 17",
          "address2": "string",
          "address3": "string",
          "pincode": "144001123",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        }
      },
      "merchantMetadata": {}
    },
    "payments": [
      {
        "id": "v1-240816104837-aa-ewN96Q-cc-O",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "FAILED",
        "paymentAmount": {
          "value": 5000,
          "currency": "INR"
        },
        "paymentMethod": "CARD",
        "paymentOption": {
          "cardData": {
            "cardType": "CREDIT",
            "networkName": "VISA",
            "issuerName": "NONE",
            "productName": "",
            "cardCategory": "CONSUMER",
            "countryCode": "IND"
          }
        }
      },
      {
        "id": "v1-240816104837-aa-ewN96Q-pt-3",
        "status": "FAILED",
        "paymentAmount": {
          "value": 5000,
          "currency": "INR"
        },
        "paymentMethod": "POINTS",
        "paymentOption": {
          "cardData": {
            "cardType": "",
            "networkName": "",
            "issuerName": "",
            "productName": "",
            "cardCategory": "",
            "countryCode": ""
          }
        },
        "captureData": []
      }
    ],
    "createdAt": "2024-08-28T18:12:32.152Z",
    "updatedAt": "2024-08-28T18:13:32.252Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json UPI Collect Payload
{
  "event_type": "PAYMENT_FAILED",
  "data": {
    "order_id": "v1-240912102222-aa-lZedaQ",
    "merchant_order_reference": "99a6329d-031a-4c94-acd9-4c1682b1933e",
    "type": "CHARGE",
    "status": "ATTEMPTED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "110047",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "notes": "some order",
    "pre_auth": false,
    "purchase_details": {
      "customer": {
        "email_id": "joe.sam@gmail.com",
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
        "id": "v1-240912102222-aa-lZedaQ-up-4",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "FAILED",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "UPI",
        "payment_option": {
          "upi_data": {
            "txn_mode": "COLLECT",
            "payee": {},
            "payer": {}
          }
        },
        "error_detail": {
          "code": "UNAUTHORIZED",
          "message": "Merchant is not configured for payment"
        },
        "created_at": "2024-09-12T10:22:22.383Z",
        "updated_at": "2024-09-12T10:22:32.173Z"
      }
    ],
    "created_at": "2024-09-12T10:22:22.383Z",
    "updated_at": "2024-09-12T10:22:32.173Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Netbanking Payload
{
  "event_type": "PAYMENT_FAILED",
  "data": {
    "order_id": "v1-241108074323-aa-YwERfn",
    "merchant_order_reference": "aa9c8b9e-5d31-4e5b-b060-cd01309b07ac",
    "type": "CHARGE",
    "status": "ATTEMPTED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "110553",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
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
        "id": "v1-241108074323-aa-YwERfm-nb-I",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "FAILED",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "NETBANKING",
        "payment_option": {
          "netbanking_data": {
            "pay_code": "NB1531",
            "txn_mode": "REDIRECT"
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "",
          "rrn": "",
          "is_aggregator": true
        },
        "error_detail": {
          "code": "UNAUTHORIZED",
          "message": "Unknown Error"
        },
        "created_at": "2024-11-08T07:43:31.162Z",
        "updated_at": "2024-11-08T07:43:49.397Z",
        "integration_mode": "SEAMLESS"
      }
    ],
    "created_at": "2024-11-08T07:43:23.680Z",
    "updated_at": "2024-11-08T07:43:49.397Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Payment Failure Payload
{
  "event_type": "PAYMENT_FAILED",
  "data": {
    "order_id": "v1-241121095300-aa-B6UOMJ",
    "merchant_order_reference": "52c6ffe7-1c2d-4d3e-882e-3fd5a59f1b16",
    "type": "CHARGE",
    "status": "ATTEMPTED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "110047",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@gmail.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
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
        }
      }
    },
    "payments": [
      {
        "id": "v1-241121095300-aa-B6UOMJ-up-o",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "FAILED",
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
        "error_detail": {
          "code": "INVALID_REQUEST",
          "message": "Third party validation failure"
        },
        "created_at": "2024-11-21T09:53:10.644Z",
        "updated_at": "2024-11-21T09:53:13.040Z"
      }
    ],
    "created_at": "2024-11-21T09:53:00.339Z",
    "updated_at": "2024-11-21T09:53:13.042Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Link Expired Payload
{
  "event_type": "PAYMENT_FAILED",
  "data": {
    "order_id": "v1-241121101135-aa-pey9CW",
    "merchant_order_reference": "9ca2bffb-1fd3-48c9-9bcf-f26bab28fd59",
    "type": "CHARGE",
    "status": "ATTEMPTED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "327000",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": false,
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@gmail.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
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
        }
      }
    },
    "payments": [
      {
        "id": "v1-241121101135-aa-pey9CW-cc-h",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "FAILED",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "RUPAY",
            "issuer_name": "HDFC BANK LIMITED AS CREDIT CARD ISS",
            "card_category": "Consumer",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "",
          "rrn": "",
          "is_aggregator": true
        },
        "error_detail": {
          "code": "PAYMENT_EXPIRED",
          "message": "The payment has expired"
        },
        "created_at": "2024-11-21T10:11:44.778Z",
        "updated_at": "2024-11-21T10:12:15.171Z"
      }
    ],
    "created_at": "2024-11-21T10:11:35.320Z",
    "updated_at": "2024-11-21T10:12:15.171Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Dynamic Currency Conversion Payment
{
  "event_type": "PAYMENT_FAILED",
  "data": {
    "order_id": "v1-240828180835-aa-IKvddb",
    "merchant_order_reference": "4de00e1f-4855-4454-bf50-c0f7dd680e27",
    "type": "CHARGE",
    "status": "ATTEMPTED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "109500",
    "order_amount": {
      "value": 10000,
      "currency": "INR"
    },
    "pre_auth": true,
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
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
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-240828180835-aa-IKvddb-cc-2",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "FAILED",
        "payment_amount": {
          "value": 123,
          "currency": "USD"
        },
        "base_amount": {
          "value": 10000,
          "currency": "INR"
        },
        "conversion_rate": 0.0123,
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "NONE",
            "product_name": "",
            "card_category": "CONSUMER",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "7248685878696292803954",
          "rrn": "",
          "is_aggregator": true
        },
        "error_detail": {
          "code": "PAYMENT_DECLINED",
          "message": "Transaction declined by Acquirer due to unknown reason"
        },
        "created_at": "2024-08-28T18:08:35.651Z",
        "updated_at": "2024-08-28T18:10:15.584Z"
      }
    ],
    "created_at": "2024-08-28T18:08:35.651Z",
    "updated_at": "2024-08-28T18:10:15.584Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Split Settlement
{
  "event_type": "PAYMENT_FAILED",
  "data": {
    "order_id": "v1-250515103122-aa-PmmJWg",
    "merchant_order_reference": "0469228d-1c8c-4408-8d22-f79cc8731913",
    "type": "CHARGE",
    "status": "FAILED",
    "merchant_id": "111302",
    "order_amount": {
      "value": 21000,
      "currency": "INR"
    },
    "pre_auth": false,
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
            "split_merchant_id": "111302",
            "split_settlement_id": "v1-250515103122-aa-PmmJWg-ss-f",
            "amount": {
              "value": 10000,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-15T10:31:22.271Z"
          },
          {
            "split_merchant_id": "111302",
            "split_settlement_id": "v1-250515103122-aa-PmmJWg-ss-g",
            "amount": {
              "value": 2000,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-15T10:31:22.271Z"
          },
          {
            "split_merchant_id": "111302",
            "split_settlement_id": "v1-250515103122-aa-PmmJWg-ss-h",
            "amount": {
              "value": 8000,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-15T10:31:22.271Z"
          },
          {
            "split_merchant_id": "111302",
            "split_settlement_id": "v1-250515103122-aa-PmmJWg-ss-i",
            "amount": {
              "value": 500,
              "currency": "INR"
            },
            "on_hold": true,
            "status": "HOLD",
            "updated_at": "2025-05-15T10:31:22.271Z"
          },
          {
            "split_merchant_id": "111302",
            "split_settlement_id": "v1-250515103122-aa-PmmJWg-ss-j",
            "amount": {
              "value": 500,
              "currency": "INR"
            },
            "on_hold": false,
            "status": "RELEASED",
            "updated_at": "2025-05-15T10:31:22.271Z"
          }
        ]
      }
    },
    "payments": [
      {
        "id": "v1-250515103122-aa-PmmJWg-cc-a",
        "merchant_payment_reference": "91a44519-9fb6-4661-80be-26a677413038",
        "status": "FAILED",
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
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN",
            "last4_digit": "1091",
            "save": false
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2025-05-15T10:31:38.638Z",
        "updated_at": "2025-05-15T10:31:47.069Z"
      }
    ],
    "refunds": [],
    "created_at": "2025-05-15T10:31:22.271Z",
    "updated_at": "2025-05-15T10:55:41.014Z",
    "integration_mode": "SEAMLESS"
  }
}
```

Note: Capture block will be present if the capture for an order fails.

### ORDER_FAILED

Triggered when order is in `FAILED` state and respective payments are `FAILED` or `CANCELLED`. Shown below are the sample payloads returned against `ORDER_FAILED` event.

```json Card Payload
{
  "event_type": "ORDER_FAILED",
  "data": {
    "order_id": "v1-241212073943-aa-IlAyt8",
    "merchant_order_reference": "2f22cbaa-2be6-453f-82e7-5ae5d871e276",
    "type": "CHARGE",
    "status": "FAILED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "108142",
    "order_amount": {
      "value": 500,
      "currency": "INR"
    },
    "pre_auth": false,
    "purchase_details": {
      "customer": {
        "email_id": "joe.sam@gmail.com",
        "first_name": "joe",
        "last_name": "kumar",
        "customer_id": "192212",
        "mobile_number": "192192883",
        "billing_address": {},
        "shipping_address": {
          "address1": "H.No 15, Sector 17",
          "address2": "string",
          "address3": "string",
          "pincode": "144001123",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        }
      }
    },
    "payments": [
      {
        "id": "v1-241212073943-aa-IlAyt8-cc-a",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "FAILED",
        "payment_amount": {
          "value": 500,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "created_at": "2024-12-12T07:40:01.653Z",
        "updated_at": "2024-12-12T07:40:01.653Z"
      }
    ],
    "refunds": [],
    "created_at": "2024-12-12T07:39:43.031Z",
    "updated_at": "2024-12-12T07:40:01.653Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Dynamic Currency Conversion Payment
{
  "event_type": "ORDER_FAILED",
  "data": {
    "order_id": "v1-240828180835-aa-IKvddb",
    "merchant_order_reference": "4de00e1f-4855-4454-bf50-c0f7dd680e27",
    "type": "CHARGE",
    "status": "FAILED",
    "callback_url": "https://sample-callback-url",
    "failure_callback_url": "https://failure.callback.com",
    "merchant_id": "109500",
    "order_amount": {
      "value": 10000,
      "currency": "INR"
    },
    "pre_auth": true,
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
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
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-240828180835-aa-IKvddb-cc-2",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "FAILED",
        "payment_amount": {
          "value": 123,
          "currency": "USD"
        },
        "base_amount": {
          "value": 10000,
          "currency": "INR"
        },
        "conversion_rate": 0.0123,
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "NONE",
            "product_name": "",
            "card_category": "CONSUMER",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "7248685878696292803954",
          "rrn": "",
          "is_aggregator": true
        },
        "error_detail": {
          "code": "PAYMENT_DECLINED",
          "message": "Transaction declined by Acquirer due to unknown reason"
        },
        "created_at": "2024-08-28T18:08:35.651Z",
        "updated_at": "2024-08-28T18:10:15.584Z"
      }
    ],
    "created_at": "2024-08-28T18:08:35.651Z",
    "updated_at": "2024-08-28T18:10:15.584Z",
    "integration_mode": "SEAMLESS"
  }
}
```

### REFUND_PROCESSED

Triggered when the refund is successful. Shown below are the sample payloads returned against different payment method.

```json Card Payload
{
  "event_type": "REFUND_PROCESSED",
  "data": {
    "order_id": "v1-240828181713-aa-hNlYwt",
    "parent_order_id": "v1-241010055924-aa-AHbN0s",
    "merchant_order_reference": "18c693c4-27ce-444d-a040-9dc3dcc06213",
    "type": "REFUND",
    "status": "PROCESSED",
    "merchant_id": "109500",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
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
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-240828181713-aa-hNlYwt-cc-K",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "7248690362736367903954",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2024-08-28T18:17:13.147Z",
        "updated_at": "2024-08-28T18:17:17.157Z"
      }
    ],
    "created_at": "2024-08-28T18:17:13.147Z",
    "updated_at": "2024-08-28T18:17:17.157Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Tokenized Card Payload
{
  "event_type": "REFUND_PROCESSED",
  "data": {
    "order_id": "v1-240828181713-aa-hNlYwt",
    "parent_order_id": "v1-241010055924-aa-AHbN0s",
    "merchant_order_reference": "18c693c4-27ce-444d-a040-9dc3dcc06213",
    "type": "REFUND",
    "status": "PROCESSED",
    "merchant_id": "109500",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
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
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-240828181713-aa-hNlYwt-cc-K",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "7248690362736367903954",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2024-08-28T18:17:13.147Z",
        "updated_at": "2024-08-28T18:17:17.157Z"
      }
    ],
    "created_at": "2024-08-28T18:17:13.147Z",
    "updated_at": "2024-08-28T18:17:17.157Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Pay by Points
{
  "event_type": "REFUND_PROCESSED",
  "data": {
    "order_id": "v1-240828181713-aa-hNlYwt",
    "parent_order_id": "v1-241010055924-aa-AHbN0s",
    "merchant_order_reference": "18c693c4-27ce-444d-a040-9dc3dcc06213",
    "type": "REFUND",
    "status": "PROCESSED",
    "merchant_id": "109500",
    "order_amount": {
      "value": 1000,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
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
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-240820071549-aa-WxMmCj-cc-3",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "paymentAmount": {
          "value": 800,
          "currency": "INR"
        },
        "paymentMethod": "CARD",
        "paymentOption": {
          "cardData": {
            "cardType": "",
            "networkName": "",
            "issuerName": "",
            "productName": "",
            "cardCategory": "",
            "countryCode": ""
          }
        },
        "captureData": []
      },
      {
        "id": "v1-240820071549-aa-WxMmCj-pt-7",
        "status": "PROCESSED",
        "paymentAmount": {
          "value": 200,
          "currency": "INR"
        },
        "paymentMethod": "POINTS",
        "paymentOption": {
          "cardData": {
            "cardType": "",
            "networkName": "",
            "issuerName": "",
            "productName": "",
            "cardCategory": "",
            "countryCode": ""
          }
        },
        "captureData": []
      }
    ],
    "createdAt": "2024-08-28T18:17:13.147Z",
    "updatedAt": "2024-08-28T18:17:13.147Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json UPI Intent Payload
{
  "event_type": "REFUND_PROCESSED",
  "data": {
    "order_id": "v1-240828181713-aa-hNlYwt",
    "parent_order_id": "v1-241010055924-aa-AHbN0s",
    "merchant_order_reference": "18c693c4-27ce-444d-a040-9dc3dcc06213",
    "type": "REFUND",
    "status": "PROCESSED",
    "merchant_id": "109500",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
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
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-240912062449-aa-V2v5g5-up-T",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "UPI",
        "payment_option": {
          "upi_data": {
            "txn_mode": "INTENT",
            "payee": {
              "reference_id": "174425",
              "reference_type": "MERCHANT",
              "vpa": "pinelabs.24092@hdfcbank",
              "acquirer_name": "HDFC"
            },
            "payer": {
              "vpa": "saklania8-2@okicici",
              "phone_number": "918979279800",
              "account_type": "SAVINGS"
            }
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "425600485036",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2024-09-12T06:24:49.834Z",
        "updated_at": "2024-09-12T06:24:53.389Z"
      }
    ],
    "created_at": "2024-09-12T06:24:49.834Z",
    "updated_at": "2024-09-12T06:24:53.389Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Card Multiple Refunds
{
  "event_type": "REFUND_PROCESSED",
  "data": {
    "order_id": "v1-240828181713-aa-hNlYwt",
    "parent_order_id": "v1-241010055924-aa-AHbN0s",
    "merchant_order_reference": "18c693c4-27ce-444d-a040-9dc3dcc06213",
    "type": "REFUND",
    "status": "PROCESSED",
    "merchant_id": "109500",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "192212",
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
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-240828181713-aa-hNlYwt-cc-K",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "7248690362736367903954",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2024-08-28T18:17:13.147Z",
        "updated_at": "2024-08-28T18:17:17.157Z"
      }
    ],
    "created_at": "2024-08-28T18:17:13.147Z",
    "updated_at": "2024-08-28T18:17:17.157Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Netbanking Payload
{
  "event_type": "REFUND_PROCESSED",
  "data": {
    "order_id": "v1-241108070043-aa-Sys3RK",
    "merchant_order_reference": "3ebf9a69-ac36-4a66-9f35-01f339c4486d",
    "type": "CHARGE",
    "status": "FULLY_REFUNDED",
    "merchant_id": "110553",
    "order_amount": {
      "value": 100,
      "currency": "INR"
    },
    "pre_auth": false,    
    "notes": "order1",
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
        "id": "v1-241108070043-aa-Sys3RJ-nb-7",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "NETBANKING",
        "acquirer_data": {
          "approval_code": "0300",
          "acquirer_reference": "USBI0001265269",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2024-11-08T07:00:54.043Z",
        "updated_at": "2024-11-08T07:01:51.687Z"
      }
    ],
    "refunds": [
      {
        "merchant_order_reference": "a887681c-1bbc-4d94-84e8-0ff90ea82686",
        "order_id": "v1-241108070811-aa-8cHklk",
        "type": "REFUND",
        "status": "PROCESSED",
        "order_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payments": [
          {
            "id": "v1-241108070811-aa-8cHklk-nb-W",
            "parent_payment_id": "v1-241108070043-aa-Sys3RJ-nb-7",
            "status": "PROCESSED",
            "payment_amount": {
              "value": 100,
              "currency": "INR"
            },
            "payment_method": "NETBANKING",
            "acquirer_data": {
              "approval_code": "0699",
              "acquirer_reference": "USBI00012652691",
              "rrn": "",
              "is_aggregator": true
            },
            "created_at": "2024-11-08T07:08:11.258Z",
            "updated_at": "2024-11-08T07:08:12.819Z"
          }
        ],
        "created_at": "2024-11-08T07:08:11.258Z",
        "updated_at": "2024-11-08T07:08:12.820Z"
      }
    ],
    "created_at": "2024-11-08T07:00:43.756Z",
    "updated_at": "2024-11-08T07:01:51.687Z",
    "integration_mode": "SEAMLESS"
  }
}
```
```json Split Settlement
{
  "event_type": "REFUND_PROCESSED",
  "data": {
    "order_id": "v1-250515122206-aa-NwXD5S",
    "parent_order_id": "v1-250515121936-aa-M3Gspz",
    "merchant_order_reference": "db602eb2-3bba-451c-ad66-992b63702e3a",
    "type": "REFUND",
    "status": "PROCESSED",
    "merchant_id": "111302",
    "order_amount": {
      "value": 10000,
      "currency": "INR"
    },
    "pre_auth": false,
    "purchase_details": {
      "merchant_metadata": {
        "key1": "value1",
        "key2": "value2"
      },
      "split_info": {
        "split_type": "AMOUNT",
        "split_details": [
          {
            "parent_order_split_settlement_id": "v1-250515121936-aa-M3Gspz-ss-f",
            "split_merchant_id": "111302",
            "split_settlement_id": "v1-250515122206-aa-NwXD5S-ss-b",
            "amount": {
              "value": 10000,
              "currency": "INR"
            },
            "on_hold": false,
            "status": "DO_NOT_RECOVER",
            "updated_at": "2025-05-15T12:22:06.857Z"
          }
        ]
      }
    },
    "payments": [
      {
        "id": "v1-250515122206-aa-NwXD5S-cc-a",
        "merchant_payment_reference": "",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 10000,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "7473117282206499303812",
          "rrn": "",
          "is_aggregator": true
        },
        "offer_data": {},
        "created_at": "2025-05-15T12:22:06.857Z",
        "updated_at": "2025-05-15T12:22:08.804Z"
      }
    ],
    "refunds": [],
    "created_at": "2025-05-15T12:22:06.857Z",
    "updated_at": "2025-05-15T12:22:08.804Z",
    "integration_mode": "SEAMLESS"
  }
}
```

### REFUND_FAILED

Triggered when the refund against an order get failed. Shown below is a sample payload returned against REFUND_FAILED event.

```json Card Payload
{
  "event_type": "REFUND_FAILED",
  "data": {
    "order_id": "v1-240924042246-aa-5oxVVr",
    "parent_order_id": "v1-240924042153-aa-mROLIp",
    "merchant_order_reference": "e5e32cb6-e5a6-4c37-9bbd-cb3552965088",
    "type": "REFUND",
    "status": "FAILED",
    "merchant_id": "109500",
    "order_amount": {
      "value": 199,
      "currency": "INR"
    },
    "pre_auth": "false",    
    "notes": "order1",
    "purchase_details": {},
    "payments": [
      {
        "id": "v1-240924042246-aa-5oxVVr-cc-N",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "FAILED",
        "payment_amount": {
          "value": 199,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "7271517532766944103954",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2024-09-24T04:22:46.880734Z",
        "updated_at": "2024-09-24T04:24:04.901502Z"
      }
    ],
    "created_at": "2024-09-24T04:22:46.880778Z",
    "updated_at": "2024-09-24T04:24:04.901573Z",
    "integration_mode": "SEAMLESS"
  }
}
```

### TOKEN_ACTIVATED

Triggered when the token is activated via the network. Shown below is the sample payload returned against token activation method.

```json Token Activated
{
  "event_type": "TOKEN_ACTIVATED",
  "data": {
    "token": {
      "merchant_payment_reference": "payment-v1-0811030624",
      "token_id": "token-v1-0811030624-aa-RBDgpR",
      "merchant_token_reference": "",
      "customer_id": "cust-v1-0811030624-aa-RBDgpR",
      "status": "ACTIVE",
      "payment_method": "CARD",
      "expired_at": "2024-10-04T13:11:29.645591Z",
      "status_reason": null,
      "merchant_metadata": {
        "key1": "XX",
        "key2": "DOF"
      },
      "card_data": {
        "last4_digit": "2363",
        "card_type": "CREDIT",
        "network_name": "VISA",
        "issuer_name": "HDFC",
        "card_category": "Consumer",
        "country_code": "IND",
        "international": false,
        "emi": true,
        "cvv_required": false
      },
      "is_compliant": true,
      "created_at": "2024-10-04T13:11:29.645657Z",
      "updated_at": "2024-10-04T13:11:29.645657Z"
    }
  }
}
```

### TOKEN_DEACTIVATED

Triggered when the token is Deactivated. Shown below is the sample payload returned for token deactivation scenario.

```json Token Deactivated
{
  "event_type": "TOKEN_DEACTIVATED",
  "data": {
    "token": {
      "merchant_payment_reference": "payment-v1-0811030624",
      "token_id": "token-v1-0811030624-aa-RBDgpR",
      "merchant_token_reference": "",
      "customer_id": "cust-v1-0811030624-aa-RBDgpR",
      "status": "DEACTIVATED",
      "payment_method": "CARD",
      "expired_at": "2024-10-04T13:11:29.645591Z",
      "status_reason": "card stolen",
      "merchant_metadata": {
        "key1": "XX",
        "key2": "DOF"
      },
      "card_data": {
        "last4_digit": "2363",
        "card_type": "CREDIT",
        "network_name": "VISA",
        "issuer_name": "HDFC",
        "card_category": "Consumer",
        "country_code": "IND",
        "international": false,
        "emi": true,
        "cvv_required": false
      },
      "is_compliant": true,
      "created_at": "2024-10-04T13:11:29.645657Z",
      "updated_at": "2024-10-04T13:11:29.645657Z"
    }
  }
}
```

### TOKEN_SUSPENDED

Triggered when the token is Suspended. Shown below is the sample payload returned against token service providers.

```json Token Suspended
{
  "event_type": "TOKEN_SUSPENDED",
  "data": {
    "token": {
      "merchant_payment_reference": "payment-v1-0811030624",
      "token_id": "token-v1-0811030624-aa-RBDgpR",
      "merchant_token_reference": "",
      "customer_id": "cust-v1-0811030624-aa-RBDgpR",
      "status": "SUSPENDED",
      "payment_method": "CARD",
      "expired_at": "2024-10-04T13:11:29.645591Z",
      "status_reason": "card stolen",
      "merchant_metadata": {
        "key1": "XX",
        "key2": "DOF"
      },
      "card_data": {
        "last4_digit": "2363",
        "card_type": "CREDIT",
        "network_name": "VISA",
        "issuer_name": "HDFC",
        "card_category": "Consumer",
        "country_code": "IND",
        "international": false,
        "emi": true,
        "cvv_required": false
      },
      "is_compliant": true,
      "created_at": "2024-10-04T13:11:29.645657Z",
      "updated_at": "2024-10-04T13:11:29.645657Z"
    }
  }
}
```

### TOKEN_PROVISION_FAILED

Triggered when token provisioning fails. Shown below is the sample payload returned when token provisioning failed.

```json Token Provision Failed
{
  "event_type": "TOKEN_PROVISION_FAILED",
  "data": {
    "token": {
      "merchant_payment_reference": "payment-v1-0811030624",
      "token_id": "token-v1-0811030624-aa-RBDgpR",
      "merchant_token_reference": "",
      "customer_id": "cust-v1-0811030624-aa-RBDgpR",
      "status": "FAILED",
      "payment_method": "CARD",
      "expired_at": "2024-10-04T13:11:29.645591Z",
      "status_reason": "card is not elegible for tokenisation",
      "failure_reason": {
        "code": "INVALID_REQUEST",
        "message": "Request is not well-formed, syntactically incorrect, or violates schema",
        "additional_error_details": {
          "source": "network",
          "step": "token_provision",
          "reason": "card is not elegible for tokenisation",
          "metadata": {}
        }
      },
      "merchant_metadata": {
        "key1": "XX",
        "key2": "DOF"
      },
      "card_data": {
        "last4_digit": "2363",
        "card_type": "CREDIT",
        "network_name": "VISA",
        "issuer_name": "HDFC",
        "card_category": "Consumer",
        "country_code": "IND",
        "international": false,
        "emi": true,
        "cvv_required": false
      },
      "is_compliant": true,
      "created_at": "2024-10-04T13:11:29.645657Z",
      "updated_at": "2024-10-04T13:11:29.645657Z"
    }
  }
}
```

<br />

```json Card Payload
{
  "event_type": "REFUND_FAILED",
  "data": {
    "order_id": "v1-240924042246-aa-5oxVVr",
    "parent_order_id": "v1-240924042153-aa-mROLIp",
    "merchant_order_reference": "e5e32cb6-e5a6-4c37-9bbd-cb3552965088",
    "type": "REFUND",
    "status": "FAILED",
    "merchant_id": "109500",
    "order_amount": {
      "value": 199,
      "currency": "INR"
    },
    "pre_auth": "false",
    "allowed_payment_methods": [],    
    "notes": "order1",
    "purchase_details": {},
    "payments": [
      {
        "id": "v1-240924042246-aa-5oxVVr-cc-N",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "FAILED",
        "payment_amount": {
          "value": 199,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "7271517532766944103954",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2024-09-24T04:22:46.880734Z",
        "updated_at": "2024-09-24T04:24:04.901502Z"
      }
    ],
    "created_at": "2024-09-24T04:22:46.880778Z",
    "updated_at": "2024-09-24T04:24:04.901573Z",
    "integration_mode": "SEAMLESS"
  }
}
```

### SUBSCRIPTION_ACTIVATED

Triggered when the subscription is activated. Shown below is the sample payload returned when subscription is activated.

```json Subscription Activated
{
  "event_type": "SUBSCRIPTION_ACTIVATED",
  "event_id": "v1-event-002",
  "merchant_id": "2345",
  "data": {
    "subscription": {
      "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
      "merchant_order_reference": "1234567890",
      "enable_notification": true,
      "plan_details": {
        "plan_id": "v1-plan-4405071524-aa-qlAtAf",
        "plan_name": "Monthly Plan",
        "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
        "frequency_count": 1,
        "frequency": "Month",
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
      "created_at": "2022-10-21T17:32:28Z",
      "modified_at": "2022-10-21T17:32:28Z"
    }
  }
}
```

### SUBSCRIPTION_PENDING

Triggered when the subscription is pending. Shown below is the sample payload returned for subscription pending scenario.

```json SUBSCRIPTION_PENDING
{
  "event_type": "SUBSCRIPTION_PENDING",
  "event_id": "v1-event-002",
  "merchant_id": "2345",
  "data": {
    "subscription": {
      "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
      "merchant_order_reference": "1234567890",
      "enable_notification": true,
      "plan_details": {
        "plan_id": "v1-plan-4405071524-aa-qlAtAf",
        "plan_name": "Monthly Plan",
        "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
        "frequency_count": 1,
        "frequency": "Month",
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
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      },
      "status": "CREATED",
      "bank_account": {
        "account_number": "123456789012345",
        "name": "Gaurav Kumar",
        "ifsc": "123456789012345"
      },
      "created_at": "2022-10-21T17:32:28Z",
      "modified_at": "2022-10-21T17:32:28Z"
    }
  }
}
```

### SUBSCRIPTION_PAUSED

Triggered when the subscription is paused. Shown below is the sample payload returned for subscription paused scenario.

```json SUBSCRIPTION_PAUSED
{
  "event_type": "SUBSCRIPTION_PAUSED",
  "event_id": "v1-event-002",
  "merchant_id": "2345",
  "data": {
    "subscription": {
      "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
      "merchant_order_reference": "1234567890",
      "enable_notification": true,
      "plan_details": {
        "plan_id": "v1-plan-4405071524-aa-qlAtAf",
        "plan_name": "Monthly Plan",
        "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
        "frequency_count": 1,
        "frequency": "Month",
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
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      },
      "status": "PAUSED",
      "bank_account": {
        "account_number": "123456789012345",
        "name": "Gaurav Kumar",
        "ifsc": "123456789012345"
      },
      "created_at": "2022-10-21T17:32:28Z",
      "modified_at": "2022-10-21T17:32:28Z"
    }
  }
}
```

### SUBSCRIPTION_RESUMED

Triggered when the subscription is resumed. Shown below is the sample payload returned for subscription resumed scenario.

```json SUBSCRIPTION_RESUMED
{
  "event_type": "SUBSCRIPTION_RESUMED",
  "event_id": "v1-event-002",
  "merchant_id": "2345",
  "data": {
    "subscription": {
      "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
      "merchant_order_reference": "1234567890",
      "enable_notification": true,
      "plan_details": {
        "plan_id": "v1-plan-4405071524-aa-qlAtAf",
        "plan_name": "Monthly Plan",
        "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
        "frequency_count": 1,
        "frequency": "Month",
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
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      },
      "status": "RESUMED",
      "bank_account": {
        "account_number": "123456789012345",
        "name": "Gaurav Kumar",
        "ifsc": "123456789012345"
      },
      "created_at": "2022-10-21T17:32:28Z",
      "modified_at": "2022-10-21T17:32:28Z"
    }
  }
}
```

### SUBSCRIPTION_COMPLETED

Triggered when the subscription is completed. Shown below is the sample payload returned for subscription completed scenario.

```json SUBSCRIPTION_COMPLETED
{
  "event_type": "SUBSCRIPTION_COMPLETED",
  "event_id": "v1-event-002",
  "merchant_id": "2345",
  "data": {
    "subscription": {
      "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
      "merchant_order_reference": "1234567890",
      "enable_notification": true,
      "plan_details": {
        "plan_id": "v1-plan-4405071524-aa-qlAtAf",
        "plan_name": "Monthly Plan",
        "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
        "frequency_count": 1,
        "frequency": "Month",
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
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      },
      "status": "COMPLETED",
      "bank_account": {
        "account_number": "123456789012345",
        "name": "Gaurav Kumar",
        "ifsc": "123456789012345"
      },
      "created_at": "2022-10-21T17:32:28Z",
      "modified_at": "2022-10-21T17:32:28Z"
    }
  }
}
```

### SUBSCRIPTION_CHARGED

Triggered when the subscription is charged. Shown below is the sample payload returned for subscription charged scenario.

```json SUBSCRIPTION_CHARGED
{
  "event_type": "SUBSCRIPTION_CHARGED",
  "event_id": "v1-event-002",
  "merchant_id": "2345",
  "data": {
    "subscription": {
      "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
      "merchant_order_reference": "1234567890",
      "enable_notification": true,
      "plan_details": {
        "plan_id": "v1-plan-4405071524-aa-qlAtAf",
        "plan_name": "Monthly Plan",
        "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
        "frequency_count": 1,
        "frequency": "Month",
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
      "created_at": "2022-10-21T17:32:28Z",
      "modified_at": "2022-10-21T17:32:28Z"
    }
  }
}
```

### SUBSCRIPTION_HALTED

Triggered when the subscription is halted. Shown below is the sample payload returned for subscription halted scenario.

```json SUBSCRIPTION_HALTED
{
  "event_type": "SUBSCRIPTION_HALTED",
  "event_id": "v1-event-002",
  "merchant_id": "2345",
  "data": {
    "subscription": {
      "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
      "merchant_order_reference": "1234567890",
      "enable_notification": true,
      "plan_details": {
        "plan_id": "v1-plan-4405071524-aa-qlAtAf",
        "plan_name": "Monthly Plan",
        "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
        "frequency_count": 1,
        "frequency": "Month",
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
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      },
      "status": "INACTIVE",
      "bank_account": {
        "account_number": "123456789012345",
        "name": "Gaurav Kumar",
        "ifsc": "123456789012345"
      },
      "created_at": "2022-10-21T17:32:28Z",
      "modified_at": "2022-10-21T17:32:28Z"
    }
  }
}
```
