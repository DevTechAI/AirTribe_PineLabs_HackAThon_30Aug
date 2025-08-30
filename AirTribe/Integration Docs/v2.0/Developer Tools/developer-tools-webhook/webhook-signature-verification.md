---
title: "Signature Verification"
slug: "webhook-signature-verification"
excerpt: "Learn how to ensure the webhook payload received is sent by Plural."
hidden: false
createdAt: "Tue Sep 17 2024 09:59:12 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 20 2024 09:24:53 GMT+0000 (Coordinated Universal Time)"
---
Webhook signature verification is a critical security measure to protect your system from unauthorized access, data tampering, and other potential threats.

We include a signature that you can use to verify that the webhook payload you receive is legitimate and sent by us. The signature is sent against the `X-verify` parameter in the header in all the webhook events.

## Verify Signature

Follow the below steps to verify the webhook signature.

1. Generate a signature on your backend server using the webhook event's payload and the SHA256 algorithm. A sample webhook event is shown below.

```json Sample Payload
{
  "event_name": "payment.captured",
  "merchant_response": {
    "merchant_id": "113484",
    "merchant_access_code": "7f532770-f8a7-46f8-a463-182727a29350",
    "unique_merchant_txn_id": "104943038807791693",
    "pine_pg_txn_status": "4",
    "txn_completion_date_time": "29/11/2023 12:18:49 PM",
    "amount_in_paisa": "20000",
    "txn_response_code": "1",
    "txn_response_msg": "SUCCESS",
    "acquirer_name": "HDFC",
    "pine_pg_transaction_id": "7831007",
    "captured_amount_in_paisa": "20188",
    "refund_amount_in_paisa": "0",
    "payment_mode": "CREDIT_DEBIT_CARD",
    "parent_txn_status": "",
    "parent_txn_response_code": "",
    "parent_txn_response_message": "",
    "masked_card_number": "************1112",
    "card_holder_name": "mojiz",
    "salted_card_hash": "B6B6A7CE1E6E2AA0DD7C028385446A3BBADCEE026A283859C69F5D2B8CC645AD",
    "rrn": "425847096720",
    "auth_code": "999999"
  }
}
```

2. Remove spaces from the above sample payload.

```json Sample Payload Without Spaces
{"event_name":"payment.captured","merchant_response":{"merchant_id": "113484","merchant_access_code":"7f532770-f8a7-46f8-a463-182727a29350","unique_merchant_txn_id":"104943038807791693","pine_pg_txn_status":"4","txn_completion_date_time":"29/11/2023 12:18:49 PM","amount_in_paisa":"20000","txn_response_code":"1","txn_response_msg":"SUCCESS","acquirer_name":"HDFC","pine_pg_transaction_id":"7831007","captured_amount_in_paisa":"20188","refund_amount_in_paisa":"0","payment_mode":"CREDIT_DEBIT_CARD","parent_txn_status":"","parent_txn_response_code":"","parent_txn_response_message":"","masked_card_number":"************1112","card_holder_name":"mojiz","salted_card_hash":"B6B6A7CE1E6E2AA0DD7C028385446A3BBADCEE026A283859C69F5D2B8CC645AD","rrn":"425847096720","auth_code": "999999"}}
```

3. Convert the payload to a Base64 encoding.

```Text Base64 Encode
eyJldmVudF9uYW1lIjoicGF5bWVudC5jYXB0dXJlZCIsIm1lcmNoYW50X3Jlc3BvbnNlIjp7Im1lcmNoYW50X2lkIjogIjExMzQ4NCIsIm1lcmNoYW50X2FjY2Vzc19jb2RlIjoiN2Y1MzI3NzAtZjhhNy00NmY4LWE0NjMtMTgyNzI3YTI5MzUwIiwidW5pcXVlX21lcmNoYW50X3R4bl9pZCI6IjEwNDk0MzAzODgwNzc5MTY5MyIsInBpbmVfcGdfdHhuX3N0YXR1cyI6IjQiLCJ0eG5fY29tcGxldGlvbl9kYXRlX3RpbWUiOiIyOS8xMS8yMDIzIDEyOjE4OjQ5IFBNIiwiYW1vdW50X2luX3BhaXNhIjoiMjAwMDAiLCJ0eG5fcmVzcG9uc2VfY29kZSI6IjEiLCJ0eG5fcmVzcG9uc2VfbXNnIjoiU1VDQ0VTUyIsImFjcXVpcmVyX25hbWUiOiJIREZDIiwicGluZV9wZ190cmFuc2FjdGlvbl9pZCI6Ijc4MzEwMDciLCJjYXB0dXJlZF9hbW91bnRfaW5fcGFpc2EiOiIyMDE4OCIsInJlZnVuZF9hbW91bnRfaW5fcGFpc2EiOiIwIiwicGF5bWVudF9tb2RlIjoiQ1JFRElUX0RFQklUX0NBUkQiLCJwYXJlbnRfdHhuX3N0YXR1cyI6IiIsInBhcmVudF90eG5fcmVzcG9uc2VfY29kZSI6IiIsInBhcmVudF90eG5fcmVzcG9uc2VfbWVzc2FnZSI6IiIsIm1hc2tlZF9jYXJkX251bWJlciI6IioqKioqKioqKioqKjExMTIiLCJjYXJkX2hvbGRlcl9uYW1lIjoibW9qaXoiLCJzYWx0ZWRfY2FyZF9oYXNoIjoiQjZCNkE3Q0UxRTZFMkFBMEREN0MwMjgzODU0NDZBM0JCQURDRUUwMjZBMjgzODU5QzY5RjVEMkI4Q0M2NDVBRCIsInJybiI6IjQyNTg0NzA5NjcyMCIsImF1dGhfY29kZSI6ICI5OTk5OTkifX0=
```

4. Use the below sample code to generate a HashMap signature using the SHA-256 algorithm.

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

5. Finally, compare the generated signature with the `X-verify` header.

> 📘 Note:
> 
> - By comparing the generated signature with the one provided, you can verify that the webhook was sent by Plural and that the data remained intact during transmission.
