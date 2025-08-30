---
title: "Cards"
slug: "seamless-integration-cards"
excerpt: "Learn about cards and how they are consumed in the payment space."
hidden: false
createdAt: "Tue Sep 10 2024 08:12:29 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Nov 13 2024 07:05:33 GMT+0000 (Coordinated Universal Time)"
---
## Overview

Cards, in the context of payments, refer to physical or virtual instruments used to facilitate financial transactions. They typically come in the form of plastic cards with embedded microchips or magnetic stripes, although virtual cards are gaining popularity for online transactions. These cards are linked to a specific account, allowing users to make purchases or withdrawals without carrying cash.

> 🚧 Watch Out
> 
> - To Integrate with Plural seamless checkout flow you must have a PCI compliance certificate.

***

## What are the different types of cards?

- **Prepaid Cards**: Cards that are loaded with funds in advance and can be used until the balance is depleted.
- **Debit Cards**: Linked directly to the cardholder's bank account, allowing them to make purchases using funds available in the account.
- **Credit Cards**: Provide a line of credit to the cardholder, allowing them to borrow funds up to a certain limit for purchases, subject to interest charges if the balance is not paid in full by the due date.
- **Corporate Cards**: Issued to employees of companies for business-related expenses, with features such as expense tracking, spending limits, and integration with corporate accounting systems.

***

## Who are the players in the cards ecosystem?

- **Cardholders**: Individuals or entities who own and use the cards for purchases or transactions.
- **Merchants**: Businesses or individuals who accept card payments for goods or services.
- **Card Issuers**: Banks or financial institutions that issue cards to customers and are responsible for account management, risk assessment, and authorization.
- **Card Networks**: Organizations such as Visa, Mastercard, American Express, and Discover, which facilitate transactions between cardholders, merchants, and issuers.
- **Acquiring Banks**: Financial institutions that establish and maintain merchant accounts, enabling businesses to accept card payments.
- **Payment Gateways**: Companies that provide technology and infrastructure for transaction processing, often acting as intermediaries between merchants and card networks.

***

## How do card payments work?

The card payments ecosystem involves a complex network of entities and processes that facilitate electronic transactions between customers, merchants, banks, and payment gateways. Here's an overview of how the system works:

- **Customer Initiates Payment**: The process begins when a customer makes a purchase using a credit or debit card on the merchant's website. The customer provides card details, including the card number, expiry date, and CVV code.
- **Merchant's Website & Mobile Apps**: The merchant's website/mobile application collects the payment information and securely transmits it to the Payment Gateway.
- **Payment Gateway**: The Payment Gateway acts as an intermediary between the merchant's website and the acquiring bank. It encrypts the customer's payment details and forwards the information to the acquiring bank for authorization.
- **Acquiring Bank**: The Acquiring Bank receives the payment authorization request from the Payment Gateway. It checks the transaction details, verifies the customer's account, and ensures that there are sufficient funds in the account for the transaction.
- **Authorization**: If the transaction is approved, the acquiring bank sends an authorization code back to the Payment Gateway. If declined, the reason for the decline is communicated back to the merchant.  
  Payment Processor: The Payment Processor, affiliated with the acquiring bank, processes the authorized transactions. It debits the customer's account and credits the merchant's account with the transaction amount, minus any fees.
- **Merchant Confirmation**: The Payment Gateway informs the merchant's website about the transaction status. The customer receives a confirmation of the successful payment.
