---
title: "Fetch Vault"
slug: "fetch-vault-1"
excerpt: "Use the below endpoint to Fetch Vault."
hidden: true
createdAt: "Thu Feb 03 2022 08:35:12 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:49:27 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

| Attribute        | Type    | Details                                 |
| :--------------- | :------ | :-------------------------------------- |
| customer_token\* | string  | vaild Token to be set for the customer. |
| payment_modes    | integer | valid payment modes value.              |

**Request Query Param:** 

```json JSON
customer_token=AGxVyLz65ucoJrx+w1u1xQ==
```

**Request Body payload:** 

```json JSON
{
    "payment_modes": [ 1 ]
}
```

**Response Payload:** 

```json 200 Success
{
  "card_details": [
    {
      "masked_card_number": "401200******1112",
      "expiry_year": "2023",
      "expiry_month": "12",
      "card_holder_name": "harsh",
      "saved_credential_token": "chYeVuIZ6NSHoAR4W8C+0A==",
      "assosiciation_type": "MASTERCARD",
      "is_debit_card_emi": false,
      "issuer_name": "HDFC",
      "card_type_id": 0
    }
  ]
}
```
```json 400 Bad Request
{
  "error_code": "16200",
  "error_message": "FETCHING_SAVE_VAULT_DATA_FAILED"
}
```
```json 500 Internal Server Error
{
  "error_code": "16010",
  "error_message": "Oops, something went wrong!"
}
```
