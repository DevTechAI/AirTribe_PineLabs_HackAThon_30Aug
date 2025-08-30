---
title: "Life Cycle"
slug: "refund-life-cycle"
excerpt: "Learn about the different statuses acquired during the checkout flow for our Refunds."
hidden: false
createdAt: "Fri Sep 27 2024 09:03:49 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Oct 18 2024 03:06:05 GMT+0000 (Coordinated Universal Time)"
---
The figure below shows the life cycle of an Refund.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c3d4fc16dd6dc03560848fbbdaf0f7e4ae72daeda5db615273c6a057fbae2dcc-image.png",
        null,
        "Figure: Refund Life Cycle"
      ],
      "align": "center",
      "border": true,
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
