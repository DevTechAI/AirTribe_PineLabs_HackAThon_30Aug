---
title: "Available Events"
slug: "available-events-copy-1"
excerpt: "Webhook events available on Plural."
hidden: true
createdAt: "Thu Mar 20 2025 10:05:11 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Mar 24 2025 09:08:56 GMT+0000 (Coordinated Universal Time)"
---
The table below list the available webhook events on Plural with descriptions.

| Webhook                    | Description                                                                           |
| :------------------------- | :------------------------------------------------------------------------------------ |
| `CUSTOMER_ACTIVATED`       | When the customer is activated on Plural's platform.                                  |
| `CUSTOMER_DELETED`         | When the customer is removed from Plural's system.                                    |
| `CUSTOMER_SUSPENDED`       | When the customer is temporarily suspended on the Plural platform through the portal. |
| `CUSTOMER_CREATION_FAILED` | When the customer creation is failed.                                                 |
| `ORDER_AUTHORIZED`         | When the order is ready for authorization.                                            |
| `ORDER_PROCESSED`          | When the payment is successfully received.                                            |
| `ORDER_CANCELLED`          | When the order is cancelled.                                                          |
| `PAYMENT_FAILED`           | When the payment against an order get failed.                                         |
| `ORDER_FAILED`             | When the order is failed.                                                             |
| `REFUND_PROCESSED`         | When the refund is successful.                                                        |
| `REFUND_FAILED`            | When the refund against an order get failed.                                          |
| `TOKEN_PROVISION_PENDING`  | The token provisioning is in initiated or in pending state                            |
| `TOKEN_ACTIVATED`          | When the token is activated via the network.                                          |
| `TOKEN_DEACTIVATED`        | When the token is deactivated.                                                        |
| `TOKEN_SUSPENDED`          | When the token is suspended.                                                          |
| `TOKEN_PROVISION_FAILED`   | When the token provisioning is failed.                                                |

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
