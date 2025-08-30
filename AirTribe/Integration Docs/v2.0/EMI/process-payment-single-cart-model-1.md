---
title: "Process Payment: Single Cart Model"
slug: "process-payment-single-cart-model-1"
excerpt: "This API Help to get Process Payment: Single Cart Model"
hidden: true
createdAt: "Fri Feb 04 2022 13:11:35 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:52:01 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Details",
    "0-0": "card_number\\*",
    "0-1": "string",
    "0-2": "Card number",
    "1-0": "card_expiry  \n\\_year\\*",
    "1-1": "string",
    "1-2": "The year of card expiry. For example: \"2025\"",
    "2-0": "card_expiry  \n\\_month\\*",
    "2-1": "string",
    "2-2": "The year of card expiry. For example: \"02\"",
    "3-0": "card_holder  \n\\_name\\*",
    "3-1": "string",
    "3-2": "Name on the card.",
    "4-0": "cvv\\*",
    "4-1": "string",
    "4-2": "CVV",
    "5-0": "is_card_to  \n\\_be_saved",
    "5-1": "Bool",
    "5-2": "saved card details ofr future use.",
    "6-0": "country_code\\*",
    "6-1": "integer",
    "6-2": "The country code of the mobile number.",
    "7-0": "mobile_number\\*",
    "7-1": "string",
    "7-2": "Mobile number of the customer.",
    "8-0": "email_id\\*",
    "8-1": "string",
    "8-2": "Email id of the cusotmer.",
    "9-0": "customer_token\\*",
    "9-1": "string",
    "9-2": "vaild Token to be set for the customer.",
    "10-0": "scheme_id\\*",
    "10-1": "string",
    "10-2": "Scheme id is the offer identifier availability of which on the card is to be checked.",
    "11-0": "program_type\\*",
    "11-1": "string",
    "11-2": "program_type.",
    "12-0": "is_scheme_valid\\*",
    "12-1": "boolean",
    "12-2": "vaild check on the schema.",
    "13-0": "product_code\\*",
    "13-1": "string",
    "13-2": "Product code is the unique identifier of the product.",
    "14-0": "product_name\\*",
    "14-1": "string",
    "14-2": "Product name",
    "15-0": "product_amount\\*",
    "15-1": "long",
    "15-2": "Product amount in paise.",
    "16-0": "subvention\\_  \ncashback_discount",
    "16-1": "string",
    "16-2": "Subvention discount cashback amount in paise. Only applicable when subvention is present.",
    "17-0": "product_discount",
    "17-1": "string",
    "17-2": "Product discount amount in paise. Only applicable if product discount is present.",
    "18-0": "subvention_cashback  \n\\_discount_percentage",
    "18-1": "long",
    "18-2": "Subvention discount cashback percentage. Its value is percentage multiplied by 10000.",
    "19-0": "product_discount  \n\\_percentage",
    "19-1": "long",
    "19-2": "Product discount cashback percentage. Its value is percentage multiplied by 10000.",
    "20-0": "subvention_type\\*",
    "20-1": "int",
    "20-2": "Type of subvention applied on the scheme. \"1\" for No cost EMI, \"2\" for Low cost EMI and \"3\" for Standard EMI",
    "21-0": "bank_interest  \n\\_rate_percentage",
    "21-1": "long",
    "21-2": "Bank interest amount in paise.",
    "22-0": "bank_interest_rate",
    "22-1": "string",
    "22-2": "Bank interest rate in percentage multiplied by 10000.",
    "23-0": "emi_scheme",
    "23-1": "string",
    "23-2": "valid emi scheme.",
    "24-0": "tenure_id\\*",
    "24-1": "string",
    "24-2": "valid tenure id.",
    "25-0": "tenure_in_month\\*",
    "25-1": "string",
    "25-2": "valid tenure in month.",
    "26-0": "monthly_installment\\*",
    "26-1": "string",
    "26-2": "vaild monthly installment.",
    "27-0": "bank_interest_rate\\*",
    "27-1": "string",
    "27-2": "vaild bank interest rate.",
    "28-0": "interest_pay_to_bank\\*",
    "28-1": "string",
    "28-2": "valid interest pay to bank.",
    "29-0": "total_offerred_  \ndiscount_cashback  \n\\_amount\\*",
    "29-1": "string",
    "29-2": "vaild cash back amount.",
    "30-0": "loan_amount\\*",
    "30-1": "string",
    "30-2": "vaild loan amount.",
    "31-0": "auth_amount\\*",
    "31-1": "string",
    "31-2": "vaild auth amount.",
    "32-0": "acquirerId",
    "32-1": "string",
    "32-2": "vaild acquire id."
  },
  "cols": 3,
  "rows": 33,
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
    "payment_data": {
        "amount_in_paisa": 2000000
    },
    "card_data": {
        "saved_card_token": "chYeVuIZ6NSHoAR4W8C+0A=="
    },
    "customer_data": {
        "customer_token": "AGxVyLz65ucoJrx+w1u1xQ=="
    },
    "emi_data": {
        "offer_scheme": {
            "product_details": [
                {
                    "schemes": [
                        {
                            "scheme_id": "46921",
                            "program_type": 106,
                            "is_scheme_valid": true
                        }
                    ],
                    "product_code": "2000",
                    "product_name": "2000",
                    "product_amount": 2000000,
                    "subvention_cashback_discount": 40000,
                    "product_discount": 0,
                    "subvention_cashback_discount_percentage": 20000,
                    "product_discount_percentage": 0,
                    "subvention_type": 2,
                    "bank_interest_rate_percentage": 50000,
                    "bank_interest_rate": 53468
                }
            ],
            "emi_scheme": null
        },
        "tenure_id": "12",
        "tenure_in_month": "12",
        "monthly_installment": 167789,
        "bank_interest_rate": 50000,
        "interest_pay_to_bank": 53468,
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

#for Debit EMI Response
{
    "content": "https://test.pinepg.in/api/v2/validate/otp?token=zoWKNhaVFps0wKD%2fCV%2btCfCqDndxEB1sy7eiF4f%2bH84%3d",
    "payment_id": 438471,
    "order_id":78612345,
    "amount_in_paise": 2000000,
    "token": "fsQNbaN6TfAu5wUbGD2ErbHi5BBJDphbu+U5PGgQ4OM=",
    "api_url": "http://pluralqa.pinepg.in/api/v1/emi/validate/otp?token=fsQNbaN6TfAu5wUbGD2ErbHi5BBJDphbu%2bU5PGgQ4OM%3d",
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
