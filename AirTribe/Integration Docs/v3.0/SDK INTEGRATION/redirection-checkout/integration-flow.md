---
title: "Integration Flow"
slug: "integration-flow"
excerpt: "Learn how you can integrate with Plural APIs to start accepting payments on your website."
hidden: true
createdAt: "Thu Jun 27 2024 06:16:07 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Jun 27 2024 11:23:25 GMT+0000 (Coordinated Universal Time)"
---
The figure below shows the steps you need to follow to integrate with Plural redirect checkout APIs in your application.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/6665901-Group_14.png",
        "",
        "Figure: Redirect Checkout Integration Flow"
      ],
      "align": "center",
      "caption": "**Figure**: Redirect Checkout Integration Flow"
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
  }
}
```

> 📘 Note:
> 
> - Contact our Integration Team to know your `merchant_id` and `merchant_access_code`. Additionally you are required to whitelist your `merchant_return_url` and get enabled with payment modes as required.

2. **Encode JSON**: Convert the updated JSON to a Base64 Encode. Use the below sample code to handle the conversion of the JSON to a Base64 Encode.

```node Node.js
var buff = Buffer.from(
  JSON.stringify({
    merchant_data: {
      merchant_id: 12345678,
      merchant_access_code: "4a8c422e-928d-4f84-bfe8-27a09af66647",
      unique_merchant_txn_id: "XYZ123",
      merchant_return_url: "https://www.pinelabs.com",
    },
    payment_data: {
      amount_in_paisa: 800,
    },
    txn_data: {
      navigation_mode: "2",
      payment_mode: "1,3,4,19,10,11,14",
      transaction_type: "1",
      time_stamp: 157588000000,
    },
  }),
).toString("base64");
console.log(buff);
```
```go Go
package main

import (
    "encoding/base64"
    "encoding/json"
    "fmt"
)

func main() {
    data: = map[string] string {
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
    }
    jsonData,
    err: = json.Marshal(data)
    if err != nil {
        fmt.Println("Error:", err)
        return
    }

    base64Str: = base64.StdEncoding.EncodeToString(jsonData)
    fmt.Println(base64Str)
}
```
```php PHP
<?php
$data = [
    "merchant_data" => [
        "merchant_id" => 12345678,
        "merchant_access_code" => "4a8c422e-928d-4f84-bfe8-27a09af66647",
        "unique_merchant_txn_id" => "XYZ123",
        "merchant_return_url" => "https://www.pinelabs.com",
    ],
    "payment_data" => [
        "amount_in_paisa" => 800,
    ],
    "txn_data" => [
        "navigation_mode" => "2",
        "payment_mode" => "1,3,4,19,10,11,14",
        "transaction_type" => "1",
        "time_stamp" => 157588000000,
    ],
];
$jsonData = json_encode($data);
$base64Str = base64_encode($jsonData);
echo $base64Str . "\n";
?>
```
```python Python
import json
import base64

data = {
    "merchant_data": {
        "merchant_id": 12345678,
        "merchant_access_code": "4a8c422e-928d-4f84-bfe8-27a09af66647",
        "unique_merchant_txn_id": "XYZ123",
        "merchant_return_url": "https://www.pinelabs.com",
    },
    "payment_data": {"amount_in_paisa": 800},
    "txn_data": {
        "navigation_mode": "2",
        "payment_mode": "1,3,4,19,10,11,14",
        "transaction_type": "1",
        "time_stamp": 157588000000,
    },
}
json_data = json.dumps(data).encode("utf-8")
base64_str = base64.b64encode(json_data).decode("utf-8")
print(base64_str)
```
```java Java
import java.util.Base64;
import org.json.JSONObject;

public class Main {
    public static void main(String[] args) {
        JSONObject jsonObject = new JSONObject();
        
        // Constructing JSON object
        JSONObject merchantData = new JSONObject();
        merchantData.put("merchant_id", 12345678);
        merchantData.put("merchant_access_code", "4a8c422e-928d-4f84-bfe8-27a09af66647");
        merchantData.put("unique_merchant_txn_id", "XYZ123");
        merchantData.put("merchant_return_url", "https://www.pinelabs.com");

        JSONObject paymentData = new JSONObject();
        paymentData.put("amount_in_paisa", 800);

        JSONObject txnData = new JSONObject();
        txnData.put("navigation_mode", "2");
        txnData.put("payment_mode", "1,3,4,19,10,11,14");
        txnData.put("transaction_type", "1");
        txnData.put("time_stamp", 157588000000L);

        jsonObject.put("merchant_data", merchantData);
        jsonObject.put("payment_data", paymentData);
        jsonObject.put("txn_data", txnData);

        // Converting JSON object to JSON string
        String jsonString = jsonObject.toString();

        // Encoding JSON string to base64
        String base64Encoded = Base64.getEncoder().encodeToString(jsonString.getBytes());

        System.out.println(base64Encoded);
    }
}
```

3. **HashMap**: Generate HashMap using the Base64 Encode and the secret key. Use the below sample code to handle the generation of HashMap using SHS256.

```javascript JavaScript
const crypto = require('crypto');

function generateSignature(signingSecret, payload) {
  try {
    // Convert signing secret to Buffer
    const secretKey = Buffer.from(signingSecret, 'utf8');

    // Convert payload object to JSON string
    const jsonString = JSON.stringify(payload);

    // Create HMAC using SHA-256 and secret key
    const hmac = crypto.createHmac('sha256', secretKey);

    // Update HMAC with JSON payload
    hmac.update(jsonString, 'utf8');

    // Compute HMAC digest and return as hexadecimal string
    return hmac.digest('hex');
  } catch (error) {
    console.error('Error generating signature:', error);
    return null;
  }
}

function main() {
  const signingSecret = '4a8c422e-928d-4f84-bfe8-27a09af66647'; // Replace with your actual signing secret

  const payload = {
    merchant_data: {
      merchant_id: 12345678,
      merchant_access_code: "4a8c422e-928d-4f84-bfe8-27a09af66647",
      unique_merchant_txn_id: "XYZ123",
      merchant_return_url: "https://www.pinelabs.com",
    },
    payment_data: {
      amount_in_paisa: 800,
    },
    txn_data: {
      navigation_mode: "2",
      payment_mode: "1,3,4,19,10,11,14",
      transaction_type: "1",
      time_stamp: 157588000000,
    },
  };

  // Generate signature
  const requestSignature = generateSignature(signingSecret, payload);

  console.log('Payload:');
  console.log(payload);
  console.log('\nGenerated Signature:');
  console.log(requestSignature);
}

main();

```
```go Go
package main

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"log"
)

func generateSignature(signingSecret string, payload interface{}) string {
	jsonPayload, err := json.Marshal(payload)
	if err != nil {
		log.Fatalf("Error marshalling JSON: %v", err)
	}

	// Convert signing secret to []byte
	secretKey := []byte(signingSecret)

	// Create HMAC using SHA-256 and secret key
	h := hmac.New(sha256.New, secretKey)

	// Update HMAC with JSON payload
	h.Write(jsonPayload)

	// Compute HMAC digest
	signature := h.Sum(nil)

	// Encode signature as Base64
	base64Encoded := base64.StdEncoding.EncodeToString(signature)

	return base64Encoded
}

func main() {
	signingSecret := "4a8c422e-928d-4f84-bfe8-27a09af66647" // Replace with your actual signing secret

	payload := map[string]interface{}{
		"merchant_data": map[string]interface{}{
			"merchant_id":            123456

```
```php PHP
<?php

function generateSignature($signingSecret, $payload) {
    // Convert payload to JSON
    $jsonPayload = json_encode($payload);
    if ($jsonPayload === false) {
        throw new Exception('Error encoding JSON: ' . json_last_error_msg());
    }

    // Create HMAC using SHA-256 and secret key
    $signature = hash_hmac('sha256', $jsonPayload, $signingSecret, true);

    // Encode signature as Base64
    $base64Encoded = base64_encode($signature);

    return $base64Encoded;
}

function main() {
    $signingSecret = "4a8c422e-928d-4f84-bfe8-27a09af66647"; // Replace with your actual signing secret

    $payload = [
        "merchant_data" => [
            "merchant_id" => 123456
        ]
    ];

    $signature = generateSignature($signingSecret, $payload);

    echo "Generated Signature: " . $signature . "\n";
}

// Run the main function
main();

?>

```
```python Python
import hmac
import hashlib
import base64
import json

def generate_signature(signing_secret, payload):
    # Convert payload to JSON
    json_payload = json.dumps(payload)
    
    # Create HMAC using SHA-256 and secret key
    secret_key = bytes(signing_secret, 'utf-8')
    h = hmac.new(secret_key, json_payload.encode('utf-8'), hashlib.sha256)
    
    # Compute HMAC digest
    signature = h.digest()
    
    # Encode signature as Base64
    base64_encoded = base64.b64encode(signature).decode('utf-8')
    
    return base64_encoded

def main():
    signing_secret = "4a8c422e-928d-4f84-bfe8-27a09af66647"  # Replace with your actual signing secret

    payload = {
        "merchant_data": {
            "merchant_id": 123456
        }
    }

    signature = generate_signature(signing_secret, payload)
    print("Generated Signature:", signature)

# Run the main function
if __name__ == "__main__":
    main()

```
```java Java
import java.nio.charset.StandardCharsets;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import org.apache.commons.codec.binary.Hex;

public class SignatureGenerator {

  public static String generateSignature(
    String signingSecret,
    String responseBody
  ) {
    try {
      byte[] secretKeyBytes = signingSecret.getBytes(StandardCharsets.UTF_8);
      SecretKeySpec keySpec = new SecretKeySpec(secretKeyBytes, "HmacSHA256");

      Mac mac = Mac.getInstance("HmacSHA256");
      mac.init(keySpec);

      byte[] prehash = responseBody.getBytes(StandardCharsets.UTF_8);
      byte[] hash = mac.doFinal(prehash);

      return Hex.encodeHexString(hash);
    } catch (NoSuchAlgorithmException | InvalidKeyException e) {
      e.printStackTrace();
      return null;
    }
  }

  public static void main(String[] args) {
    String signingSecret = "<enter_your_signing_secret>";
    String responseBody = "<enter the JSON payload>";

    String requestSignature = generateSignature(signingSecret, responseBody);
    System.out.println(requestSignature);
  }
}

```

## 2. Generate Payment Link

To generate a Payment Link use our Accept Payment API. You need to pass the HashMap generated as the authorization header and the Base64 Encode in the request body of this API.

Use the below endpoint to Accept payment.

```text Accept Payment Endpoints
UAT: https://uat.pinepg.in/api/v2/accept/payment
PROD: https://pinepg.in/api/v2/accept/payment
```

> 📘 Note:
> 
> Use UAT environment endpoint to test. While Integrating our APIs on your backend server use our production environment endpoint.

Shown below is a sample request and sample response for a Accept Payment API.

```json Sample Request
{
  "request": "ewogICJtZXJjaGFudF9kYXRhIjogewogICAgIm1lcmNoYW50X2lkIjogMTA4NTA2LAogICAgIm1lcmNoYW50X2FjY2Vzc19jb2RlIjogIjRhOGM0MjJkLTkyOGMtNGY4My1iZmU4LTI3YTA5YWY2NjY0NyIsCiAgICAidW5pcXVlX21lcmNoYW50X3R4bl9pZCI6ICJYWVoxMjMiLAogICAgIm1lcmNoYW50X3JldHVybl91cmwiOiAiaHR0cDovLzE5Mi4xNjguMTAxLjkzOjcwNTAvQ2hhcmdpbmdSZXNwLmFzcHgiCiAgfSwKICAicGF5bWVudF9kYXRhIjogewogICAgImFtb3VudF9pbl9wYWlzYSI6IDgwMAogIH0sCiAgInR4bl9kYXRhIjogewogICAgIm5hdmlnYXRpb25fbW9kZSI6ICIyIiwKICAgICJwYXltZW50X21vZGUiOiAiMSwzLDQsMTksMTAsMTEsMTQiLAogICAgInRyYW5zYWN0aW9uX3R5cGUiOiAiMSIsCiAgICAidGltZV9zdGFtcCI6IDE1NzU4ODAwMDAwMAogIH0KfQ=="
}
```
```json Sample Response

```

Refer to our Accept Payment API Documentation for more information.

## 3. Accept Payment

Use the generated link returned in our accept payment API to redirect your customers to the plural hosted page to accept payment. After successful payment we redirect your customers to your website.

You can know the status of the payment using the below.

1. **Webhook Notification**: We send Webhook notifications on the successful payment or any changes to the payments object.

```json Sample Webhook Payload

```

> 📘 Note:
> 
> You can use our Retrieve Payment API to check the status of the payment.

2. **Retrieve Payment API**

Use this API to retrieve the specified payment.

Use the below endpoint to Retrieve the Payment API.

```text Retrieve Payment API

```

<br />

Use the generated HashMap as the authorization header of the accept payment API. Additionally send the Base64 Encode in the request body and trigger the API. In the response we return the payment link to accept the payment.
