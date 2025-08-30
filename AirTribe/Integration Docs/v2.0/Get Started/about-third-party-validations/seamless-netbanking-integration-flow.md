---
title: "Seamless NetBanking Integration Flow"
slug: "seamless-netbanking-integration-flow"
excerpt: "Learn how to integrate with Plural APIs to use Plural Third Party Validation."
hidden: false
createdAt: "Wed Nov 06 2024 05:43:40 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Jan 31 2025 07:32:06 GMT+0000 (Coordinated Universal Time)"
---
By Integrating with Plural's Third-Party Validation (TPV), you can ensure transaction are made from the pre-registered bank accounts through conditional validation checks. Seamlessly comply with SEBI guidelines for secure online payments. Provide seamless payment experience using Netbanking.

The figure below shows the step-by-step procedure for integrating with Plural Third Party Validation (TPV).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/93e1e09-Group_20_1.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]


1. **Prerequisite**: Our accept payment API use Base64 Encode as an input request. And use HashMap to authorize the payment.
   1. **Enter Payment Details**: Enter the payment and merchant details using the sample JSON payload.
   2. **Encode JSON**: Use the updated payment and merchant details JSON to convert to a Base64 Encode.
   3. **HashMap**: Along with the Base64 Encode pass the secret key and generate an HashMap secret.
2. **Accept Payment**: Integrate our Accept Payment API in you Backend server and use this API to initiate a payment.
3. **Generate Payment Link**: Integrate our Generate Payment Link API in your Backend and use this API to generate a Payment Link.

> 📘 Note:
> 
> **Handle Payment**: After generating the URL, use this Link to navigate your customers to their mobile apps. You can do this by rendering the URL returned by Plural as a button or a link for the customer to use.

## 1. Prerequisite

1. **Enter Payment Details**: Use the below JSON to enter the payment Details. You are required to enter the `merchant_data` and `payment_data` child object.

```json JSON
{
  "merchant_data": {
    "merchant_id": 12345678,
    "merchant_access_code": "4a8c422e-928d-4f84-bfe8-27a09af66647",
    "unique_merchant_txn_id": "XYZ123",
    "merchant_return_url": "https://www.pinelabs.com"
  },
  "payment_data": {
    "amount_in_paisa": 800
  },
  "txn_data": {
    "navigation_mode": "7",
    "payment_mode": "3",
    "transaction_type": "1",
    "time_stamp": 157588000000
  }
}
```

### JSON Parameters

<details>

<summary>Click Here</summary>

The table below lists the various JSON parameters.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "merchant_data",
    "0-1": "`object`",
    "0-2": "`M`",
    "0-3": "An object that contains the merchant details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/prerequisite#merchant-data-child-object\" target =\"_blank\">Learn more about our `merchant_data` child object</a>.",
    "1-0": "payment_data",
    "1-1": "`object`",
    "1-2": "`M`",
    "1-3": "An object that contains the payment details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/prerequisite#payment-data-child-object\" target =\"_blank\">Learn more about our `payment_data` child object</a>.",
    "2-0": "txn_data",
    "2-1": "`object`",
    "2-2": "`M`",
    "2-3": "An object that contains the transaction details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/prerequisite#txn-data-child-object\" target =\"_blank\">Learn more about our `txn_data` child object</a>.",
    "3-0": "customer_data",
    "3-1": "`object`",
    "3-2": "`O`",
    "3-3": "An object that contains the customer details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/prerequisite#customer-data-child-object\" target =\"_blank\">Learn more about our `customer_data` child object</a>.",
    "4-0": "udf_data",
    "4-1": "`object`",
    "4-2": "`O`",
    "4-3": "An object that contains the user defined details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/prerequisite#udf-data-child-object\" target =\"_blank\">Learn more about our `merchant_data` child object</a>.",
    "5-0": "`product_details`",
    "5-1": "`array of object`",
    "5-2": "`O`",
    "5-3": "An object that contains the array of product details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/prerequisite#product-details-child-object\" target =\"_blank\">Learn more about our `merchant_data` child object</a>."
  },
  "cols": 4,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


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
    "2-0": "unique_merchant_txn_id",
    "2-1": "`string`",
    "2-2": "`M`",
    "2-3": "Unique identifier of the specific transaction.  \n  \nExample: `xyz123`",
    "3-0": "merchant_return_url",
    "3-1": "`string`",
    "3-2": "`M`",
    "3-3": "Merchant return URL.  \n  \nExample: `https://www.pinelabs.com`  \n  \n**Note**: Your customer's are redirected to this page after a successful payment."
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

The table below lists the various parameters in the `payment_data` child object.

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
    "0-3": "The transaction amount in paisa.  \n  \nExample: `800`"
  },
  "cols": 4,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Txn Data [Child Object]

The table below lists the various parameters in the `transaction_data` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "navigation_mode",
    "0-1": "`integer`",
    "0-2": "`M`",
    "0-3": "Checkout navigation mode.  \n  \nExample: `7`  \n  \nAccepted values:<ul><li>`2`: For Redirect Checkout.</li><li>`7`: For Seamless Checkout.</ul></li>  \n  \n**Note**: Currently TPV is available through Seamless checkout only.",
    "1-0": "payment_mode",
    "1-1": "`string`",
    "1-2": "`M`",
    "1-3": "The payment mode you prefer to accept payment.  \n  \nAccepted values: <ul><li>`3`: For Netbanking.</ul></li>",
    "2-0": "transaction_type",
    "2-1": "`integer`",
    "2-2": "`M`",
    "2-3": "The type of transaction.  \n  \nExample: `1`  \n  \nAccepted values: <ul><li>`1`: For Purchase.</ul></li>",
    "3-0": "time_stamp",
    "3-1": "`integer`",
    "3-2": "`O`",
    "3-3": "Unix timestamp.  \n  \nExample: `157588000000`"
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


#### Customer Data [Child Object]

The table below lists the various parameters in the `customer_data` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "email_id",
    "0-1": "`string`",
    "0-2": "`O`",
    "0-3": "Customer's email address.  \n  \nExample: `kevin.bob@example.com`",
    "1-0": "first_name",
    "1-1": "`string`",
    "1-2": "`O`",
    "1-3": "Customer's first name.  \n  \nExample: `Kevin`",
    "2-0": "last_name",
    "2-1": "`string`",
    "2-2": "`O`",
    "2-3": "Customer's last name.  \n  \nExample: `Bob`",
    "3-0": "customer_id",
    "3-1": "`string`",
    "3-2": "`O`",
    "3-3": "Unique identifier of the customer.  \n  \nExample: `123456`",
    "4-0": "mobile_no",
    "4-1": "`string`",
    "4-2": "`O`",
    "4-3": "Customer's mobile number.  \n  \nExample: `9876543210`",
    "5-0": "billing_data",
    "5-1": "`object`",
    "5-2": "`O`",
    "5-3": "An object that contains the billing details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/prerequisite#billing-data-child-object\" target =\"_blank\">Learn more about our `merchant_data` child object</a>.",
    "6-0": "shipping_data",
    "6-1": "`object`",
    "6-2": "`O`",
    "6-3": "An object that contains the shipping details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/prerequisite#shipping-data-child-object\" target =\"_blank\">Learn more about our `merchant_data` child object</a>."
  },
  "cols": 4,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Billing Data [Child Object]

The table below lists the various parameters in the `billing_data` child object. This is part of the `customer_data` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "address1",
    "0-1": "`string`",
    "0-2": "`O`",
    "0-3": "Customer's billing address1.  \n  \nExample: `No 10 Church street Bangalore`",
    "1-0": "address2",
    "1-1": "`string`",
    "1-2": "`O`",
    "1-3": "Customer's billing address2.  \n  \nExample: `No 10 Brigade road Bangalore`",
    "2-0": "address3",
    "2-1": "`string`",
    "2-2": "`O`",
    "2-3": "Customer's billing address3.  \n  \nExample: `No 10 M G road Bangalore`",
    "3-0": "pincode",
    "3-1": "`string`",
    "3-2": "`O`",
    "3-3": "PIncode of the billing address.  \n  \nExample: `560001`",
    "4-0": "city",
    "4-1": "`string`",
    "4-2": "`O`",
    "4-3": "City of the billing address.  \n  \nExample: `Bangalore`",
    "5-0": "state",
    "5-1": "`string`",
    "5-2": "`O`",
    "5-3": "State of the billing address.  \n  \nExample: `Karanataka`",
    "6-0": "country",
    "6-1": "`string`",
    "6-2": "`O`",
    "6-3": "Country of the billing address.  \n  \nExample: `India`"
  },
  "cols": 4,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Shipping Data [Child Object]

The table below lists the various parameters in the `shipping_data` child object. This is part of the `customer_data` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "address1",
    "0-1": "`string`",
    "0-2": "`O`",
    "0-3": "Customer's shipping address1.  \n  \nExample: `No 10 Church street Bangalore`",
    "1-0": "address2",
    "1-1": "`string`",
    "1-2": "`O`",
    "1-3": "Customer's shipping address2.  \n  \nExample: `No 10 Brigade road Bangalore`",
    "2-0": "address3",
    "2-1": "`string`",
    "2-2": "`O`",
    "2-3": "Customer's shipping address3.  \n  \nExample: `No 10 M G road Bangalore`",
    "3-0": "pincode",
    "3-1": "`string`",
    "3-2": "`O`",
    "3-3": "PIncode of the shipping address.  \n  \nExample: `560001`",
    "4-0": "city",
    "4-1": "`string`",
    "4-2": "`O`",
    "4-3": "City of the shipping address.  \n  \nExample: `Bangalore`",
    "5-0": "state",
    "5-1": "`string`",
    "5-2": "`O`",
    "5-3": "State of the shipping address.  \n  \nExample: `Karanataka`",
    "6-0": "country",
    "6-1": "`string`",
    "6-2": "`O`",
    "6-3": "Country of the shipping address.  \n  \nExample: `India`"
  },
  "cols": 4,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Udf Data [Child Object]

The table below lists the various parameters in the `udf_data` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "udf_field_1",
    "0-1": "`string`",
    "0-2": "`O`",
    "0-3": "User defined value1.  \n  \nExample: `DD`",
    "1-0": "udf_field_2",
    "1-1": "`string`",
    "1-2": "`O`",
    "1-3": "User defined value2  \n  \nExample: `XOF`",
    "2-0": "udf_field_3",
    "2-1": "`string`",
    "2-2": "`O`",
    "2-3": "User defined value3.  \n  \nExample: `XOA`",
    "3-0": "udf_field_4",
    "3-1": "`string`",
    "3-2": "`O`",
    "3-3": "User defined value4.  \n  \nExample: `ASDF`"
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


#### Product Details [Child Object]

The table below lists the various parameters in the `product_details` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "product_code",
    "0-1": "`string`",
    "0-2": "`M`",
    "0-3": "The product code.  \n  \nExample: `7803`",
    "1-0": "product_amount",
    "1-1": "`string`",
    "1-2": "`M`",
    "1-3": "The product amount.  \n  \nExample: `10000`"
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


<br />

> 📘 Note:
> 
> - The sum of all the products `product_amount` must be equal to the total cart value `payment_data.amount_in_paisa`.

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
    merchant_data.put("unique_merchant_txn_id", "XYZ123");
    merchant_data.put("merchant_return_url", "whitelisted_merchant_return_url");
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

## 2. Accept Payment API

Use this API to generate a token against a payment.

Use the below Endpoints to accept payment.

```text Accept Payment UAT Endpoint
POST: https://uat.pinepg.in/api/v2/accept/payment
```
```Text Accept Payment PROD Endpoint
POST: https://pinepg.in/api/v2/accept/payment
```

Shown below are the sample request and sample response for a Accept Payment API.

```json Sample Request
{
  "request": "ewogICJtZXJjaGFudF9kYXRhIjogewogICAgIm1lcmNoYW50X2lkIjogMjIyMDgyLAogICAgIm1lcmNoYW50X2FjY2Vzc19jb2RlIjogImNmZDA1YzBjLTM5ZjEtNDIzMi1iZDZmLTZkM2E4NjA4ZTFiZSIsCiAgICAidW5pcXVlX21lcmNoYW50X3R4bl9pZCI6ICJ0ZXN0aW5nZWRnZXNlYW1sZXNzMTEyMzQ1NDMyIiwKICAgICJtZXJjaGFudF9yZXR1cm5fdXJsIjogImh0dHBzOi8vc3RhZ2Utd2ViYXBwLnBheXRtLmluL3Blb24ucGhwIgogIH0sCiAgInBheW1lbnRfZGF0YSI6IHsKICAgICJhbW91bnRfaW5fcGFpc2EiOiA4MDAKICB9LAogICJ0eG5fZGF0YSI6IHsKICAgICJuYXZpZ2F0aW9uX21vZGUiOiAiNyIsCiAgICAicGF5bWVudF9tb2RlIjogIjEwIiwKICAgICJ0cmFuc2FjdGlvbl90eXBlIjogIjEiLAogICAgInRpbWVfc3RhbXAiOiAxNTc1ODgwMDAwMDAKICB9Cn0="
}
```
```json Sample Response
{
  "token": "S087B99vA68R0L9gb8JI%2bqjds%2bOZaArBKLb3s7eQ%2fg7k%3d",
  "response_code": 1,
  "response_message": "SUCCESS"
}
```

Refer to our <a href="https://developer.pluralonline.com/v2.0/reference/tpv-accept-payment" target="_blank">Accept Payment API Documentation</a> for more information.

## 3. Generate Payment Link

To Generate a Payment Link, use our Generate Payment Link API. 

Use the below endpoints to Generate a Payment Link.

```text Generate Payment Link UAT Endpoint
POST: https://uat.pinepg.in/api/v2/process/payment
```
```Text Generate Payment Link Prod Endpoint
POST: https://pinepg.in/api/v2/process/payment
```

### Query Parameter

`Token`: You need to pass the token generated in the Accept Payment API as the query parameter.

Shown below is a sample request and sample response for a Generate Payment Link API.

```json Sample Request
{
  "netbanking_data": {
    "pay_code": "NB1535"
  },
  "tpv_data": {
    "account_number": "1234567890123456",
    "name": "Kenin",
    "ifsc": ""
  }
}
```
```json Sample Response
{
  "redirect_url": "https://uat.pinepg.in/pinepg/v2/process/payment?token=S01VHxGYfOhZdIEej6%2fKIZ88MiRRxF6vL8HdnOjLKDt2CY%3d",
  "response_code": 1,
  "response_message": "SUCCESS"
}
```

Refer to our <a href="https://developer.pluralonline.com/v2.0/reference/tpv-generate-payment-link" target="_blank">Generate Payment Link API Documentation</a> for more information.

> 📘 Note:
> 
> - For PNB accounts, pass 16-digit account numbers with a prefix zero.  
>   Example: If the account number is 123456789012345, pass it as 0123456789012345.
> - For PSBI, Canara, and CITI accounts, pass 17-digit account numbers with a prefix zero.  
>   Example: If the account number is 1234567890123456, pass it as 01234567890123456.
> - For all other banks, pass the account number as is.

## Handle Payments

Use the generated link returned in our Generate Payment Link API to redirect your customers to the seamless checkout to accept payment.

To know the status of the payment you can use the below options.

1. **<a href="<https://developer.pluralonline.com/v2.0/reference/payment-inquiry-refund" target="_blank">Inquiry API</a>**: Use this API to check transaction statuses.
2. **<a href="https://developer.pluralonline.com/v2.0/docs/developer-tools-webhook" target="_blank">Webhook Notification</a>**: We send Webhook notifications on the successful payment or any changes to the payment's response object.
