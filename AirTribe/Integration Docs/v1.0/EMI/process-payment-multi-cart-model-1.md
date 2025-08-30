---
title: "Process Payment: Multi Cart Model"
slug: "process-payment-multi-cart-model-1"
excerpt: "This API Help to get Process Payment: Multi Cart Model"
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Fri Feb 04 2022 13:51:29 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Feb 18 2022 12:52:08 GMT+0000 (Coordinated Universal Time)"
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
    "0-2": "merchant_id is the unique identifier of the merchant.",
    "1-0": "card_number\\*",
    "1-1": "string",
    "1-2": "Card number",
    "2-0": "card_expiry  \n\\_year\\*",
    "2-1": "string",
    "2-2": "The year of card expiry. For example: \"2025\"",
    "3-0": "card_expiry  \n\\_month\\*",
    "3-1": "string",
    "3-2": "The year of card expiry. For example: \"02\"",
    "4-0": "card_holder  \n\\_name\\*",
    "4-1": "string",
    "4-2": "Name on the card.",
    "5-0": "cvv\\*",
    "5-1": "string",
    "5-2": "CVV",
    "6-0": "is_card_to  \n\\_be_saved",
    "6-1": "Bool",
    "6-2": "saved card details ofr future use.",
    "7-0": "country_code\\*",
    "7-1": "integer",
    "7-2": "The country code of the mobile number.",
    "8-0": "mobile_number\\*",
    "8-1": "string",
    "8-2": "Mobile number of the customer.",
    "9-0": "email_id\\*",
    "9-1": "string",
    "9-2": "Email id of the cusotmer.",
    "10-0": "customer_token\\*",
    "10-1": "string",
    "10-2": "vaild Token to be set for the customer.",
    "11-0": "scheme_id\\*",
    "11-1": "string",
    "11-2": "Scheme id is the offer identifier availability of which on the card is to be checked.",
    "12-0": "program_type\\*",
    "12-1": "string",
    "12-2": "program_type.",
    "13-0": "is_scheme_valid\\*",
    "13-1": "boolean",
    "13-2": "vaild check on the schema.",
    "14-0": "product_code\\*",
    "14-1": "string",
    "14-2": "Product code is the unique identifier of the product.",
    "15-0": "product_name\\*",
    "15-1": "string",
    "15-2": "Product name",
    "16-0": "product_amount\\*",
    "16-1": "long",
    "16-2": "Product amount in paise.",
    "17-0": "subvention\\_  \ncashback_discount",
    "17-1": "string",
    "17-2": "Subvention discount cashback amount in paise. Only applicable when subvention is present.",
    "18-0": "product_discount",
    "18-1": "string",
    "18-2": "Product discount amount in paise. Only applicable if product discount is present.",
    "19-0": "subvention_cashback  \n\\_discount_percentage",
    "19-1": "long",
    "19-2": "Subvention discount cashback percentage. Its value is percentage multiplied by 10000.",
    "20-0": "product_discount  \n\\_percentage",
    "20-1": "long",
    "20-2": "Product discount cashback percentage. Its value is percentage multiplied by 10000.",
    "21-0": "subvention_type\\*",
    "21-1": "int",
    "21-2": "Type of subvention applied on the scheme. \"1\" for No cost EMI, \"2\" for Low cost EMI and \"3\" for Standard EMI",
    "22-0": "bank_interest_  \nrate_percentage",
    "22-1": "long",
    "22-2": "Bank interest amount in paise.",
    "23-0": "bank_interest_rate",
    "23-1": "string",
    "23-2": "Bank interest rate in percentage multiplied by 10000.",
    "24-0": "emi_scheme",
    "24-1": "string",
    "24-2": "valid emi scheme.",
    "25-0": "tenure_id\\*",
    "25-1": "string",
    "25-2": "valid tenure id.",
    "26-0": "tenure_in_month\\*",
    "26-1": "string",
    "26-2": "valid tenure in month.",
    "27-0": "monthly_installment\\*",
    "27-1": "string",
    "27-2": "vaild monthly installment.",
    "28-0": "bank_interest_rate\\*",
    "28-1": "string",
    "28-2": "vaild bank interest rate.",
    "29-0": "interest_pay_to_bank\\*",
    "29-1": "string",
    "29-2": "valid interest pay to bank.",
    "30-0": "total_offerred_  \ndiscount_cashback  \n\\_amount\\*",
    "30-1": "string",
    "30-2": "vaild cash back amount.",
    "31-0": "loan_amount\\*",
    "31-1": "string",
    "31-2": "vaild loan amount.",
    "32-0": "auth_amount\\*",
    "32-1": "string",
    "32-2": "vaild auth amount.",
    "33-0": "acquirerId",
    "33-1": "string",
    "33-2": "vaild acquire id."
  },
  "cols": 3,
  "rows": 34,
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
        "merchant_id": 11607
    },
    "card_data": {
        "card_number": "4012001037141112",
        "card_expiry_year": "2023",
        "card_expiry_month": "11",
        "card_holder_name": "Harsh",
        "cvv": "123",
        "is_card_to_be_saved": true
    },
    "customer_data": {
        "country_code": "91",
        "mobile_number": "9582492891",
        "email_id": "harsh.kumar@pinelabs.com",
        "customer_token": "AGxVyLz65ucoJrx+w1u1xQ=="
    },
    "emi_data": {
        "offer_scheme": {
            "product_details": [
                {
                    "schemes": [
                        {
                            "scheme_id": "48916",
                            "program_type": 112,
                            "is_scheme_valid": true
                        }
                    ],
                    "product_code": "2000",
                    "product_name": "2000",
                    "product_amount": 1000000,
                    "subvention_cashback_discount": 20000,
                    "product_discount": 0,
                    "subvention_cashback_discount_percentage": 20000,
                    "product_discount_percentage": 0,
                    "subvention_type": 2,
                    "bank_interest_rate_percentage": 60000,
                    "bank_interest_rate": 24661
                },
                {
                    "schemes": [
                        {
                            "scheme_id": "48916",
                            "program_type": 112,
                            "is_scheme_valid": true
                        }
                    ],
                    "product_code": "2001",
                    "product_name": "2001",
                    "product_amount": 1000000,
                    "subvention_cashback_discount": 20000,
                    "product_discount": 0,
                    "subvention_cashback_discount_percentage": 20000,
                    "product_discount_percentage": 0,
                    "subvention_type": 2,
                    "bank_interest_rate_percentage": 60000,
                    "bank_interest_rate": 24661
                }
            ],
            "emi_scheme": {
                "scheme_id": "46918",
                "program_type": 105,
                "is_scheme_valid": true
            }
        },
        "tenure_id": "9",
        "tenure_in_month": "9",
        "monthly_installment": 223258,
        "bank_interest_rate": 60000,
        "interest_pay_to_bank": 49322,
        "total_offerred_discount_cashback_amount": 40000,
        "loan_amount": 1960000,
        "auth_amount": 1960000
    },
    "acquirer_data": {
        "acquirerId": 8004
    }
}
```

**Response Payload:** 

```json 200 Success
{
    "content": "&lt;!DOCTYPE html>&lt;html>&lt;head>&lt;title> Redirecting ... &lt;/title>&lt;/head>&lt;body>&lt;script>var url = &#39;https://test.pinepg.in/pinepg/v2/process/payment?token=QNd7t3Tb5GdZG11%2bg%2fJdy%2b%2f1FIwnko2haekL5yb%2fvio%3d&#39;;window.location = url;&lt;/script>&lt;/body>&lt;/html>",
    "payment_id": 438470,
    "order_id": 78612345,
    "amount_in_paise": 2000000,
    "token": "ZCgfoCQy4z3Stfb6fJeC69iBcTFINGqvhlKf3hEduhU=",
    "api_url": null,
    "response_code": 14010,
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
