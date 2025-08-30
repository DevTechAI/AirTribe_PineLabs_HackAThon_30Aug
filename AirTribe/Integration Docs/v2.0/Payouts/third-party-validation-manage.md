---
title: "Manage Third Party Validation"
slug: "third-party-validation-manage"
excerpt: "Learn how you can manage payments using Plural APIs."
hidden: true
createdAt: "Fri Jul 05 2024 07:37:19 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 27 2024 16:31:15 GMT+0000 (Coordinated Universal Time)"
---
Listed below are the various options available to manage your TPV payments.

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

```text HashMap Payload
ppc_MerchantAccessCode=cfd05c0c-39f1-4232-bd6f-6d3a8608e1be&ppc_MerchantID=279082&ppc_TransactionType=3&ppc_UniqueMerchantTxnID=testingedgeseamless1123145432
```

> 📘 Note:
> 
> - The HashMap payload is sorted alphabetically by the key names. Please ensure you use the same order of key-value pairs as provided in the payload to generate a HashMap secret.

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

### 2. Refund

A Refund request allows you to initiate a refund for a specific transactions.

As a pre-requisite you must generate the HashMap secret key to pass against the `ppc_DIA_SECRET` parameter of the Refund request.

Follow the below steps to generate a HashMap secret key.

1. Use the `&` separated payload format provided below to enter the transaction details you wish to Refund.

```text HashMap Payload
ppc_Amount=100&ppc_CurrencyCode=356&ppc_MerchantAccessCode=bcf441be-411b-46a1-aa88-c6e852a7d68c&ppc_MerchantID=106600&ppc_PinePGTransactionID=14709745&ppc_TransactionType=10&ppc_UniqueMerchantTxnID=refund%20test
```

> 📘 Note:
> 
> The sample payload is sorted alphabetically by the key names. Please ensure you use the same order of key-value pairs as provided in the payload to generate a HashMap secret..

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

Refer to our <a href="https://developer.pluralonline.com/v2.0/reference/tpv-inquiry-refund" target="_blank">Inquiry/Refund API Documentation</a> for more information.
