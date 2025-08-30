---
title: "Process Payment UPI INTENT"
slug: "process-payment-upi-intent"
excerpt: "Use the below endpoint to Process Payment UPI Intent"
hidden: true
createdAt: "Tue Jan 03 2023 13:12:27 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:50:50 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

| Parameter Name  | Type   | Description                                                         |
| :-------------- | :----- | :------------------------------------------------------------------ |
| upi_option      | string | Default it will be UPI.                                             |
| txn_mode \*     | string | User need to provide  "INTENT" key word to perform the intent flow. |
| payment_mode    | string | Default it will be UPI.                                             |
| navigation_mode | string | Default it will be "SEAMLESS".                                      |

**Request Body payload:** 

```json JSON
{
    "upi_data": {
        "upi_option": "UPI",
        "txn_mode": "INTENT"
    },
    "txn_data": {
        "payment_mode": "UPI",
        "navigation_mode": "SEAMLESS"
    }
}
```

**Response Payload:** 

```json 200 Success
{
    "content": null,
    "payment_id": 1676890,
    "order_id": 75744,
    "amount_in_paise": 500,
    "timer_page_time_out_in_seconds": 180,
    "pg_upi_unique_request_id": null,
    "deep_link": "upi://pay?pa=setu1044442777674318986@kaypay&pn=Ravi%20Maurya&am=5.00&tr=1044442777674318986&tn=Payment%20for%207681067&cu=INR&mode=04",
    "short_link": "https://sandbox.bills.pe/wjm02tnrzq77",
    "response_code": 1,
    "response_message": "Payment Successful!"
}
```
```json 400 Bad Request
{
    "response_code": 11001,
    "response_message": "Sorry, your transaction has failed."
}
```

**Response Parameters** 

| Parameter Name                 | Type   | Description                           |
| :----------------------------- | :----- | :------------------------------------ |
| content                        | string | Html content to load the output data. |
| payment_id                     | long   | Unique payment id.                    |
| order_id                       | long   | Unique order id.                      |
| amount_in_paise                | long   | Amount paid in paise.                 |
| timer_page_time_out_in_seconds | int    | Timer for the page render.            |
| pg_upi_unique_request_id       | string | Unique Request Id                     |
| deep_link                      | string | Intent link for andriod devices.      |
| short_link                     | string | Intent link for IOS devices.          |
| response_code                  | string | Response code.                        |
| response_message               | string | Short message about code.             |

**Note**:  
For UPI Intent, every 5 sec inquiry call is mandatory on timer page to get status update.
