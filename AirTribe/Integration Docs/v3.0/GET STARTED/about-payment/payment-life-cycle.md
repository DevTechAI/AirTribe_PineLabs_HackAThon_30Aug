---
title: "Life Cycle"
slug: "payment-life-cycle"
excerpt: "Learn about the different statuses acquired during the checkout flow for our Payments."
hidden: false
createdAt: "Thu Aug 22 2024 10:09:44 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Oct 18 2024 02:59:29 GMT+0000 (Coordinated Universal Time)"
---
The figure below shows the life cycle of an Payments.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bcf3f24bbcf945ebfd2416e3889c7eb04b1fceb4b059fd5df63b2b440d528e54-image.png",
        null,
        "Figure: Payment Life Cycle"
      ],
      "align": "center",
      "border": true,
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
