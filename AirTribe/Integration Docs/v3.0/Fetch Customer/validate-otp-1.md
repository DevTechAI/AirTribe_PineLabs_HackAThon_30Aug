---
title: "Validate OTP"
slug: "validate-otp-1"
excerpt: "Use the below endpoint to Validate OTP."
hidden: true
createdAt: "Thu Feb 03 2022 08:19:01 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:49:04 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

| Attribute   | Type   | Details                                 |
| :---------- | :----- | :-------------------------------------- |
| otp_token\* | string | vaild Token to be set for the customer. |
| otp\*       | string | vaild otp to be set for the url.        |

**Request Query Param:** 

```json JSON
otp_token=xxxx&otp=xxx
```

**Response Payload:** 

```json 200 Success
true
```
```json 400 Bad Request
{
  "error_code": "16260",
  "error_message": "INVALID_OTP_TOKEN"
}

{
  "error_code": "16080",
  "error_message": "OTP_EXPIRED"
}

{
  "error_code": "16090",
  "error_message": "MAX_OTP_ATTEMPTED_REACHED"
}
```
```json 500 Internal Server Error
{
  "error_code": "16010",
  "error_message": "Oops, something went wrong!"
}
```
