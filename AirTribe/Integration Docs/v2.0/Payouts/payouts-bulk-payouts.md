---
title: "Bulk Payouts"
slug: "payouts-bulk-payouts"
excerpt: "Learn how you can use Plural bulk payouts to initiate multiple payouts."
hidden: false
createdAt: "Wed Oct 09 2024 11:09:24 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Oct 10 2024 14:37:49 GMT+0000 (Coordinated Universal Time)"
---
Learn how you can use Plural Payments to accept payments from your customers.

By integrating with Plural bulk payouts, you can process multiple payments to bank accounts in a single transaction. This solution eases the payment process for your vendors, employees, and contractors in large volumes. Bulk payouts are highly efficient as they automate and streamline mass payments, saving time and reducing errors associated with manual transactions.

You must enter all the payout bank account details in a file and upload the file in our Upload File API. You must enter the bank account details in the below format.

| clientReferenceId | beneficiaryId | payeeName | accountNumber   | branchCode     | vpa                     | email               | phone        | amountCurrency | amountValue | mode   | dateTime                          | remarks  | saveBeneficiary | validate |
| :---------------- | :------------ | :-------- | :-------------- | :------------- | :---------------------- | :------------------ | :----------- | :------------- | :---------- | :----- | :-------------------------------- | :------- | :-------------- | :------- |
| `test1607-281915` | `0E32EB7CB2`  | `Kevin`   | `1234567890123` | `ICICI0000139` | `kevin@examplebank.com` | `kevin@example.com` | `9876543210` | `INR`          | `100`       | `IMPS` | Format: `yyyy-MM-dd'T'HH:mm:ss'Z` | `Rent`   | `true`          | `false`  |
| `test1607-281916` | `0E32EB7CB3`  | `Bob`     | `1234567890124` | `ICICI0000140` | `bob@examplebank.com`   | `bob@example.com`   | `9876543211` | `INR`          | `1000`      | `IMPS` | Format: `yyyy-MM-dd'T'HH:mm:ss'Z` | `Salary` | `true`          | `false`  |

We process the payout to individual accounts in the queue. To know the status of the payouts create use our Get Bulk Payout Status API to know the real time status or can rely on webhook notifications.

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/v2.0/reference/prerequisite" target="_blank">Prerequisite</a> documentation to learn more about the fields and type.

## Key Features of Bulk Payouts:

1. **Batch Processing**: Payouts are processed in batches, where multiple payouts are bundled into a single payout request.
2. **Multiple Payment Methods**: Bulk payouts can be made via bank account transfers and UPI.
3. **Automated and Scheduled Payouts**: These payouts can be scheduled to process at specific intervals or triggered based on predefined conditions.
4. **Error Handling and Reconciliation**: Comprehensive reporting and tracking allow businesses to easily identify and resolve any failed payout, ensuring that all payouts are properly processed.
5. **High Scalability**: Whether paying hundreds or thousands of recipients, bulk payouts are designed to handle large volumes of payouts without manual intervention.

## Benefits:

**Time Efficiency**: A single request can handle hundreds or thousands of payments, reducing manual efforts and the time required for mass disbursements.  
**Cost Efficiency**: Bulk processing reduces transaction fees that might be higher with individual transfers.  
**Error Minimization**: Automation reduces the likelihood of human error when sending payouts manually.  
Bulk payouts provide a highly efficient, automated, and scalable process for businesses to handle multiple payouts, offering significant advantages over traditional, manual payout methods.

## Use Cases for Bulk Payouts:

- **Employee Salaries**: Companies can use bulk payouts to deposit salaries into their employees’ bank accounts in a single batch process.
- **Vendor Payments**: Large businesses can pay multiple vendors at once, reducing the administrative burden of individual transfers.
- **Incentives & Cashback**: Businesses running promotional campaigns or loyalty programs can distribute incentives, cashback, or rewards to a large number of customers simultaneously.
- **Loan Disbursement**: Financial institutions can disburse loans or payments to multiple beneficiaries in one go.
