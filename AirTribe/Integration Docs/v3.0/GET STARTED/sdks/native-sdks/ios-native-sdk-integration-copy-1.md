---
title: "iOS Native SDK Integration (COPY)"
slug: "ios-native-sdk-integration-copy-1"
excerpt: "Learn how you can start integrating with Plural iOS Native SDK."
hidden: true
createdAt: "Tue May 27 2025 06:47:36 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue May 27 2025 06:47:36 GMT+0000 (Coordinated Universal Time)"
---
The iOS Native SDK integration involves the following steps below:

1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/ios-native-sdk-integration#1-prerequisite-integrate-apis-in-your-backend" >\[Prerequisite] Integrate APIs in Your Backend</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/ios-native-sdk-integration#11-generate-auth-token" >Generate Auth Token</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/ios-native-sdk-integration#12-create-hosted-checkout" >Create Hosted Checkout</a>
2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/ios-native-sdk-integration#2-installation" >Installation</a>
3. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/ios-native-sdk-integration#3-initialize-sdk" >Initialize SDK</a>
4. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/ios-native-sdk-integration#4-handle-payments" >Handle Payments</a>
5. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/ios-native-sdk-integration#5-manage-transactions" >Manage Transactions</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/ios-native-sdk-integration#51-get-order-by-order-id" >Fetch APIs</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/ios-native-sdk-integration#52-webhooks" >Webhooks</a>

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

Install Plural iOS Native SDK using Xcode. To add the SDK to your app, import the `.xcframework` file to the project using the following steps:

1. **Download the SDK Framework**: You can download the SDK as a `(SDKFramework).xcframework` file here, which is in a package format that Apple recommends for distributing binary frameworks.
2. **Add Framework to Your Package**:

   1. **Drag and Drop**: Simply drag and drop the `(SDKFramework).xcframework` file into your Xcode project in the Project Navigator under the Frameworks section.
   2. **Dialog Box Settings**: A dialog box will appear when you drop the `(SDKFramework).xcframework` file into your project. Ensure that the checkbox labeled `Copy items if needed` is selected. This ensures that the framework gets copied into your project directory, making it available whenever you need to build the project.
   3. Drag and drop the `.xcframework` in the app.

      [block:image]{"images":[{"image":["https://files.readme.io/1cadf4f6d16efba8c5ea455979bc634bc55c923edcd5ea56e0c185c10145f340-image.png",null,""],"align":"center","sizing":"700px"}]}[/block]
   4. copy files to destination.

   [block:image]{"images":[{"image":["https://files.readme.io/0a92b6b19463f76e0abc3b410873f76b0f65c03212be8b521e567a9b7195c7ec-image.png",null,""],"align":"center","sizing":"700px"}]}[/block]

> 📘 Note:
> 
> The `userSDKFramework` function, created during the SDK installation, implements startPayment. Use this function to pass the order token and initiate the call to `Plural_IOS_SDK`.
> 
> ![](https://files.readme.io/11974d277c39c3843304e4c2d506cc3927fa8faaa117c1ec33af8a4561216080-image.png)

> 🚧 Watch Out:
> 
> Ensure that the minimum compilation compatibility version is set to iOS 16 or 17

3. **Configure the App Target**: You need to configure the target to embed the SDK framework properly.

   1. Navigate to the General tab of your target's settings. Add the `(SDKFramework).xcframework` file under the Frameworks, Libraries, and Embedded Content section. 
   2. Ensure you choose `Embed & Sign`. This ensures the framework is embedded in your app when it's built and signed properly to run on iOS devices.

      [block:image]{"images":[{"image":["https://files.readme.io/6e60022ac8a21735260e3e95383449d8d6b862eb5522379d1731ea644608ec52-image.png",null,""],"align":"center","sizing":"700px"}]}[/block]

> 📘 Note:
> 
> - Once the `.xcframework` is embedded, you can import the package in the view controller.

4. **Network Check**: In the SDK, there is an internet connectivity function that accesses a URL (`example.com`). To ensure this works as expected, you need to update the `Info.plist`[Information Property List] file in your app to allow this connection.

> 👍 - Once this is added, you can check if the exception is being displayed in the Signing and Capabilities tab

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/b5e5061dabaadb35b179c049772007cbdada31853e4595ae7b3c1e5370a35e66-Screenshot_2024-10-16_at_12.59.04_PM.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


- To enable UPI payments, add URL Schemes in the Info.plist file:

  [block:image]{"images":[{"image":["https://files.readme.io/352bf4367256cbec10fd4a181d5c80cd71b76eb5e379067220ff577b14e83a76-image.png",null,"Property List View"],"align":"center","sizing":"700px","caption":"Property List View"}]}[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/34a30e40e86a555653fa59686f14bd2cb8347aad50d98e317b843d60e66295ba-image.png",
        null,
        "Source Code View"
      ],
      "align": "center",
      "sizing": "700px",
      "caption": "Source Code View"
    }
  ]
}
[/block]


Without these entries, the SDK won’t be able to navigate to the required UPI payment app.

## 3. Initialize SDK

a) To initialise the iOS Native SDK, follow the below steps:

1. Import the SDK into the app and, 
2. Create an object of the class `EdgeController` to initiate the payment function. In your application, you are creating a function that passes the **order token** received from the create order response to start the payment function of our SDK.

   [block:image]{"images":[{"image":["https://files.readme.io/4996a6df8b0ef0d0388d96f7e2f89ae28fd5e09ba26dc05f5f32a30e0b1e30c0-image.png",null,""],"align":"center","sizing":"700px"}]}[/block]

**Parameters for startPayment**:

**from**: Pass the context of the current ViewController where the SDK is invoked(generally ‘self’). 

**orderToken**: The token generated from the Create Hosted Checkout API response.

**MerchantCallbackResponse**: An instance that sends callback messages to the merchant IOS app. This value remains constant.

b) The user must define a Response Callback class that includes the following functions:

```swift Sample Response Callback Function
public class MerchantCallbackResponse: UIViewController, ResponseCallback {
  public func onErrorOccured(code: Int, message: String) {
      print("Test app response: error occurred")
      NotificationCenter.default.post(name: Notification.Name("ErrorFlowTransactionNotification"), object: nil)
  }

  public func onTransactionResponse() {
      print("Test app response: transaction response")
        
      // Post a notification for the transaction response and call Inquery from inside it.
      NotificationCenter.default.post(name: Notification.Name("TransactionResponseNotification"), object: nil)
      print("Notification posted.")
      print("Success Flow.")
  }

  public func onCancelTxn(code: Int, message: String) {
      print("Test app response: cancel transaction")
    
      // Post a notification to trigger the flow in the ViewController
      NotificationCenter.default.post(name: Notification.Name("ErrorFlowTransactionNotification"), object: nil)
  }

  public func onPressedBackButton(code: Int, message: String) {
      print("Test app response: back pressed")
  } 
} 
```

## 4. Handle Payments

You need to implement call-back methods to handle your payment responses. This will provide the payment status and reason for transaction failures. Based on the reasons for failures, handling can be built at your end. Transaction callbacks can be listened to via overriding methods of ResponseCallback. 

 In case of success, inside the SDK we check if the URL being loaded is the completion/final URL in the checkout flow. If that URL is being opened, then `onTransactionResponse()` is called from your app, which will return the flow back to your app from the SDK, indicating a successful transaction.

**internetNotAvailable**: This method is called when the internet is not available.  
**onErrorOccured**: This method is called when SDK is unable to load the payment page.  
**onPressedBackButton**: This method is called when the user presses the back button  
**onCancelTxn**: This method is called when the user cancels the transaction.

```swift Sample Override Function
public class MerchantCallbackResponse: UIViewController, ResponseCallback {
    
    public func internetNotAvailable(code: Int, message: String) {
        print("Test app response: internet not available")
    }

    public func onErrorOccured(code: Int, message: String) {
        print("Test app response: error occurred")
    }

    public func onTransactionResponse() {
        print("Test app response: transaction response")
    }

    public func onCancelTxn(code: Int, message: String) {
        print("Test app response: transaction cancelled")
    }

    public func onPressedBackButton(code: Int, message: String) {
        print("Test app response: back pressed")
    }
}
```

## 5. Manage Transactions

To get the status of the transaction made from your application, you can use our Fetch APIs to know the real time status.

### 5.1. Get Order by Order ID

Use this API to know the real time status of the transaction made on your application. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/orders-get-by-order-id" target="_blank">Get Order by Order ID API</a> documentation to learn more.

### 5.2. Webhooks

You can configure the webhook events to know the status of your transactions. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/developer-tools-webhook" target="_blank">Webhooks</a> documentation to learn more.
