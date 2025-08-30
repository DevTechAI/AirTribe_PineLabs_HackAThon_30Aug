---
title: "Settlements"
slug: "settlement"
excerpt: "Learn about the Plural settlement process and how to manage your settlements efficiently."
hidden: false
createdAt: "Thu Oct 24 2024 06:28:31 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Jan 17 2025 06:43:06 GMT+0000 (Coordinated Universal Time)"
---
Settlement is the process where the funds collected from your customers' transactions are transferred to your bank account. This marks the final step in the payment cycle, ensuring that the money from completed transactions is deposited into your Bank account. You can manage settlements using APIs or from the Dashboard.

Captured payments are auto-settled into your bank account (which was provided during your KYC verification), following your designated settlement cycle.

## Settlement Types

Settlement types in payment processing refer to the various methods by which funds are transferred from Plural to your bank account. Common settlement types of Plural are listed below.

1. **T+1 Settlements**: This is a standard settlement type where `T` represents the transaction day. The `+1` indicates that the settlement to the merchant occurs one business day after the transaction. This model provides a predictable and routine flow of funds.
2. **Early Batch Settlements**: In this model, transactions are batched and settled earlier than the standard `T+1` timeline. This type of settlement is beneficial for merchants requiring faster access to funds, improving their cash flow management.
3. **Same-Day Settlements**: As the name suggests, same-day settlements involve processing and transferring funds to the merchant on the same day of the transaction. This type of settlement offers the quickest turnaround, ideal for businesses that prioritize immediate liquidity.

> 📘 Note:
> 
> - **Date Range**: The maximum date range for retrieving settlement data is 60 days.
> - **Page Size**: API supports a maximum of 10 records per page, one page at a time.
> - **Historical Data Storage**: Settlement data available for up to 6 months.
> - **Real-Time Availability**: Settlement data is typically real-time, with a potential delay of up to 3 hours in rare cases.
