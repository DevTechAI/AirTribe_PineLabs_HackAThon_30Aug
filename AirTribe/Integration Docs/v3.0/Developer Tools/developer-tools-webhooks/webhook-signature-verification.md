---
title: "Signature Verification"
slug: "webhook-signature-verification"
excerpt: "Learn how to ensure the webhook payload received is sent by Plural."
hidden: false
createdAt: "Fri Sep 27 2024 08:50:08 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Oct 28 2024 06:18:01 GMT+0000 (Coordinated Universal Time)"
---
Webhook signature verification is a critical security measure to protect your system from unauthorized access, data tampering, and other potential threats.

We include a signature that you can use to verify that the webhook payload you receive is legitimate and sent by us. The signature is sent against the `webhook-signature` parameter in the header in all the webhook events.

## Verify Signature

Follow the below steps to verify the webhook signature.

1. All the webhook events sent from Plural include these three header information along with the body which are used for verification.
   1. `webhook-id`: A unique identifier of the webhook event. This remains the same when the webhook is resent and this can be ignored.
   2. `webhook-timestamp`: The unix timestamp (in seconds) when the webhook event was triggered.
   3. `webhook-signature`: Base64 encoded webhook signature.
2. Use the `webhook_id`, `webhook_timestamp`, `body`, and `secret_key` to generate a signature.

> 📘 Note
> 
> - Where `body` is the raw response body of a webhook event. Ensure that the webhook body remains unparsed.
> - `secret_key`: You can find your secret key under settings on the <a href="https://dashboardv2.pluralonline.com/login" target="_blank">Plural dashboard</a>.
> - Implementing webhook signature verification is mandatory.

3. You can use the sample code below to generate a signature and encode it to Base64.

```java Java
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;
public class Main {
  public static void main(String[] args) {
    String webhook_id = "<webhook_id>"; // Replace with actual webhook_id
    String webhook_timestamp = "<webhook_timestamp>"; // Replace with actual webhook_timestamp
    String body = "<body>"; // Replace with actual body

    String signedContent = webhook_id + "." + webhook_timestamp + "." + body;
    String secret = "<secret_key>"; // Replace with actual secret key

    // Need to base64 decode the secret
    byte[] secretBytes = Base64.getDecoder().decode(secret);
    String signature = "";

    try {
      Mac mac = Mac.getInstance("HmacSHA256");
      SecretKeySpec secretKeySpec = new SecretKeySpec(secretBytes, "HmacSHA256");
      mac.init(secretKeySpec);
      byte[] hmacBytes = mac.doFinal(signedContent.getBytes(StandardCharsets.UTF_8));
      signature = Base64.getEncoder().encodeToString(hmacBytes);
    } catch (Exception e) {
      e.printStackTrace();
    }

    System.out.println(signature);
  }
}
```

4. Next, compare the generated signature with the header `webhook_signature`.
5. To compare the signatures it's recommended to use a constant-time string comparison method in order to prevent timing attacks.
6. Additionally, you can also compare the webhook timestamp against your system timestamp to ensure it's within your acceptable time range.

> 📘 Note:
> 
> By comparing the generated signature with the one provided, you can verify that the webhook was sent by Plural and that the data remained intact during transmission.

### Example:

The example below illustrates the webhook signature verification process clearly and provides a step-by-step guide for a better understanding.

1. **Merchant Secret Key**: The merchant has a secret key, abc1234. Before using this key for signature verification, we need to encode it to Base64, which results in: `YWJjMTIzNA==`
2. **Webhook Event**: A webhook event is received with the following details:
   1. webhook-id: `msg_2nEfCaUDn9fynC9Kz2upo1QSydl`
   2. webhook-timestamp: `1728543028`
   3. webhook-signature: `v1,Ns46HrH+Nfu9dZtBUVvSLyrOD5JH0SAGlNo3M5yobfQ=`
3. **Signature Verification**: To verify the authenticity of this webhook, we need to recreate the signature using the webhook-id, webhook-timestamp, and the request body.
   1. First, combine the webhook-id, webhook-timestamp, and the body into a single string (signed content):
   2. Now, use the Base64 decoded secret (YWJjMTIzNA==) as the key to generate the HMAC SHA-256 signature over the signed content. The code provided performs this operation.

```kotlin
fun main() {
    val webhookId = "msg_2nEfCaUDn9fynC9Kz2upo1QSydl"
    val webhookTimestamp = "1728543028"
    val body = "{\"payload\":\"payload\"}"
 
    val signedContent = "$webhookId.$webhookTimestamp.$body"
    val secret = "YWJjMTIzNA=="
 
    // Base64 decode the secret
    val secretBytes = Base64.getDecoder().decode(secret)
    var signature = ""
 
    try {
        val mac = Mac.getInstance("HmacSHA256")
        val secretKeySpec = SecretKeySpec(secretBytes, "HmacSHA256")
        mac.init(secretKeySpec)
        val hmacBytes = mac.doFinal(signedContent.toByteArray(StandardCharsets.UTF_8))
        signature = Base64.getEncoder().encodeToString(hmacBytes)
    } catch (e: Exception) {
        e.printStackTrace()
    }
 
    println(signature)
}
```

The output of this code will generate the following signature: `Ns46HrH+Nfu9dZtBUVvSLyrOD5JH0SAGlNo3M5yobfQ=`

4. **Webhook Signature Validation**: The received webhook signature starts with the prefix v1, indicating the version of the signature algorithm. In this case, the v1 prefix is followed by the signature: `Ns46HrH+Nfu9dZtBUVvSLyrOD5JH0SAGlNo3M5yobfQ=` By matching the generated signature with the part of the received signature after prefix v1, we confirm that the webhook is authentic. The webhook has been securely sent from Plural.
