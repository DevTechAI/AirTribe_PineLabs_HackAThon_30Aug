---
title: "Available Events"
slug: "webhook-available-events"
excerpt: "Overview of webhook events available on Plural."
hidden: false
createdAt: "Tue Sep 17 2024 09:47:00 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Oct 21 2024 11:45:21 GMT+0000 (Coordinated Universal Time)"
---
The table below list the various webhook events triggerd during the redirect checkout.

| Webhook Events           | Description                                          |
| :----------------------- | :--------------------------------------------------- |
| `payment.captured`       | Triggered when the payment is captured successfully. |
| `payment.completion`     | Triggered when the payment is successfully received. |
| `payment.failed`         | Triggered when the payment gets failed.              |
| `payment.refund.success` | Triggered when the payment refund is successful.     |
| `payment.refund.failed`  | Triggered when the payment refund is failed.         |
| `payment.pending`        | Triggered when the payment is pending for captured.  |

## Sample Payloads

### Payment Captured

Triggered when the payment is captured successfully.

```json Card Payment
{
  "event_name": "payment.captured",
  "merchant_response": {
    "merchant_id": "29792",
    "payment_mode": "EMI",
    "merchant_access_code": "d860a376-2182-4448-9d87-2b2c752b8991",
    "unique_merchant_txn_id": "c-947711168513-03070150-1",
    "pine_pg_txn_status": "4",
    "txn_completion_date_time": "03/03/2024 12:33:02 PM",
    "product_code": "273865",
    "captured_amount_in_paisa": "13559000",
    "refund_amount_in_paisa": "0",
    "txn_response_code": "1",
    "amount_in_paisa": "14059000",
    "txn_response_msg": "SUCCESS",
    "acquirer_name": "HDFC_FSS_IN_HOUSE",
    "pine_pg_transaction_id": "294774500",
    "rrn": "406358019945",
    "auth_code": "055712",
    "masked_card_number": "************2562",
    "card_holder_name": "name",
    "mobile_no": "9810505359",
    "salted_card_hash": "651BB095DE12C950EF09401518017A06C5DC1A1FE5D0E7782A373F7CFB5482A3",
    "udf_field_1": "110014C25 1st FloorJangpura extension jangpura new delhiDELHIDELHI",
    "udf_field_2": "492001Hudco Regional Office 1B Surya ApartmentsKatora Talab Civil Lines RaipurRAIPURCHHATTISGARH",
    "udf_field_3": "273865",
    "udf_field_4": "01eae2ec05761000bbea86e16dcb4b79CROMA41646",
    "emi_tenure_month": "1",
    "emi_interest_rate_percent": "0.00",
    "emi_principal_amount_in_paisa": "13559000",
    "emi_amount_payable_each_month_in_paisa": "0",
    "is_brand_emi_txn": "1",
    "emi_cashback_type": "0",
    "parent_txn_status": "",
    "parent_txn_response_code": "",
    "parent_txn_response_message": "",
    "issuer_name": "HDFC",
    "product_category": "MacBook Air",
    "manufacturer": "Apple Macbook",
    "product_discount": "500000"
  }
}
```
```json Net Banking
{
  "event_name": "payment.captured",
  "merchant_response": {
    "merchant_id": "106600",
    "merchant_access_code": "bcf441be-411b-46a1-aa88-c6e852a7d68c",
    "unique_merchant_txn_id": "103032654052977513",
    "pine_pg_txn_status": "4",
    "txn_completion_date_time": "25/04/2022 01:41:55 PM",
    "amount_in_paisa": "1000000",
    "txn_response_code": "1",
    "txn_response_msg": "SUCCESS",
    "acquirer_name": "BILLDESK",
    "pine_pg_transaction_id": "7378878",
    "captured_amount_in_paisa": "1000000",
    "refund_amount_in_paisa": "0",
    "payment_mode": "NET_BANKING",
    "parent_txn_status": "",
    "parent_txn_response_code": "",
    "parent_txn_response_message": ""
  }
}
```

### Payment Completion

Triggered when the payment is successfully received.

```json UPI Payment
{
  "event_name": "payment.completion",
  "merchant_response": {
    "merchant_id": "324915",
    "payment_mode": "UPI",
    "merchant_access_code": "a46ee454-20c9-4dd8-8c4e-1773bc631c4c",
    "unique_merchant_txn_id": "6363240303123137",
    "pine_pg_txn_status": "4",
    "txn_completion_date_time": "03/03/2024 12:32:22 PM",
    "captured_amount_in_paisa": "208450",
    "refund_amount_in_paisa": "0",
    "txn_response_code": "1",
    "amount_in_paisa": "208450",
    "txn_response_msg": "SUCCESS",
    "acquirer_name": "UPI_HDFC",
    "pine_pg_transaction_id": "294774320",
    "rrn": "406348028427",
    "auth_code": "NA",
    "parent_txn_status": "",
    "parent_txn_response_code": "",
    "parent_txn_response_message": ""
  }
}
```

### Payment Failed

Triggered when the payment is failed.

```json Card Payment
{
  "event_name": "payment.failed",
  "merchant_response": {
    "merchant_id": "321999",
    "payment_mode": "CREDIT_DEBIT_CARD",
    "merchant_access_code": "0164c5ab-bdec-4072-ba65-2705a7d167e2",
    "unique_merchant_txn_id": "op-202403030706319383572-1",
    "pine_pg_txn_status": "-7",
    "txn_completion_date_time": "03/03/2024 12:37:25 PM",
    "captured_amount_in_paisa": "0",
    "refund_amount_in_paisa": "0",
    "txn_response_code": "-1",
    "amount_in_paisa": "2699900",
    "txn_response_msg": "FAILURE",
    "acquirer_name": "HDFC_FSS_IN_HOUSE",
    "pine_pg_transaction_id": "294775759",
    "rrn": "406379027843",
    "masked_card_number": "************7523",
    "card_holder_name": "name",
    "mobile_no": "9597874830",
    "salted_card_hash": "1C857604514EC029415325BE2DB5B0AC6627CF6AC9EA429FF005F68A1B99E1FE",
    "udf_field_1": "M112403036446004968",
    "parent_txn_status": "",
    "parent_txn_response_code": "",
    "parent_txn_response_message": ""
  }
}
```

### Payment Refund Success

Triggered when the payment refund is successful.

```json UPI Payment
{
    "event_name": "payment.refund.success",
    "merchant_response": {
        "merchant_id": "325742",
        "payment_mode": "UPI",
        "merchant_access_code": "fb5d3fe0-340f-49bd-bd28-7026646744b0",
        "unique_merchant_txn_id": "325742_0103202412284150866_325742_0103202417002419855",
        "pine_pg_txn_status": "6",
        "txn_completion_date_time": "02/03/2024 09:36:25 AM",
        "captured_amount_in_paisa": "0",
        "refund_amount_in_paisa": "730000",
        "txn_response_code": "1",
        "amount_in_paisa": "730000",
        "txn_response_msg": "SUCCESS",
        "acquirer_name": "KOTAK_SETU",
        "pine_pg_transaction_id": "294176488",
        "rrn": "1706959061633674606",
        "parent_txn_status": "",
        "parent_txn_response_code": "",
        "parent_txn_response_message": ""
    }
}
```

### Payment Refund Failed

Triggered when the payment refund is failed.

```json Card Payment
{
    "event_name": "payment.refund.failed",
    "merchant_response": {
        "merchant_id": "29792",
        "merchant_access_code": "d860a376-2182-4448-9d87-2b2c752b8991",
        "unique_merchant_txn_id": "erfce7e85eefe34dc5bb",
        "pine_pg_txn_status": "-7",
        "txn_completion_date_time": "20/10/2024 09:50:03 AM",
        "amount_in_paisa": "2184800",
        "txn_response_code": "-78",
        "txn_response_msg": "Credit Greater Than Debit",
        "acquirer_name": "HDFC_FSS_IN_HOUSE",
        "pine_pg_transaction_id": "426714139",
        "captured_amount_in_paisa": "0",
        "refund_amount_in_paisa": "0",
        "payment_mode": "EMI",
        "parent_txn_status": "",
        "parent_txn_response_code": "",
        "parent_txn_response_message": ""
    }
}
```

### Payment Pending

Triggered when the payment is pending for captured.

```json UPI Payment
{
  "event_name": "payment.pending",
  "merchant_response": {
    "merchant_id": "312827",
    "payment_mode": "UPI",
    "merchant_access_code": "07ccfc3c-a880-425a-b1f4-bf2511799224",
    "unique_merchant_txn_id": "makeO-ord_yuiGhYrKodXbE9-1",
    "pine_pg_txn_status": "1",
    "txn_completion_date_time": "03/03/2024 12:41:03 PM",
    "captured_amount_in_paisa": "0",
    "refund_amount_in_paisa": "0",
    "txn_response_code": "-966",
    "amount_in_paisa": "9900",
    "txn_response_msg": "Debit Failure",
    "acquirer_name": "KOTAK_SETU",
    "pine_pg_transaction_id": "294776679",
    "rrn": "1709449852127361869",
    "udf_field_2": "ICICI10",
    "parent_txn_status": "",
    "parent_txn_response_code": "",
    "parent_txn_response_message": ""
  }
}
```
