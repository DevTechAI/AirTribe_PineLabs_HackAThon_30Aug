---
title: "EMI Calculator: Multi Cart Model"
slug: "emi-calculator-multi-cart-model-1"
excerpt: "This API Help to get EMI Calculator: Multi Cart Model"
hidden: true
createdAt: "Fri Feb 04 2022 13:30:37 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:52:14 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:**

| Attribute         | Type    | Details                                                                                                                                                                                                 |
| :---------------- | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| merchant_id\*     | integer | merchant_id is the unique identifier of the merchant. This id is assigned to you by Plural. You can find merchant_id under the credentials section of the settings section of Plural Console dashboard. |
| amount_in_paisa\* | long    | Amount is paise                                                                                                                                                                                         |
| product_code\*    | string  | Product code is the unique identifier of the product on which the offers details are intended to be fetched.                                                                                            |
| product_amount\*  | long    | Product amount in paise                                                                                                                                                                                 |

**Request Body payload:** 

```json JSON
{
    "merchant_data": {
        "merchant_id": 11607
    },
    "payment_data": {
        "amount_in_paisa": 2000000
    },
    "product_details": [
        {
            "product_code": "2000",
            "product_amount": 1000000
        },
        {
            "product_code": "2001",
            "product_amount": 1000000
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
                                        "scheme_id": "48916",
                                        "program_type": 112,
                                        "is_scheme_valid": true
                                    }
                                ],
                                "product_code": "2000",
                                "product_name": "2000",
                                "product_amount": 1000000,
                                "subvention_cashback_discount": 40000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 40000,
                                "product_discount_percentage": 0,
                                "subvention_type": 1,
                                "bank_interest_rate_percentage": 100000,
                                "bank_interest_rate": 16041
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
                                "subvention_cashback_discount": 40000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 40000,
                                "product_discount_percentage": 0,
                                "subvention_type": 1,
                                "bank_interest_rate_percentage": 100000,
                                "bank_interest_rate": 16041
                            }
                        ],
                        "emi_scheme": {
                            "scheme_id": "46918",
                            "program_type": 105,
                            "is_scheme_valid": true
                        }
                    },
                    "tenure_id": "3",
                    "tenure_in_month": "3",
                    "monthly_installment": 650695,
                    "bank_interest_rate": 100000,
                    "interest_pay_to_bank": 32085,
                    "total_offerred_discount_cashback_amount": 80000,
                    "loan_amount": 1920000,
                    "auth_amount": 1920000
                },
                {
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
                                "subvention_cashback_discount": 30000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 30000,
                                "product_discount_percentage": 0,
                                "subvention_type": 2,
                                "bank_interest_rate_percentage": 80000,
                                "bank_interest_rate": 22754
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
                                "subvention_cashback_discount": 30000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 30000,
                                "product_discount_percentage": 0,
                                "subvention_type": 2,
                                "bank_interest_rate_percentage": 80000,
                                "bank_interest_rate": 22754
                            }
                        ],
                        "emi_scheme": {
                            "scheme_id": "46918",
                            "program_type": 105,
                            "is_scheme_valid": true
                        }
                    },
                    "tenure_id": "6",
                    "tenure_in_month": "6",
                    "monthly_installment": 330918,
                    "bank_interest_rate": 80000,
                    "interest_pay_to_bank": 45508,
                    "total_offerred_discount_cashback_amount": 60000,
                    "loan_amount": 1940000,
                    "auth_amount": 1940000
                },
                {
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
                                        "scheme_id": "48935",
                                        "program_type": 112,
                                        "is_scheme_valid": true
                                    }
                                ],
                                "product_code": "2000",
                                "product_name": "2000",
                                "product_amount": 1000000,
                                "subvention_cashback_discount": 10000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 10000,
                                "product_discount_percentage": 0,
                                "subvention_type": 2,
                                "bank_interest_rate_percentage": 135000,
                                "bank_interest_rate": 22356
                            },
                            {
                                "schemes": [],
                                "product_code": "2001",
                                "product_name": "2001",
                                "product_amount": 1000000,
                                "subvention_cashback_discount": 0,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 0,
                                "product_discount_percentage": 0,
                                "subvention_type": 3,
                                "bank_interest_rate_percentage": 135000,
                                "bank_interest_rate": 22583
                            }
                        ],
                        "emi_scheme": {
                            "scheme_id": "48931",
                            "program_type": 105,
                            "is_scheme_valid": true
                        }
                    },
                    "tenure_id": "3",
                    "tenure_in_month": "3",
                    "monthly_installment": 678313,
                    "bank_interest_rate": 135000,
                    "interest_pay_to_bank": 44939,
                    "total_offerred_discount_cashback_amount": 10000,
                    "loan_amount": 1990000,
                    "auth_amount": 1990000
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
                                "schemes": [],
                                "product_code": "2000",
                                "product_name": "2000",
                                "product_amount": 1000000,
                                "subvention_cashback_discount": 0,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 0,
                                "product_discount_percentage": 0,
                                "subvention_type": 3,
                                "bank_interest_rate_percentage": 160000,
                                "bank_interest_rate": 67841
                            },
                            {
                                "schemes": [],
                                "product_code": "2001",
                                "product_name": "2001",
                                "product_amount": 1000000,
                                "subvention_cashback_discount": 0,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 0,
                                "product_discount_percentage": 0,
                                "subvention_type": 3,
                                "bank_interest_rate_percentage": 160000,
                                "bank_interest_rate": 67841
                            }
                        ],
                        "emi_scheme": {
                            "scheme_id": "48929",
                            "program_type": 105,
                            "is_scheme_valid": true
                        }
                    },
                    "tenure_id": "9",
                    "tenure_in_month": "9",
                    "monthly_installment": 237298,
                    "bank_interest_rate": 160000,
                    "interest_pay_to_bank": 135682,
                    "total_offerred_discount_cashback_amount": 0,
                    "loan_amount": 2000000,
                    "auth_amount": 2000000
                },
                {
                    "offer_scheme": {
                        "product_details": [
                            {
                                "schemes": [],
                                "product_code": "2000",
                                "product_name": "2000",
                                "product_amount": 1000000,
                                "subvention_cashback_discount": 0,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 0,
                                "product_discount_percentage": 0,
                                "subvention_type": 3,
                                "bank_interest_rate_percentage": 140000,
                                "bank_interest_rate": 77432
                            },
                            {
                                "schemes": [],
                                "product_code": "2001",
                                "product_name": "2001",
                                "product_amount": 1000000,
                                "subvention_cashback_discount": 0,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 0,
                                "product_discount_percentage": 0,
                                "subvention_type": 3,
                                "bank_interest_rate_percentage": 140000,
                                "bank_interest_rate": 77432
                            }
                        ],
                        "emi_scheme": {
                            "scheme_id": "48929",
                            "program_type": 105,
                            "is_scheme_valid": true
                        }
                    },
                    "tenure_id": "12",
                    "tenure_in_month": "12",
                    "monthly_installment": 179573,
                    "bank_interest_rate": 140000,
                    "interest_pay_to_bank": 154876,
                    "total_offerred_discount_cashback_amount": 0,
                    "loan_amount": 2000000,
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
                                        "scheme_id": "48925",
                                        "program_type": 112,
                                        "is_scheme_valid": true
                                    }
                                ],
                                "product_code": "2000",
                                "product_name": "2000",
                                "product_amount": 1000000,
                                "subvention_cashback_discount": 24500,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 24500,
                                "product_discount_percentage": 0,
                                "subvention_type": 2,
                                "bank_interest_rate_percentage": 110000,
                                "bank_interest_rate": 31528
                            },
                            {
                                "schemes": [],
                                "product_code": "2001",
                                "product_name": "2001",
                                "product_amount": 1000000,
                                "subvention_cashback_discount": 0,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 0,
                                "product_discount_percentage": 0,
                                "subvention_type": 3,
                                "bank_interest_rate_percentage": 110000,
                                "bank_interest_rate": 32324
                            }
                        ],
                        "emi_scheme": {
                            "scheme_id": "48928",
                            "program_type": 105,
                            "is_scheme_valid": true
                        }
                    },
                    "tenure_id": "6",
                    "tenure_in_month": "6",
                    "monthly_installment": 339892,
                    "bank_interest_rate": 110000,
                    "interest_pay_to_bank": 63852,
                    "total_offerred_discount_cashback_amount": 24500,
                    "loan_amount": 1975500,
                    "auth_amount": 1975500
                }
            ],
            "issuer_name": "Federal Debit",
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
                                        "scheme_id": "48933",
                                        "program_type": 112,
                                        "is_scheme_valid": true
                                    }
                                ],
                                "product_code": "2000",
                                "product_name": "2000",
                                "product_amount": 1000000,
                                "subvention_cashback_discount": 45000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 45000,
                                "product_discount_percentage": 0,
                                "subvention_type": 1,
                                "bank_interest_rate_percentage": 160000,
                                "bank_interest_rate": 45056
                            },
                            {
                                "schemes": [],
                                "product_code": "2001",
                                "product_name": "2001",
                                "product_amount": 1000000,
                                "subvention_cashback_discount": 0,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 0,
                                "product_discount_percentage": 0,
                                "subvention_type": 3,
                                "bank_interest_rate_percentage": 160000,
                                "bank_interest_rate": 47180
                            }
                        ],
                        "emi_scheme": {
                            "scheme_id": "48926",
                            "program_type": 105,
                            "is_scheme_valid": true
                        }
                    },
                    "tenure_id": "6",
                    "tenure_in_month": "6",
                    "monthly_installment": 341206,
                    "bank_interest_rate": 160000,
                    "interest_pay_to_bank": 92236,
                    "total_offerred_discount_cashback_amount": 45000,
                    "loan_amount": 1955000,
                    "auth_amount": 1955000
                },
                {
                    "offer_scheme": {
                        "product_details": [
                            {
                                "schemes": [
                                    {
                                        "scheme_id": "48933",
                                        "program_type": 112,
                                        "is_scheme_valid": true
                                    }
                                ],
                                "product_code": "2000",
                                "product_name": "2000",
                                "product_amount": 1000000,
                                "subvention_cashback_discount": 40000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 40000,
                                "product_discount_percentage": 0,
                                "subvention_type": 2,
                                "bank_interest_rate_percentage": 140000,
                                "bank_interest_rate": 56856
                            },
                            {
                                "schemes": [],
                                "product_code": "2001",
                                "product_name": "2001",
                                "product_amount": 1000000,
                                "subvention_cashback_discount": 0,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 0,
                                "product_discount_percentage": 0,
                                "subvention_type": 3,
                                "bank_interest_rate_percentage": 140000,
                                "bank_interest_rate": 59228
                            }
                        ],
                        "emi_scheme": {
                            "scheme_id": "48926",
                            "program_type": 105,
                            "is_scheme_valid": true
                        }
                    },
                    "tenure_id": "9",
                    "tenure_in_month": "9",
                    "monthly_installment": 230677,
                    "bank_interest_rate": 140000,
                    "interest_pay_to_bank": 116093,
                    "total_offerred_discount_cashback_amount": 40000,
                    "loan_amount": 1960000,
                    "auth_amount": 1960000
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
                                        "scheme_id": "48924",
                                        "program_type": 112,
                                        "is_scheme_valid": true
                                    }
                                ],
                                "product_code": "2000",
                                "product_name": "2000",
                                "product_amount": 1000000,
                                "subvention_cashback_discount": 40000,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 40000,
                                "product_discount_percentage": 0,
                                "subvention_type": 2,
                                "bank_interest_rate_percentage": 134100,
                                "bank_interest_rate": 54426
                            },
                            {
                                "schemes": [],
                                "product_code": "2001",
                                "product_name": "2001",
                                "product_amount": 1000000,
                                "subvention_cashback_discount": 0,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 0,
                                "product_discount_percentage": 0,
                                "subvention_type": 3,
                                "bank_interest_rate_percentage": 134100,
                                "bank_interest_rate": 56699
                            }
                        ],
                        "emi_scheme": {
                            "scheme_id": "48927",
                            "program_type": 105,
                            "is_scheme_valid": true
                        }
                    },
                    "tenure_id": "9",
                    "tenure_in_month": "9",
                    "monthly_installment": 230126,
                    "bank_interest_rate": 134100,
                    "interest_pay_to_bank": 111134,
                    "total_offerred_discount_cashback_amount": 40000,
                    "loan_amount": 1960000,
                    "auth_amount": 1960000
                },
                {
                    "offer_scheme": {
                        "product_details": [
                            {
                                "schemes": [
                                    {
                                        "scheme_id": "48924",
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
                                "bank_interest_rate_percentage": 110000,
                                "bank_interest_rate": 59356
                            },
                            {
                                "schemes": [],
                                "product_code": "2001",
                                "product_name": "2001",
                                "product_amount": 1000000,
                                "subvention_cashback_discount": 0,
                                "product_discount": 0,
                                "subvention_cashback_discount_percentage": 0,
                                "product_discount_percentage": 0,
                                "subvention_type": 3,
                                "bank_interest_rate_percentage": 110000,
                                "bank_interest_rate": 60572
                            }
                        ],
                        "emi_scheme": {
                            "scheme_id": "48927",
                            "program_type": 105,
                            "is_scheme_valid": true
                        }
                    },
                    "tenure_id": "12",
                    "tenure_in_month": "12",
                    "monthly_installment": 174994,
                    "bank_interest_rate": 110000,
                    "interest_pay_to_bank": 119928,
                    "total_offerred_discount_cashback_amount": 20000,
                    "loan_amount": 1980000,
                    "auth_amount": 1980000
                }
            ],
            "issuer_name": "Kotak Debit",
            "is_debit_emi_issuer": true
        }
    ],
    "acquirer_data": {
        "acquirerId": 8004
    },
    "response_code": 14010,
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
