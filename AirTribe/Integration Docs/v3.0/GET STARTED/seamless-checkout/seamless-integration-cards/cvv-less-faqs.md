---
title: "FAQs (Frequently Asked Questions)"
slug: "cvv-less-faqs"
excerpt: "Refer to frequently asked questions and answers about Plural CVV-less card transactions."
hidden: false
createdAt: "Fri Jan 03 2025 04:56:16 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Jan 16 2025 08:55:25 GMT+0000 (Coordinated Universal Time)"
---
<details><summary><b>1. What is CVV?</b></summary><br>CVV is a 3 or 4-digit code, typically located on the back of a card, used to verify the cardholder's identity during card-based transactions.</details>

***

<details><summary><b>2. What is the SwiftPay - NoCVV feature?</b></summary><br>SwiftPay - NoCVV eliminates the need for the CVV during tokenized transactions. This feature enhances the payment experience by allowing users to complete payments with saved cards without entering the CVV. The overall payment flow remains the same, aside from not needing to input the CVV.</details>

***

<details><summary><b>3. What is Tokenization?</b></summary><br>Tokenization is the process of replacing a card number with a unique identifier called a token. This token is specific to the merchant, customer, and token requestor, providing a secure payment method.</details>

***

<details><summary><b>4. Does using this feature compromise security?</b></summary><br>No, this feature doesn’t compromise security. OTP is still required to authenticate the CVV-less transaction. The card token is created using user consent, CVV, and OTP, ensuring secure transactions without the need for CVV entry in future payments. The feature is fully secure and compliant with RBI guidelines.</details>

***

<details><summary><b>5. Is there a transaction limit with this feature?</b></summary><br>There is no specific transaction limit imposed by this feature. Payments can be made up to the limit set by existing constraints such as card limits and account types.</details>

***

<details><summary><b>6. Does this feature support guest checkout journeys?</b></summary><br>No, the CVV-less feature applies only to tokenized transactions. For new or guest checkout users or repeat transactions using the card number (PAN), entering the CVV is still mandatory. If the CVV field is omitted, the transaction will fail.</details>

***

<details><summary><b>7. Do all cards support this feature?</b></summary><br>The CVV-less flow is gaining traction and depends on support from Card Networks and Payment Gateways. Currently, the feature is available for seamless merchant integration (redirect coming soon) with credit and debit cards: full swipe, EMI, full swipe with offers, and EMI with offers on VISA and MasterCard, with Rupay support coming soon.</details>

***

<details><summary><b>8. Will this feature impact other products?</b></summary><br>No, the SwiftPay - No CVV feature will not affect existing products like Payouts, Subscriptions, Offers, EMIs, etc.</details>
