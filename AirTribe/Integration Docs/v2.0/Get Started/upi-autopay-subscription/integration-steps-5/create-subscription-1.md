---
title: "Create Subscription"
slug: "create-subscription-1"
excerpt: "Learn how to create Subscriptions by using Plural APIs."
hidden: true
createdAt: "Tue Dec 10 2024 09:57:39 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Dec 11 2024 04:53:55 GMT+0000 (Coordinated Universal Time)"
---
## Prerequisite

## 1. Generate Token and order ID

Our Create Order API use Base64 Encode as an input request. And use HashMap to authorize the payment.

### 1.1 Enter Payment Details

 Use the below JSON to enter the payment Details. You are required to enter the `merchant_data`, `payment_info_data`, `subscription_data` and `payment_category_type`.

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

### 1.2 Encode JSON

Convert the updated JSON to a Base64 Encode. Use the below sample code to handle the conversion of the JSON to a Base64 Encode.

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

### 1.3 HashMap

Generate HashMap using the Base64 Encode and the secret key. Use the below sample code to handle the generation of HashMap using SHA256.

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

### 1.4 Create order API

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

`Token`: You need to pass the token generated in the Create Order API as the query parameter.

### 2.1 Collect Flow

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
"response_code": "1",
"response_message": "Transaction Initiated",
"merchant_order_id": "aank_1011",
"order_id": 123982,
"subscription_id": "239",
"plan_id": "34"
}
```

### 2.2 Intent Flow

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
