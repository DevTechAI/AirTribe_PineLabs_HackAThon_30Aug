---
title: "Integration Steps"
slug: "emi-integration-steps"
excerpt: "Learn how to integrate Plural EMI APIs in your application, enabling your customers to make payments using EMI options."
hidden: false
createdAt: "Mon Nov 25 2024 10:31:41 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Apr 21 2025 06:30:46 GMT+0000 (Coordinated Universal Time)"
---
Follow the below steps to integrate with Plural EMI APIs to enable your customers to make payments using EMI.

1. <a href="https://developer.pluralonline.com/v2.0/docs/emi-integration-steps#1-emi-calculator" >EMI Calculator</a>
2. <a href="https://developer.pluralonline.com/v2.0/docs/emi-integration-steps#2-scheme-validation" >Scheme Validation</a>
3. <a href="https://developer.pluralonline.com/v2.0/docs/emi-integration-steps#3-accept-payment-api" >Accept Payment</a>
   1. <a href="https://developer.pluralonline.com/v2.0/docs/emi-integration-steps#31-prerequisite" >Prerequisite</a>
      1. <a href="https://developer.pluralonline.com/v2.0/docs/emi-integration-steps#311-enter-payment-details" >Enter Payment Details</a>
      2. <a href="https://developer.pluralonline.com/v2.0/docs/emi-integration-steps#312-encode-json" >Encode JSON</a>
      3. <a href="https://developer.pluralonline.com/v2.0/docs/emi-integration-steps#313-hashmap" >HashMap</a>
4. <a href="https://developer.pluralonline.com/v2.0/docs/emi-integration-steps#4-process-payment" >Process Payment</a>

> 📘 Note:
> 
> **Handle Payment**: After generating the URL, Use this Link to navigate your customer's to their mobile apps. You can do this by rendering the URL returned by Plural as a button or a link for the customer to use.

## 1. EMI Calculator

Use this API to calculate the monthly instalments and breakdown.

Use the below Endpoints to calculate the monthly Instalment.

```text EMI Calculator UAT Endpoint
POST: https://uat.pinepg.in/api/v3/emi/calculator
```
```Text EMI Calculator PROD Endpoint
POST: https://pinepg.in/api/v3/emi/calculator
```

Shown below are the sample request and sample response for a EMI Calculator API.

```json Multicart Sample Request
{
  "merchant_data": {
    "merchant_id": 3473,
    "merchant_access_code": "57e39383-b053-4db9-a708-26d8971886e7"
  },
  "payment_data": {
    "amount_in_paisa": 1000
  },
  "product_details": [
    {
      "product_code": "SMG975FCWG",
      "product_amount": 500
    },
    {
      "product_code": "40",
      "product_amount": 500
    }
  ]
}
```
```json Multicart Sample Response
{
  "issuer": [
    {
      "list_emi_tenure": [
        {
          "offer_scheme": {
            "product_details": [
              {
                "schemes": [
                  {
                    "scheme_id": 1682,
                    "program_type": 112,
                    "is_scheme_valid": true
                  }
                ],
                "product_code": "SMG975FCWG",
                "product_amount": 500,
                "subvention_cashback_discount": 11705,
                "product_discount": 0,
                "subvention_cashback_discount_percentage": 21500,
                "product_discount_percentage": 0,
                "subvention_type": 1
              },
              {
                "schemes": [],
                "product_code": "40",
                "product_amount": 500,
                "subvention_cashback_discount": 0,
                "product_discount": 0,
                "subvention_cashback_discount_percentage": 0,
                "product_discount_percentage": 0
              }
            ],
            "emi_scheme": {
              "scheme_id": 1683,
              "program_type": 105,
              "is_scheme_valid": true
            }
          },
          "tenure_id": "3",
          "tenure_in_month": "3",
          "monthly_installment": 370652,
          "bank_interest_rate": 130000,
          "interest_pay_to_bank": 23661,
          "total_offerred_discount_cashback_amount": 11705,
          "loan_amount": 1088295,
          "auth_amount": 1088295
        },
        {
          "offer_scheme": {
            "product_details": [
              {
                "schemes": [
                  {
                    "scheme_id": 1682,
                    "program_type": 112,
                    "is_scheme_valid": true
                  }
                ],
                "product_code": "SMG975FCWG",
                "product_amount": 500,
                "subvention_cashback_discount": 20266,
                "product_discount": 0,
                "subvention_cashback_discount_percentage": 37000,
                "product_discount_percentage": 0,
                "subvention_type": 1
              },
              {
                "schemes": [],
                "product_code": "40",
                "product_amount": 500,
                "subvention_cashback_discount": 0,
                "product_discount": 0,
                "subvention_cashback_discount_percentage": 0,
                "product_discount_percentage": 0
              }
            ],
            "emi_scheme": {
              "scheme_id": 1683,
              "program_type": 105,
              "is_scheme_valid": true
            }
          },
          "tenure_id": "6",
          "tenure_in_month": "6",
          "monthly_installment": 186840,
          "bank_interest_rate": 130000,
          "interest_pay_to_bank": 41306,
          "total_offerred_discount_cashback_amount": 20266,
          "loan_amount": 1079734,
          "auth_amount": 1079734
        },
        {
          "offer_scheme": {
            "product_details": [
              {
                "schemes": [
                  {
                    "scheme_id": 1682,
                    "program_type": 112,
                    "is_scheme_valid": true
                  }
                ],
                "product_code": "SM-G975FCWG",
                "product_amount": 500,
                "subvention_cashback_discount": 30756,
                "product_discount": 0,
                "subvention_cashback_discount_percentage": 56000,
                "product_discount_percentage": 0,
                "subvention_type": 1
              },
              {
                "schemes": [],
                "product_code": "40",
                "product_amount": 500,
                "subvention_cashback_discount": 0,
                "product_discount": 0,
                "subvention_cashback_discount_percentage": 0,
                "product_discount_percentage": 0
              }
            ],
            "emi_scheme": {
              "scheme_id": 1683,
              "program_type": 105,
              "is_scheme_valid": true
            }
          },
          "tenure_id": "9",
          "tenure_in_month": "9",
          "monthly_installment": 125841,
          "bank_interest_rate": 140000,
          "interest_pay_to_bank": 63325,
          "total_offerred_discount_cashback_amount": 30756,
          "loan_amount": 1069244,
          "auth_amount": 1069244
        },
        {
          "offer_scheme": {
            "product_details": [
              {
                "schemes": [
                  {
                    "scheme_id": 1682,
                    "program_type": 112,
                    "is_scheme_valid": true
                  }
                ],
                "product_code": "SMG975FCWG",
                "product_amount": 500,
                "subvention_cashback_discount": 39532,
                "product_discount": 0,
                "subvention_cashback_discount_percentage": 56000,
                "product_discount_percentage": 0,
                "subvention_type": 1
              },
              {
                "schemes": [],
                "product_code": "40",
                "product_amount": 500,
                "subvention_cashback_discount": 0,
                "product_discount": 0,
                "subvention_cashback_discount_percentage": 0,
                "product_discount_percentage": 0
              }
            ],
            "emi_scheme": {
              "scheme_id": 1683,
              "program_type": 105,
              "is_scheme_valid": true
            }
          },
          "tenure_id": "12",
          "tenure_in_month": "12",
          "monthly_installment": 95215,
          "bank_interest_rate": 140000,
          "interest_pay_to_bank": 82112,
          "total_offerred_discount_cashback_amount": 39532,
          "loan_amount": 1060468,
          "auth_amount": 1060468
        },
        {
          "offer_scheme": {
            "product_details": [
              {
                "schemes": [
                  {
                    "scheme_id": 1682,
                    "program_type": 112,
                    "is_scheme_valid": true
                  }
                ],
                "product_code": "SMG975FCWG",
                "product_amount": 500,
                "subvention_cashback_discount": 60209,
                "product_discount": 0,
                "subvention_cashback_discount_percentage": 0,
                "product_discount_percentage": 0,
                "subvention_type": 1
              },
              {
                "schemes": [],
                "product_code": "40",
                "product_amount": 500,
                "subvention_cashback_discount": 0,
                "product_discount": 0,
                "subvention_cashback_discount_percentage": 0,
                "product_discount_percentage": 0
              }
            ],
            "emi_scheme": {
              "scheme_id": 1683,
              "program_type": 105,
              "is_scheme_valid": true
            }
          },
          "tenure_id": "18",
          "tenure_in_month": "18",
          "monthly_installment": 64867,
          "bank_interest_rate": 150000,
          "interest_pay_to_bank": 127815,
          "total_offerred_discount_cashback_amount": 60209,
          "loan_amount": 1039791,
          "auth_amount": 1039791
        }
      ],
      "issuer_name": "HDFC",
      "is_debit_emi_issuer": false
    }
  ],
  "response_code": 1,
  "response_message": "SUCCESS"
}
```
```json Singlecart Sample Request
{
  "product_details": [
    {
      "product_code": "SMG988BZAP",
      "product_amount": 1000
    }
  ],
  "payment_data": {
    "amount_in_paisa": 1000
  },
  "merchant_data": {
    "merchant_access_code": "dsfff33-5e6e-411a-99fe-dsdsjsfff",
    "merchant_id": "10838"
  }
}
```
```json Singlecart Sample Response
{
  "issuer": [
    {
      "list_emi_tenure": [
        {
          "offer_scheme": {
            "product_details": [
              {
                "schemes": [],
                "product_code": "SMG988BZAP",
                "product_amount": 1000,
                "subvention_cashback_discount": 0,
                "product_discount": 0,
                "subvention_cashback_discount_percentage": 0,
                "product_discount_percentage": 0,
                "subvention_type": 3,
                "bank_interest_rate_percentage": 150000,
                "bank_interest_rate": 747888
              }
            ],
            "emi_scheme": {
              "scheme_id": 21878,
              "program_type": 105,
              "is_scheme_valid": true
            }
          },
          "tenure_id": "12",
          "tenure_in_month": "12",
          "monthly_installment": 812324,
          "bank_interest_rate": 150000,
          "interest_pay_to_bank": 747888,
          "total_offerred_discount_cashback_amount": 0,
          "loan_amount": 9000000,
          "auth_amount": 9000000
        },
        {
          "offer_scheme": {
            "product_details": [
              {
                "schemes": [],
                "product_code": "SMG988BZAP",
                "product_amount": 1000,
                "subvention_cashback_discount": 0,
                "product_discount": 0,
                "subvention_cashback_discount_percentage": 0,
                "product_discount_percentage": 0,
                "subvention_type": 3,
                "bank_interest_rate_percentage": 150000,
                "bank_interest_rate": 1473096
              }
            ],
            "emi_scheme": {
              "scheme_id": 21878,
              "program_type": 105,
              "is_scheme_valid": true
            }
          },
          "tenure_id": "24",
          "tenure_in_month": "24",
          "monthly_installment": 436379,
          "bank_interest_rate": 150000,
          "interest_pay_to_bank": 1473096,
          "total_offerred_discount_cashback_amount": 0,
          "loan_amount": 9000000,
          "auth_amount": 9000000
        },
        {
          "offer_scheme": {
            "product_details": [
              {
                "schemes": [],
                "product_code": "SMG988BZAP",
                "product_amount": 1000,
                "subvention_cashback_discount": 0,
                "product_discount": 0,
                "subvention_cashback_discount_percentage": 0,
                "product_discount_percentage": 0,
                "subvention_type": 3,
                "bank_interest_rate_percentage": 150000,
                "bank_interest_rate": 571806
              }
            ],
            "emi_scheme": {
              "scheme_id": 21878,
              "program_type": 105,
              "is_scheme_valid": true
            }
          },
          "tenure_id": "9",
          "tenure_in_month": "9",
          "monthly_installment": 1063534,
          "bank_interest_rate": 150000,
          "interest_pay_to_bank": 571806,
          "total_offerred_discount_cashback_amount": 0,
          "loan_amount": 9000000,
          "auth_amount": 9000000
        },
        {
          "offer_scheme": {
            "product_details": [
              {
                "schemes": [],
                "product_code": "SMG988BZAP",
                "product_amount": 1000,
                "subvention_cashback_discount": 0,
                "product_discount": 0,
                "subvention_cashback_discount_percentage": 0,
                "product_discount_percentage": 0,
                "subvention_type": 3,
                "bank_interest_rate_percentage": 150000,
                "bank_interest_rate": 397824
              }
            ],
            "emi_scheme": {
              "scheme_id": 21878,
              "program_type": 105,
              "is_scheme_valid": true
            }
          },
          "tenure_id": "6",
          "tenure_in_month": "6",
          "monthly_installment": 1566304,
          "bank_interest_rate": 150000,
          "interest_pay_to_bank": 397824,
          "total_offerred_discount_cashback_amount": 0,
          "loan_amount": 9000000,
          "auth_amount": 9000000
        },
        {
          "offer_scheme": {
            "product_details": [
              {
                "schemes": [],
                "product_code": "SMG988BZAP",
                "product_amount": 1000,
                "subvention_cashback_discount": 0,
                "product_discount": 0,
                "subvention_cashback_discount_percentage": 0,
                "product_discount_percentage": 0,
                "subvention_type": 3,
                "bank_interest_rate_percentage": 150000,
                "bank_interest_rate": 1106334
              }
            ],
            "emi_scheme": {
              "scheme_id": 21878,
              "program_type": 105,
              "is_scheme_valid": true
            }
          },
          "tenure_id": "18",
          "tenure_in_month": "18",
          "monthly_installment": 561463,
          "bank_interest_rate": 150000,
          "interest_pay_to_bank": 1106334,
          "total_offerred_discount_cashback_amount": 0,
          "loan_amount": 9000000,
          "auth_amount": 9000000
        }
      ],
      "issuer_name": "HDFC",
      "is_debit_emi_issuer": false
    }
  ],
  "response_code": 1,
  "response_message": "SUCCESS"
}
```

Refer to our <a href="https://developer.pluralonline.com/v2.0/reference/emi-calculator" target="_blank">EMI Calculator API Documentation</a> for more information.

## 2. Scheme Validation

Use this API to check the validity of the offer selected on a Card.

Use the below Endpoints to validate the offer applicable on the card.

```text Scheme Validation UAT Endpoint
POST: https://uat.pinepg.in/api/v3/scheme/validation
```
```Text Scheme Validation PROD Endpoint
POST: https://pinepg.in/api/v3/scheme/validation
```

Shown below are the sample request and sample response for a Scheme Validation API.

```json Sample Request
{
  "merchant_data": {
    "merchant_id": 3473,
    "merchant_access_code": "57e39383-b053-4db9-a708-26d8971886e7"
  },
  "payment_data": {
    "amount_in_paisa": 1000
  },
  "card_data": {
    "card_number": "4012001037141112",
    "card_expiry_year": "2020",
    "card_expiry_month": "09",
    "card_holder_name": "harsh"
  },
  "emi_data": {
    "offer_scheme": {
      "product_details": [
        {
          "schemes": [
            {
              "scheme_id": 1682,
              "program_type": 112,
              "is_scheme_valid": true
            }
          ],
          "product_code": "SMG975FCWG",
          "product_amount": 1000,
          "subvention_cashback_discount": 11705,
          "product_discount": 0,
          "subvention_cashback_discount_percentage": 21500,
          "product_discount_percentage": 0,
          "subvention_type": 1
        },
        {
          "schemes": [],
          "product_code": "40",
          "product_amount": 1000,
          "subvention_cashback_discount": 0,
          "product_discount": 0,
          "subvention_cashback_discount_percentage": 0,
          "product_discount_percentage": 0
        }
      ],
      "emi_scheme": {
        "scheme_id": 1683,
        "program_type": 105,
        "is_scheme_valid": true
      }
    },
    "tenure_id": "3",
    "tenure_in_month": "3",
    "monthly_installment": 370652,
    "bank_interest_rate": 130000,
    "interest_pay_to_bank": 23661,
    "total_offerred_discount_cashback_amount": 11705,
    "loan_amount": 1088295,
    "auth_amount": 1088295
  }
}
```
```json Sample Response
{
  "response_code": 1,
  "response_message": "SUCCESS"
}
```

Refer to our <a href="https://developer.pluralonline.com/v2.0/reference/emi-schme-validation" target="_blank">Scheme Validation API Documentation</a> for more information.

## 3. Accept Payment API

Use this API to generate a token against a payment. Before initiating the API as a prerequisite you must encode the JSON to a Base64 and generate an HashMap to authenticate the API.

### 3.1. Prerequisite

#### 3.1.1. Enter Payment Details

Use the below JSON to enter the payment Details. You are required to enter the `merchant_data` and `payment_data` child object.

```json JSON Singlecart
{
  "merchant_data": {
    "merchant_id": 12345678,
    "merchant_access_code": "4a8c422e-928d-4f84-bfe8-27a09af66647",
    "unique_merchant_txn_id": "XYZ123",
    "merchant_return_url": "https://www.pinelabs.com"
  },
  "payment_data": {
    "amount_in_paisa": 800
  },
  "txn_data": {
    "navigation_mode": "7",
    "payment_mode": "10",
    "transaction_type": "1",
    "time_stamp": 157588000000
  },
  "product_details": {
    "product_code": "7803",
    "product_amount": "1000"
  }
}
```
```json JSON Multicart
{
  "merchant_data": {
    "merchant_id": 12345678,
    "merchant_access_code": "4a8c422e-928d-4f84-bfe8-27a09af66647",
    "unique_merchant_txn_id": "XYZ123",
    "merchant_return_url": "https://www.pinelabs.com"
  },
  "payment_data": {
    "amount_in_paisa": 2000
  },
  "txn_data": {
    "navigation_mode": "7",
    "payment_mode": "10",
    "transaction_type": "1",
    "time_stamp": 157588000000
  },
  "product_details": [
    {
      "product_code": "7803",
      "product_amount": "1000"
    },
    {
      "product_code": "7806",
      "product_amount": "1000"
    }
  ]
}
```

##### JSON Parameters

<details>

<summary>Click Here</summary>

The table below lists the various JSON parameters.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "merchant_data",
    "0-1": "`object`",
    "0-2": "`M`",
    "0-3": "An object that contains the merchant details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/prerequisite#merchant-data-child-object\" target =\"_blank\">Learn more about our `merchant_data` child object</a>.",
    "1-0": "payment_data",
    "1-1": "`object`",
    "1-2": "`M`",
    "1-3": "An object that contains the payment details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/prerequisite#payment-data-child-object\" target =\"_blank\">Learn more about our `payment_data` child object</a>.",
    "2-0": "txn_data",
    "2-1": "`object`",
    "2-2": "`M`",
    "2-3": "An object that contains the transaction details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/prerequisite#txn-data-child-object\" target =\"_blank\">Learn more about our `txn_data` child object</a>.",
    "3-0": "customer_data",
    "3-1": "`object`",
    "3-2": "`O`",
    "3-3": "An object that contains the customer details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/prerequisite#customer-data-child-object\" target =\"_blank\">Learn more about our `customer_data` child object</a>.",
    "4-0": "udf_data",
    "4-1": "`object`",
    "4-2": "`O`",
    "4-3": "An object that contains the user defined details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/prerequisite#udf-data-child-object\" target =\"_blank\">Learn more about our `merchant_data` child object</a>.",
    "5-0": "`product_details`",
    "5-1": "`array of object`",
    "5-2": "`O`",
    "5-3": "An object that contains the array of product details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/prerequisite#product-details-child-object\" target =\"_blank\">Learn more about our `merchant_data` child object</a>."
  },
  "cols": 4,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Merchant Data [Child Object]

The table below lists the various parameters in the `merchant_data` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "merchant_id",
    "0-1": "`integer`",
    "0-2": "`M`",
    "0-3": "Unique identifier of the merchant in the Plural database.  \n  \nExample: `123456`",
    "1-0": "merchant_access_code",
    "1-1": "`string`",
    "1-2": "`M`",
    "1-3": "Unique merchant access code provided by Plural.  \n  \nExample: `4a8c422e-928d-4f84-bfe8-27a09af66647`",
    "2-0": "unique_merchant_txn_id",
    "2-1": "`string`",
    "2-2": "`M`",
    "2-3": "Unique identifier of the specific transaction.  \n  \nExample: `xyz123`",
    "3-0": "merchant_return_url",
    "3-1": "`string`",
    "3-2": "`M`",
    "3-3": "Merchant return URL.  \n  \nExample: `https://www.pinelabs.com`  \n  \n**Note**: Your customer's are redirected to this page after a successful payment."
  },
  "cols": 4,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 Note:
> 
> - Contact our <a href="mailto:pgsupport@pinelabs.com" target="_blank">support team</a> to know your `merchant_id` and `merchant_access_code`. Additionally you are required to whitelist your `merchant_return_url` and get enabled with payment modes as required.

##### Payment Data [Child Object]

The table below lists the various parameters in the `payment_data` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "amount_in_paisa",
    "0-1": "`integer`",
    "0-2": "`M`",
    "0-3": "The transaction amount in paisa.  \n  \nExample: `800`"
  },
  "cols": 4,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Txn Data [Child Object]

The table below lists the various parameters in the `transaction_data` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "navigation_mode",
    "0-1": "`integer`",
    "0-2": "`M`",
    "0-3": "Checkout navigation mode.  \n  \nExample: `7`  \n  \nAccepted values:<ul><li>`2`: For Redirect Checkout.</li><li>`7`: For Seamless Checkout.</ul></li>  \n  \n**Note**: Currently TPV is available through Seamless checkout only.",
    "1-0": "payment_mode",
    "1-1": "`string`",
    "1-2": "`M`",
    "1-3": "The payment mode you prefer to accept payment.  \n  \nAccepted values: <ul><li>`1`: For CREDIT/DEBIT CARD.</ul></li>",
    "2-0": "transaction_type",
    "2-1": "`integer`",
    "2-2": "`M`",
    "2-3": "The type of transaction.  \n  \nExample: `1`  \n  \nAccepted values: <ul><li>`1`: For Purchase.</ul></li>",
    "3-0": "time_stamp",
    "3-1": "`integer`",
    "3-2": "`O`",
    "3-3": "Unix timestamp.  \n  \nExample: `157588000000`"
  },
  "cols": 4,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Customer Data [Child Object]

The table below lists the various parameters in the `customer_data` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "email_id",
    "0-1": "`string`",
    "0-2": "`O`",
    "0-3": "Customer's email address.  \n  \nExample: `kevin.bob@example.com`",
    "1-0": "first_name",
    "1-1": "`string`",
    "1-2": "`O`",
    "1-3": "Customer's first name.  \n  \nExample: `Kevin`",
    "2-0": "last_name",
    "2-1": "`string`",
    "2-2": "`O`",
    "2-3": "Customer's last name.  \n  \nExample: `Bob`",
    "3-0": "customer_id",
    "3-1": "`string`",
    "3-2": "`O`",
    "3-3": "Unique identifier of the customer.  \n  \nExample: `123456`",
    "4-0": "mobile_no",
    "4-1": "`string`",
    "4-2": "`O`",
    "4-3": "Customer's mobile number.  \n  \nExample: `9876543210`",
    "5-0": "billing_data",
    "5-1": "`object`",
    "5-2": "`O`",
    "5-3": "An object that contains the billing details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/prerequisite#billing-data-child-object\" target =\"_blank\">Learn more about our `merchant_data` child object</a>.",
    "6-0": "shipping_data",
    "6-1": "`object`",
    "6-2": "`O`",
    "6-3": "An object that contains the shipping details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/prerequisite#shipping-data-child-object\" target =\"_blank\">Learn more about our `merchant_data` child object</a>."
  },
  "cols": 4,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Billing Data [Child Object]

The table below lists the various parameters in the `billing_data` child object. This is part of the `customer_data` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "address1",
    "0-1": "`string`",
    "0-2": "`O`",
    "0-3": "Customer's billing address1.  \n  \nExample: `No 10 Church street Bangalore`",
    "1-0": "address2",
    "1-1": "`string`",
    "1-2": "`O`",
    "1-3": "Customer's billing address2.  \n  \nExample: `No 10 Brigade road Bangalore`",
    "2-0": "address3",
    "2-1": "`string`",
    "2-2": "`O`",
    "2-3": "Customer's billing address3.  \n  \nExample: `No 10 M G road Bangalore`",
    "3-0": "pincode",
    "3-1": "`string`",
    "3-2": "`O`",
    "3-3": "PIncode of the billing address.  \n  \nExample: `560001`",
    "4-0": "city",
    "4-1": "`string`",
    "4-2": "`O`",
    "4-3": "City of the billing address.  \n  \nExample: `Bangalore`",
    "5-0": "state",
    "5-1": "`string`",
    "5-2": "`O`",
    "5-3": "State of the billing address.  \n  \nExample: `Karanataka`",
    "6-0": "country",
    "6-1": "`string`",
    "6-2": "`O`",
    "6-3": "Country of the billing address.  \n  \nExample: `India`"
  },
  "cols": 4,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Shipping Data [Child Object]

The table below lists the various parameters in the `shipping_data` child object. This is part of the `customer_data` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "address1",
    "0-1": "`string`",
    "0-2": "`O`",
    "0-3": "Customer's shipping address1.  \n  \nExample: `No 10 Church street Bangalore`",
    "1-0": "address2",
    "1-1": "`string`",
    "1-2": "`O`",
    "1-3": "Customer's shipping address2.  \n  \nExample: `No 10 Brigade road Bangalore`",
    "2-0": "address3",
    "2-1": "`string`",
    "2-2": "`O`",
    "2-3": "Customer's shipping address3.  \n  \nExample: `No 10 M G road Bangalore`",
    "3-0": "pincode",
    "3-1": "`string`",
    "3-2": "`O`",
    "3-3": "PIncode of the shipping address.  \n  \nExample: `560001`",
    "4-0": "city",
    "4-1": "`string`",
    "4-2": "`O`",
    "4-3": "City of the shipping address.  \n  \nExample: `Bangalore`",
    "5-0": "state",
    "5-1": "`string`",
    "5-2": "`O`",
    "5-3": "State of the shipping address.  \n  \nExample: `Karanataka`",
    "6-0": "country",
    "6-1": "`string`",
    "6-2": "`O`",
    "6-3": "Country of the shipping address.  \n  \nExample: `India`"
  },
  "cols": 4,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Udf Data [Child Object]

The table below lists the various parameters in the `udf_data` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "udf_field_1",
    "0-1": "`string`",
    "0-2": "`O`",
    "0-3": "User defined value1.  \n  \nExample: `DD`",
    "1-0": "udf_field_2",
    "1-1": "`string`",
    "1-2": "`O`",
    "1-3": "User defined value2  \n  \nExample: `XOF`",
    "2-0": "udf_field_3",
    "2-1": "`string`",
    "2-2": "`O`",
    "2-3": "User defined value3.  \n  \nExample: `XOA`",
    "3-0": "udf_field_4",
    "3-1": "`string`",
    "3-2": "`O`",
    "3-3": "User defined value4.  \n  \nExample: `ASDF`"
  },
  "cols": 4,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Product Details [Child Object]

The table below lists the various parameters in the `product_details` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "product_code",
    "0-1": "`string`",
    "0-2": "`M`",
    "0-3": "The product code.  \n  \nExample: `7803`",
    "1-0": "product_amount",
    "1-1": "`string`",
    "1-2": "`M`",
    "1-3": "The product amount.  \n  \nExample: `10000`"
  },
  "cols": 4,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 Note:
> 
> - The sum of all the products `product_amount` must be equal to the total cart value `payment_data.amount_in_paisa`.

</details>

#### 3.1.2. Encode JSON

Convert the updated JSON to a Base64 Encode. Use the below sample code to handle the conversion of the JSON to a Base64 Encode.

```java Java
import java.util.Base64;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.stream.Collectors;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class SignatureGenerator {
  private static Map < String, Object > clean(Map < String, Object > arr) {
    return arr.entrySet().stream()
      .filter(entry -> entry.getValue() != null && !entry.getValue().toString().isEmpty())
      .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
  }
  public static void main(String[] args) {
    Map < String, Object > requestBody = new LinkedHashMap < > ();
    Map < String, Object > merchant_data = new LinkedHashMap < > ();
    merchant_data.put("merchant_id", "merchant_id");
    merchant_data.put("merchant_access_code", "merchant_access_code");
    merchant_data.put("unique_merchant_txn_id", "XYZ123");
    merchant_data.put("merchant_return_url", "whitelisted_merchant_return_url");
    requestBody.put("merchant_data", merchant_data);

    Map < String, Object > paymentDataObject = new LinkedHashMap < > ();
    paymentDataObject.put("amount_in_paisa", 100);
    requestBody.put("payment_data", paymentDataObject);
    Map < String, Object > txnObject = new LinkedHashMap < > ();
    txnObject.put("navigation_mode", "2");
    txnObject.put("payment_mode", "1,3,4,19,10,11,14");
    txnObject.put("transaction_type", "1");
    requestBody.put("txn_data", txnObject);

    Map < String, Object > requestBodyCleaned = clean(requestBody);
    Map < String, Object > mapStatus = new HashMap < > ();
    mapStatus.put("result", requestBodyCleaned);
    Gson gson = new GsonBuilder().disableHtmlEscaping().create();
    String jsonString2 = gson.toJson(requestBodyCleaned);
    jsonString2 = jsonString2.replace("\\/", "/");

    // Encoding JSON string to base64
    String base64Encoded = Base64.getEncoder().encodeToString(jsonString2.getBytes());

    System.out.println(base64Encoded);
  }
}
```

#### 3.1.3. HashMap:

Generate HashMap using the Base64 Encode and the secret key. Use the below sample code to handle the generation of HashMap using SHA256.

```java Java
import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import javax.xml.bind.DatatypeConverter;

public class SignatureGenerator {

    public static String jsonHash(String request, String secret) throws NoSuchAlgorithmException, InvalidKeyException, IllegalStateException, UnsupportedEncodingException {
        SecretKeySpec secretKeySpec = new SecretKeySpec(DatatypeConverter.parseHexBinary(secret), "HmacSHA256");
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(secretKeySpec);
        byte[] hmacBytes = mac.doFinal(request.getBytes("UTF-8"));
        String ss = String.format("%02x", new BigInteger(1, hmacBytes));
        return bytesToHex(hmacBytes).toUpperCase();
    }
    private static String bytesToHex(byte[] bytes) {
        StringBuilder result = new StringBuilder();
        for (byte b : bytes) {
            result.append(String.format("%02X", b));
        }
        return result.toString();
    }

    public static void main(String[] args) throws UnsupportedEncodingException, NoSuchAlgorithmException, InvalidKeyException {
        String responseBody = "<Base64EncodedPayload>";
        String signingSecret = "<Secret>";

        String requestSignature = SignatureGenerator.jsonHash(responseBody,signingSecret);
        System.out.println(requestSignature);
    }
} 
```

After successfully converting the JSON to a Base64 encode and generated a HashMap secret use the below Endpoints to accept payment.

```text Accept Payment UAT Endpoint
POST: https://uat.pinepg.in/api/v2/accept/payment
```
```Text Accept Payment PROD Endpoint
POST: https://pinepg.in/api/v2/accept/payment
```

Shown below are the sample request and sample response for a Accept Payment API.

```json Sample Request
{
  "request": "ewogICJtZXJjaGFudF9kYXRhIjogewogICAgIm1lcmNoYW50X2lkIjogMjIyMDgyLAogICAgIm1lcmNoYW50X2FjY2Vzc19jb2RlIjogImNmZDA1YzBjLTM5ZjEtNDIzMi1iZDZmLTZkM2E4NjA4ZTFiZSIsCiAgICAidW5pcXVlX21lcmNoYW50X3R4bl9pZCI6ICJ0ZXN0aW5nZWRnZXNlYW1sZXNzMTEyMzQ1NDMyIiwKICAgICJtZXJjaGFudF9yZXR1cm5fdXJsIjogImh0dHBzOi8vc3RhZ2Utd2ViYXBwLnBheXRtLmluL3Blb24ucGhwIgogIH0sCiAgInBheW1lbnRfZGF0YSI6IHsKICAgICJhbW91bnRfaW5fcGFpc2EiOiA4MDAKICB9LAogICJ0eG5fZGF0YSI6IHsKICAgICJuYXZpZ2F0aW9uX21vZGUiOiAiNyIsCiAgICAicGF5bWVudF9tb2RlIjogIjEwIiwKICAgICJ0cmFuc2FjdGlvbl90eXBlIjogIjEiLAogICAgInRpbWVfc3RhbXAiOiAxNTc1ODgwMDAwMDAKICB9Cn0="
}
```
```json Sample Response
{
  "token": "S087B99vA68R0L9gb8JI%2bqjds%2bOZaArBKLb3s7eQ%2fg7k%3d",
  "response_code": 1,
  "response_message": "SUCCESS"
}
```

Refer to our <a href="https://developer.pluralonline.com/v2.0/reference/emi-accept-payment" target="_blank">Accept Payment API Documentation</a> for more information.

## 4. Process Payment

To Generate a Payment Link use our Process Payment API. 

Use the below endpoints to Process Payment.

```text Process Payment UAT Endpoint
POST: https://uat.pinepg.in/api/v2/process/payment
```
```Text Process Payment Prod Endpoint
POST: https://pinepg.in/api/v2/process/payment
```

### Query Parameter

`Token`: You need to pass the token generated in the Accept Payment API as the query parameter.

Shown below is a sample request and sample response for a Process Payment API.

```json Sample Request
{
  "card_data": {
    "card_number": "4012001037141112",
    "card_expiry_year": "2030",
    "card_expiry_month": "12",
    "card_holder_name": "Test",
    "cvv": "123"
  }
}
```
```json Sample Response
{
  "response_code": 1,
  "response_message": "SUCCESS",
  "redirect_url": "http://hostname:port/pinepg/v2/process/payment?token=848RFsu%2bRnNcSsaZdzEgkeosvCc2o5lK TV4uKJF%2fcjE%3d"
}
```

Refer to our <a href="https://developer.pluralonline.com/v2.0/reference/emi-process-payment" target="_blank">Process Payment API Documentation</a> for more information.

## Handle Payments

Use the generated link returned in our Generate Payment Link API to redirect your customers to the seamless checkout to accept payment.

To know the status of the payment you can use the below options.

1. **<a href="https://developer.pluralonline.com/v2.0/reference/payment-inquiry-refund" target="_blank">Inquiry API</a>**: Use this API to check transaction statuses.
2. **<a href="https://developer.pluralonline.com/v2.0/docs/developer-tools-webhook" target="_blank">Webhook Notification</a>**: We send Webhook notifications on the successful payment or any changes to the payments response object.
