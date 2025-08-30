---
title: "Life Cycle"
slug: "pay-by-link-life-cycle"
excerpt: "Learn about the different statuses of Pay by Link."
hidden: false
createdAt: "Tue Mar 18 2025 09:05:39 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri May 02 2025 11:12:56 GMT+0000 (Coordinated Universal Time)"
---
The figure below shows the life cycle of a Payment Link.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/52e867e7cc11f0a1c24acc5e6b5e439f9fdd2fb5505b0a85bad291b744b51013-28-04-2025_pay_by_link.jpg",
        null,
        "Figure: Pay by Link Life Cycle"
      ],
      "align": "center",
      "sizing": "700px",
      "border": true,
      "caption": "Figure: Pay by Link Life Cycle"
    }
  ]
}
[/block]


The table below list the various statuses that a Payment Link can have during its life cycle.

| Status              | Description                                                                                                                                                 |
| :------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CREATED`           | When the create payment link request is successfully received by Plural. The payment link has been created and shared with the customer.                    |
| `CLICKED`           | The customer has clicked on the link but hasn't initiated the payment yet.                                                                                  |
| `PAYMENT_INITIATED` | When the Create Order request is successfully received by Plural. The payment is initiated against an order.                                                |
| `PROCESSED`         | The full payment has been successfully completed by the customer.                                                                                           |
| `CANCELLED`         | When the cancel payment link request is successfully received by Plural. Indicates that you have cancelled the Payment Link.                                |
| `EXPIRED`           | When the current timestamp meets or exceeds the specified expiration timestamp for the payment link. The link has expired, and no payments can be accepted. |
