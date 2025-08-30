---
title: "Create Payment"
slug: "create-payment"
excerpt: "Learn how to integrate with Plural Create Payment API."
hidden: true
createdAt: "Fri Feb 28 2025 12:46:30 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Mar 03 2025 07:16:54 GMT+0000 (Coordinated Universal Time)"
---
Subscription payments allow you to automate recurring billing for your customers using UPI payment methods. To facilitate these payments, you can use the Create Payment API to initiate transactions based on the chosen UPI method.

## UPI Payment Methods Supported

- **UPI Intent**
- **UPI Collect**

By integrating these UPI payment methods into your subscription flow, you can enable a seamless and automated billing process, improving your customer convenience while ensuring a stable revenue stream.

In the create payment API response we return the `challenge_url` you need to use this URL to navigate your users to the checkout page.
