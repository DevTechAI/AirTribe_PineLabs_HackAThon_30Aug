---
title: "Refund"
slug: "refund-1"
excerpt: "This API Help to Refund."
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Fri Feb 04 2022 09:13:36 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Oct 04 2022 14:40:23 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

| Parameter Name    | Type    | Description                               |
| :---------------- | :------ | :---------------------------------------- |
| unique_txn_id\*   | string  | valid transaction unique id is generated. |
| amount_in_paise\* | long    | valid total amount in paise.              |
| merchant_id\*     | integer | vaild merchant id.                        |
| order_id\*        | integer | vaild order id of product.                |
| payment_id\*      | integer | valid payment id generated one.           |

**Request Body payload:** 

```json Sample payload for Base64
{
   "unique_txn_id":"RefundTwXN_03",
   "amount_in_paise":100,
   "merchant_id":11607,
   "order_id":106730,
   "payment_id":438381
}
```
```json Partial refund
{
    "unique_txn_id": "RefundMicro000211",
    "amount_in_paise": 200,
    "merchant_id": 11471,
    "order_id": 96874,
    "payment_id": 1257333
}
```

**Request Base64 Body payload:** 

```json Sample Request
{
    "request": "ewogICAidW5pcXVlX3R4bl9pZCI6IlJlZnVuZFR3WE5fMDMiLAogICAiYW1vdW50X2luX3BhaXNlIjoxMDAsCiAgICJtZXJjaGFudF9pZCI6MTE2MDcsCiAgICJvcmRlcl9pZCI6MTA2NzMwLAogICAicGF5bWVudF9pZCI6NDM4MzgxCn0="
}
```
```json Partial refund
{"request": "ew0KICAgICJ1bmlxdWVfdHhuX2lkIjogIlJlZnVuZE1pY3JvMDAwMjExIiwNCiAgICAiYW1vdW50X2luX3BhaXNlIjogMjAwLA0KICAgICJtZXJjaGFudF9pZCI6IDExNDcxLA0KICAgICJvcmRlcl9pZCI6IDk2ODc0LA0KICAgICJwYXltZW50X2lkIjogMTI1NzMzMw0KfQ==" }
```

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
    "payment_info_data": {
        "acquirer_name": "RAZOR_PAY",
        "captured_amount_in_paisa": "0",
        "refund_amount_in_paisa": "200",
        "payment_completion_date_time": "NA",
        "payment_id": "NA",
        "payment_status": "REFUNDED",
        "payment_response_code": "1",
        "payment_response_message": "NA",
        "rrn": "NA",
        "unique_request_id": "NA",
        "refund_id": "1013279",
        "payment_mode": "WALLET",
        "gateway_transaction_id": "rfnd_Iqghc3OQbb3A7w"
    }
}
```
```json Partial refund
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
    "payment_info_data": {
        "acquirer_name": "EDGE",
        "captured_amount_in_paisa": "0",
        "refund_amount_in_paisa": "200",
        "payment_completion_date_time": "NA",
        "payment_id": "NA",
        "payment_status": "REFUNDED",
        "payment_response_code": "1",
        "payment_response_message": "NA",
        "rrn": "NA",
        "unique_request_id": "NA",
        "refund_id": "1257377",
        "payment_mode": "CREDIT_DEBIT",
        "gateway_transaction_id": "7630357"
    }
}
```
