---
title: "Manage Payments"
slug: "manage-payments"
excerpt: "Learn how you can manage payments using Plural APIs."
hidden: false
createdAt: "Wed Aug 28 2024 11:23:46 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Jan 23 2025 06:32:51 GMT+0000 (Coordinated Universal Time)"
---
Listed below are the various options available to manage your payments.

1. **Inquiry**: Use this request to know the payment statuses.
2. **Refund**: Use this request to refund the payment.

Use the below endpoint to handle both Inquiry and Refund operations. The type of operation is identified by the content of the request body.

```text Inquiry/Refund UAT Endpoint
POST: https://uat.pinepg.in/api/PG/v2
```
```text Inquiry/Refund Prod Endpoint
POST: https://pinepg.in/api/PG/v2
```

## Request Headers

- **Content-Type**: `application/x-www-form-urlencoded`

## Operations

### 1. Inquiry

An Inquiry request allows you to retrieve the status or details of a specific transaction.

As a pre-requisite you must generate the HashMap secret key to pass against the `ppc_DIA_SECRET` parameter of the Inquiry API request.

Follow the below steps to generate a HashMap secret key.

1. Use the `&` separated payload format provided below to enter the transaction details you wish to Inquire about.

```text Request Payload
ppc_MerchantAccessCode=cfd05c0c-39f1-4232-bd6f-6d3a8608e1be&ppc_MerchantID=279082&ppc_TransactionType=3&ppc_UniqueMerchantTxnID=testingedgeseamless1123145432
```

#### Request Payload Parameters

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
    "0-0": "ppc_MerchantAccessCode",
    "0-1": "`string`",
    "0-2": "`M`",
    "0-3": "Unique access code of the merchant in Plural database.  \n  \nExample: `1a39a6d4-46b7-124d-929d-21bf0e9ed123`",
    "1-0": "ppc_MerchantID",
    "1-1": "`string`",
    "1-2": "`M`",
    "1-3": "Unique identifier of the merchant in the Plural database.  \n  \nExample: `123456`",
    "2-0": "ppc_TransactionType",
    "2-1": "`string`",
    "2-2": "`M`",
    "2-3": "The type of operation.  \n  \nAccepted values:<ul><li>`3`: For Inquiry.</li><li> `10`: For Refund.</ul></li>",
    "3-0": "ppc_UniqueMerchantTxnID",
    "3-1": "`string`",
    "3-2": "`M`",
    "3-3": "Unique merchant transaction ID.  \n  \nExample: 1234567890  \n  \n**Note**: You must enter the transaction ID passed in the accept payment API request."
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


</details>

> 📘 Note:
> 
> - The Request payload is sorted alphabetically by the key names. 
> - Please ensure you use the same order of key-value pairs as provided in the payload to generate a HashMap secret.

2. Use the sample code provided below to generate a SHA256 HashMap.
3. In the sample code use the request payload with updated transaction details along with your secret key to generate a SHA256 Hash.

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
        String responseBody = "<HashMap_payload>";
        String signingSecret = "<Secret_key>";

        String requestSignature = SignatureGenerator.jsonHash(responseBody,signingSecret);
        System.out.println(requestSignature);
    }
}
```

4. Use the generate HashMap secret against the `ppc_DIA_SECRET` in the Inquiry request.

Shown below is a sample request and sample response for a Inquiry Request.

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

Refer to our <a href="https://developer.pluralonline.com/v2.0/reference/payment-inquiry" target="_blank">Inquiry API Documentation</a> for more information.

### 2. Refund

A Refund request allows you to initiate a refund for a specific transaction.

As a pre-requisite you must generate the HashMap secret key to pass against the `ppc_DIA_SECRET` parameter of the Refund request.

Follow the below steps to generate a HashMap secret key.

1. Use the `&` separated payload format provided below to enter the transaction details you wish to Refund.

```text HashMap Payload
ppc_Amount=100&ppc_CurrencyCode=356&ppc_MerchantAccessCode=bcf441be-411b-46a1-aa88-c6e852a7d68c&ppc_MerchantID=106600&ppc_PinePGTransactionID=14709745&ppc_TransactionType=10&ppc_UniqueMerchantTxnID=refund%20test
```

#### Request Payload Parameters

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
    "0-0": "ppc_Amount",
    "0-1": "`string`",
    "0-2": "`M`",
    "0-3": "The total amount to be refunded.  \n  \nExample: `10000`",
    "1-0": "ppc_CurrencyCode",
    "1-1": "`string`",
    "1-2": "`M`",
    "1-3": "The currency code of the amount to be refunded.  \n  \nExample: `356`: For INR.",
    "2-0": "ppc_MerchantAccessCode",
    "2-1": "`string`",
    "2-2": "`M`",
    "2-3": "Unique access code of the merchant in Plural database.  \n  \nExample: `1a39a6d4-46b7-124d-929d-21bf0e9ed123`",
    "3-0": "ppc_MerchantID",
    "3-1": "`string`",
    "3-2": "`M`",
    "3-3": "Unique identifier of the merchant in the Plural database.  \n  \nExample: `123456`",
    "4-0": "ppc_PinePGTransactionID",
    "4-1": "`string`",
    "4-2": "`M`",
    "4-3": "Unique transaction ID generated by Plural against an Order ID.  \n  \nExample: `12345`",
    "5-0": "ppc_TransactionType",
    "5-1": "`string`",
    "5-2": "`M`",
    "5-3": "The type of operation.  \n  \nAccepted values:<ul><li>`3`: For Inquiry.</li><li> `10`: For Refund.</ul></li>",
    "6-0": "ppc_UniqueMerchantTxnID",
    "6-1": "`string`",
    "6-2": "`M`",
    "6-3": "Unique merchant transaction ID.  \n  \nExample: 1234567890  \n  \n**Note**: You must enter the transaction ID passed in the accept payment API request."
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


</details>

> 📘 Note:
> 
> The sample payload is sorted alphabetically by the key names. Please ensure you use the same order of key-value pairs as provided in the payload to generate a HashMap secret.

2. Use the sample code provided below to generate a SHA256 Hash.
3. In the sample code use the HashMap payload with updated transaction details along with your secret key to generate a SHA256 Hash.

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
        String responseBody = "<HashMap_payload>";
        String signingSecret = "<Secret_key>";

        String requestSignature = SignatureGenerator.jsonHash(responseBody,signingSecret);
        System.out.println(requestSignature);
    }
}
```

4. Use the generate HashMap secret against the `ppc_DIA_SECRET` in the Refund request.

Shown below is a sample request and sample response for a Refund request.

```text Sample Request
ppc_Amount=10000&ppc_CurrencyCode=356&ppc_DIA_SECRET=1781AE06CAF31A32B79F31B82B140484 DD9C1B95CC0DD26C1CB4F1AE0D13C066&ppc_DIA_SECRET_TYPE=SHA256&ppc_MerchantAccessCode=58 ad283b-7c93-4f19-b072-
b17e8ecfb20e&ppc_MerchantID=2415&ppc_PinePGTransactionID=87943&ppc_TransactionType=10&ppc_UniqueMerchantTxnID
=100000000000007687&ppc_ImeiProductDetails=W3sicHJvZHVjdF9jb2RlIjoiNzgwMyIsImltZWlfbm8iOiI5ODQ4NDg4ODQ0In0sIH sicHJvZHVjdF9jb2RlIjoieGlhb21pX3BybyIsImltZWlfbm8iOiI5ODQ4NDg4Mjg0NSJ9XQ==
```
```json Sample Response
{
  "ppc_MerchantID": "279082",
  "ppc_MerchantAccessCode": "cfd05c0c-39f1-4232-bd6f-6d3a8608e1be",
  "ppc_PinePGTxnStatus": "1",
  "ppc_TransactionCompletionDateTime": "01/08/2024 10:25:07 AM",
  "ppc_UniqueMerchantTxnID": "Refund_1",
  "ppc_Amount": "100",
  "ppc_TxnResponseCode": "2",
  "ppc_TxnResponseMessage": "REFUND PROCESS INITIATED",
  "ppc_PinePGTransactionID": "0",
  "ppc_CapturedAmount": "0",
  "ppc_RefundedAmount": "0",
  "ppc_ParentTxnResponseCode": "1",
  "ppc_Parent_TxnStatus": "4",
  "ppc_ParentTxnResponseMessage": "SUCCESS",
  "ppc_DIA_SECRET": "EE3844A2B85588D20AA173269BCC4F3375ABDEE8631CFF1366B271FABB47AE6F",
  "ppc_DIA_SECRET_TYPE": "SHA256"
}
```

Below are the possible response combinations for an Inquiry and Refund call:

| ppc_Parent_TxnStatus | ppc_ParentTxnResponseCode | Transaction State                                  | Transaction Type                         |
| :------------------- | :------------------------ | :------------------------------------------------- | :--------------------------------------- |
| 4                    | 1                         | Success                                            | Purchase                                 |
| 1                    | \-1                       | Failure                                            | Purchase                                 |
| 1                    | 1                         | Initiated                                          | Purchase                                 |
| 6                    | 1                         | Full Refund Success                                | Full Refund                              |
| 9                    | 1                         | Partial Refund Success                             | Partial Refund                           |
| \-7                  | Anycode                   | Failure - Purchase / Full Refund / Partial  Refund | Purchase / Full Refund / Partial  Refund |

Refer to our <a href="https://developer.pluralonline.com/v2.0/reference/payment-refund" target="_blank">Refund API Documentation</a> for more information.
