---
title: "Bulk Payouts"
slug: "bulk-payouts"
excerpt: "Learn how to initiate a bulk payout using Plural APIs."
hidden: false
createdAt: "Wed Oct 09 2024 05:13:12 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Oct 10 2024 14:43:49 GMT+0000 (Coordinated Universal Time)"
---
By integrating with Plural bulk payouts, you can process multiple payments to bank accounts in a single transaction. This solution eases the payment process for your vendors, employees, and contractors in large volumes. Bulk payouts are highly efficient as they automate and streamline mass payments, saving time and reducing errors associated with manual transactions.

You must enter all the payout bank account details in a file and upload the file in our Upload File API. You must enter the bank account details in the below format.

| clientReferenceId | beneficiaryId | payeeName | accountNumber   | branchCode     | vpa                     | email               | phone        | amountCurrency | amountValue | mode   | dateTime                          | remarks  | saveBeneficiary | validate |
| :---------------- | :------------ | :-------- | :-------------- | :------------- | :---------------------- | :------------------ | :----------- | :------------- | :---------- | :----- | :-------------------------------- | :------- | :-------------- | :------- |
| `test1607-281915` | `0E32EB7CB2`  | `Kevin`   | `1234567890123` | `ICICI0000139` | `kevin@examplebank.com` | `kevin@example.com` | `9876543210` | `INR`          | `100`       | `IMPS` | Format: `yyyy-MM-dd'T'HH:mm:ss'Z` | `Rent`   | `true`          | `false`  |
| `test1607-281916` | `0E32EB7CB3`  | `Bob`     | `1234567890124` | `ICICI0000140` | `bob@examplebank.com`   | `bob@example.com`   | `9876543211` | `INR`          | `1000`      | `IMPS` | Format: `yyyy-MM-dd'T'HH:mm:ss'Z` | `Salary` | `true`          | `false`  |

We process the payout to individual accounts in the queue. To know the status of the payouts create use our Get Bulk Payout Status API to know the real time status or can rely on webhook notifications.
