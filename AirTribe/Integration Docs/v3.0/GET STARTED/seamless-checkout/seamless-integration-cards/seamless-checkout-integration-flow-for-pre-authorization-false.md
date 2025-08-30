---
title: "Integration Flow When Pre-Authorization False"
slug: "seamless-checkout-integration-flow-for-pre-authorization-false"
excerpt: "Learn how you can integrate with Plural APIs to start accepting payments on your website."
hidden: true
createdAt: "Thu Jul 25 2024 07:36:17 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Dec 23 2024 07:08:16 GMT+0000 (Coordinated Universal Time)"
---
Follow the below steps to integrate with Plural seamless checkout APIs in your application.

## 1. [Prerequisite] Generate Token

Integrate our Generate Token API in your backend servers to generate the access token. Use the token generated to authenticate Plural APIs.

Use the below endpoint to generate a token.

```text Generate Token Endpoint for UAT
POST: POST: https://pluraluat.v2.pinepg.in/api/auth/v1/token
```
```text Generate Token Endpoint for PROD
POST: https://api.pluralpay.in/api/auth/v1/token
```

Below is a sample request and response for the Generate Token API.

```json Sample Request
{
  "client_id": "1234567890",
  "client_secret": "asdfgwei7egyhuggwp39w8rh",
  "grant_type": "client_credentials"
}
```
```json Sample Response
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
  "expires_in": 3600
}
```

Refer to our <a href="https://developer.pluralonline.com/v3.0/reference/generate-token" target="_blank">Generate Token API</a> documentation to learn more.

## 2. Create Order

To create an Order use our Create Order API, for authentication use the generated access token in the headers of the API request.

Use the below endpoint to create an order.

```Text Create Order Endpoint for UAT
POST: https://pluraluat.v2.pinepg.in/api/pay/v1/orders
```
```text Create Order Endpoint for PROD
POST: https://api.pluralpay.in/api/pay/v1/orders
```

Below is a sample request and response for a Create Order API.

```json Sample Request
{
  "merchant_order_reference": 112345,
  "order_amount": {
    "value": 1100,
    "currency": "INR"
  },
  "pre_auth": false,
  "purchase_details": {
    "customer": {
      "email_id": "kevin.bob@example.com",
      "first_name": "Kevin",
      "last_name": "Bob",
      "customer_id": "123456",
      "mobile_number": "9876543210",
      "billing_address": {
        "address1": "10 Downing Street Westminster London",
        "address2": "Oxford Street Westminster London",
        "address3": "Baker Street Westminster London",
        "pincode": "51524036",
        "city": "Westminster",
        "state": "Westminster",
        "country": "London"
      },
      "shipping_address": {
        "address1": "10 Downing Street Westminster London",
        "address2": "Oxford Street Westminster London",
        "address3": "Baker Street Westminster London",
        "pincode": "51524036",
        "city": "Westminster",
        "state": "Westminster",
        "country": "London"
      }
    },
    "merchant_metadata": {
      "key1": "DD",
      "key2": "XOF"
    }
  }
}
```
```json Sample Response
{
  "data": {
    "order_id": "v1-4405071524-aa-qlAtAf",
    "merchant_order_reference": "112345",
    "type": "CHARGE",
    "status": "CREATED",
    "merchant_id": "104359",
    "order_amount": {
      "value": 1100,
      "currency": "INR"
    },
    "pre_auth": false,
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "123456",
        "mobile_number": "9876543210",
        "billing_address": {
          "address1": "10 Downing Street Westminster London",
          "address2": "Oxford Street Westminster London",
          "address3": "Baker Street Westminster London",
          "pincode": "51524036",
          "city": "Westminster",
          "state": "Westminster",
          "country": "London"
        },
        "shipping_address": {
          "address1": "10 Downing Street Westminster London",
          "address2": "Oxford Street Westminster London",
          "address3": "Baker Street Westminster London",
          "pincode": "51524036",
          "city": "Westminster",
          "state": "Westminster",
          "country": "London"
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [],
    "created_at": "2024-07-15T05:44:51.174263Z",
    "updated_at": "2024-07-15T05:44:51.174455Z"
  }
}
```

Refer to our <a href="https://developer.pluralonline.com/v3.0/reference/orders-create" target="_blank">Create Order API</a> documentation to learn more.

> 📘 Note:
> 
> Plural orders API supports pre-authorization as an option. When the per-authorization is set to true you can capture the payment after successful delivery or service. To learn more about our Orders pre-auth refer to our Orders documentation.

## 3. Create Payment

To create a payment use our Create Payment API, use the `order_id` returned in the response of a Create Order API to link the payment against an order.

Use the below endpoint to create a payment.

```text Create Payment Endpoint for UAT
POST: https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/payments
```
```text Create Payment Endpoint for PROD
POST: https://api.pluralpay.in/api/pay/v1/orders/{order_id}/payments
```

Below is a sample request and sample response for Create Payment API.

```json Sample Request
{
  "payments": [
    {
      "merchant_payment_reference": "",
      "payment_method": "CARD",
      "payment_amount": {
        "value": 1100,
        "currency": "INR"
      },
      "payment_option": {
        "card_details": {
          "name": "Anil Reddy",
          "card_number": "4111111111111111",
          "cvv": "272",
          "expiry_month": "04",
          "expiry_year": "2029",
          "registered_mobile_number": "9876543210"
        }
      }
    }
  ]
}
```
```json Sample Response
{
  "data": {
    "order_id": "v1-4405071524-aa-qlAtAf",
    "merchant_order_reference": "112345",
    "type": "CHARGE",
    "status": "PENDING",
    "challenge_url": "https://api.pluralpay.in/web/auth/landing/?token=S50%2B0lOoYHlA03j3y8Of4%2BZEzhD8MuFFLKP6NXx9uiaBBXlNhpCRA4wqkPd%2Bs9eRz7H",
    "merchant_id": "123456",
    "order_amount": {
      "value": 1100,
      "currency": "INR"
    },
    "pre_auth": false,
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "123456",
        "mobile_number": "9876543210",
        "billing_address": {
          "address1": "10 Downing Street Westminster London",
          "address2": "Oxford Street Westminster London",
          "address3": "Baker Street Westminster London",
          "pincode": "51524036",
          "city": "Westminster",
          "state": "Westminster",
          "country": "London"
        },
        "shipping_address": {
          "address1": "10 Downing Street Westminster London",
          "address2": "Oxford Street Westminster London",
          "address3": "Baker Street Westminster London",
          "pincode": "51524036",
          "city": "Westminster",
          "state": "Westminster",
          "country": "London"
        }
      },
      "merchant_metadata": {
        "key1": "value1",
        "key2": "value2"
      }
    },
    "payments": [
      {
        "id": "v1-5307071124-aa-dmkVNf-cc-c",
        "status": "PENDING",
        "payment_amount": {
          "value": 1100,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "KOTAK",
            "card_category": "CONSUMER",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "capture_data": []
      }
    ],
    "created_at": "2024-07-11T07:53:43.358640Z",
    "updated_at": "2024-07-11T07:56:18.044812Z"
  }
}
```

Refer to our <a href="https://developer.pluralonline.com/v3.0/reference/payments-create" target="_blank">Create Payment API</a> documentation to learn more.

## 4. Handle Payment

In create payment API response we return a `challenge_url`, use this challenge url to navigate your customers to the checkout page to accept payment.

> 📘 Note:
> 
> - On successful payment we send the webhook event `ORDER_AUTHORIZED` and the status of the payment is updated to `authorized`.
> - You can capture or cancel an order only when the order status is `authorized`.

### 4.1 Store Payment Details on Your Server

On a successful and failed payment we return the following fields to the return url.

- We recommend you to store the payment details on your server.
- It is recommended to validate the authenticity of the payment details returned. You can authenticate by verifying the signature.

```json Success Callback Response
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "payment_status": "AUTHORIZED",
  "signature": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
}
```
```json Failure Callbak Response
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "payment_status": "AUTHORIZED",
  "error_code": "USER_AUTHENTICATION_REQUIRED",
  "error_message": "Consumer Authentication Required",
  "signature": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
}
```

### 4.2 Verify Payment Signature

Ensure you follow this as a mandatory step to verify the authenticity of the details returned to the checkout form for successful payments.

Follow the below steps to verify the signature.

1. Create a signature on your server using the following parameters using the SHA256 algorithm.
   1. `order_id`: Unique Identifier generated for an order request on Plural database.
   2. `payment_status`: Payment status.
   3. `error_code`: Short code for the error returned.
   4. `error_message`: Corresponding error message for the code.
   5. `secret_key`: The Onboarding team has provided you with this information as part of the onboarding process.

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
        String input = "order_id=<order_id>&status=<status>";
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

2. If the signature generated on your server matches the Plural signature returned in the return URL, it confirms that the payment details are from Plural.
3. Capture the status returned on your database. Once the payment status is `AUTHORIZED` you can either capture or cancel an order.
