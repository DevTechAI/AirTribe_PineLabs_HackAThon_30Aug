---
title: "Android Native SDK Integration"
slug: "android-native-sdk-integration"
excerpt: "Learn how you can start integrating with Plural Android Native SDK."
hidden: false
createdAt: "Mon Mar 24 2025 05:52:21 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue May 20 2025 05:17:59 GMT+0000 (Coordinated Universal Time)"
---
The Android Native SDK integration involves the following steps below:

1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-native-sdk-integration#1-prerequisite-integrate-apis-in-your-backend" >\[Prerequisite] Integrate APIs in Your Backend</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-native-sdk-integration#11-generate-auth-token" >Generate Auth Token</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-native-sdk-integration#12-create-hosted-checkout" >Create Hosted Checkout</a>
2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-native-sdk-integration#2-installation" >Installation</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-native-sdk-integration#21-configure-build-setting" >Configure Build Setting</a>
3. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-native-sdk-integration#3-initialize-sdk" >Initialize SDK</a>
4. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-native-sdk-integration#4-handle-payments" >Handle Payments</a>
5. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-native-sdk-integration#5-manage-transactions" >Manage Transactions</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-native-sdk-integration#51-get-order-by-order-id" >Fetch APIs</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-native-sdk-integration#52-webhooks" >Webhooks</a>

> 📘 Note:
> 
> - Ensure you store your Client ID and Secret in your Backend securely.
> - Integrate our APIs on your backend system.
> - We strictly recommend not to call our APIs from the frontend.

## 1. [Prerequisite] Integrate APIs in Your Backend

Start a payment by triggering the payment flow. To start a payment, follow the below steps:

### 1.1. Generate Auth Token

Integrate our Generate Token API in your backend servers to generate the auth token. Use the token generated to authenticate Plural APIs.

Below are the sample requests and response for the Generate Token API.

```curl cURL – UAT
curl --location 'https://pluraluat.v2.pinepg.in/api/auth/v1/token' \
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
curl --location 'https://api.pluralpay.in/api/auth/v1/token' \
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

### 1.2. Create Hosted Checkout

Use this API to create a hosted checkout, for authentication use the generated access token in the headers of the API request.

Below are the sample requests and response for a Create Hosted Checkout API.

```curl cURL - UAT
curl --location 'https://pluraluat.v2.pinepg.in/api/checkout/v1/orders' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
--header 'Content-Type: application/json' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'accept: application/json' \
--data '
{
  "merchant_order_reference": "f4c45dbd-6eba-453d-b317-158c6ba12825",
  "order_amount": {
    "value": 500,
    "currency": "INR"
  },
  "purchase_details": {
    "customer": {
      "email_id": "joe.sam@gmail.com",
      "first_name": "joe",
      "last_name": "kumar",
      "customer_id": "192212",
      "mobile_number": "192192883",
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
      "key1": "value1",
      "key2": "value2"
    },
    "integration_mode": "SDK"
  }
}
'
```
```curl cURL - PROD
curl --location 'https://api.pluralpay.in/api/checkout/v1/orders' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
--header 'Content-Type: application/json' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'accept: application/json' \
--data '
{
  "merchant_order_reference": "f4c45dbd-6eba-453d-b317-158c6ba12825",
  "order_amount": {
    "value": 500,
    "currency": "INR"
  },
  "purchase_details": {
    "customer": {
      "email_id": "joe.sam@gmail.com",
      "first_name": "joe",
      "last_name": "kumar",
      "customer_id": "192212",
      "mobile_number": "192192883",
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
      "key1": "value1",
      "key2": "value2"
    },
    "integration_mode": "SDK"
  }
}
'
```
```json Sample Response
{
  "token": "REDIRECT TOKEN",
  "order_id": "ORDER ID",
  "redirect_url": "https://api.pluralonline.com/api/v3/checkout-bff/redirect/checkout?token=REDIRECT TOKEN",
  "response_code": 200,
  "response_message": "Order Creation Successful."
}
```

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/hosted-checkout-create" target="_blank">Create Hosted Checkout API</a> documentation to learn more.

## 2. Installation

To include the Plural Android SDK in your project, follow these steps:

### 2.1. Configure Build Setting

1. Navigate to the build.gradle file of your app module (usually located at app/build.gradle).
2. Include the below dependencies in your `build.gradle` file.

```text PROD Implementation
dependencies {
  implementation 'com.github.plural-pinelabs:Plural_Android_SDK:1.2'
}
```
```text UAT Implementation
dependencies {
  implementation 'com.github.plural-pinelabs:Plural_Android_SDK:9.1'
}
```

3. After adding the necessary dependencies to your `build.gradle` file, click on "Sync Now" in the notification bar to sync your project with the updated Gradle files.
4. Next, include the following code in your `AndroidManifest.xml` file to obtain the required static permissions.

```Text Code
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
```

## 3. Initialize SDK

To initialise the Plural SDK, follow these steps:

1. **Create an `PluralSDKManager` object**: Initialise an instance of PluralSDKManager as shown below in your project:

```Text SDK Manager Object
val sdkManager = PluralSDKManager()
```

2. **Invoke startPayment**: Use the `sdkManager` object to call the `startPayment` method, which is defined in the Android SDK.

```text Start Payment
sdkManager.startPayment(context, token, PaymentResultCallBack)
```

**Parameters Used in a Payment**

**context**: Refers to the activity context where this method is called.  
**token**:  The token generated from the Create Hosted Checkout API response.  
**PaymentResultCallBack**: `PaymentResultCallBack` is a constant that handles callback messages sent back to your Android app.

## 4. Handle Payments

You need to implement call-back methods to handle your payment responses. This will provide the payment status and reason for transaction failures. Based on the reasons for failures, handling can be built at your end. Transaction callbacks can be listened to via overriding methods of `PaymentResultCallBack`. 

 **onErrorOccured**: This method is called when SDK is unable to load the payment page.  
**onSuccessOccured**: This method is called when transaction is complete. Transaction can be failed or success.  
**onCancelTransaction**: This method is called when the user cancels the transaction.

```kotlin Sample Override Function
override fun onErrorOccured(orderId: String?, code: String?, message: String?) {
    Toast.makeText(context: this, text: "Error occurred ->$message", Toast.LENGTH_SHORT).show()
}

override fun onSuccessOccured(orderId: String?) {Toast.makeText(context: this, text: "Payment Successful ${orderId}",Toast.LENGTH_SHORT).show()
}

override fun onCancelTransaction() {Toast.makeText(this text: "Cancel transaction", Toast.LENGTH_SHORT).show()}()
}
```

## 5. Manage Transactions

To get the status of the transaction made from your application, you can use our Fetch APIs to know the real time status.

### 5.1. Get Order by Order ID

Use this API to know the real time status of the transaction made on your application. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/orders-get-by-order-id" target="_blank">Get Order by Order ID API</a> documentation to learn more.

### 5.2. Webhooks

You can configure the webhook events to know the status of your transactions. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/developer-tools-webhook" target="_blank">Webhooks</a> documentation to learn more.
