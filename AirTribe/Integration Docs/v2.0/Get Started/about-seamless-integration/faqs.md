---
title: "FAQs"
slug: "faqs"
excerpt: "Learn about the CVV FAQs."
hidden: false
createdAt: "Mon Jan 06 2025 05:29:41 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jan 07 2025 04:43:50 GMT+0000 (Coordinated Universal Time)"
---
1. **What is CVV**?  
   CVV is a 3 or 4-digit code, typically located on the back of a card, used to verify the cardholder's identity during card-based transactions.
2. **What is the SwiftPay - NoCVV feature**?  
   SwiftPay - NoCVV eliminates the need for the CVV during tokenized transactions. This feature enhances the payment experience by allowing users to complete payments with saved cards without entering the CVV. The overall payment flow remains the same, aside from not needing to input the CVV.
3. **What is Tokenization**?  
   Tokenization is the process of replacing a card number with a unique identifier called a token. This token is specific to the merchant, customer, and token requestor, providing a secure payment method.
4. **Does using this feature compromise security**?  
   No, this feature doesn’t compromise security. OTP is still required to authenticate the CVV-less transaction. The card token is created using user consent, CVV, and OTP, ensuring secure transactions without the need for CVV entry in future payments. The feature is fully secure and compliant with RBI guidelines.
5. **Is there a transaction limit with this feature**?  
   There is no specific transaction limit imposed by this feature. Payments can be made up to the limit set by existing constraints such as card limits and account types.
6. **Does this feature support guest checkout journeys**?  
   No, the CVV-less feature applies only to tokenized transactions. For new or guest checkout users or repeat transactions using the card number (PAN), entering the CVV is still mandatory. If the CVV field is omitted, the transaction will fail.
7. **Do all cards support this feature**?  
   The CVV-less flow is gaining traction and depends on support from Card Networks and Payment Gateways. Currently, the feature is available for seamless merchant integration (redirect coming soon) with credit and debit cards: full swipe, EMI, full swipe with offers, and EMI with offers on VISA and MasterCard, with Rupay support coming soon.
8. **Will this feature impact other products**?  
   No, the SwiftPay - NoCVV feature will not affect existing products like Payouts, Subscriptions, Offers, EMIs, etc.
