---
title: "Test Card Details"
slug: "payments-test-card-details"
excerpt: "Learn about the test card details needed for testing card payments."
hidden: false
createdAt: "Tue Sep 17 2024 07:04:00 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Oct 18 2024 09:46:00 GMT+0000 (Coordinated Universal Time)"
---
Test cards enable thorough testing of payment solutions in a controlled & secure environment, ensuring a smooth and reliable experience for customers when the system goes live.

Test cards allow businesses to simulate real-world payment scenarios without risking actual transactions. This helps identify issues or bugs in the payment system before going live.

Use the below test card details to test the gateway, fraud detection systems, and transaction workflows function correctly as expected.

**Test Card Details for Indian Payments**

| Network      | Card Number        | CVV   | Expiry Date             | Last 4 Digits |
| :----------- | :----------------- | :---- | :---------------------- | :------------ |
| `VISA`       | `4012001037141112` | `065` | Any future Month & Year | `1112`        |
| `MASTERCARD` | `5200000000001096` | `123` | Any future Month & Year | `1096`        |

**Tokenized Test Card Details**

| Network      | Card Number        | Cryptogram                     | CVV   | Expiry Date             | Last 4 Digits |
| :----------- | :----------------- | :----------------------------- | :---- | :---------------------- | :------------ |
| `VISA`       | `4000000000001091` | `/wAAAAAAl9SX1HsAmWKSgqwAAAA=` | `123` | Any future Month & Year | `1091`        |
| `MASTERCARD` | `5200000000001096` | `/wAAAAAAl9SX1HsAmWKSgqwAAAA=` | `123` | Any future Month & Year | `1096`        |

**Test Card Details for International Remittance**

| Network | Card Number      | CVV   | Expiry Date             | Last 4 Digits |
| :------ | :--------------- | :---- | :---------------------- | :------------ |
| `VISA`  | 4242424242424242 | `123` | Any future Month & Year | `4242`        |

> 📘 Note: **Diners Token Testing**
> 
> - You cannot test Diners token in the UAT (User Acceptance Testing) environment. Currently, this functionality is available only in production environment. To test Diners tokens, please proceed with live transactions with the production setup.
> - Rupay card does not work on UAT environment.
