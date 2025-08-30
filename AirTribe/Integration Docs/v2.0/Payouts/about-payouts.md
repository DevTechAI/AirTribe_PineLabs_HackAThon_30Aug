---
title: "About Payouts"
slug: "about-payouts"
excerpt: "Learn how to create payouts using the dashboard and Plural APIs."
hidden: false
createdAt: "Fri Oct 04 2024 05:33:04 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Oct 14 2024 10:58:46 GMT+0000 (Coordinated Universal Time)"
---
Payouts are transactions made to beneficiaries. For every payout, you must specify the amount and the beneficiary to whom you must send the money. You become eligible to make payouts after you sign up and complete the account activation and KYC verification.

> 📘 Note:
> 
> - Currently, we support payouts from the YES Bank accounts only. 
> - You can add up to 3 current accounts to our system.

A payout transaction is made to a beneficiary account associated with a beneficiary.

## Get Started with Plural Payouts

- You can use our payout feature over a connected banking model.
- It allows you to make payouts directly from your payout bank account. Currently, we only support payouts from YES bank accounts. This means you will need a YES bank current account to initiate payouts using Plural.
- If you already have a YES Bank account, our team will assist you with completing the KYC verification process and activating your payout account.
- For UPI payouts, you will need to obtain the UPI details and MID from the bank. 
- Once you have these, our team will assist in adding UPI as a payout option for your account. 

> 📘 Note:
> 
> - No extra documents are required, as this process is included in the same KYC verification. Inform our onboarding team and the bank that you want UPI enabled as a payout mode.

## Payout Modes

You can make payouts using different payment modes that can be used to transfer to individuals or entities.

The table below indicates the payout modes, transaction limits, and operating hours for each payout mode.

[block:parameters]
{
  "data": {
    "h-0": "Payment Mode",
    "h-1": "Transfer Limit",
    "h-2": "Settlement Time",
    "0-0": "NEFT",
    "0-1": "Upper Limit: `10,00,00,000`  \nLower Limit: `1`",
    "0-2": "`2` hours",
    "1-0": "RTGS",
    "1-1": "Upper Limit: `10,00,00,000`  \nLower Limit: `2,00,000`",
    "1-2": "`1` min",
    "2-0": "IMPS",
    "2-1": "Upper Limit: `5,00,000`  \nLower Limit: `1`",
    "2-2": "`1` min",
    "3-0": "UPI",
    "3-1": "Upper Limit: `1,00,000`  \nLower Limit: `1`",
    "3-2": "Instant"
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


## Beneficiary

You can create a beneficiary by passing the beneficiary details, such as beneficiary name, account number, IFSC, VPA handle and the amount to be paid.

## How to Initiate Payouts

You can make a payout in 3 simple steps from the dashboard. Follow the below steps to complete a payout.

1. Add beneficiary details such as, beneficiary name, bank account number, IFSC, and VPA handle.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6099b434a66b3dc9fa1426409fef07e74e84b92aa1c738c8842903e2896e33f2-Initiate_Individual_Payout.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


2. Choose transfer type and enter the amount.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e7c4770a766942df7d8fc6b185bdc361b501139ee15174696aed903caabd7076-Step_2_Initiate_Individual_Payout.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


3. Review the beneficiary details, payout details, and confirm the payout.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/efe9b4333d9ebbc7d38e6acae63be4a9d264e74ab3cf1cad405dbf25e74eaf49-Step_3_Review.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


## Plural Payout Types

Plural payout support, Individual Transfers, and Bulk Transfers are two distinct methods of distributing funds, each suited to different use cases depending on the number of the transactions.

1. **Individual Transfer**  
   In individual transfers, funds are sent to a single beneficiary at a time. Here are some options available for a Individual payout.
   1. **Schedule Payout**: You can schedule a time to process a payout request.
   2. **Update Schedule Payout**: You can update the schedule time of the payout request.
   3. **Cancel Schedule Payout**: You can also cancel a scheduled payout request.
2. **Bulk Transfer**  
   Bulk transfer involves sending payouts to multiple beneficiaries in a queue. The sender uploads an Excel file containing beneficiary details, and the system processes all the payments simultaneously.
