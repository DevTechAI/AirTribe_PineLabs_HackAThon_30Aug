---
title: "Inquiry All Payments"
slug: "inquiry-all-payments-1"
excerpt: "This API Help to get Inquiry All Payments"
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Fri Feb 04 2022 11:22:12 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Oct 04 2022 11:53:43 GMT+0000 (Coordinated Universal Time)"
---
**Response Payload:** 

```json 200 Success
{
"payment_info_data": [
{
"acquirer_name": "Edge",
"auth_code": "NA",
"captured_amount_in_paisa": "200",
"card_holder_name": "dskfk",
"masked_card_number": "************1112",
"merchant_return_url": "http://localhost/PINE/pluralxt-pinelabs-php/response_page.php",
"mobile_no": "NA",
"payment_completion_date_time": "2022-02-11T18:39:54.973Z",
"payment_id": "1013950",
"payment_status": "CAPTURED",
"payment_response_code": "1",
"payment_response_message": "NA",
"product_code": "NA",
"rrn": "425847096720",
"refund_amount_in_paisa": "0",
"salted_card_hash": "CE88E1CF9247936231DB21D02498C6470625892F7FE4A6FAC2FE8F6A03D3E4AE",
"udf_field_1": "123",
"udf_field_2": "NA",
"udf_field_3": "NA",
"udf_field_4": "NA",
"udf_field_5": "NA",
"payment_mode": "CREDIT_DEBIT",
"issuer_name": "NONE",
"gateway_payment_id": "7306277",
"card_type": ""
}
],
"merchant_data": {
"merchant_id": 11565,
"order_id": "68P4681148P944I"
},
"order_data": {
"order_status": "CHARGED",
"plural_order_id": 34417,
"amount": 200,
"order_desc": "Test Order"
}
}
```
```json Partial refund
{
    "payment_info_data": [
        {
            "acquirer_name": "Edge",
            "auth_code": "NA",
            "captured_amount_in_paisa": "10000",
            "card_holder_name": "CardUser82o",
            "masked_card_number": "************1704",
            "merchant_return_url": "https://beta.nobroker.in/nbpay,http://192.168.101.93:7050/chargingresp.aspx,http://localhost/Pine/response1.php,http://10.200.146.139:7020/chargingrespnew.aspx",
            "mobile_no": "NA",
            "payment_completion_date_time": "2022-10-03T02:23:28.440Z",
            "payment_id": "1257333",
            "payment_status": "PARTIALLY_REFUNDED",
            "payment_response_code": "1",
            "payment_response_message": "NA",
            "product_code": "NA",
            "rrn": "425847096720",
            "refund_amount_in_paisa": "200",
            "salted_card_hash": "1969CC66531F443DABE1E71E684A3F307AB4A720F43380825D099F9438C9116D",
            "udf_field_1": "NA",
            "udf_field_2": "NA",
            "udf_field_3": "NA",
            "udf_field_4": "NA",
            "udf_field_5": "NA",
            "payment_mode": "CREDIT_DEBIT",
            "issuer_name": "NONE",
            "gateway_payment_id": "7630215",
            "card_type": ""
        }
    ],
    "merchant_data": {
        "merchant_id": 11471,
        "order_id": "nbpay293279392667184"
    },
    "order_data": {
        "order_status": "PARTIAL_REFUNDED",
        "plural_order_id": 96874,
        "amount": 10000,
        "order_desc": null
    }
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
    "0-2": "unique merchant id.",
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
    "6-0": "refund_amount",
    "6-1": "string",
    "6-2": "refund amount.",
    "7-0": "acquirer_name",
    "7-1": "string",
    "7-2": "acquirer name.",
    "8-0": "auth_code",
    "8-1": "string",
    "8-2": "authenticate code",
    "9-0": "captured_amount  \n\\_in_paisa",
    "9-1": "string",
    "9-2": "captured amount in paisa.",
    "10-0": "card_holder_name",
    "10-1": "string",
    "10-2": "cardholder name.",
    "11-0": "masked_card_number",
    "11-1": "string",
    "11-2": "masked card number.",
    "12-0": "merchant_return_url",
    "12-1": "string",
    "12-2": "merchant return url.",
    "13-0": "mobile_no",
    "13-1": "string",
    "13-2": "valid mobile number.",
    "14-0": "payment_completion  \n\\_date_time",
    "14-1": "string",
    "14-2": "payment completion  \ndate time.",
    "15-0": "payment_id",
    "15-1": "string",
    "15-2": "unique payment id.",
    "16-0": "payment_status",
    "16-1": "string",
    "16-2": "payment status.",
    "17-0": "payment_response  \n\\_code",
    "17-1": "string",
    "17-2": "paymentresponse codes.",
    "18-0": "payment_response  \n\\_message",
    "18-1": "string",
    "18-2": "Short payment message about code.",
    "19-0": "product_code",
    "19-1": "string",
    "19-2": "product code.",
    "20-0": "rrn",
    "20-1": "string",
    "20-2": "RRN number.",
    "21-0": "refund_amount  \n\\_in_paisa",
    "21-1": "string",
    "21-2": "refund amount in paisa.",
    "22-0": "salted_card_hash",
    "22-1": "string",
    "22-2": "salted card hash.",
    "23-0": "udf_field_1",
    "23-1": "string",
    "23-2": "UDF 1",
    "24-0": "udf_field_2",
    "24-1": "string",
    "24-2": "UDF 2",
    "25-0": "udf_field_3",
    "25-1": "string",
    "25-2": "UDF 3",
    "26-0": "udf_field_4",
    "26-1": "string",
    "26-2": "UDF 4",
    "27-0": "payment_mode",
    "27-1": "string",
    "27-2": "payment mode.",
    "28-0": "issuer_name",
    "28-1": "string",
    "28-2": "name of the issuer.",
    "29-0": "gateway\\_  \npayment_id",
    "29-1": "string",
    "29-2": "gateway payment id."
  },
  "cols": 3,
  "rows": 30,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]
