---
title: "UPI (Unified Payments Interface)"
slug: "seamless-integration-upi"
excerpt: "Learn about UPI and how they are consumed in the payment space."
hidden: false
createdAt: "Tue Sep 10 2024 09:08:05 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Dec 02 2024 10:38:34 GMT+0000 (Coordinated Universal Time)"
---
## Product Features

1. **UPI Collect Flow**: The UPI Collect feature allows businesses to request payments from customers by generating dynamic payment requests. This feature streamlines payment collection, eliminating the need for traditional methods like cash or card transactions.

- Customers initiate the process by entering their UPI ID or Virtual Payment Address (VPA).
- The UPI ID is validated to ensure accuracy.
- A collect notification is sent to the customer’s UPI app.
- The customer approves the payment request by entering their 4-digit UPI PIN.

This flow enables secure, real-time payments that benefit both merchants and customers by offering a simple and efficient payment experience.

2. **UPI Intent Flow**: The Intent Flow offers customers a frictionless checkout experience by allowing them to select their preferred UPI app for completing payments.

- Customers choose their preferred UPI app from a list.
- They are redirected to the selected app.
- Customers finalize the transaction by entering their 4-digit UPI PIN in the UPI app.

This flow provides users with control over their payment experience, offering a fast and intuitive process.

3. **Third-Party Validation (TPV)**: Third-Party Validation (TPV) helps merchants ensure that transactions are conducted using the customer’s authorized bank account, verified during registration or KYC (Know Your Customer) with the merchant.

***

## Why TPV is Important:

TPV is a regulatory requirement, especially for businesses in the BFSI sector that deal with securities, broking, and mutual funds. According to SEBI (Securities and Exchange Board of India) guidelines, UPI transactions must be made only from bank accounts that customers have registered with your business.

### Who Needs TPV?

TPV is mandatory for merchants in sectors like:

- Broking
- Mutual Funds
- Securities

### Feature Advantages:

- **Transaction Authenticity**: Ensures payments are made only from the customer’s registered bank account.
- **Enhanced Security**: Provides a secure connection between the customer’s bank account and the transaction.
- **Fraud Prevention**: Reduces the risk of unauthorised transactions.
- **Regulatory Compliance**: Complies with SEBI guidelines for UPI transactions.

Refer to our <a href="https://developer.pluralonline.com/docs/about-third-party-validations" target="_blank">Third Party Validation</a> documentation to learn more.
