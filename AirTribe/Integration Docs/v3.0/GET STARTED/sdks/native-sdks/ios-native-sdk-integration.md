---
title: "iOS Native SDK Integration"
slug: "ios-native-sdk-integration"
excerpt: "Learn how you can start integrating with Plural iOS Native SDK."
hidden: false
createdAt: "Mon Mar 24 2025 06:30:25 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue May 27 2025 06:51:09 GMT+0000 (Coordinated Universal Time)"
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

<details><summary>Click here for request and response parameter information.</summary>

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid #5A0083;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n        .required-label {\n            color: red;\n            font-size: 12px;\n            vertical-align: super;\n            margin-left: 4px;\n    }\n    </style>\n</head>\n<body>\n     <div class=\"tab-container\">\n        <div class=\"tab active\" data-target=\"tab5\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Request Parameters</div>\n\n        <div class=\"tab\" data-target=\"tab6\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Response Parameters</div>\n\n    <div id=\"tab5\" class=\"tab-content active\">\n      \n      <p>The table below lists the request parameters of our Generate Token API.</p>\n\n<table>\n    <thead>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td> client_id&nbsp;<span class=\"required-label\">required</span>  \n          </td>\n          <td><code>string</code></td>\n            <td>\n                Unique client identifier in the Plural database.<br><br>\n              Example: <code>a17ce30e-f88e-4f81-ada1-c3b4909ed232</code><br><br>\n                <strong>Note:</strong> The Onboarding team has provided you with this information as part of the onboarding process.\n            </td>\n        </tr>\n        <tr>\n            <td>client_secret&nbsp;<span class=\"required-label\">required</span>              \n          </td>\n          <td><code>string</code></td>\n            <td>\n                Unique client secret key provided while onboarding.<br><br>\n              Example: <code>fgwei7egyhuggwp39w8rh</code><br><br>\n                <strong>Note:</strong> The Onboarding team has provided you with this information as part of the onboarding process.\n            </td>\n        </tr>\n        <tr>\n            <td>grant_type&nbsp;<span class=\"required-label\">required</span>\n          </td>\n          <td><code>string</code></td>\n            <td>\n                The grant type to generate an access token.<br><br>\n              Accepted value: <code>client_credentials</code>\n            </td>\n        </tr>\n    </tbody>\n</table>\n\n      \n    </div>\n    <div id=\"tab6\" class=\" tab-content\">\n      \n      <p style=\"\">The table below lists the response parameters of our Generate Token API.</p> \n      <table>\n    <thead>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th> <!-- Ensure this is present -->\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td>access_token</td>\n            <td><code>string</code></td>\n            <td>\n                The access token generated by the system.<br><br>\n                • Minimum length: 1 character.<br>\n                • Maximum length: 8192 characters.<br><br>\n                Example: <code>eyJhbGciOiJIUzI1NiIsIn</code><br><br>\n                <strong>Note:</strong> Use this token in the authorization headers to authenticate Plural APIs.\n            </td>\n        </tr>\n        <tr>\n            <td>expires_at</td>\n            <td><code>string</code></td>\n            <td>\n                Access duration timestamp.<br><br>\n                Example: <code>2024-06-28T13:26:06.909140Z</code>\n            </td>\n        </tr>\n    </tbody>\n</table>\n\n      \n    </div>\n</body>\n</html>"
}
[/block]


</details>

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

<details><summary>Click here for request and response parameter information.</summary>

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid #5A0083;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n        .required-label {\n            color: red;\n            font-size: 12px;\n            vertical-align: super;\n            margin-left: 4px;\n      }\n    </style>\n</head>\n<body>\n    <div class=\"tab-container\">\n        <div class=\"tab active\" data-target=\"tab3\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Request Parameters</div>\n\n        <div class=\"tab\" data-target=\"tab4\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Response Parameters</div>\n\n    <div id=\"tab3\" class=\"tab-content active\">\n      \n      \n      <body>\n    <p>The table below lists the request parameters of our Create Checkout Link API.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>merchant_order_reference&nbsp;<span class=\"required-label\">required</span>\n              </td>\n                <td><code>string</code></td>\n                <td>\n                    Enter a unique identifier for the order request.<br><br><ul><li>\n                    Minimum: 1 character.</li><li>\n                  Maximum: 50 characters.</ul></li>\n          Example: <code>1234567890</code><br><br>\n          Supported characters:<ul><li><code>A-Z</code></li><li><code>a-z</code></li><li><code>0-9</code></li><li><code>-</code></li><li><code>_</code></ul></li>\n                </td>\n            </tr>\n            <tr>\n                <td>order_amount&nbsp;<span class=\"required-label\">required</span></td>\n                <td><code>object</code></td>\n                <td>An object that contains the transaction amount details.<br><br><a href=\"#order-amount-child-object\">Learn more about the <code>order_amount</code> child object.</a>\n                </td>\n            </tr>\n                <td>pre_auth</td>\n                <td><code>boolean</code></td>\n                <td>\n                    The pre-authorization type.<br><br>\n                    Possible values:<br><ul><li>\n                  <code>false</code> (default): When pre-authorization is not required.<br></li><li>\n                    <code>true</code>: When pre-authorization is needed.\n                </td>\n            </tr>\n            <tr>\n                <td>allowed_payment_methods</td>\n                <td><code>array of strings</code></td>\n                <td>\n                    The type of payment methods you want to offer customers.<br><br>\n                  Accepted values:<ul><li><code>CARD</code></li><li><code>UPI</code></li><li><code>POINTS</code></li><li><code>NETBANKING</code></li><li><code>WALLET</code></li><li><code>CREDIT_EMI</code></li><li><code>DEBIT_EMI</code></ul></li>\n                    Example: CARD<br><br>\n <strong>Note</strong>: Ensure it is configured for you.\n                </td>\n            </tr>\n            <tr>\n                <td>notes</td>\n                <td><code>string</code></td>\n                <td>Note to show against an order.<br><br>\n                    Example: <code>Order1</code>\n                </td>\n            </tr>\n<tr>\n  <td>callback_url</td>\n  <td><code>string</code></td>\n  <td>Use this URL to redirect your customers to specific success or failure pages based on the order or product details.<br><br>Example: https\\://sample-callback-url>/td>\n            <tr>\n                <td>purchase_details</td>\n                <td><code>object</code></td>\n                <td>An object that contains purchase details.<br><br><a href=\"#purchase-details-child-object\">Learn more about the <code>purchase_details</code> child object.</a>\n                </td>\n            </tr>\n        </tbody>\n    </table>\n    <h2 id=\"order-amount-child-object\"> Order Amount [Child Object]</h2>\n        <p> The table below lists the various parameters in the <code>order_amount</code> child object. This object is part of the <code>Create Checkout Link</code> request object.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td><code>integer</code></td>\n                <td>\n                    Transaction amount in Paisa.<br><br><ul><li>\n                  Minimum value: <code>100</code> (₹1).</li><li>\n                  Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>\n          Example: <code>1000</code>\n                </td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td><code>string</code></td>\n                <td>\n                    Type of currency.<br><br>\n                  Example: <code>INR</code>\n                </td>\n            </tr>\n        </tbody>\n    </table>\n\n<h2 id=\"purchase-details-child-object\">Purchase Details [Child Object]</h2>\n<p>The table below lists the various parameters in the <code>purchase_details</code> child object. This object is part of the <code>Create Checkout Link</code> request object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n      <tr>\n            <td>bank_details&nbsp;<span class=\"required-label\">required</span>\n        </td>\n          <td><code>object</code></td>\n            <td>An object that contains the bank account details.<br><br><a href=\"#bank-details-child-object\">Learn more about the <code>bank_details</code> child object</a>.</td>\n        </tr>\n        <tr>\n            <td>customer</td>\n          <td><code>object</code></td>\n            <td>An object that contains the customer details.<br><br><a href=\"#customer-child-object\"> Learn more about the <code>customer</code> child object.</a></td>\n        </tr>\n        <tr>\n            <td>merchant_metadata</td>\n            <td><code>object</code></td>\n            <td>An object of key-value pair that can be used to store additional information.<br><br>Example: <code>\"key1\": \"DD\"</code></td>\n      </tr>\n    </table>\n<h3 id=\"bank-details-child-object\">Bank Details [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>bank_details</code> child object. This is part of the <code>purchase_details</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>account_number&nbsp;<span class=\"required-label\">required</span>\n          </td>\n          <td><code>string</code></td>\n          <td>Customer's bank account number.<br><br>Example: <code>500000004545</code></td>\n        </tr>\n        <tr>\n            <td>ifsc_code</td>\n          <td><code>string</code></td>\n          <td>Customer's bank IFSC.<br><br>Example: <code>BANK0000123</code></td>\n        </tr>\n        <tr>\n            <td>bank_name</td>\n          <td><code>string</code></td>\n          <td>Customer's account holding bank name.<br><br>Example: <code>Example Bank</code></td>\n        </tr>\n</table>\n    \n    <h3 id=\"customer-child-object\">Customer [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>customer</code> child object. This is part of the <code>purchase_details</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>email_id</td>\n          <td><code>string</code></td>\n          <td>Customer's email address.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>kevin.bob@example.com</code></td>\n        </tr>\n        <tr>\n            <td>first_name</td>\n          <td><code>string</code></td>\n          <td>Customer's first name.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>Kevin</code></td>\n        </tr>\n        <tr>\n            <td>last_name</td>\n          <td><code>string</code></td>\n          <td>Customer's last name.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>Bob</code></td>\n        </tr>\n        <tr>\n            <td>customer_id</td>\n          <td><code>string</code></td>\n            <td>Unique identifier of the customer in the Plural database.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>19</code> characters.</ul></li>Example: <code>123456</code></td>\n        </tr>\n        <tr>\n            <td>mobile_number</td>\n          <td><code>string</code></td>\n          <td>Customer's mobile number.<ul><li>Minimum length: <code>9</code> characters.</li><li>Maximum length: <code>20</code> characters.</ul></li>Example: <code>9876543210</code></td>\n        </tr>\n        <tr>\n            <td>billing_address</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the billing address.<br><br><a href=\"#billing-address-child-object\">Learn more about our <code>billing_address</code> child object.</a></td>\n        </tr>\n        <tr>\n            <td>shipping_address</td>\n          <td><code>object</code></td>\n            <td>An object that contains the shipping address details.<br><br><a href=\"#shipping-address-child-object\">Learn more about our <code>shipping_address</code> child object.</a></td>\n        </tr>\n    </table>\n<h2 id=\"billing-address-child-object\">Billing Address [Child Object]</h2>\n  <p>The table below lists the various parameters in the <code>billing_address</code> child object. This is part of the <code>customer</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr><td>address1</td><td><code>string</code></td><td>Customer's billing address1.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>10 Downing Street Westminster London</code></td></tr>\n        <tr><td>address2</td><td><code>string</code></td><td>Customer's billing address2.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Oxford Street Westminster London</code></td></tr>\n        <tr><td>address3</td><td><code>string</code></td><td>Customer's billing address3.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Baker Street Westminster London</code></td></tr>\n        <tr><td>pincode</td><td><code>string</code></td><td>Pincode of the billing address.<ul><li>Min length: <code>6</code> characters.</li><li>Max length: <code>10</code> characters.</ul></li>Example: <code>51524036</code></td></tr>\n        <tr><td>city</td><td><code>string</code></td><td>City of the billing address. <ul><li>Max length: <code>50</code> characters. </ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>state</td><td><code>string</code></td><td>State of the billing address. <ul><li>Max length: <code>50<code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>country</td><td><code>string</code></td><td>Country of the billing address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>London</code></td></tr>\n    </table>\n\n    <h2 id=\"shipping-address-child-object\">Shipping Address [Child Object]</h2>\n  <p>The table below lists the various parameters in the <code>shipping_address</code> child object. This is part of the <code>customer</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr><td>address1</td><td><code>string</code></td><td>Customer's shipping address1.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>10 Downing Street Westminster London</code></td></tr>\n        <tr><td>address2</td><td><code>string</code></td><td>Customer's shipping address2.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Oxford Street Westminster London</code></td></tr>\n        <tr><td>address3</td><td><code>string</code></td><td>Customer's shipping address3.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Baker Street Westminster London</code></td></tr>\n        <tr><td>pincode</td><td><code>string</code></td><td>Pincode of the shipping address.<ul><li>Min length: <code>6</code> characters</li><li>Max length: <code>10</code> characters.</ul></li>Example: <code>51524036</code></td></tr>\n        <tr><td>city</td><td><code>string</code></td><td>City of the shipping address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>state</td><td><code>string</code></td><td>State of the shipping address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>country</td><td><code>string</code></td><td>Country of the shipping address. <ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>London</code></td>\n\t\t</tr>\n</tbody>\n    </table>\n\n</div>\n<div id=\"tab4\" class=\" tab-content\">\n      \n           \n        <body>\n          <p>The table below lists the various parameters returned in the Generate Checkout Link response objects.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <td>token</td>\n                <td><code>string</code></td>\n                <td>Token generated by our system for Plural Hosted Checkout.<br><br>Example: <span style=\"word-break: break-word;\"><code>eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c\n                  </code></span></td>\n            </tr>\n            <tr>\n                <td>order_id</td>\n                <td><code>string</code></td>\n                <td>Unique identifier of the order in the Plural database.<br><br>Example: <code>v1-5757575757-aa-hU1rUd</code></td>\n            </tr>\n            <tr>\n                <td>redirect_url</td>\n                <td><code>string</code></td>\n                <td>The checkout link generated on our system.<br><br>Example: <code>https://api.pluralonline.com/api/v3/checkout-bff/redirect/checkout?token=<<Redirect Token>></code></td>\n            </tr>\n            <tr>\n                <td>response_code</td>\n                <td><code>integer</code></td>\n                <td>Response code of the request.<br><br>Example: <code>200</code></td>\n            </tr>\n            <tr>\n                <td>response_message</td>\n                <td><code>string</code></td>\n                <td>Corresponding message to the response code.<br><br>Example: <code>Order Creation Successful</code>\n              </td>\n            </tr>\n    \t\t</table>\n      </div>\n</body>\n</html>"
}
[/block]


</details>

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
