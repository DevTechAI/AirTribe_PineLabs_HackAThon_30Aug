---
title: "Object"
slug: "payment-object"
excerpt: "Overview of the Payments API responses."
hidden: false
createdAt: "Wed Aug 28 2024 11:57:19 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Oct 18 2024 06:59:27 GMT+0000 (Coordinated Universal Time)"
---
## Accept Payment API

Shown below is a sample response returned in our Accept Payment API.

```json Accept Payment Sample Response for Redirect Flow
{
  "token": "ubrjAgbVaJVrGz67y%2fZCjCveYWNymE7ULAlOO7FCbz4%3d",
  "response_code": 1,
  "response_message": "SUCCESS",
  "redirect_url": "http://hostname:port/api/v2/process/payment?token=ubrjAgbVaJVrGz67y%2fZCjCveYWNymE7ULAlOO7FCbz4% 3d "
}
```
```json Accept Payment Sample Response For Seamless Flow
{
  "token": "S03%2fbPRIyC1A6jR%2bmmQrUeW4oQEL4vFBA722BtwavAdQuw%3d",
  "response_code": 1,
  "response_message": "SUCCESS"
}
```

The table below lists the various parameters returned in the Accept payment API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "token",
    "0-1": "`string`",
    "0-2": "Unique token created for a transaction.  \n  \nExample: `S03%2fbPRIyC1A6jR%2bmmQrUeW4oQEL4vFBA722BtwavAdQuw%3d`  \n  \n**Note**: You need to pass this token in our Generate Payment Link API.",
    "1-0": "response_code",
    "1-1": "`integer`",
    "1-2": "The status of the API request.  \n  \nPossible value:<ul><li>`1`: Denotes success.</ul></li>",
    "2-0": "response_message",
    "2-1": "`string`",
    "2-2": "Message corresponding to the response code.  \n  \nExample: `SUCCESS`",
    "3-0": "redirect_url",
    "3-1": "`string`",
    "3-2": "Plural hosted checkout URL. Navigate your customers to this URL to accept payment.  \n  \nExample: `http\\://hostname:port/api/v2/process/payment?token=ubrjAgbVaJVrGz67y%2fZCjCveYWNymE7ULAlOO7FCbz4% 3d`  \n  \n**Note**: This parameter is returned for Redirect Mode only."
  },
  "cols": 3,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Process Payment API

Shown below are the sample responses returned in our Process Payment API.

```json Card Payment Sample Response
{
  "response_code": 1,
  "response_message": "SUCCESS",
  "redirect_url": "http://hostname:port/pinepg/v2/process/payment?token=848RFsu%2bRnNcSsaZdzEgkeosvCc2o5lK TV4uKJF%2fcjE%3d"
}
```
```json UPI Intent Sample Response
{
  "pg_upi_unique_request_id": "170724PLPre22116284",
  "deep_link": "upi://pay?pa=pl.pinelabs@pineaxis&pn=Pinelabs%20Private%20Limited%20dummy&am=8.00&mam=8.00&tr=SU01J2ZMXHX4PVBVASQJPBG2XW6V&tn=Payment%20for%20342027241&cu=INR&mc=7399",
  "pine_pg_transaction_id": 342027241,
  "short_link": "https://upipay.setu.co/nO6yP65XUmwh",
  "response_code": 1,
  "response_message": "SUCCESS"
}
```
```json UPI Collect Sample Reponse
{
  "response_code": 1,
  "response_message": "SUCCESS"
}
```

The table below lists the various parameters returned in the Generate payment link API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "pg_upi_unique_request_id",
    "0-1": "`string`",
    "0-2": "Unique identifier of the UPI request in the plural database.  \n  \nExample: `170724PLPre22116284`",
    "1-0": "deep_link",
    "1-1": "`string`",
    "1-2": "Deep link returned by the acquirer.  \n  \nExample: `upi://pay?pa=pl.pinelabs@pineaxis&pn=Pinelabs%20Private%20Limited%20dummy&am=8.00&mam=8.00&tr=SU01J2ZMXHX4PVBVASQJPBG2XW6V&tn=Payment%20for%20342027241&cu=INR&mc=7399`  \n  \n**Note**: Navigate your customer to this URL to process payment.",
    "2-0": "pine_pg_transaction_id",
    "2-1": "`integer`",
    "2-2": "Unique identifier of the transaction in the Plural database.  \n  \nExample: `342027241`",
    "3-0": "short_link",
    "3-1": "`string`",
    "3-2": "Use this link to redirect your customer to a QR code page.  \n  \nExample: `https://upipay.setu.co/nO6yP65XUmwh`",
    "4-0": "response_code",
    "4-1": "`integer`",
    "4-2": "The status of the API request.  \n  \nPossible value:<ul><li>`1`: Denotes success.</ul></li>",
    "5-0": "response_message",
    "5-1": "`string`",
    "5-2": "Message corresponding to the response code.  \n  \nExample:`success`"
  },
  "cols": 3,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 Note:
> 
> - For UPI Intent use the link generated to navigate your customer's to accept payment.
> - For UPI collect we send notifications to the customer's VPA handle.

## Inquiry/Refund API

Shown below is the sample responses returned in our Inquiry/Refund API.

```json Inquiry Sample Response
{
  "ppc_MerchantID": "123456",
  "ppc_MerchantAccessCode": "1a39a6d4-46b7-124d-929d-21bf0e9ed123",
  "ppc_PinePGTxnStatus": "7",
  "ppc_TransactionCompletionDateTime": "17/07/2024 12:41:54 PM",
  "ppc_UniqueMerchantTxnID": "testingedgeseamless1123145432",
  "ppc_Amount": "10000",
  "ppc_TxnResponseCode": "1",
  "ppc_TxnResponseMessage": "SUCCESS",
  "ppc_PinePGTransactionID": "342048376",
  "ppc_CapturedAmount": "100",
  "ppc_RefundedAmount": "0",
  "ppc_AcquirerName": "KOTAK_SETU",
  "ppc_DIA_SECRET": "9FFA2E99D14B6357E50D9AF2CF9D01D67B03FA1020BB88A82E76C962313FC004",
  "ppc_DIA_SECRET_TYPE": "SHA256",
  "ppc_PaymentMode": "10",
  "ppc_Parent_TxnStatus": "4",
  "ppc_ParentTxnResponseCode": "1",
  "ppc_ParentTxnResponseMessage": "SUCCESS",
  "ppc_UdfField1": "",
  "ppc_UdfField2": "",
  "ppc_UdfField3": "",
  "ppc_UdfField4": "",
  "ppc_RRN": "1721200204930238149",
  "ppc_AcquirerResponseCode": "SUCCESS",
  "ppc_AcquirerResponseMessage": "SUCCESS"
}
```
```json Refund Sample Response
{
  "ppc_MerchantID": "123456",
  "ppc_MerchantAccessCode": "1a39a6d4-46b7-124d-929d-21bf0e9ed123",
  "ppc_PinePGTxnStatus": "1",
  "ppc_TransactionCompletionDateTime": "01/08/2024 10:25:07 AM",
  "ppc_UniqueMerchantTxnID": "Refund_1",
  "ppc_Amount": "100",
  "ppc_TxnResponseCode": "2",
  "ppc_TxnResponseMessage": "REFUND PROCESS INITIATED",
  "ppc_PinePGTransactionID": "0",
  "ppc_CapturedAmount": "0",
  "ppc_RefundedAmount": "0",
  "ppc_ParentTxnResponseCode": "1",
  "ppc_Parent_TxnStatus": "4",
  "ppc_ParentTxnResponseMessage": "SUCCESS",
  "ppc_DIA_SECRET": "EE3844A2B85588D20AA173269BCC4F3375ABDEE8631CFF1366B271FABB47AE6F",
  "ppc_DIA_SECRET_TYPE": "SHA256"
}
```

The table below lists the various parameters returned in the Inquiry/Refund API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "ppc_MerchantID",
    "0-1": "`string`",
    "0-2": "Unique identifier of the merchant in Plural database.  \n  \nExample: `123456`",
    "1-0": "ppc_MerchantAccessCode",
    "1-1": "`string`",
    "1-2": "Unique access code of the merchant in Plural database.  \n  \nExample: `1a39a6d4-46b7-124d-929d-21bf0e9ed123`  \n  \n**Note**: The access key shared while onboarding if not received contact our Integration team.",
    "2-0": "ppc_PinePGTxnStatus",
    "2-1": "`string`",
    "2-2": "The status of the transaction.  \n  \nExample: `7`  \n  \n**Note**: Please refer to the Pine PG transaction status table to know the status.",
    "3-0": "ppc_TransactionCompletionDateTime",
    "3-1": "`string`",
    "3-2": "The date and time at which the transaction was completed.  \n  \nExample: `17/07/2024 12:41:54 PM`",
    "4-0": "ppc_UniqueMerchantTxnID",
    "4-1": "`string`",
    "4-2": "Unique merchant transaction ID.  \n  \nExample: `1234567890`  \n  \n**Note**: You must use the transaction ID passed in the accept payment API request.",
    "5-0": "ppc_Amount",
    "5-1": "`string`",
    "5-2": "The total transaction amount against the payment recieved.  \n  \nExample: `10000`",
    "6-0": "ppc_TxnResponseCode",
    "6-1": "`string`",
    "6-2": "The response status of the transaction.  \n  \nExample: `1`  \n  \n**Note**: Please refer to the Pine PG transaction status table to know the status.",
    "7-0": "ppc_TxnResponseMessage",
    "7-1": "`string`",
    "7-2": "Message corresponding to the response status of the transaction.  \n  \nExample: `SUCCESS`",
    "8-0": "ppc_PinePGTransactionID",
    "8-1": "`string`",
    "8-2": "Unique transaction ID generated by Plural against an Order ID.  \n  \nExample: `342048376`",
    "9-0": "ppc_CapturedAmount",
    "9-1": "`string`",
    "9-2": "The total amount captured.  \n  \nExample: `100`",
    "10-0": "ppc_RefundedAmount",
    "10-1": "`string`",
    "10-2": "The total amount refunded.  \n  \nExample: `0`",
    "11-0": "ppc_AcquirerName",
    "11-1": "`string`",
    "11-2": "The acquirer name for this transaction.  \n  \nExample: `KOTAK_SETU`",
    "12-0": "ppc_DIA_SECRET",
    "12-1": "`string`",
    "12-2": "HashMap secret key generated using the request payload and the secret key.  \n  \nExample: `9FFA2E99D14B6357E50D9AF2CF9D01D67B03FA1020BB88A82E76C962313FC004`",
    "13-0": "ppc_DIA_SECRET_TYPE",
    "13-1": "`string`",
    "13-2": "HashMap secret generation type.  \n  \nAccepted values:<ul><li>`SHA256`</li><li>`MD5`</ul></li>",
    "14-0": "ppc_PaymentMode",
    "14-1": "`string`",
    "14-2": "Payment mode selected for the particular transaction.  \n  \nExample: `10`: For UPI.",
    "15-0": "ppc_Parent_TxnStatus",
    "15-1": "`string`",
    "15-2": "The status code of the purchase transaction.  \n  \nExample: `4`",
    "16-0": "ppc_ParentTxnResponseCode",
    "16-1": "`string`",
    "16-2": "The response code for the purchase transaction.  \n  \nExample: `1`",
    "17-0": "ppc_ParentTxnResponseMessage",
    "17-1": "`string`",
    "17-2": "Message corresponding to the status and response code.  \n  \nExample: `SUCCESS`",
    "18-0": "ppc_UdfField1",
    "18-1": "`string`",
    "18-2": "User defined field1.  \n  \nExample: `DD`",
    "19-0": "ppc_UdfField2",
    "19-1": "`string`",
    "19-2": "User defined field2.  \n  \nExample: `XOF`",
    "20-0": "ppc_UdfField3",
    "20-1": "`string`",
    "20-2": "User defined field3.  \n  \nExample: `XOA`",
    "21-0": "ppc_UdfField4",
    "21-1": "`string`",
    "21-2": "User defined field4.  \n  \nExample: `ASD`",
    "22-0": "ppc_RRN",
    "22-1": "`string`",
    "22-2": "Unique Retrieval Reference Number of the transaction.  \n  \nExample: `1721200204930238149`",
    "23-0": "ppc_AcquirerResponseCode",
    "23-1": "`string`",
    "23-2": "The response code received from the acquirer.  \n  \nExample: `SUCCESS`",
    "24-0": "ppc_AcquirerResponseMessage",
    "24-1": "`string`",
    "24-2": "Message corresponding to the acquirer code.  \n  \nExample: `SUCCESS`"
  },
  "cols": 3,
  "rows": 25,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]
