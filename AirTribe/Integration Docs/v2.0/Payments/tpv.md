---
title: "Third Party Validation"
slug: "tpv"
excerpt: "Learn how you can use Plural TPV APIs to accept payments from your customers."
hidden: false
createdAt: "Fri Jul 19 2024 09:55:22 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Aug 21 2024 11:31:57 GMT+0000 (Coordinated Universal Time)"
---
Third-party validation (TPV) is essential for businesses in the Banking, Financial Services, and Insurance (BFSI) sector, particularly for entities involved in Securities, Broking, and Mutual Funds. According to SEBI guidelines, transactions should originate exclusively from bank accounts registered during customer onboarding. Here’s how they can achieve this using Plural APIs:

1. **Accept Payment**: Use Plural Accept Payment API to generate a token for the particular transaction by including the relevant details such as the payment amount, customer information and a unique reference ID.
2. **Generate a Payment Link**: Use Plural Generate Payment Link API, including relevant payment details and bank account details to generate a payment link.
3. **Handle Payments**: Share the payment links with your investors to accept payment, once they click on it. This action redirects them to their UPI app. Use the generated links to navigate your customers to their UPI apps.

> 📘 Note:
> 
> - We validate the investor’s bank account details against the received payment account. This process ensures compliance with regulatory guidelines and prevents unauthorized payments.

By using Plural TPV Payment Links and validating registered account details, the organization ensures that payments come only from authorized sources.
