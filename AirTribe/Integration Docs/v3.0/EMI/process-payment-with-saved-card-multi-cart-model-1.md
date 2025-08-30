---
title: "Process Payment with Saved Card: Multi Cart Model"
slug: "process-payment-with-saved-card-multi-cart-model-1"
excerpt: "This API Help to get Process Payment with Saved Card: Multi Cart Model"
hidden: true
metadata: 
  image: []
  robots: "index"
createdAt: "Fri Feb 04 2022 13:54:01 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Feb 04 2022 13:54:01 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

| Attribute                                 | Type    | Details                                                                                                      |
| :---------------------------------------- | :------ | :----------------------------------------------------------------------------------------------------------- |
| merchant_id                               | integer | merchant_id is the unique identifier of the merchant.                                                        |
| saved_card_token                          | string  | saved card token for future use.                                                                             |
| country_code\*                            | integer | The country code of the mobile number.                                                                       |
| mobile_number\*                           | string  | Mobile number of the customer.                                                                               |
| email_id\*                                | string  | Email id of the cusotmer.                                                                                    |
| customer_token\*                          | string  | vaild Token to be set for the customer.                                                                      |
| scheme_id\*                               | string  | Scheme id is the offer identifier availability of which on the card is to be checked.                        |
| program_type\*                            | string  | program_type.                                                                                                |
| is_scheme_valid\*                         | boolean | vaild check on the schema.                                                                                   |
| product_code\*                            | string  | Product code is the unique identifier of the product.                                                        |
| product_name\*                            | string  | Product name                                                                                                 |
| product_amount\*                          | long    | Product amount in paise.                                                                                     |
| subvention_cashback_discount              | string  | Subvention discount cashback amount in paise. Only applicable when subvention is present.                    |
| product_discount                          | string  | Product discount amount in paise. Only applicable if product discount is present.                            |
| subvention_cashback_discount_percentage   | long    | Subvention discount cashback percentage. Its value is percentage multiplied by 10000.                        |
| product_discount_percentage               | long    | Product discount cashback percentage. Its value is percentage multiplied by 10000.                           |
| subvention_type\*                         | int     | Type of subvention applied on the scheme. "1" for No cost EMI, "2" for Low cost EMI and "3" for Standard EMI |
| bank_interest_rate_percentage             | long    | Bank interest amount in paise.                                                                               |
| bank_interest_rate                        | string  | Bank interest rate in percentage multiplied by 10000.                                                        |
| emi_scheme                                | string  | valid emi scheme.                                                                                            |
| tenure_id\*                               | string  | valid tenure id.                                                                                             |
| tenure_in_month\*                         | string  | valid tenure in month.                                                                                       |
| monthly_installment\*                     | string  | vaild monthly installment.                                                                                   |
| bank_interest_rate\*                      | string  | vaild bank interest rate.                                                                                    |
| interest_pay_to_bank\*                    | string  | valid interest pay to bank.                                                                                  |
| total_offerred_discount_cashback_amount\* | string  | vaild cash back amount.                                                                                      |
| loan_amount\*                             | string  | vaild loan amount.                                                                                           |
| auth_amount\*                             | string  | vaild auth amount.                                                                                           |
| acquirerId                                | string  | vaild acquire id.                                                                                            |

**Request Body payload:** 

```json JSON
{
    "merchant_data": {
        "merchant_id": 11607
    },
    "card_data": {
        "saved_card_token": "chYeVuIZ6NSHoAR4W8C+0A=="
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
