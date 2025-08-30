---
title: "Integration Steps - Hosted Checkout"
slug: "integration-steps-hosted-checkout"
excerpt: "Learn how you can integrate with Plural APIs to start accepting payments on your website."
hidden: true
createdAt: "Mon Oct 07 2024 11:26:50 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Oct 14 2024 07:37:13 GMT+0000 (Coordinated Universal Time)"
---
Follow the below steps to integrate with Plural seamless checkout APIs in your application.

1. <a style="text-decoration:none" href ="https://developer.pluralonline.com/docs/integration-steps-plural-hosted-checkout#1-prerequisite-generate-token" >\[Prerequisite] Generate Token</a>
2. <a style="text-decoration:none" href ="https://developer.pluralonline.com/docs/integration-steps-plural-hosted-checkout#2-check-point-balance-api" >Payment Option API</a>
3. <a style="text-decoration:none" href ="https://developer.pluralonline.com/docs/integration-steps-plural-hosted-checkout#3-create-hosted-checkout" >Create Hosted Checkout</a>
4. <a style="text-decoration:none" href ="https://developer.pluralonline.com/docs/integration-steps-plural-hosted-checkout#4-handle-payment" >Handle Payment</a>
   1. <a style="text-decoration:none" href ="https://developer.pluralonline.com/docs/integration-steps-plural-hosted-checkout#41-store-payment-details-on-your-server" >Store Payment Details on Your Server</a>
   2. <a style="text-decoration:none" href ="https://developer.pluralonline.com/docs/integration-steps-plural-hosted-checkout#42-verify-payment-signature" >Verify Payment Signature</a>
5. <a style="text-decoration:none" href ="https://developer.pluralonline.com/docs/integration-steps-plural-hosted-checkout#5-capture-order" >Capture Order</a>
6. <a style="text-decoration:none" href ="https://developer.pluralonline.com/docs/integration-steps-plural-hosted-checkout#6-cancel-order" >Cancel Order</a>

## 1. [Prerequisite] Generate Token

> 🚧 Watch Out
> 
> - To Integrate with Plural seamless checkout flow you must have a PCI compliance certificate.

Integrate our Generate Token API in your backend servers to generate the access token. Use the token generated to authenticate Plural APIs.

Use the below endpoint to generate a token.

```text Generate Token Endpoint for UAT
POST: https://pluraluat.v2.pinepg.in/api/auth/v1/token
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

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/v3.0/reference/generate-token" target="_blank">Generate Token API</a> documentation to learn more.

## 2. Check Point Balance API

Use this API to check the Point balance and eligibility.

To authenticate this API, use the generated access token in the Authorization headers of the API request.

Use the below endpoint to check the eligibility and points balance.

```Text Create Order Endpoint for UAT
POST: https://pluraluat.v2.pinepg.in/payment-option
```
```text Create Order Endpoint for PROD
POST: https://api.pluralpay.in/payment-option
```

Below is a sample request and response for a Payment Option API

```json Sample Request
{
  "payment_option": {
    "points_card_details": {
      "card_last4": "1112",
      "card_number": "4111111111111112",
      "registered_mobile_number": "9876543210"
    }
  },
  "order_details": {
    "order_amount": {
      "value": 5000,
      "currency": "INR"
    }
  }
}
```
```json Sample Response
{
  "balance": {
    "value": 23718050,
    "currency": "INR"
  },
  "redeemable_amount": {
    "value": 3500,
    "currency": "INR"
  },
  "redeemable_points": 140,
  "is_eligible": true
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/reference/pay-by-point-check-point-balance" target="_blank">Check Point Balance API</a> documentation to learn more.

> 👍 Customer consent before redeeming points
> 
> - The **Pay by Points** option is not enabled by default.
> - Customers must explicitly provide consent to use their rewards or points as part of the payment for an order.
> - It is mandatory to obtain customer consent before redeeming their rewards/points in compliance with legal agreements established with our partner Banks.

## 3. Create Hosted Checkout

Use this API to create a hosted checkout, for authentication use the generated access token in the headers of the API request.

Use the below endpoint to create an order.

```Text Create Order Endpoint for UAT
POST: https://pluraluat.v2.pinepg.in/api/checkout/v1/orders
```
```text Create Order Endpoint for PROD
POST: https://api.pluralpay.in/api/checkout/v1/orders
```

Below is a sample request and response for a Create Order API.

```json Sample Request
{
  "order_amount": {
    "merchant_order_reference": "819e2785-155d-4cbf-ab20-a8ed5111c0f12",
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
  "token": "<<Redirect Token>>",
  "order_id": "v1-5757575757-aa-hU1rUd",
  "redirect_url": "https://api.pluralonline.com/api/v3/checkout-bff/redirect/checkout?token=<<Redirect Token>>",
  "response_code": 200,
  "response_message": "Order Creation Successful."
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/v3.0/reference/orders-create" target="_blank">Create Order API</a> documentation to learn more.

> 📘 Note:
> 
> When the pre-authorization is set to true you can capture the payment after successful delivery or service.

## 4. Handle Payment

In create payment API response we return a `challenge_url`, use this challenge url to navigate your customers to the checkout page to accept payment.

> 📘 Note:
> 
> - On successful payment we send the webhook event `ORDER_AUTHORIZED` and the status of the payment is updated to `authorized`.
> - You can capture or cancel an order only when the order status is `authorized`.

### 4.1 Store Payment Details on Your Server

On a successful and failed payment we return the following fields to the return url.

- We recommend you to store the payment details on your server.
- You must validate the authenticity of the payment details returned. You can authenticate by verifying the signature.

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

2. If the signature generated on your server matches the Plural signature returned in the return URL, it confirms that the payment details are from Plural.
3. Capture the status returned on your database. Once the payment status is `AUTHORIZED` you can either capture or cancel an order.

## 5. Capture Order

> 📘 Important:
> 
> - With pre-authorization set to true, you can capture or cancel a payment for an order.

Use this API to capture the payment against an order. On successful capture of an order the order status is updated as `processed`.

Use the below endpoint to capture the payment against the order.

```text Capture Order Endpoint for UAT
PUT: https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/capture
```
```text Capture Order Endpoint for PROD
PUT: https://api.pluralpay.in/api/pay/v1/orders/{order_id}/capture
```

Shown below is a sample request and sample response for a Capture Order API.

```json Sample Request
{
  "merchant_capture_reference": "merchant-capture-ref-r4y"
}
```
```json Sample Response
{
  "data": {
    "order_id": "v1-5757575757-aa-hU1rUd",
    "merchant_order_reference": "f4548bbf-a029-43d3-9209-e3385c80b1e9",
    "type": "CHARGE",
    "status": "PROCESSED",
    "merchant_id": "123456",
    "order_amount": {
      "value": 1100,
      "currency": "INR"
    },
    "pre_auth": true,
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "232323",
        "mobile_number": "9876543210",
        "billing_address": {
          "address1": "H.No 15, Sector 17",
          "address2": "",
          "address3": "",
          "pincode": "61232112",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        },
        "shipping_address": {
          "address1": "H.No 15, Sector 17",
          "address2": "string",
          "address3": "string",
          "pincode": "144001123",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-1111071924-aa-zzSkOA-cc-G",
        "status": "PROCESSED",
        "payment_amount": {
          "value": 1100,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "NONE",
            "card_category": "CONSUMER",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "000000",
          "acquirer_reference": "202456643801053",
          "rrn": "420145000226"
        },
        "capture_data": [
          {
            "merchant_capture_reference": "f31d8c60-0dc8-4788-a577-5ced930cc175",
            "capture_amount": {
              "value": 1100,
              "currency": "INR"
            },
            "created_at": "2024-07-19T11:13:21.523516426Z"
          }
        ],
        "created_at": "2024-07-19T11:11:48.944147Z",
        "updated_at": "2024-07-19T11:13:23.962461Z"
      }
    ],
    "created_at": "2024-07-19T11:11:48.944147Z",
    "updated_at": "2024-07-19T11:13:23.962461Z"
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/v3.0/reference/orders-capture" target="_blank">Capture Order API</a> documentation to learn more.

## 6. Cancel Order

Use this API to cancel the payment against an order.

Use the below endpoint to cancel the payment against the order.

```text Cancel Order Endpoint for UAT
PuT: https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/cancel
```
```text Cancel Order Endpoint for PROD
PUT: https://api.pluralpay.in/api/pay/v1/orders/{order_id}/cancel
```

Shown below is a sample request and sample response for a Cancel Order API.

```json Sample Response
{
  "data": {
    "order_id": "v1-5757575757-aa-hU1rUd",
    "merchant_order_reference": "2177120b-3be1-4330-a15f-53ce14d19841",
    "type": "CHARGE",
    "status": "CANCELLED",
    "merchant_id": "123456",
    "order_amount": {
      "value": 50000,
      "currency": "INR"
    },
    "pre_auth": true,
    "purchase_details": {
      "customer": {
        "email_id": "kevin.bob@example.com",
        "first_name": "Kevin",
        "last_name": "Bob",
        "customer_id": "232323",
        "mobile_number": "9876543210",
        "billing_address": {
          "address1": "H.No 15, Sector 17",
          "address2": "",
          "address3": "",
          "pincode": "61232112",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        },
        "shipping_address": {
          "address1": "H.No 15, Sector 17",
          "address2": "",
          "address3": "",
          "pincode": "144001123",
          "city": "CHANDIGARH",
          "state": "PUNJAB",
          "country": "INDIA"
        }
      },
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      }
    },
    "payments": [
      {
        "id": "v1-2711071924-aa-VxIzq1-cc-Z",
        "status": "CANCELLED",
        "payment_amount": {
          "value": 1100,
          "currency": "INR"
        },
        "payment_method": "CARD",
        "payment_option": {
          "card_data": {
            "card_type": "CREDIT",
            "network_name": "VISA",
            "issuer_name": "NONE",
            "card_category": "CONSUMER",
            "country_code": "IND",
            "token_txn_type": "ALT_TOKEN"
          }
        },
        "acquirer_data": {
          "approval_code": "000000",
          "acquirer_reference": "202456644249243",
          "rrn": "420123000239"
        },
        "created_at": "2024-07-19T11:27:55.664651Z",
        "updated_at": "2024-07-19T11:28:52.487287Z"
      }
    ],
    "created_at": "2024-07-19T11:27:55.664651Z",
    "updated_at": "2024-07-19T11:28:52.487287Z"
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/v3.0/reference/orders-cancel" target="_blank">Cancel Order API documentation to learn more.
