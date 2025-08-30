---
title: "Cardless Integration Steps"
slug: "affordability-suite-cardless-integration-steps-1"
excerpt: "Learn how to integrate the Plural Affordability Suite to provide your merchants with a seamless shopping experience."
hidden: true
createdAt: "Fri Jan 24 2025 07:19:55 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri May 02 2025 10:48:19 GMT+0000 (Coordinated Universal Time)"
---
Follow the below steps to integrate with Plural affordability suite in your application.

1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/affordability-suite-cardless-integration-steps#1-prerequisite-generate-token" >\[Prerequisite] Generate Token</a>
2. <a href="https://developer.pluralonline.com/docs/affordability-suite-cardless-integration-steps#2-offer-discovery-cardless" >Offer Discovery Cardless</a>
3. <a href="https://developer.pluralonline.com/docs/affordability-suite-cardless-integration-steps#3-offer-validation" >Offer Validation</a>
4. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/affordability-suite-cardless-integration-steps#4-create-order" >Create Order</a>
5. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/affordability-suite-cardless-integration-steps#5-create-card-payment" >Create Card Payment</a>
6. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/affordability-suite-cardless-integration-steps#6-handle-payment" >Handle Payment</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/affordability-suite-cardless-integration-steps#61-store-payment-details-on-your-server" >Store Payment Details on Your Server</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/affordability-suite-cardless-integration-steps#62-verify-payment-signature" >Verify Payment Signature</a>
7. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/affordability-suite-cardless-integration-steps#7-capture-order" >Capture Order</a>
8. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/affordability-suite-cardless-integration-steps#8-cancel-order" >Cancel Order</a>

> 📘 Note
> 
> - Ensure you store your Client ID and Secret in your Backend securely.
> - Integrate our APIs on your backend system.
> - We strictly recommend not to call our APIs from the frontend.

> 🚧 Watch Out
> 
> - To Integrate with Plural seamless checkout flow you must have a PCI compliance certificate.

## 1. [Prerequisite] Generate Token

Integrate our Generate Token API in your backend servers to generate the access token. Use the token generated to authenticate Plural APIs.

Use the below endpoint to generate a token.

```text Generate Token Endpoint for UAT
POST: https://pluraluat.v2.pinepg.in/api/auth/v1/token
```
```text Generate Token Endpoint for PROD
POST: https://api.pluralpay.in/api/auth/v1/token
```

Below is a sample request and response for the Generate Token API.

```json Sample Request
{
  "client_id": "1234567890",
  "client_secret": "asdfgwei7egyhuggwp39w8rh",
  "grant_type": "client_credentials"
}
```
```json Sample Response
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
  "expires_in": 3600
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/v3.0/reference/generate-token" target="_blank">Generate Token API</a> documentation to learn more.

## 2. Offer Discovery Cardless

Use this API to check the offers cardless and calculate the EMI.

Use the below endpoint to discover the offers cardless.

```text Offer Discovery Cardless Endpoint for UAT
POST: https://pluraluat.v2.pinepg.in/api/affordability/v1/offer/discovery
```
```text Offer Discovery Cardless Endpoint for PROD
POST: https://api.pluralpay.in/api/affordability/v1/offer/discovery
```

Below is a sample request and response for the Offer Discovery Cardless API.

```json Sample Request
{
  "order_amount": {
    "currency": "INR",
    "value": 1010000
  },
  "payment_option": {
    "cardless_details": {
      "pan_last_digits": "8907",
      "registered_mobile_number": "99914152866"
    }
  }
}
```
```json Sample Response
{
  "issuers": [
    {
      "id": "23",
      "name": "INDUSIND CC",
      "issuer_type": "CC_BANK",
      "priority": 1,
      "tenures": [
        {
          "tenure_id": "1",
          "name": "3 Months",
          "tenure_type": "MONTH",
          "tenure_value": 3,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1232139
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 410713
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1232139
          },
          "interest_amount": {
            "currency": "INR",
            "value": 32139
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "2",
          "name": "6 Months",
          "tenure_type": "MONTH",
          "tenure_value": 6,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1256616
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 209436
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1256616
          },
          "interest_amount": {
            "currency": "INR",
            "value": 56616
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "3",
          "name": "9 Months",
          "tenure_type": "MONTH",
          "tenure_value": 9,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1281411
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 142379
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1281411
          },
          "interest_amount": {
            "currency": "INR",
            "value": 81411
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "4",
          "name": "12 Months",
          "tenure_type": "MONTH",
          "tenure_value": 12,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1306524
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 108877
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1306524
          },
          "interest_amount": {
            "currency": "INR",
            "value": 106524
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "5",
          "name": "18 Months",
          "tenure_type": "MONTH",
          "tenure_value": 18,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1357686
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 75427
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1357686
          },
          "interest_amount": {
            "currency": "INR",
            "value": 157686
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "6",
          "name": "24 Months",
          "tenure_type": "MONTH",
          "tenure_value": 24,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1410120
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 58755
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1410120
          },
          "interest_amount": {
            "currency": "INR",
            "value": 210120
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        }
      ],
      "issuer_data": {}
    }
  ]
}
```
```
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/offer-discovery-create" target="_blank">Offer Discovery API</a> documentation to learn more.

## 3. Offer Validation

Use this API for validating applied offers.

Use the below endpoint to validate the offers applied.

```text Offer Validation Endpoint for UAT
POST: https://pluraluat.v2.pinepg.in/api/affordability/v1/offer/validate
```
```text Offer Validation Endpoint for PROD
POST: https://api.pluralpay.in/api/affordability/v1/offer/validate
```

Below is a sample request and response for the Offer Validation API.

```json Sample Request
{
  "order_amount": {
    "value": 2000000,
    "currency": "INR"
  },
  "payment_amount": {
    "value": 1950000,
    "currency": "INR"
  },
  "offer_data": {
    "offer_details": {
      "tenure": {
        "loan_amount": {
          "currency": "INR",
          "value": 1950000
        },
        "total_discount_amount": {
          "currency": "INR",
          "value": 50000
        },
        "net_payment_amount": {
          "currency": "INR",
          "value": 2015358
        },
        "monthly_emi_amount": {
          "currency": "INR",
          "value": 671786
        },
        "total_emi_amount": {
          "currency": "INR",
          "value": 2015358
        },
        "interest_amount": {
          "currency": "INR",
          "value": 65358
        },
        "processing_fee_details": {
          "amount": {
            "currency": "INR",
            "value": 19900
          }
        },
        "tenure_id": "1",
        "name": "3 Months",
        "tenure_type": "MONTH",
        "tenure_value": 3,
        "issuer_offer_parameters": [
          {
            "program_type": "BANK_EMI",
            "offer_id": "1564",
            "offer_parameter_id": "63814"
          },
          {
            "program_type": "MERCHANT_BANK_OFFER",
            "offer_id": "1523",
            "offer_parameter_id": "63566"
          }
        ],
        "discount": {
          "discount_type": "INSTANT",
          "amount": {
            "currency": "INR",
            "value": 50000
          }
        },
        "interest_rate_percentage": 20,
        "emi_type": "STANDARD"
      },
      "id": "6",
      "name": "HDFC CC",
      "issuer_type": "CC_BANK",
      "priority": 1
    }
  },
  "payment_method": "CREDIT_EMI",
  "payment_option": {
    "card_details": {
      "card_number": "4690000046910000"
    }
  }
}
```
```json Sample Response
{
  "code": "ELIGIBLE",
  "message": "Offer is Eligible"
}
```
```json Shared response
{    "payments": [        {            "merchant_payment_reference": {{$guid}},            "payment_method": "CARDLESS_EMI",            "payment_amount": {                "value": 17800,                "currency": "INR"            },            "payment_option": {                "cardless_details": {                    "pan_last_digits": "1089",                    "registered_mobile_number": "9582223917"                }            },            "offer_data": {                "offer_details": {                    "id": "7",                    "name": "HDFC DC",                    "issuer_type": "DC_BANK",                    "priority": 1,                    "tenure": {                        "tenure_id": "1",                        "name": "3 Months",                        "tenure_type": "MONTH",                        "tenure_value": 3,                        "issuer_offer_parameters": [                            {                                "program_type": "BANK_EMI",                                "offer_id": "1",                                "offer_parameter_id": "1"                            }                        ],                        "details": [],                        "loan_amount": {                            "currency": "INR",                            "value": 17800                        },                        "net_payment_amount": {                            "currency": "INR",                            "value": 18276                        },                        "monthly_emi_amount": {                            "currency": "INR",                            "value": 6092                        },                        "total_emi_amount": {                            "currency": "INR",                            "value": 18276                        },                        "interest_amount": {                            "currency": "INR",                            "value": 476                        },                        "interest_rate_percentage": 16.0,                        "processing_fee_details": {                            "amount": {                                "currency": "INR",                                "value": 29900                            }                        },                        "emi_type": "STANDARD"                    }                }            }        }    ]}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/offer-validation-create" target="_blank">Offer Validation API</a> documentation to learn more.

## 4. Create Order

To create an Order use our Create Order API, for authentication use the generated access token in the headers of the API request.

Use the below endpoint to create an order.

```Text Create Order Endpoint for UAT
POST: https://pluraluat.v2.pinepg.in/api/pay/v1/orders
```
```text Create Order Endpoint for PROD
POST: https://api.pluralpay.in/api/pay/v1/orders
```

Below is a sample request and response for a Create Order API.

```json Sample Request
{
  "merchant_order_reference": 112345,
  "order_amount": {
    "value": 1100,
    "currency": "INR"
  },
  "pre_auth": false,
  "notes": "order1",
  "callback_url": "https://sample-callback-url",
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
  "cart_coupon_discount_amount": {
    "value": 100,
    "currency": "INR"
  }
}
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
    "callback_url": "https://sample-callback-url",
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
    "updated_at": "2024-07-15T05:44:51.174Z",
    "cart_coupon_discount_amount": {
      "value": 100,
      "currency": "INR"
    }
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/reference/affordability-suite-orders-create" target="_blank">Create Order API</a> documentation to learn more.

> 📘 Note:
> 
> When the pre-authorization is set to true you can capture the payment after successful delivery or service.

## 5. Create Payment

To create a payment use our Create Payment API, use the `order_id` returned in the response of a Create Order API to link the payment against an order.

Use the below endpoint to create a payment.

```text Create Payment Endpoint for UAT
POST: https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/payments
```
```text Create Payment Endpoint for PROD
POST: https://api.pluralpay.in/api/pay/v1/orders/{order_id}/payments
```

Below is a sample request and sample response for Create Payment API.

```json Sample Request
{
  "payments": [
    {
      "merchant_payment_reference": "c7a7f778-b68f-462b-a6af-50698df12a4a",
      "payment_method": "CARDLESS_EMI",
      "payment_amount": {
        "value": 17800,
        "currency": "INR"
      },
      "payment_option": {
        "cardless_details": {
          "pan_last_digits": "1089",
          "registered_mobile_number": "9582223917"
        }
      },
      "offer_data": {
        "offer_details": {
          "id": "7",
          "name": "HDFC DC",
          "issuer_type": "DC_BANK",
          "priority": 1,
          "tenure": {
            "tenure_id": "1",
            "name": "3 Months",
            "tenure_type": "MONTH",
            "tenure_value": 3,
            "issuer_offer_parameters": [
              {
                "program_type": "BANK_EMI",
                "offer_id": "1",
                "offer_parameter_id": "1"
              }
            ],
            "details": [],
            "loan_amount": {
              "currency": "INR",
              "value": 17800
            },
            "net_payment_amount": {
              "currency": "INR",
              "value": 18276
            },
            "monthly_emi_amount": {
              "currency": "INR",
              "value": 6092
            },
            "total_emi_amount": {
              "currency": "INR",
              "value": 18276
            },
            "interest_amount": {
              "currency": "INR",
              "value": 476
            },
            "interest_rate_percentage": 16,
            "processing_fee_details": {
              "amount": {
                "currency": "INR",
                "value": 29900
              }
            },
            "emi_type": "STANDARD"
          }
        }
      }
    }
  ]
}
```
```json Sample Response
{
  "data": {
    "order_id": "v1-250124055307-aa-6OZ8sm",
    "merchant_order_reference": "53cf1451-4dfd-417d-a1c8-c8bd603d5200",
    "type": "CHARGE",
    "status": "PENDING",
    "challenge_url": "https://pluraluat.v2.pinepg.in/web/auth/landing/?token=S50f2FXi%2FYAGe2bLZEW%2FA2VHzXthz0m9igmtsP61ODtY5u4pR6RYB5IlJwK0%2Fuo%2FBs9",
    "merchant_id": "111163",
    "order_amount": {
      "value": 1600000,
      "currency": "INR"
    },
    "pre_auth": false,
    "allowed_payment_methods": [],
    "purchase_details": {
      "customer": {
        "country_code": "91",
        "billing_address": {},
        "shipping_address": {},
        "is_edit_customer_details_allowed": false
      }
    },
    "payments": [
      {
        "id": "v1-250124055307-aa-6OZ8sm-ce-a",
        "merchant_payment_reference": "c7a7f778-b68f-462b-a6af-50698df12a4a",
        "status": "FAILED",
        "payment_amount": {
          "value": 1550000,
          "currency": "INR"
        },
        "payment_method": "CREDIT_EMI",
        "offer_data": {
          "offer_details": {
            "id": "6",
            "name": "HDFC CC",
            "issuer_type": "CC_BANK",
            "priority": 1,
            "tenure": {
              "tenure_id": "1",
              "name": "3 Months",
              "tenure_type": "MONTH",
              "tenure_value": 3,
              "issuer_offer_parameters": [
                {
                  "program_type": "BANK_EMI",
                  "offer_id": "1803",
                  "offer_parameter_id": "72559"
                },
                {
                  "program_type": "MERCHANT_BANK_OFFER",
                  "offer_id": "1523",
                  "offer_parameter_id": "63566"
                }
              ],
              "details": [],
              "discount": {
                "discount_type": "INSTANT",
                "amount": {
                  "currency": "INR",
                  "value": 50000
                },
                "breakup": {
                  "merchant": {},
                  "issuer": {},
                  "brand": {},
                  "dealer": {}
                }
              },
              "loan_amount": {
                "currency": "INR",
                "value": 1550000
              },
              "total_discount_amount": {
                "currency": "INR",
                "value": 50000
              },
              "net_payment_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "monthly_emi_amount": {
                "currency": "INR",
                "value": 533984
              },
              "total_emi_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "interest_amount": {
                "currency": "INR",
                "value": 51952
              },
              "interest_rate_percentage": 20,
              "processing_fee_details": {
                "amount": {
                  "currency": "INR",
                  "value": 19900
                }
              },
              "processing_fee_amount": {
                "currency": "INR",
                "value": 19900
              },
              "emi_type": "STANDARD"
            }
          }
        },
        "error_detail": {
          "code": "INTERNAL_ERROR",
          "message": "Payment processor is unavailable"
        },
        "created_at": "2025-01-24T05:53:24.476Z",
        "updated_at": "2025-01-24T05:53:25.492Z"
      },
      {
        "id": "v1-250124055307-aa-6OZ8sm-ce-b",
        "merchant_payment_reference": "32e3ba62-bb95-41bb-be81-1b87ab96c0ed",
        "status": "PENDING",
        "payment_amount": {
          "value": 1550000,
          "currency": "INR"
        },
        "payment_method": "CREDIT_EMI",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "INTL HDQTRS-CENTER OWNED",
            "card_category": "Consumer",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN",
            "save": false
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "",
          "rrn": "",
          "is_aggregator": true
        },
        "offer_data": {
          "offer_details": {
            "id": "6",
            "name": "HDFC CC",
            "issuer_type": "CC_BANK",
            "priority": 1,
            "tenure": {
              "tenure_id": "1",
              "name": "3 Months",
              "tenure_type": "MONTH",
              "tenure_value": 3,
              "issuer_offer_parameters": [
                {
                  "program_type": "BANK_EMI",
                  "offer_id": "1803",
                  "offer_parameter_id": "72559"
                },
                {
                  "program_type": "MERCHANT_BANK_OFFER",
                  "offer_id": "1523",
                  "offer_parameter_id": "63566"
                }
              ],
              "details": [],
              "discount": {
                "discount_type": "INSTANT",
                "amount": {
                  "currency": "INR",
                  "value": 50000
                },
                "breakup": {
                  "merchant": {},
                  "issuer": {},
                  "brand": {},
                  "dealer": {}
                }
              },
              "loan_amount": {
                "currency": "INR",
                "value": 1550000
              },
              "total_discount_amount": {
                "currency": "INR",
                "value": 50000
              },
              "net_payment_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "monthly_emi_amount": {
                "currency": "INR",
                "value": 533984
              },
              "total_emi_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "interest_amount": {
                "currency": "INR",
                "value": 51952
              },
              "interest_rate_percentage": 20,
              "processing_fee_details": {
                "amount": {
                  "currency": "INR",
                  "value": 19900
                }
              },
              "processing_fee_amount": {
                "currency": "INR",
                "value": 19900
              },
              "emi_type": "STANDARD"
            }
          }
        },
        "created_at": "2025-01-24T05:53:58.092Z",
        "updated_at": "2025-01-24T05:53:59.679Z"
      }
    ],
    "created_at": "2025-01-24T05:53:07.740Z",
    "updated_at": "2025-01-24T05:53:59.680Z",
    "integration_mode": "SEAMLESS",
    "payment_retries_remaining": 8
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/reference/affordability-suite-create-payment" target="_blank">Create Payment API</a> documentation to learn more.

## 6. Handle Payment

In create payment API response we return a `challenge_url`, use this challenge url to navigate your customers to the checkout page to accept payment.

### 6.1 Store Payment Details on Your Server

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

> 📘 Important:
> 
> - With pre-authorization set to true, you can capture or cancel a payment for an order.

## 7. Get Order by Order ID

Use this API to retrieve the order by order ID.

Use the below endpoint to capture the payment against the order.

```text Get Order by Order ID Endpoint for UAT
GET: https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}
```
```text Get Order by Order ID Endpoint for PROD
GET: https://api.pluralpay.in/api/pay/v1/orders/{order_id}
```

Shown below is a sample request and sample response for a Get Order by Order ID API.

```json Sample Response
{
  "data": {
    "order_id": "v1-250124055307-aa-6OZ8sm",
    "merchant_order_reference": "53cf1451-4dfd-417d-a1c8-c8bd603d5200",
    "type": "CHARGE",
    "status": "PENDING",
    "challenge_url": "https://pluraluat.v2.pinepg.in/web/auth/landing/?token=S50f2FXi%2FYAGe2bLZEW%2FA2VHzXthz0m9igmtsP61ODtY5u4pR6RYB5IlJwK0%2Fuo%2FBs9",
    "merchant_id": "111163",
    "order_amount": {
      "value": 1600000,
      "currency": "INR"
    },
    "pre_auth": false,
    "allowed_payment_methods": [],
    "purchase_details": {
      "customer": {
        "country_code": "91",
        "billing_address": {},
        "shipping_address": {},
        "is_edit_customer_details_allowed": false
      }
    },
    "payments": [
      {
        "id": "v1-250124055307-aa-6OZ8sm-ce-a",
        "merchant_payment_reference": "c7a7f778-b68f-462b-a6af-50698df12a4a",
        "status": "FAILED",
        "payment_amount": {
          "value": 1550000,
          "currency": "INR"
        },
        "payment_method": "CREDIT_EMI",
        "offer_data": {
          "offer_details": {
            "id": "6",
            "name": "HDFC CC",
            "issuer_type": "CC_BANK",
            "priority": 1,
            "tenure": {
              "tenure_id": "1",
              "name": "3 Months",
              "tenure_type": "MONTH",
              "tenure_value": 3,
              "issuer_offer_parameters": [
                {
                  "program_type": "BANK_EMI",
                  "offer_id": "1803",
                  "offer_parameter_id": "72559"
                },
                {
                  "program_type": "MERCHANT_BANK_OFFER",
                  "offer_id": "1523",
                  "offer_parameter_id": "63566"
                }
              ],
              "details": [],
              "discount": {
                "discount_type": "INSTANT",
                "amount": {
                  "currency": "INR",
                  "value": 50000
                },
                "breakup": {
                  "merchant": {},
                  "issuer": {},
                  "brand": {},
                  "dealer": {}
                }
              },
              "loan_amount": {
                "currency": "INR",
                "value": 1550000
              },
              "total_discount_amount": {
                "currency": "INR",
                "value": 50000
              },
              "net_payment_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "monthly_emi_amount": {
                "currency": "INR",
                "value": 533984
              },
              "total_emi_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "interest_amount": {
                "currency": "INR",
                "value": 51952
              },
              "interest_rate_percentage": 20,
              "processing_fee_details": {
                "amount": {
                  "currency": "INR",
                  "value": 19900
                }
              },
              "processing_fee_amount": {
                "currency": "INR",
                "value": 19900
              },
              "emi_type": "STANDARD"
            }
          }
        },
        "error_detail": {
          "code": "INTERNAL_ERROR",
          "message": "Payment processor is unavailable"
        },
        "created_at": "2025-01-24T05:53:24.476Z",
        "updated_at": "2025-01-24T05:53:25.492Z"
      },
      {
        "id": "v1-250124055307-aa-6OZ8sm-ce-b",
        "merchant_payment_reference": "32e3ba62-bb95-41bb-be81-1b87ab96c0ed",
        "status": "PENDING",
        "payment_amount": {
          "value": 1550000,
          "currency": "INR"
        },
        "payment_method": "CREDIT_EMI",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "INTL HDQTRS-CENTER OWNED",
            "card_category": "Consumer",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN",
            "save": false
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "",
          "rrn": "",
          "is_aggregator": true
        },
        "offer_data": {
          "offer_details": {
            "id": "6",
            "name": "HDFC CC",
            "issuer_type": "CC_BANK",
            "priority": 1,
            "tenure": {
              "tenure_id": "1",
              "name": "3 Months",
              "tenure_type": "MONTH",
              "tenure_value": 3,
              "issuer_offer_parameters": [
                {
                  "program_type": "BANK_EMI",
                  "offer_id": "1803",
                  "offer_parameter_id": "72559"
                },
                {
                  "program_type": "MERCHANT_BANK_OFFER",
                  "offer_id": "1523",
                  "offer_parameter_id": "63566"
                }
              ],
              "details": [],
              "discount": {
                "discount_type": "INSTANT",
                "amount": {
                  "currency": "INR",
                  "value": 50000
                },
                "breakup": {
                  "merchant": {},
                  "issuer": {},
                  "brand": {},
                  "dealer": {}
                }
              },
              "loan_amount": {
                "currency": "INR",
                "value": 1550000
              },
              "total_discount_amount": {
                "currency": "INR",
                "value": 50000
              },
              "net_payment_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "monthly_emi_amount": {
                "currency": "INR",
                "value": 533984
              },
              "total_emi_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "interest_amount": {
                "currency": "INR",
                "value": 51952
              },
              "interest_rate_percentage": 20,
              "processing_fee_details": {
                "amount": {
                  "currency": "INR",
                  "value": 19900
                }
              },
              "processing_fee_amount": {
                "currency": "INR",
                "value": 19900
              },
              "emi_type": "STANDARD"
            }
          }
        },
        "created_at": "2025-01-24T05:53:58.092Z",
        "updated_at": "2025-01-24T05:53:59.679Z"
      }
    ],
    "created_at": "2025-01-24T05:53:07.740Z",
    "updated_at": "2025-01-24T05:53:59.680Z",
    "integration_mode": "SEAMLESS",
    "payment_retries_remaining": 8
  }
}
```

Refer to our <a style="text-decoration:none;" href="https://developer.pluralonline.com/reference/orders-get-by-order-id" target="_blank">Get Order by Order ID API</a> documentation to learn more.

### To Know Your Payment Status

To check your payment status, you can either rely on Webhook events or use our **Get Orders** APIs for real-time updates.

1. **Webhook Notification**: We send Webhook notifications on the successful payment or any changes to the payments object. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/developer-tools-webhook" target="_blank">Webhooks</a> documentation to learn more.
2. **Get Orders API**: Use our Get Orders API to know the real time status of the payment. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/order-manage#3-get-order-by-order-id" target="_blank">Manage Orders</a> documentation to learn more.

### Refunds

Plural processes refund directly to the customer's original payment method to prevent chargebacks.

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/payment-refund" target="_blank">Refunds</a> documentation to learn more.

## Pre Authorization Flow - Credit EMI

In our orders API, we provide pre-authorization as an option. With pre-authorization set to true, you can capture payment for an order after successful delivery.

When pre-auth is set to true, and the payment is successfully created, you have the following options:

**Capture Order**: Utilize the plural capture order API in your backend to capture the payment against an order.

**Cancel Order**: Use the plural cancel order API in your backend to cancel the payment against an order.

> 📘 Note:
> 
> - On successful payment we send the webhook event `ORDER_AUTHORIZED` and the status of the payment is updated to `authorized`.
> - You can capture or cancel an order only when the order status is `authorized`.

### 1. Capture Order

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
  "merchant_capture_reference": "merchant-capture-ref-r4y",
  "capture_amount": {
    "value": 1600000,
    "currency": "INR"
  }
}
```
```json Sample Response
{
  "data": {
    "order_id": "v1-250124055307-aa-6OZ8sm",
    "merchant_order_reference": "53cf1451-4dfd-417d-a1c8-c8bd603d5200",
    "type": "CHARGE",
    "status": "PROCESSED",
    "challenge_url": "https://pluraluat.v2.pinepg.in/web/auth/landing/?token=S50f2FXi%2FYAGe2bLZEW%2FA2VHzXthz0m9igmtsP61ODtY5u4pR6RYB5IlJwK0%2Fuo%2FBs9",
    "merchant_id": "111163",
    "order_amount": {
      "value": 1600000,
      "currency": "INR"
    },
    "pre_auth": false,
    "allowed_payment_methods": [],
    "purchase_details": {
      "customer": {
        "country_code": "91",
        "billing_address": {},
        "shipping_address": {},
        "is_edit_customer_details_allowed": false
      }
    },
    "payments": [
      {
        "id": "v1-250124055307-aa-6OZ8sm-ce-a",
        "merchant_payment_reference": "c7a7f778-b68f-462b-a6af-50698df12a4a",
        "status": "FAILED",
        "payment_amount": {
          "value": 1550000,
          "currency": "INR"
        },
        "payment_method": "CREDIT_EMI",
        "offer_data": {
          "offer_details": {
            "id": "6",
            "name": "HDFC CC",
            "issuer_type": "CC_BANK",
            "priority": 1,
            "tenure": {
              "tenure_id": "1",
              "name": "3 Months",
              "tenure_type": "MONTH",
              "tenure_value": 3,
              "issuer_offer_parameters": [
                {
                  "program_type": "BANK_EMI",
                  "offer_id": "1803",
                  "offer_parameter_id": "72559"
                },
                {
                  "program_type": "MERCHANT_BANK_OFFER",
                  "offer_id": "1523",
                  "offer_parameter_id": "63566"
                }
              ],
              "details": [],
              "discount": {
                "discount_type": "INSTANT",
                "amount": {
                  "currency": "INR",
                  "value": 50000
                },
                "breakup": {
                  "merchant": {},
                  "issuer": {},
                  "brand": {},
                  "dealer": {}
                }
              },
              "loan_amount": {
                "currency": "INR",
                "value": 1550000
              },
              "total_discount_amount": {
                "currency": "INR",
                "value": 50000
              },
              "net_payment_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "monthly_emi_amount": {
                "currency": "INR",
                "value": 533984
              },
              "total_emi_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "interest_amount": {
                "currency": "INR",
                "value": 51952
              },
              "interest_rate_percentage": 20,
              "processing_fee_details": {
                "amount": {
                  "currency": "INR",
                  "value": 19900
                }
              },
              "processing_fee_amount": {
                "currency": "INR",
                "value": 19900
              },
              "emi_type": "STANDARD"
            }
          }
        },
        "error_detail": {
          "code": "INTERNAL_ERROR",
          "message": "Payment processor is unavailable"
        },
        "created_at": "2025-01-24T05:53:24.476Z",
        "updated_at": "2025-01-24T05:53:25.492Z"
      },
      {
        "id": "v1-250124055307-aa-6OZ8sm-ce-b",
        "merchant_payment_reference": "32e3ba62-bb95-41bb-be81-1b87ab96c0ed",
        "status": "PENDING",
        "payment_amount": {
          "value": 1550000,
          "currency": "INR"
        },
        "payment_method": "CREDIT_EMI",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "INTL HDQTRS-CENTER OWNED",
            "card_category": "Consumer",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN",
            "save": false
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "",
          "rrn": "",
          "is_aggregator": true
        },
        "offer_data": {
          "offer_details": {
            "id": "6",
            "name": "HDFC CC",
            "issuer_type": "CC_BANK",
            "priority": 1,
            "tenure": {
              "tenure_id": "1",
              "name": "3 Months",
              "tenure_type": "MONTH",
              "tenure_value": 3,
              "issuer_offer_parameters": [
                {
                  "program_type": "BANK_EMI",
                  "offer_id": "1803",
                  "offer_parameter_id": "72559"
                },
                {
                  "program_type": "MERCHANT_BANK_OFFER",
                  "offer_id": "1523",
                  "offer_parameter_id": "63566"
                }
              ],
              "details": [],
              "discount": {
                "discount_type": "INSTANT",
                "amount": {
                  "currency": "INR",
                  "value": 50000
                },
                "breakup": {
                  "merchant": {},
                  "issuer": {},
                  "brand": {},
                  "dealer": {}
                }
              },
              "loan_amount": {
                "currency": "INR",
                "value": 1550000
              },
              "total_discount_amount": {
                "currency": "INR",
                "value": 50000
              },
              "net_payment_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "monthly_emi_amount": {
                "currency": "INR",
                "value": 533984
              },
              "total_emi_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "interest_amount": {
                "currency": "INR",
                "value": 51952
              },
              "interest_rate_percentage": 20,
              "processing_fee_details": {
                "amount": {
                  "currency": "INR",
                  "value": 19900
                }
              },
              "processing_fee_amount": {
                "currency": "INR",
                "value": 19900
              },
              "emi_type": "STANDARD"
            }
          }
        },
        "created_at": "2025-01-24T05:53:58.092Z",
        "updated_at": "2025-01-24T05:53:59.679Z"
      }
    ],
    "created_at": "2025-01-24T05:53:07.740Z",
    "updated_at": "2025-01-24T05:53:59.680Z",
    "integration_mode": "SEAMLESS",
    "payment_retries_remaining": 8
  }
}
```

Refer to our <a style="text-decoration:none;" href="https://developer.pluralonline.com/v3.0/reference/orders-capture" target="_blank">Capture Order API</a> documentation to learn more.

### 2. Cancel Order

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
    "order_id": "v1-250124055307-aa-6OZ8sm",
    "merchant_order_reference": "53cf1451-4dfd-417d-a1c8-c8bd603d5200",
    "type": "CHARGE",
    "status": "CANCELLED",
    "challenge_url": "https://pluraluat.v2.pinepg.in/web/auth/landing/?token=S50f2FXi%2FYAGe2bLZEW%2FA2VHzXthz0m9igmtsP61ODtY5u4pR6RYB5IlJwK0%2Fuo%2FBs9",
    "merchant_id": "111163",
    "order_amount": {
      "value": 1600000,
      "currency": "INR"
    },
    "pre_auth": false,
    "allowed_payment_methods": [],
    "purchase_details": {
      "customer": {
        "country_code": "91",
        "billing_address": {},
        "shipping_address": {},
        "is_edit_customer_details_allowed": false
      }
    },
    "payments": [
      {
        "id": "v1-250124055307-aa-6OZ8sm-ce-a",
        "merchant_payment_reference": "c7a7f778-b68f-462b-a6af-50698df12a4a",
        "status": "FAILED",
        "payment_amount": {
          "value": 1550000,
          "currency": "INR"
        },
        "payment_method": "CREDIT_EMI",
        "offer_data": {
          "offer_details": {
            "id": "6",
            "name": "HDFC CC",
            "issuer_type": "CC_BANK",
            "priority": 1,
            "tenure": {
              "tenure_id": "1",
              "name": "3 Months",
              "tenure_type": "MONTH",
              "tenure_value": 3,
              "issuer_offer_parameters": [
                {
                  "program_type": "BANK_EMI",
                  "offer_id": "1803",
                  "offer_parameter_id": "72559"
                },
                {
                  "program_type": "MERCHANT_BANK_OFFER",
                  "offer_id": "1523",
                  "offer_parameter_id": "63566"
                }
              ],
              "details": [],
              "discount": {
                "discount_type": "INSTANT",
                "amount": {
                  "currency": "INR",
                  "value": 50000
                },
                "breakup": {
                  "merchant": {},
                  "issuer": {},
                  "brand": {},
                  "dealer": {}
                }
              },
              "loan_amount": {
                "currency": "INR",
                "value": 1550000
              },
              "total_discount_amount": {
                "currency": "INR",
                "value": 50000
              },
              "net_payment_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "monthly_emi_amount": {
                "currency": "INR",
                "value": 533984
              },
              "total_emi_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "interest_amount": {
                "currency": "INR",
                "value": 51952
              },
              "interest_rate_percentage": 20,
              "processing_fee_details": {
                "amount": {
                  "currency": "INR",
                  "value": 19900
                }
              },
              "processing_fee_amount": {
                "currency": "INR",
                "value": 19900
              },
              "emi_type": "STANDARD"
            }
          }
        },
        "error_detail": {
          "code": "INTERNAL_ERROR",
          "message": "Payment processor is unavailable"
        },
        "created_at": "2025-01-24T05:53:24.476Z",
        "updated_at": "2025-01-24T05:53:25.492Z"
      },
      {
        "id": "v1-250124055307-aa-6OZ8sm-ce-b",
        "merchant_payment_reference": "32e3ba62-bb95-41bb-be81-1b87ab96c0ed",
        "status": "PENDING",
        "payment_amount": {
          "value": 1550000,
          "currency": "INR"
        },
        "payment_method": "CREDIT_EMI",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "INTL HDQTRS-CENTER OWNED",
            "card_category": "Consumer",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN",
            "save": false
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "",
          "rrn": "",
          "is_aggregator": true
        },
        "offer_data": {
          "offer_details": {
            "id": "6",
            "name": "HDFC CC",
            "issuer_type": "CC_BANK",
            "priority": 1,
            "tenure": {
              "tenure_id": "1",
              "name": "3 Months",
              "tenure_type": "MONTH",
              "tenure_value": 3,
              "issuer_offer_parameters": [
                {
                  "program_type": "BANK_EMI",
                  "offer_id": "1803",
                  "offer_parameter_id": "72559"
                },
                {
                  "program_type": "MERCHANT_BANK_OFFER",
                  "offer_id": "1523",
                  "offer_parameter_id": "63566"
                }
              ],
              "details": [],
              "discount": {
                "discount_type": "INSTANT",
                "amount": {
                  "currency": "INR",
                  "value": 50000
                },
                "breakup": {
                  "merchant": {},
                  "issuer": {},
                  "brand": {},
                  "dealer": {}
                }
              },
              "loan_amount": {
                "currency": "INR",
                "value": 1550000
              },
              "total_discount_amount": {
                "currency": "INR",
                "value": 50000
              },
              "net_payment_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "monthly_emi_amount": {
                "currency": "INR",
                "value": 533984
              },
              "total_emi_amount": {
                "currency": "INR",
                "value": 1601952
              },
              "interest_amount": {
                "currency": "INR",
                "value": 51952
              },
              "interest_rate_percentage": 20,
              "processing_fee_details": {
                "amount": {
                  "currency": "INR",
                  "value": 19900
                }
              },
              "processing_fee_amount": {
                "currency": "INR",
                "value": 19900
              },
              "emi_type": "STANDARD"
            }
          }
        },
        "created_at": "2025-01-24T05:53:58.092Z",
        "updated_at": "2025-01-24T05:53:59.679Z"
      }
    ],
    "created_at": "2025-01-24T05:53:07.740Z",
    "updated_at": "2025-01-24T05:53:59.680Z",
    "integration_mode": "SEAMLESS",
    "payment_retries_remaining": 8
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/v3.0/reference/orders-cancel" target="_blank">Cancel Order API</a> documentation to learn more.
