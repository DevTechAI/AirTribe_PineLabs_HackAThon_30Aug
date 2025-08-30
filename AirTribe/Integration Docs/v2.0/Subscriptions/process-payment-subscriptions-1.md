---
title: "Process Payment - Subscriptions"
slug: "process-payment-subscriptions-1"
excerpt: "This page will help you get started with Process Payment - Subscriptions."
hidden: true
createdAt: "Wed Jul 05 2023 06:28:28 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:55:16 GMT+0000 (Coordinated Universal Time)"
---
Use the below endpoint to Process Payment for Subscriptions

**Request Parameters:**

[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "params",
    "h-2": "Nested Params",
    "h-3": "Data Type",
    "h-4": "Description",
    "0-0": "merchantId\\*",
    "0-1": "",
    "0-2": "",
    "0-3": "string",
    "0-4": "Onboarded Merchant ID",
    "1-0": "clientUniqueReference\\*",
    "1-1": "",
    "1-2": "",
    "1-3": "string",
    "1-4": "unique reference number assigned to a merchant",
    "2-0": "enableNotification",
    "2-1": "",
    "2-2": "false/true",
    "2-3": "boolean",
    "2-4": "default false",
    "3-0": "plan\\*",
    "3-1": "{}",
    "3-2": "",
    "3-3": "",
    "3-4": "plan details",
    "4-0": "",
    "4-1": "planId",
    "4-2": "",
    "4-3": "string",
    "4-4": "required if its plural maintained plan",
    "5-0": "",
    "5-1": "merchantMaintainedPlan",
    "5-2": "",
    "5-3": "boolean",
    "5-4": "**false**: if its plural maintained plan **true**: if its merchant maintained plan",
    "6-0": "",
    "6-1": "merchantPlanId",
    "6-2": "",
    "6-3": "string",
    "6-4": "",
    "7-0": "",
    "7-1": "merchantId",
    "7-2": "",
    "7-3": "string",
    "7-4": "",
    "8-0": "",
    "8-1": "planName",
    "8-2": "",
    "8-3": "string",
    "8-4": "",
    "9-0": "",
    "9-1": "planDescription",
    "9-2": "",
    "9-3": "string",
    "9-4": "",
    "10-0": "",
    "10-1": "frequency",
    "10-2": "",
    "10-3": "string",
    "10-4": "",
    "11-0": "",
    "11-1": "frequencyType",
    "11-2": "",
    "11-3": "string",
    "11-4": "",
    "12-0": "",
    "12-1": "maxUsers",
    "12-2": "",
    "12-3": "string",
    "12-4": "",
    "13-0": "",
    "13-1": "notes",
    "13-2": "",
    "13-3": "string",
    "13-4": "",
    "14-0": "",
    "14-1": "amount",
    "14-2": "",
    "14-3": "",
    "14-4": "",
    "15-0": "",
    "15-1": "",
    "15-2": "value",
    "15-3": "integer",
    "15-4": "value given in numbers",
    "16-0": "",
    "16-1": "",
    "16-2": "currency",
    "16-3": "string",
    "16-4": "which currency used for transaction: INR",
    "17-0": "",
    "17-1": "maxLimitAmount",
    "17-2": "",
    "17-3": "",
    "17-4": "",
    "18-0": "",
    "18-1": "",
    "18-2": "value",
    "18-3": "integer",
    "18-4": "value given in numbers",
    "19-0": "",
    "19-1": "",
    "19-2": "currency",
    "19-3": "string",
    "19-4": "which currency used for transaction: INR",
    "20-0": "",
    "20-1": "trialPeriodInDays",
    "20-2": "",
    "20-3": "integer",
    "20-4": "",
    "21-0": "",
    "21-1": "startDate",
    "21-2": "string(UTC format date time example: 2023-02-06 18:30:00)",
    "21-3": "string",
    "21-4": "start date of the plan 2023-02-06 18:30:00",
    "22-0": "",
    "22-1": "endDate",
    "22-2": "string(UTC format date time example: 2023-02-06 18:30:00)",
    "22-3": "string",
    "22-4": "end date of the plan 2023-02-06 18:30:00",
    "23-0": "quantity\\*",
    "23-1": "",
    "23-2": "number of subscription needed  \ndefault is 1",
    "23-3": "integer",
    "23-4": "number of subscription needed",
    "24-0": "startDate\\*",
    "24-1": "startDate",
    "24-2": "string(UTC format example: 2023-02-06 18:30:00)",
    "24-3": "string",
    "24-4": "start date of subscription 2023-02-06 18:30:00",
    "25-0": "endDate\\*",
    "25-1": "endDate",
    "25-2": "string(UTC format date time example: 2023-02-06 18:30:00)",
    "25-3": "string",
    "25-4": "end date of subscription",
    "26-0": "customerData\\*",
    "26-1": "{}",
    "26-2": "",
    "26-3": "",
    "26-4": "",
    "27-0": "",
    "27-1": "firstName",
    "27-2": "",
    "27-3": "string",
    "27-4": "forst name of the customer",
    "28-0": "",
    "28-1": "lastName",
    "28-2": "",
    "28-3": "string",
    "28-4": "last name of the customer",
    "29-0": "",
    "29-1": "countryCode\\*",
    "29-2": "",
    "29-3": "string",
    "29-4": "for india its 91, phone country code",
    "30-0": "",
    "30-1": "customerMobile\\*",
    "30-2": "",
    "30-3": "string",
    "30-4": "customer mobile number to send any notification",
    "31-0": "",
    "31-1": "customerEmail\\*",
    "31-2": "",
    "31-3": "string",
    "31-4": "email to send any notification",
    "32-0": "autoDebit",
    "32-1": "",
    "32-2": "default true",
    "32-3": "boolean",
    "32-4": "whether auto-debit opted or not",
    "33-0": "upi_data\\*",
    "33-1": "{}",
    "33-2": "",
    "33-3": "",
    "33-4": "",
    "34-0": "",
    "34-1": "txnMode: \"C/I\"\"",
    "34-2": "",
    "34-3": "string",
    "34-4": "customer upi id **I:INTENT** vpa will not be needed                      **C: COLLECT** vpa will be needed",
    "35-0": "payments",
    "35-1": "{}",
    "35-2": "",
    "35-3": "",
    "35-4": "",
    "36-0": "",
    "36-1": "amountLimit",
    "36-2": "",
    "36-3": "string",
    "36-4": "",
    "37-0": "",
    "37-1": "debitDay",
    "37-2": "",
    "37-3": "integer",
    "37-4": "which day debit should happen, default:1",
    "38-0": "",
    "38-1": "debitRule",
    "38-2": "",
    "38-3": "string",
    "38-4": "default is ON",
    "39-0": "",
    "39-1": "blockFund",
    "39-2": "",
    "39-3": "string",
    "39-4": "should customer blocked for this customer.default: N",
    "40-0": "",
    "40-1": "",
    "40-2": "",
    "40-3": "",
    "40-4": ""
  },
  "cols": 5,
  "rows": 41,
  "align": [
    "left",
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


**Request Body payload:** 

```json JSON
{
	"merchantId": "3000004",
	"clientUniqueReference": "Merchant_Plan_001",
	"enableNotification": true,
	"plan": {
		"planId": "",
		"merchantMaintainedPlan": false,		
		"merchantPlanId": "merch007",
		"merchantId": "3004",
		"planName": "MPPlanDayNT",
		"planDescription": "Merchant Maintained Plan feb 06 ",
		"frequency": 1,
		"frequencyType": "Day",
		"maxUsers": "100",
		"notes": "Sample message",
		"amount": {
			"value": 220,
			"currency": "INR"
		},
		"maxLimitAmount": {
			"value": 220,
			"currency": "INR"
		},
		"trialPeriodInDays": 0,
		"startDate": "2023-02-06 18:30:00",
		"endDate": "2023-02-10 18:30:00"
	},
	"quantity": 1,
	"startDate": "2023-02-06 18:30:00",
	"endDate": "2023-02-10 18:30:00",
	"customerData": {
		"firstName": "Dhakshin",
		"lastName": "K",
		"countryCode": "91",
		"customerMobile": "9444600695",
		"customerEmail": "test@test.cm"
	},
	"autoDebit": true,
	"upi_data": {
		"vpa": "dhakshin@okaxis"
	},
	"payments": {
		"amountLimit": "M",
		"debitDay": 1,
		"debitRule": "ON",
		"blockFund": "N"
	}
}
```

**Response Payload:** 

```json 200 Success
{
	"response_code": "1",
	"response_message": "Transaction initiated",
	"merchant_order_id": "3565203",
	"order_id": 3565203,
	"subscription_id": "130",
	"plan_id": "17"
}
```
```json 400 Bad Request
{
    "response_code": 12404,
    "response_message": "Create subscription failed"
}
```
```json 400 Bad Request
{    "response_code": 12408,  
     "response_message": "Invalid Upi Details"
}
```

**Response Parameters** 

| Parameter Name   | Type   | Description                                    |
| :--------------- | :----- | :--------------------------------------------- |
| response_code    | string | response code received                         |
| response_message | string | Short message about code.                      |
| subscription_id  | string | created subscription id on successful scenario |
| plan_id          | string | id captured while processing the payment       |
