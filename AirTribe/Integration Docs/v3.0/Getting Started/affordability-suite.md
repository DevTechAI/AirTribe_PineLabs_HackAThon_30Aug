---
title: "Affordability Suite"
slug: "affordability-suite"
excerpt: "Learn how to integrate with Plural EMI APIs and offer EMI payments on the purchase."
hidden: false
createdAt: "Tue Jan 21 2025 13:57:26 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jan 28 2025 13:31:54 GMT+0000 (Coordinated Universal Time)"
---
You can integrate with Plural EMI APIs to allow your users to use the affordability suite for your customers. Before redirecting your merchant to the checkout page, you can allow customers to calculate the monthly instalments and discover the offers.

You can use Plural EMI options using the payment method as `CARD` only.

Plural EMI APIs can be used for the following actions.

- **Offer Discovery**: 
- **Offer Discovery Cardless**: 
- **Offer Validation**:
- **Create Order**:
- **Create Payment**: 

In the create payment API response we return the challenge_url you need to use this URL to navigate your users to the checkout page.

## Pre-authorization

In our orders API, we provide pre-authorization as an option. With pre-authorization set to true, you can capture payment for an order after successful delivery. 

When `pre-auth` is set to true, and the payment is successfully created, you have the following options:

1. **Capture Order**: Utilize the plural capture order API in your backend to capture the payment against an order.
2. **Cancel Order**: Use the plural cancel order API in your backend to cancel the payment against an order.
