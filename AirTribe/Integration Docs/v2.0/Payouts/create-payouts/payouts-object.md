---
title: "Object"
slug: "payouts-object"
excerpt: "Overview of Payout APIs sample response object."
hidden: false
createdAt: "Fri Jul 19 2024 07:07:56 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Oct 10 2024 14:42:02 GMT+0000 (Coordinated Universal Time)"
---
## Payout to Beneficiary

Shown below is a sample response returned for a payout to beneficiary API.

```json Payout to Beneficiary Sample Response
{
  "clientReferenceId": "test1607-281913",
  "requestReferenceId": "req-446b28bdd4e0444ab8cc381278c0a7db",
  "paymentReferenceId": "txn-a9304bb5bdd6444782466575afd023e4",
  "beneficiaryId": "0E32EB7CB2",
  "payeeName": "Kevin",
  "accountNumber": "1234567890123",
  "branchCode": "ICICI0000139",
  "vpa": "",
  "email": "kevin.bob@example.com",
  "phone": "9021221212",
  "amount": {
    "currency": "INR",
    "value": 25000
  },
  "mode": "IMPS",
  "status": "PENDING",
  "message": "Payment instruction pending to be executed",
  "scheduledAt": "",
  "remarks": "Rent",
  "_links": [
    {
      "rel": "status",
      "href": "http://pluralqa.pinepg.in:8000/payouts/v2/payments?paymentReferenceId=txn-a9304bb5bdd6444782466575afd023e4"
    }
  ]
}
```

The table below lists the various parameters returned in the payout to beneficiary sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "clientReferenceId",
    "0-1": "`string`",
    "0-2": "Unique identifier entered while creating a Payout request.  \n  \nExample: `test1607-281915`",
    "1-0": "requestReferenceId",
    "1-1": "`string`",
    "1-2": "Unique identifier of the payout request in Plural database.  \n  \nExample:  `req-446b28bdd4e0444ab8cc381278c0a7db`",
    "2-0": "paymentReferenceId",
    "2-1": "`string`",
    "2-2": "Unique identifier of the payout reference in Plural database.  \n  \nExample: `txn-a9304bb5bdd6444782466575afd023e4`",
    "3-0": "beneficiaryId",
    "3-1": "`string`",
    "3-2": "Unique Identifier representing the beneficiary.  \n  \nExample: `0E32EB7CB2`",
    "4-0": "payeeName",
    "4-1": "`string`",
    "4-2": "Beneficiary name.  \n  \nExample: `Kevin`",
    "5-0": "accountNumber",
    "5-1": "`string`",
    "5-2": "Beneficiary bank account number.  \n  \nExample: `1234567890123`",
    "6-0": "branchCode",
    "6-1": "`string`",
    "6-2": "Beneficiary branch IFSC.  \n  \nExample: `ICICI0000139`",
    "7-0": "vpa",
    "7-1": "`string`",
    "7-2": "Beneficiary VPA handle.  \n  \nExample: `kevin.bob@examplebank.com`",
    "8-0": "email",
    "8-1": "`string`",
    "8-2": "Beneficiary email address.  \n  \nExample: `kevin.bob@example.com`",
    "9-0": "phone",
    "9-1": "`string`",
    "9-2": "Beneficiary phone number.  \n  \nExample: `9876543210`",
    "10-0": "amount",
    "10-1": "`object`",
    "10-2": "An object that contains the payout amount details.",
    "11-0": "mode",
    "11-1": "`string`",
    "11-2": "Mode you wish to initiate a payout.  \n  \nAccepted values:<ul><li>`UPI`</li><li>`IMPS`</li><li>`NEFT`</li><li>`RTGS`</ul></li>",
    "12-0": "status",
    "12-1": "`string`",
    "12-2": "Payout status.  \n  \nExample: `PENDING`",
    "13-0": "message",
    "13-1": "`string`",
    "13-2": "Corresponding message to the status.  \n  \nExample: `Payment instruction pending to be executed`",
    "14-0": "scheduledAt",
    "14-1": "`string`",
    "14-2": "Use this parameter to schedule a payout for future. The time value is in UTC.  \n  \nExample: ",
    "15-0": "remarks",
    "15-1": "`string`",
    "15-2": "Payout remarks.  \n  \nExample: `Rent`",
    "16-0": "\\_links",
    "16-1": "`boolean`",
    "16-2": "An object that contains the payment link details."
  },
  "cols": 3,
  "rows": 17,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This object is part of the `payout to beneficiary` sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`string`",
    "0-2": "Type of currency.  \n  \nExample: `INR`",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "The transaction amount is Paisa.  <ul><li>Minimum value: `100` (₹1).</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### \_Links [Child Object]

The table below lists the various parameters in the `links` child object. This object is part of the `payout to beneficiary` sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "rel",
    "0-1": "`string`",
    "0-2": "Relationship to the resource.  \n  \nExample: `status`",
    "1-0": "href",
    "1-1": "`string`",
    "1-2": "Link to access the resource.  \n  \nExample: `http://pluralqa.pinepg.in:8000/payouts/v2/payments?paymentReferenceId=txn-a9304bb5bdd6444782466575afd023e4`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Payout to Account Number

Shown below is a sample response returned for a payout to account number API.

```json Payout to Account Number Sample Response
{
  "clientReferenceId": "test1607-281915",
  "beneficiaryId": "0E32EB7CB2",
  "requestReferenceId": "req-6fb7b8893b724a478b0ffe308fc8f742",
  "paymentReferenceId": "txn-f642f7f6f2af4d5bb8da5de9e5f0bbc8",
  "accountNumber": "3988439646104",
  "branchCode": "NPCI0000139",
  "vpa": "",
  "email": "abhi@gmail.com",
  "phone": "9021221212",
  "amount": {
    "currency": "INR",
    "value": 250000
  },
  "mode": "IMPS",
  "status": "PENDING",
  "message": "Payment instruction pending to be executed",
  "scheduledAt": "",
  "remarks": "Success1",
  "_links": [
    {
      "rel": "status",
      "href": "http://pluralqa.pinepg.in:8000/payouts/v2/payments?paymentReferenceId=txn-f642f7f6f2af4d5bb8da5de9e5f0bbc8"
    }
  ]
}
```

The table below lists the various parameters returned in the payout to account number sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "clientReferenceId",
    "0-1": "`string`",
    "0-2": "Unique identifier entered while creating a Payout request.  \n  \nExample: `test1607-281915`",
    "1-0": "beneficiaryId",
    "1-1": "`string`",
    "1-2": "Unique Identifier representing the beneficiary.  \n  \nExample: `0E32EB7CB2`",
    "2-0": "requestReferenceId",
    "2-1": "`string`",
    "2-2": "Unique identifier of the payout request in Plural database.  \n  \nExample:  `req-446b28bdd4e0444ab8cc381278c0a7db`",
    "3-0": "paymentReferenceId",
    "3-1": "`string`",
    "3-2": "Unique identifier of the payout reference in Plural database.  \n  \nExample: `txn-a9304bb5bdd6444782466575afd023e4`",
    "4-0": "payeeName",
    "4-1": "`string`",
    "4-2": "Beneficiary name.  \n  \nExample: `Kevin`",
    "5-0": "accountNumber",
    "5-1": "`string`",
    "5-2": "Beneficiary bank account number.  \n  \nExample: `1234567890123`",
    "6-0": "branchCode",
    "6-1": "`string`",
    "6-2": "Beneficiary branch IFSC.  \n  \nExample: `ICICI0000139`",
    "7-0": "vpa",
    "7-1": "`string`",
    "7-2": "Beneficiary VPA handle.  \n  \nExample: `kevin.bob@examplebank.com`",
    "8-0": "email",
    "8-1": "`string`",
    "8-2": "Beneficiary email address.  \n  \nExample: `kevin.bob@example.com`",
    "9-0": "phone",
    "9-1": "`string`",
    "9-2": "Beneficiary phone number.  \n  \nExample: `9876543210`",
    "10-0": "amount",
    "10-1": "`object`",
    "10-2": "An object that contains the payout amount details.",
    "11-0": "mode",
    "11-1": "`string`",
    "11-2": "Mode you wish to initiate a payout.  \n  \nAccepted values:<ul><li>`UPI`</li><li>`IMPS`</li><li>`NEFT`</li><li>`RTGS`</ul></li>",
    "12-0": "status",
    "12-1": "`string`",
    "12-2": "Payout status.  \n  \nExample: `PENDING`",
    "13-0": "message",
    "13-1": "`string`",
    "13-2": "Corresponding message to the status.  \n  \nExample: `Payment instruction pending to be executed`",
    "14-0": "scheduledAt",
    "14-1": "`string`",
    "14-2": "Use this parameter to schedule a payout for future. The time value is in UTC.  \n  \nExample: ",
    "15-0": "remarks",
    "15-1": "`string`",
    "15-2": "Payout remarks.  \n  \nExample: `Rent`",
    "16-0": "\\_links",
    "16-1": "`boolean`",
    "16-2": "An object that contains the payment link details."
  },
  "cols": 3,
  "rows": 17,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This object is part of the `payout to account number` sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`string`",
    "0-2": "Type of currency.  \n  \nExample: `INR`",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "The transaction amount is Paisa.  <ul><li>Minimum value: `100` (₹1).</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### \_Links [Child Object]

The table below lists the various parameters in the `links` child object. This object is part of the `payout to account number` sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "rel",
    "0-1": "`string`",
    "0-2": "Relationship to the resource.  \n  \nExample: `status`",
    "1-0": "href",
    "1-1": "`string`",
    "1-2": "Link to access the resource.  \n  \nExample: `http://pluralqa.pinepg.in:8000/payouts/v2/payments?paymentReferenceId=txn-a9304bb5bdd6444782466575afd023e4`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Scheduled Account Payout

Shown below is a sample response returned for a scheduled account payout API.

```json Scheduled Account Payout Sample Response
{
  "clientReferenceId": "test4feb0-11",
  "requestReferenceId": "req-6efea0eaabb9403ab2a2e172695f4764",
  "paymentReferenceId": "txn-7d349ed08ad041e385ee2a03ebf6cf25",
  "payeeName": "Rishendrasai",
  "accountNumber": "919000664017",
  "branchCode": "PYTM0123456",
  "vpa": "",
  "email": "s.john@g.com",
  "phone": "9000664017",
  "amount": {
    "currency": "INR",
    "value": 100
  },
  "mode": "IMPS",
  "status": "SCHEDULED",
  "message": "Payment instruction scheduled for execution",
  "scheduledAt": "2024-03-24T08:24:00Z",
  "remarks": "Test transaction",
  "_links": [
    {
      "rel": "status",
      "href": "http://pluralqa.pinepg.in:8000/payouts/v2/payments?paymentReferenceId=txn-7d349ed08ad041e385ee2a03ebf6cf25"
    }
  ]
}
```
```json Update Scheduled Payout Sample Response
{
  "clientReferenceId": "test4feb0-10",
  "requestReferenceId": "req-7c85bda19bf141c981b94e750c6041b6",
  "paymentReferenceId": "txn-f9e00a80a357418d908a67bd30cdbc37",
  "payeeName": "Rishendrasai",
  "accountNumber": "919000664016",
  "branchCode": "PYTM0123456",
  "vpa": "",
  "email": "s.john@g.com",
  "phone": "9000664016",
  "amount": {
    "currency": "INR",
    "value": 100
  },
  "mode": "IMPS",
  "status": "SCHEDULED",
  "message": "Payment instruction pending to be executed",
  "scheduledAt": "",
  "remarks": "Test transaction",
  "_links": [
    {
      "rel": "status",
      "href": "http://pluralqa.pinepg.in:8000/payouts/v2/payments?paymentReferenceId=txn-f9e00a80a357418d908a67bd30cdbc37"
    }
  ]
}
```
```json Cancel Schedule Payout
{
  "clientReferenceId": "test4feb0-10",
  "requestReferenceId": "req-7c85bda19bf141c981b94e750c6041b6",
  "paymentReferenceId": "txn-f9e00a80a357418d908a67bd30cdbc37",
  "payeeName": "Rishendrasai",
  "accountNumber": "919000664016",
  "branchCode": "PYTM0123456",
  "vpa": "",
  "email": "s.john@g.com",
  "phone": "9000664016",
  "amount": {
    "currency": "INR",
    "value": 100
  },
  "mode": "IMPS",
  "status": "CANCELLED",
  "message": "Payment instruction pending to be executed",
  "scheduledAt": "",
  "remarks": "Test transaction",
  "_links": [
    {
      "rel": "status",
      "href": "http://pluralqa.pinepg.in:8000/payouts/v2/payments?paymentReferenceId=txn-f9e00a80a357418d908a67bd30cdbc37"
    }
  ]
}
```

The table below lists the various parameters returned in the scheduled account payout sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "clientReferenceId",
    "0-1": "`string`",
    "0-2": "Unique identifier entered while creating a Payout request.  \n  \nExample: `test1607-281915`",
    "1-0": "requestReferenceId",
    "1-1": "`string`",
    "1-2": "Unique identifier of the payout request in Plural database.  \n  \nExample:  `req-446b28bdd4e0444ab8cc381278c0a7db`",
    "2-0": "paymentReferenceId",
    "2-1": "`string`",
    "2-2": "Unique identifier of the payout reference in Plural database.  \n  \nExample: `txn-a9304bb5bdd6444782466575afd023e4`",
    "3-0": "payeeName",
    "3-1": "`string`",
    "3-2": "Beneficiary name.  \n  \nExample: `Kevin`",
    "4-0": "accountNumber",
    "4-1": "`string`",
    "4-2": "Beneficiary bank account number.  \n  \nExample: `1234567890123`",
    "5-0": "branchCode",
    "5-1": "`string`",
    "5-2": "Beneficiary branch IFSC.  \n  \nExample: `ICICI0000139`",
    "6-0": "vpa",
    "6-1": "`string`",
    "6-2": "Beneficiary VPA handle.  \n  \nExample: `kevin.bob@examplebank.com`",
    "7-0": "email",
    "7-1": "`string`",
    "7-2": "Beneficiary email address.  \n  \nExample: `kevin.bob@example.com`",
    "8-0": "phone",
    "8-1": "`string`",
    "8-2": "Beneficiary phone number.  \n  \nExample: `9876543210`",
    "9-0": "amount",
    "9-1": "`object`",
    "9-2": "An object that contains the payout amount details.",
    "10-0": "mode",
    "10-1": "`string`",
    "10-2": "Mode you wish to initiate a payout.  \n  \nAccepted values:<ul><li>`UPI`</li><li>`IMPS`</li><li>`NEFT`</li><li>`RTGS`</ul></li>",
    "11-0": "status",
    "11-1": "`string`",
    "11-2": "Payout status.  \n  \nExample: `PENDING`",
    "12-0": "message",
    "12-1": "`string`",
    "12-2": "Corresponding message to the status.  \n  \nExample: `Payment instruction pending to be executed`",
    "13-0": "scheduledAt",
    "13-1": "`string`",
    "13-2": "Use this parameter to schedule a payout for future. The time value is in UTC.  \n  \nExample: ",
    "14-0": "remarks",
    "14-1": "`string`",
    "14-2": "Payout remarks.  \n  \nExample: `Rent`",
    "15-0": "\\_links",
    "15-1": "`boolean`",
    "15-2": "An object that contains the payment link details."
  },
  "cols": 3,
  "rows": 16,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This object is part of the `scheduled account payout` sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`string`",
    "0-2": "Type of currency.  \n  \nExample: `INR`",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "The transaction amount is Paisa.  <ul><li>Minimum value: `100` (₹1).</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### \_Links [Child Object]

The table below lists the various parameters in the `links` child object. This object is part of the `scheduled account payout` sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "rel",
    "0-1": "`string`",
    "0-2": "Relationship to the resource.  \n  \nExample: `status`",
    "1-0": "href",
    "1-1": "`string`",
    "1-2": "Link to access the resource.  \n  \nExample: `http://pluralqa.pinepg.in:8000/payouts/v2/payments?paymentReferenceId=txn-a9304bb5bdd6444782466575afd023e4`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Update Scheduled Payout

Shown below is a sample response returned for a update scheduled payout API.

```json Update Scheduled Payout Sample Response
{
  "clientReferenceId": "test4feb0-10",
  "requestReferenceId": "req-7c85bda19bf141c981b94e750c6041b6",
  "paymentReferenceId": "txn-f9e00a80a357418d908a67bd30cdbc37",
  "payeeName": "Rishendrasai",
  "accountNumber": "919000664016",
  "branchCode": "PYTM0123456",
  "vpa": "",
  "email": "s.john@g.com",
  "phone": "9000664016",
  "amount": {
    "currency": "INR",
    "value": 100
  },
  "mode": "IMPS",
  "status": "SCHEDULED",
  "message": "Payment instruction pending to be executed",
  "scheduledAt": "",
  "remarks": "Test transaction",
  "_links": [
    {
      "rel": "status",
      "href": "http://pluralqa.pinepg.in:8000/payouts/v2/payments?paymentReferenceId=txn-f9e00a80a357418d908a67bd30cdbc37"
    }
  ]
}
```

The table below lists the various parameters returned in the update scheduled payout sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "clientReferenceId",
    "0-1": "`string`",
    "0-2": "Unique identifier entered while creating a Payout request.  \n  \nExample: `test1607-281915`",
    "1-0": "requestReferenceId",
    "1-1": "`string`",
    "1-2": "Unique identifier of the payout request in Plural database.  \n  \nExample:  `req-446b28bdd4e0444ab8cc381278c0a7db`",
    "2-0": "paymentReferenceId",
    "2-1": "`string`",
    "2-2": "Unique identifier of the payout reference in Plural database.  \n  \nExample: `txn-a9304bb5bdd6444782466575afd023e4`",
    "3-0": "payeeName",
    "3-1": "`string`",
    "3-2": "Beneficiary name.  \n  \nExample: `Kevin`",
    "4-0": "accountNumber",
    "4-1": "`string`",
    "4-2": "Beneficiary bank account number.  \n  \nExample: `1234567890123`",
    "5-0": "branchCode",
    "5-1": "`string`",
    "5-2": "Beneficiary branch IFSC.  \n  \nExample: `ICICI0000139`",
    "6-0": "vpa",
    "6-1": "`string`",
    "6-2": "Beneficiary VPA handle.  \n  \nExample: `kevin.bob@examplebank.com`",
    "7-0": "email",
    "7-1": "`string`",
    "7-2": "Beneficiary email address.  \n  \nExample: `kevin.bob@example.com`",
    "8-0": "phone",
    "8-1": "`string`",
    "8-2": "Beneficiary phone number.  \n  \nExample: `9876543210`",
    "9-0": "amount",
    "9-1": "`object`",
    "9-2": "An object that contains the payout amount details.",
    "10-0": "mode",
    "10-1": "`string`",
    "10-2": "Mode you wish to initiate a payout.  \n  \nAccepted values:<ul><li>`UPI`</li><li>`IMPS`</li><li>`NEFT`</li><li>`RTGS`</ul></li>",
    "11-0": "status",
    "11-1": "`string`",
    "11-2": "Payout status.  \n  \nExample: `PENDING`",
    "12-0": "message",
    "12-1": "`string`",
    "12-2": "Corresponding message to the status.  \n  \nExample: `Payment instruction pending to be executed`",
    "13-0": "scheduledAt",
    "13-1": "`string`",
    "13-2": "Use this parameter to schedule a payout for future. The time value is in UTC.  \n  \nExample: ",
    "14-0": "remarks",
    "14-1": "`string`",
    "14-2": "Payout remarks.  \n  \nExample: `Rent`",
    "15-0": "\\_links",
    "15-1": "`boolean`",
    "15-2": "An object that contains the payment link details."
  },
  "cols": 3,
  "rows": 16,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This object is part of the `update scheduled payout` sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`string`",
    "0-2": "Type of currency.  \n  \nExample: `INR`",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "The transaction amount is Paisa.  <ul><li>Minimum value: `100` (₹1).</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### \_Links [Child Object]

The table below lists the various parameters in the `links` child object. This object is part of the `update scheduled payout` sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "rel",
    "0-1": "`string`",
    "0-2": "Relationship to the resource.  \n  \nExample: `status`",
    "1-0": "href",
    "1-1": "`string`",
    "1-2": "Link to access the resource.  \n  \nExample: `http://pluralqa.pinepg.in:8000/payouts/v2/payments?paymentReferenceId=txn-a9304bb5bdd6444782466575afd023e4`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Cancel Scheduled Payout

Shown below is a sample response returned for a cancel scheduled payout API.

```json Cancel Schedule Payout
{
  "clientReferenceId": "test4feb0-10",
  "requestReferenceId": "req-7c85bda19bf141c981b94e750c6041b6",
  "paymentReferenceId": "txn-f9e00a80a357418d908a67bd30cdbc37",
  "payeeName": "Rishendrasai",
  "accountNumber": "919000664016",
  "branchCode": "PYTM0123456",
  "vpa": "",
  "email": "s.john@g.com",
  "phone": "9000664016",
  "amount": {
    "currency": "INR",
    "value": 100
  },
  "mode": "IMPS",
  "status": "CANCELLED",
  "message": "Payment instruction pending to be executed",
  "scheduledAt": "",
  "remarks": "Test transaction",
  "_links": [
    {
      "rel": "status",
      "href": "http://pluralqa.pinepg.in:8000/payouts/v2/payments?paymentReferenceId=txn-f9e00a80a357418d908a67bd30cdbc37"
    }
  ]
}
```

The table below lists the various parameters returned in the cancel scheduled payout sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "clientReferenceId",
    "0-1": "`string`",
    "0-2": "Unique identifier entered while creating a Payout request.  \n  \nExample: `test1607-281915`",
    "1-0": "requestReferenceId",
    "1-1": "`string`",
    "1-2": "Unique identifier of the payout request in Plural database.  \n  \nExample:  `req-446b28bdd4e0444ab8cc381278c0a7db`",
    "2-0": "paymentReferenceId",
    "2-1": "`string`",
    "2-2": "Unique identifier of the payout reference in Plural database.  \n  \nExample: `txn-a9304bb5bdd6444782466575afd023e4`",
    "3-0": "payeeName",
    "3-1": "`string`",
    "3-2": "Beneficiary name.  \n  \nExample: `Kevin`",
    "4-0": "accountNumber",
    "4-1": "`string`",
    "4-2": "Beneficiary bank account number.  \n  \nExample: `1234567890123`",
    "5-0": "branchCode",
    "5-1": "`string`",
    "5-2": "Beneficiary branch IFSC.  \n  \nExample: `ICICI0000139`",
    "6-0": "vpa",
    "6-1": "`string`",
    "6-2": "Beneficiary VPA handle.  \n  \nExample: `kevin.bob@examplebank.com`",
    "7-0": "email",
    "7-1": "`string`",
    "7-2": "Beneficiary email address.  \n  \nExample: `kevin.bob@example.com`",
    "8-0": "phone",
    "8-1": "`string`",
    "8-2": "Beneficiary phone number.  \n  \nExample: `9876543210`",
    "9-0": "amount",
    "9-1": "`object`",
    "9-2": "An object that contains the payout amount details.",
    "10-0": "mode",
    "10-1": "`string`",
    "10-2": "Mode you wish to initiate a payout.  \n  \nAccepted values:<ul><li>`UPI`</li><li>`IMPS`</li><li>`NEFT`</li><li>`RTGS`</ul></li>",
    "11-0": "status",
    "11-1": "`string`",
    "11-2": "Payout status.  \n  \nExample: `PENDING`",
    "12-0": "message",
    "12-1": "`string`",
    "12-2": "Corresponding message to the status.  \n  \nExample: `Payment instruction pending to be executed`",
    "13-0": "scheduledAt",
    "13-1": "`string`",
    "13-2": "Use this parameter to schedule a payout for future. The time value is in UTC.  \n  \nExample: ",
    "14-0": "remarks",
    "14-1": "`string`",
    "14-2": "Payout remarks.  \n  \nExample: `Rent`",
    "15-0": "\\_links",
    "15-1": "`boolean`",
    "15-2": "An object that contains the payment link details."
  },
  "cols": 3,
  "rows": 16,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This object is part of the `cancel scheduled payout` sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`string`",
    "0-2": "Type of currency.  \n  \nExample: `INR`",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "The transaction amount is Paisa.  <ul><li>Minimum value: `100` (₹1).</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### \_Links [Child Object]

The table below lists the various parameters in the `links` child object. This object is part of the `cancel scheduled payout` sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "rel",
    "0-1": "`string`",
    "0-2": "Relationship to the resource.  \n  \nExample: `status`",
    "1-0": "href",
    "1-1": "`string`",
    "1-2": "Link to access the resource.  \n  \nExample: `http://pluralqa.pinepg.in:8000/payouts/v2/payments?paymentReferenceId=txn-a9304bb5bdd6444782466575afd023e4`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]
