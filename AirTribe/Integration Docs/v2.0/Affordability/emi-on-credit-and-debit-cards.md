---
title: "EMI on Credit and Debit Cards"
slug: "emi-on-credit-and-debit-cards"
excerpt: "Learn how to integrate with Plural EMI APIs and offer EMI payments on the purchase."
hidden: false
createdAt: "Fri Nov 15 2024 10:39:19 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Jan 31 2025 07:10:40 GMT+0000 (Coordinated Universal Time)"
---
You can integrate with Plural EMI APIs to allow your users to use the affordability suite for your customers. Before redirecting your merchant to the checkout page, you can allow customers to calculate the monthly installments and check the scheme validations.

To use Plural EMIs it is good to ensure the scheme validation and offer availability on the card.

You can use Plural EMI options using the payment method as `CARD` only.

Plural EMI APIs can be used for the following actions.

- **Calculate EMI**
- **Scheme Validation**
- **Create Order**
- **Create Payment**

In the create payment API response we return the challenge_url you need to use this URL to navigate your users to the checkout page.
