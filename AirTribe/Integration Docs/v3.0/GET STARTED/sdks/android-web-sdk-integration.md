---
title: "Android Web SDK Integration"
slug: "android-web-sdk-integration"
excerpt: "Learn how you can start integrating with Plural Android Web SDK."
hidden: false
createdAt: "Mon Oct 21 2024 09:02:45 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Apr 07 2025 05:15:54 GMT+0000 (Coordinated Universal Time)"
---
The Android Web SDK integration involves the following steps below:

1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-web-sdk-integration#1-installation" >Installation</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-web-sdk-integration#11-configure-build-setting" >Configure Build Setting</a>
2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-web-sdk-integration#2-integrate-apis" >Integrate APIs in Your Backend</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-web-sdk-integration#21-generate-auth-token" >Generate Auth Token</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-web-sdk-integration#22-create-hosted-checkout" >Create Hosted Checkout</a>
3. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-web-sdk-integration#3-initialize-sdk" >Initialize SDK</a>
4. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-web-sdk-integration#4-handle-payments" >Handle Payments</a>
5. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-web-sdk-integration#5-manage-transactions" >Manage Transactions</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-web-sdk-integration#51-get-order-by-order-id" >Fetch APIs</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/android-web-sdk-integration#52-webhooks" >Webhooks</a>

> 📘 Note:
> 
> - Ensure you store your Client ID and Secret in your Backend securely.
> - Integrate our APIs on your backend system.
> - We strictly recommend not to call our APIs from the frontend.

## 1. Installation

Install Pine Labs android SDK using Android Studio or IntelliJ. To add the SDK to your app, import the `.aar` file to the project using the following steps:

1. From the Android Studio package manager, select project.
2. Create a new directory in a project named `libs`.
3. Download your Android SDK `.aar` file <a href="https://github.com/plural-pinelabs/Plural_Android_Web_SDK" target="_blank">here</a>.
4. Paste your `.aar` file inside the libs folder

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ba70366863a0d202608b5eee88fee433390a2e44cb02fd37f1ef2ea308299701-Group_1171279972.png",
        "",
        "Figure: Installation"
      ],
      "align": "center",
      "sizing": "700px",
      "border": true,
      "caption": "Figure: Installation"
    }
  ]
}
[/block]


### 1.1. Configure Build Setting

1. Include the below dependencies in your `build.gradle` file.

```text Implementation
implementation files('libs/EDGE-SDK.aar')
```

2. After adding the necessary dependencies to your `build.gradle` file, sync your project.
3. Next, include the following code in your `AndroidManifest.xml` file to obtain the required static permissions.

```Text Code
<uses-permission android:name="android.permission.INTERNET"/>

<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
```

## 2. Integrate APIs in Your Backend

Start a payment by triggering the payment flow. To start a payment follow the below steps:

### 2.1. Generate Auth Token

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

### 2.2. Create Hosted Checkout

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
  "merchant_order_reference": 112345171,
  "order_amount": {
    "value": 500,
    "currency": "INR"
  },
  "pre_auth": false,    
  "notes": "order1",
  "purchase_details": {
    "customer": {
      "email_id": "kevin.bob@example.com",
      "first_name": "Kevin",
      "last_name": "Bob",
      "customer_id": "192212",
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
  "merchant_order_reference": 112345171,
  "order_amount": {
    "value": 500,
    "currency": "INR"
  },
  "pre_auth": false,    
  "notes": "order1",
  "purchase_details": {
    "customer": {
      "email_id": "kevin.bob@example.com",
      "first_name": "Kevin",
      "last_name": "Bob",
      "customer_id": "192212",
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

**Parameters Used in a Payment**

**context**: Refers to the activity context where this method is called.  
**redirectUrl**:  The challenge URL generated when the order creation endpoint is invoked.  
**callback**: `EdgeResponseCallback` is a constant that handles callback messages sent back to your Android app.

## 3. Initialize SDK

To initialise the android web SDK, follow the below steps:

1. **Create an `EdgeManager` object**: Initialise an instance of EdgeManager as shown below in your project.

```Text Edge Manager Object
val edgeManager = EdgeManager()
```

2. **Invoke startPayment**: Use the `edgeManager` object to call the `startPayment` method, which is defined in the Android SDK.

```text Start Payment
edgeManager.startPayment(context, redirectUrl, EdgeResponseCallback)
```

## 4. Handle Payments

You need to implement call-back methods to handle your payment responses. This will provide the payment status and reason for transaction failures. Based on the reasons for failures, handling can be built at your end. Transaction callbacks can be listened to via overriding methods of EdgeResponseCallback. 

**onTransactionResponse**: This method is called when the transaction is completed. Transaction can be a failure or a success.   
**internetNotAvailable**: This method is called when the internet is not available.  
**onErrorOccured**: This method is called when SDK is unable to load the payment page.  
**onPressedBackButton**: This method is called when the user presses the back button  
**onCancelTxn**: This method is called when the user cancels the transaction.

```kotlin Sample Override Function
override fun onInternetNotAvailable(code: Int, message: String?) {
    Toast.makeText(context: this, message, Toast.LENGTH_SHORT).show()
}

override fun onErrorOccurred(code: Int, message: String?) {
    Toast.makeText(context: this, text: "Error occurred ->$message", Toast.LENGTH_SHORT).show()
}

override fun onTransactionResponse() {
    Toast.makeText(context: this, text: "Transaction success", Toast.LENGTH_SHORT).show()
    inquiryDetails(token)
}

override fun onCancelTxn(code: Int, message: String?) {
    Toast.makeText(context: this, message, Toast.LENGTH_SHORT).show()
}

override fun onPressedBackButton(code: Int, message: String?) {
    Toast.makeText(context: this, message, Toast.LENGTH_SHORT).show()
}
```

## 5. Manage Transactions

To get the status of the transaction made from your application, you can use our Fetch APIs to know the real time status.

### 5.1. Get Order by Order ID

Use this API to know the real time status of the transaction made on your application. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/orders-get-by-order-id" target="_blank">Get Order by Order ID API</a> documentation to learn more.

### 5.2. Webhooks

You can configure the webhook events to know the status of your transactions. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/developer-tools-webhook" target="_blank">Webhooks</a> documentation to learn more.
