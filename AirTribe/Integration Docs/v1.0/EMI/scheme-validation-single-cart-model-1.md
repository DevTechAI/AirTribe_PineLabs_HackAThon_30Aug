---
title: "Scheme Validation: Single Cart Model"
slug: "scheme-validation-single-cart-model-1"
excerpt: "This API Help to set Scheme Validation: Single Cart Model"
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Fri Feb 04 2022 11:43:58 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Feb 09 2022 11:36:12 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Details",
    "0-0": "merchant_id\\*",
    "0-1": "integer",
    "0-2": "merchant_id is the unique identifier of the merchant. This id is assigned to you by Plural. You can find merchant_id under the credentials section of the settings section of Plural Console dashboard.",
    "1-0": "amount_in_paisa\\*",
    "1-1": "long",
    "1-2": "Amount is paise.",
    "2-0": "card_number\\*",
    "2-1": "string",
    "2-2": "vaild Card numbder.",
    "3-0": "scheme_id\\*",
    "3-1": "string",
    "3-2": "Scheme id is the offer identifier availability of which on the card is to be checked.",
    "4-0": "program_type\\*",
    "4-1": "string",
    "4-2": "program_type.",
    "5-0": "is_scheme_valid\\*",
    "5-1": "boolean",
    "5-2": "vaild check on the schema.",
    "6-0": "product_code\\*",
    "6-1": "string",
    "6-2": "Product code is the unique identifier of the product.",
    "7-0": "product_name\\*",
    "7-1": "string",
    "7-2": "Product name",
    "8-0": "product_amount\\*",
    "8-1": "long",
    "8-2": "Product amount in paise.",
    "9-0": "subvention_cashback  \n\\_discount",
    "9-1": "string",
    "9-2": "Subvention discount cashback amount in paise. Only applicable when subvention is present.",
    "10-0": "product_discount",
    "10-1": "string",
    "10-2": "Product discount amount in paise. Only applicable if product discount is present.",
    "11-0": "subvention_cashback  \n\\_discount_percentage",
    "11-1": "long",
    "11-2": "Subvention discount cashback percentage. Its value is percentage multiplied by 10000.",
    "12-0": "product_discount  \n\\_percentage",
    "12-1": "long",
    "12-2": "Product discount cashback percentage. Its value is percentage multiplied by 10000.",
    "13-0": "subvention_type\\*",
    "13-1": "int",
    "13-2": "Type of subvention applied on the scheme. \"1\" for No cost EMI, \"2\" for Low cost EMI and \"3\" for Standard EMI",
    "14-0": "bank_interest_  \nrate_percentage",
    "14-1": "long",
    "14-2": "Bank interest amount in paise.",
    "15-0": "bank_interest_rate",
    "15-1": "string",
    "15-2": "Bank interest rate in percentage multiplied by 10000.",
    "16-0": "emi_scheme",
    "16-1": "string",
    "16-2": "valid emi scheme.",
    "17-0": "tenure_id\\*",
    "17-1": "string",
    "17-2": "valid tenure id.",
    "18-0": "tenure_in_month\\*",
    "18-1": "string",
    "18-2": "valid tenure in month.",
    "19-0": "monthly_installment\\*",
    "19-1": "string",
    "19-2": "vaild monthly installment.",
    "20-0": "bank_interest_rate\\*",
    "20-1": "string",
    "20-2": "vaild bank interest rate.",
    "21-0": "interest_pay_  \nto_bank\\*",
    "21-1": "string",
    "21-2": "valid interest pay to bank.",
    "22-0": "total_offerred_discount  \n\\_cashback_amount\\*",
    "22-1": "string",
    "22-2": "vaild cash back amount.",
    "23-0": "loan_amount\\*",
    "23-1": "string",
    "23-2": "vaild loan amount.",
    "24-0": "auth_amount\\*",
    "24-1": "string",
    "24-2": "vaild auth amount.",
    "25-0": "acquirerId\\*",
    "25-1": "string",
    "25-2": "vaild acquire id."
  },
  "cols": 3,
  "rows": 26,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


**Request Body payload:** 

```json JSON
{
    "merchant_data": {
        "merchant_id": 11565
    },
    "payment_data": {
        "amount_in_paisa": 1000000
    },
    "card_data": {
        "card_number": "4012001037141112"
    },
    "emi_data": {
        "offer_scheme": {
            "product_details": [
                {
                    "schemes": [
                        {
                            "scheme_id": "47049",
                            "program_type": 106,
                            "is_scheme_valid": true
                        }
                    ],
                    "product_code": "testproduct01",
                    "product_name": "testproduct01",
                    "product_amount": 1000000,
                    "subvention_cashback_discount": 24500,
                    "product_discount": 0,
                    "subvention_cashback_discount_percentage": 24500,
                    "product_discount_percentage": 0,
                    "subvention_type": 1,
                    "additional_cashback": "Rs1000 Additional Cashback",
                    "bank_interest_rate_percentage": 150000,
                    "bank_interest_rate": 24487
                }
            ],
            "emi_scheme": null
        },
        "tenure_id": "3",
        "tenure_in_month": "3",
        "monthly_installment": 333329,
        "bank_interest_rate": 150000,
        "interest_pay_to_bank": 24487,
        "total_offerred_discount_cashback_amount": 24500,
        "loan_amount": 975500,
        "auth_amount": 975500
    },
    "acquirer_data": {
        "acquirerId": 8004
    }
}
```

**Response Payload:** 

```json 200 Success
{
"response_code": 1,
"response_message": "SUCCESS"
}
```
```json 400 Bad Request
{
  "response_code": 14845,
  "response_message": "Request Data is not valid"
}

{
  "response_code": 14826,
  "response_message": "Offer is not applicable on card"
}

{
  "response_code": 14819,
  "response_message": "Offer is outdated"
}
```
```json 500 Internal Server Error
{
  "error_code": "14020",
  "error_message": "Oops, something went wrong!"
}
```
