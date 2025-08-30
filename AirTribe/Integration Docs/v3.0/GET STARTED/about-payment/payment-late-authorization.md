---
title: "Late Authorization"
slug: "payment-late-authorization"
excerpt: "Learn how you can handle late authorised payments with Plural."
hidden: false
createdAt: "Fri Sep 13 2024 06:55:50 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Oct 18 2024 09:29:34 GMT+0000 (Coordinated Universal Time)"
---
Late authorization is a situation in payment processing where a transaction authorization is delayed. Typically, when your customer makes a payment, our payment system requests authorization from the issuing bank or card network to confirm that the funds or credit are available. In the case of late authorization, this response takes longer than expected, potentially leading to issues such as:

1. **Customer Experience Impact**: The customer may be left uncertain about whether their payment was successful or not, causing frustration.
2. **Risk of Chargebacks**: In some cases, if the customer attempts to initiate the payment again due to the delay, it could lead to double charges or disputes.

With Plural, you can handle such scenarios by enabling late authorization. You can have your respective time enabled as per your requirement, after which they treat the payment as failed if no authorization response is received.

> 📘 Note:
> 
> You can contact our <a href="mailto:pgsupport@pinelabs.com" target="_blank">support team</a> to enable late authorization for your account.

***

## Late Authorization Flow

The flow diagram below illustrates the late authorization process.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/40c9c73c8eb881b16bf30619f2d8a124e7465c5bd561b2264402b84f4257c445-Screenshot_2024-09-17_at_11.15.14_AM.png",
        "",
        "Figure: Late Authorization Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Figure: Late Authorization Flow"
    }
  ]
}
[/block]


For example consider a merchant who has set the late authorization time to 10 seconds. Here's how the payment status typically unfolds:

- **Payment Initiation**: The customer completes the payment and the payment status is in a `pending` state. If the bank's gateway doesn't return a response to Plural within the configured time, the payment status is marked as "failed."
- **Plural Validation**: If no response is received from the bank within the 10-second window, Plural automatically updates the payment status to "Failed" due to timeout.
- **Refund**: We initiate refunds for late authorised payments.

> 📘 Note:
> 
> Customers can retry to make a new payment against the order.

## Key Features:

1. **Configurable Timeout**: You can configure the late authorization timeout based on your specific needs and the payment modes you use.  
   For example, if a merchant expects a terminal status within 10 minutes for a particular payment mode, Plural’s system will automatically handle the transaction if it exceeds that threshold.
2. **Automatic Reversal**: If a transaction eventually succeeds after the timeout, Plural ensures that the customer receives an automatic reversal if necessary, ensuring customer satisfaction.
3. **Resource Optimisation**: By enforcing a late authorization timeout, Plural prevents merchants from repeatedly querying the transaction status, which can consume system resources and affect overall performance.

## Default Handling

For merchants who have not enabled the late authorization configuration, Plural provides a default solution to prevent system overload:

- **Mode-wise Default Timeout**: Plural implements a default timeout of 5 hours. This ensures that even for merchants without late authorization configuration, transactions will be reversed appropriately after a default period.
- **Transaction Failure Post Timeout**: After the default timeout expires, Plural marks the transaction as failed. This allows the merchant to stop querying the transaction status unnecessarily.

Integrating with Plural payments, you can rest assured that Plural handles all transactions, even those stuck in a non-terminal state, ensuring timely resolution through either a terminal success or an automatic failure.
