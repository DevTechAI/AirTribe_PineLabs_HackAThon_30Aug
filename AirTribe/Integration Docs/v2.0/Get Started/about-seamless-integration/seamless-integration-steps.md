---
title: "Integration Steps"
slug: "seamless-integration-steps"
excerpt: "Learn how you can integrate with Plural APIs to start accepting payments on your website."
hidden: false
createdAt: "Fri Sep 27 2024 11:45:35 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Apr 08 2025 11:14:07 GMT+0000 (Coordinated Universal Time)"
---
Follow the below steps to integrate with Plural seamless checkout APIs in your application.

1. <a style="text-decoration:none" href="https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#1-prerequisite" >Prerequisite</a>.
2. <a style="text-decoration:none" href="https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#2-accept-payment-api" target ="_blank">Accept Payment</a>.
3. <a style="text-decoration:none" href="https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#3-process-payment-api" target ="_blank">Process Payment</a>.
   1. <a style="text-decoration:none" href="https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#1-cards" target ="_blank">Cards</a>.
   2. <a style="text-decoration:none" href="https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#2-upi" target ="_blank">UPI</a>.
   3. <a style="text-decoration:none" href="https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#3-net-banking" target ="_blank">Net Banking</a>.
   4. <a style="text-decoration:none" href="https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#4-wallets" target ="_blank">Wallets</a>.
4. <a style="text-decoration:none" href="https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#4-handle-payment" target ="_blank">Handle Payments</a>.
   1. <a style="text-decoration:none" href="https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#41-store-payment-details" target ="_blank">Store Payment Details</a>.
   2. <a style="text-decoration:none" href="https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#42-verify-payment-signature" target ="_blank">Verify Payment Signature</a>.

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
    "payment_mode": "10",
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
    "0-3": "An object that contains the merchant details.  \n  \n<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#merchant-data-child-object\" target =\"_blank\">Learn more about our `merchant_data` child object</a>.",
    "1-0": "payment_data",
    "1-1": "`object`",
    "1-2": "`M`",
    "1-3": "An object that contains the payment details.  \n  \n<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#payment-data-child-object\" target =\"_blank\">Learn more about our `payment_data` child object</a>.",
    "2-0": "txn_data",
    "2-1": "`object`",
    "2-2": "`M`",
    "2-3": "An object that contains the transaction details.  \n  \n<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#txn-data-child-object\" target =\"_blank\">Learn more about our `txn_data` child object</a>.",
    "3-0": "customer_data",
    "3-1": "`object`",
    "3-2": "`O`",
    "3-3": "An object that contains the customer details.  \n  \n<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#customer-data-child-object\" target =\"_blank\">Learn more about our `customer_data` child object</a>.",
    "4-0": "udf_data",
    "4-1": "`object`",
    "4-2": "`O`",
    "4-3": "An object that contains the user defined details.  \n  \n<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#udf-data-child-object\" target =\"_blank\">Learn more about our `udf_data` child object</a>.",
    "5-0": "`product_details`",
    "5-1": "`array of object`",
    "5-2": "`O`",
    "5-3": "An object that contains the array of product details.  \n  \n<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#product-details-child-object\" target =\"_blank\">Learn more about our `product_details` child object</a>."
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
    "1-3": "The payment mode you prefer to accept payment.  \n  \nAccepted values: <ul><li>`1`: CREDIT/DEBIT CARD</li><li>`3`: NET BANKING</li><li>`4`:CREDIT EMI</li><li>`10`: UPI</li><li>`11`: WALLET</li><li>`14`: DEBIT EMI</li><li>`16`: PREBOOKING</li><li>`17`: BNPL/FLEXIPAY</li><li>`19`: Cardless EMI</li><li>`20`: PBP (Paybypoints)</ul></li>",
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
    "5-3": "An object that contains the billing details.  \n  \n<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#billing-data-child-object\" target =\"_blank\">Learn more about our `billing_data` child object</a>.",
    "6-0": "shipping_data",
    "6-1": "`object`",
    "6-2": "`O`",
    "6-3": "An object that contains the shipping details.  \n  \n<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#shipping-data-child-object\" target =\"_blank\">Learn more about our `shipping_data` child object</a>."
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

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/v2.0/reference/tpv-accept-payment" target="_blank">Accept Payment API Documentation</a> for more information.

## 3. Process Payment API

Use this API process a Payment. You can use the same API to process a payment using the below methods of payment.

- Card Payment
- UPI Payment
- Net Banking
- Wallet

> 📘 Note:
> 
> - Ensure that you use the appropriate payloads corresponding to the specific payment methods for which you want to initiate a request.
> - We also verify the payment method provided in the "Accept Payment" request before processing the process payment.

Use the below endpoints to Process a Payment.

```text Process Payment UAT Endpoint
POST: https://uat.pinepg.in/api/v2/accept/payment
```
```Text Process Payment Prod Endpoint
POST: https://pinepg.in/api/v2/accept/payment
```

### Query Parameter

`Token`: You need to pass the token generated in the Accept Payment API as the query parameter.

### 1. Cards

> 🚧 Watch Out
> 
> - To Integrate with Plural seamless checkout flow you must have a PCI compliance certificate.

Shown below is a sample request and sample response for a Process Payment API via Cards.

```json Sample Request
{
  "card_data": {
    "card_number": "4012001037141112",
    "card_expiry_year": "2030",
    "card_expiry_month": "12",
    "card_holder_name": "Test",
    "cvv": "123"
  }
}
```
```json Sample Response

```

#### Sample Request

<details>

<summary>Click Here</summary>

The table below lists all the request parameters.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "card_data",
    "0-1": "`object`",
    "0-2": "`M`",
    "0-3": "An object that contains the card details.  \n  \n<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#card-data-child-object\" target =\"_blank\">Learn more about our `card_daata` child object</a>."
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


##### Card Data [Child Object]

The table below lists the various parameters in the `card_data` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "card_number",
    "0-1": "`string`",
    "0-2": "`M`",
    "0-3": "Card Number.  \n  \nExample: `123456789012`  \n  \nSupported characters: `0-9`",
    "1-0": "card_expiry_year",
    "1-1": "`string`",
    "1-2": "`M`",
    "1-3": "Card expiry year as on the card.  \n  \nHas to be 4 digits.  \n  \nExample: `2024`  \n  \nSupported characters: `0-9`",
    "2-0": "card_expiry_month",
    "2-1": "`string`",
    "2-2": "`M`",
    "2-3": "Card expiry month as on the card.  \n  \nHas to be 2 digits.  \n  \nExample: `08`  \n  \nSupported characters: `0-9`",
    "3-0": "card_holder_name",
    "3-1": "`string`",
    "3-2": "`M`",
    "3-3": "Card holder name.  \n  \nExample: `Kevin`",
    "4-0": "cvv",
    "4-1": "`string`",
    "4-2": "`M`",
    "4-3": "Card Verification Value [cvv] of the card.  \n  \nExample: `123`  \n  \nSupported characters: `0-9`"
  },
  "cols": 4,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


</details>

### 2. UPI

UPI Payments can be further categorized into two types: Collect and Intent. You can use this process payment API to process both Collect and Intent payment requests.

#### UPI Intent

Shown below is a sample request and sample response for a Process Payment API via UPI Intent flow.

```json Sample Request
{
  "upi_data": {
    "upi_option": "UPI",
    "txn_mode": "INTENT"
  }
}
```
```json Sample Response
{
  "pg_upi_unique_request_id": "170724PLPre22116284",
  "deep_link": "upi://pay?pa=pl.pinelabs@pineaxis&pn=Pinelabs%20Private%20Limited%20dummy&am=8.00&mam=8.00&tr=SU01J2ZMXHX4PVBVASQJPBG2XW6V&tn=Payment%20for%20342027241&cu=INR&mc=7399",
  "pine_pg_transaction_id": 342027241,
  "short_link": "https://upipay.setu.co/nO6yP65XUmwh",
  "response_code": 1,
  "response_message": "SUCCESS"
}
```

#### UPI Collect

Shown below is a sample request and sample response for a Process Payment API via UPI Collect flow.

```json Sample Request
{
  "upi_data": {
    "vpa": "test@upi",
    "upi_option": "UPI "
  }
}
```
```json Sample Response
{
  "response_code": 1,
  "response_message": "SUCCESS"
}
```

##### Sample Request

<details>

<summary>Click Here</summary>

The table below lists all the request parameters.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "upi_data",
    "0-1": "`object`",
    "0-2": "`M`",
    "0-3": "An object that contains the UPI details.  \n  \n<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#upi-data-child-object\" target =\"_blank\">Learn more about our `upi_data` child object</a>."
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


#### UPI Data [Child Object]

The table below lists the various parameters in the `upi_data` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "upi_option",
    "0-1": "`string`",
    "0-2": "`M`",
    "0-3": "UPI Payment options.  \n  \nAccepted values:<ul><li>`UPI`</li><li>`GPAY`</ul></li>",
    "1-0": "txn_mode",
    "1-1": "`string`",
    "1-2": "`C`",
    "1-3": "Transaction mode of the UPI payment.  \n  \nAccepted value: `INTENT`  \n  \n**Note**: Mandatory for UPI intent payment.",
    "2-0": "vpa",
    "2-1": "`string`",
    "2-2": "`C`",
    "2-3": "VPA handle of your customer's.  \n  \nExample: `kevin.bob@examplebank.com`  \n  \n**Note**: Mandatory for UPI Collect payment."
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


</details>

### 3. Net Banking

Shown below is a sample request and sample response for a Process Payment API via Net Banking.

```json Sample Request
{
  "netbanking_data": {
    "pay_code": "NB1493"
  }
}
```
```json Sample Response
{
  "response_code": 1,
  "response_message": "SUCCESS",
  "redirect_url": "http://hostname:port/pinepg/v2/process/payment?token=848RFsu%2bRnNcSsaZdzEgkeosvCc2o5lK TV4uKJF%2fcjE%3d"
}
```

#### Sample Request

<details>

<summary>Click Here</summary>

The table below lists all the request parameters.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "netbanking_data",
    "0-1": "`object`",
    "0-2": "`M`",
    "0-3": "An object that contains the Net Bankding details.  \n  \n<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#netbanking-data-child-object\" target =\"_blank\">Learn more about our `netbanking_data` child object</a>."
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


#### Netbanking Data [Child Object]

The table below lists the various parameters in the `netbanking_data` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "pay_code",
    "0-1": "`string`",
    "0-2": "`M`",
    "0-3": "Payment codes of corresponding Banks.  \n  \nExample: `NB1493`"
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


The table below lists the various pay codes of the corresponding Banks.

| Pay Code | Bank Name                                |
| :------- | :--------------------------------------- |
| `NB1148` | Kotak Bank                               |
| `NB1378` | Andhra Bank                              |
| `NB1484` | Andhra Bank Corporate                    |
| `NB1530` | Allahabad Bank                           |
| `NB1529` | AU Small Finance Bank                    |
| `NB1485` | Bank of Baroda - Corporate Banking       |
| `NB1486` | Bank of Bahrain and Kuwait               |
| `NB1487` | Bank of Baroda - Retail Banking          |
| `NB1511` | Bassien Catholic Coop Bank               |
| `NB1533` | Bandhan Bank - Corporate                 |
| `NB1508` | Bandhan Bank                             |
| `NB1229` | Bank of Maharashtra                      |
| `NB1527` | Barclays Bank - Corporate Net Banking    |
| `NB1147` | Central Bank                             |
| `NB1224` | Canara Bank                              |
| `NB1488` | Cosmos Bank                              |
| `NB1489` | Punjab National Bank - Corporate Banking |
| `NB1523` | Corporation Bank - Corporate             |
| `NB1135` | Corporation Bank                         |
| `NB1272` | Catholic Syrian Bank                     |
| `NB1215` | City Union Bank                          |
| `NB1490` | Deutsche Bank                            |
| `NB1509` | Digibank by DBS                          |
| `NB1491` | Development Credit Bank                  |
| `NB1492` | Dena Bank                                |
| `NB1526` | Dhanlaxmi Bank Corporate                 |
| `NB1373` | Dhanalakshmi Bank                        |
| `NB1515` | Equitas Small Finance Bank               |
| `NB1518` | ESAF Small Finance Bank                  |
| `NB1029` | Federal Bank                             |
| `NB1532` | Fincare Bank - Retail                    |
| `NB1007` | HDFC Bank                                |
| `NB1016` | ICICI Bank                               |
| `NB1493` | IDBI Bank                                |
| `NB1521` | IDBI Corporate                           |
| `NB1510` | IDFC FIRST Bank                          |
| `NB1431` | IndusInd Bank                            |
| `NB1143` | Indian Bank                              |
| `NB1213` | Indian Overseas Bank                     |
| `NB1015` | JK Bank                                  |
| `NB1503` | Janata Sahakari Bank Ltd Pune            |
| `NB1133` | Karnataka Bank                           |
| `NB1506` | Kalyan Janata Sahakari Bank              |
| `NB1514` | The Kalupur Commercial Co-Operative Bank |
| `NB1494` | Karur Vysya Bank                         |
| `NB1495` | Laxmi Vilas Bank - Corporate Net Banking |
| `NB1496` | Laxmi Vilas Bank - Retail Net Banking    |
| `NB1507` | Mehsana urban Co-op Bank                 |
| `NB1520` | North East Small Finance Bank Ltd        |
| `NB1504` | NKGSB Co-op Bank                         |
| `NB1154` | Oriental Bank of Commerce                |
| `NB1534` | Karnataka Gramin Bank                    |
| `NB1497` | Punjab & Maharashtra Co-op Bank          |
| `NB1381` | Punjab National Bank                     |
| `NB1512` | PNB Yuva Netbanking                      |
| `NB1421` | Punjab and Sindh Bank                    |
| `NB1513` | RBL Bank Limited                         |
| `NB1524` | RBL Bank Limited - Corporate Banking     |
| `NB1531` | State bank Of India                      |
| `NB1498` | Standard Chartered Bank                  |
| `NB1499` | South Indian Bank                        |
| `NB1517` | Suryoday Small Finance Bank              |
| `NB1525` | Shamrao Vithal Co-op Bank - Corporate    |
| `NB1500` | Shamrao Vithal Co-op Bank                |
| `NB1380` | Saraswat Bank                            |
| `NB1501` | Syndicate Bank                           |
| `NB1516` | Thane Bharat Sahakari Bank Ltd           |
| `NB1505` | TJSB Bank                                |
| `NB1439` | Tamilnad Mercantile Bank                 |
| `NB1502` | Tamil Nadu State Co-operative Bank       |
| `NB1216` | Union Bank of India                      |
| `NB1483` | UCO Bank                                 |
| `NB1212` | United Bank Of India                     |
| `NB1004` | AXIS Bank                                |
| `NB1379` | Vijaya Bank                              |
| `NB1519` | Varachha Co-operative Bank Limited       |
| `NB1522` | Yes Bank Corporate                       |
| `NB1146` | Yes Bank                                 |

</details>

### 4. Wallets

Shown below is a sample request and sample response for a Process Payment API via Wallets.

```json Sample Request
{
  "wallet_data": {
    "wallet_code": "payzapp",
    "mobile_number": "9899189287"
  }
}
```
```json Sample Response
{
  "response_code": 1,
  "response_message": "SUCCESS",
  "redirect_url": "http://hostname:port/pinepg/v2/process/payment?token=848RFsu%2bRnNcSsaZdzEgkeosvCc2o5lK TV4uKJF%2fcjE%3d"
}
```

#### Sample Request

<details>

<summary>Click Here</summary>

The table below lists all the request parameters.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "wallet_data",
    "0-1": "`object`",
    "0-2": "`M`",
    "0-3": "An object that contains the Wallet details.  \n  \n<a style=\"text-decoration:none\" href=\"https://developer.pluralonline.com/v2.0/docs/seamless-integration-steps#wallet-data-child-object\" target =\"_blank\">Learn more about our `wallet_data` child object</a>."
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


#### Wallet Data [Child Object]

The table below lists the various parameters in the `wallet_data` child object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Requirement Type",
    "h-3": "Description",
    "0-0": "wallet_code",
    "0-1": "`string`",
    "0-2": "`M`",
    "0-3": "Unique code of the wallet.  \n  \nAccepted values:<ul><li>`OXY`: Oxygen</li><li>`PAYTM`: Paytm</li><li>`PAYZAPP`: PayZapp</li><li>`PHONEPE`: PhonePe</ul></li>",
    "1-0": "mobile_number",
    "1-1": "`string`",
    "1-2": "`M`",
    "1-3": "Registered mobile number of the wallet.  \n  \nExample: `9876543210`"
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

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/v2.0/reference/tpv-generate-payment-link" target="_blank">Process Payment API Documentation</a> for more information.

## 4. Handle Payment

Use the generated link returned in our accept payment API to redirect your customers to the plural hosted checkout page to accept payment. After successful payment we redirect your customers to your website.

> 📘 Note:
> 
> - On successful payment we send the webhook event `payment.captured` and the status of the payment is updated to `SUCCESS`.

### 4.1 Store Payment Details

On a successful and failed payment we return the following fields to the return url.

- We recommend you to store the payment details on your server.
- It is recommended to validate the authenticity of the payment details returned. You can authenticate by verifying the signature.

Shown below is a sample callback response returned to the return URL.

```json Sample Callback Response
{
  "merchant_id": "106598",
  "merchant_access_code": "4a39a6d4-46b7-474d-929d-21bf0e9ed607",
  "unique_merchant_txn_id": "TestNode3222",
  "pine_pg_txn_status": "4",
  "txn_completion_date_time": "18/03/2024 04:44:49 PM",
  "amount_in_paisa": "1000",
  "txn_response_code": "1",
  "txn_response_msg": "SUCCESS",
  "acquirer_name": "BILLDESK",
  "pine_pg_transaction_id": "14635747",
  "captured_amount_in_paisa": "1000",
  "refund_amount_in_paisa": "0",
  "payment_mode": "3",
  "mobile_no": "",
  "udf_field_1": "",
  "udf_field_2": "",
  "udf_field_3": "",
  "udf_field_4": "",
  "Acquirer_Response_Code": "0300",
  "Acquirer_Response_Message": "DEFAULT",
  "parent_txn_status": "",
  "parent_txn_response_code": "",
  "parent_txn_response_message": "",
  "dia_secret": "156A7BD91DCC0A7BD9D080FDC900581A7BC65D8B17A535E24CE6A042B93DF7C9",
  "dia_secret_type": "SHA256"
}
```

Refer to the below table to know the status of the transaction through the sample callback response.

[block:parameters]
{
  "data": {
    "h-0": "PinePGTxnStatus",
    "h-1": "TxnResponseCode",
    "h-2": "Transaction Status",
    "0-0": "`4`",
    "0-1": "`1`",
    "0-2": "Success",
    "1-0": "`1`",
    "1-1": "`0`",
    "1-2": "To know the status of the transaction please use our <a href=\"https://developer.pluralonline.com/v2.0/reference/payment-inquiry\" target=\"_blank\">Inquiry API</a>.",
    "2-0": "`-7`",
    "2-1": "Any Code",
    "2-2": "Failed"
  },
  "cols": 3,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


> 📘 Note:
> 
> - Signature is sent against `dia_secret` key use this signature to verify the payment.

### 4.2 Verify Payment Signature

Ensure you follow this as a mandatory step to verify the authenticity of the details returned to the checkout form for a transaction. Follow the below steps to verify the payment signature.

1. Generate a signature on your server using the response callback with the SHA256 algorithm. Follow the below steps to generate a signature.
   1. Remove `dia_secret` and `dia_secret_type` from the response callback returned to the return URL.
   2. Sort the remaining payload in alphabetical order.
   3. Convert the sorted payload into a string with values separated by `&`.
   4. Use the string generated with the MID secret to create a signature using the SHA256 algorithm.

The samples for the above steps are shown below.

```json Updated Sample Callback
{
  "merchant_id": "106598",
  "merchant_access_code": "4a39a6d4-46b7-474d-929d-21bf0e9ed607",
  "unique_merchant_txn_id": "TestNode3222",
  "pine_pg_txn_status": "4",
  "txn_completion_date_time": "18/03/2024 04:44:49 PM",
  "amount_in_paisa": "1000",
  "txn_response_code": "1",
  "txn_response_msg": "SUCCESS",
  "acquirer_name": "BILLDESK",
  "pine_pg_transaction_id": "14635747",
  "captured_amount_in_paisa": "1000",
  "refund_amount_in_paisa": "0",
  "payment_mode": "3",
  "mobile_no": "",
  "udf_field_1": "",
  "udf_field_2": "",
  "udf_field_3": "",
  "udf_field_4": "",
  "Acquirer_Response_Code": "0300",
  "Acquirer_Response_Message": "DEFAULT",
  "parent_txn_status": "",
  "parent_txn_response_code": "",
  "parent_txn_response_message": ""
}
```
```json Sorted Payload
Acquirer_Response_Code=0300
Acquirer_Response_Message=DEFAULT
acquirer_name=BILLDESK
amount_in_paisa=1000
captured_amount_in_paisa=1000
merchant_access_code=4a39a6d4-46b7-474d-929d-21bf0e9ed607
merchant_id=106598
mobile_no=
parent_txn_response_code=
parent_txn_response_message=
parent_txn_status=
payment_mode=3
pine_pg_transaction_id=14635747
pine_pg_txn_status=4
refund_amount_in_paisa=0
txn_completion_date_time=18/03/2024 04:44:49 PM
txn_response_code=1
txn_response_msg=SUCCESS
udf_field_1=
udf_field_2=
udf_field_3=
udf_field_4=
unique_merchant_txn_id=TestNode3222
```
```json Converted String Payload
Acquirer_Response_Code=0300&Acquirer_Response_Message=DEFAULT&acquirer_name=BILLDESK&amount_in_paisa=1000&ca
ptured_amount_in_paisa=1000&merchant_access_code=4a39a6d4-46b7-474d-929d21bf0e9ed607&merchant_id=106598&mobile_no=&parent_txn_response_code=&parent_txn_response_message=&parent_txn_
status=&payment_mode=3&pine_pg_transaction_id=14635747&pine_pg_txn_status=4&refund_amount_in_paisa=0&txn_compl
etion_date_time=18/03/2024 04:44:49
PM&txn_response_code=1&txn_response_msg=SUCCESS&udf_field_1=&udf_field_2=&udf_field_3=&udf_field_4=&unique_merc
hant_txn_id=TestNode3222
```

2. Use the below sample code to construct HashMap signature using the SHA256 algorithm.

```java Java
import java.io.UnsupportedEncodingException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
 
public class hash {
    public static void main(String[] args) {
        // Test the GenerateHash method
        String input = "<string>";
        String secretKey = "<secret_key>";  // Example key in hex
 
        String hash = GenerateHash(input, secretKey);
        System.out.println("Generated Hash: " + hash);
    }
    public static String GenerateHash(String input, String strSecretKey) {
        String strHash = "";
        try {
            if (!isValidString(input) || !isValidString(strSecretKey)) {
                return strHash;
            }
            byte[] convertedHashKey = new byte[strSecretKey.length() / 2];
 
            for (int i = 0; i < strSecretKey.length() / 2; i++) {
                convertedHashKey[i] =
                        (byte)Integer.parseInt(strSecretKey.substring(i * 2, (i*2)+2),16); //hexNumber radix
            }
            strHash = hmacDigest(input.toString(), convertedHashKey,
                    "HmacSHA256");
        } catch (Exception ex) {
            strHash = "";
        }
        return strHash.toUpperCase();
    }
    private static String hmacDigest(String msg, byte[] keyString, String algo) {
        String digest = null;
        try {
            SecretKeySpec key = new SecretKeySpec(keyString, algo);
            Mac mac = Mac.getInstance(algo);
            mac.init(key);
            byte[] bytes = mac.doFinal(msg.getBytes("UTF-8"));
            StringBuffer hash = new StringBuffer();
            for (int i = 0; i < bytes.length; i++) {
                String hex = Integer.toHexString(0xFF & bytes[i]);
                if (hex.length() == 1) {
                    hash.append('0');
                }
                hash.append(hex);
            }
            digest = hash.toString();
        } catch (UnsupportedEncodingException e) {
// logger.error("Exception occured in hashing the pine payment gateway request"+e);
        } catch (InvalidKeyException e) {
// logger.error("Exception occured in hashing the pine payment gateway request"+e);
        } catch (NoSuchAlgorithmException e) {
// logger.error("Exception occured in hashing the pine payment gateway request"+e);
        }
        return digest;
    }
    public static boolean isValidString(String str){
        if(str != null && !"".equals(str.trim())){
            return true;
        }
        return false;
    }
}
```

3. If the signature generated on your server matches the Plural signature returned against the `dia_secret`key, it confirms that the payment details are from Plural.
4. Capture the status returned on your database.

## Know Your Payment Status

You can know the status of the payment using the below.

1. **Webhook Notification**: We send Webhook notifications on the successful payment or any changes to the payments object.

```json Payment Captured
{
  "event_name": "payment.captured",
  "merchant_response": {
    "merchant_id": "29792",
    "payment_mode": "EMI",
    "merchant_access_code": "d860a376-2182-4448-9d87-2b2c752b8991",
    "unique_merchant_txn_id": "c-947711168513-03070150-1",
    "pine_pg_txn_status": "4",
    "txn_completion_date_time": "03/03/2024 12:33:02 PM",
    "product_code": "273865",
    "captured_amount_in_paisa": "13559000",
    "refund_amount_in_paisa": "0",
    "txn_response_code": "1",
    "amount_in_paisa": "14059000",
    "txn_response_msg": "SUCCESS",
    "acquirer_name": "HDFC_FSS_IN_HOUSE",
    "pine_pg_transaction_id": "294774500",
    "rrn": "406358019945",
    "auth_code": "055712",
    "masked_card_number": "************2562",
    "card_holder_name": "name",
    "mobile_no": "9810505359",
    "salted_card_hash": "651BB095DE12C950EF09401518017A06C5DC1A1FE5D0E7782A373F7CFB5482A3",
    "udf_field_1": "110014C25 1st FloorJangpura extension jangpura new delhiDELHIDELHI",
    "udf_field_2": "492001Hudco Regional Office 1B Surya ApartmentsKatora Talab Civil Lines RaipurRAIPURCHHATTISGARH",
    "udf_field_3": "273865",
    "udf_field_4": "01eae2ec05761000bbea86e16dcb4b79CROMA41646",
    "emi_tenure_month": "1",
    "emi_interest_rate_percent": "0.00",
    "emi_principal_amount_in_paisa": "13559000",
    "emi_amount_payable_each_month_in_paisa": "0",
    "is_brand_emi_txn": "1",
    "emi_cashback_type": "0",
    "parent_txn_status": "",
    "parent_txn_response_code": "",
    "parent_txn_response_message": "",
    "issuer_name": "HDFC",
    "product_category": "MacBook Air",
    "manufacturer": "Apple Macbook",
    "product_discount": "500000"
  }
}
```

> 📘 Note:
> 
> - Webhooks are asynchronous, so for time-sensitive actions, we recommend polling our Inquiry API.

2. **Inquiry API**

Use this API to retrieve the status of the specified payment.

Use the below endpoint to retrieve the status of the Payment.

```text Inquiry UAT Endpoint
PSOT: https://uat.pinepg.in/api/PG/v2
```
```text Inquiry PROD Endpoint
PSOT: https://pinepg.in/api/PG/v2
```

Shown below is a sample request and sample response for a Inquiry API.

```text Sample Request
ppc_DIA_SECRET=DECF2D9D903BACAF85DA88B5686BC0FB6AB7681673E99191C86B4DC78C27277F&ppc_
DIA_SECRET_TYPE=SHA256&ppc_MerchantAccessCode=58ad283b-7c93-4f19-b072- b17e8ecfb20e&ppc_MerchantID=2415&ppc_TransactionType=3&ppc_UniqueMerchantTxnID=100000000000007687
```
```json Sample Response
{
  "ppc_MerchantID": "279082",
  "ppc_MerchantAccessCode": "cfd05c0c-39f1-4232-bd6f-6d3a8608e1be",
  "ppc_PinePGTxnStatus": "7",
  "ppc_TransactionCompletionDateTime": "17/07/2024 12:41:54 PM",
  "ppc_UniqueMerchantTxnID": "testingedgeseamless1123145432",
  "ppc_Amount": "100",
  "ppc_TxnResponseCode": "1",
  "ppc_TxnResponseMessage": "SUCCESS",
  "ppc_PinePGTransactionID": "342048376",
  "ppc_CapturedAmount": "100",
  "ppc_RefundedAmount": "0",
  "ppc_AcquirerName": "KOTAK_SETU",
  "ppc_DIA_SECRET": "9FFA2E99D14B6357E50D9AF2CF9D01D67B03FA1020BB88A82E76C962313FC004",
  "ppc_DIA_SECRET_TYPE": "SHA256",
  "ppc_PaymentMode": "10",
  "ppc_Parent_TxnStatus": "4",
  "ppc_ParentTxnResponseCode": "1",
  "ppc_ParentTxnResponseMessage": "SUCCESS",
  "ppc_UdfField1": "",
  "ppc_UdfField2": "",
  "ppc_UdfField3": "",
  "ppc_UdfField4": "",
  "ppc_RRN": "1721200204930238149",
  "ppc_AcquirerResponseCode": "SUCCESS",
  "ppc_AcquirerResponseMessage": "SUCCESS"
}
```
