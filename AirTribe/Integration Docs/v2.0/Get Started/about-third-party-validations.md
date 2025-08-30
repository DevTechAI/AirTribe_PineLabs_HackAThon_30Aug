---
title: "Third Party Validation"
slug: "about-third-party-validations"
excerpt: "Learn how you can integrate with Plural TPV to validate your customer's Bank Account."
hidden: false
createdAt: "Fri Jul 05 2024 06:37:15 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Sep 30 2024 07:35:55 GMT+0000 (Coordinated Universal Time)"
---
By integrating with Plural’s Third Party Validations (TPV), you can seamlessly comply with SEBI guidelines for online payment collections at the checkout. Investors can conveniently make payments via UPI and Net Banking. According to SEBI guidelines, transactions should exclusively occur from bank accounts registered during customer onboarding.

Third Party Validations (TPV) for bank accounts are crucial for BFSI companies dealing with mutual funds, securities, and brokerage.

## Plural TPV Workflow

The figure below shows the workflow of plural third party validation.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c59815b-Group_18.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


1. **Accept Payment**: Use Plural Accept Payment API to initiate the payment.
2. **Generate Payment Link**: Use Plural Generate Payment Link API to generate a payment link. We return `deep_link` and also a `short_link` in the response.

> 📘 Note:
> 
> Use this URL to redirect to a mobile app. You can do this by rendering the URL returned by Plural as a button or a link for the customer to use.

## Use Case

Suppose an organization wants to ensure that its investors make payments exclusively from their registered bank accounts. Here’s how they can achieve this using Plural APIs:

1. **Create a Payment Link**: The organization generates a payment link using Plural APIs, including relevant details such as the payment amount, customer information, and a unique reference ID.
2. **Customer Interaction**: When investors receive the Payment Link, they click on it. This action redirects them to their UPI app.
3. **Payment Validation**: During payment initiation, the system validates the investor’s bank account details against the received payment account. If the payment originates from a registered account number, it proceeds successfully. Otherwise, the payment fails.
4. **Regulatory Compliance**: This process ensures compliance with regulatory guidelines and prevents unauthorized payments.

By using Plural TPV Payment Links and validating registered account details, the organization ensures that payments come only from authorized sources.
