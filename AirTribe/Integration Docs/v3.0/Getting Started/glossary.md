---
title: "Glossary"
slug: "glossary"
excerpt: "A list of commonly used terms related to Plural by Pine Labs Payments."
hidden: true
createdAt: "Tue Apr 08 2025 04:50:00 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Apr 21 2025 05:56:33 GMT+0000 (Coordinated Universal Time)"
---
The table below lists the commonly used terms in Plural by Pine Labs Payments and their descriptions.

[block:parameters]
{
  "data": {
    "h-0": "Term",
    "h-1": "Descriptions",
    "0-0": "Two Factor Authentication [2FA]",
    "0-1": "2FA is an optional security layer that helps protect your account from unauthorized access. You must provide the code sent to your registered mobile number to sign in.",
    "1-0": "API",
    "1-1": "Application Programming Interface (API) is a software code by which two applications can talk to each other.",
    "2-0": "Authentication",
    "2-1": "The process of verifying the identity of a user, system, or application before granting access. For example, the Bank authenticates customer payment details before processing the transaction.",
    "3-0": "Pre-Authorization",
    "3-1": "Our Order Management system supports `pre-authorization` as an optional feature. When `pre-authorization` is enabled (`pre-auth` = `true`), you gain the flexibility to either **capture** or **cancel** a payment for an order.  \n  \nOnce a payment is successfully created with `pre-authorization` enabled:<ul><li>The amount is debited from the customer's account and credited to Plural.</li><li>You can capture the payment after the product is delivered or the service is fulfilled.</li><li>If the payment is not captured, a refund will automatically be initiated to the customer's account.</ul></li>",
    "4-0": "Authorized",
    "4-1": "When the payment is received successfully. The money is blocked by the issuer at payer account and waiting for the partner authorization to credit to the partner bank account or customer account.",
    "5-0": "Processed",
    "5-1": "When the payment is received successfully. The money is debited from the payer account and credited to the partner bank account successfully.",
    "6-0": "Hosted Checkout",
    "6-1": "Hosted Checkout is a secure, fully-managed payments platform provided by Plural that enables businesses to accept payments quickly across all devices. It's ideal for businesses looking for a fast, simple, and low-effort integration with minimal setup. Additionally, Plural handles all security and compliance requirements.",
    "7-0": "Seamless Checkout",
    "7-1": "Seamless Checkout is a secure, fully managed payment platform provided by Plural that enables businesses to accept payments quickly and seamlessly across all devices. Ideal for businesses that want complete control over the customer experience. Seamless Checkout offers a more customizable option while ensuring customers remain on your website throughout the process.",
    "8-0": "Late Authorization",
    "8-1": "Late authorization refers to a delay in the process of verifying a payment during a transaction. When a customer makes a payment, the payment system typically sends a request to the issuing bank or card network to confirm if funds or credit are available. In a late authorization scenario, this response is delayed, which can cause uncertainty for the customer about whether the payment was successful, potentially leading to a poor user experience.",
    "9-0": "Orders",
    "9-1": "The successful confirmation made by the customer to the vendor to purchase, sell, deliver, or receive goods or services based on agreed-upon terms and conditions.",
    "10-0": "Payments",
    "10-1": "Payment refers to the transfer of money by a customer using any payment method, such as a debit card or credit card, in exchange for a product or service.",
    "11-0": "Payment Gateway",
    "11-1": "Payment Gateway is a technology that allows merchants to securely accept and process payments from customers, typically for online transactions.",
    "12-0": "Payment Methods",
    "12-1": "Payment methods are the options customers choose from when they need to complete a transaction. For example: Credit Cards (e.g., Visa, MasterCard), Debit Cards, Net Banking, UPI (Unified Payments Interface), Wallets (e.g., Paytm, PhonePe, Google Pay), Buy Now, Pay Later (BNPL), EMI (Equated Monthly Instalments), Cash on Delivery (COD) – mostly in e-commerce, Bank Transfers, QR Code Payments etc.",
    "13-0": "Refunds",
    "13-1": "A refund is the return of money to a customer, usually after a purchase has been canceled, a product is returned, or a service is not delivered as expected.",
    "14-0": "Settlements",
    "14-1": "Settlement is when you receive the money paid by your customers for a particular product or service.",
    "15-0": "Third-Party Validation (TPV)",
    "15-1": "Third-Party Validation (TPV) of bank accounts is a mandatory requirement for businesses in the BFSI (Banking, Financial Services, and Insurance) sector, particularly those involved in Securities, Broking, and Mutual Funds. According to Securities and Exchange Board of India (SEBI) guidelines, investors must make transactions exclusively from the bank accounts they registered when onboarding with your business.",
    "16-0": "Tokenization",
    "16-1": "Tokenization is a secure method of processing a card payment where sensitive card details are replaced with network-issued tokens. Instead of saving customer card data, payment networks generate a unique token for each card only after receiving the customer’s consent making the process both secure and regulation-friendly.",
    "17-0": "Transaction",
    "17-1": "A transaction is a payment activity on a Plural by Pine Labs account, including inflow of funds (payments received), payouts (payments made to employees, contractors, and vendors), and refunds."
  },
  "cols": 2,
  "rows": 18,
  "align": [
    "left",
    "left"
  ]
}
[/block]
