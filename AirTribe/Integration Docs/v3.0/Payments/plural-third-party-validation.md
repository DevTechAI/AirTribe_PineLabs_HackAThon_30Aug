---
title: "Plural Third Party Validation"
slug: "plural-third-party-validation"
excerpt: "Learn how you can integrate with Plural TPV to validate your customer's Bank Account."
hidden: true
createdAt: "Fri Jul 05 2024 06:37:15 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Jul 05 2024 08:05:16 GMT+0000 (Coordinated Universal Time)"
---
By integrating with Plural’s Third Party Validations (TPV), you can seamlessly comply with SEBI guidelines for online payment collections through major banks at the checkout. Investors can conveniently make payments via UPI (collect and intent flows). According to SEBI guidelines, transactions should exclusively occur from bank accounts registered during customer onboarding.

Third Party Validations (TPV) for bank accounts are crucial for BFSI companies dealing with mutual funds, securities, and brokerage.

## Plural TPV Workflow

The figure below shows the workflow of plural third party validation.

<br />

1. **Create Order**: Use Plural Order API to create an order.
2. **Generate TPV Link**: Use Plural Payment API to create a payment against the order placed.
3. **Share Payment Details**: Merchant can share a QR code or Link to receive payment from their customers. 

> 📘 Note:
> 
> If the payment is made using the registered bank account the payment will be processed else it will be rejected.

## Best Practices

Follow these best practices while doing Plural third party validation.
