---
title: "Prerequisite"
slug: "bulk-payouts-prerequisite"
excerpt: "Learn about the prerequisites of our Upload file API."
hidden: false
createdAt: "Wed Oct 09 2024 10:36:48 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Oct 10 2024 14:44:26 GMT+0000 (Coordinated Universal Time)"
---
Plural upload file API use the file uploaded in the request and process the individual payouts in a queue. You must enter the bank account details in the below format.

| clientReferenceId | beneficiaryId | payeeName | accountNumber   | branchCode     | vpa                     | email               | phone        | amountCurrency | amountValue | mode   | dateTime                          | remarks  | saveBeneficiary | validate |
| :---------------- | :------------ | :-------- | :-------------- | :------------- | :---------------------- | :------------------ | :----------- | :------------- | :---------- | :----- | :-------------------------------- | :------- | :-------------- | :------- |
| `test1607-281915` | `0E32EB7CB2`  | `Kevin`   | `1234567890123` | `ICICI0000139` | `kevin@examplebank.com` | `kevin@example.com` | `9876543210` | `INR`          | `100`       | `IMPS` | Format: `yyyy-MM-dd'T'HH:mm:ss'Z` | `Rent`   | `true`          | `false`  |
| `test1607-281916` | `0E32EB7CB3`  | `Bob`     | `1234567890124` | `ICICI0000140` | `bob@examplebank.com`   | `bob@example.com`   | `9876543211` | `INR`          | `1000`      | `IMPS` | Format: `yyyy-MM-dd'T'HH:mm:ss'Z` | `Salary` | `true`          | `false`  |

The table below lists all the fields that must be included in the file to be uploaded using our Upload File API for processing a bulk payout.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Required Type",
    "h-3": "Description",
    "0-0": "clientReferenceId",
    "0-1": "`string`",
    "0-2": "`M`",
    "0-3": "Unique identifier entered while creating a Payout request.  \n  \nExample: `test1607-281915`",
    "1-0": "beneficiaryId",
    "1-1": "`string`",
    "1-2": "`O`",
    "1-3": "Unique Identifier representing the beneficiary.  \n  \nExample: `0E32EB7CB2`",
    "2-0": "payeeName",
    "2-1": "`string`",
    "2-2": "`C`",
    "2-3": "Beneficiary name.  \n  \nExample: `Kevin`",
    "3-0": "accountNumber",
    "3-1": "`string`",
    "3-2": "`C`",
    "3-3": "Beneficiary bank account number.  \n  \nExample: `1234567890123`",
    "4-0": "branchCode",
    "4-1": "`string`",
    "4-2": "`C`",
    "4-3": "Beneficiary branch IFSC.  \n  \nExample: `ICICI0000139`",
    "5-0": "vpa",
    "5-1": "`string`",
    "5-2": "`C`",
    "5-3": "Beneficiary VPA handle.  \n  \nExample: `kevin.bob@examplebank.com`",
    "6-0": "email",
    "6-1": "`string`",
    "6-2": "`O`",
    "6-3": "Beneficiary email address.  \n  \nExample: `kevin.bob@example.com`",
    "7-0": "phone",
    "7-1": "`string`",
    "7-2": "`O`",
    "7-3": "Beneficiary phone number.  \n  \nExample: `9876543210`",
    "8-0": "amountCurrency",
    "8-1": "`string`",
    "8-2": "`M`",
    "8-3": "Type of currency.  \n  \nExample: `INR`",
    "9-0": "amountValue",
    "9-1": "`string`",
    "9-2": "`M`",
    "9-3": "The transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1).</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
    "10-0": "mode",
    "10-1": "`string`",
    "10-2": "`M`",
    "10-3": "Mode you wish to initiate a payout.  \n  \nAccepted values:<ul><li>`UPI`</li><li>`IMPS`</li><li>`NEFT`</li><li>`RTGS`</ul></li>",
    "11-0": "dateTime",
    "11-1": "`string`",
    "11-2": "`O`",
    "11-3": "Use this parameter to schedule a payout for future. The time value is in UTC.  \n  \nExample: `yyyy-MM-dd'T'HH:mm:ss'Z`",
    "12-0": "remarks",
    "12-1": "`string`",
    "12-2": "`M`",
    "12-3": "Payout remarks.  \n  \nExample: `Rent`",
    "13-0": "saveBeneficiary",
    "13-1": "`boolean`",
    "13-2": "`O`",
    "13-3": "Accepted values to save beneficiary.<ul><li>`true`: Beneficiary details are saved against the account.</li><li>`false`: Beneficiary details are not saved against the account.</ul></li>",
    "14-0": "validate",
    "14-1": "`boolean`",
    "14-2": "`O`",
    "14-3": "Accepted values to validate the VPA handle before initiating a payout.<ul><li>`true`: VPA verification is done.</li><li>`false`: VPA verification is not done.</ul></li>"
  },
  "cols": 4,
  "rows": 15,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]
