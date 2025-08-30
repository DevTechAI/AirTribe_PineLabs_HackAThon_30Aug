---
title: "Test Details"
slug: "test-details"
excerpt: "Use the following test credentials to test transactions for both one-time and EMI payments."
hidden: false
createdAt: "Mon Sep 02 2024 10:51:21 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Oct 18 2024 09:46:38 GMT+0000 (Coordinated Universal Time)"
---
## One Time Payments

| Card Network | Card Number         | CVV        | Expiry Date     |
| :----------- | :------------------ | :--------- | :-------------- |
| Mastercard   | 5267 3181 8797 5449 | Random CVV | Any future date |
| Visa         | 4111 1111 1111 1111 | Random CVV | Any future date |

## Credit Card EMI Payments

| Card Network    | Card Issuer | Card Number         | CVV | Expiry Date     |
| :-------------- | :---------- | :------------------ | :-- | :-------------- |
| Visa/Mastercard | HDFC        | 4012 0010 3714 1112 | 123 | Any future date |
| Visa            | ICICI       | 4444 3333 2222 1111 | 123 | Any future date |
| Mastercard      | ICICI       | 5241 8100 0000 0000 | 123 | Any future date |

## Debit Card EMI Payments

| Card Issuer | Card Number         | Mobile Number |
| :---------- | :------------------ | :------------ |
| HDFC        | 4444 3333 2222 1111 | 9686540540    |
| Kotak       | 4012 0010 3717 1234 | 8470086938    |

> 📘 Note:
> 
> - Currently, we do not have any test credentials for UPI and wallet transactions on UAT.
> - Rupay card does not work on UAT environment.
