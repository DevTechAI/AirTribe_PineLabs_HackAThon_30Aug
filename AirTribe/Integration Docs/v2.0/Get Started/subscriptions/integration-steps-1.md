---
title: "Integration Steps"
slug: "integration-steps-1"
excerpt: "Learn how to integrate and create Subscriptions by using Plural APIs."
hidden: true
createdAt: "Mon Nov 25 2024 09:44:17 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Dec 10 2024 06:52:17 GMT+0000 (Coordinated Universal Time)"
---
Integrating the Subscriptions product into your system enables seamless management of recurring payments and subscription-based services. This guide provides a step-by-step approach to help you integrate and utilize the Subscription APIs effectively.

## Prerequisite

### 1. X-Verify Token Authentication

You can generate the X-Verify token by following below steps:

1. Once you are successfully onboarded to Edge, you will be onboarded with ICICI through either the Edge MCUI portal or ICICI DMO (Direct Merchant Onboarding API).
2. Once registered with ICICI for UPI AutoPay, you will be onboarded on the Plural Dashboard.
3. From the Plural Dashboard, you can access your **Plural Merchant ID**, **Access Code**, and **Secret Key**.
4. You can follow the X-verify generation process from \<a herf="<https://developer.pluralonline.com/docs/hash-generation-logic"target="_blank">here></a>.

> 📘 Note:
> 
> 1. **X Verify Token**:  
>    Use only for the following APIs:
>    - Create Order ID API
>    - Process Payment API
> 2. **JWT Token**:  
>    Use for the following APIs:
>    - Get Plan API
>    - Get Subscription API
>    - Presentation API
>    - Retry API
>    - Resume API

## 1. Generate Token and order ID

Our Create Order API use Base64 Encode as an input request. And use HashMap to authorize the payment.

1. **Enter Payment Details**: Use the below JSON to enter the payment Details. You are required to enter the `merchant_data`, `payment_info_data`, `subscription_data` and `payment_category_type`.

```json JSON
{
    "merchant_data": {
        "merchant_id": "123456",
        "merchant_access_code": "417de6c4-7202-4748-8b8f-05106010137d",
        "merchant_return_url": "https://www.pinelabs.com",
        "merchant_order_id": "test_sim_501"
    },
    "payment_info_data": {
        "amount": 20000,
        "currency_code": "INR",
        "order_desc": "Test Order"
    },
        "subscription_data": {
        "plan_details": "{\"merchantId\":\"123456\",\"startDate\":\"2024-03-08T23:00:00Z\",\"endDate\":\"2024-03-15T15:00:00Z\",\"plan\":{\"planId\":\"37\"}}}"
    },
    "payment_category_type": "RECURRANCE"
}
```

> 📘 Note:
> 
> The amount field inside "**payment_info_data**" data object should be equal to the plan amount and if it is not equal, then the default value will be Plan Amount value.

### JSON Parameters

<details>

<summary>Click Here</summary>

The table below lists the various JSON parameters.

| Parameter             | Type     | Requirement Type | Description                                       |
| :-------------------- | :------- | :--------------- | :------------------------------------------------ |
| merchant_data         | `Object` | `M`              | An object that contains the merchant details.     |
| payment_info_data     | `Object` | `M`              | An object that contains the payment details.      |
| subscription_data     | `Object` | `M`              | An object that contains subscription related data |
| payment_category_type | `string` | `M`              | Fixed value for subscription "RECURRANCE"         |

#### Merchant Data [Child Object]

The table below lists the various parameters in the `merchant_data` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "merchant_id",
    "0-1": "`integer`",
    "0-2": "`M`",
    "0-3": "Unique identifier of the merchant in the Plural database.  \n  \nExample: `123456`",
    "1-0": "merchant_access_code",
    "1-1": "`string`",
    "1-2": "`M`",
    "1-3": "Unique merchant access code provided by Plural.  \n  \nExample: `4a8c422e-928d-4f84-bfe8-27a09af66647`",
    "2-0": "merchant_return_url",
    "2-1": "`string`",
    "2-2": "`M`",
    "2-3": "Merchant return URL.  \n  \nExample: `https://www.pinelabs.com`  \n  \n**Note**: Your customer's are redirected to this page after a successful payment.",
    "3-0": "unique_order_id",
    "3-1": "`string`",
    "3-2": "`M`",
    "3-3": "Unique identifier of the specific transaction.  \n  \nExample: `xyz123`"
  },
  "cols": 4,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 Note:
> 
> - Contact our <a href="mailto:pgsupport@pinelabs.com" target="_blank">support team</a> to know your `merchant_id` and `merchant_access_code`. Additionally you are required to whitelist your `merchant_return_url` and get enabled with payment modes as required.

#### Payment Data [Child Object]

The table below lists the various parameters in the `payment_info_data` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "amount_in_paisa",
    "0-1": "`integer`",
    "0-2": "`M`",
    "0-3": "The transaction amount in paisa.  \n  \nExample: `800`",
    "1-0": "currency_code",
    "1-1": "`String`",
    "1-2": "`M`",
    "1-3": "Currency code in which in the payment is intended. The currency code for Indian rupee is 'INR'",
    "2-0": "order_desc",
    "2-1": "`String`",
    "2-2": "`M`",
    "2-3": "The description of the order."
  },
  "cols": 4,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Plan Details [Child Object]

The table below lists the various parameters in the `subscription_data` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "merchantId",
    "0-1": "`String`",
    "0-2": "`M`",
    "0-3": "Unique identifier of the merchant in the Plural database.  \n  \nExample: `123456`",
    "1-0": "startDate",
    "1-1": "`string`",
    "1-2": "`M`",
    "1-3": "Subscription start Date  \n  \n**Validations**:  \nUTC time format example: 2023-01-31T18:30:00Z  \n**Note**:  \nstartDate should not be past date and time.",
    "2-0": "endDate",
    "2-1": "`integer`",
    "2-2": "`M`",
    "2-3": "Subscription end Date  \n  \n**Validations**:  \n UTC time format example: 2023-02-15T18:30:00Z  \n**Note**:  \nendDate should be greater than the start date."
  },
  "cols": 4,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Plan Data [Child Object]

The table below lists the various parameters in the `Plan Object` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "planId",
    "0-1": "`string`",
    "0-2": "`C`",
    "0-3": "It is a planId  \n  \n**Note**:  \nRequired only for plural maintained  \nNot required in case of merchant-maintained plan  \n  \n**Validations**:  \nShould be a valid and active plan.",
    "1-0": "merchantPlanId",
    "1-1": "`string`",
    "1-2": "`C`",
    "1-3": "Required only for merchant-maintained plan  \n Not required in case of plural maintained plan  \n  \n**Validations**:  \nShould be a valid name without special characters.\\`",
    "2-0": "frequencyType",
    "2-1": "`string`",
    "2-2": "`C`",
    "2-3": "Required only for merchant-maintained plan  \nNot required in case of merchant  maintained plan  \n  \n**Validations**: Frequency type can only be pass as per Enum: Day, Week, Month, Year, AS(As Presented), OT(One Time)  \nAS signifies that once the mandate is approved, merchants have the ability to schedule debits as and when presented utilizing the presentation APIs.  \n  \nOT indicates that one-time customers will incur charges only on a single occasion.",
    "3-0": "amount",
    "3-1": "`Object`",
    "3-2": "`O`",
    "3-3": "It is a composite object with below attributes.  \n  \nAmount in lowest denomination of respective currency. For INR it is amount in paise.  \n**Note:**  \nRequired only for merchant-maintained plan  \nNot required in case of merchant-maintained plan"
  },
  "cols": 4,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Amount Data [Child Object]

The table below lists the various parameters in the `Amount` child object. 

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "currency",
    "0-1": "`string`",
    "0-2": "`M`",
    "0-3": "Currency code in ISO format  \n  \nValidations:  \nShould be \"INR\"",
    "1-0": "value",
    "1-1": "`Number`",
    "1-2": "`M`",
    "1-3": "Amount in lowest denomination of respective currency. For INR it is amount in paise."
  },
  "cols": 4,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


</details>

2. **Encode JSON**: Convert the updated JSON to a Base64 Encode. Use the below sample code to handle the conversion of the JSON to a Base64 Encode.

```java Java
import java.util.Base64;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.stream.Collectors;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

public class SignatureGenerator {
  private static Map < String, Object > clean(Map < String, Object > arr) {
    return arr.entrySet().stream()
      .filter(entry -> entry.getValue() != null && !entry.getValue().toString().isEmpty())
      .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
  }
  public static void main(String[] args) {
    Map < String, Object > requestBody = new LinkedHashMap < > ();
    Map < String, Object > merchant_data = new LinkedHashMap < > ();
    merchant_data.put("merchant_id", "merchant_id");
    merchant_data.put("merchant_access_code", "merchant_access_code");
    merchant_data.put("merchant_return_url", "whitelisted_merchant_return_url");
    merchant_data.put("merchant_order_id", "merchant_order_id");
    requestBody.put("merchant_data", merchant_data);

    Map < String, Object > paymentDataObject = new LinkedHashMap < > ();
    paymentDataObject.put("amount_in_paisa", 100);
    requestBody.put("payment_data", paymentDataObject);
    Map < String, Object > txnObject = new LinkedHashMap < > ();
    txnObject.put("navigation_mode", "2");
    txnObject.put("payment_mode", "1,3,4,19,10,11,14");
    txnObject.put("transaction_type", "1");
    requestBody.put("txn_data", txnObject);

    Map < String, Object > requestBodyCleaned = clean(requestBody);
    Map < String, Object > mapStatus = new HashMap < > ();
    mapStatus.put("result", requestBodyCleaned);
    Gson gson = new GsonBuilder().disableHtmlEscaping().create();
    String jsonString2 = gson.toJson(requestBodyCleaned);
    jsonString2 = jsonString2.replace("\\/", "/");

    // Encoding JSON string to base64
    String base64Encoded = Base64.getEncoder().encodeToString(jsonString2.getBytes());

    System.out.println(base64Encoded);
  }
}
```

3. **HashMap**: Generate HashMap using the Base64 Encode and the secret key. Use the below sample code to handle the generation of HashMap using SHA256.

```java Java
import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import javax.xml.bind.DatatypeConverter;

public class SignatureGenerator {

    public static String jsonHash(String request, String secret) throws NoSuchAlgorithmException, InvalidKeyException, IllegalStateException, UnsupportedEncodingException {
        SecretKeySpec secretKeySpec = new SecretKeySpec(DatatypeConverter.parseHexBinary(secret), "HmacSHA256");
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(secretKeySpec);
        byte[] hmacBytes = mac.doFinal(request.getBytes("UTF-8"));
        String ss = String.format("%02x", new BigInteger(1, hmacBytes));
        return bytesToHex(hmacBytes).toUpperCase();
    }
    private static String bytesToHex(byte[] bytes) {
        StringBuilder result = new StringBuilder();
        for (byte b : bytes) {
            result.append(String.format("%02X", b));
        }
        return result.toString();
    }

    public static void main(String[] args) throws UnsupportedEncodingException, NoSuchAlgorithmException, InvalidKeyException {
        String responseBody = "<Base64EncodedPayload>";
        String signingSecret = "<Secret>";

        String requestSignature = SignatureGenerator.jsonHash(responseBody,signingSecret);
        System.out.println(requestSignature);
    }
} 
```

4. **Create order API**

Use the generated hash in the header to send a request. This step creates an order Id and token which can be used to process this order.  
Shown below are the sample cURL request and sample response for a Create Order API.

```curl cURL Request for UAT
curl --location 'https://api-staging.pluralonline.com/api/v1/order/create' \
--header 'X-Verify: <<HASH_VALUE>>' \
--header 'Content-Type: application/json' \
--data '{
    "request":"Base64_encoded_string"
}'
```
```curl cURL Request for Prod
curl --location 'https://api.pluralonline.com/api/v1/order/create' \
--header 'X-Verify: <<HASH_VALUE>>' \
--header 'Content-Type: application/json' \
--data '{
    "request":"Base64_encoded_string"
}'
```
```json Sample Response
{
    "token": "pMvPyims9dNIPAVl%2FPqkQZLXKtftqHDbe9SdX6BzZWQ%3D",
    "plural_order_id": "123823"
}
```

## 2. Process Payment API

You can use process payment API to create the Subscriptions.

### Query Parameter

`Token`: You need to pass the token generated in the Create Order API as the query parameter.

Shown below are the Sample cURL Request and response for Plural Maintained Plan for Collect Flow.

```curl cURL Request for UAT
curl --location 'https://api-staging.pluralonline.com/api/v1/upi/subscription/process/payment?token=pMvPyims9dNIPAVl%2FPqkQZLXKtftqHDbe9SdX6BzZWQ%3D' \
--header 'Content-Type: application/json' \
--data-raw '{
    "merchantId": "123456",
    "clientUniqueReference": "aank_1010",
    "enableNotification": false,
    "plan": {
        "planId":"89"
    },
    "quantity": 1,
    "startDate": "2024-03-14 16:00:00",
    "endDate": "2024-04-18 15:00:00",
    "customerData": {
        "firstName": " ",
        "lastName": " ",
        "countryCode": "91",
        "customerMobile": "8761234789",
        "customerEmail": "test2@test.com"
    },
    "autoDebit": true,
    "upi_data": {
        "txnMode": "C",
        "vpa": "callback@icici"
    },
    "payments": {
        "amountLimit": "M",
        "debitDay": 0,
        "debitRule": "NA",
        "blockFund": "Y",
        "remark":"S",
        "revokable": "N"
    }
}'
```
```curl cURL Request for PROD
curl --location 'https://api.pluralonline.com/api/v1/upi/subscription/process/payment?token=pMvPyims9dNIPAVl%2FPqkQZLXKtftqHDbe9SdX6BzZWQ%3D' \
--header 'Content-Type: application/json' \
--data-raw '{
    "merchantId": "123456",
    "clientUniqueReference": "aank_1010",
    "enableNotification": false,
    "plan": {
        "planId":"89"
    },
    "quantity": 1,
    "startDate": "2024-03-14 16:00:00",
    "endDate": "2024-04-18 15:00:00",
    "customerData": {
        "firstName": " ",
        "lastName": " ",
        "countryCode": "91",
        "customerMobile": "8761234789",
        "customerEmail": "test2@test.com"
    },
    "autoDebit": true,
    "upi_data": {
        "txnMode": "C",
        "vpa": "callback@icici"
    },
    "payments": {
        "amountLimit": "M",
        "debitDay": 0,
        "debitRule": "NA",
        "blockFund": "Y",
        "remark":"S",
        "revokable": "N"
    }
}'
```
```json Sample Response
{
"response_code": "1",
"response_message": "Transaction Initiated",
"merchant_order_id": "aank_1011",
"order_id": 123982,
"subscription_id": "239",
"plan_id": "34"
}
```

Shown below are the Sample cURL Request and response for Plural Maintained Plan for Intent Flow.

```curl cURL Request for UAT
curl --location 'https://api-staging.pluralonline.com/api/v1/upi/subscription/process/payment?token=pMvPyims9dNIPAVl%2FPqkQZLXKtftqHDbe9SdX6BzZWQ%3D' \
--header 'Content-Type: application/json' \
--data-raw '{
    "merchantId": "123456",
    "clientUniqueReference": "simulator_test_11",
    "enableNotification": false,
    "plan": {
        "merchantMaintainedPlan": true,
        "startDate" : "2024-03-06 18:00:00",
        "endDate" : "2024-03-30 23:00:00",
        "merchantPlanId": "merchant plan A",
        "planName": "merchant plan for daily frequency",
        "frequencyType": "AS",
        "frequency":"5",
        "planDescription": "A customer will be charged every Day with this plan",
        "amount": {"value":250,"currency":"INR"},
        "maxLimitAmount": {"value":2500.0,"currency":"INR"}
    },
    "quantity": 1,
    "startDate": "2024-03-06 18:00:00",
    "endDate": "2024-03-30 23:00:00",
    "customerData": {
        "firstName": " ",
        "lastName": " ",
        "countryCode": "91",
        "customerMobile": "8761234789",
        "customerEmail": "test2@test.com"
    },
    "autoDebit": true,
    "upi_data": {
        "txnMode": "C",
        "vpa": "callback@icici"
    },
    "payments": {
        "amountLimit": "M",
        "debitDay": 0,
        "debitRule": "NA",
        "blockFund": "Y",
        "remark": "S",
        "revokable": "N"
    }    

}'
```
```curl cURL Request for PROD
curl --location 'https://api.pluralonline.com/api/v1/upi/subscription/process/payment?token=pMvPyims9dNIPAVl%2FPqkQZLXKtftqHDbe9SdX6BzZWQ%3D' \
--header 'Content-Type: application/json' \
--data-raw '{
    "merchantId": "123456",
    "clientUniqueReference": "simulator_test_11",
    "enableNotification": false,
    "plan": {
        "merchantMaintainedPlan": true,
        "startDate" : "2024-03-06 18:00:00",
        "endDate" : "2024-03-30 23:00:00",
        "merchantPlanId": "merchant plan A",
        "planName": "merchant plan for daily frequency",
        "frequencyType": "AS",
        "frequency":"5",
        "planDescription": "A customer will be charged every Day with this plan",
        "amount": {"value":250,"currency":"INR"},
        "maxLimitAmount": {"value":2500.0,"currency":"INR"}
    },
    "quantity": 1,
    "startDate": "2024-03-06 18:00:00",
    "endDate": "2024-03-30 23:00:00",
    "customerData": {
        "firstName": " ",
        "lastName": " ",
        "countryCode": "91",
        "customerMobile": "8761234789",
        "customerEmail": "test2@test.com"
    },
    "autoDebit": true,
    "upi_data": {
        "txnMode": "C",
        "vpa": "callback@icici"
    },
    "payments": {
        "amountLimit": "M",
        "debitDay": 0,
        "debitRule": "NA",
        "blockFund": "Y",
        "remark": "S",
        "revokable": "N"
    }    

}'
```
```json Sample Response
{
    "response_code": "1",
    "response_message": "Transaction Successful",
    "merchant_order_id": " ",
    "order_id": 123765,
    "subscription_id": "85",
    "plan_id": "37",
    "refId": "EZM2024022710191500149026",
    "signedQRData": "upi://mandate?pa=pinelabstest@icici&pn=Pinelabs&tr=EZM2024022710191500149026&am=100.00&cu=INR&orgid=400011&mc=5818&purpose=14&tn=Mandate+Request&validitystart=27022024&validityend=05032024&amrule=MAX&Recur=DAILY&Rev=Y&Share=Y&Block=N&txnType=CREATE&mode=13&sign=MEYCIQCy1VKznbRag4OhpdcDiabv57M1XEvai23Eg8G+TmOiTgIhAPDnROQuMmayCTqI7mfxUKSqbemhiXlGIj0lg9DDLLEk"
}
```

The API supports two types of subscription flows: ** Intent Flow** and** Collect Flow**, enabling you to choose the one that best suits your payment model. For fixed frequencies (e.g., daily, weekly), the mandate execution is automated after customer approval. For custom frequencies, the execution depends on additional conditions, ensuring compliance with banking requirements.

Whether you opt for a **Plural Maintained Plan** or design your own **Merchant Maintained Plan**, the Process Payment API ensures smooth integration and functionality.

> 🚧 Watch Out:
> 
> 1. **Restrictions on OT Mandates with Trials**:  
>    OT (One-Time) mandates cannot include a trial period due to acquirer bank restrictions. Ensure that all OT mandates are configured without a trial option to comply with these limitations.
> 2. **Presentation APIs for AS Frequencies**:  
>    When using the **AS** (As per schedule) frequency, you must integrate the Presentation APIs for mandate execution after the customer's bank approval.

### JWT Authentication

You can generate the JWT token by following below steps:

**Step 1: Generating Private/Public Key for JWT Authentication**

1. **Generate RSA Key Pair: **
   - Generate a 2048-bit RSA private key and its corresponding public key.
   - Keep the private key secure; it will be used to generate JWT tokens.
   - Share the public key with the Subscriptions onboarding team.
2. **Onboarding Process: **  
   After successfully onboarding to the Subscriptions product, the onboarding team will provide you with the following details:
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

## 3. Get Plan API

This section covers two key APIs: GetPlanById and GetAllPlans. These APIs help you manage and retrieve plan-related information effectively.

### 3.1 Get Plan By ID

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

### 3.2 Get All Plans

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

## 4. Get Subscriptions API

Subscriptions are mandates created for every plan and there are 3 APIs available to get details of subscriptions.

### 4.1 Get All Subscriptions

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

### 4.2 Get Subscription By ID

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

### 4.3 Get All Transaction

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

## 5. Presentation API

The Presentation API enables you to schedule debits for **Mandate Subscriptions** with the frequency type set to `AS ` (As and when Presented). 

With the Presentation API, you gain greater flexibility and control, allowing you to schedule debits as per your convenience.

### 5.1 Schedule Presentation

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

### 5.2 Cancel Presentation

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

### 5.3 Get Presentation by Id

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

### 5.4 Get All Presentations

Use this API to get details of all presentations scheduled for a merchant.

Shown below are the Sample cURL Request and response for **Get Presentations**.

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

## 6. Retry API

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

## 7. Resume API

Resume API is used to resume a Subscription when the Subscription is Halted or Paused by Merchant.

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
