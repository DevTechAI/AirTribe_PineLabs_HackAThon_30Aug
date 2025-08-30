---
title: "Payments"
slug: "payments"
excerpt: "Learn how you can use Plural Payments APIs to accept payments from your customers."
hidden: true
createdAt: "Thu Jul 11 2024 09:17:28 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Sep 26 2024 15:40:48 GMT+0000 (Coordinated Universal Time)"
---
Payments refer to the transfer of money from one person to another person, in exchange for goods and services. Online payments are an essential aspect of commerce, ensuring that businesses receive compensation for their offerings and customers can complete the payments conveniently and securely.

To use Plurals Payment APIs as a prerequisite you are required to create an order and link the order against the payment.

Using Plural Payment APIs you can accept payments using `cards`, `upi`, and `points`

Plural Payments APIs can be used for the following actions.

- Create Payment
- Refund Payment

In the create payment API response we return the `challenge_url` you need to use this URL to navigate your users to the checkout page.
