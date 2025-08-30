---
title: "Integration Flow"
slug: "plural-hosted-checkout-integration-flow"
excerpt: "Learn how you can integrate with Plural APIs to start accepting payments on Plural hosted checkout."
hidden: false
createdAt: "Thu Jun 27 2024 06:16:07 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Apr 08 2025 11:13:22 GMT+0000 (Coordinated Universal Time)"
---
The figure below shows the steps you need to follow to integrate with Plural hosted checkout APIs in your application.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8c5a388884d885e21d82a63a48985b703ed0d9cafa90770db44420afee5bb0aa-Group_83.png",
        "",
        "Figure: Redirect Checkout Integration Flow"
      ],
      "align": "center",
      "caption": "**Figure**: Plural Hosted Checkout Integration Flow"
    }
  ]
}
[/block]


## 1. **Prerequisite**

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
    "navigation_mode": "2",
    "payment_mode": "1,3,4,19,10,11,14",
    "transaction_type": "1",
    "time_stamp": 157588000000
  },
  "customer_data": {
    "email_id": "kevin.bob@example.com",
    "first_name": "Kevin",
    "last_name": "Bob",
    "customer_id": "123456",
    "mobile_no": "9876543210",
    "billing_data": {
      "address1": "Chruch street",
      "address2": "Brigade road",
      "address3": "",
      "pincode": "560018",
      "city": "Bangalore",
      "state": "Karnataka",
      "country": "India"
    },
    "shipping_data": {
      "address1": "Chruch street",
      "address2": "Brigade road",
      "address3": "",
      "pincode": "560018",
      "city": "Bangalore",
      "state": "Karnataka",
      "country": "India"
    }
  },
  "udf_data": {
    "udf_field_1": "Eecltronic purchase order",
    "udf_field_2": "",
    "udf_field_3": "",
    "udf_field_4": ""
  },
  "product_details": [
    {
      "product_code": "7803",
      "product_amount": "1000"
    }
  ]
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
    "0-3": "An object that contains the merchant details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/docs/plural-hosted-checkout-integration-flow#merchant-data-child-object\" target =\"_blank\">Learn more about our `merchant_data` child object</a>.",
    "1-0": "payment_data",
    "1-1": "`object`",
    "1-2": "`M`",
    "1-3": "An object that contains the payment details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/docs/plural-hosted-checkout-integration-flow#payment-data-child-object\" target =\"_blank\">Learn more about our `payment_data` child object</a>.",
    "2-0": "txn_data",
    "2-1": "`object`",
    "2-2": "`M`",
    "2-3": "An object that contains the transaction details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/docs/plural-hosted-checkout-integration-flow#txn-data-child-object\" target =\"_blank\">Learn more about our `txn_data` child object</a>.",
    "3-0": "customer_data",
    "3-1": "`object`",
    "3-2": "`O`",
    "3-3": "An object that contains the customer details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/docs/plural-hosted-checkout-integration-flow#customer-data-child-object\" target =\"_blank\">Learn more about our `customer_data` child object</a>.",
    "4-0": "udf_data",
    "4-1": "`object`",
    "4-2": "`O`",
    "4-3": "An object that contains the user defined details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/docs/plural-hosted-checkout-integration-flow#udf-data-child-object\" target =\"_blank\">Learn more about our `udf_data` child object</a>.",
    "5-0": "`product_details`",
    "5-1": "`array of object`",
    "5-2": "`O`",
    "5-3": "An object that contains the array of product details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/docs/plural-hosted-checkout-integration-flow#product-details-child-object\" target =\"_blank\">Learn more about our `product_details` child object</a>."
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
    "3-3": "Merchant return URL.  \n  \nExample: `https://www.pinelabs.com`  \n  \n**Note**: Your customer's are redirected to this page after the successful payment."
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
    "0-3": "Checkout navigation mode.  \n  \nExample: `2`  \n  \nAccepted values:<ul><li>`2`: For Redirect Checkout.</li><li>`7`: For Seamless Checkout.</ul></li>",
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
    "3-3": "Unique identifier of the customer in Plural database.  \n  \nExample: `123456`",
    "4-0": "mobile_no",
    "4-1": "`string`",
    "4-2": "`O`",
    "4-3": "Customer's mobile number.  \n  \nExample: `9876543210`",
    "5-0": "billing_data",
    "5-1": "`object`",
    "5-2": "`O`",
    "5-3": "An object that contains the billing details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/docs/plural-hosted-checkout-integration-flow#billing-data-child-object\" target =\"_blank\">Learn more about our `billing_data` child object</a>.",
    "6-0": "shipping_data",
    "6-1": "`object`",
    "6-2": "`O`",
    "6-3": "An object that contains the shipping details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/docs/plural-hosted-checkout-integration-flow#shipping-data-child-object\" target =\"_blank\">Learn more about our `shipping_data` child object</a>."
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
    "3-3": "Pincode of the billing address.  \n  \nExample: `560001`",
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
    "3-3": "Pincode of the shipping address.  \n  \nExample: `560001`",
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
    "0-3": "User defined value1.  \n  \nExample: `Purchase`",
    "1-0": "udf_field_2",
    "1-1": "`string`",
    "1-2": "`O`",
    "1-3": "User defined value2  \n  \nExample: `Purchase`",
    "2-0": "udf_field_3",
    "2-1": "`string`",
    "2-2": "`O`",
    "2-3": "User defined value3.  \n  \nExample: `Purchase`",
    "3-0": "udf_field_4",
    "3-1": "`string`",
    "3-2": "`O`",
    "3-3": "User defined value4.  \n  \nExample: `Purchase`"
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

3. **HashMap**: Generate HashMap using the Base64 Encode and the secret key. Use the below sample code to handle the generation of HashMap using SHA-256.

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

## 2. Accept Payment

Use our accept payment API to generate the Plural hosted checkout link. Additionally, you need to pass the HashMap generated as the authorization header and the Base64 Encode in the request body of this API.

Use the below endpoint to Accept payment.

```text Accept Payment UAT Endpoint
POST: https://uat.pinepg.in/api/v2/accept/payment
```
```text Accept Payment PROD Endpoint
POST: https://pinepg.in/api/v2/accept/payment
```

### Headers

You are required to pass this header in our Accept Payment API.

| Key        | Value                                                                   |
| :--------- | :---------------------------------------------------------------------- |
| `X-VERIFY` | Use the generated HashMap, we use this to authenticate the API request. |

Shown below is a sample request and sample response for a Accept Payment API.

```json Sample Request
{
  "request": "ewogICJtZXJjaGFudF9kYXRhIjogewogICAgIm1lcmNoYW50X2lkIjogMTA4NTA2LAogICAgIm1lcmNoYW50X2FjY2Vzc19jb2RlIjogIjRhOGM0MjJkLTkyOGMtNGY4My1iZmU4LTI3YTA5YWY2NjY0NyIsCiAgICAidW5pcXVlX21lcmNoYW50X3R4bl9pZCI6ICJYWVoxMjMiLAogICAgIm1lcmNoYW50X3JldHVybl91cmwiOiAiaHR0cDovLzE5Mi4xNjguMTAxLjkzOjcwNTAvQ2hhcmdpbmdSZXNwLmFzcHgiCiAgfSwKICAicGF5bWVudF9kYXRhIjogewogICAgImFtb3VudF9pbl9wYWlzYSI6IDgwMAogIH0sCiAgInR4bl9kYXRhIjogewogICAgIm5hdmlnYXRpb25fbW9kZSI6ICIyIiwKICAgICJwYXltZW50X21vZGUiOiAiMSwzLDQsMTksMTAsMTEsMTQiLAogICAgInRyYW5zYWN0aW9uX3R5cGUiOiAiMSIsCiAgICAidGltZV9zdGFtcCI6IDE1NzU4ODAwMDAwMAogIH0KfQ=="
}
```
```json Sample Response
{
    "token": "S01NF8ntxnKu9E%2faXLt7ELcFH7NpfstrSj4jCTV91GHOvQ%3d",
    "redirect_url": "https://pinepg.in/pinepg/v2/process/payment?token=S01NF8ntxnKu9E%2faXLt7ELcFH7NpfstrSj4jCTV91GHOvQ%3d",
    "response_code": 1,
    "response_message": "SUCCESS"
}
```

Refer to our Accept Payment API documentation for more information.

## 3. Handle Payment

Use the generated link returned in our accept payment API to redirect your customers to the plural hosted checkout page to accept payment. After successful payment we redirect your customers to your website.

> 📘 Note:
> 
> - On successful payment we send the webhook event `payment.captured` and the status of the payment is updated to `SUCCESS`.

### 3.1 Store Payment Details

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

### 3.2 Verify Payment Signature

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
> Webhooks are asynchronous, so for time-sensitive actions, we recommend polling our Inquiry API.

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
