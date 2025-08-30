---
title: "Inquiry All Refunds"
slug: "inquiry-all-refunds-1"
excerpt: "This API Help to get Inquiry All Refunds"
hidden: true
createdAt: "Fri Feb 04 2022 11:29:21 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:53:37 GMT+0000 (Coordinated Universal Time)"
---
**Response Payload:** 

```json 200 Success
{
    "merchant_data": {
        "merchant_id": 11565,
        "order_id": "E37L74P3A65P660"
    },
    "order_data": {
        "order_status": "REFUNDED",
        "plural_order_id": 33890,
        "amount": 200,
        "order_desc": "TEST"
    },
    "payment_info_data": [
        {
            "acquirer_name": "RazorPay",
            "captured_amount_in_paisa": "0",
            "refund_amount_in_paisa": "200",
            "payment_completion_date_time": "NA",
            "payment_id": "1013170",
            "payment_status": "REFUNDED",
            "payment_response_code": "1",
            "payment_response_message": "NA",
            "rrn": "NA",
            "unique_request_id": "E37L74P3A65P660",
            "refund_id": "1013279",
            "payment_mode": "WALLET",
            "gateway_transaction_id": "rfnd_Iqghc3OQbb3A7w"
        }
    ]
}
```
```json Partial refunds transaction
{
    "merchant_data": {
        "merchant_id": 11471,
        "order_id": "nbpay293279392667184"
    },
    "order_data": {
        "order_status": "PARTIAL_REFUNDED",
        "plural_order_id": 96874,
        "amount": 10000,
        "order_desc": null
    },
    "payment_info_data": [
        {
            "acquirer_name": "Edge",
            "captured_amount_in_paisa": "0",
            "refund_amount_in_paisa": "200",
            "payment_completion_date_time": "NA",
            "payment_id": "1257333",
            "payment_status": "REFUNDED",
            "payment_response_code": "1",
            "payment_response_message": "NA",
            "rrn": "NA",
            "unique_request_id": "nbpay293279392667184",
            "refund_id": "1257377",
            "payment_mode": "CREDIT_DEBIT",
            "gateway_transaction_id": "7630357"
        }
    ]
}
```

**Response Parameters** 

[block:parameters]
{
  "data": {
    "h-0": "Parameter Name",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant_id",
    "0-1": "string",
    "0-2": "unique merchant id",
    "1-0": "order_id",
    "1-1": "string",
    "1-2": "unique order id.",
    "2-0": "order_status",
    "2-1": "string",
    "2-2": "status of the order.",
    "3-0": "plural_order_id",
    "3-1": "string",
    "3-2": "unique plural order id.",
    "4-0": "amount",
    "4-1": "long",
    "4-2": "amount in paise.",
    "5-0": "order_desc",
    "5-1": "string",
    "5-2": "order arrangement.",
    "6-0": "acquirer_name",
    "6-1": "string",
    "6-2": "acquirer name.",
    "7-0": "captured_amount  \n\\_in_paisa",
    "7-1": "string",
    "7-2": "captured amount in paisa.",
    "8-0": "refund_amount  \n\\_in_paisa",
    "8-1": "string",
    "8-2": "refund amount.",
    "9-0": "payment_completion  \n\\_date_time",
    "9-1": "string",
    "9-2": "payment completion  \ndate time.",
    "10-0": "payment_id",
    "10-1": "string",
    "10-2": "unique payment id.",
    "11-0": "payment_status",
    "11-1": "string",
    "11-2": "payment status.",
    "12-0": "payment_response  \n\\_code",
    "12-1": "string",
    "12-2": "payment response codes.",
    "13-0": "payment_response  \n\\_message",
    "13-1": "string",
    "13-2": "Short payment message about code.",
    "14-0": "rrn",
    "14-1": "string",
    "14-2": "RRN number.",
    "15-0": "unique_request_id",
    "15-1": "string",
    "15-2": "unique request id.",
    "16-0": "refund_id\tstring",
    "16-1": "unique",
    "16-2": "refund id.",
    "17-0": "payment_mode",
    "17-1": "string",
    "17-2": "payment mode.",
    "18-0": "gateway_transaction_id",
    "18-1": "string",
    "18-2": "gateway payment id."
  },
  "cols": 3,
  "rows": 19,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]
