---
title: "Life Cycle"
slug: "payments-life-cycle"
excerpt: "Overview of the different statuses acquired during the checkout flow for our Orders, Payments, and Refunds."
hidden: true
createdAt: "Fri Jul 26 2024 11:26:15 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Aug 20 2024 05:15:55 GMT+0000 (Coordinated Universal Time)"
---
# Order Life Cycle

Learn about the different statuses acquired during the checkout flow for our Orders.

The figure below shows the life cycle of an Order.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/75fb842-Group_76.png",
        "",
        "Figure: Order Life Cycle"
      ],
      "align": "center",
      "caption": "Figure: Order Life Cycle"
    }
  ]
}
[/block]


The table below list the various statuses that our Orders can have during its life cycle.

[block:parameters]
{
  "data": {
    "h-0": "Status",
    "h-1": "Description",
    "0-0": "`CREATED`",
    "0-1": "When the Create Order request is successfully received by Plural.",
    "1-0": "`ATTEMPTED`",
    "1-1": "When the payment on a pending order fails, order acquire this status.",
    "2-0": "`PENDING`",
    "2-1": "When the order is linked against a payment request.  \n  \n**Note**: To link a payment use the order_id generated in our Create Payment API and create a payment request. This successfully links your payment against the order.",
    "3-0": "`AUTHORIZED`",
    "3-1": "**Only when `pre_auth` is `true`**. When the payment is received successfully. The money is blocked by the issuer at payer account and waiting for the partner authorization to credit to the partner bank account or customer account.  \n  \n**Note**: When pre-authorization is enabled, you have the option to either capture or cancel a payment settlement to your account.<ol><li>**Capture Order**: Integrate with our Capture Order API to complete the payment for an order. For instance, you can secure the payment once the product or service has been successfully provided to the purchaser. Subsequently, the funds are transferred to the partner’s bank account.</li><li>**Cancel Order**: Utilize the Cancel Order API to revoke the payment for an order. For example, if the product or service fails to reach the buyer, you can annul the payment. The refunded amount will then be credited back to the customer’s account.</ol></li>",
    "4-0": "`PROCESSED`",
    "4-1": "When the payment is received successfully. The money is debited from the payer account and credited to the partner bank account successfully.",
    "5-0": "`CANCELLED`",
    "5-1": "When the payment gets cancelled.  \n  \n**Note**: <ul><li>When `pre_auth` is set to `true`.The partner can void the payment if there is a failure in delivering the product or service. </li><li>Similarly, the customer also has the option to cancel the payment during the checkout process.",
    "6-0": "`FAILED`",
    "6-1": "Payment acceptance failed for reasons such as maximum retries for OTP verification etc.",
    "7-0": "`FULLY_REFUNDED`",
    "7-1": "When the payment is completely refunded. The money is debited from the partner bank account and credited to the customer's bank account.",
    "8-0": "`PARTIALLY_REFUNDED`",
    "8-1": "When the partial refund is successful. The money is debited from the partner bank account and credited to the customer's bank account."
  },
  "cols": 2,
  "rows": 9,
  "align": [
    "left",
    "left"
  ]
}
[/block]


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


<br />

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
