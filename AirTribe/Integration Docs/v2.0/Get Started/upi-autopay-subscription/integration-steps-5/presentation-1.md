---
title: "Presentation"
slug: "presentation-1"
excerpt: ""
hidden: true
createdAt: "Tue Dec 10 2024 09:58:10 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Dec 11 2024 04:33:57 GMT+0000 (Coordinated Universal Time)"
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

## 1. Presentation API

The Presentation API enables you to schedule debits for **Mandate Subscriptions** with the frequency type set to `AS ` (As and when Presented). 

With the Presentation API, you gain greater flexibility and control, allowing you to schedule debits as per your convenience.

### 1.1 Schedule Presentation

Schedule Presentation API is used to schedule debits for As Presented Frequency Type Subscriptions.

Shown below are the Sample cURL Request and response for **Presentation API**.

```curl cURL Request for UAT
curl --location 'https://api-staging.pluralonline.com/api/v1/public/mandates/presentation' \

--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <<YOUR JWT TOKEN>>' \
--data '{
"subscriptionId": "97",
"collectByDate": "02/03/2024 03:29 PM",
"amount": {
"value": 11100,
"currency": "INR"
}
}' 
```
```curl cURL Request for PROD
curl --location 'https://api.pluralonline.com/api/v1/public/mandates/presentation' \

--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <<YOUR JWT TOKEN>>' \
--data '{
"subscriptionId": "97",
"collectByDate": "02/03/2024 03:29 PM",
"amount": {
"value": 11100,
"currency": "INR"
}
}' 
```
```json Sample Response
{
"subscriptionId": "36",
"presentationId": 94,
"collectByDate": "24/02/2024 06:30 PM",
"amount": {
"value": 11100,
"currency": "INR"
},
"message": "The debit is successfully scheduled at 24/02/2024 06:30 PM"
}
```

### 1.2 Cancel Presentation

Use this API to cancel a scheduled debit/presentation.

Shown below are the Sample cURL Request and response for **Cancel Presentation API**.

```curl cURL Request for UAT
curl --location 'https://api-staging.pluralonline.com/api/v1/public/mandates/cancelPresentation/<<PresentationID>>' \

--header 'Authorization: Bearer <<YOUR JWT TOKEN>>' \  
```
```curl cURL Request for PROD
curl --location 'https://api.pluralonline.com/api/v1/public/mandates/cancelPresentation/<<PresentationID>>' \

--header 'Authorization: Bearer <<YOUR JWT TOKEN>>' \  
```
```json Sample Response
{
"subscriptionId": "36",
"presentationId": "42",
"presentationStatus": "CANCELLED",
"message": "Presentation 42 is cancelled successfully"
}
```

### 1.3 Get Presentation by Id

Use this API to get all the details of a particular presentation by Presentation Id.

Shown below are the Sample cURL Request and response for **Presentation by ID**.

```curl cURL Request for UAT
curl --location 'https://api-staging.pluralonline.com/api/v1/public/mandates/presentation/<<PresentationId>>' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <<YOUR JWT TOKEN>>' \
```
```curl cURL Request for PROD
curl --location 'https://api.pluralonline.com/api/v1/public/mandates/presentation/<<PresentationId>>' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <<YOUR JWT TOKEN>>' \
```
```json Sample Response
{
"subscriptionId": 36,
"presentation": {
"presentationId": 94,
"presentationStatus": "DEBIT_SCHEDULED",
"debitAmount": {
"value": 11100.0,
"currency": "INR"
},
"debitDate": "24/02/2024 06:30 PM",
"preDebitNotificationStatus": "Success",
"preDebitNotificationInitiatedOn": "23/02/2024 12:13 PM",
"isExpired": false,
"responseMessage": "TRANSACTION INITIATED"
}
} 
```

### 1.4 Get All Presentations

Use this API to get details of all presentations scheduled for a merchant.

Shown below are the Sample cURL Request and response for **Get Presentations**

```curl cURL Request for UAT
curl --location 'https://api-staging.pluralonline.com/api/v1/public/mandates/getPresentations' \

--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <<YOUR JWT TOKEN>>' \
--data '{
"subscriptionId": 10,
"presentationId": 10,
"presentationStatus": "DEBIT_SCHEDULED",
"amount": 10000,
"amountRange": "isEqual",
"fromDate": "2024-03-01",
"toDate": "2024-04-01",
"size": 10,
"page": 1,
"sort": "amount,asc"
}' 
```
```curl cURL Request for PROD
curl --location 'https://api.pluralonline.com/api/v1/public/mandates/getPresentations' \

--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <<YOUR JWT TOKEN>>' \
--data '{
"subscriptionId": 10,
"presentationId": 10,
"presentationStatus": "DEBIT_SCHEDULED",
"amount": 10000,
"amountRange": "isEqual",
"fromDate": "2024-03-01",
"toDate": "2024-04-01",
"size": 10,
"page": 1,
"sort": "amount,asc"
}' 
```
```json Sample Response
{
"links": {
"first": {
"href": "http://localhost:8183/api/v1/public/mandates/getPresentations?page=0&size=5&sort=isExpired,desc"
},
"self": {
"href": "http://localhost:8183/api/v1/public/mandates/getPresentations?page=0&size=5&sort=isExpired,desc"
},
"next": {
"href": "http://localhost:8183/api/v1/public/mandates/getPresentations?page=1&size=5&sort=isExpired,desc"
},
"last": {
"href": "http://localhost:8183/api/v1/public/mandates/getPresentations?page=4&size=5&sort=isExpired,desc"
}
},
"page": {
"size": 5,
"totalElements": 25,
"totalPages": 5,
"number": 0
},
"presentations": [
{
"presentationId": 23,
"presentationStatus": "DEBIT_INITIATED",
"subscriptionId": 36,
"subscriptionStatus": "Active",
"debitAmount": {
"value": 11100.0,
"currency": "INR"
},
"debitDate": "20/02/2024 06:30 pm",
"preDebitNotificationStatus": "Success",
"debitStatus": "Success",
"debitInitiatedOn": "20/02/2024 06:30 pm",
"preDebitNotificationInitiatedOn": "19/02/2024 02:54 pm",
"isExpired": true,
"responseMessage": "TRANSACTION INITIATED"
},
{
"presentationId": 24,
"presentationStatus": "DEBIT_SCHEDULED",
"subscriptionId": 36,
"subscriptionStatus": "Active",
"debitAmount": {
"value": 11100.0,
"currency": "INR"
},
"debitDate": "20/02/2024 07:30 pm",
"preDebitNotificationStatus": "Success",
"preDebitNotificationInitiatedOn": "19/02/2024 02:55 pm",
"isExpired": true
"responseMessage": "TRANSACTION INITIATED"
}
]
}
```

## 2. Retry API

The Retry API allows you to reattempt executing mandates when initial executions fail due to insufficient funds or other errors. It ensures flexibility in retrying debits, empowering you to address issues arising from execution failures effectively. This API is applicable for all mandate frequency types, both fixed and variable, except for one-time (OT) mandates.

You can utilize the Retry API to perform up to three external retries before the next scheduled execution, providing you greater control over resolving execution failures. This feature is exclusively available for merchants onboarded with Plural.

> 📘 Note:
> 
> 1. **Internal Retry Mechanism**:
> 
> - After an execution failure, the system automatically performs two internal retries to execute the mandate.
> - If the time difference between the current time and the next scheduled mandate execution is within 2 hours, retries occur at 1-minute intervals.
> - If the time difference exceeds 2 hours, the first retry occurs 10 minutes after the failure, and the second retry follows 50 minutes later.
> 
> 2. **External Retries**:
>    - You can perform up to 3 external retries before the next scheduled execute mandate.
>    - This allows greater control over managing failed transactions effectively.

> 🚧 Watch Out:
> 
> 1. **One-Time (OT) Mandates**:  
>    The Retry API does not support mandates with a one-time frequency. Ensure your use case aligns with supported frequency types.
> 2. **Bank and Merchant Errors**:  
>    Use the Retry API to mitigate errors caused by insufficient funds, bank issues, or merchant-side challenges. However, repeated failures may require further investigation of the root cause.

Shown below are the Sample cURL Request and response for **Retry API**.

```curl cURL Request for UAT
curl --location 'https://api-staging.pluralonline.com/api/v1/public/mandates/retry' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <<YOUR JWT TOKEN>>' \ 
--data '{
"subscriptionId":"202"
}'  
```
```curl cURL Request for PROD
curl --location 'https://api.pluralonline.com/api/v1/public/mandates/retry' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <<YOUR JWT TOKEN>>' \ 
--data '{
"subscriptionId":"202"
}' 
```
```json Sample Response
{

    "debitRetryCountLeft": 2,

    "debitResponse": {

        "response": "5009",

        "terminalId": "5818",

        "merchantId": 120054,

        "subMerchantId": 414077,

        "bankRRN": 269693266898,

        "merchantTransactionId": "7856699",

        "amount": 16000,

        "success": "Failed",

        "message": "Service unavailable. Please try later.",

        "subscriptionId": "202"

    }
 }  
```

## 3. Resume API

Use the Resume API to reactivate a subscription that has been `paused` or` halted` by the merchant. This ensures that the subscription returns to its active state and continues seamlessly.

Shown below are the Sample cURL Request and response for **Resume API**.

```curl cURL Request for UAT
curl --location 'https://api-staging.pluralonline.com/api/v1/public/subscriptions/resume' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <<JWT_TOKEN>>' \
--data '{"subscriptionId":"79"}' 
```
```curl cURL Request for PROD
curl --location 'https://api.pluralonline.com/api/v1/public/subscriptions/resume' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <<JWT_TOKEN>>' \
--data '{"subscriptionId":"79"}' 
```
```json Sample Response
{
 "subscriptionId":"79",
 "message":"Subscription has been resumed successfully."
}
```

## Handle Payments

To know the status of the payment you can use the below options.

1. **<a href="<https://developer.pluralonline.com/v2.0/reference/payment-inquiry-refund" target="_blank">Inquiry API</a>**: Use this API to check transaction statuses.
2. **<a href="https://developer.pluralonline.com/v2.0/docs/developer-tools-webhook" target="_blank">Webhook Notification</a>**: We send Webhook notifications on the successful payment or any changes to the payments response object.
