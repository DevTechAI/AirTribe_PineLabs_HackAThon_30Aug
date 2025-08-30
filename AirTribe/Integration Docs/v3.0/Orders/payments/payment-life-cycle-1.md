---
title: "Life Cycle"
slug: "payment-life-cycle-1"
excerpt: "Learn about the different statuses acquired during the checkout flow for our Payments and Refunds."
hidden: true
createdAt: "Tue Aug 13 2024 10:32:29 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 13 2024 06:57:16 GMT+0000 (Coordinated Universal Time)"
---
# Payment Life Cycle

Learn about the different statuses acquired during the checkout flow for our Payments.

The figure below shows the life cycle of an Payments.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c53133e-Group_72.png",
        "",
        "Figure: Payment Life Cycle"
      ],
      "align": "center",
      "caption": "Figure: Payment Life Cycle"
    }
  ]
}
[/block]


The table below list the various statuses that our Payments can have during its life cycle.

[block:parameters]
{
  "data": {
    "h-0": "Status",
    "h-1": "Description",
    "0-0": "`PENDING`",
    "0-1": "When the create payment request is successfully received by Plural.",
    "1-0": "`AUTHORIZED`",
    "1-1": "**Only when `pre_auth` is `true`**. When the payment is received successfully. The money is credited from the payer account and waiting for the partner authorization to credit to the partner bank account.",
    "2-0": "`PROCESSED`",
    "2-1": "When the payment is received successfully. The money is debited from the payer account and credited to the partner bank account successfully.",
    "3-0": "`CANCELLED`",
    "3-1": "When the payment get cancelled.  \n  \n**Note**: <ul><li>When `pre_auth` is set to `true`.The partner can cancel the payment if there is a failure in delivering the product or service. </li><li>Similarly, the customer also has the option to cancel the payment during the checkout process.",
    "4-0": "`FAILED`",
    "4-1": "When the payment fails, this can be for many reasons such as maximum retries for OTP verification, partner downtime etc."
  },
  "cols": 2,
  "rows": 5,
  "align": [
    "left",
    "left"
  ]
}
[/block]


# Refund Life Cycle

Learn about the different statuses acquired during the checkout flow for our Refunds.

The figure below shows the life cycle of an Refund.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/18b57ac-Group_75.png",
        "",
        "Figure: Refund Life Cycle"
      ],
      "align": "center",
      "caption": "Figure: Refund Life Cycle"
    }
  ]
}
[/block]


The table below list the various statuses that our Refunds can have during its life cycle.

[block:parameters]
{
  "data": {
    "h-0": "Status",
    "h-1": "Description",
    "0-0": "`CREATED`",
    "0-1": "When the create refund request is successfully received by Plural.",
    "1-0": "`PENDING`",
    "1-1": "When we have processed the refund and waiting for the response from the acquirer.  \n  \n**Note**: You can rely on Webhook events for updates or use our get order API to know the updated status.",
    "2-0": "`PROCESSED`",
    "2-1": "When the refund is successful. The money is debited from the partner account and credited to the customer's bank account.",
    "3-0": "`FAILED`",
    "3-1": "When the refund fails."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]
