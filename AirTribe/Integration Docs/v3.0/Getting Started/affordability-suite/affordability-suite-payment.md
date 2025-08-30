---
title: "Payment"
slug: "affordability-suite-payment"
excerpt: "Learn how to integrate with Plural orders API."
hidden: false
createdAt: "Wed Jan 22 2025 17:57:00 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jan 28 2025 13:31:56 GMT+0000 (Coordinated Universal Time)"
---
With Plural EMI (Equated Monthly Installments), you can allow your customers to break down the cost of a product into smaller monthly payments instead of paying the full amount. Your customers can use this to purchase high-value items like electronics, appliances, vehicles, or even services like education and travel.

To use Plurals Payment APIs as a prerequisite you are required to create an order and link the order against the payment.

Using Plural Payment APIs you can accept EMI payments using `cards`only.

Plural Payments APIs can be used for the following actions.

- Create Payment
- Refund Payment

In the create payment API response we return the `challenge_url` you need to use this URL to navigate your users to the checkout page.
