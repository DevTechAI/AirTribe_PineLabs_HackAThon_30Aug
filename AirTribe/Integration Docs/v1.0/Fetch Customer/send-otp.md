---
title: "Send OTP"
slug: "send-otp"
excerpt: "Use the below endpoint to send OTP."
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Thu Feb 03 2022 07:40:55 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Jul 31 2023 11:26:55 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

| Attribute        | Type   | Details                                 |
| :--------------- | :----- | :-------------------------------------- |
| customer_token\* | string | vaild Token to be set for the customer. |

**Request Query Param:** 

```json JSON
customer_token=ZFhzD5JEumvXURWWNCEJBQ==
```

**Response Payload:** 

```json 200 Success
{
  "otp_token": "hB76D6sIDlZ8JIchzezQcA==",
  "otp_timer_in_seconds": 360
}
```
```json 400 Bad Request
{
  "error_code": "16050",
  "error_message": "CUSTOMER_NOT_FOUND"
}
```
```json 500 Internal Server Error
{
  "error_code": "16070",
  "error_message": "FAILURE_IN_SENDING_SMS"
}
{
  "error_code": "16010",
  "error_message": "Oops, something went wrong!"
}
```
