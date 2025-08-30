---
title: "Life Cycle"
slug: "orders-life-cycle"
excerpt: "Learn about the different statuses acquired during the checkout flow for our Orders."
hidden: true
createdAt: "Tue Aug 13 2024 10:10:58 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 20 2024 10:23:07 GMT+0000 (Coordinated Universal Time)"
---
## Pre-authorization is True

> 📘 Note:
> 
> - The `ATTEMPTED` status is currently unavailable. Orders will proceed directly from `CREATED` to `PENDING`, skipping the `ATTEMPTED` status.
> - The transitions from `CREATED to CANCELLED` and `PENDING to CANCELLED` are also not available at this time.
> - The diagram illustrates the status flow planned for implementation in future updates.

The figure below shows the life cycle of an Order when the Pre-authorization is set to true.

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
    "3-1": "When the payment is received successfully. The money is blocked by the issuer at payer account and waiting for the partner authorization to credit to the partner bank account or customer account.  \n  \n**Note**: When pre-authorization is enabled, you have the option to either capture or cancel a payment settlement to your account.<ol><li>**Capture Order**: Integrate with our Capture Order API to complete the payment for an order. For instance, you can secure the payment once the product or service has been successfully provided to the purchaser. Subsequently, the funds are transferred to the partner’s bank account.</li><li>**Cancel Order**: Utilize the Cancel Order API to revoke the payment for an order. For example, if the product or service fails to reach the buyer, you can annul the payment. The refunded amount will then be credited back to the customer’s account.</ol></li>",
    "4-0": "`PROCESSED`",
    "4-1": "When the payment is received successfully. The money is debited from the payer account and credited to the partner bank account successfully.",
    "5-0": "`CANCELLED`",
    "5-1": "When the payment is cancelled.  \n  \n**Note**: <ul><li>The partner can void the payment if there is a failure in delivering the product or service. </li><li>Similarly, the customer also has the option to cancel the payment during the checkout process.",
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


## Pre-authorization is False

> 📘 Note:
> 
> - The `ATTEMPTED` status is currently unavailable. Orders will proceed directly from `CREATED` to `PENDING`, skipping the `ATTEMPTED` status.
> - The transitions from `CREATED to CANCELLED` and `PENDING to CANCELLED` are also not available at this time.
> - The diagram illustrates the status flow planned for implementation in future updates.

The figure below shows the life cycle of an Order when the Pre-authorization is set to false.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/93e8c81-Group_79.png",
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
    "3-0": "`PROCESSED`",
    "3-1": "When the payment is received successfully. The money is debited from the payer account and credited to the partner bank account successfully.",
    "4-0": "`CANCELLED`",
    "4-1": "When the payment is cancelled.",
    "5-0": "`FAILED`",
    "5-1": "Payment acceptance failed for reasons such as maximum retries for OTP verification etc.",
    "6-0": "`FULLY_REFUNDED`",
    "6-1": "When the payment is completely refunded. The money is debited from the partner bank account and credited to the customer's bank account.",
    "7-0": "`PARTIALLY_REFUNDED`",
    "7-1": "When the partial refund is successful. The money is debited from the partner bank account and credited to the customer's bank account."
  },
  "cols": 2,
  "rows": 8,
  "align": [
    "left",
    "left"
  ]
}
[/block]
