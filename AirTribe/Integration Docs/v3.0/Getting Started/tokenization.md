---
title: "Tokenization"
slug: "tokenization"
excerpt: "Learn how to generate, fetch, and delete tokens using Plural tokens APIs."
hidden: false
createdAt: "Thu Feb 13 2025 07:15:47 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu May 22 2025 05:05:07 GMT+0000 (Coordinated Universal Time)"
---
Plural's Token Management helps you to securely process payments, using network-issued tokens instead of storing sensitive card details. In compliance with COFT regulations, you cannot save customer card information directly. Instead, payment networks provision tokens against a customer’s card with their consent.

By integrating Plural’s APIs, you can store and manage these tokens within the customer vault, enabling seamless and secure transactions. These tokens can be used for future payments, simplifying the checkout experience while enhancing security and reducing risks of fraud. Token Management ensures compliance with industry standards, allowing you to offer a frictionless digital payment process without handling sensitive card data.

Plural Tokens APIs can be used for the following actions.

- **Generate Card Token**: Use this API to generate a card token.
- **Generate Cryptogram**: Use this API to generate a Cryptogram.
- **Get Customer Tokens Linked to Customer ID**: Use this API to fetch the Token information generated and saved in the Plural database by passing the `customer_id` in the path parameter.
- **Get Customer Token by Token ID**: Use this API to fetch the specific Token information generated and saved in the Plural database by passing the `token_id` in the path parameter.
- **Delete Customer Token by Customer ID**: Use this API to delete the token information saved in the Plural database.
