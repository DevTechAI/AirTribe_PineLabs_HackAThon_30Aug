---
title: "Life Cycle"
slug: "life-cycle-copy"
excerpt: "Learn about the different statuses acquired during the checkout flow for our Orders."
hidden: true
createdAt: "Thu Aug 29 2024 12:53:10 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Aug 29 2024 12:57:13 GMT+0000 (Coordinated Universal Time)"
---
## Pre-authorization is True

The figure below shows the life cycle of an Order when the Pre-authorization is set to true.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4a7f52b1c11edf7f85da2acbb40660a399d6175e8359d0f605e0b9baedd10e69-Group_89.png",
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
    "1-0": "`PENDING`",
    "1-1": "When the order is linked against a payment request.  \n  \n**Note**: To link a payment use the order_id generated in our Create Payment API and create a payment request. This successfully links your payment against the order.",
    "2-0": "`AUTHORIZED`",
    "2-1": "When the payment is received successfully. The money is blocked by the issuer at payer account and waiting for the partner authorization to credit to the partner bank account or customer account.  \n  \n**Note**: When pre-authorization is enabled, you have the option to either capture or cancel a payment settlement to your account.<ol><li>**Capture Order**: Integrate with our Capture Order API to complete the payment for an order. For instance, you can secure the payment once the product or service has been successfully provided to the purchaser. Subsequently, the funds are transferred to the partner’s bank account.</li><li>**Cancel Order**: Utilize the Cancel Order API to revoke the payment for an order. For example, if the product or service fails to reach the buyer, you can annul the payment. The refunded amount will then be credited back to the customer’s account.</ol></li>",
    "3-0": "`PROCESSED`",
    "3-1": "When the payment is received successfully. The money is debited from the payer account and credited to the partner bank account successfully.",
    "4-0": "`CANCELLED`",
    "4-1": "When the payment is cancelled.  \n  \n**Note**: <ul><li>The partner can void the payment if there is a failure in delivering the product or service. </li><li>Similarly, the customer also has the option to cancel the payment during the checkout process.",
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


## Pre-authorization is False

The figure below shows the life cycle of an Order when the Pre-authorization is set to false.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0f8650ede7e568cc5703bcf5a61454d18465e65078481f15721d3225df495f2f-Group_87.png",
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
    "1-0": "`PENDING`",
    "1-1": "When the order is linked against a payment request.  \n  \n**Note**: To link a payment use the order_id generated in our Create Payment API and create a payment request. This successfully links your payment against the order.",
    "2-0": "`PROCESSED`",
    "2-1": "When the payment is received successfully. The money is debited from the payer account and credited to the partner bank account successfully.",
    "3-0": "`CANCELLED`",
    "3-1": "When the payment is cancelled.",
    "4-0": "`FAILED`",
    "4-1": "Payment acceptance failed for reasons such as maximum retries for OTP verification etc.",
    "5-0": "`FULLY_REFUNDED`",
    "5-1": "When the payment is completely refunded. The money is debited from the partner bank account and credited to the customer's bank account.",
    "6-0": "`PARTIALLY_REFUNDED`",
    "6-1": "When the partial refund is successful. The money is debited from the partner bank account and credited to the customer's bank account."
  },
  "cols": 2,
  "rows": 7,
  "align": [
    "left",
    "left"
  ]
}
[/block]
