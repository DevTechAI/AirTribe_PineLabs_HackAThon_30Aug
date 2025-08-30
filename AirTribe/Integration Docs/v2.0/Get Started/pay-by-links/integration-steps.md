---
title: "Integration Steps"
slug: "integration-steps"
excerpt: "Discover how to integrate Plural Pay by Links APIs to easily generate a payment link."
hidden: true
createdAt: "Mon Nov 11 2024 04:42:14 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Nov 28 2024 08:40:29 GMT+0000 (Coordinated Universal Time)"
---
## Integration Step

To integrate Pay by Links, follow this step:

### Create Payment Link

Integrate our Create Payment Link API in your backend servers to create the Payment Link.

Use the below endpoint to create a payment link.

```text Create Payment Link Endpoint for UAT
POST: https://uat.pinepg.in/api/PaymentURL/CreatePaymentURL
```
```text Create Payment Link Endpoint for PROD
POST: https://pinepg.in/api/PaymentURL/CreatePaymentURL
```

Below is a sample request and response for the Create Payment Link API.

```json Sample Request
{
curl --location 'https://uat.pinepg.in/api/PaymentURL/CreatePaymentURL' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: TS01385dd8=011bd729b034eb8e8135594e3f4c1d0ef3824bd7d5def20985983a21614dcba8d88cd327e877d24e2407ce81d06573d568cd6953d1; TS01922b00=012ce8bebce0d7fd4184a2d056e6cad909c1a590b1c4d8e0a38524267b66b55c3bb3e16b64120908c846a3a057f240ec42027d003c; TS01385dd8=011bd729b0f04b211c7467c2acd534a73153be1346e89f446af60bbf9c84cdabdecb6ad3f39420b00a384d0b1eb42e22d57ed4172b' \
--data-urlencode 'MERCHANT_ID=106600' \
--data-urlencode 'MERCHANT_ACCESS_CODE=bcf441be-411b-46a1-aa88-c6e852a7d68c' \
--data-urlencode 'AMOUNT=20000' \
--data-urlencode 'REFERENCE_NO=pl_644123' \
--data-urlencode 'CUSTOMER_MOBILE_NO=8147986823' \
--data-urlencode 'CUSTOMER_EMAIL_ID=meghana.r@pinelabs.com' \
--data-urlencode 'PAYMENT_MODE=1'
}
```
```json Sample Response
{
    "RESPONSE_CODE": 1,
    "RESPONSE_MESSAGE": "SUCCESS",
    "PAYMENT_URL": "https://pyn.onl/PLUTUS/m81hnc1",
    "PAYMENT_LINK_ID": 5275034
}
```

#### JSON Parameters

<details>

<summary>Click Here</summary>

The table below lists the various JSON parameters.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "`MERCHANT_ID`",
    "0-1": "`Int`",
    "0-2": "`M`",
    "0-3": "Unique identifier of the merchant in Plural database.  \n Example: `106598`",
    "1-0": "`MERCHANT_ACCESS_CODE`",
    "1-1": "`String`",
    "1-2": "`M`",
    "1-3": "Unique access code of the merchant in Plural database.  \n  \n Example: `1a39a6d4-46b7-124d-929d-21bf0e9ed123`  \n  \n**Note**: The access key shared while onboarding if not received contact our Integration team.",
    "2-0": "`REFERENCE_NO`",
    "2-1": "`String`",
    "2-2": "`M`",
    "2-3": "Reference number of merchant which is maintained by pine labs.  \n(Max length is 100)",
    "3-0": "`AMOUNT`",
    "3-1": "`Int64`",
    "3-2": "`M`",
    "3-3": "Amount in paise",
    "4-0": "`PAYMENT_MODE`",
    "4-1": "`String`",
    "4-2": "`M`",
    "4-3": "The payment mode you prefer to accept payment.  \n  \nAccepted values:  \n1: CREDIT/DEBIT CARD  \n3: NET BANKING  \n4:CREDIT EMI  \n10: UPI  \n11: WALLET  \n14: DEBIT EMI  \n16: PREBOOKING  \n17: BNPL/FLEXIPAY  \n19: Cardless EMI  \n20: PBP (Paybypoints)",
    "5-0": "`PRODUCT_DESCRIPTION`",
    "5-1": "`String`",
    "5-2": "`O`",
    "5-3": "Description of product/service",
    "6-0": "`PRODUCT_CODE`",
    "6-1": "`String`",
    "6-2": "`O`",
    "6-3": "Merchant product code (required if brand EMI enabled)",
    "7-0": "`CUSTOMER_MOBILE_NO`",
    "7-1": "`String`",
    "7-2": "`O`",
    "7-3": "Customer's 10-digit mobile number",
    "8-0": "`CUSTOMER_EMAIL_ID`",
    "8-1": "`String`",
    "8-2": "`O`",
    "8-3": "Customer's email address"
  },
  "cols": 4,
  "rows": 9,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


</details>

#### Resend Payment Link

- Use an HTTP POST request to access the Resend SMS-Email API.
- This API will resend the SMS or email containing the payment link to the customer.

Use the below endpoint to send payment link.

```text Resend Payment Link Endpoint for UAT
POST: https://uat.pinepg.in/api/PaymentURL/ResendSmsEmail
```
```text Resend Payment Link Endpoint for PROD
POST: https://pinepg.in/api/PaymentURL/ResendSmsEmail
```

Below is a sample request and response for the Resend Payment Link API.

```json Sample Request
{
curl --location 'https://uat.pinepg.in/api/PaymentURL/ResendSmsEmail' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: TS01385dd8=011bd729b034eb8e8135594e3f4c1d0ef3824bd7d5def20985983a21614dcba8d88cd327e877d24e2407ce81d06573d568cd6953d1; TS01922b00=012ce8bebce0d7fd4184a2d056e6cad909c1a590b1c4d8e0a38524267b66b55c3bb3e16b64120908c846a3a057f240ec42027d003c; TS01385dd8=011bd729b03490ec937b5a39b2dff1a49d2ed0caa5d6ba9a531e7c490b620416468fc3e7ed6eb1db5ffad7111dcabd1d675c8f0081' \
--data-urlencode 'MERCHANT_ID=106600' \
--data-urlencode 'MERCHANT_ACCESS_CODE=bcf441be-411b-46a1-aa88-c6e852a7d68c' \
--data-urlencode 'PAYMENT_LINK_ID=5275034'
}
```
```json Sample Response
{
    "RESPONSE_CODE": 1,
    "RESPONSE_MESSAGE": "SUCCESS"
}
```

#### JSON Parameters

<details>

<summary>Click Here</summary>

The table below lists the various JSON parameters.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "`MERCHANT_ID`",
    "0-1": "`Int`",
    "0-2": "`M`",
    "0-3": "Unique identifier of the merchant in Plural database.  \n Example: `106598`",
    "1-0": "`MERCHANT_ACCESS_CODE`",
    "1-1": "`String`",
    "1-2": "`M`",
    "1-3": "Unique access code of the merchant in Plural database.  \n  \nExample: `1a39a6d4-46b7-124d-929d-21bf0e9ed123`  \n  \n**Note**: The access key shared while onboarding if not received contact our Integration team.",
    "2-0": "`PAYMENT_LINK_ID`",
    "2-1": "`Int64`",
    "2-2": "`M`",
    "2-3": "Payment ID which comes in response parameter of create payment link API"
  },
  "cols": 4,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


</details>

## Handle Payments

### Get Payment Status

Use the below endpoint to Get Status link.

```text Get Payment Status Link Endpoint for UAT
POST: https://uat.pinepg.in/api/PaymentURL/GetStatus
```
```text Get Payment Status Link Endpoint for PROD
POST: https://pinepg.in/api/PaymentURL/GetStatus
```

Below is a sample request and response for the Get Status Link API.

```json Sample Request
{
curl --location --request POST 'https://uat.pinepg.in/api/PaymentURL/GetStatus' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'MERCHANT_ID=107598' \
--data-urlencode 'MERCHANT_ACCESS_CODE=8ba31498-3eb1-4ac9-8eaf-4fc4620b528f' \
--data-urlencode 'REFERENCE_NO=0123'
}
```
```json Sample Response
{
   "RESPONSE_CODE": 1,
    "RESPONSE_MESSAGE": "SUCCESS",
    "PAYMENT_MODE": 3,
    "PINE_PG_TRANSACTION_ID": 14619963,
    "ACQUIRER_NAME": "BILLDESK",
    "REFERENCE_NO": "0123",
    "AMOUNT": 50000,
    "TXN_STATUS": "7",
    "REFUND_AMOUNT": "0",
    "PARENT_TXN_STATUS": "4",
    "ACQUIRER_RESPONSE_CODE": "0300",
    "ACQUIRER_RESPONSE_MESSAGE": "DEFAULT"
}
```

#### JSON Parameters

<details>

<summary>Click Here</summary>

The table below lists the various JSON parameters.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "`MERCHANT_ID`",
    "0-1": "`Int`",
    "0-2": "`M`",
    "0-3": "Unique identifier of the merchant in Plural database.  \n Example: `106598`",
    "1-0": "`MERCHANT_ACCESS_CODE`",
    "1-1": "`String`",
    "1-2": "`M`",
    "1-3": "Unique access code of the merchant in Plural database.  \n  \nExample: `1a39a6d4-46b7-124d-929d-21bf0e9ed123`  \n  \n**Note**: The access key shared while onboarding if not received contact our Integration team.",
    "2-0": "`REFERENCE_NO`",
    "2-1": "`String`",
    "2-2": "`M`",
    "2-3": "Transaction reference number used in link creation"
  },
  "cols": 4,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


</details>

### Response Codes

| Response Code | Response Message                                                     |
| :------------ | :------------------------------------------------------------------- |
| 1             | SUCCESS                                                              |
| \-1           | FAILURE                                                              |
| \-2           | INVALID AMOUNT                                                       |
| \-3           | INVALID MERCHANT_ID                                                  |
| \-4           | INVALID PRODUCT DESCRIPTION                                          |
| \-5           | INVALID CUSTOMER EMAIL ID                                            |
| \-6           | INVALID CUSTOMER MOBILE NO                                           |
| \-7           | INVALID PRODUCT_CODE                                                 |
| \-8           | INVALID MERCHANT_ACCESS_CODE                                         |
| \-9           | INVALID MERCHANT ID ACCESS CODE                                      |
| \-10          | BRAND_EMI_NOT_ENABLED_AND_PRODUCT_CODE_PRESENT_IN_REQUEST            |
| \-11          | EITHER PRODUCT_CODE NOT PRESENT OR MAPPING NOT PRESENT WITH MERCHANT |

<br />

### Real-Time Transaction Response to Merchant

For those needing real-time payment responses, the payment gateway can send transaction response parameters via redirect post to your hosted web page. You can update orders based on the payment response.

### Callback Response

For successful transactions, the payment gateway will send the following response parameters to your callback URL:  
•	RESPONSE_CODE  
•	RESPONSE_MESSAGE  
•	AUTH_CODE  
•	RRN  
•	PINE_PG_TRANSACTION_ID  
•	ACQUIRER_NAME  
•	REFERENCE_NO  
•	AMOUNT  
•	MERCHANT_ID  
•	PAYMENT_MODE

To know the status of the payment you can use the below option.

1. **<a href="https://developer.pluralonline.com/v2.0/docs/developer-tools-webhook" target="_blank">Webhook Notification</a>**: We send Webhook notifications on the successful payment or any changes to the payment's response object.
