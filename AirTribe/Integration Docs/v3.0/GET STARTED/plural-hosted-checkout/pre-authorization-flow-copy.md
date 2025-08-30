---
title: "Pre-Authorization Flow"
slug: "pre-authorization-flow-copy"
excerpt: "Learn how you can integrate with Plural APIs to start accepting payments on Plural Hosted Checkout."
hidden: true
createdAt: "Mon Mar 10 2025 10:49:56 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon May 12 2025 11:49:28 GMT+0000 (Coordinated Universal Time)"
---
Follow the below steps to integrate with Plural hosted checkout APIs in your application.

1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/plural-hosted-checkout-integration-steps#1-prerequisite-generate-token" >\[Prerequisite] Generate Token</a>
2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/plural-hosted-checkout-integration-steps#2-generate-checkout-link" >Generate Checkout Link</a>
3. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/plural-hosted-checkout-integration-steps#3-handle-payment" >Handle Payment</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/plural-hosted-checkout-integration-steps#31-store-payment-details-on-your-server" >Store Payment Details on Your Server</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/plural-hosted-checkout-integration-steps#32-verify-payment-signature" >Verify Payment Signature</a>
4. <a style="text-decoration:underline;" href="<https://developer.pluralonline.com/docs/plural-hosted-checkout-integration-steps#4-capture-order">Capture Order</a>
5. <a style="text-decoration:underline; " href="<https://developer.pluralonline.com/docs/plural-hosted-checkout-integration-steps#5-cancel-order">Cancel Order</a>

> 📘 Note
> 
> - Ensure you store your Client ID and Secret in your Backend securely.
> - Integrate our APIs on your backend system.
> - We strictly recommend not to call our APIs from the frontend.

## 1. [Prerequisite] Generate Token

Integrate our Generate Token API in your backend servers to generate the access token. Use the token generated to authenticate Plural APIs.

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

<details><summary>Click here for request and response parameter information.</summary>

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid #5A0083;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n        .required-label {\n            color: red;\n            font-size: 12px;\n            vertical-align: super;\n            margin-left: 4px;\n      }\n    </style>\n</head>\n<body>\n    <div class=\"tab-container\">\n        <div class=\"tab active\" data-target=\"tab1\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Request Parameters</div>\n\n        <div class=\"tab\" data-target=\"tab2\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Response Parameters</div>\n\n    <div id=\"tab1\" class=\"tab-content active\">\n      \n      <p>The table below lists the request parameters of our Generate Token API.</p>\n\n<table>\n    <thead>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td>client_id&nbsp;<span class=\"required-label\">required</span></td>\n          <td><code>string</code></td>\n            <td>\n                Unique client identifier in the Plural database.<br><br>\n              Example: <code>a17ce30e-f88e-4f81-ada1-c3b4909ed232</code><br><br>\n                <strong>Note:</strong> The Onboarding team has provided you with this information as part of the onboarding process.\n            </td>\n        </tr>\n        <tr>\n            <td>client_secret&nbsp;<span class=\"required-label\">required</span></td>\n          <td><code>string</code></td>\n            <td>\n                Unique client secret key provided while onboarding.<br><br>\n              Example: <code>fgwei7egyhuggwp39w8rh</code><br><br>\n                <strong>Note:</strong> The Onboarding team has provided you with this information as part of the onboarding process.\n            </td>\n        </tr>\n        <tr>\n            <td>grant_type&nbsp;<span class=\"required-label\">required</span></td>\n          <td><code>string</code></td>\n            <td>\n                The grant type to generate an access token.<br><br>\n              Accepted value: <code>client_credentials</code>\n            </td>\n        </tr>\n    </tbody>\n</table>\n\n      \n    </div>\n    <div id=\"tab2\" class=\" tab-content\">\n      \n      <p style=\"\">The table below lists the response parameters of our Generate Token API.</p> \n      <table>\n    <thead>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th> <!-- Ensure this is present -->\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td>access_token</td>\n            <td><code>string</code></td>\n            <td>\n                The access token generated by the system.<br><br>\n                • Minimum length: 1 character.<br>\n                • Maximum length: 8192 characters.<br><br>\n                Example: <code>eyJhbGciOiJIUzI1NiIsIn</code><br><br>\n                <strong>Note:</strong> Use this token in the authorization headers to authenticate Plural APIs.\n            </td>\n        </tr>\n        <tr>\n            <td>expires_at</td>\n            <td><code>string</code></td>\n            <td>\n                Access duration timestamp.<br><br>\n                Example: <code>2024-06-28T13:26:06.909140Z</code>\n            </td>\n        </tr>\n    </tbody>\n</table>\n\n      \n    </div>\n</body>\n</html>\n"
}
[/block]


</details>

## 2. Generate Checkout Link

To create a Plural-hosted checkout link, use our Generate Checkout Link API. Include the access token in the request headers for Bearer Authentication.

Below are the sample requests and response for a Generate Checkout Link API.

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
  "integration_mode": "IFRAME",
  "pre_auth": false,
  "allowed_payment_methods": [
    "CARD",
    "UPI",
    "NETBANKING",
    "POINTS",
    "WALLET"
  ],
  "notes": "order1",
  "purchase_details": {
    "bank_details": {
      "account_number": "500000004545",
      "ifsc_code": "BANK0000123",
      "bank_name": "Example Bank"
    },
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
  "allowed_payment_methods":[
    "CARD",
    "UPI",
    "NETBANKING",
    "POINTS",
    "WALLET"
  ],    
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
  "token": "<<Redirect Token>>",
  "order_id": "<<Order ID>>",
  "redirect_url": "https://api.pluralonline.com/api/v3/checkout-bff/redirect/checkout?token=<<Redirect Token>>",
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

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/v3.0/reference/orders-create" target="_blank">Generate Checkout Link API</a> documentation to learn more.

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/payments-test-card-details" target="_blank">Test Card Details</a> documentation to learn more.

> 📘 Note:
> 
> - You can set `pre-auth` as true to use pre-authorization flow for card payments only through hosted checkout.

## 3. Handle Payment

In the response to the Generate Checkout Link API, a `redirect_url` is returned. Use this URL to redirect your customers to the Plural-hosted checkout page to accept payment.

> 📘 Note:
> 
> **For `pre_auth` true**
> 
> - On successful payment we send the webhook event `ORDER_AUTHORIZED` and the status of the payment is updated to `AUTHORIZED`.
> - You can capture or cancel an order only when the order status is `AUTHORIZED`.
> 
> **For `pre_auth` false**
> 
> - On successful payment we send the webhook event `ORDER_PROCESSED` and the status of the payment is updated to `PROCESSED`

### 3.1 Store Payment Details on Your Server

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

### 3.2 Verify Payment Signature

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

> 📘 Important:
> 
> - With pre-authorization set to true, you can capture or cancel a payment for an order against a card payment.

## 4. Capture Order

Use this API to capture the payment against an order. On successful capture of an order the order status is updated as `processed`.

Shown below are the sample requests and sample response for a Capture Order API.

```curl cURL - UAT
curl --request PUT \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/orders/order_id/capture \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c ' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_capture_reference": "merchant-capture-ref-r4y",
  "capture_amount": {
    "value": 4000,
    "currency": "INR"
  }
}
'
```
```curl cURL - PROD
curl --request PUT \
     --url https://api.pluralpay.in/api/pay/v1/orders/order_id/capture \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c ' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_capture_reference": "merchant-capture-ref-r4y",
  "capture_amount": {
    "value": 4000,
    "currency": "INR"
  }
}
'
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
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
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
            "created_at": "2024-07-19T11:13:21.523Z"
          }
        ],
        "created_at": "2024-07-19T11:11:48.944Z",
        "updated_at": "2024-07-19T11:13:23.962Z"
      }
    ],
    "created_at": "2024-07-19T11:11:48.944Z",
    "updated_at": "2024-07-19T11:13:23.962Z"
  }
}
```

<details><summary>Click here for request and response parameter information.</summary>

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid #5A0083;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n        .required-label {\n            color: red;\n            font-size: 12px;\n            vertical-align: super;\n            margin-left: 4px;\n      }\n    </style>\n</head>\n<body>\n    <div class=\"tab-container\">\n        <div class=\"tab active\" data-target=\"tab5\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Request Parameters</div>\n\n        <div class=\"tab\" data-target=\"tab6\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Response Parameters</div>\n\n    <div id=\"tab5\" class=\"tab-content active\">\n      \n  \n  <p>The table below lists the path parameter of our Capture Order API.</p>\n\n<table>\n    <thead>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td>order_id&nbsp;<span class=\"required-label\">required</span></td>\n            <td><code>string</code></td>\n            <td>\n                Unique identifier of the order in the Plural database.<br><br>\n                Example: <code>v1-5757575757-aa-hU1rUd</code>\n            </td>\n        </tr>\n    </tbody>\n</table>\n\n<p>The table below lists the request parameter of our Capture Order API.</p>\n\n<table>\n    <thead>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td>merchant_capture_reference&nbsp;<span class=\"required-label\">required</span></td>\n            <td><code>string</code></td>\n            <td>\n                Enter a unique identifier for the capture order request.<ul><li>Maximum length: <code>50</code> characters.</li><li>Minimum length: <code>1</code> character.</ul></li>Example: <code>123456789</code><br><br>Supported characters:<ul><li><code>A-Z</code></li><li><code>a-z</code></li><li><code>0-9</code></li><li><code>-</code></li><li><code>\\</code></li><li><code>_</code></ul></li>\n            </td>\n        </tr>\n        <tr>\n            <td>capture_amount</td>\n            <td><code>object</code></td>\n            <td>\n              <strong>Mandatory for a partial capture request</strong>.<br><br>\n                An object that contains the capture amount details.<br><br><a href=\"#capture-amount-child-object\">Learn more about our <code>capture_amount</code> child object.\n            </td>\n        </tr>\n    </tbody>\n</table>\n<h2 id=\"capture-amount-child-object\"> Capture Amount [Child Object]</h2>\n<p>The table below lists the various parameters in the <code>capture_amount</code> child object. This object is part of the <code>capture_order</code> request object.</p>\n\n<table>\n    <thead>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td>value&nbsp;<span class=\"required-label\">required</span></td>\n            <td><code>integer</code></td>\n            <td>\n                The split amount in Paisa.<ul><li>\n              Minimum value: <code>100</code> (₹1).</li><li>\n              Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>\n                Example: <code>100</code>\n            </td>\n        </tr>\n        <tr>\n            <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n            <td><code>string</code></td>\n            <td>\n                Type of currency.<br><br>\n                Example: <code>INR</code>\n            </td>\n        </tr>\n    </tbody>\n</table>\n\n\n      \n    </div>\n    <div id=\"tab6\" class=\" tab-content\">\n      \n      <p>The table below lists the various parameters returned in the orders response objects.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>order_id</td>\n          <td><code>string</code></td>\n          <td>Unique identifier of the order in the Plural database.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>v1-5757575757-aa-hU1rUd</code></td>\n        </tr>\n        <tr>\n            <td>merchant_order_reference</td>\n          <td><code>string</code></td>\n          <td>Unique identifier entered while creating an order.<ul><li>Min length: <code>1</code> character.</li><li>Max length: <code>50</code> characters.</ul></li>Example: <code>82d57572-057c-4826-5775-385a52150554</code></td>\n        </tr>\n        <tr>\n            <td>type</td>\n          <td><code>string</code></td>\n          <td>Payment type.<br><br>Possible values:<ul><li><code>CHARGE</code></li><li><code>REFUND</code></td>\n        </tr>\n        <tr>\n            <td>status</td>\n          <td><code>string</code></td>\n          <td>Order status.<br><br>Possible values:<ul><li><code>CREATED</code>: When the order is successfully created.</li><li><code>PENDING</code>: When the order is linked against a payment request.</li><li><code>PROCESSED</code>: When the payment is received successfully.</li><li><code>AUTHORIZED</code>: <strong>Only when pre_auth is true</strong>. When the payment is ready for authorization.</li><li><code>CANCELLED</code>: When the payment gets cancelled.</li><li><code>ATTEMPTED</code>: When the payment is unsuccessful due to incorrect OTP. You can retry OTP</li><li><code>FAILED</code>: Payment acceptance failed for reasons such as cancel transactions, maximum retries for OTP verification etc.</li><li><code>FULLY_REFUNDED</code>: When the payment is completely refunded.</li><li><code>PARTIALLY_REFUNDED</code>: When the partial refund is successful.</ul></li></td>\n        </tr>\n        <tr>\n            <td>merchant_id</td>\n          <td><code>string</code></td>\n            <td>Unique identifier of the merchant in the Plural database.<br><br>Example: <code>123456</code></td>\n        </tr>\n        <tr>\n            <td>order_amount</td>\n          <td><code>object</code></td>\n            <td>An object that contains the transaction amount details.<br><br><a href=\"#order-amount-child-object-2\">Learn more about our <code>order_amount</code> child object.</td>\n        </tr>\n        <tr>\n            <td>notes</td>\n          <td><code>string</code></td>\n          <td>The note you want to show against an order.<br><br>Example: <code>Order1</code></td>\n        </tr>\n        <tr>\n            <td>pre_auth</td>\n          <td><code>boolean</code></td>\n          <td>The pre-authorization type.<br><br>Possible values:<ul><li><code>true</code>: When pre-authorization is needed.</li><li><code>false</code>: When pre-authorization is not required.</ul></li>Example: <code>false</code></td>\n        </tr>\n        <tr>\n            <td>allowed_payment_methods</td>\n          <td><code>array of strings</code></td>\n            <td>The type of payment methods you want to offer customers.<br><br>Accepted values:<ul><li><code>CARD</code></li><li><code>UPI</code></li><li><code>POINTS</code></li><li><code>NETBANKING</code></li><li><code>WALLET</code></li><li><code>CREDIT_EMI</code></li><li><code>DEBIT_EMI</code></ul></li>Example: <code>CARD</code><br><br><strong>Note</strong>: Before selecting a payment method, ensure it is configured for you.</td>\n        </tr>\n        <tr>\n            <td>callback_url</td>\n          <td><code>string</code></td>\n            <td>URL to redirect customers to success or failure pages.<br><br>Example: <code>https://sample-callback-url</code></td>\n        </tr>\n        <tr>\n            <td>purchase_details</td>\n          <td><code>object</code></td>\n            <td>An object that contains the purchase details.<br><br><a href=\"#purchase-details-child-object-1\">Learn more about the <code>purchase_details</code> child object.</a><br><br><strong>Note</strong>: The presence of the object key-values depends on the Input request.</td>\n        </tr>\n        <tr>\n            <td>payments</td>\n          <td><code>array of objects</code></td>\n            <td>An array of objects that contains the payment details.<br><br><a href=\"#payments-child-object\">Learn more about the <code>payments</code> child object.</a><br><br><strong>Note</strong>: Payment object is returned only for the orders linked with a payment.</td>\n        </tr>\n        <tr>\n            <td>created_at</td>\n          <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp when the order request was received.<br><br>Example: <code>2024-07-09T07:57:08.022Z</code></td>\n        </tr>\n        <tr>\n            <td>updated_at</td>\n          <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp when the order object was updated.<br><br>Example: <code>2024-07-09T07:57:08.022Z</code></td>\n        </tr>\n        <tr>\n          <td>integration_mode</td>\n          <td><code>string></code></td>\n          <td>Type of integration.<br><br>Example: <code>SEAMLESS</code>\n        </tr>\n        <tr>\n          <td>payment_retries_remaining</td>\n          <td><code>integer></code></td>\n          <td>Number of retry attempts left.<br><br>Example: <code>9</code>\n        </tr>\n    </table>\n\n <h2 id=\"order-amount-child-object-2\">Order Amount [Child Object]</h2>\n        <p> The table below lists the various parameters in the <code>order_amount</code> child object. <br><br>This object is part of the <code>create order</code> request object.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value</td>\n                <td><code>integer</code></td>\n                <td>\n                    Transaction amount in Paisa.<br><br><ul><li>\n                  Minimum value: <code>100</code> (₹1).</li><li>\n                  Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>\n          Example: <code>1000</code>\n                </td>\n            </tr>\n            <tr>\n                <td>currency</td>\n                <td><code>string</code></td>\n                <td>\n                    Type of currency.<br><br>\n                  Example: <code>INR</code>\n                </td>\n            </tr>\n        </tbody>\n    </table>\n\n<h2 id=\"purchase-details-child-object-1\">Purchase Details [Child Object]</h2>\n<p>The table below lists the various parameters in the <code>purchase_details</code> child object. This object is part of the <code>create order</code> request object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>customer</td>\n          <td><code>object</code></td>\n            <td>An object that contains the customer details.<br><br><a href=\"#customer-child-object-1\">Learn more about the <code>customer</code> child object.</td>\n        </tr>\n        <tr>\n            <td>merchant_metadata</td>\n            <td><code>object</code></td>\n            <td>An object of key-value pair that can be used to store additional information.<br><br>Example: <code>\"key1\": \"DD\"</code></td>\n        </tr>\n    </table>\n    \n    <h2 id=\"customer-child-object-1\">Customer [Child Object]</h2>\n<p>The table below lists the various parameters in the <code>customer</code> child object. This is part of the <code>purchase_details</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>email_id</td>\n          <td><code>string</code></td>\n          <td>Customer's email address.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>kevin.bob@example.com</code></td>\n        </tr>\n        <tr>\n            <td>first_name</td>\n          <td><code>string</code></td>\n          <td>Customer's first name.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>Kevin</code></td>\n        </tr>\n        <tr>\n            <td>last_name</td>\n          <td><code>string</code></td>\n          <td>Customer's last name.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>Bob</code></td>\n        </tr>\n        <tr>\n            <td>customer_id</td>\n          <td><code>string</code></td>\n            <td>Unique identifier of the customer in the Plural database.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>19</code> characters.</ul></li>Example: <code>123456</code></td>\n        </tr>\n        <tr>\n            <td>mobile_number</td>\n          <td><code>string</code></td>\n          <td>Customer's mobile number.<ul><li>Minimum length: <code>9</code> characters.</li><li>Maximum length: <code>20</code> characters.</ul></li>Example: <code>9876543210</code></td>\n        </tr>\n        <tr>\n            <td>billing_address</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the billing address.<br><br><a href=\"#billing-address-child-object-1\">Learn more about our <code>billing_address</code> child object.</td>\n        </tr>\n        <tr>\n            <td>shipping_address</td>\n          <td><code>object</code></td>\n            <td>An object that contains the shipping address details.<br><br><a href=\"#shipping-address-child-object-1\">Learn more about our <code>shipping_address</code> child object.</td>\n        </tr>\n    </table>\n<h2 id=\"billing-address-child-object-1\">Billing Address [Child Object]</h2>\n  <p>The table below lists the various parameters in the <code>billing_address</code> child object. This is part of the <code>customer</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr><td>address1</td><td><code>string</code></td><td>Customer's billing address1.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>10 Downing Street Westminster London</code></td></tr>\n        <tr><td>address2</td><td><code>string</code></td><td>Customer's billing address2.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Oxford Street Westminster London</code></td></tr>\n        <tr><td>address3</td><td><code>string</code></td><td>Customer's billing address3.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Baker Street Westminster London</code></td></tr>\n        <tr><td>pincode</td><td><code>string</code></td><td>Pincode of the billing address.<ul><li>Min length: <code>6</code> characters.</li><li>Max length: <code>10</code> characters.</ul></li>Example: <code>51524036</code></td></tr>\n        <tr><td>city</td><td><code>string</code></td><td>City of the billing address. <ul><li>Max length: <code>50</code> characters. </ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>state</td><td><code>string</code></td><td>State of the billing address. <ul><li>Max length: <code>50<code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>country</td><td><code>string</code></td><td>Country of the billing address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>London</code></td></tr>\n    </table>\n\n    <h2 id=\"shipping-address-child-object-1\">Shipping Address [Child Object]</h2>\n  <p>The table below lists the various parameters in the <code>shipping_address</code> child object. This is part of the <code>customer</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr><td>address1</td><td><code>string</code></td><td>Customer's shipping address1.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>10 Downing Street Westminster London</code></td></tr>\n        <tr><td>address2</td><td><code>string</code></td><td>Customer's shipping address2.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Oxford Street Westminster London</code></td></tr>\n        <tr><td>address3</td><td><code>string</code></td><td>Customer's shipping address3.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Baker Street Westminster London</code></td></tr>\n        <tr><td>pincode</td><td><code>string</code></td><td>Pincode of the shipping address.<ul><li>Min length: <code>6</code> characters</li><li>Max length: <code>10</code> characters.</ul></li>Example: <code>51524036</code></td></tr>\n        <tr><td>city</td><td><code>string</code></td><td>City of the shipping address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>state</td><td><code>string</code></td><td>State of the shipping address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>country</td><td><code>string</code></td><td>Country of the shipping address. <ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>London</code></td></tr>\n    </table>\n\n\n<h2 id=\"payments-child-object\">Payments [Child Object]</h2>\n<p>The table below lists the various parameters in the <code>payments</code> child object. This object is part of the <code>payments</code> sample response object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>id</td>\n          <td><code>string</code></td>\n            <td>Unique identifier of the payment in the Plural database.<ul><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>v1-5206071124-aa-mpLhF3-cc-l</code></td>\n        </tr>\n        <tr>\n            <td>merchant_payment_reference</td>\n          <td><code>string</code></td>\n            <td>A unique Payment Reference id sent by merchant.<br><br>Example: <code>008cf04b-a770-4777-854e-b1e6c1230609</code></td>\n        </tr>\n        <tr>\n            <td>status</td>\n          <td><code>string</code></td>\n          <td>Payment status.<br><br>Possible values:<ul></li><code>PENDING</code>: When the create payment API request is successfully received by Plural.</li><li><code>AUTHORIZED</code>: <strong>Only when <code>pre_auth</code> is true</strong>. When the payment is ready for authorization.</li><li><code>CANCELLED</code>: When the payment gets cancelled.</li><li><code>PROCESSED</code>: When the payment is successfully received by Plural.</li><li><code>FAILED</code>: When the payment fails, this can be for many reasons such as canceling payments, etc.</ul></li>Example: <code>PENDING</code></td>\n        </tr>\n        <tr>\n            <td>payment_amount</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the payment amount.<br><br><a href=\"#payment-amount-child-object\">Learn more about our <code>payment_amount</code> child object.</td>\n        </tr>\n        <tr>\n            <td>payment_method</td>\n          <td><code>string</code></td>\n          <td>Type of payment method.<br><br>Accepted values:<ul><li><code>CARD</code></li><li><code>UPI</code></li><li><code>POINTS</code></ul></li>Example: <code>CARD</code></td>\n        </tr>\n        <tr>\n            <td>payment_option</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the payment options.<br><br><a href=\"#payment-option-child-object\">Learn more about our <code>payment_option</code> child object.</td>\n        </tr>\n        <tr>\n            <td>acquirer_data</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the acquirer data.<br><br><a href=\"#acquirer-data-child-object\">Learn more about our <code>acquirer_data</code> child object.</td>\n        </tr>\n        <tr>\n            <td>capture_data</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the capture data.<br><br><a href=\"#capture-data-child-object\">Learn more about our <code>capture_data</code> child object.</a><br><br><strong>Note</strong>: The presence of the key-value pairs against this object depends on the pre-authorization type.</td>\n        </tr>\n        <tr>\n            <td>created_at</td>\n          <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp, when the create payment request was received by Plural.<br><br>Example: <code>2024-07-11T06:52:12.484Z</code></td>\n        </tr>\n        <tr>\n            <td>updated_at</td>\n          <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp, when the payment response object is updated.<br><br>Example: <code>2024-07-11T06:59:38.260Z</code></td>\n        </tr>\n    </table>\n\n<h3 id=\"payment-amount-child-object\">Payment Amount [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>payment_amount</code> child object. This object is part of the <code>payments</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>value</td>\n          <td><code>integer</code></td>\n          <td>The transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1).</li><li>Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>Example: <code>100</code></td>\n        </tr>\n        <tr>\n            <td>currency</td>\n          <td><code>string</code></td>\n          <td>Type of currency.<br><br>Example: <code>INR</code></td>\n        </tr>\n    </table>\n\n    <h3 id=\"payment-option-child-object\">Payment Option [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>payment_option</code> child object. This object is part of the <code>payments</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>card_data</td>\n          <td><code>object</code></td>\n            <td>An object that contains the card details.<br><br><a href=\"#card-data-child-object\">Learn more about our <code>card_data</code> child object.</td>\n        </tr>\n    </table>\n\n<h4 id=\"card-data-child-object\">Card Data [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>card_data</code> child object. This object is part of the <code>payment_option</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>card_type</td>\n          <td><code>string</code></td>\n          <td>Type of card.<br><br>Possible values:<ul><li><code>DEBIT</code></li><li><code>CREDIT</code></ul></li>Example: <code>CREDIT</code></td>\n        </tr>\n        <tr>\n            <td>network_name</td>\n          <td><code>string</code></td>\n          <td>Card network providers.<br><br>Example: <code>VISA</code></td>\n        </tr>\n        <tr>\n            <td>issuer_name</td>\n          <td><code>string</code></td>\n          <td>Card issuer entity.<br><br>Example: <code>HDFC</code></td>\n        </tr>\n        <tr>\n            <td>card_category</td>\n          <td><code>string</code></td>\n          <td>The card category type.<br><br>Possible values:<ul><li><code>CONSUMER</code></li><li><code>COMMERCIAL</code></li><li><code>PREMIUM</code></li><li><code>SUPER_PREMIUM</code></li><li><code>PLATINUM</code></li><li><code>OTHER</code></li><li><code>BUSINESS</code></li><li><code>GOVERNMENT_NOTES</code></li><li><code>PAYOUTS</code></li><li><code>ELITE</code></li><li><code>STANDARD</code></ul></li></td>\n        </tr>\n        <tr>\n            <td>country_code</td>\n          <td><code>string</code></td>\n          <td>Card issuer's country.<br><br>Example: <code>IND</code></td>\n        </tr>\n        <tr>\n            <td>token_txn_type</td>\n          <td><code>string</code></td>\n            <td>Transaction token type.<br><br>Possible values:<ul><li><code>ALT_TOKEN</code></li><li><code>NETWORK_TOKEN</code></li><li><code>ISSUER_TOKEN</code></ul></li>Example: <code>ALT_TOKEN</code></td>\n        </tr>\n    </table>\n\n    <h4 id=\"acquirer-data-child-object\">Acquirer Data [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>acquirer_data</code> child object. This object is part of the <code>payments</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>approval_code</td>\n          <td><code>string</code></td>\n            <td>Authorization code returned from acquirer against the payment.<br><br>Example: <code>030376</code></td>\n        </tr>\n        <tr>\n            <td>acquirer_reference</td>\n          <td><code>string</code></td>\n            <td>Unique reference returned from acquirer for the payment.<br><br>Example: <code>202455840588334</code></td>\n        </tr>\n        <tr>\n            <td>rrn</td>\n          <td><code>string</code></td>\n            <td>Retrieval reference number returned from acquirer for the payment.<br><br>Example: <code>419335023601</code></td>\n        </tr>\n        <tr>\n            <td>is_aggregator</td>\n          <td><code>boolean</code></td>\n          <td>The selected aggregator model type.<br><br>Accepted values:<ul><li><code>true</code> - Plural is responsible for settling funds related to this payment.</li><li><code>false</code> - Plural is not responsible for settling funds related to this payment.</ul></li><strong>Note</strong>:<ul><li>When is_aggregator is set to true, Plural acts as the acquirer on behalf of merchants, receiving funds from banks into a designated \"Nodal Account\".</li><li>When is_aggregator is set to false, the Merchant has a direct relationship with the bank, and the responsibility for settlement of funds lies with both of those parties.</ul></li></td>\n        </tr>\n    </table>\n\n    <h4 id=\"capture-data-child-object\">Capture Data [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>capture_data</code> child object. This object is part of the <code>payments</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>merchant_capture_reference</td>\n          <td><code>string</code></td>\n            <td>Unique identifier passed while creating the capture payment request.<br><br>Example: <code>5742ef1e-4606-4c11-5757-705f4d415b6d</code></td>\n        </tr>\n        <tr>\n            <td>capture_amount</td>\n          <td><code>object</code></td>\n            <td>An object that contains the capture amount details.<br><br><a href=\"#capture-amount-child-object-1\">Learn more about our <code>capture_amount</code> child object.</td>\n        </tr>\n        <tr>\n            <td>created_at</td>\n          <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp, when the amount was captured.<br><br>Example: <code>2024-07-11T11:52:12.484105Z</code></td>\n        </tr>\n    </table>\n\n    <h5 id=\"capture-amount-child-object-1\">Capture Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>capture_amount</code> child object. This object is part of the <code>capture_data</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>value</td>\n          <td><code>integer</code></td>\n          <td>The transaction amount is in Paisa.<ul><li>Minimum value: <code>100</code> (₹1). </li><li>Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>Example: <code>100</code></td>\n        </tr>\n        <tr>\n            <td>currency</td>\n          <td><code>string</code></td>\n          <td>Type of currency.<br><br>Example: <code>INR</code></td>\n        </tr>\n    </table>\n      \n    </div>\n</body>\n</html>\n"
}
[/block]


</details>

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/v3.0/reference/orders-capture" target="_blank">Capture Order API</a> documentation to learn more.

## 5. Cancel Order

Use this API to cancel the payment against an order.

Use the below endpoint to cancel the payment against the order.

```text Cancel Order Endpoint for UAT
PuT: https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/cancel
```
```text Cancel Order Endpoint for PROD
PUT: https://api.pluralpay.in/api/pay/v1/orders/{order_id}/cancel
```

Shown below is a sample response for a Cancel Order API.

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
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
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
        "created_at": "2024-07-19T11:27:55.664Z",
        "updated_at": "2024-07-19T11:28:52.487Z"
      }
    ],
    "created_at": "2024-07-19T11:27:55.664Z",
    "updated_at": "2024-07-19T11:28:52.487Z"
  }
}
```

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/v3.0/reference/orders-cancel" target="_blank">Cancel Order API</a> documentation to learn more.

### To Know Your Payment Status

To check your payment status, you can either rely on Webhook events or use our **Get Orders** APIs for real-time updates.

1. **Webhook Notification**: We send Webhook notifications on the successful payment or any changes to the payments object. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/developer-tools-webhook" target="_blank">Webhooks</a> documentation to learn more.
2. **Get Orders API**: Use our Get Orders API to know the real time status of the payment. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/order-manage#3-get-order-by-order-id" target="_blank">Manage Orders</a> documentation to learn more.

### Refunds

Plural processes refund directly to the customer's original payment method to prevent chargebacks.

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/payment-refund" target="_blank">Refunds</a> documentation to learn more.
