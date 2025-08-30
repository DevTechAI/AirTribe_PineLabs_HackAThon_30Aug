---
title: "Tokenization"
slug: "tokenizations"
excerpt: "Learn about the Plural Tokens"
hidden: true
createdAt: "Mon Feb 10 2025 09:17:45 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Feb 18 2025 04:58:43 GMT+0000 (Coordinated Universal Time)"
---
Plural’s Token Management allows you to securely process payments by using network-issued tokens instead of storing sensitive card details. In compliance with COFT regulations, you cannot save customer card information directly. Instead, payment networks provision tokens against a customer’s card with their consent.

By integrating Plural’s APIs, you can store and manage these tokens within the customer vault, enabling seamless and secure transactions. These tokens can be used for future payments, simplifying the checkout experience while enhancing security and reducing risks for fraud. Token Management ensures compliance with industry standards, allowing you to offer a frictionless digital payment process without handling sensitive card data.

## How Tokens Are Stored in the System

### Token

A Token is a non-sensitive replacement for the actual Primary Account Number (PAN) of a payment card. Its primary role is to store card information securely and be used for future transactions without exposing sensitive data. When a user saves a card on a Plural platform, the system generates a Token ID. This ID can then be used for transactions, subscriptions, or recurring payments, without the need to store or transmit the actual card number.

### Service provider token

A Service Provider Token is a specific token that is created and managed by an external entity - either a card network (e.g., Visa, Mastercard) or a card issuer (e.g., a bank). This token is essentially a representation of the card created by the third-party service provider to replace the actual PAN. The Service Provider Token is linked to the Token ID within the platform, but it reflects the external tokenization source used for the token creation.
