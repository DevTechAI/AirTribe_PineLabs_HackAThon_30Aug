---
title: "Payments"
slug: "about-payment"
excerpt: "Learn how you can use Plural Payments to accept payments from your customers."
hidden: false
createdAt: "Fri Sep 27 2024 06:31:51 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Oct 17 2024 15:11:27 GMT+0000 (Coordinated Universal Time)"
---
Payments refer to the transfer of money from one person to another person, in exchange for goods and services. Online payments are an essential aspect of commerce, ensuring that businesses receive compensation for their offerings and customers can complete the payments conveniently and securely.

To use Plurals Payment APIs as a prerequisite you are required to create an order.

Using Plural Payment APIs you can accept payments using the below methods.

- `cards`,
- `upi`, and
- `points`

Plural Payments APIs can be used for the following actions.

- <a style="text-decoration:underline;" href="https://developer.pluralonline.com/v3.0/reference/payments-create" target="_blank">Create a Payment</a>
- <a style="text-decoration:underline;" href="https://developer.pluralonline.com/v3.0/reference/payments-refund" target="_blank">Refund a Payment</a> 

In the create payment API response we return the `challenge_url` you need to use this URL to navigate your users to the checkout page.
