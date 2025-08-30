---
title: "Object"
slug: "object"
excerpt: "Overview of the Pay by Link APIs response."
hidden: false
createdAt: "Wed Nov 13 2024 07:57:24 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Dec 10 2024 07:39:41 GMT+0000 (Coordinated Universal Time)"
---
## Create Payment Link API

Shown below is a sample response returned in our Create Payment Link API.

```json Create Payment Link Sample Response
{
  "RESPONSE_CODE": 1,
  "RESPONSE_MESSAGE": "SUCCESS",
  "PAYMENT_URL": "https://pyn.onl/PLUTUS/m81hnc1",
  "PAYMENT_LINK_ID": 5275034
}
```

The table below lists the various parameters returned in the Create Payment Link API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "RESPONSE_CODE",
    "0-1": "`integer`",
    "0-2": "The Response Code of the API request.  \n  \nPossible value:<ul><li>`1`: SUCCESS. </li><li>`-1`: FAILURE. </li><li>`-2`: INVALID AMOUNT.</li><li>`-3`: INVALID MERCHANT_ID.</li><li>`-4`: INVALID PRODUCT DESCRIPTION.</li><li>`-5`: INVALID CUSTOMER EMAIL ID.</li><li>`-6`: INVALID CUSTOMER MOBILE NO.</li><li>`-7`: INVALID PRODUCT_CODE.</li><li>`-8`: INVALID MERCHANT_ACCESS_CODE.</li><li>`-9`: INVALID MERCHANT ID ACCESS CODE.</li><li>`-10`: BRAND_EMI_NOT_ENABLED_AND_PRODUCT_CODE_PRESENT_IN_REQUEST.</li><li>`-11`: EITHER PRODUCT_CODE NOT PRESENT OR MAPPING NOT PRESENT WITH MERCHANT.</ul></li>",
    "1-0": "RESPONSE_MESSAGE",
    "1-1": "`string`",
    "1-2": "Message corresponding to the response code.  \n  \nExample: `SUCCESS`",
    "2-0": "PAYMENT_URL",
    "2-1": "`string`",
    "2-2": "Plural Payment URL. Navigate your customers to this URL to do the payment.  \n  \nExample: `https://pyn.onl/PLUTUS/m81hnc1`",
    "3-0": "PAYMENT_LINK_ID",
    "3-1": "`Int64`",
    "3-2": "Payment ID which comes in response parameter of create payment link API"
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


## Resend Payment Link API

Shown below is a sample response returned in our Resend Payment Link API.

```json Resend Payment Link Sample Response
{
  "RESPONSE_CODE": 1,
  "RESPONSE_MESSAGE": "SUCCESS"
}
```

The table below lists the various parameters returned in the Resend Payment Link API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "RESPONSE_CODE",
    "0-1": "`integer`",
    "0-2": "The Response Code of the API request.  \n  \nPossible value:<ul><li>`1`: SUCCESS. </li><li>`-1`: FAILURE. </li><li>`-2`: INVALID AMOUNT.</li><li>`-3`: INVALID MERCHANT_ID.</li><li>`-4`: INVALID PRODUCT DESCRIPTION.</li><li>`-5`: INVALID CUSTOMER EMAIL ID.</li><li>`-6`: INVALID CUSTOMER MOBILE NO.</li><li>`-7`: INVALID PRODUCT_CODE.</li><li>`-8`: INVALID MERCHANT_ACCESS_CODE.</li><li>`-9`: INVALID MERCHANT ID ACCESS CODE.</li><li>`-10`: BRAND_EMI_NOT_ENABLED_AND_PRODUCT_CODE_PRESENT_IN_REQUEST.</li><li>`-11`: EITHER PRODUCT_CODE NOT PRESENT OR MAPPING NOT PRESENT WITH MERCHANT.</ul></li>",
    "1-0": "RESPONSE_MESSAGE",
    "1-1": "`string`",
    "1-2": "Message corresponding to the response code.  \n  \nExample: `SUCCESS`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Get Payment Status API

Shown below is a sample response returned in our Get Payment Status API.

```json Get Payment Status Sample Response
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

The table below lists the various parameters returned in the Get Payment Status API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "RESPONSE_CODE",
    "0-1": "`integer`",
    "0-2": "The Response Code of the API request.  \n  \nPossible value:<ul><li>`1`: SUCCESS. </li><li>`-1`: FAILURE. </li><li>`-2`: INVALID AMOUNT.</li><li>`-3`: INVALID MERCHANT_ID.</li><li>`-4`: INVALID PRODUCT DESCRIPTION.</li><li>`-5`: INVALID CUSTOMER EMAIL ID.</li><li>`-6`: INVALID CUSTOMER MOBILE NO.</li><li>`-7`: INVALID PRODUCT_CODE.</li><li>`-8`: INVALID MERCHANT_ACCESS_CODE.</li><li>`-9`: INVALID MERCHANT ID ACCESS CODE.</li><li>`-10`: BRAND_EMI_NOT_ENABLED_AND_PRODUCT_CODE_PRESENT_IN_REQUEST.</li><li>`-11`: EITHER PRODUCT_CODE NOT PRESENT OR MAPPING NOT PRESENT WITH MERCHANT.</ul></li>",
    "1-0": "RESPONSE_MESSAGE",
    "1-1": "`string`",
    "1-2": "Message corresponding to the response code.  \n  \nExample: `SUCCESS`",
    "2-0": "PAYMENT_MODE",
    "2-1": "`string`",
    "2-2": "The payment mode you prefer to accept payment.  \n  \nAccepted values: <ul><li>`1`: CREDIT/DEBIT CARD</li><li>`3`: NET BANKING</li><li>`4`:CREDIT EMI</li><li>`10`: UPI</li><li>`11`: WALLET</li><li>`14`: DEBIT EMI</li><li>`16`: PREBOOKING</li><li>`17`: BNPL/FLEXIPAY</li><li>`19`: Cardless EMI</li><li>`20`: PBP (Paybypoints)</ul></li>",
    "3-0": "PINE_PG_TRANSACTION_ID",
    "3-1": "`string`",
    "3-2": "Unique transaction ID generated by Plural against an Order ID.  \nExample: `12345678`",
    "4-0": "ACQUIRER_NAME",
    "4-1": "`string`",
    "4-2": "The acquirer's name for this transaction.  \n  \nExample: `BILLDESK`",
    "5-0": "REFERENCE_NO",
    "5-1": "`string`",
    "5-2": "Reference number of merchant which is maintained by pine labs.  \n(Max length is 100)  \nExample: `ABCDEFG`",
    "6-0": "AMOUNT",
    "6-1": "`Int64`",
    "6-2": "Amount in Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh)</ul></li>Example: `1100`",
    "7-0": "TXN_STATUS",
    "7-1": "`string`",
    "7-2": "The status of the transaction.  \n**Note**: Please refer to the Pine PG transaction status table to know the status.",
    "8-0": "REFUND_AMOUNT",
    "8-1": "`Int64`",
    "8-2": "The total amount refunded.  \n  \nExample: `0`",
    "9-0": "PARENT_TXN_STATUS",
    "9-1": "`integer`",
    "9-2": "The status code of the purchase transaction.  \n  \nExample: `4`",
    "10-0": "ACQUIRER_RESPONSE_CODE",
    "10-1": "`string`",
    "10-2": "The response code received from the acquirer.  \n  \nExample: `1234`",
    "11-0": "ACQUIRER_RESPONSE_MESSAGE",
    "11-1": "`string`",
    "11-2": "Message corresponding to the acquirer code.  \n  \nExample: `DEFAULT`"
  },
  "cols": 3,
  "rows": 12,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]
