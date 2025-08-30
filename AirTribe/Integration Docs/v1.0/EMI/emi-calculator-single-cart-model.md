---
title: "EMI Calculator: Single Cart Model"
slug: "emi-calculator-single-cart-model"
excerpt: "EMI Calculator as the name suggests provides a platform /API information exchange to display various EMI offers details. This is to fetch the offers details for Single Cart Model. The single Cart Model is the one in which only a single product is added to the cart."
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Fri Feb 04 2022 11:31:57 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Feb 09 2022 11:32:35 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:**

| Attribute        | Type    | Details                                                                                                                                                                                                 |
| :--------------- | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| merchant_id\*    | integer | merchant_id is the unique identifier of the merchant. This id is assigned to you by Plural. You can find merchant_id under the credentials section of the settings section of Plural Console dashboard. |
| amount_in_paisa  | long    | Amount is paise                                                                                                                                                                                         |
| product_code\*   | string  | Product code is the unique identifier of the product on which the offers details are intended to be fetched.                                                                                            |
| product_amount\* | long    | Product amount in paise                                                                                                                                                                                 |

**Request Body payload:** 

```json JSON
{
    "merchant_data": {
        "merchant_id": 11565
    },
    "payment_data": {
        "amount_in_paisa": 2000000
    },
    "product_details": [
        {
            "product_code": "testproduct01",
            "product_amount": 2000000
        }
    ]
}
```

**Response Payload:** 

```json 200 Success
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
                                        "scheme_id": "47049",
                                        "program_type": 106,
                                        "is_scheme_valid": true
                                    }
                                ],
                                "product_code": "testproduct01",
                                "product_name": "testproduct01",
                                "product_amount": 2000000,
                                "subvention_cashback_discount": 49000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 24500,
                                "product_discount_percentage": 0,
                                "subvention_type": 1,
                                "additional_cashback": "Rs1000 Additional Cashback",
                                "bank_interest_rate_percentage": 150000,
                                "bank_interest_rate": 48974
                            }
                        ],
                        "emi_scheme": null
                    },
                    "tenure_id": "3",
                    "tenure_in_month": "3",
                    "monthly_installment": 666658,
                    "bank_interest_rate": 150000,
                    "interest_pay_to_bank": 48974,
                    "total_offerred_discount_cashback_amount": 49000,
                    "loan_amount": 1951000,
                    "auth_amount": 1951000
                },
                {
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
                                "product_amount": 2000000,
                                "subvention_cashback_discount": 90000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 45000,
                                "product_discount_percentage": 0,
                                "subvention_type": 1,
                                "additional_cashback": "Rs2000 Additional Cashback",
                                "bank_interest_rate_percentage": 150000,
                                "bank_interest_rate": 84424
                            }
                        ],
                        "emi_scheme": null
                    },
                    "tenure_id": "6",
                    "tenure_in_month": "6",
                    "monthly_installment": 332404,
                    "bank_interest_rate": 150000,
                    "interest_pay_to_bank": 84424,
                    "total_offerred_discount_cashback_amount": 90000,
                    "loan_amount": 1910000,
                    "auth_amount": 1910000
                },
                {
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
                                "product_amount": 2000000,
                                "subvention_cashback_discount": 49000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 24500,
                                "product_discount_percentage": 0,
                                "subvention_type": 2,
                                "bank_interest_rate_percentage": 150000,
                                "bank_interest_rate": 127069
                            }
                        ],
                        "emi_scheme": null
                    },
                    "tenure_id": "9",
                    "tenure_in_month": "9",
                    "monthly_installment": 236341,
                    "bank_interest_rate": 150000,
                    "interest_pay_to_bank": 127069,
                    "total_offerred_discount_cashback_amount": 49000,
                    "loan_amount": 2000000,
                    "auth_amount": 2000000
                },
                {
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
                                "product_amount": 2000000,
                                "subvention_cashback_discount": 0,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 0,
                                "product_discount_percentage": 0,
                                "subvention_type": 3,
                                "additional_cashback": "Rs.5000 additional discount cashback",
                                "bank_interest_rate_percentage": 150000,
                                "bank_interest_rate": 205780
                            }
                        ],
                        "emi_scheme": null
                    },
                    "tenure_id": "15",
                    "tenure_in_month": "15",
                    "monthly_installment": 147052,
                    "bank_interest_rate": 150000,
                    "interest_pay_to_bank": 205780,
                    "total_offerred_discount_cashback_amount": 0,
                    "loan_amount": 2000000,
                    "auth_amount": 2000000
                },
                {
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
                                "product_amount": 2000000,
                                "subvention_cashback_discount": 0,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 0,
                                "product_discount_percentage": 0,
                                "subvention_type": 3,
                                "additional_cashback": "Rs.5000 additional discount cashback",
                                "bank_interest_rate_percentage": 150000,
                                "bank_interest_rate": 245842
                            }
                        ],
                        "emi_scheme": null
                    },
                    "tenure_id": "18",
                    "tenure_in_month": "18",
                    "monthly_installment": 124769,
                    "bank_interest_rate": 150000,
                    "interest_pay_to_bank": 245842,
                    "total_offerred_discount_cashback_amount": 0,
                    "loan_amount": 2000000,
                    "auth_amount": 2000000
                },
                {
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
                                "product_amount": 2000000,
                                "subvention_cashback_discount": 0,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 0,
                                "product_discount_percentage": 0,
                                "bank_interest_rate_percentage": 0,
                                "bank_interest_rate": 0
                            }
                        ],
                        "emi_scheme": null
                    },
                    "tenure_id": "96",
                    "tenure_in_month": "1",
                    "monthly_installment": 0,
                    "bank_interest_rate": 0,
                    "interest_pay_to_bank": 0,
                    "total_offerred_discount_cashback_amount": 0,
                    "loan_amount": 2000000,
                    "auth_amount": 2000000
                },
                {
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
                                "product_amount": 2000000,
                                "subvention_cashback_discount": 49000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 24500,
                                "product_discount_percentage": 0,
                                "subvention_type": 2,
                                "bank_interest_rate_percentage": 150000,
                                "bank_interest_rate": 179333
                            }
                        ],
                        "emi_scheme": null
                    },
                    "tenure_id": "1086",
                    "tenure_in_month": "13",
                    "monthly_installment": 167641,
                    "bank_interest_rate": 150000,
                    "interest_pay_to_bank": 179333,
                    "total_offerred_discount_cashback_amount": 49000,
                    "loan_amount": 2000000,
                    "auth_amount": 2000000
                }
            ],
            "issuer_name": "HDFC",
            "is_debit_emi_issuer": false
        },
        {
            "list_emi_tenure": [
                {
                    "offer_scheme": {
                        "product_details": [
                            {
                                "schemes": [
                                    {
                                        "scheme_id": "47035",
                                        "program_type": 106,
                                        "is_scheme_valid": true
                                    }
                                ],
                                "product_code": "testproduct01",
                                "product_name": "testproduct01",
                                "product_amount": 2000000,
                                "subvention_cashback_discount": 49000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 24500,
                                "product_discount_percentage": 0,
                                "subvention_type": 1,
                                "bank_interest_rate_percentage": 150000,
                                "bank_interest_rate": 48974
                            }
                        ],
                        "emi_scheme": null
                    },
                    "tenure_id": "3",
                    "tenure_in_month": "3",
                    "monthly_installment": 666658,
                    "bank_interest_rate": 150000,
                    "interest_pay_to_bank": 48974,
                    "total_offerred_discount_cashback_amount": 49000,
                    "loan_amount": 1951000,
                    "auth_amount": 2000000
                }
            ],
            "issuer_name": "ICICI",
            "is_debit_emi_issuer": false
        },
        {
            "list_emi_tenure": [
                {
                    "offer_scheme": {
                        "product_details": [
                            {
                                "schemes": [
                                    {
                                        "scheme_id": "47031",
                                        "program_type": 106,
                                        "is_scheme_valid": true
                                    }
                                ],
                                "product_code": "testproduct01",
                                "product_name": "testproduct01",
                                "product_amount": 2000000,
                                "subvention_cashback_discount": 49000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 24500,
                                "product_discount_percentage": 0,
                                "subvention_type": 1,
                                "bank_interest_rate_percentage": 150000,
                                "bank_interest_rate": 48974
                            }
                        ],
                        "emi_scheme": null
                    },
                    "tenure_id": "3",
                    "tenure_in_month": "3",
                    "monthly_installment": 666658,
                    "bank_interest_rate": 150000,
                    "interest_pay_to_bank": 48974,
                    "total_offerred_discount_cashback_amount": 49000,
                    "loan_amount": 1951000,
                    "auth_amount": 2000000
                }
            ],
            "issuer_name": "AXIS",
            "is_debit_emi_issuer": false
        },
        {
            "list_emi_tenure": [
                {
                    "offer_scheme": {
                        "product_details": [
                            {
                                "schemes": [
                                    {
                                        "scheme_id": "47064",
                                        "program_type": 106,
                                        "is_scheme_valid": true
                                    }
                                ],
                                "product_code": "testproduct01",
                                "product_name": "testproduct01",
                                "product_amount": 2000000,
                                "subvention_cashback_discount": 53000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 26500,
                                "product_discount_percentage": 0,
                                "subvention_type": 1,
                                "additional_cashback": "Rs 1000 Additional Cashback",
                                "bank_interest_rate_percentage": 160000,
                                "bank_interest_rate": 52146
                            }
                        ],
                        "emi_scheme": null
                    },
                    "tenure_id": "3",
                    "tenure_in_month": "3",
                    "monthly_installment": 666382,
                    "bank_interest_rate": 160000,
                    "interest_pay_to_bank": 52146,
                    "total_offerred_discount_cashback_amount": 53000,
                    "loan_amount": 1947000,
                    "auth_amount": 1947000
                },
                {
                    "offer_scheme": {
                        "product_details": [
                            {
                                "schemes": [
                                    {
                                        "scheme_id": "47064",
                                        "program_type": 106,
                                        "is_scheme_valid": true
                                    }
                                ],
                                "product_code": "testproduct01",
                                "product_name": "testproduct01",
                                "product_amount": 2000000,
                                "subvention_cashback_discount": 53000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 26500,
                                "product_discount_percentage": 0,
                                "subvention_type": 2,
                                "additional_cashback": "Rs 1500 Additional Cashback",
                                "bank_interest_rate_percentage": 160000,
                                "bank_interest_rate": 94360
                            }
                        ],
                        "emi_scheme": null
                    },
                    "tenure_id": "6",
                    "tenure_in_month": "6",
                    "monthly_installment": 349060,
                    "bank_interest_rate": 160000,
                    "interest_pay_to_bank": 94360,
                    "total_offerred_discount_cashback_amount": 53000,
                    "loan_amount": 2000000,
                    "auth_amount": 2000000
                },
                {
                    "offer_scheme": {
                        "product_details": [
                            {
                                "schemes": [
                                    {
                                        "scheme_id": "47064",
                                        "program_type": 106,
                                        "is_scheme_valid": true
                                    }
                                ],
                                "product_code": "testproduct01",
                                "product_name": "testproduct01",
                                "product_amount": 2000000,
                                "subvention_cashback_discount": 0,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 0,
                                "product_discount_percentage": 0,
                                "subvention_type": 3,
                                "bank_interest_rate_percentage": 160000,
                                "bank_interest_rate": 135682
                            }
                        ],
                        "emi_scheme": null
                    },
                    "tenure_id": "9",
                    "tenure_in_month": "9",
                    "monthly_installment": 237298,
                    "bank_interest_rate": 160000,
                    "interest_pay_to_bank": 135682,
                    "total_offerred_discount_cashback_amount": 0,
                    "loan_amount": 2000000,
                    "auth_amount": 2000000
                }
            ],
            "issuer_name": "HDFC Bank Debit Card",
            "is_debit_emi_issuer": true
        },
        {
            "list_emi_tenure": [
                {
                    "offer_scheme": {
                        "product_details": [
                            {
                                "schemes": [
                                    {
                                        "scheme_id": "47034",
                                        "program_type": 106,
                                        "is_scheme_valid": true
                                    }
                                ],
                                "product_code": "testproduct01",
                                "product_name": "testproduct01",
                                "product_amount": 2000000,
                                "subvention_cashback_discount": 49000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 24500,
                                "product_discount_percentage": 0,
                                "subvention_type": 1,
                                "bank_interest_rate_percentage": 150000,
                                "bank_interest_rate": 48974
                            }
                        ],
                        "emi_scheme": null
                    },
                    "tenure_id": "3",
                    "tenure_in_month": "3",
                    "monthly_installment": 666658,
                    "bank_interest_rate": 150000,
                    "interest_pay_to_bank": 48974,
                    "total_offerred_discount_cashback_amount": 49000,
                    "loan_amount": 1951000,
                    "auth_amount": 2000000
                }
            ],
            "issuer_name": "KOTAK",
            "is_debit_emi_issuer": false
        },
        {
            "list_emi_tenure": [
                {
                    "offer_scheme": {
                        "product_details": [
                            {
                                "schemes": [
                                    {
                                        "scheme_id": "47036",
                                        "program_type": 106,
                                        "is_scheme_valid": true
                                    }
                                ],
                                "product_code": "testproduct01",
                                "product_name": "testproduct01",
                                "product_amount": 2000000,
                                "subvention_cashback_discount": 49000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 24500,
                                "product_discount_percentage": 0,
                                "subvention_type": 1,
                                "bank_interest_rate_percentage": 150000,
                                "bank_interest_rate": 48974
                            }
                        ],
                        "emi_scheme": null
                    },
                    "tenure_id": "3",
                    "tenure_in_month": "3",
                    "monthly_installment": 666658,
                    "bank_interest_rate": 150000,
                    "interest_pay_to_bank": 48974,
                    "total_offerred_discount_cashback_amount": 49000,
                    "loan_amount": 1951000,
                    "auth_amount": 2000000
                }
            ],
            "issuer_name": "YES",
            "is_debit_emi_issuer": false
        }
    ],
    "acquirer_data": {
        "acquirerId": 8004
    },
    "response_code": 1,
    "response_message": "SUCCESS"
}
```
```json 400 Bad Request
{
  "error_code": "14845",
  "error_message": "Request Data is not valid"
}
```
```json 500 Internal server Error
{
  "error_code": "14020",
  "error_message": "Oops, something went wrong!"
}
```
