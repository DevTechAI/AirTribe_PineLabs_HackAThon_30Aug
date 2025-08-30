---
title: "Object"
slug: "object-1"
excerpt: "Overview of the settlements response object."
hidden: false
createdAt: "Fri Oct 18 2024 04:49:50 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Oct 24 2024 12:19:07 GMT+0000 (Coordinated Universal Time)"
---
## List all Settlements

Shown below is a sample response returned through our List all Settlements API.

```json Settlements Object
{
  "data": [
    {
      "total_amount": 0.96,
      "actual_transaction_amount": 2,
      "total_deduction_amount": 0.08,
      "total_transactions_count": 2,
      "last_processed_date": "2024-10-09T07:00:00",
      "settled_date": "2024-10-09T10:59:46",
      "utr_number": "410092786849",
      "programs": [
        "UPI"
      ],
      "system": "PG",
      "bank_name": "HDFC Bank Ltd",
      "bank_acc_number": "04992990009595"
    },
    {
      "total_amount": 0.98,
      "actual_transaction_amount": 1,
      "total_deduction_amount": 0.04,
      "total_transactions_count": 1,
      "last_processed_date": "2024-10-08T07:00:00",
      "settled_date": "2024-10-08T11:16:40",
      "utr_number": "410080488411",
      "programs": [
        "UPI"
      ],
      "system": "PG",
      "bank_name": "HDFC Bank Ltd",
      "bank_acc_number": "04992990009595"
    },
    {
      "total_amount": 0.96,
      "actual_transaction_amount": 2,
      "total_deduction_amount": 0.08,
      "total_transactions_count": 2,
      "last_processed_date": "2024-10-07T07:00:00",
      "settled_date": "2024-10-07T11:36:44",
      "utr_number": "410077587729",
      "programs": [
        "UPI"
      ],
      "system": "PG",
      "bank_name": "HDFC Bank Ltd",
      "bank_acc_number": "04992990009595"
    },
    {
      "total_amount": 3.92,
      "actual_transaction_amount": 4,
      "total_deduction_amount": 0.16,
      "total_transactions_count": 4,
      "last_processed_date": "2024-10-06T07:00:00",
      "settled_date": "2024-10-07T10:48:02",
      "utr_number": "410077424703",
      "programs": [
        "UPI"
      ],
      "system": "PG",
      "bank_name": "HDFC Bank Ltd",
      "bank_acc_number": "04992990009595"
    },
    {
      "total_amount": 0.98,
      "actual_transaction_amount": 1,
      "total_deduction_amount": 0.04,
      "total_transactions_count": 1,
      "last_processed_date": "2024-10-05T07:00:00",
      "settled_date": "2024-10-05T10:58:12",
      "utr_number": "410055402704",
      "programs": [
        "UPI"
      ],
      "system": "PG",
      "bank_name": "HDFC Bank Ltd",
      "bank_acc_number": "04992990009595"
    },
    {
      "total_amount": 1.94,
      "actual_transaction_amount": 3,
      "total_deduction_amount": 0.12,
      "total_transactions_count": 3,
      "last_processed_date": "2024-10-04T06:32:13",
      "settled_date": "2024-10-04T11:14:39",
      "utr_number": "410041942381",
      "programs": [
        "UPI"
      ],
      "system": "PG",
      "bank_name": "HDFC Bank Ltd",
      "bank_acc_number": "04992990009595"
    },
    {
      "total_amount": 0.98,
      "actual_transaction_amount": 1,
      "total_deduction_amount": 0.04,
      "total_transactions_count": 1,
      "last_processed_date": "2024-10-03T06:35:20",
      "settled_date": "2024-10-03T10:58:43",
      "utr_number": "410039900271",
      "programs": [
        "UPI"
      ],
      "system": "PG",
      "bank_name": "HDFC Bank Ltd",
      "bank_acc_number": "04992990009595"
    }
  ],
  "total_settlement_count": 7,
  "total_transactions_count": 14,
  "total_settlement_amount": 10.72
}
```

The table below lists the various parameters returned in the Settlements response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "data",
    "0-1": "`array of objects`",
    "0-2": "An array of objects that contains the settlement objects.",
    "1-0": "total_settlement_count",
    "1-1": "`integer`",
    "1-2": "The total number of settlement.  \n  \nExample: `7`",
    "2-0": "total_transactions_count",
    "2-1": "`integer`",
    "2-2": "The total number of transactions.  \n  \nExample: `14`",
    "3-0": "total_settlement_amount",
    "3-1": "`integer`",
    "3-2": "The total settlement amount.  \n  \nExample: `15`"
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


### Data [Child Object]

The table below lists the various parameters in the `data` child object. This is part of the `settlement` response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "total_amount",
    "0-1": "`integer`",
    "0-2": "Total settlement amount.  \n  \nExample: `0.98`",
    "1-0": "actual_transaction_amount",
    "1-1": "`integer`",
    "1-2": "The total transaction amount without deductions.  \n  \nExample: `1`",
    "2-0": "total_deduction_amount",
    "2-1": "`integer`",
    "2-2": "Total deduction amount for a transaction.  \n  \nExample: `0.04`",
    "3-0": "total_transactions_count",
    "3-1": "`integer`",
    "3-2": "The total number of transactions settled within a specific UTR [Unique Transaction Reference].  \n  \nExample: `1`",
    "4-0": "last_processed_date",
    "4-1": "`string`",
    "4-2": "The date when the transaction was last processed and selected for settlement.  \n  \nExample: `2024-10-05T07:00:00`",
    "5-0": "settled_date",
    "5-1": "`string`",
    "5-2": "The date on which a batch of transactions was settled..  \n  \nExample: `2024-10-03T10:58:43`",
    "6-0": "utr_number",
    "6-1": "`string`",
    "6-2": "Unique transaction reference [UTR] generated for the settlement.  \n  \nExample: `410039900271`",
    "7-0": "programs",
    "7-1": "`array of objects`",
    "7-2": "An array of objects that contains all the program details.",
    "8-0": "system",
    "8-1": "`string`",
    "8-2": "A constant string value.  \n  \nHas to be 2 digits.  \n  \nExample: `PG`",
    "9-0": "bank_name",
    "9-1": "`string`",
    "9-2": "Settlement bank name.<ul><li>Minimum length: 1 characters</li><li>Maximum length: 50 characters.</ul></li>Example: `HDFC Bank Ltd`",
    "10-0": "bank_acc_number",
    "10-1": "`string`",
    "10-2": "Settlement bank account number.<ul><li>Minimum length: 1 characters</li><li>Maximum length: 50 characters.</ul></li>Example: `04992990009595`"
  },
  "cols": 3,
  "rows": 11,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## List Settlements by UTR

Shown below is a sample response returned through our list settlements by UTR API.

```
{
    "utr_number": "410092786849",
    "bank_name": "HDFC Bank Ltd",
    "bank_acc_number": "04992990009595",
    "programs": [
        "UPI"
    ],
    "total_transaction_count": 2,
    "total_transaction_amount": 2,
    "actual_transaction_amount": 2,
    "total_refund": 0,
    "total_chargeback_recovery_amount": 0,
    "total_loan_recovery_amount": 0,
    "total_mdr_amount": 0.04,
    "total_gst_amount": 0,
    "total_late_settlement_fee": 0,
    "total_settled_amount": 0.96,
    "total_mar_amount": 0,
    "split_fund_amount": 0,
    "total_platform_fee": 0,
    "other_deductions": 0,
    "additional_mdr_amount": 0,
    "total_convenience_fee": 0,
    "total_gst_on_c_c_f": 0,
    "total_cashback_amount": 0,
    "total_merchant_cashback": 0,
    "total_merchant_convenience_fee": 0,
    "transactions": [
        {
            "transaction_id": "v1-241008182747-aa-8JwMy9-up-k",
            "system": "PG",
            "processed_date": "2024-10-09T07:00:00",
            "transaction_date": "2024-10-08T00:00:00",
            "transaction_amount": 1,
            "actual_transaction_amount": 1,
            "total_deduction_amount": 0.02,
            "settled_amount": 0,
            "store_address": "sec 62 noida",
            "acquirer_name": "UPI_HDFC",
            "tid": "HDFC000028502654",
            "is_emi": false,
            "utr_number": "410092786849",
            "program": "UPI",
            "payout_status": "Success"
        },
        {
            "transaction_id": "v1-241008182412-aa-rnfH9Q-up-F",
            "system": "PG",
            "processed_date": "2024-10-09T07:00:00",
            "transaction_date": "2024-10-08T00:00:00",
            "transaction_amount": 1,
            "actual_transaction_amount": 1,
            "total_deduction_amount": 0.02,
            "settled_amount": 0.96,
            "store_address": "sec 62 noida",
            "acquirer_name": "UPI_HDFC",
            "tid": "HDFC000028502654",
            "is_emi": false,
            "utr_number": "410092786849",
            "program": "UPI",
            "payout_status": "Success"
        }
    ],
    "pagination": {
        "total_pages": 2,
        "current_page": "1"
    }
}
```

The table below lists the various parameters returned in the Settlements response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "utr_number",
    "0-1": "`string`",
    "0-2": "Unique Transaction Reference [UTR] provided by the Bank.<ul><li>Minimum length: `16` characters.</li><li>Maximum length: `50` characters.</ul></li>Example: `410092786849`",
    "1-0": "bank_name",
    "1-1": "`string`",
    "1-2": "Settlement bank name.  \n  \nExample: `HDFC Bank Ltd`",
    "2-0": "bank_acc_number",
    "2-1": "`string`",
    "2-2": "Settlement bank account number.  \n  \nExample: `04992990009595`",
    "3-0": "programs",
    "3-1": "`array of object`",
    "3-2": "An array of objects that contains all the program details.",
    "4-0": "total_transaction_count",
    "4-1": "`integer`",
    "4-2": "The total number of transactions settled within a specific UTR [Unique Transaction Reference].  \n  \nExample: `1`",
    "5-0": "total_transaction_amount",
    "5-1": "`integer`",
    "5-2": "The total transaction amount settled after deductions within a specific UTR [Unique Transaction Reference].  \n  \nExample: `2`",
    "6-0": "actual_transaction_amount",
    "6-1": "`integer`",
    "6-2": "The total transaction amount without deductions.  \n  \nExample: `1`",
    "7-0": "total_refund",
    "7-1": "`integer`",
    "7-2": "Total refund amount deducted within a UTR.  \n  \nExample: `0`",
    "8-0": "total_chargeback_recovery_amount",
    "8-1": "`integer`",
    "8-2": "The total chargeback recovery amount in given UTR.  \n  \nExample: `0`",
    "9-0": "total_loan_recovery_amount",
    "9-1": "`integer`",
    "9-2": "The total amount recovered from loan in given UTR.  \n  \nExample: `0`",
    "10-0": "total_mdr_amount",
    "10-1": "`integer`",
    "10-2": "The total MDR [Merchant Discount Rate] amount deducted in given UTR.  \n  \nExample: `0.04`",
    "11-0": "total_gst_amount",
    "11-1": "`integer`",
    "11-2": "The total GST amount charged within a given UTR.  \n  \nExample: `0` ",
    "12-0": "total_late_settlement_fee",
    "12-1": "`integer`",
    "12-2": "The total fee charged for late settlement in the given UTR.  \n  \nExample: `0`",
    "13-0": "total_settled_amount",
    "13-1": "`integer`",
    "13-2": "The total amount settled within a given UTR.  \n  \nExample: `0.96`",
    "14-0": "total_mar_amount",
    "14-1": "`integer`",
    "14-2": "The total Merchant Acquisition Rate [MAR] charged.  \n  \nExample: `0`",
    "15-0": "split_fund_amount",
    "15-1": "`integer`",
    "15-2": "The split amount of the transaction.  \n  \nExample: `0`",
    "16-0": "total_platform_fee",
    "16-1": "`integer`",
    "16-2": "The total fee charged by the platform.  \n  \nExample: `0`",
    "17-0": "other_deductions",
    "17-1": "`integer`",
    "17-2": "Other deductions of the transaction.  \n  \nExample: `0`",
    "18-0": "additional_mdr_amount",
    "18-1": "`integer`",
    "18-2": "Additional MDR [Merchant Discount Rate] deducted.  \n  \nExample: `0`",
    "19-0": "total_convenience_fee",
    "19-1": "`integer`",
    "19-2": "The total convenience fee charged.  \n  \nExample: `0`",
    "20-0": "total_gst_on_c_c_f",
    "20-1": "`integer`",
    "20-2": "GST charged on convenience fees.  \n  \nExample: `0`",
    "21-0": "total_cashback_amount",
    "21-1": "`integer`",
    "21-2": "The total cashback amount provided.  \n  \nExample: `0`",
    "22-0": "total_merchant_cashback",
    "22-1": "`integer`",
    "22-2": "The total cashback amount provided.  \n  \nExample: `0`",
    "23-0": "total_merchant_convenience_fee",
    "23-1": "`integer`",
    "23-2": "The total convenience fee charged.  \n  \nExample: `0`",
    "24-0": "transactions",
    "24-1": "`array of objects`",
    "24-2": "An array of objects that contains the transaction details.",
    "25-0": "pagination",
    "25-1": "`object`",
    "25-2": "An object that contains the pagination details."
  },
  "cols": 3,
  "rows": 26,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Transactions [Child Object]

The table below lists the various parameters in the `transactions` child object. This is part of the `settlements by UTR` response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "transaction_id",
    "0-1": "`string`",
    "0-2": "Unique identifier for a transaction in Plural database.  \n  \nExample: `v1-241008182747-aa-8JwMy9-up-k`",
    "1-0": "system",
    "1-1": "`string`",
    "1-2": "A constant string value.  \n  \nHas to be 2 digits.  \n  \nExample: `PG`",
    "2-0": "processed_date",
    "2-1": "`string`",
    "2-2": "The date when the transaction was processed.  \n  \nExample: `2024-10-09T07:00:00`",
    "3-0": "transaction_date",
    "3-1": "`string`",
    "3-2": "The date of the transaction.  \n  \nExample: `2024-10-08T00:00:00`",
    "4-0": "transaction_amount",
    "4-1": "`integer`",
    "4-2": "The transaction amount.  \n  \nExample: `1`",
    "5-0": "actual_transaction_amount",
    "5-1": "`integer`",
    "5-2": "The total transaction amount without deductions.  \n  \nExample: `1`",
    "6-0": "total_deduction_amount",
    "6-1": "`integer`",
    "6-2": "Total deduction amount for a transaction.  \n  \nExample: `0.02`",
    "7-0": "settled_amount",
    "7-1": "`integer`",
    "7-2": "The total settlement amount of the transaction.  \n  \nExample: `0`",
    "8-0": "store_address",
    "8-1": "`string`",
    "8-2": "The address of the store where the transaction was created.  \n  \nExample: `sec 62 noida`  \n  \n**Note**: Applicable only in case of pos transactions.",
    "9-0": "acquirer_name",
    "9-1": "`string`",
    "9-2": "The name of the acquirer.  \n  \nExample: `UPI_HDFC`",
    "10-0": "tid",
    "10-1": "`string`",
    "10-2": "The Terminal ID for the transaction.  \n  \nExample: `HDFC000028502654`",
    "11-0": "is_emi",
    "11-1": "`boolean`",
    "11-2": "This Indicates if the transaction was an EMI [Equated Monthly Installment].  \n  \nExample: `false`",
    "12-0": "utr_number",
    "12-1": "`string`",
    "12-2": "Unique Transaction Reference [UTR] provided by the Bank.<ul><li>Minimum length: `16` characters.</li><li>Maximum length: `50` characters.</ul></li>Example: `410092786849`",
    "13-0": "program",
    "13-1": "`string`",
    "13-2": "The payment method used for the transaction.  \n  \nExample: `UPI`",
    "14-0": "payout_status",
    "14-1": "`string`",
    "14-2": "The status of the payout.  \n  \nExample: `Success`"
  },
  "cols": 3,
  "rows": 15,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Pagination [Child Object]

The table below lists the various parameters in the `pagination` child object. This is part of the `settlements by UTR` response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "total_pages",
    "0-1": "`integer`",
    "0-2": "The total number of pages.  \n  \nExample: `2`",
    "1-0": "current_page",
    "1-1": "`string`",
    "1-2": "Current page.  \n  \nExample: `1`"
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
