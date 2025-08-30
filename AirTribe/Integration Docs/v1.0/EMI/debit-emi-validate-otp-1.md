---
title: "Debit EMI: Validate OTP"
slug: "debit-emi-validate-otp-1"
excerpt: "This API Help to get Debit EMI: Validate OTP"
hidden: true
metadata: 
  image: []
  robots: "index"
createdAt: "Fri Feb 04 2022 14:14:15 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Feb 09 2022 11:53:55 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

| Attribute | Type    | Details                        |
| :-------- | :------ | :----------------------------- |
| otp\*     | integer | vaild otp to validate the EMI. |

**Request Body payload:** 

```json JSON
{"otp":"123456"}
```

**Response Payload:** 

```json 200 Success
{
    "api_url": "http://pluralqa.pinepg.in/api/v1/emi/order/confirmation?token=fsQNbaN6TfAu5wUbGD2ErbHi5BBJDphbu%2bU5PGgQ4OM%3d",
    "validate_otp_response": {
        "customer_name": "Harsh Kumar ",
        "interest_rate": 160000,
        "merchant_name": "Aditya Vision",
        "total_amount_in_paise": 1955000,
        "emi_amount_in_paise": 341207,
        "address": "Noida 62,201301",
        "tenure_in_months": "6",
        "last6digitaccountnumber": "872806",
        "otp_attempts_left": 0,
        "IsMaxAttemptsExcceded": false
    },
    "response_code": 14010,
    "response_message": SUCCESS
}
```
```json 400 Bad Request
{
  "error_code": "14806",
  "error_message": "Invalid OTP"
}
{
  "error_code": "14100",
  "error_message": "You have entered an incorrect OTP. Please enter the correct OTP"
}
```
```json 500 Internal Server Error

```
