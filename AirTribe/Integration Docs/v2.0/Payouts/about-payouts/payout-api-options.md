---
title: "Payout APIs"
slug: "payout-api-options"
excerpt: "Learn about the different types of Payout APIs available with Plural payout, each API is tailored to handle a specific kind of payout."
hidden: false
createdAt: "Mon Oct 14 2024 11:07:13 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Oct 15 2024 12:09:24 GMT+0000 (Coordinated Universal Time)"
---
Plural payout support, Individual Transfers, and Bulk Transfers are two distinct methods of distributing funds, each suited to different use cases depending on the number of the transactions.

## 1. **Individual Transfer**

In individual transfers, funds are sent to a single beneficiary or bank account number at a time.

1. **Create a Payout to Bank Account Number**: You can initiate a payout to a bank account number and save the account details as a beneficiary linked to your account for future transactions. You can also perform the below action using the same API.
   1. **Schedule a Payout**: You can schedule a specific time to process a payout request. This allows you to initiate a scheduled payout to a beneficiary or directly to a bank account.
   2. **Create a Payout to Beneficiary**: You can save the Beneficiary details returned in our Create a Payout to Bank Account Number API to initiate a future payout to the Beneficiary details saved.
2. **Update Schedule Payout**: You can update the schedule time of the payout request.
3. **Cancel Schedule Payout**: You can also cancel a scheduled payout request.

The table below lists the various options available in our Payouts API and gives a brief description of each:

[block:parameters]
{
  "data": {
    "h-0": "API Endpoint",
    "h-1": "Description",
    "0-0": "<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/reference/payouts-to-account-number\" target=\"_blank\">Create a Payout to Bank Account Number</a>",
    "0-1": "Use this API to initiate a payout to a bank account number and save the account details as a beneficiary linked to your account for future transactions.",
    "1-0": "<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/reference/update-scheduled-payout\" target=\"_blank\">Update Schedule Payout</a>",
    "1-1": "Use this API to update the schedule time of the scheduled payout.",
    "2-0": "<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/reference/cancel-scheduled-payout\" target=\"_blank\">Cancel Scheduled Payout</a>",
    "2-1": "Use this API to cancel a schedule payout.",
    "3-0": "<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/reference/get-payout-status\" target=\"_blank\">Get Payout Status</a>",
    "3-1": "Use this API to fetch the payout status."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## 2. **Bulk Transfer**

Bulk transfer involves sending payouts to multiple beneficiaries in a queue. The sender uploads an Excel file containing beneficiary details, and the system processes all the payments simultaneously.

[block:parameters]
{
  "data": {
    "h-0": "API Endpoint",
    "h-1": "Description",
    "0-0": "<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/reference/bulk-payouts-upload-file\" target=\"_blank\">Upload File</a>",
    "0-1": "Use this API to initiate Bulk payout.",
    "1-0": "<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/reference/payouts-get-bulk-payouts-status\" target=\"_blank\">Get Bulk Payouts Status</a>",
    "1-1": "Use this API to get the status of the bulk payout"
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]
