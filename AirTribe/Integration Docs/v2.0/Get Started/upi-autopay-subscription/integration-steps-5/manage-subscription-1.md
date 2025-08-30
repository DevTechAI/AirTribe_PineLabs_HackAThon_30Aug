---
title: "Manage Subscription"
slug: "manage-subscription-1"
excerpt: "Learn how to manage Subscriptions by using Plural APIs."
hidden: true
createdAt: "Tue Dec 10 2024 09:57:56 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Dec 11 2024 04:54:21 GMT+0000 (Coordinated Universal Time)"
---
## Prerequisite

### JWT Authentication

You can generate the JWT token by following below steps:

**Step 1: Generating Private/Public Key for JWT Authentication**

1. **Generate RSA Key Pair: **
   - Generate a 2048-bit RSA private key and its corresponding public key.
   - Keep the private key secure; it will be used to generate JWT tokens.
   - Share the public key with the Subscriptions onboarding team.
2. After successfully onboarding to the Subscriptions product, the onboarding team will provide you with the following details:
   - **secretKey**: Used to encrypt data claims while creating the JWT token.
   - **mid**: Your unique merchant ID on the platform (also called Plural Merchant ID).
   - **iss**: The token issuer, representing your merchant's name.
   - **agr**: Indicates the source system where your mid is registered (e.g., "Plural").
   - **srv**: Represents the product platform (e.g., "Subscription" for Subscription APIs).
   - **userReferenceId**: A unique reference ID for your merchant.
   - **audience**: A constant value, "Plural."

Step 2: **Generating JWT Tokens**  
Once you have the required keys and details, follow these steps to generate a JWT token:

1. **Install SDKs: **  
   o	Use the SDKs provided by the onboarding team for JWT token generation and RSA key management.
2. **Create JWT Token: **
   - Use your private key to sign the token.
   - Include all necessary claims (`mid`, `iss`, `agr`, `srv`, `userReferenceId`, and `audience`) when creating the token.
   - Encrypt the claims using the provided secretKey.
3. **Set Token Expiration**:  
   The token is valid for 30 minutes from the time of creation.
4. **Authenticate API Calls**:  
   Include the generated JWT token in the Authorization header for all Subscription API requests.

## 1. Get Plan API

This section covers two key APIs: GetPlanById and GetAllPlans. These APIs help you manage and retrieve plan-related information effectively.

### 1.1 Get Plan By ID

The **GetPlanById API** is designed to retrieve details of a specific plan using its unique planId.

- Use this API to access all plans created by you.
- It ensures precise data retrieval by targeting individual plan IDs.

Shown below are the Sample cURL Request and response for Get Plan by Id.

```curl cURL Request for UAT
curl --location 'https://api-staging.pluralonline.com/api/v1/public/plans/<<planId>>' \
--header 'Authorization: Bearer <<JWT_TOKEN>>'
```
```curl cURL Request for PROD
curl --location 'https://api.pluralonline.com/api/v1/public/plans/<<planId>>' \
--header 'Authorization: Bearer <<JWT_TOKEN>>'
```
```json Sample Response
{
    "planId": "33",
    "status": "Active",
    "activeSubscriptionCount": 2,
    "createdOn": "2024-02-13T05:20:21.894Z",
    "merchantId": "215",
    "planName": "temp_plan_aank26",
    "planDescription": "dumaka",
    "notes": "",
    "frequency": 1,
    "frequencyType": "AS",
    "amount": {
        "value": 11100.0,
        "currency": "INR"
    },
    "maxLimitAmount": {
        "value": 123100.0,
        "currency": "INR"
    },
    "trialPeriodInDays": 0,
    "maxUsers": 90,
    "startDate": "2024-02-13T08:01:04.211Z",
    "endDate": "2025-02-13T08:01:04.211Z"
}
```

### 1.2 Get All Plans

The **GetAllPlans API** allows you to fetch a list of plans based on various filters.

- Include specific parameters in the API request to refine your search.
- This is useful for retrieving broader sets of plans according to your preferences or requirements. 

Shown below are the Sample cURL Request and response for **Get All Plan**.

```curl cURL Request for UAT
curl --location 'https://api-staging.pluralonline.com/api/v1/public/plans/getPlans' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <<JWT_TOKEN>>' \
--data '{
  "fromDate": "2024-01-20",
  "toDate": "2024-03-21",
  "page": 1,
  "size": 10,

  "sort":"Id,asc"

}'
```
```curl cURL Request for PROD
curl --location 'https://api.pluralonline.com/api/v1/public/plans/getPlans' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <<JWT_TOKEN>>' \
--data '{
  "fromDate": "2024-01-20",
  "toDate": "2024-03-21",
  "page": 1,
  "size": 10,

  "sort":"Id,asc"

}'
```
```json Sample Response
"links": {
        "first": {
            "href": "<<URL>>/api/v1/public/plans/getPlans?page=0&size=2&sort=id,asc"
        },
        "self": {
            "href": "<<URL>>/api/v1/public/plans/getPlans?page=0&size=2&sort=id,asc"
        },
        "next": {
            "href": "<<URL>>/api/v1/public/plans/getPlans?page=1&size=2&sort=id,asc"
        },
        "last": {
            "href": "<<URL>>/api/v1/public/plans/getPlans?page=4&size=2&sort=id,asc"
        }
    },
    "page": {
        "size": 2,
        "totalElements": 10,
        "totalPages": 5,
        "number": 0
    },
    "plans": [
        {
            "planId": "46",
            "status": "Active",
            "activeSubscriptionCount": 0,
            "createdOn": "2024-03-03T11:37:25.451Z",
            "merchantId": "215",
            "planName": "aankitDay1",
            "planDescription": "Day Plan",
            "notes": "",
            "frequency": 1,
            "frequencyType": "Day",
            "amount": {
                "value": 15000.0,
                "currency": "INR"
            },
            "maxLimitAmount": {
                "value": 1000000.0,
                "currency": "INR"
            },
            "trialPeriodInDays": 0,
            "maxUsers": 5,
            "startDate": "2024-03-03T11:37:24.305Z",
            "endDate": "2024-04-03T11:37:24.305Z"
        },
        {
            "planId": "47",
            "status": "Active",
            "activeSubscriptionCount": 1,
            "createdOn": "2024-03-04T03:12:07.864Z",
            "merchantId": "215",
            "planName": "temp_plan_aank29",
            "planDescription": "dumaka",
            "notes": "",
            "frequency": 1,
            "frequencyType": "AS",
            "amount": {
                "value": 20000.0,
                "currency": "INR"
            },
            "maxLimitAmount": {
                "value": 123100.0,
                "currency": "INR"
            },
            "trialPeriodInDays": 0,
            "maxUsers": 90,
            "startDate": "2024-03-04T08:01:04.211Z",
            "endDate": "2025-03-04T08:01:04.211Z"
        }
    ]
}
```

## 2. Get Subscriptions API

Subscriptions are mandates created for every plan and there are 3 APIs available to get details of subscriptions.

### 2.1 Get All Subscriptions

Use this API to get details of all subscriptions available for you.

Shown below are the Sample cURL Request and response for **Get Subscriptions**.

```curl cURL Request for UAT
curl --location 'https://api-staging.pluralonline.com/api/v1/public/subscriptions/getSubscriptions' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <<YOUR JWT TOKEN>>' \
--data '{
   "fromDate": "2024-03-20",
  "toDate": "2024-03-21",
  "size": 5,
  "page": 1,
  "sort": "amount,asc"
}'
```
```curl cURL Request for PROD
curl --location 'https://api.pluralonline.com/api/v1/public/subscriptions/getSubscriptions' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <<YOUR JWT TOKEN>>' \
--data '{
   "fromDate": "2024-03-20",
  "toDate": "2024-03-21",
  "size": 5,
  "page": 1,
  "sort": "amount,asc"
}'
```
```json Sample Response
{
    "links": {
        "first": {
            "href": "http://pluralqa.pinepg.in:8000/api/v1/public/subscriptions/getSubscriptions?page=0&size=1&sort=amount,asc"
        },
        "self": {
            "href": "http://pluralqa.pinepg.in:8000/api/v1/public/subscriptions/getSubscriptions?page=0&size=1&sort=amount,asc"
        },
        "next": {
            "href": "http://pluralqa.pinepg.in:8000/api/v1/public/subscriptions/getSubscriptions?page=1&size=1&sort=amount,asc"
        },
        "last": {
            "href": "http://pluralqa.pinepg.in:8000/api/v1/public/subscriptions/getSubscriptions?page=9&size=1&sort=amount,asc"
        }
    },
    "page": {
        "size": 1,
        "totalElements": 10,
        "totalPages": 10,
        "number": 0
    },
    "subscriptions": [
        {
            "merchantId": 271,
            "createMandate": {
                "pluralTransactionId": "7278",
                "merchantTransactionId": "M24O02L26D05501",
                "status": "CREATE-SUCCESS",
                "message": "Transaction Initiated",
                "amount": "10000.0",
                "bankRRN": "405700963278"
            },
            "transactions": [
                {
                    "pluralTransactionId": "2451335",
                    "merchantTransactionId": "7853458",
                    "status": "SUCCESS",
                    "message": "Transaction Initiated",
                    "amount": "10000.0",
                    "bankRRN": "405700379058"
                },
                {
                    "merchantTransactionId": "M24X02M28G11410",
                    "message": "Transaction Successful",
                    "amount": "10000.0",
                    "bankRRN": "405900966563"
                },
                {
                    "merchantTransactionId": "M24I02S28Z11756",
                    "message": "Transaction Successful",
                    "amount": "10000.0",
                    "bankRRN": "405900966570"
                },
                {
                    "merchantTransactionId": "M24B02A28P11663",
                    "message": "Transaction Successful",
                    "amount": "10000.0",
                    "bankRRN": "405900966574"
                },
                {
                    "merchantTransactionId": "M24P02Z28Q11741",
                    "message": "Transaction Successful",
                    "amount": "10000.0",
                    "bankRRN": "405900966578"
                },
                {
                    "merchantTransactionId": "M24H02D28W1153",
                    "message": "Transaction Successful",
                    "amount": "10000.0",
                    "bankRRN": "405900966582"
                },
                {
                    "merchantTransactionId": "M24Y02O28E11747",
                    "message": "Transaction Successful",
                    "amount": "10000.0",
                    "bankRRN": "405900966586"
                },
                {
                    "merchantTransactionId": "M24F02J28J11648",
                    "message": "Transaction Successful",
                    "amount": "10000.0",
                    "bankRRN": "405900966590"
                },
                {
                    "pluralTransactionId": "2464526",
                    "merchantTransactionId": "7854052",
                    "message": "Invalid Sequence Number",
                    "amount": "10000.0",
                    "bankRRN": "406000381952"
                }
            ],
            "subscriptionId": "84",
            "merchantMaintainedPlan": false,
            "clientUniqueReference": "niyati_122",
            "enableNotification": false,
            "quantity": 1,
            "subscriptionStartDate": "2024-02-26T11:00:00Z",
            "subscriptionEndDate": "2024-03-27T12:00:00Z",
            "customerData": {
                "firstName": "ryan2",
                "lastName": "robert",
                "countryCode": "91",
                "customerMobile": "8761234789",
                "customerEmail": "test2@test.com"
            },
            "autoDebit": true,
            "paymentMode": "UPI",
            "integrationMode": "SEAMLESS",
            "paymentGateway": {
                "accessCode": "4d8648d3-476d-408b-a00d-32066335f89c",
                "mId": "120054",
                "secretCode": "425BC2AA96CA441194CA607E9C7455E8",
                "name": "EDGE"
            },
            "planStartDate": "2024-02-23T08:01:04.211Z",
            "planEndDate": "2024-12-14T08:01:04.211Z",
            "planFrequency": 1,
            "planFrequencyType": "AS",
            "billDate": "2024-02-26",
            "trialEndDate": "2024-02-26T11:00:00Z",
            "createdOn": "2024-02-26T05:06:59.328504Z",
            "amount": {
                "value": 10000.0,
                "currency": "INR"
            },
            "plan": {
                "planName": "temp_plan_23FEB01",
                "planDescription": "23FEB01",
                "maxUsers": "90",
                "notes": "",
                "maxLimitAmount": {
                    "value": 50000.0,
                    "currency": "INR"
                },
                "amount": {
                    "value": 10000.0,
                    "currency": "INR"
                },
                "trialPeriodInDays": 0
            },
            "status": "Active"
        }
    ]
}
```

### 2.2 Get Subscription By ID

Use this API to get all the details of a particular subscription by Subscription Id.

Shown below are the Sample cURL Request and response for **Get Subscriptions by Id**.

```curl cURL Request for UAT
curl --location 'https://api-staging.pluralonline.com/api/v1/public/subscriptions/<<ID>>' \
--header 'Authorization: Bearer Bearer <<YOUR JWT TOKEN>>' \
```
```curl cURL Request for PROD
curl --location 'https://api.pluralonline.com/api/v1/public/subscriptions/<<ID>>' \
--header 'Authorization: Bearer Bearer <<YOUR JWT TOKEN>>' \
```
```json Sample Response
{
  "merchantId": 271,
  "createMandate": {
    "pluralTransactionId": "7412",
    "merchantTransactionId": "M24C03S04G07552",
    "status": "CREATE-SUCCESS",
    "message": "Transaction Initiated",
    "amount": "10000.0",
    "bankRRN": "406400970708"
  },
  "transactions": [
    {
      "merchantTransactionId": "M24X03Y04O09527",
      "message": "Transaction Successful",
      "amount": "10000.0",
      "bankRRN": "406400970890"
    },
    {
      "pluralTransactionId": "2475025",
      "merchantTransactionId": "7854419",
      "status": "SUCCESS",
      "message": "Transaction Initiated",
      "amount": "10000.0",
      "bankRRN": "406400383485"
    },
    {
      "merchantTransactionId": "M24B03Q04J09665",
      "message": "Transaction Initiated",
      "amount": "10000.0",
      "bankRRN": "406400970886"
    },
    {
      "merchantTransactionId": "M24P03U04P09219",
      "message": "Transaction Initiated",
      "amount": "10000.0",
      "bankRRN": "406400970887"
    },
    {
      "merchantTransactionId": "M24V03I04A09360",
      "message": "Transaction Initiated",
      "amount": "10000.0",
      "bankRRN": "406400970888"
    },
    {
      "pluralTransactionId": "2478093",
      "merchantTransactionId": "7854547",
      "status": "EXECUTE-FAILURE",
      "message": "Transaction Initiated",
      "amount": "10000.0",
      "bankRRN": "406500384329"
    },
    {
      "pluralTransactionId": "2478192",
      "merchantTransactionId": "7854549",
      "status": "EXECUTE-FAILURE",
      "message": "Transaction Initiated",
      "amount": "10000.0",
      "bankRRN": "406500384340"
    },
    {
      "pluralTransactionId": "2478476",
      "merchantTransactionId": "7854556",
      "status": "SUCCESS",
      "message": "Transaction Initiated",
      "amount": "10000.0",
      "bankRRN": "406500384500"
    },
    {
      "pluralTransactionId": "2478478",
      "merchantTransactionId": "7854562",
      "status": "SUCCESS",
      "message": "Transaction Initiated",
      "amount": "10000.0",
      "bankRRN": "406500384557"
    },
    {
      "pluralTransactionId": "2479276",
      "merchantTransactionId": "7854597",
      "status": "SUCCESS",
      "message": "Transaction Initiated",
      "amount": "10000.0",
      "bankRRN": "406500384647"
    },
    {
      "amount": "10000.0"
    }
  ],
  "subscriptionId": "127",
  "merchantMaintainedPlan": false,
  "clientUniqueReference": "niyati_147",
  "enableNotification": false,
  "quantity": 1,
  "subscriptionStartDate": "2024-03-04T11:00:00Z",
  "subscriptionEndDate": "2024-03-27T12:00:00Z",
  "customerData": {
    "firstName": "ryan2",
    "lastName": "robert",
    "countryCode": "91",
    "customerMobile": "8761234789",
    "customerEmail": "test2@test.com"
  },
  "autoDebit": true,
  "paymentMode": "UPI",
  "integrationMode": "SEAMLESS",
  "paymentGateway": {
    "accessCode": "4d8648d3-476d-408b-a00d-32066335f89c",
    "mId": "120054",
    "secretCode": "425BC2AA96CA441194CA607E9C7455E8",
    "name": "EDGE"
  },
  "planStartDate": "2024-02-23T08:01:04.211Z",
  "planEndDate": "2024-12-14T08:01:04.211Z",
  "planFrequency": 1,
  "planFrequencyType": "AS",
  "billDate": "2024-03-04",
  "trialEndDate": "2024-03-04T11:00:00Z",
  "createdOn": "2024-03-04T07:55:11.8496Z",
  "amount": {
    "value": 10000,
    "currency": "INR"
  },
  "plan": {
    "planName": "temp_plan_23FEB01",
    "planDescription": "23FEB01",
    "maxUsers": "90",
    "notes": "",
    "maxLimitAmount": {
      "value": 50000,
      "currency": "INR"
    },
    "amount": {
      "value": 10000,
      "currency": "INR"
    },
    "trialPeriodInDays": 0
  },
  "status": "Active"
}


```

### 2.3 Get All Transaction

Use this API to get all the details of a transactions for a subscription available for you.

Shown below are the Sample cURL Request and response for **Get All Transaction**.

```curl cURL Request for UAT
curl --location 'https://api-staging.pluralonline.com/api/v1/public/subscriptions/getTransactions' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <<YOUR JWT TOKEN>>' \
 --data '
{
"subscriptionId": 234,
"requestType":"C",
"fromDate": "2024-03-16",
"toDate": "2024-03-19",
"size": 10,
"page": 1,
"sort": "amount,asc"
}'
```
```curl cURL Request for PROD
curl --location 'https://api.pluralonline.com/api/v1/public/subscriptions/getTransactions' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <<YOUR JWT TOKEN>>' \
 --data '
{
"subscriptionId": 234,
"requestType":"C",
"fromDate": "2024-03-16",
"toDate": "2024-03-19",
"size": 10,
"page": 1,
"sort": "amount,asc"
}'
```
```json Sample Response
{
    "links": {
        "self": {
            "href": "<<URL>>/api/v1/public/subscriptions/getTransactions?page=0&size=1&sort=amount,asc"
        }
    },
    "page": {
        "size": 1,
        "totalElements": 1,
        "totalPages": 1,
        "number": 0
    },
    "transactionsBySubscription": [
        {
            "upiTransactionId": "371",
            "status": "CREATE-SUCCESS",
            "merchantTransactionId": "M24C03S04G07552",
            "umn": "547ae978a54e4e859b74aa20d810348a@icici",
            "requestType": "C",
            "lastUpdated": "2024-03-04 13:25:09.0"
        }
    ]
}
```
