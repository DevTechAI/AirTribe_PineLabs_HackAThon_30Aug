---
title: "Scheme Validation through Saved Card: Single Cart"
slug: "scheme-validation-through-saved-card-single-cart-1"
excerpt: "This API Help to get Scheme Validation through Saved Card: Single Cart"
hidden: true
createdAt: "Fri Feb 04 2022 13:04:37 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Jan 31 2025 07:32:56 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

| Attribute                                 | Type    | Details                                                                                                                                                                                                 |
| :---------------------------------------- | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| merchant_id\*                             | string  | merchant_id is the unique identifier of the merchant. This id is assigned to you by Plural. You can find merchant_id under the credentials section of the settings section of Plural Console dashboard. |
| amount_in_paisa\*                         | string  | Amount is paise.                                                                                                                                                                                        |
| card_number\*                             | string  | vaild Card numbder.                                                                                                                                                                                     |
| scheme_id\*                               | string  | Scheme id is the offer identifier availability of which on the card is to be checked.                                                                                                                   |
| program_type\*                            | string  | program_type.                                                                                                                                                                                           |
| is_scheme_valid\*                         | boolean | vaild check on the schema.                                                                                                                                                                              |
| product_code\*                            | string  | Product code is the unique identifier of the product.                                                                                                                                                   |
| product_name\*                            | string  | Product name                                                                                                                                                                                            |
| product_amount\*                          | long    | Product amount in paise.                                                                                                                                                                                |
| subvention_cashback_discount              | string  | Subvention discount cashback amount in paise. Only applicable when subvention is present.                                                                                                               |
| product_discount                          | string  | Product discount amount in paise. Only applicable if product discount is present.                                                                                                                       |
| subvention_cashback_discount_percentage   | long    | Subvention discount cashback percentage. Its value is percentage multiplied by 10000.                                                                                                                   |
| product_discount_percentage               | long    | Product discount cashback percentage. Its value is percentage multiplied by 10000.                                                                                                                      |
| subvention_type\*                         | int     | Type of subvention applied on the scheme. "1" for No cost EMI, "2" for Low cost EMI and "3" for Standard EMI                                                                                            |
| bank_interest_rate_percentage             | long    | Bank interest amount in paise.                                                                                                                                                                          |
| bank_interest_rate                        | string  | Bank interest rate in percentage multiplied by 10000.                                                                                                                                                   |
| emi_scheme                                | string  | valid emi scheme.                                                                                                                                                                                       |
| tenure_id\*                               | string  | valid tenure id.                                                                                                                                                                                        |
| tenure_in_month\*                         | string  | valid tenure in month.                                                                                                                                                                                  |
| monthly_installment\*                     | string  | vaild monthly installment.                                                                                                                                                                              |
| bank_interest_rate\*                      | string  | vaild bank interest rate.                                                                                                                                                                               |
| interest_pay_to_bank\*                    | string  | valid interest pay to bank.                                                                                                                                                                             |
| total_offerred_discount_cashback_amount\* | string  | vaild cash back amount.                                                                                                                                                                                 |
| loan_amount\*                             | string  | vaild loan amount.                                                                                                                                                                                      |
| auth_amount\*                             | string  | vaild auth amount.                                                                                                                                                                                      |
| acquirerId                                | string  | vaild acquire id.                                                                                                                                                                                       |

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
