---
title: "Integration Steps"
slug: "iframe-integration-steps"
excerpt: "Learn how to integrate the Plural payment gateway on your website with an embedded iFrame setup."
hidden: false
createdAt: "Mon Nov 04 2024 07:13:43 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Mar 24 2025 10:16:14 GMT+0000 (Coordinated Universal Time)"
---
Follow the below steps to integrate with Plural payment gateway using iFrame setup.

1. <a href="https://developer.pluralonline.com/docs/iframe-integration-steps#1-prerequisite-generate-token" >\[Prerequisite] Generate Token</a>
2. <a href="https://developer.pluralonline.com/docs/iframe-integration-steps#2-create-checkout" >Create Checkout</a>
3. <a href="https://developer.pluralonline.com/docs/iframe-integration-steps#3-integrate-with-checkout-on-client-side" >Integrate with Checkout on Client Side</a>
4. <a href="https://developer.pluralonline.com/docs/iframe-integration-steps#4-handle-transaction-response" >Handle Transaction Response</a>
   1. <a href="https://developer.pluralonline.com/docs/iframe-integration-steps#41-store-payment-details-on-your-server" >Handle Payment Success and Failure</a>
   2. <a href="https://developer.pluralonline.com/docs/iframe-integration-steps#42-verify-payment-signature" >Verify Payment Signature</a>

> 📘 Note
> 
> - Ensure you store your Client ID and Secret in your Backend securely.
> - Integrate our APIs on your backend system.
> - We strictly recommend not to call our APIs from the frontend.

## 1. [Prerequisite] Generate Token

Integrate our Generate Token API in your backend servers to generate the access token. Use the token generated to authenticate Plural APIs.

Below are the sample requests and response for the Generate Token API.

```curl cURL – UAT
curl --request POST \
--url https://pluraluat.v2.pinepg.in/api/auth/v1/token \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--data '
{
  "client_id": "a17ce30e-f88e-4f81-ada1-c3b4909ed232",
  "client_secret": "fgwei7egyhuggwp39w8rh",
  "grant_type": "client_credentials"
}
'
```
```curl cURL – PROD
curl --request POST \
--url https://api.pluralpay.in/api/auth/v1/token \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--data '
{
  "client_id": "a17ce30e-f88e-4f81-ada1-c3b4909ed232",
  "client_secret": "fgwei7egyhuggwp39w8rh",
  "grant_type": "client_credentials"
}
'
```
```json Sample Response
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
  "expires_in": 3600
}
```

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/v3.0/reference/generate-token" target="_blank">Generate Token API</a> documentation to learn more.

## 2. Create Checkout Link

Use this API to generate a checkout Link. Include the access token in the request headers for Bearer Authentication.

Below are the sample requests and response for a Create Checkout API.

```curl cURL - UAT
curl --request POST \
--url https://pluraluat.v2.pinepg.in/api/checkout/v1/orders \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
--header 'Content-Type: application/json' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'accept: application/json' \
--data '
{
  "merchant_order_reference":112345171,
  "order_amount":{
    "value":500,
    "currency":"INR"
  },
  "integration_mode":"IFRAME",
  "pre_auth":false,
  "allowed_payment_methods":[
    "CARD",
    "UPI",
    "NETBANKING",
    "POINTS",
    "WALLET"
  ],
  "notes":"order1",
  "callback_url":"https://sample-callback-url",
  "failure_callback_url": "https://sample-failure-callback-url",
  "purchase_details":{
    "customer":{
      "email_id":"kevin.bob@example.com",
      "first_name":"Kevin",
      "last_name":"Bob",
      "customer_id":"192212",
      "mobile_number":"9876543210",
      "billing_address":{
        "address1":"H.No 15, Sector 17",
        "address2":"",
        "address3":"",
        "pincode":"61232112",
        "city":"CHANDIGARH",
        "state":"PUNJAB",
        "country":"INDIA"
      },
      "shipping_address":{
        "address1":"H.No 15, Sector 17",
        "address2":"",
        "address3":"",
        "pincode":"144001123",
        "city":"CHANDIGARH",
        "state":"PUNJAB",
        "country":"INDIA"
      }
    },
    "merchant_metadata":{
      "key1":"DD",
      "key2":"XOF"
    }
  }
}
'
```
```curl cURL - PROD
curl --request POST \
--url https://api.pluralpay.in/api/checkout/v1/orders \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
--header 'Content-Type: application/json' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'accept: application/json' \
--data '
{
  "merchant_order_reference":112345171,
  "order_amount":{
    "value":500,
    "currency":"INR"
  },
  "integration_mode":"IFRAME",
  "pre_auth":false,
  "allowed_payment_methods":[
    "CARD",
    "UPI",
    "NETBANKING",
    "POINTS",
    "WALLET"
  ],
  "notes":"order1",
  "callback_url":"https://sample-callback-url",
  "failure_callback_url": "https://sample-failure-callback-url",
  "purchase_details":{
    "customer":{
      "email_id":"kevin.bob@example.com",
      "first_name":"Kevin",
      "last_name":"Bob",
      "customer_id":"192212",
      "mobile_number":"9876543210",
      "billing_address":{
        "address1":"H.No 15, Sector 17",
        "address2":"",
        "address3":"",
        "pincode":"61232112",
        "city":"CHANDIGARH",
        "state":"PUNJAB",
        "country":"INDIA"
      },
      "shipping_address":{
        "address1":"H.No 15, Sector 17",
        "address2":"",
        "address3":"",
        "pincode":"144001123",
        "city":"CHANDIGARH",
        "state":"PUNJAB",
        "country":"INDIA"
      }
    },
    "merchant_metadata":{
      "key1":"DD",
      "key2":"XOF"
    }
  }
}
'
```
```json Sample Response
{
  "token": "<<Redirect Token>>",
  "order_id": "<<Order ID>>",
  "redirect_url": "https://api.pluralonline.com/api/v3/checkout-bff/redirect/checkout?token=<<Redirect Token>>",
  "response_code": 200,
  "response_message": "Order Creation Successful."
}
```

> ❗️ Watch OUT
> 
> The parameter `"integration_mode": "IFRAME"` is mandatory to render the iframe checkout.

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/payments-test-card-details" target="_blank">Test Card Details</a> documentation to learn more.

## 3. Integrate with Checkout on Client Side

To integrate with iFrame checkout on Client Side use the below code.

```javascript JS Checkout Code
<html>
<button id="pay_button">Pay</button>
<script src="https://checkout-staging.pluralonline.com/v3/web-sdk-checkout.js"></script>
<script>
function handleCheckout(redirectUrl) {
  const options = {
    redirectUrl,
    successHandler: async function (response) {
      console.log(response);
    },
    failedHandler: async function (response) {
        console.log(response);
    },
  };

  const plural = new Plural(options);
  plural.open(options);
}

document.getElementById("pay_button").onclick = function(e){
    handleCheckout("https://api-staging.pluralonline.com/api/v3/checkout-bff/redirect/checkout?token=V3_N7fMbGAfE8xDtTMLptiWhWL%2Fgz7bv0aBUuFRH5NlzAPYpii%2BcRyvm1xllb8TP5JG"); // Pass `redirect_url` returned in our Create Checkout API response.
}
</script>
</html>
```

**Configuration Object**:

<details>

<summary>To View Click Here</summary>

Defines a configuration object labeled as `options` that contains key settings listed below:

- **redirectUrl**: Use this key to pass the `redirect_url` returned in our Create Checkout API response.
- **successHandler**: Handler functions are asynchronous, where you can customize handlers according to your specific needs.
- **failureHandler**: Handler functions are asynchronous, allowing you to add handlers to notify users as required based on specific requirements.

</details>

## 4. Handle Transaction Response

You can add custom handler logic to manage specific actions or events within the `successHandler`and `failureHandler` function to enhance responsiveness. It is essential to handle both `successHandler` and `failureHandler` functions and signature verification.

### 4.1 Handle Payment Success and Failure

On a successful and failed payment we return the following parameters listed below.

```json Success Response
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "status": "AUTHORIZED",
  "signature": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
}
```
```json Failure Response
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "status": "FAILED",
  "signature": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
}
```

- We recommend you to collect the payment details and send them to your server.
- You must validate the authenticity of the payment details returned. You can authenticate by verifying the signature.

### 4.2 Verify Payment Signature

Ensure you follow this as a mandatory step to verify the authenticity of the details returned to the checkout form for successful payments.

Follow the below steps to verify the signature.

1. Create a signature on your server using the following parameters using the SHA256 algorithm.
   1. `order_id`: Unique Identifier generated for an order request on Plural database.
   2. `status`: Payment status.
   3. `secret_key`: The Onboarding team has provided you with this information as part of the onboarding process.

Use the below sample code to construct HashMap signature using the SHA256 algorithm.

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

> 📘 Note:
> 
> To create a request string, format the key-value pairs of data returned to the return URL. The pairs are separated by `&` and arranged in ascending order based on a lexicographical comparison of the keys.

Shown below is a example to create a request string.

```text Success
"key1=value1&key2=value2", ["order_id=random_order_id&status=AUTHORIZED"]
```
```text Failed
"key1=value1&key2=value2&key3=value3&key4=value4", ["error_code=USER_AUTHENTICATION_FAILED&error_message=Consumer Authentication required&order_id=<order_id>&status=FAILED"]
```

2. If the signature generated on your server matches the Plural signature returned, it confirms that the payment details are from Plural.

### To Know Your Payment Status

To check your payment status, you can either rely on Webhook events or use our **Get Orders** APIs for real-time updates.

1. **Webhook Notification**: We send Webhook notifications on the successful payment or any changes to the payments object. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/developer-tools-webhook" target="_blank">Webhooks</a> documentation to learn more.
2. **Get Orders API**: Use our Get Orders API to know the real time status of the payment. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/order-manage#3-get-order-by-order-id" target="_blank">Manage Orders</a> documentation to learn more.

### Refunds

Plural processes refund directly to the customer's original payment method to prevent chargebacks.

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/payment-refund" target="_blank">Refunds</a> documentation to learn more.
