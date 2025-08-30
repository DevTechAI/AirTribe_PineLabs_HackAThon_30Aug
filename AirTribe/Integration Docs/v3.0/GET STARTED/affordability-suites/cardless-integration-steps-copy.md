---
title: "Cardless - Integration Steps"
slug: "cardless-integration-steps-copy"
excerpt: "Learn how to integrate the Plural Affordability Suite to provide your merchants with a seamless shopping experience."
hidden: true
createdAt: "Wed May 07 2025 09:52:08 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon May 12 2025 13:24:07 GMT+0000 (Coordinated Universal Time)"
---
Follow the below steps to integrate with Plural affordability suite in your application.

1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/credit-emi-integration-steps#1-prerequisite-generate-token" >\[Prerequisite] Generate Token</a>
2. <a href="https://developer.pluralonline.com/docs/credit-emi-integration-steps#2-offer-discovery" >Offer Discovery Cardless</a>
3. <a href="https://developer.pluralonline.com/docs/credit-emi-integration-steps#3-offer-validation" >Offer Validation</a>
4. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/credit-emi-integration-steps#4-create-order" >Create Order</a>
5. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/credit-emi-integration-steps#5-create-payment" >Create Payment</a>
6. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/credit-emi-integration-steps#6-handle-payment" >Handle Payment</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/credit-emi-integration-steps#61-store-payment-details-on-your-server" >Store Payment Details on Your Server</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/credit-emi-integration-steps#62-verify-payment-signature" >Verify Payment Signature</a>
7. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/credit-emi-integration-steps#7-get-order-by-order-id" >Get Order by Order ID</a>

> 📘 Note
> 
> - Ensure you store your Client ID and Secret in your Backend securely.
> - Integrate our APIs on your backend system.
> - We strictly recommend not to call our APIs from the frontend.

> 🚧 Watch Out
> 
> - To Integrate with Plural seamless checkout flow you must have a PCI compliance certificate.

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

<details><summary>Click here for request and response parameter information.</summary>

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid #5A0083;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n        .required-label {\n            color: red;\n            font-size: 12px;\n            vertical-align: super;\n            margin-left: 4px;\n    }\n    </style>\n</head>\n<body>\n     <div class=\"tab-container\">\n        <div class=\"tab active\" data-target=\"tab5\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Request Parameters</div>\n\n        <div class=\"tab\" data-target=\"tab6\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Response Parameters</div>\n\n    <div id=\"tab5\" class=\"tab-content active\">\n      \n      <p>The table below lists the request parameters of our Generate Token API.</p>\n\n<table>\n    <thead>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td> client_id&nbsp;<span class=\"required-label\">required</span>  \n          </td>\n          <td><code>string</code></td>\n            <td>\n                Unique client identifier in the Plural database.<br><br>\n              Example: <code>a17ce30e-f88e-4f81-ada1-c3b4909ed232</code><br><br>\n                <strong>Note:</strong> The Onboarding team has provided you with this information as part of the onboarding process.\n            </td>\n        </tr>\n        <tr>\n            <td>client_secret&nbsp;<span class=\"required-label\">required</span>              \n          </td>\n          <td><code>string</code></td>\n            <td>\n                Unique client secret key provided while onboarding.<br><br>\n              Example: <code>fgwei7egyhuggwp39w8rh</code><br><br>\n                <strong>Note:</strong> The Onboarding team has provided you with this information as part of the onboarding process.\n            </td>\n        </tr>\n        <tr>\n            <td>grant_type&nbsp;<span class=\"required-label\">required</span>\n          </td>\n          <td><code>string</code></td>\n            <td>\n                The grant type to generate an access token.<br><br>\n              Accepted value: <code>client_credentials</code>\n            </td>\n        </tr>\n    </tbody>\n</table>\n\n      \n    </div>\n    <div id=\"tab6\" class=\" tab-content\">\n      \n      <p style=\"\">The table below lists the response parameters of our Generate Token API.</p> \n      <table>\n    <thead>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th> <!-- Ensure this is present -->\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td>access_token</td>\n            <td><code>string</code></td>\n            <td>\n                The access token generated by the system.<br><br>\n                • Minimum length: 1 character.<br>\n                • Maximum length: 8192 characters.<br><br>\n                Example: <code>eyJhbGciOiJIUzI1NiIsIn</code><br><br>\n                <strong>Note:</strong> Use this token in the authorization headers to authenticate Plural APIs.\n            </td>\n        </tr>\n        <tr>\n            <td>expires_at</td>\n            <td><code>string</code></td>\n            <td>\n                Access duration timestamp.<br><br>\n                Example: <code>2024-06-28T13:26:06.909140Z</code>\n            </td>\n        </tr>\n    </tbody>\n</table>\n\n      \n    </div>\n</body>\n</html>"
}
[/block]


</details>

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/v3.0/reference/generate-token" target="_blank">Generate Token API</a> documentation to learn more.

## 2. Offer Discovery Cardless

Use this API to check the offers cardless and calculate the EMI.

Below are the sample requests and response for the Offer Discovery Cardless API.

### 2.1. Bank EMI

```curl cURL - UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/affordability/v1/offer/discovery \
     --compressed \
     --header 'Accept-Encoding: gzip' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "order_amount": {
    "currency": "INR",
    "value": 1200000
  }
}
'
```
```curl cURL - PROD
curl --request POST \
     --url https://api.pluralpay.in/api/affordability/v1/offer/discovery \
     --compressed \
     --header 'Accept-Encoding: gzip' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "order_amount": {
    "currency": "INR",
    "value": 1200000
  }
}
'
```
```json Sample Response
{
  "issuers": [
    {
      "id": "23",
      "name": "INDUSIND CC",
      "issuer_type": "CC_BANK",
      "priority": 1,
      "tenures": [
        {
          "tenure_id": "1",
          "name": "3 Months",
          "tenure_type": "MONTH",
          "tenure_value": 3,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1232139
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 410713
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1232139
          },
          "interest_amount": {
            "currency": "INR",
            "value": 32139
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "2",
          "name": "6 Months",
          "tenure_type": "MONTH",
          "tenure_value": 6,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1256616
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 209436
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1256616
          },
          "interest_amount": {
            "currency": "INR",
            "value": 56616
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "3",
          "name": "9 Months",
          "tenure_type": "MONTH",
          "tenure_value": 9,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1281411
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 142379
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1281411
          },
          "interest_amount": {
            "currency": "INR",
            "value": 81411
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "4",
          "name": "12 Months",
          "tenure_type": "MONTH",
          "tenure_value": 12,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1306524
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 108877
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1306524
          },
          "interest_amount": {
            "currency": "INR",
            "value": 106524
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "5",
          "name": "18 Months",
          "tenure_type": "MONTH",
          "tenure_value": 18,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1357686
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 75427
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1357686
          },
          "interest_amount": {
            "currency": "INR",
            "value": 157686
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "6",
          "name": "24 Months",
          "tenure_type": "MONTH",
          "tenure_value": 24,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1410120
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 58755
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1410120
          },
          "interest_amount": {
            "currency": "INR",
            "value": 210120
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        }
      ],
      "issuer_data": {}
    }
  ]
}
```

<details><summary>Click here for request and response parameter information.</summary>

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n   <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid #5A0083;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n    </style>\n</head>\n<body>\n    <div class=\"tab-container\">\n        <div class=\"tab active\" data-target=\"tab47\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Request Parameters</div>\n\n        <div class=\"tab\" data-target=\"tab48\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Response Parameters</div>\n\n    <div id=\"tab47\" class=\"tab-content active\">\n\n      <body>\n      \n      <p>The table below lists the request parameters of our <code>Offer Discovery API</code>.</p>\n\n<table>\n    <thead>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td>order_amount&nbsp;<span class=\"required-label\">required</span>\n          </td>\n            <td><code>object</code></td>\n            <td>\n                An object that contains the transaction amount details.<br><br>\n                <a href=\"#order-amount-child-object\">Learn more about our order_amount child object</a>.\n            </td>\n        </tr>\n    </tbody>\n</table>\n\n      <h3  id=\"order-amount-child-object\">Order Amount [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>order_amount</code> child object. This object is part of the <code>Offer Discovery API</code> request object.</p>\n\n<table>\n    <thead>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td>value&nbsp;<span class=\"required-label\">required</span>\n          </td>\n            <td><code>integer</code></td>\n            <td>\n                The transaction amount in Paisa.<ul><li>\n              Minimum value: <code>100</code> (₹1)</li><li>\n              Maximum value: <code>100000000</code> (₹10 lakh)</ul></li>\n                Example: <code>100</code>\n            </td>\n        </tr>\n        <tr>\n            <td>currency&nbsp;<span class=\"required-label\">required</span>\n          </td>\n            <td><code>string</code></td>\n            <td>\n                Type of currency.<br><br>\n                Example: <code>INR</code>\n            </td>\n        </tr>\n    </tbody>\n</table>\n      \n    </div>\n    <div id=\"tab48\" class=\" tab-content\">\n      <p>The table below lists the various parameters returned in the <code>offer discovery bank emi response</code> object.</p>\n  <table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>id</td>\n      <td><code>String</code></td>\n      <td>Unique identifier of the issuer id in the Plural database.<br><br>Example: <code>23</code></td>\n    </tr>\n    <tr>\n      <td>name</td>\n      <td><code>String</code></td>\n      <td>Name of the Issuer.<br><br>Example: <code>INDUSIND CC</code></td>\n    </tr>\n    <tr>\n      <td>display_name</td>\n      <td><code>string</code></td>\n      <td>Name of the issuer offering the offer.<br><br>Example: <code>INDUSIND</code></td>\n    </tr>\n    <tr>\n      <td>issuer_type</td>\n      <td><code>String</code></td>\n      <td>The type of the Issuer offering the offer.<br><br>Accepted values: <ul><li><code>CC_BANK</code></li><li><code>DC_BANK</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>priority</td>\n      <td><code>integer</code></td>\n      <td>The priority of the issuer providing the offer.<br><br>Example: <code>1</code></td>\n    </tr>\n    <tr>\n      <td>tenures</td>\n      <td><code>array of objects</code></td>\n      <td>An array of objects that contains the tenures details.<br><br><a href=\"#tenures-child-object\">Learn more about the <code>tenures</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>issuer_data</td>\n      <td><code>objects</code></td>\n      <td>An object that contains the issuer data details.<br><br><a href=\"#issuer-data-child-object\">Learn more about the <code>issuer_data</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n      <h3 id=\"tenures-child-object\">Tenures [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>tenures</code> object. This is part of the <code>offer discovery Bank EMI</code> response object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>tenure_id</td>\n      <td><code>String</code></td>\n      <td>Tenure id in the Plural database.<br><br>Example: <code>1</code></td>\n    </tr>\n    <tr>\n      <td>name</td>\n      <td><code>String</code></td>\n      <td>The name of the Issuer offering the offer.<br><br>Example: <code>3 Months</code></td>\n    </tr>\n    <tr>\n      <td>tenure_type</td>\n      <td><code>String</code></td>\n      <td>The type of the Tenure.<br><br>Accepted values: <ul><li><code>MONTH</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>tenure_value</td>\n      <td><code>integer</code></td>\n      <td>The value of the tenure.<br><br>Example: <code>3</code></td>\n    </tr>\n    <tr>\n      <td>issuer_offer_parameters</td>\n      <td><code>array of objects</code></td>\n      <td>An array of objects that contains the <code>issuer_offer_parameters</code> details.<br><br><a href=\"#issuer-offer-parameters-child-object\">Learn more about the <code>issuer_offer_parameters</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>details</td>\n      <td><code>array of objects</code></td>\n      <td>An array of objects that contains the <code>product details</code>.<br><br><a href=\"#details-child-object\">Learn more about the <code>details</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>discount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the discount details.<br><br><a href=\"#discount-child-object\">Learn more about the <code>discount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>loan_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the loan amount details.<br><br><a href=\"#loan-amount-child-object\">Learn more about the <code>loan_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>total_discount_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the total discount amount details.<br><br><a href=\"#total-discount-amount-child-object\">Learn more about the <code>total_discount_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>net_payment_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the net payment amount details.<br><br><a href=\"#net-payment-amount-child-object\">Learn more about the <code>net_payment_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>monthly_emi_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the monthly EMI amount details.<br><br><a href=\"#monthly-emi-amount-child-object\">Learn more about the <code>monthly_emi_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>total_emi_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the total EMI amount details.<br><br><a href=\"#total-emi-amount-child-object\">Learn more about the <code>total_emi_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>interest_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the interest amount details.<br><br><a href=\"#interest-amount-child-object\">Learn more about the <code>interest_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>total_subvention_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the total subvention amount details.<br><br><a href=\"#total-subvention-amount-child-object\">Learn more about the <code>total_subvention_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>interest_rate_percentage</td>\n      <td><code>float</code></td>\n      <td>Interest rate percentage for the tenure.<br><br>Example: <code>16.90</code></td>\n    </tr>\n    <tr>\n      <td>processing_fee_details</td>\n      <td><code>object</code></td>\n      <td>An object that contains the processing fee details.<br><br><a href=\"#processing-fee-details-child-object\">Learn more about the <code>processing_fee_details</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>convenience_fee_breakdown</td>\n      <td><code>object</code></td>\n      <td>An object that contains the convenience fee breakdown details.<br><br><a href=\"#convenience-fee-breakdown-child-object\">Learn more about our <code>convenience_fee_breakdown</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>cart_coupon_discount_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the cart coupon discount amount details.<br><br><a href=\"#cart-coupon-discount-amount-child-object\">Learn more about our <code>cart_coupon_discount_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>total_coupon_discount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the total coupon discount details.<br><br><a href=\"#total-coupon-discount-child-object\">Learn more about our <code>total_coupon_discount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>emi_type</td>\n      <td><code>strings</code></td>\n      <td>Type of EMI.<br><br>Example: <code>STANDARD</code><br><br>Accepted values: <ul><li><code>LOW_COST</code></li><li><code>NO_COST</code></li><li><code>STANDARD</code></li></ul></td>\n    </tr>\n  </tbody>\n</table>\n      <h4 id=\"issuer-offer-parameters-child-object\">Issuer Offer Parameters [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>issuer_offer_parameters</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>program_type</td>\n      <td><code>String</code></td>\n      <td>Unique identifier of the issuer id in the Plural database.<br><br>Example: <code>23</code></td>\n    </tr>\n    <tr>\n      <td>offer_id</td>\n      <td><code>String</code></td>\n      <td>Name of the Issuer.<br><br>Example: <code>INDUSIND CC</code></td>\n    </tr>\n    <tr>\n      <td>offer_parameter_id</td>\n      <td><code>String</code></td>\n      <td>The type of the Issuer offering the offer.<br><br>Accepted values: <ul><li><code>Credit</code></li><li><code>Debit</code></li><li><code>Cardless</code></li><li><code>NBFC</code></li></ul></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"details-child-object\">Details [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>details</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>product_code</td>\n      <td><code>String</code></td>\n      <td>Unique Product identifier of the product.<br><br>Example: <code>redmi_1</code></td>\n    </tr>\n    <tr>\n      <td>product_display_name</td>\n      <td><code>string</code></td>\n      <td>Name of the Product.<br><br>Example: <code>Oneplus 13R</code></td>\n    </tr>\n    <tr>\n      <td>brand_id</td>\n      <td><code>String</code></td>\n      <td>Unique brand identifier of the product.<br><br>Example: <code>3</code></td>\n    </tr>\n    <tr>\n      <td>product_offer_parameters</td>\n      <td><code>array of objects</code></td>\n      <td>An array of objects that contains the product offer schemes for the product EMI details.<br><br><a href=\"#product-offer-parameters-child-object\">Learn more about the <code>product_offer_parameters</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>product_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the product amount details.<br><br><a href=\"#product-amount-child-object\">Learn more about the <code>product_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>product_coupon_discount_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the product coupon discount amount details.<br><br><a href=\"#product-coupon-discount-amount-child-object\">Learn more about the <code>product_coupon_discount_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>subvention</td>\n      <td><code>object</code></td>\n      <td>An object that contains the subvention details.<br><br><a href=\"#subvention-child-object\">Learn more about the <code>subvention</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>discount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the product discount details.<br><br><a href=\"#discount-child-object\">Learn more about the <code>discount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>brand_name</td>\n      <td><code>string</code></td>\n      <td>Name of the Brand.<br><br>Example: <code>Oneplus</code></td>\n    </tr>\n    <tr>\n      <td>interest_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the interest amount details.<br><br><a href=\"#interest-amount-child-object\">Learn more about the <code>interest_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>interest_rate</td>\n      <td><code>double</code></td>\n      <td>Rate of interest applied on the product.<br><br>Example: <code>2</code></td>\n    </tr>\n    <tr>\n      <td>cart_coupon_discount_product_share</td>\n      <td><code>object</code></td>\n      <td>An object that contains the cart coupon discount product share details.<br><br><a href=\"#cart-coupon-discount-product-share-child-object\">Learn more about the <code>cart_coupon_discount_product_share</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n      <h5 id=\"product-offer-parameters-child-object\">Product Offer Parameters [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>product_offer_parameters</code> child object. This is part of the <code>details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>program_type</td>\n      <td><code>String</code></td>\n      <td>Type of the Program.<br><br>Example: <code>BRAND_EMI</code><br><br>Accepted values: <ul><li><code>BRAND_EMI</code></li><li><code>BANK_EMI</code></li><li><code>MERCHANT_BRAND_OFFER</code></li><li><code>MERCHANT_BANK_OFFER</code></li><li><code>BRAND_OFFER</code></li><li><code>MY_EMI</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>offer_id</td>\n      <td><code>string</code></td>\n      <td>Unique identifier of the offer.<br><br>Example: <code>309</code></td>\n    </tr>\n    <tr>\n      <td>offer_parameter_id</td>\n      <td><code>string</code></td>\n      <td>Unique offer parameter identifier.<br><br>Example: <code>20</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"product-amount-child-object\">Product Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>product_amount</code> child object. This is part of the <code>details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount in Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"product-coupon-discount-amount-child-object\">Product Coupon Discount Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>product_coupon_discount_amount</code> child object. This is part of the <code>details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount in Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n      <h5 id=\"subvention-child-object\">Subvention [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>subvention</code> child object. This is part of the <code>details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>subvention_type</td>\n      <td><code>String</code></td>\n      <td>Type of subvention.<br><br>Example: <code>INSTANT</code><br><br>Accepted values:<ul><li><code>INSTANT</code></li><li><code>POST</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>offer_type</td>\n      <td><code>string</code></td>\n      <td>Type of the offer.<br><br>Accepted values:<ul><li><code>LOW_COST</code></li><li><code>NO_COST</code></li><li><code>STANDARD</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>percentage</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n    <tr>\n      <td>amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the subvention amount details.<br><br><a href=\"#amount-child-object\">Learn more about the <code>amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>breakup</td>\n      <td><code>object</code></td>\n      <td>An object that contains the subvention breakup details.<br><br><a href=\"#breakup-child-object\">Learn more about the <code>breakup</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>max_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the maximum subvention amount details.<br><br><a href=\"#max-amount-child-object\">Learn more about the <code>max_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>min_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the minimum subvention amount details.<br><br><a href=\"#min-amount-child-object\">Learn more about the <code>min_amount</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n\n<h6 id=\"amount-child-object\">Amount [Child Object]</h6>\n<p>The table below lists the various parameters in the <code>amount</code> child object. This is part of the <code>subvention</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h6 id=\"breakup-child-object\">Breakup [Child Object]</h6>\n<p>The table below lists the various parameters in the <code>breakup</code> child object. This is part of the <code>subvention</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>brand</td>\n      <td><code>object</code></td>\n      <td>An object that contains the breakup details of the brand.<br><br><a href=\"#brand-child-object\">Learn more about the <code>brand</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n\n<h6 id=\"brand-child-object\">Brand [Child Object]</h6>\n<p>The table below lists the various parameters in the <code>brand</code> child object. This is part of the <code>breakup</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the breakup amount details of the brand.<br><br><a href=\"#amount-child-object\">Learn more about the <code>amount</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n      <h6 id=\"amount-child-object\">Amount [Child Object]</h6>\n<p>The table below lists the various parameters in the <code>amount</code> child object. This is part of the <code>brand</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"max-amount-child-object\">Max Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>max_amount</code> child object. This is part of the <code>subvention</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"min-amount-child-object\">Min Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>min_amount</code> child object. This is part of the <code>subvention</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"discount-child-object\">Discount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>discount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>discount_type</td>\n      <td><code>String</code></td>\n      <td>Type of discount.<br><br>Possible values:<ul><li><code>INSTANT</code></li><li><code>DEFERRED</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>discount_string</td>\n      <td><code>string</code></td>\n      <td>The additional discount provided by the offering entity after a specific period.<br><br>Example: <code>1000</code></td>\n    </tr>\n    <tr>\n      <td>percentage</td>\n      <td><code>Double</code></td>\n      <td>The discount percentage provided by the offering entity.<br><br>Example: <code>16.90</code></td>\n    </tr>\n    <tr>\n      <td>amount</td>\n      <td><code>string</code></td>\n      <td>Discount amount.<br><br>Example: <code>2000</code></td>\n    </tr>\n    <tr>\n      <td>max_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the maximum discount amount details.<br><br><a href=\"#max-amount-child-object1\">Learn more about the <code>max_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>min_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the minimum discount amount details.<br><br><a href=\"#min-amount-child-object1\">Learn more about the <code>min_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>discount_deferred_duration_value</td>\n      <td><code>integer</code></td>\n      <td>The duration value for the deferred discount.<br><br>Example:</td>\n    </tr>\n    <tr>\n      <td>discount_deferred_duration_type</td>\n      <td><code>string</code></td>\n      <td>Discount duration type deferred.<br><br>Possible values:<ul><li><code>DAY</code></li><li><code>MONTH</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>breakup</td>\n      <td><code>object</code></td>\n      <td>An object that contains the product offer details with breakup.<br><br><a href=\"#breakup-child-object1\">Learn more about the <code>breakup</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n      <h5 id=\"max-amount-child-object1\">Max Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>max_amount</code> child object. This is part of the <code>discount</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"min-amount-child-object1\">Min Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>min_amount</code> child object. This is part of the <code>discount</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"breakup-child-object1\">Breakup [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>breakup</code> child object. This is part of the <code>discount</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>merchant</td>\n      <td><code>object</code></td>\n      <td>An object that contains the merchant breakup details.<br><br><a href=\"#merchant-child-object\">Learn more about the <code>merchant</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>issuer</td>\n      <td><code>object</code></td>\n      <td>An object that contains the issuer breakup details.<br><br><a href=\"#issuer-child-object\">Learn more about the <code>issuer</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>brand</td>\n      <td><code>object</code></td>\n      <td>An object that contains the brand breakup details.<br><br><a href=\"#brand-child-object1\">Learn more about the <code>brand</code> child object.</a></td>\n    </tr>\n    <tr>\n      <td>dealer</td>\n      <td><code>object</code></td>\n      <td>An object that contains the dealer breakup details.<br><br><a href=\"#dealer-child-object\">Learn more about the <code>dealer</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n\n<h6 id=\"merchant-child-object\">Merchant [Child Object]</h6>\n<p>The table below lists the various parameters in the <code>merchant</code> child object. This is part of the <code>breakup</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the breakup amount details.<br><br><a href=\"#amount-child-object1\">Learn more about the <code>amount</code> child object.</a></td>\n    </tr>\n  </tbody>\n</table>\n\n<h6 id=\"issuer-child-object\">Issuer [Child Object]</h6>\n<p>The table below lists the various parameters in the <code>issuer</code> child object. This is part of the <code>breakup</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the breakup amount details.<br><br><a href=\"#amount-child-object1\">Learn more about the <code>amount</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n      <h6 id=\"brand-child-object1\">Brand [Child Object]</h6>\n<p>The table below lists the various parameters in the <code>brand</code> child object. This is part of the <code>breakup</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the breakup amount details.<br><br><a href=\"#amount-child-object1\">Learn more about the <code>amount</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n\n<h6 id=\"dealer-child-object\">Dealer [Child Object]</h6>\n<p>The table below lists the various parameters in the <code>dealer</code> child object. This is part of the <code>breakup</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n   </tr>\n     </thead>\n  <tbody>\n    <tr>\n      <td>amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the breakup amount details.<br><br><a href=\"#amount-child-object1\">Learn more about the <code>amount</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"amount-child-object1\">Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>amount</code> child object. This is part of the <code>breakup</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"interest-amount-child-object\">Interest Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>interest_amount</code> child object. This is part of the <code>details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"cart-coupon-discount-product-share-child-object\">Cart Coupon Discount Product Share [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>cart_coupon_discount_product_share</code> child object. This is part of the <code>details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n      <h4 id=\"loan-amount-child-object\">Loan Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>loan_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"total-discount-amount-child-object\">Total Discount Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>total_discount_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"net-payment-amount-child-object\">Net Payment Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>net_payment_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"monthly-emi-amount-child-object\">Monthly EMI Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>monthly_emi_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"total-emi-amount-child-object\">Total EMI Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>total_emi_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n      <h4 id=\"interest-amount-child-object\">Interest Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>interest_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"total-subvention-amount-child-object\">Total Subvention Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>total_subvention_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"processing-fee-details-child-object\">Processing Fee Details [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>processing_fee_details</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"convenience-fee-breakdown-child-object\">Convenience Fee Breakdown [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>convenience_fee_breakdown</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>fee_calculated_on_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the fee calculation amount details.<br><br><a href=\"#fee-calculated-on-amount-child-object\">Learn more about the <code>fee_calculated_on_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>fee_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the fee amount details.<br><br><a href=\"#fee-amount-child-object\">Learn more about the <code>fee_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>tax_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the tax amount details.<br><br><a href=\"#tax-amount-child-object\">Learn more about the <code>tax_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>additional_fee_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the additional fee amount details.<br><br><a href=\"#additional-fee-amount-child-object\">Learn more about the <code>additional_fee_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>maximum_fee_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the maximum fee amount details.<br><br><a href=\"#maximum-fee-amount-child-object\">Learn more about the <code>maximum_fee_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>applicable_fee_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the applicable fee amount details.<br><br><a href=\"#applicable-fee-amount-child-object\">Learn more about the <code>applicable_fee_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>subvented_fee_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the subvented fee amount details.<br><br><a href=\"#subvented-fee-amount-child-object\">Learn more about the <code>subvented_fee_amount</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n      <h5 id=\"fee-calculated-on-amount-child-object\">Fee Calculated on Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>fee_calculated_on_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"fee-amount-child-object\">Fee Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>fee_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"tax-amount-child-object\">Tax Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>tax_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"additional-fee-amount-child-object\">Additional Fee Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>additional_fee_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"maximum-fee-amount-child-object\">Maximum Fee Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>maximum_fee_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n      <h5 id=\"applicable-fee-amount-child-object\">Applicable Fee Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>applicable_fee_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"subvented-fee-amount-child-object\">Subvented Fee Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>subvented_fee_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"cart-coupon-discount-amount-child-object\">Cart Coupon Discount Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>cart_coupon_discount_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"total-coupon-discount-child-object\">Total Coupon Discount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>total_coupon_discount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h3 id=\"issuer-data-child-object\">Issuer Data [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>issuer_data</code> object. This is part of the offer discovery response object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>otp_length</td>\n      <td><code>integer</code></td>\n      <td>Length of the OTP.<br><br>Example: <code>4</code></td>\n    </tr>\n    <tr>\n      <td>otp_time_in_sec</td>\n      <td><code>integer</code></td>\n      <td>OTP validity time in seconds.<br><br>Example: <code>120</code></td>\n    </tr>\n    <tr>\n      <td>otp_retry_count</td>\n      <td><code>integer</code></td>\n      <td>Maximum OTP retry count.<br><br>Example:</td>\n    </tr>\n    <tr>\n      <td>is_consent_page_required</td>\n      <td><code>Boolean</code></td>\n      <td>Status of the required consent page.<ul><li><code>true</code>: When the consent page is required.</li><li><code>false</code>: When the consent page is not required.</li></ul></td>\n    </tr>\n    <tr>\n      <td>consent_data</td>\n      <td><code>String</code></td>\n      <td>Transaction consent data.<br><br>Example:</td>\n    </tr>\n    <tr>\n      <td>terms_and_conditions</td>\n      <td><code>String</code></td>\n      <td>Transaction terms and conditions.<br><br>Example:</td>\n    </tr>\n    <tr>\n      <td>show_key_fact_statement</td>\n      <td><code>Boolean</code></td>\n      <td>Key fact statement status.<ul><li><code>true</code>: When the key fact statement needs to be displayed.</li><li><code>false</code>: When the key fact statement is not required to be displayed.</li></ul></td>\n    </tr>\n    <tr>\n      <td>auth_type</td>\n      <td><code>String</code></td>\n      <td>Authentication type.<br><br>Accepted values:<ul><li><code>PENNY_DROP</code></li><li><code>OTP</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>penny_transaction_amount</td>\n      <td><code>string</code></td>\n      <td>Applicable amount for penny transaction.<br><br>Example: <code>100</code></td>\n    </tr>\n    <tr>\n      <td>is_tokenized_transaction_supported</td>\n      <td><code>Boolean</code></td>\n      <td>Tokenized transactions support status.<ul><li><code>true</code>: Tokenized transaction is supported.</li><li><code>false</code>: Tokenized transaction is not supported.</li></ul></td>\n    </tr>\n    <tr>\n      <td>pan_number_last_digit_count</td>\n      <td><code>String</code></td>\n      <td>Last digit count of PAN.</td>\n    </tr>\n    <tr>\n      <td>offer_validation_parameters_required</td>\n      <td><code>String</code></td>\n      <td>Parameters required in offer validation API.</td>\n    </tr>\n  </tbody>\n</table>\n\n      \n    </div>\n</body>\n</html>\n"
}
[/block]


</details>

### 2.2. Brand EMI

```curl cURL - UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/affordability/v1/offer/discovery \
     --compressed \
     --header 'Accept-Encoding: gzip' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "order_amount": {
    "currency": "INR",
    "value": 1200000
  },
  "product_details": [
    {
      "product_code": "xyz",
      "product_amount": {
        "currency": "INR",
        "value": 1200000
      },
      "product_coupon_discount_amount": {
        "currency": "INR",
        "value": 1200000
      }
    }
  ],
  "cart_coupon_discount_amount": {
    "currency": "INR",
    "value": 1200000
  }
}
'
```
```curl cURL - PROD
curl --request POST \
     --url https://api.pluralpay.in/api/affordability/v1/offer/discovery \
     --compressed \
     --header 'Accept-Encoding: gzip' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "order_amount": {
    "currency": "INR",
    "value": 1200000
  },
  "product_details": [
    {
      "product_code": "xyz",
      "product_amount": {
        "currency": "INR",
        "value": 1200000
      },
      "product_coupon_discount_amount": {
        "currency": "INR",
        "value": 1200000
      }
    }
  ],
  "cart_coupon_discount_amount": {
    "currency": "INR",
    "value": 1200000
  }
}
'
```
```json Sample Response
{
  "issuers": [
    {
      "id": "25",
      "name": "PNB CC",
      "issuer_type": "CC_BANK",
      "priority": 1,
      "tenures": [
        {
          "tenure_id": "1",
          "name": "3 Months",
          "tenure_type": "MONTH",
          "tenure_value": 3,
          "issuer_offer_parameters": [
            {
              "program_type": "BRAND_EMI",
              "offer_id": "309",
              "offer_parameter_id": "20"
            }
          ],
          "details": [
            {
              "product_code": "redmi_1",
              "brand_id": "3",
              "product_offer_parameters": [
                {
                  "program_type": "BRAND_OFFER",
                  "offer_id": "309",
                  "offer_parameter_id": "20"
                }
              ],
              "product_amount": {
                "currency": "INR",
                "value": 2000000
              },
              "subvention": {
                "subvention_type": "INSTANT",
                "percentage": 5,
                "amount": {
                  "currency": "INR",
                  "value": 85714
                },
                "breakup": {
                  "brand": {
                    "amount": {
                      "currency": "INR",
                      "value": 85714
                    }
                  }
                }
              },
              "discount": {
                "discount_type": "INSTANT",
                "percentage": 10,
                "amount": {
                  "currency": "INR",
                  "value": 200000
                },
                "breakup": {
                  "merchant": {
                    "amount": {
                      "currency": "INR",
                      "value": 100000
                    }
                  },
                  "brand": {
                    "amount": {
                      "currency": "INR",
                      "value": 100000
                    }
                  }
                }
              }
            }
          ],
          "discount": {
            "discount_type": "INSTANT",
            "percentage": 10,
            "amount": {
              "currency": "INR",
              "value": 200000
            },
            "breakup": {
              "merchant": {
                "amount": {
                  "currency": "INR",
                  "value": 100000
                }
              },
              "brand": {
                "amount": {
                  "currency": "INR",
                  "value": 100000
                }
              }
            }
          },
          "loan_amount": {
            "currency": "INR",
            "value": 1714286
          },
          "total_discount_amount": {
            "currency": "INR",
            "value": 200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1760202
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 586734
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1760202
          },
          "interest_amount": {
            "currency": "INR",
            "value": 45916
          },
          "total_subvention_amount": {
            "currency": "INR",
            "value": 85714
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "NO_COST"
        },
        {
          "tenure_id": "12",
          "name": "36 Months",
          "tenure_type": "MONTH",
          "tenure_value": 36,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1562",
              "offer_parameter_id": "63812"
            }
          ],
          "details": [],
          "loan_amount": {
            "currency": "INR",
            "value": 2000000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 2531304
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 70314
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 2531304
          },
          "interest_amount": {
            "currency": "INR",
            "value": 531304
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "2",
          "name": "6 Months",
          "tenure_type": "MONTH",
          "tenure_value": 6,
          "issuer_offer_parameters": [
            {
              "program_type": "BRAND_EMI",
              "offer_id": "309",
              "offer_parameter_id": "20"
            }
          ],
          "details": [
            {
              "product_code": "redmi_1",
              "brand_id": "3",
              "product_offer_parameters": [
                {
                  "program_type": "BRAND_OFFER",
                  "offer_id": "309",
                  "offer_parameter_id": "20"
                }
              ],
              "product_amount": {
                "currency": "INR",
                "value": 2000000
              },
              "subvention": {
                "subvention_type": "POST",
                "percentage": 5,
                "amount": {
                  "currency": "INR",
                  "value": 90000
                },
                "breakup": {
                  "brand": {
                    "amount": {
                      "currency": "INR",
                      "value": 90000
                    }
                  }
                }
              },
              "discount": {
                "discount_type": "INSTANT",
                "percentage": 10,
                "amount": {
                  "currency": "INR",
                  "value": 200000
                },
                "breakup": {
                  "merchant": {
                    "amount": {
                      "currency": "INR",
                      "value": 100000
                    }
                  },
                  "brand": {
                    "amount": {
                      "currency": "INR",
                      "value": 100000
                    }
                  }
                }
              }
            }
          ],
          "discount": {
            "discount_type": "INSTANT",
            "percentage": 10,
            "amount": {
              "currency": "INR",
              "value": 200000
            },
            "breakup": {
              "merchant": {
                "amount": {
                  "currency": "INR",
                  "value": 100000
                }
              },
              "brand": {
                "amount": {
                  "currency": "INR",
                  "value": 100000
                }
              }
            }
          },
          "loan_amount": {
            "currency": "INR",
            "value": 1800000
          },
          "total_discount_amount": {
            "currency": "INR",
            "value": 200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1884924
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 314154
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1884924
          },
          "interest_amount": {
            "currency": "INR",
            "value": 84924
          },
          "total_subvention_amount": {
            "currency": "INR",
            "value": 90000
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "NO_COST"
        },
        {
          "tenure_id": "3",
          "name": "9 Months",
          "tenure_type": "MONTH",
          "tenure_value": 9,
          "issuer_offer_parameters": [
            {
              "program_type": "BRAND_EMI",
              "offer_id": "309",
              "offer_parameter_id": "20"
            }
          ],
          "details": [
            {
              "product_code": "redmi_1",
              "brand_id": "3",
              "product_offer_parameters": [
                {
                  "program_type": "BRAND_OFFER",
                  "offer_id": "309",
                  "offer_parameter_id": "20"
                }
              ],
              "product_amount": {
                "currency": "INR",
                "value": 2000000
              },
              "subvention": {
                "subvention_type": "POST",
                "percentage": 5,
                "amount": {
                  "currency": "INR",
                  "value": 90000
                },
                "breakup": {
                  "brand": {
                    "amount": {
                      "currency": "INR",
                      "value": 90000
                    }
                  }
                }
              },
              "discount": {
                "discount_type": "INSTANT",
                "percentage": 10,
                "amount": {
                  "currency": "INR",
                  "value": 200000
                },
                "breakup": {
                  "merchant": {
                    "amount": {
                      "currency": "INR",
                      "value": 100000
                    }
                  },
                  "brand": {
                    "amount": {
                      "currency": "INR",
                      "value": 100000
                    }
                  }
                }
              }
            }
          ],
          "discount": {
            "discount_type": "INSTANT",
            "percentage": 10,
            "amount": {
              "currency": "INR",
              "value": 200000
            },
            "breakup": {
              "merchant": {
                "amount": {
                  "currency": "INR",
                  "value": 100000
                }
              },
              "brand": {
                "amount": {
                  "currency": "INR",
                  "value": 100000
                }
              }
            }
          },
          "loan_amount": {
            "currency": "INR",
            "value": 1800000
          },
          "total_discount_amount": {
            "currency": "INR",
            "value": 200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1922112
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 213568
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1922112
          },
          "interest_amount": {
            "currency": "INR",
            "value": 122112
          },
          "total_subvention_amount": {
            "currency": "INR",
            "value": 90000
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 29900
            }
          },
          "emi_type": "LOW_COST"
        },
        {
          "tenure_id": "4",
          "name": "12 Months",
          "tenure_type": "MONTH",
          "tenure_value": 12,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "loan_amount": {
            "currency": "INR",
            "value": 2000000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 2177532
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 181461
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 2177532
          },
          "interest_amount": {
            "currency": "INR",
            "value": 177532
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "5",
          "name": "18 Months",
          "tenure_type": "MONTH",
          "tenure_value": 18,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1595",
              "offer_parameter_id": "63850"
            }
          ],
          "details": [],
          "loan_amount": {
            "currency": "INR",
            "value": 2000000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 2262816
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 125712
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 2262816
          },
          "interest_amount": {
            "currency": "INR",
            "value": 262816
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "6",
          "name": "24 Months",
          "tenure_type": "MONTH",
          "tenure_value": 24,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "loan_amount": {
            "currency": "INR",
            "value": 2000000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 2350224
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 97926
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 2350224
          },
          "interest_amount": {
            "currency": "INR",
            "value": 350224
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        }
      ],
      "issuer_data": {}
    }
  ]
}
```

<details><summary>Click here for request and response parameter information.</summary>

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n   <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid #5A0083;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n    </style>\n</head>\n<body>\n    <div class=\"tab-container\">\n        <div class=\"tab active\" data-target=\"tab49\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Request Parameters</div>\n\n        <div class=\"tab\" data-target=\"tab50\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Response Parameters</div>\n\n    <div id=\"tab49\" class=\"tab-content active\">\n\n      <body>\n      <p>The table below lists the request parameters of our Offer Discovery API.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>order_amount&nbsp;<span class=\"required-label\">required</span>\n      </td>\n      <td><code>object</code></td>\n      <td>An object that contains the transaction amount details.<br><br><a href=\"#order-amount-child-object2\">Learn more about our <code>order_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>product_details&nbsp;<span class=\"required-label\">required</span>\n      </td>\n      <td><code>object</code></td>\n      <td>An object that contains product details.<br><br><a href=\"#product-details-child-object\">Learn more about our <code>product_details</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>cart_coupon_discount_amount</td>\n      <td><code>string</code></td>\n      <td>An object that contains the cart coupon discount details.<br><br><a href=\"#cart-coupon-discount-amount-child-object2\">Learn more about our <code>cart_coupon_discount_amount</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n\n<h3 id=\"order-amount-child-object2\">Order Amount [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>order_amount</code> child object. This object is part of the <code>offer Discovery Brand EMI</code> sample request object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>value&nbsp;<span class=\"required-label\">required</span>\n      </td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n    <tr>\n      <td>currency&nbsp;<span class=\"required-label\">required</span>\n      </td>\n      <td><code>string</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h3 id=\"product-details-child-object\">Product Details [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>product_details</code> child object. This is part of the <code>offer Discovery Brand EMI</code> sample request object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>product_code&nbsp;<span class=\"required-label\">required</span>\n      </td>\n      <td><code>String</code></td>\n      <td>Unique Product identifier of the product.<br><br>Example: <code>redmi_1</code></td>\n    </tr>\n    <tr>\n      <td>product_amount&nbsp;<span class=\"required-label\">required</span>\n      </td>\n      <td><code>object</code></td>\n      <td>An object that contains the product amount details.<br><br><a href=\"#product-amount-child-object2\">Learn more about the <code>product_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>product_coupon_discount_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the product coupon discount details.<br><br><a href=\"#product-coupon-discount-amount-child-object2\">Learn more about the <code>product_coupon_discount_amount</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"product-amount-child-object2\">Product Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>product_amount</code> child object. This object is part of the <code>product_details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>value&nbsp;<span class=\"required-label\">required</span>\n      </td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n    <tr>\n      <td>currency&nbsp;<span class=\"required-label\">required</span>\n      </td>\n      <td><code>string</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"product-coupon-discount-amount-child-object2\">Product Coupon Discount Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>product_coupon_discount_amount</code> child object. This object is part of the <code>product_details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>value&nbsp;<span class=\"required-label\">required</span>\n      </td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n    <tr>\n      <td>currency&nbsp;<span class=\"required-label\">required</span>\n      </td>\n      <td><code>string</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h3 id=\"cart-coupon-discount-amount-child-object2\">Cart Coupon Discount Amount [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>cart_coupon_discount_amount</code> child object. This object is part of the <code>offer Discovery Brand EMI</code> sample request object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>value&nbsp;<span class=\"required-label\">required</span>\n      </td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n    <tr>\n      <td>currency&nbsp;<span class=\"required-label\">required</span>\n      </td>\n      <td><code>string</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n  </tbody>\n</table>\n      \n      \n    </div>\n    <div id=\"tab50\" class=\" tab-content\">\n      <p>The table below lists the various parameters returned in the <code>offer discovery brand emi response</code> object.</p>\n  <table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>id</td>\n      <td><code>String</code></td>\n      <td>Unique identifier of the issuer id in the Plural database.<br><br>Example: <code>23</code></td>\n    </tr>\n    <tr>\n      <td>name</td>\n      <td><code>String</code></td>\n      <td>Name of the Issuer.<br><br>Example: <code>INDUSIND CC</code></td>\n    </tr>\n    <tr>\n      <td>display_name</td>\n      <td><code>string</code></td>\n      <td>Name of the issuer offering the offer.<br><br>Example: <code>INDUSIND</code></td>\n    </tr>\n    <tr>\n      <td>issuer_type</td>\n      <td><code>String</code></td>\n      <td>The type of the Issuer offering the offer.<br><br>Accepted values: <ul><li><code>CC_BANK</code></li><li><code>DC_BANK</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>priority</td>\n      <td><code>integer</code></td>\n      <td>The priority of the issuer providing the offer.<br><br>Example: <code>1</code></td>\n    </tr>\n    <tr>\n      <td>tenures</td>\n      <td><code>array of objects</code></td>\n      <td>An array of objects that contains the tenures details.<br><br><a href=\"#tenures-child-object2\">Learn more about the <code>tenures</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>issuer_data</td>\n      <td><code>objects</code></td>\n      <td>An object that contains the issuer data details.<br><br><a href=\"#issuer-data-child-object2\">Learn more about the <code>issuer_data</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n      <h3 id=\"tenures-child-object2\">Tenures [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>tenures</code> object. This is part of the offer discovery response object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>tenure_id</td>\n      <td><code>String</code></td>\n      <td>Tenure id in the Plural database.<br><br>Example: <code>1</code></td>\n    </tr>\n    <tr>\n      <td>name</td>\n      <td><code>String</code></td>\n      <td>The name of the Issuer offering the offer.<br><br>Example: <code>3 Months</code></td>\n    </tr>\n    <tr>\n      <td>tenure_type</td>\n      <td><code>String</code></td>\n      <td>The type of the Tenure.<br><br>Accepted values: <ul><li><code>MONTH</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>tenure_value</td>\n      <td><code>integer</code></td>\n      <td>The value of the tenure.<br><br>Example: <code>3</code></td>\n    </tr>\n    <tr>\n      <td>issuer_offer_parameters</td>\n      <td><code>array of objects</code></td>\n      <td>An array of objects that contains the <code>issuer_offer_parameters</code> details.<br><br><a href=\"#issuer-offer-parameters-child-object2\">Learn more about the <code>issuer_offer_parameters</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>details</td>\n      <td><code>array of objects</code></td>\n      <td>An array of objects that contains the <code>product details</code>.<br><br><a href=\"#details-child-object2\">Learn more about the <code>details</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>discount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the discount details.<br><br><a href=\"#discount-child-object3\">Learn more about the <code>discount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>loan_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the loan amount details.<br><br><a href=\"#loan-amount-child-object2\">Learn more about the <code>loan_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>total_discount_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the total discount amount details.<br><br><a href=\"#total-discount-amount-child-object2\">Learn more about the <code>total_discount_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>net_payment_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the net payment amount details.<br><br><a href=\"#net-payment-amount-child-object2\">Learn more about the <code>net_payment_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>monthly_emi_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the monthly EMI amount details.<br><br><a href=\"#monthly-emi-amount-child-object2\">Learn more about the <code>monthly_emi_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>total_emi_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the total EMI amount details.<br><br><a href=\"#total-emi-amount-child-object2\">Learn more about the <code>total_emi_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>interest_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the interest amount details.<br><br><a href=\"#interest-amount-child-object2\">Learn more about the <code>interest_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>total_subvention_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the total subvention amount details.<br><br><a href=\"#total-subvention-amount-child-object2\">Learn more about the <code>total_subvention_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>interest_rate_percentage</td>\n      <td><code>float</code></td>\n      <td>Interest rate percentage for the tenure.<br><br>Example: <code>16.90</code></td>\n    </tr>\n    <tr>\n      <td>processing_fee_details</td>\n      <td><code>object</code></td>\n      <td>An object that contains the processing fee details.<br><br><a href=\"#processing-fee-details-child-object2\">Learn more about the <code>processing_fee_details</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>convenience_fee_breakdown</td>\n      <td><code>object</code></td>\n      <td>An object that contains the convenience fee breakdown details.<br><br><a href=\"#convenience-fee-breakdown-child-object2\">Learn more about our <code>convenience_fee_breakdown</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>cart_coupon_discount_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the cart coupon discount amount details.<br><br><a href=\"#cart-coupon-discount-amount-child-object3\">Learn more about our <code>cart_coupon_discount_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>total_coupon_discount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the total coupon discount details.<br><br><a href=\"#total-coupon-discount-child-object2\">Learn more about our <code>total_coupon_discount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>emi_type</td>\n      <td><code>strings</code></td>\n      <td>Type of EMI.<br><br>Example: <code>STANDARD</code><br><br>Accepted values: <ul><li><code>LOW_COST</code></li><li><code>NO_COST</code></li><li><code>STANDARD</code></li></ul></td>\n    </tr>\n  </tbody>\n</table>\n      <h4 id=\"issuer-offer-parameters-child-object2\">Issuer Offer Parameters [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>issuer_offer_parameters</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>program_type</td>\n      <td><code>String</code></td>\n      <td>Unique identifier of the issuer id in the Plural database.<br><br>Example: <code>23</code></td>\n    </tr>\n    <tr>\n      <td>offer_id</td>\n      <td><code>String</code></td>\n      <td>Name of the Issuer.<br><br>Example: <code>INDUSIND CC</code></td>\n    </tr>\n    <tr>\n      <td>offer_parameter_id</td>\n      <td><code>String</code></td>\n      <td>The type of the Issuer offering the offer.<br><br>Accepted values: <ul><li><code>Credit</code></li><li><code>Debit</code></li><li><code>Cardless</code></li><li><code>NBFC</code></li></ul></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"details-child-object2\">Details [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>details</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>product_code</td>\n      <td><code>String</code></td>\n      <td>Unique Product identifier of the product.<br><br>Example: <code>redmi_1</code></td>\n    </tr>\n    <tr>\n      <td>product_display_name</td>\n      <td><code>string</code></td>\n      <td>Name of the Product.<br><br>Example: <code>Oneplus 13R</code></td>\n    </tr>\n    <tr>\n      <td>brand_id</td>\n      <td><code>String</code></td>\n      <td>Unique brand identifier of the product.<br><br>Example: <code>3</code></td>\n    </tr>\n    <tr>\n      <td>product_offer_parameters</td>\n      <td><code>array of objects</code></td>\n      <td>An array of objects that contains the product offer schemes for the product EMI details.<br><br><a href=\"#product-offer-parameters-child-object3\">Learn more about the <code>product_offer_parameters</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>product_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the product amount details.<br><br><a href=\"#product-amount-child-object3\">Learn more about the <code>product_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>product_coupon_discount_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the product coupon discount amount details.<br><br><a href=\"#product-coupon-discount-amount-child-object3\">Learn more about the <code>product_coupon_discount_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>subvention</td>\n      <td><code>object</code></td>\n      <td>An object that contains the subvention details.<br><br><a href=\"#subvention-child-object2\">Learn more about the <code>subvention</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>discount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the product discount details.<br><br><a href=\"#discount-child-object4\">Learn more about the <code>discount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>brand_name</td>\n      <td><code>string</code></td>\n      <td>Name of the Brand.<br><br>Example: <code>Oneplus</code></td>\n    </tr>\n    <tr>\n      <td>interest_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the interest amount details.<br><br><a href=\"#interest-amount-child-object2\">Learn more about the <code>interest_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>interest_rate</td>\n      <td><code>double</code></td>\n      <td>Rate of interest applied on the product.<br><br>Example: <code>2</code></td>\n    </tr>\n    <tr>\n      <td>cart_coupon_discount_product_share</td>\n      <td><code>object</code></td>\n      <td>An object that contains the cart coupon discount product share details.<br><br><a href=\"#cart-coupon-discount-product-share-child-object2\">Learn more about the <code>cart_coupon_discount_product_share</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n      <h5 id=\"product-offer-parameters-child-object3\">Product Offer Parameters [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>product_offer_parameters</code> child object. This is part of the <code>details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>program_type</td>\n      <td><code>String</code></td>\n      <td>Type of the Program.<br><br>Example: <code>BRAND_EMI</code><br><br>Accepted values: <ul><li><code>BRAND_EMI</code></li><li><code>BANK_EMI</code></li><li><code>MERCHANT_BRAND_OFFER</code></li><li><code>MERCHANT_BANK_OFFER</code></li><li><code>BRAND_OFFER</code></li><li><code>MY_EMI</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>offer_id</td>\n      <td><code>string</code></td>\n      <td>Unique identifier of the offer.<br><br>Example: <code>309</code></td>\n    </tr>\n    <tr>\n      <td>offer_parameter_id</td>\n      <td><code>string</code></td>\n      <td>Unique offer parameter identifier.<br><br>Example: <code>20</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"product-amount-child-object3\">Product Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>product_amount</code> child object. This is part of the <code>details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount in Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"product-coupon-discount-amount-child-object3\">Product Coupon Discount Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>product_coupon_discount_amount</code> child object. This is part of the <code>details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount in Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n      <h5 id=\"subvention-child-object2\">Subvention [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>subvention</code> child object. This is part of the <code>details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>subvention_type</td>\n      <td><code>String</code></td>\n      <td>Type of subvention.<br><br>Example: <code>INSTANT</code><br><br>Accepted values:<ul><li><code>INSTANT</code></li><li><code>POST</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>offer_type</td>\n      <td><code>string</code></td>\n      <td>Type of the offer.<br><br>Accepted values:<ul><li><code>LOW_COST</code></li><li><code>NO_COST</code></li><li><code>STANDARD</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>percentage</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n    <tr>\n      <td>amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the subvention amount details.<br><br><a href=\"#amount-child-object3\">Learn more about the <code>amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>breakup</td>\n      <td><code>object</code></td>\n      <td>An object that contains the subvention breakup details.<br><br><a href=\"#breakup-child-object2\">Learn more about the <code>breakup</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>max_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the maximum subvention amount details.<br><br><a href=\"#max-amount-child-object2\">Learn more about the <code>max_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>min_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the minimum subvention amount details.<br><br><a href=\"#min-amount-child-object2\">Learn more about the <code>min_amount</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n\n<h6 id=\"amount-child-object3\">Amount [Child Object]</h6>\n<p>The table below lists the various parameters in the <code>amount</code> child object. This is part of the <code>subvention</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h6 id=\"breakup-child-object2\">Breakup [Child Object]</h6>\n<p>The table below lists the various parameters in the <code>breakup</code> child object. This is part of the <code>subvention</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>brand</td>\n      <td><code>object</code></td>\n      <td>An object that contains the breakup details of the brand.<br><br><a href=\"#brand-child-object5\">Learn more about the <code>brand</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n\n<h6 id=\"brand-child-object5\">Brand [Child Object]</h6>\n<p>The table below lists the various parameters in the <code>brand</code> child object. This is part of the <code>breakup</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the breakup amount details of the brand.<br><br><a href=\"#amount-child-object4\">Learn more about the <code>amount</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n      <h6 id=\"amount-child-object4\">Amount [Child Object]</h6>\n<p>The table below lists the various parameters in the <code>amount</code> child object. This is part of the <code>brand</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"max-amount-child-object2\">Max Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>max_amount</code> child object. This is part of the <code>subvention</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"min-amount-child-object2\">Min Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>min_amount</code> child object. This is part of the <code>subvention</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"discount-child-object4\">Discount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>discount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>discount_type</td>\n      <td><code>String</code></td>\n      <td>Type of discount.<br><br>Possible values:<ul><li><code>INSTANT</code></li><li><code>DEFERRED</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>discount_string</td>\n      <td><code>string</code></td>\n      <td>The additional discount provided by the offering entity after a specific period.<br><br>Example: <code>1000</code></td>\n    </tr>\n    <tr>\n      <td>percentage</td>\n      <td><code>Double</code></td>\n      <td>The discount percentage provided by the offering entity.<br><br>Example: <code>16.90</code></td>\n    </tr>\n    <tr>\n      <td>amount</td>\n      <td><code>string</code></td>\n      <td>Discount amount.<br><br>Example: <code>2000</code></td>\n    </tr>\n    <tr>\n      <td>max_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the maximum discount amount details.<br><br><a href=\"#max-amount-child-object3\">Learn more about the <code>max_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>min_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the minimum discount amount details.<br><br><a href=\"#min-amount-child-object3\">Learn more about the <code>min_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>discount_deferred_duration_value</td>\n      <td><code>integer</code></td>\n      <td>The duration value for the deferred discount.<br><br>Example:</td>\n    </tr>\n    <tr>\n      <td>discount_deferred_duration_type</td>\n      <td><code>string</code></td>\n      <td>Discount duration type deferred.<br><br>Possible values:<ul><li><code>DAY</code></li><li><code>MONTH</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>breakup</td>\n      <td><code>object</code></td>\n      <td>An object that contains the product offer details with breakup.<br><br><a href=\"#breakup-child-object3\">Learn more about the <code>breakup</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n      <h5 id=\"max-amount-child-object3\">Max Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>max_amount</code> child object. This is part of the <code>discount</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"min-amount-child-object3\">Min Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>min_amount</code> child object. This is part of the <code>discount</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"breakup-child-object3\">Breakup [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>breakup</code> child object. This is part of the <code>discount</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>merchant</td>\n      <td><code>object</code></td>\n      <td>An object that contains the merchant breakup details.<br><br><a href=\"#merchant-child-object2\">Learn more about the <code>merchant</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>issuer</td>\n      <td><code>object</code></td>\n      <td>An object that contains the issuer breakup details.<br><br><a href=\"#issuer-child-object2\">Learn more about the <code>issuer</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>brand</td>\n      <td><code>object</code></td>\n      <td>An object that contains the brand breakup details.<br><br><a href=\"#brand-child-object6\">Learn more about the <code>brand</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>dealer</td>\n      <td><code>object</code></td>\n      <td>An object that contains the dealer breakup details.<br><br><a href=\"#dealer-child-object2\">Learn more about the <code>dealer</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n\n<h6 id=\"merchant-child-object2\">Merchant [Child Object]</h6>\n<p>The table below lists the various parameters in the <code>merchant</code> child object. This is part of the <code>breakup</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the breakup amount details.<br><br><a href=\"#amount-child-object5\">Learn more about the <code>amount</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n\n<h6 id=\"issuer-child-object2\">Issuer [Child Object]</h6>\n<p>The table below lists the various parameters in the <code>issuer</code> child object. This is part of the <code>breakup</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the breakup amount details.<br><br><a href=\"#amount-child-object5\">Learn more about the <code>amount</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n      <h6 id=\"brand-child-object6\">Brand [Child Object]</h6>\n<p>The table below lists the various parameters in the <code>brand</code> child object. This is part of the <code>breakup</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the breakup amount details.<br><br><a href=\"#amount-child-object5\">Learn more about the <code>amount</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n\n<h6 id=\"dealer-child-object2\">Dealer [Child Object]</h6>\n<p>The table below lists the various parameters in the <code>dealer</code> child object. This is part of the <code>breakup</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n   </tr>\n     </thead>\n  <tbody>\n    <tr>\n      <td>amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the breakup amount details.<br><br><a href=\"#amount-child-object5\">Learn more about the <code>amount</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"amount-child-object5\">Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>amount</code> child object. This is part of the <code>breakup</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"interest-amount-child-object2\">Interest Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>interest_amount</code> child object. This is part of the <code>details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"cart-coupon-discount-product-share-child-object2\">Cart Coupon Discount Product Share [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>cart_coupon_discount_product_share</code> child object. This is part of the <code>details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n      <h4 id=\"loan-amount-child-object2\">Loan Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>loan_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"total-discount-amount-child-object2\">Total Discount Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>total_discount_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"net-payment-amount-child-object2\">Net Payment Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>net_payment_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"monthly-emi-amount-child-object2\">Monthly EMI Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>monthly_emi_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"total-emi-amount-child-object2\">Total EMI Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>total_emi_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n      <h4 id=\"interest-amount-child-object2\">Interest Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>interest_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"total-subvention-amount-child-object2\">Total Subvention Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>total_subvention_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"processing-fee-details-child-object2\">Processing Fee Details [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>processing_fee_details</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"convenience-fee-breakdown-child-object2\">Convenience Fee Breakdown [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>convenience_fee_breakdown</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>fee_calculated_on_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the fee calculation amount details.<br><br><a href=\"#fee-calculated-on-amount-child-object2\">Learn more about the <code>fee_calculated_on_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>fee_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the fee amount details.<br><br><a href=\"#fee-amount-child-object2\">Learn more about the <code>fee_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>tax_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the tax amount details.<br><br><a href=\"#tax-amount-child-object2\">Learn more about the <code>tax_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>additional_fee_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the additional fee amount details.<br><br><a href=\"#additional-fee-amount-child-object2\">Learn more about the <code>additional_fee_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>maximum_fee_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the maximum fee amount details.<br><br><a href=\"#maximum-fee-amount-child-object2\">Learn more about the <code>maximum_fee_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>applicable_fee_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the applicable fee amount details.<br><br><a href=\"#applicable-fee-amount-child-object2\">Learn more about the <code>applicable_fee_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>subvented_fee_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the subvented fee amount details.<br><br><a href=\"#subvented-fee-amount-child-object2\">Learn more about the <code>subvented_fee_amount</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n      <h5 id=\"fee-calculated-on-amount-child-object2\">Fee Calculated on Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>fee_calculated_on_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"fee-amount-child-object2\">Fee Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>fee_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"tax-amount-child-object2\">Tax Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>tax_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"additional-fee-amount-child-object2\">Additional Fee Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>additional_fee_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"maximum-fee-amount-child-object2\">Maximum Fee Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>maximum_fee_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n      <h5 id=\"applicable-fee-amount-child-object2\">Applicable Fee Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>applicable_fee_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"subvented-fee-amount-child-object2\">Subvented Fee Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>subvented_fee_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"cart-coupon-discount-amount-child-object3\">Cart Coupon Discount Amount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>cart_coupon_discount_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"total-coupon-discount-child-object2\">Total Coupon Discount [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>total_coupon_discount</code> child object. This is part of the <code>tenures</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h3 id=\"issuer-data-child-object2\">Issuer Data [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>issuer_data</code> object. This is part of the offer discovery response object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>otp_length</td>\n      <td><code>integer</code></td>\n      <td>Length of the OTP.<br><br>Example: <code>4</code></td>\n    </tr>\n    <tr>\n      <td>otp_time_in_sec</td>\n      <td><code>integer</code></td>\n      <td>OTP validity time in seconds.<br><br>Example: <code>120</code></td>\n    </tr>\n    <tr>\n      <td>otp_retry_count</td>\n      <td><code>integer</code></td>\n      <td>Maximum OTP retry count.<br><br>Example:</td>\n    </tr>\n    <tr>\n      <td>is_consent_page_required</td>\n      <td><code>Boolean</code></td>\n      <td>Status of the required consent page.<ul><li><code>true</code>: When the consent page is required.</li><li><code>false</code>: When the consent page is not required.</li></ul></td>\n    </tr>\n    <tr>\n      <td>consent_data</td>\n      <td><code>String</code></td>\n      <td>Transaction consent data.<br><br>Example:</td>\n    </tr>\n    <tr>\n      <td>terms_and_conditions</td>\n      <td><code>String</code></td>\n      <td>Transaction terms and conditions.<br><br>Example:</td>\n    </tr>\n    <tr>\n      <td>show_key_fact_statement</td>\n      <td><code>Boolean</code></td>\n      <td>Key fact statement status.<ul><li><code>true</code>: When the key fact statement needs to be displayed.</li><li><code>false</code>: When the key fact statement is not required to be displayed.</li></ul></td>\n    </tr>\n    <tr>\n      <td>auth_type</td>\n      <td><code>String</code></td>\n      <td>Authentication type.<br><br>Accepted values:<ul><li><code>PENNY_DROP</code></li><li><code>OTP</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>penny_transaction_amount</td>\n      <td><code>string</code></td>\n      <td>Applicable amount for penny transaction.<br><br>Example: <code>100</code></td>\n    </tr>\n    <tr>\n      <td>is_tokenized_transaction_supported</td>\n      <td><code>Boolean</code></td>\n      <td>Tokenized transactions support status.<ul><li><code>true</code>: Tokenized transaction is supported.</li><li><code>false</code>: Tokenized transaction is not supported.</li></ul></td>\n    </tr>\n    <tr>\n      <td>pan_number_last_digit_count</td>\n      <td><code>String</code></td>\n      <td>Last digit count of PAN.</td>\n    </tr>\n    <tr>\n      <td>offer_validation_parameters_required</td>\n      <td><code>String</code></td>\n      <td>Parameters required in offer validation API.</td>\n    </tr>\n  </tbody>\n</table>\n\n      \n    </div>\n</body>\n</html>\n"
}
[/block]


</details>

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/offer-discovery-create" target="_blank">Offer Discovery API</a> documentation to learn more.

## 3. Offer Validation

Use this API for validating applied offers.

Below is a sample request and response for the Offer Validation API.

```curl cURL - UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/affordability/v1/offer/validate \
     --compressed \
     --header 'Accept-Encoding: gzip' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "order_amount": {
    "value": 2000000,
    "currency": "INR"
  },
  "payment_amount": {
    "value": 1950000,
    "currency": "INR"
  },
  "offer_data": {
    "offer_details": {
      "tenure": {
        "loan_amount": {
          "currency": "INR",
          "value": 1950000
        },
        "total_discount_amount": {
          "currency": "INR",
          "value": 50000
        },
        "net_payment_amount": {
          "currency": "INR",
          "value": 2015358
        },
        "monthly_emi_amount": {
          "currency": "INR",
          "value": 671786
        },
        "total_emi_amount": {
          "currency": "INR",
          "value": 2015358
        },
        "interest_amount": {
          "currency": "INR",
          "value": 65358
        },
        "processing_fee_details": {
          "amount": {
            "currency": "INR",
            "value": 19900
          }
        },
        "tenure_id": "1",
        "name": "3 Months",
        "tenure_type": "MONTH",
        "tenure_value": 3,
        "issuer_offer_parameters": [
          {
            "program_type": "BANK_EMI",
            "offer_id": "1564",
            "offer_parameter_id": "63814"
          },
          {
            "program_type": "MERCHANT_BANK_OFFER",
            "offer_id": "1523",
            "offer_parameter_id": "63566"
          }
        ],
        "discount": {
          "discount_type": "INSTANT",
          "amount": {
            "currency": "INR",
            "value": 50000
          }
        },
        "interest_rate_percentage": 20,
        "emi_type": "STANDARD"
      },
      "id": "6",
      "name": "HDFC CC",
      "issuer_type": "CC_BANK",
      "priority": 1
    }
  },
  "payment_method": "CREDIT_EMI",
  "payment_option": {
    "card_details": {
      "card_number": "4690000046910000"
    }
  }
}
'
```
```curl cURL - PROD
curl --request POST \
     --url https://api.pluralpay.in/api/affordability/v1/offer/validate \
     --compressed \
     --header 'Accept-Encoding: gzip' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "order_amount": {
    "value": 2000000,
    "currency": "INR"
  },
  "payment_amount": {
    "value": 1950000,
    "currency": "INR"
  },
  "offer_data": {
    "offer_details": {
      "tenure": {
        "loan_amount": {
          "currency": "INR",
          "value": 1950000
        },
        "total_discount_amount": {
          "currency": "INR",
          "value": 50000
        },
        "net_payment_amount": {
          "currency": "INR",
          "value": 2015358
        },
        "monthly_emi_amount": {
          "currency": "INR",
          "value": 671786
        },
        "total_emi_amount": {
          "currency": "INR",
          "value": 2015358
        },
        "interest_amount": {
          "currency": "INR",
          "value": 65358
        },
        "processing_fee_details": {
          "amount": {
            "currency": "INR",
            "value": 19900
          }
        },
        "tenure_id": "1",
        "name": "3 Months",
        "tenure_type": "MONTH",
        "tenure_value": 3,
        "issuer_offer_parameters": [
          {
            "program_type": "BANK_EMI",
            "offer_id": "1564",
            "offer_parameter_id": "63814"
          },
          {
            "program_type": "MERCHANT_BANK_OFFER",
            "offer_id": "1523",
            "offer_parameter_id": "63566"
          }
        ],
        "discount": {
          "discount_type": "INSTANT",
          "amount": {
            "currency": "INR",
            "value": 50000
          }
        },
        "interest_rate_percentage": 20,
        "emi_type": "STANDARD"
      },
      "id": "6",
      "name": "HDFC CC",
      "issuer_type": "CC_BANK",
      "priority": 1
    }
  },
  "payment_method": "CREDIT_EMI",
  "payment_option": {
    "card_details": {
      "card_number": "4690000046910000"
    }
  }
}
'
```
```json Sample Response
{
  "code": "ELIGIBLE",
  "message": "Offer is Eligible"
}
```

<details><summary>Click here for request and response parameter information.</summary>

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n   <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid #5A0083;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n    </style>\n</head>\n<body>\n    <div class=\"tab-container\">\n        <div class=\"tab active\" data-target=\"tab51\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Request Parameters</div>\n\n        <div class=\"tab\" data-target=\"tab52\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Response Parameters</div>\n\n    <div id=\"tab51\" class=\"tab-content active\">\n\n      <body>\n    <p>The table below lists the request parameters of our Offer Validation API.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>payment_method&nbsp;<span class=\"required-label\">required</span></td>\n                <td>string</td>\n                <td>Type of payment method you want to use to accept a payment.<br><br>Accepted values:<ul><li><code>CREDIT_EMI</code></li><li><code>DEBIT_EMI</code></li><li><code>CARDLESS_EMI</code></li></ul></td>\n            </tr>\n            <tr>\n                <td>order_amount&nbsp;<span class=\"required-label\">required</span></td>\n                <td>object</td>\n                <td>An object that contains the transaction amount details.<br><br><a href=\"#order-amount-child-object31\">Learn more about our <code>order_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>payment_amount&nbsp;<span class=\"required-label\">required</span></td>\n                <td>object</td>\n                <td>An object that contains the payment amount details after the offer has been applied.<br><br><a href=\"#payment-amount-child-object31\">Learn more about our <code>payment_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>offer_data&nbsp;<span class=\"required-label\">required</span></td>\n                <td>object</td>\n                <td>An object that contains details related to the offer.<br><br><a href=\"#offer-data-child-object31\">Learn more about our <code>offer_data</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>customer_details</td>\n                <td>object</td>\n                <td>An object that contains details related to the customer.<br><br><a href=\"#customer-details-child-object31\">Learn more about our <code>customer_details</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h3 id=\"order-amount-child-object31\">Order Amount [Child Object]</h3>\n    <p>The table below lists the various parameters in the <code>order_amount</code> child object. This object is part of the <code>offer validation</code> sample request object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>string</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n</html>\n<body>\n    <h3 id=\"payment-amount-child-object31\">Payment Amount [Child Object]</h3>\n    <p>The table below lists the various parameters in the <code>payment_amount</code> child object. This object is part of the <code>offer validation</code> sample request object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>string</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h3 id=\"offer-data-child-object31\">Offer Data [Child Object]</h3>\n    <p>The table below lists the various parameters in the <code>offer_data</code> child object. This object is part of the <code>offer validation</code> sample request object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>offer_details</td>\n                <td>object</td>\n                <td>An object that contains details related to the offer issuer.<br><br><a href=\"#offer-details-child-object31\">Learn more about our <code>offer_details</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h4 id=\"offer-details-child-object31\">Offer Details [Child Object]</h4>\n    <p>The table below lists the various parameters in the <code>offer_details</code> child object. This object is part of the <code>offer_data</code> sample request object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>id</td>\n                <td>string</td>\n                <td>The ID of the Issuer offering the offer.</td>\n            </tr>\n            <tr>\n                <td>name</td>\n                <td>string</td>\n                <td>The name of the Issuer offering the offer.</td>\n            </tr>\n            <tr>\n                <td>issuer_type</td>\n                <td>string</td>\n                <td>The type of the Issuer offering the offer.<br><br>Example:<ul><li><code>CC_BANK</code></li><li><code>DC_BANK</code></li></ul></td>\n            </tr>\n            <tr>\n                <td>priority</td>\n                <td>string</td>\n                <td>The priority of the Issuer offering the offer.</td>\n            </tr>\n            <tr>\n                <td>tenure</td>\n                <td>object</td>\n                <td>The EMI tenure details related to the offer.<br><br><a href=\"#tenures-child-object31\">Learn more about our <code>tenure</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n</html>\n<body>\n    <h4 id=\"tenures-child-object31\">Tenure [Child Object]</h4>\n    <p>The table below lists the various parameters in the <code>tenures</code> object. This is part of the <code>offer_details</code> request object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>tenure_id&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Tenure id in the Plural database.<br><br>Example: <code>1</code></td>\n            </tr>\n            <tr>\n                <td>name&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n              <td>The name of the Tenure.</td>\n                </tr>\n            <tr>\n                <td>tenure_type&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>The type of the Tenure.<br><br>Accepted values:<ul><li><code>DAY</code></li><li><code>MONTH</code></li></ul></td>\n            </tr>\n            <tr>\n                <td>tenure_value</td>\n                <td>integer</td>\n                <td>The value of the tenure.<br><br>Example: <code>3</code></td>\n            </tr>\n            <tr>\n                <td>issuer_offer_parameters&nbsp;<span class=\"required-label\">required</span></td>\n                <td>string</td>\n                <td>List of Offer Schemes for the tenure.</td>\n            </tr>\n            <tr>\n                <td>details</td>\n                <td>array of objects</td>\n                <td>An array of objects that contains the <code>product details</code>.<br><br><a href=\"#details-child-object31\">Learn more about the <code>details</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>discount</td>\n                <td>object</td>\n                <td>An object that contains the discount details.<br><br><a href=\"#discount-child-object31\">Learn more about the <code>discount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>loan_amount</td>\n                <td>object</td>\n                <td>An object that contains the loan amount details.<br><br><a href=\"#loan-amount-child-object31\">Learn more about the <code>loan_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>total_discount_amount</td>\n                <td>object</td>\n                <td>Total discount amount for the tenure.<br><br><a href=\"#total-discount-amount-child-object31\">Learn more about the <code>total_discount_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>net_payment_amount</td>\n                <td>object</td>\n                <td>An object that contains the net payment amount details.<br><br><a href=\"#net-payment-amount-child-object31\">Learn more about the <code>net_payment_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>monthly_emi_amount</td>\n                <td>object</td>\n                <td>An object that contains the monthly EMI amount details.<br><br><a href=\"#monthly-emi-amount-child-object31\">Learn more about the <code>monthly_emi_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>total_emi_amount</td>\n                <td>object</td>\n                <td>An object that contains the total EMI amount details.<br><br><a href=\"#total-emi-amount-child-object31\">Learn more about the <code>total_emi_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>interest_amount</td>\n                <td>object</td>\n                <td>An object that contains the interest amount details.<br><br><a href=\"#interest-amount-child-object31\">Learn more about the <code>interest_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>total_subvention_amount</td>\n                <td>object</td>\n                <td>An object that contains the total subvention amount details.<br><br><a href=\"#total-subvention-amount-child-object31\">Learn more about the <code>total_subvention_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>interest_rate_percentage&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Interest rate percentage for the tenure.</td>\n            </tr>\n            <tr>\n                <td>processing_fee_details</td>\n                <td>object</td>\n                <td>Processing fee details for the tenure.<br><br><a href=\"#processing-fee-details-child-object31\">Learn more about the <code>processing_fee_details</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>emi_type&nbsp;<span class=\"required-label\">required</span></td>\n                <td>strings</td>\n                <td>Type of EMI.<br><br>Example: <code>STANDARD</code><br><br>Accepted values:<ul><li><code>LOW_COST</code></li><li><code>NO_COST</code></li><li><code>STANDARD</code></li></ul></td>\n            </tr>\n            <tr>\n                <td>convenience_fee_breakdown</td>\n                <td>object</td>\n                <td>An object that contains the convenience fee breakdown details.<br><br><a href=\"#convenience-fee-breakdown-child-object31\">Learn more about the <code>convenience_fee_breakdown</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>cart_coupon_discount_amount</td>\n                <td>object</td>\n                <td>An object that contains the cart coupon discount amount details.<br><br><a href=\"#cart-coupon-discount-amount-child-object31\">Learn more about the <code>cart_coupon_discount_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>total_coupon_discount</td>\n                <td>object</td>\n                <td>An object that contains the total coupon discount details.<br><br><a href=\"#total-coupon-discount-child-object31\">Learn more about the <code>total_coupon_discount</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n</html>\n<body>\n    <h4 id=\"details-child-object31\">Details [Child Object]</h4>\n    <p>The table below lists the various parameters in the <code>details</code> child object. This is part of the <code>tenures</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>product_code</td>\n                <td>String</td>\n                <td>Unique Product identifier of the product.<br><br>Example: <code>redmi_1</code></td>\n            </tr>\n            <tr>\n                <td>product_display_name</td>\n                <td>String</td>\n                <td>Name of the Product.<br><br>Example: <code>Oneplus 13R</code></td>\n            </tr>\n            <tr>\n                <td>brand_id</td>\n                <td>String</td>\n                <td>Unique brand identifier of the product.<br><br>Example: <code>3</code></td>\n            </tr>\n            <tr>\n                <td>product_offer_parameters</td>\n                <td>array of objects</td>\n                <td>An array of objects that contains the product offer schemes for the product EMI details.<br><br><a href=\"#product-offer-parameters-child-object31\">Learn more about the <code>product_offer_parameters</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>product_amount</td>\n                <td>object</td>\n                <td>An object that contains the product amount details.<br><br><a href=\"#product-amount-child-object31\">Learn more about the <code>product_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>product_coupon_discount_amount</td>\n                <td>object</td>\n                <td>An object that contains the product coupon discount amount details.<br><br><a href=\"#product-coupon-discount-amount-child-object31\">Learn more about the <code>product_coupon_discount_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>subvention</td>\n                <td>object</td>\n                <td>An object that contains the subvention details.<br><br><a href=\"#subvention-child-object31\">Learn more about the <code>subvention</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>discount</td>\n                <td>object</td>\n                <td>An object that contains the product discount details.<br><br><a href=\"#discount-child-object31\">Learn more about the <code>discount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>brand_name</td>\n                <td>string</td>\n                <td>Name of the Brand.<br><br>Example: <code>Oneplus</code></td>\n            </tr>\n            <tr>\n                <td>interest_amount</td>\n                <td>object</td>\n                <td>An object that contains the interest amount details.<br><br><a href=\"#interest-amount-child-object31\">Learn more about the <code>interest_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>interest_rate</td>\n                <td>string</td>\n                <td>Rate of interest applied on the product.<br><br>Example: <code>19</code></td>\n            </tr>\n            <tr>\n                <td>cart_coupon_discount_product_share</td>\n                <td>object</td>\n                <td>An object that contains the cart coupon discount product share details.<br><br><a href=\"#cart-coupon-discount-product-share-child-object32\">Learn more about the <code>cart_coupon_discount_product_share</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h5 id=\"product-offer-parameters-child-object31\">Product Offer Parameters [Child Object]</h5>\n    <p>The table below lists the various parameters in the <code>product_offer_parameters</code> child object. This is part of the <code>details</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>program_type</td>\n                <td>String</td>\n                <td>Type of the Program.<br><br>Example: <code>BRAND_EMI</code><br><br>Accepted values:<ul><li><code>BRAND_EMI</code></li><li><code>BANK_EMI</code></li><li><code>MERCHANT_BRAND_OFFER</code></li><li><code>MERCHANT_BANK_OFFER</code></li><li><code>BRAND_OFFER</code></li><li><code>MY_EMI</code></li></ul></td>\n            </tr>\n            <tr>\n                <td>offer_id</td>\n                <td>string</td>\n                <td>Unique identifier of the offer.<br><br>Example: <code>309</code></td>\n            </tr>\n            <tr>\n                <td>offer_parameter_id</td>\n                <td>string</td>\n                <td>Unique offer parameter identifier.<br><br>Example: <code>20</code></td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n</html>\n<body>\n    <h5 id=\"product-amount-child-object31\">Product Amount [Child Object]</h5>\n    <p>The table below lists the various parameters in the <code>product_amount</code> child object. This is part of the <code>details</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h5 id=\"product-coupon-discount-amount-child-object31\">Product Coupon Discount Amount [Child Object]</h5>\n    <p>The table below lists the various parameters in the <code>product_coupon_discount_amount</code> child object. This is part of the <code>details</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h5 id=\"subvention-child-object31\">Subvention [Child Object]</h5>\n    <p>The table below lists the various parameters in the <code>subvention</code> child object. This is part of the <code>details</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>subvention_type</td>\n                <td>String</td>\n                <td>Type of subvention.<br><br>Example: <code>INSTANT</code><br><br>Accepted values:<ul><li><code>INSTANT</code></li><li><code>POST</code></li></ul></td>\n            </tr>\n            <tr>\n                <td>percentage</td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>amount</td>\n                <td>object</td>\n                <td>An object that contains the subvention amount details.<br><br><a href=\"#amount-child-object31\">Learn more about the <code>amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>breakup</td>\n                <td>object</td>\n                <td>An object that contains the subvention breakup details.<br><br><a href=\"#breakup-child-object31\">Learn more about the <code>breakup</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>max_amount</td>\n                <td>object</td>\n                <td>An object that contains the maximum subvention amount details.<br><br><a href=\"#max-amount-child-object31\">Learn more about the <code>max_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>min_amount</td>\n                <td>object</td>\n                <td>An object that contains the minimum subvention amount details.<br><br><a href=\"#min-amount-child-object31\">Learn more about the <code>min_amount</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n</html>\n</head>\n<body>\n    <h6 id=\"amount-child-object31\">Amount [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>amount</code> child object. This is part of the <code>subvention</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h6 id=\"breakup-child-object31\">Breakup [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>breakup</code> child object. This is part of the <code>subvention</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>brand</td>\n                <td>object</td>\n                <td>An object that contains the breakup details of the brand.<br><br><a href=\"#brand-child-object31\">Learn more about the <code>brand</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>merchant</td>\n                <td>object</td>\n                <td>An object that contains the breakup details of the merchant.<br><br><a href=\"#merchant-child-object31\">Learn more about the <code>merchant</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>issuer</td>\n                <td>object</td>\n                <td>An object that contains the breakup details of the issuer.<br><br><a href=\"#issuer-child-object31\">Learn more about the <code>issuer</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>dealer</td>\n                <td>object</td>\n                <td>An object that contains the breakup details of the dealer.<br><br><a href=\"#dealer-child-object31\">Learn more about the <code>dealer</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h6 id=\"brand-child-object31\">Brand [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>brand</code> child object. This is part of the <code>breakup</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>amount</td>\n                <td>object</td>\n                <td>An object that contains the breakup amount details of the brand.<br><br><a href=\"#amount-child-object32\">Learn more about the <code>amount</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n</html>\n<body>\n    <h6 id=\"amount-child-object32\">Amount [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>amount</code> child object. This is part of the <code>brand</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h6 id=\"merchant-child-object31\">Merchant [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>merchant</code> child object. This is part of the <code>breakup</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>amount</td>\n                <td>object</td>\n                <td>An object that contains the breakup details of the merchant.<br><br><a href=\"#amount-child-object33\">Learn more about the <code>amount</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h6 id=\"amount-child-object33\">Amount [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>amount</code> child object. This is part of the <code>merchant</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h6 id=\"issuer-child-object31\">Issuer [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>issuer</code> child object. This is part of the <code>breakup</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>amount</td>\n                <td>object</td>\n                <td>An object that contains the breakup details of the issuer.<br><br><a href=\"#amount-child-object34\">Learn more about the <code>amount</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n</html>\n<body>\n    <h6 id=\"amount-child-object34\">Amount [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>amount</code> child object. This is part of the <code>issuer</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h6 id=\"dealer-child-object31\">Dealer [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>dealer</code> child object. This is part of the <code>breakup</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>amount</td>\n                <td>object</td>\n                <td>An object that contains the breakup details of the dealer.<br><br><a href=\"#amount-child-object35\">Learn more about the <code>amount</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h6 id=\"amount-child-object35\">Amount [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>amount</code> child object. This is part of the <code>issuer</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h6 id=\"max-amount-child-object31\">Max Amount [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>max_amount</code> child object. This is part of the <code>subvention</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n</html>\n<body>\n    <h6 id=\"min-amount-child-object31\">Min Amount [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>min_amount</code> child object. This is part of the <code>subvention</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h4 id=\"discount-child-object31\">Discount [Child Object]</h4>\n    <p>The table below lists the various parameters in the <code>discount</code> child object. This is part of the <code>tenures</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>discount_type</td>\n                <td>String</td>\n                <td>Type of discount.<br><br>Possible values:<ul><li><code>INSTANT</code></li><li><code>DEFERRED</code></li></ul></td>\n            </tr>\n            <tr>\n                <td>discount_string</td>\n                <td>String</td>\n                <td>The additional discount provided by the offering entity after a specific period.<br><br>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>percentage</td>\n                <td>Double</td>\n                <td>The discount percentage provided by the offering entity.<br><br>Example: 16.90</td>\n            </tr>\n            <tr>\n                <td>amount</td>\n                <td>string</td>\n                <td>Discount amount.<br><br>Example: 2000</td>\n            </tr>\n            <tr>\n                <td>max_amount</td>\n                <td>object</td>\n                <td>An object that contains the maximum discount amount details.<br><br><a href=\"#max-amount-child-object31\">Learn more about the <code>max_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>min_amount</td>\n                <td>object</td>\n                <td>An object that contains the minimum discount amount details.<br><br><a href=\"#min-amount-child-object31\">Learn more about the <code>min_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>discount_deferred_duration_value</td>\n                <td>integer</td>\n                <td>The duration value for the deferred discount.<br><br>Example:</td>\n            </tr>\n            <tr>\n                <td>discount_deferred_duration_type</td>\n                <td>string</td>\n                <td>Discount duration type deferred.<br><br>Possible values:<ul><li><code>DAY</code></li><li><code>MONTH</code></li></ul></td>\n            </tr>\n            <tr>\n                <td>breakup</td>\n                <td>object</td>\n                <td>An object that contains the product offer details with breakup.<br><br><a href=\"#breakup-child-object31\">Learn more about the <code>breakup</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n</html>\n<body>\n    <h6 id=\"maximum-amount-child-object31\">Maximum Amount [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>max_amount</code> child object. This is part of the <code>discount</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h6 id=\"minimum-amount-child-object31\">Minimum Amount [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>min_amount</code> child object. This is part of the <code>discount</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h5 id=\"breakup-child-object31\">Breakup [Child Object]</h5>\n    <p>The table below lists the various parameters in the <code>breakup</code> child object. This is part of the <code>discount</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>brand</td>\n                <td>object</td>\n                <td>An object that contains the brand breakup details.<br><br><a href=\"#brand-child-object32\">Learn more about the <code>brand</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>merchant</td>\n                <td>object</td>\n                <td>An object that contains the merchant breakup details.<br><br><a href=\"#merchant-child-object32\">Learn more about the <code>merchant</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>issuer</td>\n                <td>object</td>\n                <td>An object that contains the issuer breakup details.<br><br><a href=\"#issuer-child-object32\">Learn more about the <code>issuer</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>dealer</td>\n                <td>object</td>\n                <td>An object that contains the dealer breakup details.<br><br><a href=\"#dealer-child-object32\">Learn more about the <code>dealer</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n</html>\n<body>\n    <h6 id=\"brand-child-object32\">Brand [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>brand</code> child object. This is part of the <code>breakup</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>amount</td>\n                <td>object</td>\n                <td>An object that contains the breakup amount details.<br><br><a href=\"#amount-child-object321\">Learn more about the <code>amount</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n    <h6 id=\"merchant-child-object32\">Merchant [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>merchant</code> child object. This is part of the <code>breakup</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>amount</td>\n                <td>object</td>\n                <td>An object that contains the breakup amount details.<br><br><a href=\"#amount-child-object321\">Learn more about the <code>amount</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h6 id=\"issuer-child-object32\">Issuer [Child Object]</h6>\n   </code> child object. This is part of the <code>breakup</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>amount</td>\n                <td>object</td>\n                <td>An object that contains the breakup amount details.<br><br><a href=\"#amount-child-object321\">Learn more about the <code>amount</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h6 id=\"dealer-child-object32\">Dealer [Child Object]</h6>\n    <p>The table below lists the various parameters in the <code>dealer</code> child object. This is part of the <code>breakup</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>amount</td>\n                <td>object</td>\n                <td>An object that contains the breakup amount details.<br><br><a href=\"#amount-child-object321\">Learn more about the <code>amount</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n</html>\n<body>\n    <h4 id=\"amount-child-object321\">Amount [Child Object]</h4>\n    <p>The table below lists the various parameters in the <code>amount</code> child object. This is part of the <code>breakup</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h4 id=\"loan-amount-child-object31\">Loan Amount [Child Object]</h4>\n    <p>The table below lists the various parameters in the <code>loan_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h4 id=\"total-discount-amount-child-object31\">Total Discount Amount [Child Object]</h4>\n    <p>The table below lists the various parameters in the <code>total_discount_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n</html>\n<body>\n    <h4 id=\"net-payment-amount-child-object31\">Net Payment Amount [Child Object]</h4>\n    <p>The table below lists the various parameters in the <code>net_payment_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n              <td>Valuevalue&nbsp;<span class=\"required-label\">required</span></td>\n              <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h4 id=\"monthly-emi-amount-child-object31\">Monthly EMI Amount [Child Object]</h4>\n    <p>The table below lists the various parameters in the <code>monthly_emi_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h4 id=\"total-emi-amount-child-object31\">Total EMI Amount [Child Object]</h4>\n    <p>The table below lists the various parameters in the <code>total_emi_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n</html>\n<body>\n    <h4 id=\"interest-amount-child-object31\">Interest Amount [Child Object]</h4>\n    <p>The table below lists the various parameters in the <code>interest_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n              <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h4 id=\"cart-coupon-discount-product-share-child-object32\">Cart Coupon Discount Product Share [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>cart_coupon_discount_product_share</code> child object. This is part of the <code>details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>currency</td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code><code>100000000</code></code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n    </tr>\n  </tbody>\n</table>\n\n    <h4 id=\"total-subvention-amount-child-object31\">Total Subvention Amount [Child Object]</h4>\n    <p>The table below lists the various parameters in the <code>total_subvention_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h4 id=\"processing-fee-details-child-object31\">Processing Fee Details [Child Object]</h4>\n    <p>The table below lists the various parameters in the <code>processing_fee_details</code> child object. This is part of the <code>tenures</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n</html>\n<body>\n    <h4 id=\"convenience-fee-breakdown-child-object31\">Convenience Fee Breakdown [Child Object]</h4>\n    <p>The table below lists the various parameters in the <code>convenience_fee_breakdown</code> child object. This is part of the <code>tenures</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>fee_calculated_on_amount</td>\n                <td>object</td>\n                <td>An object that contains the fee calculation amount details.<br><br><a href=\"#fee-calculated-on-amount-child-object31\">Learn more about the <code>fee_calculated_on_amount</code> child object</a>.</td>\n            </tr>\n          <tr>\n           <td>fee_amount</td>\n                <td>object</td>\n                <td>An object that contains the fee amount details.<br><br><a href=\"#fee-amount-child-object31\">Learn more about the <code>fee_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>tax_amount</td>\n                <td>object</td>\n                <td>An object that contains the tax amount details.<br><br><a href=\"#tax-amount-child-object31\">Learn more about the <code>tax_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>additional_fee_amount</td>\n                <td>object</td>\n                <td>An object that contains the additional fee amount details.<br><br><a href=\"#additional-fee-amount-child-object31\">Learn more about the <code>additional_fee_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>maximum_fee_amount</td>\n                <td>object</td>\n                <td>An object that contains the maximum fee amount details.<br><br><a href=\"#maximum-fee-amount-child-object31\">Learn more about the <code>maximum_fee_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>applicable_fee_amount</td>\n                <td>object</td>\n                <td>An object that contains the applicable fee amount details.<br><br><a href=\"#applicable-fee-amount-child-object31\">Learn more about the <code>applicable_fee_amount</code> child object</a>.</td>\n            </tr>\n            <tr>\n                <td>subvented_fee_amount</td>\n                <td>object</td>\n                <td>An object that contains the subvented fee amount details.<br><br><a href=\"#subvented-fee-amount-child-object31\">Learn more about the <code>subvented_fee_amount</code> child object</a>.</td>\n            </tr>\n        </tbody>\n    </table>\n\n    <h5 id=\"fee-calculated-on-amount-child-object31\">Fee Calculated on Amount [Child Object]</h5>\n    <p>The table below lists the various parameters in the <code>fee_calculated_on_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td>integer</td>\n                <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td>String</td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n</html>\n<h5 id=\"fee-amount-child-object31\">Fee Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>fee_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>value&nbsp;<span class=\"required-label\">required</span></td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.\n        <ul>\n          <li>Minimum value: <code>100</code> (₹1)</li>\n          <li>Maximum value: <code>100000000</code> (₹10 lakh)</li>\n        </ul>\n        Example: <code>1000</code>\n      </td>\n    </tr>\n    <tr>\n      <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"tax-amount-child-object31\">Tax Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>tax_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>value&nbsp;<span class=\"required-label\">required</span></td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.\n        <ul>\n          <li>Minimum value: <code>100</code> (₹1)</li>\n          <li>Maximum value: <code>100000000</code> (₹10 lakh)</li>\n        </ul>\n        Example: <code>1000</code>\n      </td>\n    </tr>\n    <tr>\n      <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"additional-fee-amount-child-object31\">Additional Fee Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>additional_fee_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>value&nbsp;<span class=\"required-label\">required</span></td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.\n        <ul>\n          <li>Minimum value: <code>100</code> (₹1)</li>\n          <li>Maximum value: <code>100000000</code> (₹10 lakh)</li>\n        </ul>\n        Example: <code>1000</code>\n      </td>\n    </tr>\n    <tr>\n      <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"maximum-fee-amount-child-object31\">Maximum Fee Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>maximum_fee_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>value&nbsp;<span class=\"required-label\">required</span></td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.\n        <ul>\n          <li>Minimum value: <code>100</code> (₹1)</li>\n          <li>Maximum value: <code>100000000</code> (₹10 lakh)</li>\n        </ul>\n        Example: <code>1000</code>\n      </td>\n    </tr>\n    <tr>\n      <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n  </tbody>\n</table>\n<h5 id=\"applicable-fee-amount-child-object31\">Applicable Fee Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>applicable_fee_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>value&nbsp;<span class=\"required-label\">required</span></td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.\n        <ul>\n          <li>Minimum value: <code>100</code> (₹1)</li>\n          <li>Maximum value: <code>100000000</code> (₹10 lakh)</li>\n        </ul>\n        Example: <code>1000</code>\n      </td>\n    </tr>\n    <tr>\n      <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h5 id=\"subvented-fee-amount-child-object31\">Subvented Fee Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>subvented_fee_amount</code> child object. This is part of the <code>convenience_fee_breakdown</code> object.</p>\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>value&nbsp;<span class=\"required-label\">required</span></td>\n      <td><code>integer</code></td>\n      <td>Transaction amount is Paisa.\n        <ul>\n          <li>Minimum value: <code>100</code> (₹1)</li>\n          <li>Maximum value: <code>100000000</code> (₹10 lakh)</li>\n        </ul>\n        Example: <code>1000</code>\n      </td>\n    </tr>\n    <tr>\n      <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n      <td><code>String</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n  </tbody>\n</table>\n\n<h4 id=\"cart-coupon-discount-amount-child-object31\">Cart Coupon Discount Amount [Child Object]</h4>\n    <p>The table below lists the various parameters in the <code>cart_coupon_discount_amount</code> child object. This is part of the <code>tenures</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td><code>integer</code></td>\n                <td>Transaction amount is Paisa.\n                  <ul>\n                    <li>Minimum value: <code>100</code> (₹1)</li>\n                    <li>Maximum value: <code>100000000</code> (₹10 lakh)</li>\n                  </ul>\n                  Example: <code>1000</code>\n                </td>\n              </tr>\n              <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td><code>String</code></td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n              </tr>\n            </tbody>\n          </table>\n\n          <h4 id=\"total-coupon-discount-child-object31\">Total Coupon Discount [Child Object]</h4>\n    <p>The table below lists the various parameters in the <code>total_coupon_discount</code> child object. This is part of the <code>tenures</code> object.</p>\n    <table border=\"1\">\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td><code>integer</code></td>\n                <td>Transaction amount is Paisa.\n                  <ul>\n                    <li>Minimum value: <code>100</code> (₹1)</li>\n                    <li>Maximum value: <code>100000000</code> (₹10 lakh)</li>\n                  </ul>\n                  Example: <code>1000</code>\n                </td>\n              </tr>\n              <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td><code>String</code></td>\n                <td>Type of currency.<br><br>Example: <code>INR</code></td>\n              </tr>\n            </tbody>\n          </table>\n\n<h3 id=\"customer-details-child-object31\">Customer Details [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>customer_details</code> object. This is part of the offer validation response object.</p>\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>customer_id</td>\n      <td><code>String</code></td>\n      <td>Details related to the customer ID, required for Plural tokenized saved cards.</td>\n    </tr>\n  </tbody>\n</table>\n\n    </div>\n    <div id=\"tab52\" class=\" tab-content\">\n     \n<body>\n    <p>The table below lists the response parameters of our Offer Validation API.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>code</td>\n                <td><code>String</code></td>\n                <td>Validation status of the offer.<br><br>Possible values:<ul><li><code>NOT_ELIGIBLE</code></li><li><code>ELIGIBLE</code></li></ul></td>\n            </tr>\n            <tr>\n                <td>message</td>\n                <td><code>String</code></td>\n                <td>Message corresponding to the validation status.<br><br>Example: <code>Offer is Eligible</code></td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n</html>\n"
}
[/block]


</details>

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/offer-validation-create" target="_blank">Offer Validation API</a> documentation to learn more.

## 4. Create Order

To create an Order, use our Create Order API, for authentication use the generated access token in the headers of the API request.

Below are the sample requests and response for a Create Order API.

```curl cURL - UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/orders \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_order_reference":112345,
  "order_amount":{
    "value":1100,
    "currency":"INR"
  },
  "pre_auth":false,
  "callback_url":"https://sample-callback-url",
  "failure_callback_url": "https://sample-failure-callback-url",
  "allowed_payment_methods":[
    "CARD",
    "UPI",
    "NETBANKING",
    "POINTS",
    "WALLET"
  ],
  "notes":"order1",
  "purchase_details":{
    "customer":{
      "email_id":"kevin.bob@example.com",
      "first_name":"Kevin",
      "last_name":"Bob",
      "customer_id":"123456",
      "mobile_number":"9876543210",
      "billing_address":{
        "address1":"10 Downing Street Westminster London",
        "address2":"Oxford Street Westminster London",
        "address3":"Baker Street Westminster London",
        "pincode":"51524036",
        "city":"Westminster",
        "state":"Westminster",
        "country":"London"
      },
      "shipping_address":{
        "address1":"10 Downing Street Westminster London",
        "address2":"Oxford Street Westminster London",
        "address3":"Baker Street Westminster London",
        "pincode":"51524036",
        "city":"Westminster",
        "state":"Westminster",
        "country":"London"
      }
    },
    "merchant_metadata":{
      "key1":"DD",
      "key2":"XOF"
    }
  },
  "cart_coupon_discount_amount":{
    "value":100,
    "currency":"INR"
  }
}
'
```
```curl cURL - PROD
curl --request POST \
     --url https://api.pluralpay.in/api/pay/v1/orders \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_order_reference":112345,
  "order_amount":{
    "value":1100,
    "currency":"INR"
  },
  "pre_auth":false,
  "callback_url":"https://sample-callback-url",
  "failure_callback_url": "https://sample-failure-callback-url",
  "allowed_payment_methods":[
    "CARD",
    "UPI",
    "NETBANKING",
    "POINTS",
    "WALLET"
  ],
  "notes":"order1",
  "purchase_details":{
    "customer":{
      "email_id":"kevin.bob@example.com",
      "first_name":"Kevin",
      "last_name":"Bob",
      "customer_id":"123456",
      "mobile_number":"9876543210",
      "billing_address":{
        "address1":"10 Downing Street Westminster London",
        "address2":"Oxford Street Westminster London",
        "address3":"Baker Street Westminster London",
        "pincode":"51524036",
        "city":"Westminster",
        "state":"Westminster",
        "country":"London"
      },
      "shipping_address":{
        "address1":"10 Downing Street Westminster London",
        "address2":"Oxford Street Westminster London",
        "address3":"Baker Street Westminster London",
        "pincode":"51524036",
        "city":"Westminster",
        "state":"Westminster",
        "country":"London"
      }
    },
    "merchant_metadata":{
      "key1":"DD",
      "key2":"XOF"
    }
  },
  "cart_coupon_discount_amount":{
    "value":100,
    "currency":"INR"
  }
}
'
```
```json Sample Response
{
  "data":{
    "order_id":"v1-4405071524-aa-qlAtAf",
    "merchant_order_reference":"112345",
    "type":"CHARGE",
    "status":"CREATED",
    "merchant_id":"104359",
    "order_amount":{
      "value":1100,
      "currency":"INR"
    },
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
        "customer_id":"123456",
        "mobile_number":"9876543210",
        "billing_address":{
          "address1":"10 Downing Street Westminster London",
          "address2":"Oxford Street Westminster London",
          "address3":"Baker Street Westminster London",
          "pincode":"51524036",
          "city":"Westminster",
          "state":"Westminster",
          "country":"London"
        },
        "shipping_address":{
          "address1":"10 Downing Street Westminster London",
          "address2":"Oxford Street Westminster London",
          "address3":"Baker Street Westminster London",
          "pincode":"51524036",
          "city":"Westminster",
          "state":"Westminster",
          "country":"London"
        }
      },
      "merchant_metadata":{
        "key1":"DD",
        "key2":"XOF"
      }
    },
    "payments":[
      
    ],
    "created_at":"2024-07-15T05:44:51.174Z",
    "updated_at":"2024-07-15T05:44:51.174Z",
    "cart_coupon_discount_amount":{
      "value":100,
      "currency":"INR"
    }
  }
}
```

<details><summary>Click here for request and response parameter information.</summary>

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid #5A0083;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n    </style>\n</head>\n<body>\n     <div class=\"tab-container\">\n        <div class=\"tab active\" data-target=\"tab53\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Request Parameters</div>\n\n        <div class=\"tab\" data-target=\"tab54\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Response Parameters</div>\n\n    <div id=\"tab53\" class=\"tab-content active\">\n      \n      \n      <body>\n    <p>The table below lists the request parameters of our Create Order API.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>merchant_order_reference&nbsp;<span class=\"required-label\">required</span></td>\n                <td><code>string</code></td>\n                <td>\n                    Enter a unique identifier for the order request.<br><br><ul><li>\n                    Minimum: 1 character.</li><li>\n                  Maximum: 50 characters.</ul></li>\n          Example: <code>1234567890</code><br><br>\n          Supported characters:<ul><li><code>A-Z</code></li><li><code>a-z</code></li><li><code>0-9</code></li><li><code>-</code></li><li><code>_</code></ul></li>\n                </td>\n            </tr>\n            <tr>\n                <td>order_amount&nbsp;<span class=\"required-label\">required</span></td>\n                <td><code>object</code></td>\n                <td>An object that contains the transaction amount details.<br><br>\n                    <a href=\"#order-amount-child-object41\">Learn more about the <code>order_amount</code> child object</a>.\n                </td>\n            </tr>\n            <tr>\n                <td>pre_auth</td>\n                <td><code>boolean</code></td>\n                <td>\n                    The pre-authorization type.<br><br>\n                    Possible values:<br><ul><li>\n                  <code>false</code> (default): When pre-authorization is not required.<br></li><li>\n                    <code>true</code>: When pre-authorization is needed.\n                </td>\n            </tr>\n        <tr>\n                <td>callback_url</td>\n                <td><code>string</code></td>\n                <td>\n                    URL to redirect customers based on order details.<br><br>\n                    Example: <code>https://sample-callback-url</code>\n                </td>\n            </tr>\n       <tr>\n                <td>failure_callback_url</td>\n                <td><code>string</code></td>\n                <td>\n                    URL to redirect customers based on order details.<br><br>\n                    Example: <code>https://sample-failure-callback-url</code>\n                </td>\n            </tr>\n      \n            <tr>\n                <td>allowed_payment_methods</td>\n                <td><code>array of strings</code></td>\n                <td>\n                    The type of payment methods you want to offer customers.<br><br>\n                  Accepted values:<ul><li><code>CARD</code></li><li><code>UPI</code></li><li><code>POINTS</code></li><li><code>NETBANKING</code></li><li><code>WALLET</code></li><li><code>CREDIT_EMI</code></li><li><code>DEBIT_EMI</code></ul></li>\n                    Example: CARD<br><br>\n <strong>Note</strong>: Ensure it is configured for you.\n                </td>\n            </tr>\n            <tr>\n                <td>notes</td>\n                <td><code>string</code></td>\n                <td>Note to show against an order.<br><br>\n                    Example: <code>Order1</code>\n                </td>\n            </tr>\n            <tr>\n                <td>purchase_details</td>\n                <td><code>object</code></td>\n                <td>An object that contains purchase details.<br><br>\n                  <a href=\"#purchase-details-child-object41\">Learn more about the <code>purchase_details</code> child object</a>.\n                </td>\n            </tr>\n  <tr>\n    <td>cart_coupon_discount_amount</td>\n    <td><code>object</code></td>\n                <td>An object that contains the cart coupon discount amount details.<br><br>\n                    <a href=\"#cart-coupon-discount-amount-child-object41\">Learn more about the <code>cart_coupon_discount_amount</code> child object</a>.\n                </td>\n            </tr>\n    \n        </tbody>\n    </table>\n    <h2 id=\"order-amount-child-object41\">Order Amount [Child Object]</h2>\n        <p> The table below lists the various parameters in the <code>order_amount</code> child object. This object is part of the <code>create order</code> request object.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value&nbsp;<span class=\"required-label\">required</span></td>\n                <td><code>integer</code></td>\n                <td>\n                    Transaction amount in Paisa.<br><br><ul><li>\n                  Minimum value: <code>100</code> (₹1).</li><li>\n                  Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>\n          Example: <code>1000</code>\n                </td>\n            </tr>\n            <tr>\n                <td>currency&nbsp;<span class=\"required-label\">required</span></td>\n                <td><code>string</code></td>\n                <td>\n                    Type of currency.<br><br>\n                  Example: <code>INR</code>\n                </td>\n            </tr>\n        </tbody>\n    </table>\n\n<h2 id=\"purchase-details-child-object41\">Purchase Details [Child Object]</h2>\n<p>The table below lists the various parameters in the <code>purchase_details</code> child object. This object is part of the <code>create order</code> request object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>customer</td>\n          <td><code>object</code></td>\n            <td>An object that contains the customer details.<br><br><a href=\"#customer-child-object41\">Learn more about the <code>customer</code> child object</a>.</td>\n        </tr>\n        <tr>\n            <td>merchant_metadata</td>\n            <td><code>object</code></td>\n            <td>An object of key-value pair that can be used to store additional information.<br><br>Example: <code>\"key1\": \"DD\"</code></td>\n        </tr>\n    </table>\n    \n    <h2 id=\"customer-child-object41\">Customer [Child Object]</h2>\n<p>The table below lists the various parameters in the <code>customer</code> child object. This is part of the <code>purchase_details</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>email_id</td>\n          <td><code>string</code></td>\n          <td>Customer's email address.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>kevin.bob@example.com</code></td>\n        </tr>\n        <tr>\n            <td>first_name</td>\n          <td><code>string</code></td>\n          <td>Customer's first name.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>Kevin</code></td>\n        </tr>\n        <tr>\n            <td>last_name</td>\n          <td><code>string</code></td>\n          <td>Customer's last name.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>Bob</code></td>\n        </tr>\n        <tr>\n            <td>customer_id</td>\n          <td><code>string</code></td>\n            <td>Unique identifier of the customer in the Plural database.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>19</code> characters.</ul></li>Example: <code>123456</code></td>\n        </tr>\n        <tr>\n            <td>mobile_number</td>\n          <td><code>string</code></td>\n          <td>Customer's mobile number.<ul><li>Minimum length: <code>9</code> characters.</li><li>Maximum length: <code>20</code> characters.</ul></li>Example: <code>9876543210</code></td>\n        </tr>\n        <tr>\n            <td>billing_address</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the billing address.<br><br><a href=\"#billing-address-child-object41\">Learn more about our <code>billing_address</code> child object</a>.</td>\n        </tr>\n        <tr>\n            <td>shipping_address</td>\n          <td><code>object</code></td>\n            <td>An object that contains the shipping address details.<br><br><a href=\"#shipping-address-child-object41\">Learn more about our <code>shipping_address</code> child object</a>.</td>\n        </tr>\n    </table>\n<h2 id=\"billing-address-child-object41\">Billing Address [Child Object]</h2>\n  <p>The table below lists the various parameters in the <code>billing_address</code> child object. This is part of the <code>customer</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr><td>address1</td><td><code>string</code></td><td>Customer's billing address1.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>10 Downing Street Westminster London</code></td></tr>\n        <tr><td>address2</td><td><code>string</code></td><td>Customer's billing address2.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Oxford Street Westminster London</code></td></tr>\n        <tr><td>address3</td><td><code>string</code></td><td>Customer's billing address3.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Baker Street Westminster London</code></td></tr>\n        <tr><td>pincode</td><td><code>string</code></td><td>Pincode of the billing address.<ul><li>Min length: <code>6</code> characters.</li><li>Max length: <code>10</code> characters.</ul></li>Example: <code>51524036</code></td></tr>\n        <tr><td>city</td><td><code>string</code></td><td>City of the billing address. <ul><li>Max length: <code>50</code> characters. </ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>state</td><td><code>string</code></td><td>State of the billing address. <ul><li>Max length: <code>50<code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>country</td><td><code>string</code></td><td>Country of the billing address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>London</code></td></tr>\n    </table>\n\n    <h2 id=\"shipping-address-child-object41\">Shipping Address [Child Object]</h2>\n  <p>The table below lists the various parameters in the <code>shipping_address</code> child object. This is part of the <code>customer</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr><td>address1</td><td><code>string</code></td><td>Customer's shipping address1.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>10 Downing Street Westminster London</code></td></tr>\n        <tr><td>address2</td><td><code>string</code></td><td>Customer's shipping address2.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Oxford Street Westminster London</code></td></tr>\n        <tr><td>address3</td><td><code>string</code></td><td>Customer's shipping address3.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Baker Street Westminster London</code></td></tr>\n        <tr><td>pincode</td><td><code>string</code></td><td>Pincode of the shipping address.<ul><li>Min length: <code>6</code> characters</li><li>Max length: <code>10</code> characters.</ul></li>Example: <code>51524036</code></td></tr>\n        <tr><td>city</td><td><code>string</code></td><td>City of the shipping address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>state</td><td><code>string</code></td><td>State of the shipping address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>country</td><td><code>string</code></td><td>Country of the shipping address. <ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>London</code></td></tr>\n    </table>\n\n<h2 id=\"cart-coupon-discount-amount-child-object41\">Cart Coupon Discount Amount [Child Object]</h2>\n        <p> The table below lists the various parameters in the <code>cart_coupon_discount_amount</code> child object. This object is part of the <code>create order</code> request object.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value</td>\n                <td><code>integer</code></td>\n                <td>\n                    Transaction amount in Paisa.<br><br><ul><li>\n                  Minimum value: <code>100</code> (₹1).</li><li>\n                  Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>\n          Example: <code>1000</code>\n                </td>\n            </tr>\n            <tr>\n                <td>currency</td>\n                <td><code>string</code></td>\n                <td>\n                    Type of currency.<br><br>\n                  Example: <code>INR</code>\n                </td>\n            </tr>\n        </tbody>\n    </table>\n</body>\n      \n      \n    </div>\n    <div id=\"tab54\" class=\" tab-content\">\n      \n        <body>\n          <p>The table below lists the various parameters returned in the orders response objects.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>order_id</td>\n          <td><code>string</code></td>\n          <td>Unique identifier of the order in the Plural database.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>v1-5757575757-aa-hU1rUd</code></td>\n        </tr>\n        <tr>\n            <td>merchant_order_reference</td>\n          <td><code>string</code></td>\n          <td>Unique identifier entered while creating an order.<ul><li>Min length: <code>1</code> character.</li><li>Max length: <code>50</code> characters.</ul></li>Example: <code>82d57572-057c-4826-5775-385a52150554</code></td>\n        </tr>\n        <tr>\n            <td>type</td>\n          <td><code>string</code></td>\n          <td>Payment type.<br><br>Possible values:<ul><li><code>CHARGE</code></li><li><code>REFUND</code></td>\n        </tr>\n        <tr>\n            <td>status</td>\n          <td><code>string</code></td>\n          <td>Order status.<br><br>Possible values:<ul><li><code>CREATED</code>: When the order is successfully created.</li><li><code>PENDING</code>: When the order is linked against a payment request.</li><li><code>PROCESSED</code>: When the payment is received successfully.</li><li><code>AUTHORIZED</code>: <strong>Only when pre_auth is true</strong>. When the payment is ready for authorization.</li><li><code>CANCELLED</code>: When the payment gets cancelled.</li><li><code>ATTEMPTED</code>: When the payment is unsuccessful due to incorrect OTP. You can retry OTP</li><li><code>FAILED</code>: Payment acceptance failed for reasons such as cancel transactions, maximum retries for OTP verification etc.</li><li><code>FULLY_REFUNDED</code>: When the payment is completely refunded.</li><li><code>PARTIALLY_REFUNDED</code>: When the partial refund is successful.</ul></li></td>\n        </tr>\n        <tr>\n            <td>challenge_url</td>\n          <td><code>string</code></td>\n          <td>Use the generated challenge_url to accept payment.<br><br><code>Note</code>: This parameter is returned only after the payment is linked against the order_id.</td>\n        </tr>\n        <tr>\n            <td>merchant_id</td>\n          <td><code>string</code></td>\n            <td>Unique identifier of the merchant in the Plural database.<br><br>Example: <code>123456</code></td>\n        </tr>\n        <tr>\n            <td>order_amount</td>\n          <td><code>object</code></td>\n            <td>An object that contains the transaction amount details.<br><br><a href=\"#order-amount-child-object42\">Learn more about our <code>order_amount</code> child object</a>.</td>\n        </tr>\n        <tr>\n            <td>notes</td>\n          <td><code>string</code></td>\n          <td>The note you want to show against an order.<br><br>Example: <code>Order1</code></td>\n        </tr>\n        <tr>\n            <td>pre_auth</td>\n          <td><code>boolean</code></td>\n          <td>The pre-authorization type.<br><br>Possible values:<ul><li><code>true</code>: When pre-authorization is needed.</li><li><code>false</code>: When pre-authorization is not required.</ul></li>Example: <code>false</code></td>\n        </tr>\n        <tr>\n            <td>allowed_payment_methods</td>\n          <td><code>array of strings</code></td>\n            <td>The type of payment methods you want to offer customers.<br><br>Accepted values:<ul><li><code>CARD</code></li><li><code>UPI</code></li><li><code>POINTS</code></li><li><code>NETBANKING</code></li><li><code>WALLET</code></li><li><code>CREDIT_EMI</code></li><li><code>DEBIT_EMI</code></ul></li>Example: <code>CARD</code><br><br><strong>Note</strong>: Before selecting a payment method, ensure it is configured for you.</td>\n        </tr>\n        <tr>\n            <td>callback_url</td>\n          <td><code>string</code></td>\n            <td>URL to redirect customers to success or failure pages.<br><br>Example: <code>https://sample-callback-url</code></td>\n        </tr>\n<tr>\n            <td>failure_callback_url</td>\n          <td><code>string</code></td>\n            <td>URL to redirect customers to success or failure pages.<br><br>Example: <code>https://sample-failure-callback-url</code></td>\n        </tr>\n        <tr>\n            <td>purchase_details</td>\n          <td><code>object</code></td>\n            <td>An object that contains the purchase details.<br><br><a href=\"#purchase-details-child-object42\">Learn more about the <code>purchase_details</code> child object</a>.<br><br><strong>Note</strong>: The presence of the object key-values depends on the Input request.</td>\n        </tr>\n        <tr>\n            <td>payments</td>\n          <td><code>array of objects</code></td>\n            <td>An array of objects that contains the payment details.<br><br>Learn more about the <code>payments</code> child object.<br><br><strong>Note</strong>: Payment object is returned only for the orders linked with a payment.</td>\n        </tr>\n        <tr>\n            <td>created_at</td>\n          <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp when the order request was received.<br><br>Example: <code>2024-07-09T07:57:08.022Z</code></td>\n        </tr>\n        <tr>\n            <td>updated_at</td>\n          <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp when the order object was updated.<br><br>Example: <code>2024-07-09T07:57:08.022Z</code></td>\n        </tr>\n<tr>\n    <td>cart_coupon_discount_amount</td>\n    <td><code>object</code></td>\n                <td>An object that contains the cart coupon discount amount details.<br><br>\n                    <a href=\"#cart-coupon-discount-amount-child-object42\">Learn more about the <code>cart_coupon_discount_amount</code> child object</a>.\n                </td>\n            </tr>\n    </table>\n\n <h2 id=\"order-amount-child-object42\">Order Amount [Child Object]</h2>\n        <p> The table below lists the various parameters in the <code>order_amount</code> child object. This object is part of the <code>create order</code> request object.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value</td>\n                <td><code>integer</code></td>\n                <td>\n                    Transaction amount in Paisa.<br><br><ul><li>\n                  Minimum value: <code>100</code> (₹1).</li><li>\n                  Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>\n          Example: <code>1000</code>\n                </td>\n            </tr>\n            <tr>\n                <td>currency</td>\n                <td><code>string</code></td>\n                <td>\n                    Type of currency.<br><br>\n                  Example: <code>INR</code>\n                </td>\n            </tr>\n        </tbody>\n    </table>\n\n<h2 id=\"purchase-details-child-object42\">Purchase Details [Child Object]</h2>\n<p>The table below lists the various parameters in the <code>purchase_details</code> child object. This object is part of the <code>create order</code> request object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>customer</td>\n          <td><code>object</code></td>\n            <td>An object that contains the customer details.<br><br><a href=\"#customer-child-object42\">Learn more about the <code>customer</code> child object</a>.</td>\n        </tr>\n        <tr>\n            <td>merchant_metadata</td>\n            <td><code>object</code></td>\n            <td>An object of key-value pair that can be used to store additional information.<br><br>Example: <code>\"key1\": \"DD\"</code></td>\n        </tr>\n    </table>\n    \n    <h2 id=\"customer-child-object42\">Customer [Child Object]</h2>\n<p>The table below lists the various parameters in the <code>customer</code> child object. This is part of the <code>purchase_details</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>email_id</td>\n          <td><code>string</code></td>\n          <td>Customer's email address.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>kevin.bob@example.com</code></td>\n        </tr>\n        <tr>\n            <td>first_name</td>\n          <td><code>string</code></td>\n          <td>Customer's first name.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>Kevin</code></td>\n        </tr>\n        <tr>\n            <td>last_name</td>\n          <td><code>string</code></td>\n          <td>Customer's last name.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>Bob</code></td>\n        </tr>\n        <tr>\n            <td>customer_id</td>\n          <td><code>string</code></td>\n            <td>Unique identifier of the customer in the Plural database.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>19</code> characters.</ul></li>Example: <code>123456</code></td>\n        </tr>\n        <tr>\n            <td>mobile_number</td>\n          <td><code>string</code></td>\n          <td>Customer's mobile number.<ul><li>Minimum length: <code>9</code> characters.</li><li>Maximum length: <code>20</code> characters.</ul></li>Example: <code>9876543210</code></td>\n        </tr>\n        <tr>\n            <td>billing_address</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the billing address.<br><br><a href=\"#billing-address-child-object42\">Learn more about our <code>billing_address</code> child object</a>.</td>\n        </tr>\n        <tr>\n            <td>shipping_address</td>\n          <td><code>object</code></td>\n            <td>An object that contains the shipping address details.<br><br><a href=\"#shipping-address-child-object42\">Learn more about our <code>shipping_address</code> child object</a>.</td>\n        </tr>\n    </table>\n<h2 id=\"billing-address-child-object42\">Billing Address [Child Object]</h2>\n  <p>The table below lists the various parameters in the <code>billing_address</code> child object. This is part of the <code>customer</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr><td>address1</td><td><code>string</code></td><td>Customer's billing address1.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>10 Downing Street Westminster London</code></td></tr>\n        <tr><td>address2</td><td><code>string</code></td><td>Customer's billing address2.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Oxford Street Westminster London</code></td></tr>\n        <tr><td>address3</td><td><code>string</code></td><td>Customer's billing address3.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Baker Street Westminster London</code></td></tr>\n        <tr><td>pincode</td><td><code>string</code></td><td>Pincode of the billing address.<ul><li>Min length: <code>6</code> characters.</li><li>Max length: <code>10</code> characters.</ul></li>Example: <code>51524036</code></td></tr>\n        <tr><td>city</td><td><code>string</code></td><td>City of the billing address. <ul><li>Max length: <code>50</code> characters. </ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>state</td><td><code>string</code></td><td>State of the billing address. <ul><li>Max length: <code>50<code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>country</td><td><code>string</code></td><td>Country of the billing address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>London</code></td></tr>\n    </table>\n\n    <h2 id=\"shipping-address-child-object42\">Shipping Address [Child Object]</h2>\n  <p>The table below lists the various parameters in the <code>shipping_address</code> child object. This is part of the <code>customer</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr><td>address1</td><td><code>string</code></td><td>Customer's shipping address1.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>10 Downing Street Westminster London</code></td></tr>\n        <tr><td>address2</td><td><code>string</code></td><td>Customer's shipping address2.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Oxford Street Westminster London</code></td></tr>\n        <tr><td>address3</td><td><code>string</code></td><td>Customer's shipping address3.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Baker Street Westminster London</code></td></tr>\n        <tr><td>pincode</td><td><code>string</code></td><td>Pincode of the shipping address.<ul><li>Min length: <code>6</code> characters</li><li>Max length: <code>10</code> characters.</ul></li>Example: <code>51524036</code></td></tr>\n        <tr><td>city</td><td><code>string</code></td><td>City of the shipping address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>state</td><td><code>string</code></td><td>State of the shipping address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>country</td><td><code>string</code></td><td>Country of the shipping address. <ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>London</code></td></tr>\n    </table>\n\n<h2 id=\"cart-coupon-discount-amount-child-object42\">Cart Coupon Discount Amount [Child Object]</h2>\n        <p> The table below lists the various parameters in the <code>cart_coupon_discount_amount</code> child object. This object is part of the <code>create order</code> response object.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value</td>\n                <td><code>integer</code></td>\n                <td>\n                    Transaction amount in Paisa.<br><br><ul><li>\n                  Minimum value: <code>100</code> (₹1).</li><li>\n                  Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>\n          Example: <code>1000</code>\n                </td>\n            </tr>\n            <tr>\n                <td>currency</td>\n                <td><code>string</code></td>\n                <td>\n                    Type of currency.<br><br>\n                  Example: <code>INR</code>\n                </td>\n            </tr>\n        </tbody>\n    </table>\n\n</body>\n      \n      \n    </div>\n</body>\n</html>"
}
[/block]


</details>

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/reference/affordability-suite-orders-create" target="_blank">Create Order API</a> documentation to learn more.

> 📘 Note:
> 
> When the pre-authorization is set to true you can capture the payment after successful delivery or service.

## 5. Create Payment

To create a payment, use our Create Payment API, use the `order_id` returned in the response of a Create Order API to link the payment against an order.

Below are the sample requests and sample response for Create Payment API.

#### **Credit EMI**

```curl cURL - UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/payments \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "payments": [
    {
      "merchant_payment_reference": "6dc93180-91d4-448e-b2a3-c859d2f1cac9",
      "payment_method": "CREDIT_EMI",
      "payment_amount": {
        "value": 219900,
        "currency": "INR"
      },
      "payment_option": {
        "card_details": {
          "name": "Kevin Bob",
          "card_number": "4000000000000000",
          "cvv": "065",
          "expiry_month": "12",
          "expiry_year": "2025",
          "registered_mobile_number": "9876543210"
        }
      },
      "offer_data": {
        "offer_details": {
          "id": "6",
          "name": "HDFC CC",
          "display_name": "HDFC BANK",
          "issuer_type": "CC_BANK",
          "priority": 1,
          "tenure": {
            "tenure_id": "6",
            "name": "24 Months",
            "tenure_type": "MONTH",
            "tenure_value": 24,
            "issuer_offer_parameters": [
              {
                "program_type": "BANK_EMI",
                "offer_id": "3498",
                "offer_parameter_id": "199796"
              },
              {
                "program_type": "MERCHANT_BANK_OFFER",
                "offer_id": "3678",
                "offer_parameter_id": "203706"
              }
            ],
            "details": [
              {
                "product_code": "xyz",
                "product_display_name": "Redmi Note 13 5G",
                "brand_name": "Xiaomi",
                "product_amount": {
                  "currency": "INR",
                  "value": 219900
                },
                "interest_amount": {
                  "currency": "INR",
                  "value": 38508
                },
                "interest_rate": 16
              }
            ],
            "loan_amount": {
              "currency": "INR",
              "value": 219900
            },
            "net_payment_amount": {
              "currency": "INR",
              "value": 258408
            },
            "monthly_emi_amount": {
              "currency": "INR",
              "value": 10767
            },
            "total_emi_amount": {
              "currency": "INR",
              "value": 258408
            },
            "interest_amount": {
              "currency": "INR",
              "value": 38508
            },
            "interest_rate_percentage": 16,
            "emi_type": "STANDARD"
          }
        }
      }
    }
  ]
}
'
```
```curl cURL - PROD
curl --request POST \
     --url https://api.pluralpay.in/api/pay/v1/orders/{order_id}/payments \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "payments": [
    {
      "merchant_payment_reference": "6dc93180-91d4-448e-b2a3-c859d2f1cac9",
      "payment_method": "CREDIT_EMI",
      "payment_amount": {
        "value": 1550000,
        "currency": "INR"
      },
      "payment_option": {
        "card_details": {
          "name": "Kevin Bob",
          "card_number": "4000000000000000",
          "cvv": "065",
          "expiry_month": "12",
          "expiry_year": "2025",
          "registered_mobile_number": "9876543210"
        }
      },
      "offer_data": {
        "offer_details": {
          "id": "6",
          "name": "HDFC CC",
          "issuer_type": "CC_BANK",
          "priority": 1,
          "tenure": {
            "tenure_id": "1",
            "name": "3 Months",
            "tenure_type": "MONTH",
            "tenure_value": 3,
            "issuer_offer_parameters": [
              {
                "program_type": "BANK_EMI",
                "offer_id": "308",
                "offer_parameter_id": "19"
              },
              {
                "program_type": "MERCHANT_BANK_OFFER",
                "offer_id": "1234",
                "offer_parameter_id": "66666"
              }
            ],
            "discount": {
              "discount_type": "INSTANT",
              "amount": {
                "currency": "INR",
                "value": 50000
              },
              "breakup": {
                "merchant": {
                  "amount": {
                    "currency": "INR",
                    "value": 50000
                  }
                }
              }
            },
            "loan_amount": {
              "currency": "INR",
              "value": 1550000
            },
            "total_discount_amount": {
              "currency": "INR",
              "value": 50000
            },
            "net_payment_amount": {
              "currency": "INR",
              "value": 1588908
            },
            "monthly_emi_amount": {
              "currency": "INR",
              "value": 529636
            },
            "total_emi_amount": {
              "currency": "INR",
              "value": 1588908
            },
            "interest_amount": {
              "currency": "INR",
              "value": 38908
            },
            "interest_rate_percentage": 15,
            "processing_fee_details": {
              "amount": {
                "currency": "INR",
                "value": 199
              }
            },
            "emi_type": "STANDARD"
          }
        }
      }
    }
  ]
}
'
```
```json Sample Response
{
  "data":{
    "order_id":"v1-250124055307-aa-6OZ8sm",
    "merchant_order_reference":"53cf1451-4dfd-417d-a1c8-c8bd603d5200",
    "type":"CHARGE",
    "status":"PENDING",
    "challenge_url":"https://pluraluat.v2.pinepg.in/web/auth/landing/?token=S50f2FXi%2FYAGe2bLZEW%2FA2VHzXthz0m9igmtsP61ODtY5u4pR6RYB5IlJwK0%2Fuo%2FBs9",
    "merchant_id":"111163",
    "order_amount":{
      "value":1600000,
      "currency":"INR"
    },
    "pre_auth":false,
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
    "purchase_details":{
      "customer":{
        "country_code":"91",
        "billing_address":{
          
        },
        "shipping_address":{
          
        },
        "is_edit_customer_details_allowed":false
      }
    },
    "payments":[
      {
        "id":"v1-250124055307-aa-6OZ8sm-ce-a",
        "merchant_payment_reference":"c7a7f778-b68f-462b-a6af-50698df12a4a",
        "status":"FAILED",
        "payment_amount":{
          "value":1550000,
          "currency":"INR"
        },
        "payment_method":"CREDIT_EMI",
        "offer_data":{
          "offer_details":{
            "id":"6",
            "name":"HDFC CC",
            "issuer_type":"CC_BANK",
            "priority":1,
            "tenure":{
              "tenure_id":"1",
              "name":"3 Months",
              "tenure_type":"MONTH",
              "tenure_value":3,
              "issuer_offer_parameters":[
                {
                  "program_type":"BANK_EMI",
                  "offer_id":"1803",
                  "offer_parameter_id":"72559"
                },
                {
                  "program_type":"MERCHANT_BANK_OFFER",
                  "offer_id":"1523",
                  "offer_parameter_id":"63566"
                }
              ],
              "details":[
                
              ],
              "discount":{
                "discount_type":"INSTANT",
                "amount":{
                  "currency":"INR",
                  "value":50000
                },
                "breakup":{
                  "merchant":{
                    
                  },
                  "issuer":{
                    
                  },
                  "brand":{
                    
                  },
                  "dealer":{
                    
                  }
                }
              },
              "loan_amount":{
                "currency":"INR",
                "value":1550000
              },
              "total_discount_amount":{
                "currency":"INR",
                "value":50000
              },
              "net_payment_amount":{
                "currency":"INR",
                "value":1601952
              },
              "monthly_emi_amount":{
                "currency":"INR",
                "value":533984
              },
              "total_emi_amount":{
                "currency":"INR",
                "value":1601952
              },
              "interest_amount":{
                "currency":"INR",
                "value":51952
              },
              "interest_rate_percentage":20,
              "processing_fee_details":{
                "amount":{
                  "currency":"INR",
                  "value":19900
                }
              },
              "processing_fee_amount":{
                "currency":"INR",
                "value":19900
              },
              "emi_type":"STANDARD"
            }
          }
        },
        "error_detail":{
          "code":"INTERNAL_ERROR",
          "message":"Payment processor is unavailable"
        },
        "created_at":"2025-01-24T05:53:24.476Z",
        "updated_at":"2025-01-24T05:53:25.492Z"
      },
      {
        "id":"v1-250124055307-aa-6OZ8sm-ce-b",
        "merchant_payment_reference":"32e3ba62-bb95-41bb-be81-1b87ab96c0ed",
        "status":"PENDING",
        "payment_amount":{
          "value":1550000,
          "currency":"INR"
        },
        "payment_method":"CREDIT_EMI",
        "payment_option":{
          "card_data":{
            "card_type":"CREDIT",
            "network_name":"VISA",
            "issuer_name":"INTL HDQTRS-CENTER OWNED",
            "card_category":"Consumer",
            "country_code":"IND",
            "token_txn_type":"ALT_TOKEN",
            "save":false
          }
        },
        "acquirer_data":{
          "approval_code":"",
          "acquirer_reference":"",
          "rrn":"",
          "is_aggregator":true
        },
        "offer_data":{
          "offer_details":{
            "id":"6",
            "name":"HDFC CC",
            "issuer_type":"CC_BANK",
            "priority":1,
            "tenure":{
              "tenure_id":"1",
              "name":"3 Months",
              "tenure_type":"MONTH",
              "tenure_value":3,
              "issuer_offer_parameters":[
                {
                  "program_type":"BANK_EMI",
                  "offer_id":"1803",
                  "offer_parameter_id":"72559"
                },
                {
                  "program_type":"MERCHANT_BANK_OFFER",
                  "offer_id":"1523",
                  "offer_parameter_id":"63566"
                }
              ],
              "details":[
                
              ],
              "discount":{
                "discount_type":"INSTANT",
                "amount":{
                  "currency":"INR",
                  "value":50000
                },
                "breakup":{
                  "merchant":{
                    
                  },
                  "issuer":{
                    
                  },
                  "brand":{
                    
                  },
                  "dealer":{
                    
                  }
                }
              },
              "loan_amount":{
                "currency":"INR",
                "value":1550000
              },
              "total_discount_amount":{
                "currency":"INR",
                "value":50000
              },
              "net_payment_amount":{
                "currency":"INR",
                "value":1601952
              },
              "monthly_emi_amount":{
                "currency":"INR",
                "value":533984
              },
              "total_emi_amount":{
                "currency":"INR",
                "value":1601952
              },
              "interest_amount":{
                "currency":"INR",
                "value":51952
              },
              "interest_rate_percentage":20,
              "processing_fee_details":{
                "amount":{
                  "currency":"INR",
                  "value":19900
                }
              },
              "processing_fee_amount":{
                "currency":"INR",
                "value":19900
              },
              "emi_type":"STANDARD"
            }
          }
        },
        "created_at":"2025-01-24T05:53:58.092Z",
        "updated_at":"2025-01-24T05:53:59.679Z"
      }
    ],
    "created_at":"2025-01-24T05:53:07.740Z",
    "updated_at":"2025-01-24T05:53:59.680Z",
    "integration_mode":"SEAMLESS",
    "payment_retries_remaining":8
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/reference/affordability-suite-create-payment" target="_blank">Create Payment API</a> documentation to learn more.

## 6. Handle Payment

In create payment API response we return a `challenge_url`, use this challenge url to navigate your customers to the checkout page to accept payment.

> 📘 Note:
> 
> - On successful payment we send the webhook event `ORDER_AUTHORIZED` and the status of the payment is updated to `authorized`.
> - You can capture or cancel an order only when the order status is `authorized`.

### 6.1 Store Payment Details on Your Server

On a successful and failed payment, we return the following fields to the return url.

- We recommend you to store the payment details on your server.
- You must validate the authenticity of the payment details returned. You can authenticate by verifying the signature.

```json Success Callback Response
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "status": "AUTHORIZED",
  "signature": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
}
```
```json Failure Callbak Response
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "status": "AUTHORIZED",
  "error_code": "USER_AUTHENTICATION_REQUIRED",
  "error_message": "Consumer Authentication Required",
  "signature": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
}
```

### 6.2 Verify Payment Signature

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

## 7. Get Order by Order ID

Use this API to retrieve the order by order ID.

Below are the sample requests and response for the Get Order by Order ID API.

```curl cURL - UAT
curl --request GET \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id} \
     --header 'accept: application/json'
```
```curl cURL - PROD
curl --request GET \
     --url https://api.pluralpay.in/api/pay/v1/orders/{order_id} \
     --header 'accept: application/json'
```
```json Sample Response
{
  "data":{
    "order_id":"v1-250124055307-aa-6OZ8sm",
    "merchant_order_reference":"53cf1451-4dfd-417d-a1c8-c8bd603d5200",
    "type":"CHARGE",
    "status":"PENDING",
    "challenge_url":"https://pluraluat.v2.pinepg.in/web/auth/landing/?token=S50f2FXi%2FYAGe2bLZEW%2FA2VHzXthz0m9igmtsP61ODtY5u4pR6RYB5IlJwK0%2Fuo%2FBs9",
    "merchant_id":"111163",
    "order_amount":{
      "value":1600000,
      "currency":"INR"
    },
    "pre_auth":false,
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
    "purchase_details":{
      "customer":{
        "country_code":"91",
        "billing_address":{
          
        },
        "shipping_address":{
          
        },
        "is_edit_customer_details_allowed":false
      }
    },
    "payments":[
      {
        "id":"v1-250124055307-aa-6OZ8sm-ce-a",
        "merchant_payment_reference":"c7a7f778-b68f-462b-a6af-50698df12a4a",
        "status":"FAILED",
        "payment_amount":{
          "value":1550000,
          "currency":"INR"
        },
        "payment_method":"CREDIT_EMI",
        "offer_data":{
          "offer_details":{
            "id":"6",
            "name":"HDFC CC",
            "issuer_type":"CC_BANK",
            "priority":1,
            "tenure":{
              "tenure_id":"1",
              "name":"3 Months",
              "tenure_type":"MONTH",
              "tenure_value":3,
              "issuer_offer_parameters":[
                {
                  "program_type":"BANK_EMI",
                  "offer_id":"1803",
                  "offer_parameter_id":"72559"
                },
                {
                  "program_type":"MERCHANT_BANK_OFFER",
                  "offer_id":"1523",
                  "offer_parameter_id":"63566"
                }
              ],
              "details":[
                
              ],
              "discount":{
                "discount_type":"INSTANT",
                "amount":{
                  "currency":"INR",
                  "value":50000
                },
                "breakup":{
                  "merchant":{
                    
                  },
                  "issuer":{
                    
                  },
                  "brand":{
                    
                  },
                  "dealer":{
                    
                  }
                }
              },
              "loan_amount":{
                "currency":"INR",
                "value":1550000
              },
              "total_discount_amount":{
                "currency":"INR",
                "value":50000
              },
              "net_payment_amount":{
                "currency":"INR",
                "value":1601952
              },
              "monthly_emi_amount":{
                "currency":"INR",
                "value":533984
              },
              "total_emi_amount":{
                "currency":"INR",
                "value":1601952
              },
              "interest_amount":{
                "currency":"INR",
                "value":51952
              },
              "interest_rate_percentage":20,
              "processing_fee_details":{
                "amount":{
                  "currency":"INR",
                  "value":19900
                }
              },
              "processing_fee_amount":{
                "currency":"INR",
                "value":19900
              },
              "emi_type":"STANDARD"
            }
          }
        },
        "error_detail":{
          "code":"INTERNAL_ERROR",
          "message":"Payment processor is unavailable"
        },
        "created_at":"2025-01-24T05:53:24.476Z",
        "updated_at":"2025-01-24T05:53:25.492Z"
      },
      {
        "id":"v1-250124055307-aa-6OZ8sm-ce-b",
        "merchant_payment_reference":"32e3ba62-bb95-41bb-be81-1b87ab96c0ed",
        "status":"PENDING",
        "payment_amount":{
          "value":1550000,
          "currency":"INR"
        },
        "payment_method":"CREDIT_EMI",
        "payment_option":{
          "card_data":{
            "card_type":"CREDIT",
            "network_name":"VISA",
            "issuer_name":"INTL HDQTRS-CENTER OWNED",
            "card_category":"Consumer",
            "country_code":"IND",
            "token_txn_type":"ALT_TOKEN",
            "save":false
          }
        },
        "acquirer_data":{
          "approval_code":"",
          "acquirer_reference":"",
          "rrn":"",
          "is_aggregator":true
        },
        "offer_data":{
          "offer_details":{
            "id":"6",
            "name":"HDFC CC",
            "issuer_type":"CC_BANK",
            "priority":1,
            "tenure":{
              "tenure_id":"1",
              "name":"3 Months",
              "tenure_type":"MONTH",
              "tenure_value":3,
              "issuer_offer_parameters":[
                {
                  "program_type":"BANK_EMI",
                  "offer_id":"1803",
                  "offer_parameter_id":"72559"
                },
                {
                  "program_type":"MERCHANT_BANK_OFFER",
                  "offer_id":"1523",
                  "offer_parameter_id":"63566"
                }
              ],
              "details":[
                
              ],
              "discount":{
                "discount_type":"INSTANT",
                "amount":{
                  "currency":"INR",
                  "value":50000
                },
                "breakup":{
                  "merchant":{
                    
                  },
                  "issuer":{
                    
                  },
                  "brand":{
                    
                  },
                  "dealer":{
                    
                  }
                }
              },
              "loan_amount":{
                "currency":"INR",
                "value":1550000
              },
              "total_discount_amount":{
                "currency":"INR",
                "value":50000
              },
              "net_payment_amount":{
                "currency":"INR",
                "value":1601952
              },
              "monthly_emi_amount":{
                "currency":"INR",
                "value":533984
              },
              "total_emi_amount":{
                "currency":"INR",
                "value":1601952
              },
              "interest_amount":{
                "currency":"INR",
                "value":51952
              },
              "interest_rate_percentage":20,
              "processing_fee_details":{
                "amount":{
                  "currency":"INR",
                  "value":19900
                }
              },
              "processing_fee_amount":{
                "currency":"INR",
                "value":19900
              },
              "emi_type":"STANDARD"
            }
          }
        },
        "created_at":"2025-01-24T05:53:58.092Z",
        "updated_at":"2025-01-24T05:53:59.679Z"
      }
    ],
    "created_at":"2025-01-24T05:53:07.740Z",
    "updated_at":"2025-01-24T05:53:59.680Z",
    "integration_mode":"SEAMLESS",
    "payment_retries_remaining":8
  }
}
```

Refer to our <a style="text-decoration:none;" href="https://developer.pluralonline.com/reference/orders-get-by-order-id" target="_blank">Get Order by Order ID API</a> documentation to learn more.

## To Know Your Payment Status

To check your payment status, you can either rely on Webhook events or use our **Get Orders** APIs for real-time updates.

1. **Webhook Notification**: We send Webhook notifications on the successful payment or any changes to the payments object. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/developer-tools-webhook" target="_blank">Webhooks</a> documentation to learn more.
2. **Get Orders API**: Use our Get Orders API to know the real time status of the payment. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/order-manage#3-get-order-by-order-id" target="_blank">Manage Orders</a> documentation to learn more.
3. **Refunds**: Plural processes refund directly to the customer's original payment method to prevent chargebacks. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/payment-refund" target="_blank">Refunds</a> documentation to learn more.

## Pre Authorization Flow - Credit EMI

Our Orders API includes an optional **pre-authorization** feature. When pre-authorization is enabled (`pre_auth` = true), you can capture payment for an order after successful delivery, ensuring that settlement remains on hold until then.

Once pre-authorization is enabled and the payment is successfully processed, you have the following options:

**Capture Order**: Utilize the plural capture order API in your backend to capture the payment against an order.

**Cancel Order**: Use the plural cancel order API in your backend to cancel the payment against an order.

> 📘 Note:
> 
> - On successful payment we send the webhook event `ORDER_AUTHORIZED` and the status of the payment is updated to `authorized`.
> - You can capture or cancel an order only when the order status is `authorized`.

### 1. Capture Order

Use this API to capture the payment against an order. On successful capture of an order the order status is updated as `processed`.

Below are the sample requests and response for the Capture Order API.

```curl cURL - UAT
curl --request PUT \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/orders/order_id/capture \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
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
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
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
  "data":{
    "order_id":"v1-5757575757-aa-hU1rUd",
    "merchant_order_reference":"f4548bbf-a029-43d3-9209-e3385c80b1e9",
    "type":"CHARGE",
    "status":"PROCESSED",
    "merchant_id":"123456",
    "order_amount":{
      "value":1100,
      "currency":"INR"
    },
    "pre_auth":true,
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
    "notes":"order1",
    "purchase_details":{
      "customer":{
        "email_id":"kevin.bob@example.com",
        "first_name":"Kevin",
        "last_name":"Bob",
        "customer_id":"232323",
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
          "address2":"string",
          "address3":"string",
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
    },
    "payments":[
      {
        "id":"v1-1111071924-aa-zzSkOA-cc-G",
        "status":"PROCESSED",
        "payment_amount":{
          "value":1100,
          "currency":"INR"
        },
        "payment_method":"CARD",
        "payment_option":{
          "card_data":{
            "card_type":"CREDIT",
            "network_name":"VISA",
            "issuer_name":"NONE",
            "card_category":"CONSUMER",
            "country_code":"IND",
            "token_txn_type":"ALT_TOKEN"
          }
        },
        "acquirer_data":{
          "approval_code":"000000",
          "acquirer_reference":"202456643801053",
          "rrn":"420145000226"
        },
        "capture_data":[
          {
            "merchant_capture_reference":"f31d8c60-0dc8-4788-a577-5ced930cc175",
            "capture_amount":{
              "value":1100,
              "currency":"INR"
            },
            "created_at":"2024-07-19T11:13:21.523Z"
          }
        ],
        "created_at":"2024-07-19T11:11:48.944Z",
        "updated_at":"2024-07-19T11:13:23.962Z"
      }
    ],
    "created_at":"2024-07-19T11:11:48.944Z",
    "updated_at":"2024-07-19T11:13:23.962Z"
  }
}
```

Refer to our <a style="text-decoration:none;" href="https://developer.pluralonline.com/v3.0/reference/orders-capture" target="_blank">Capture Order API</a> documentation to learn more.

### 2. Cancel Order

Use this API to cancel the payment against an order.

Below are the sample requests and response for the Cancel Order API.

```curl cURL - UAT
curl --request PUT \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/cancel \
     --header 'accept: application/json'
```
```curl cURL - PROD
curl --request PUT \
     --url https://api.pluralpay.in/api/pay/v1/orders/{order_id}/cancel \
     --header 'accept: application/json'
```
```json Sample Response
{
  "data":{
    "order_id":"v1-250124055307-aa-6OZ8sm",
    "merchant_order_reference":"53cf1451-4dfd-417d-a1c8-c8bd603d5200",
    "type":"CHARGE",
    "status":"CANCELLED",
    "challenge_url":"https://pluraluat.v2.pinepg.in/web/auth/landing/?token=S50f2FXi%2FYAGe2bLZEW%2FA2VHzXthz0m9igmtsP61ODtY5u4pR6RYB5IlJwK0%2Fuo%2FBs9",
    "merchant_id":"111163",
    "order_amount":{
      "value":1600000,
      "currency":"INR"
    },
    "pre_auth":false,
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
    "purchase_details":{
      "customer":{
        "country_code":"91",
        "billing_address":{
          
        },
        "shipping_address":{
          
        },
        "is_edit_customer_details_allowed":false
      }
    },
    "payments":[
      {
        "id":"v1-250124055307-aa-6OZ8sm-ce-a",
        "merchant_payment_reference":"c7a7f778-b68f-462b-a6af-50698df12a4a",
        "status":"FAILED",
        "payment_amount":{
          "value":1550000,
          "currency":"INR"
        },
        "payment_method":"CREDIT_EMI",
        "offer_data":{
          "offer_details":{
            "id":"6",
            "name":"HDFC CC",
            "issuer_type":"CC_BANK",
            "priority":1,
            "tenure":{
              "tenure_id":"1",
              "name":"3 Months",
              "tenure_type":"MONTH",
              "tenure_value":3,
              "issuer_offer_parameters":[
                {
                  "program_type":"BANK_EMI",
                  "offer_id":"1803",
                  "offer_parameter_id":"72559"
                },
                {
                  "program_type":"MERCHANT_BANK_OFFER",
                  "offer_id":"1523",
                  "offer_parameter_id":"63566"
                }
              ],
              "details":[
                
              ],
              "discount":{
                "discount_type":"INSTANT",
                "amount":{
                  "currency":"INR",
                  "value":50000
                },
                "breakup":{
                  "merchant":{
                    
                  },
                  "issuer":{
                    
                  },
                  "brand":{
                    
                  },
                  "dealer":{
                    
                  }
                }
              },
              "loan_amount":{
                "currency":"INR",
                "value":1550000
              },
              "total_discount_amount":{
                "currency":"INR",
                "value":50000
              },
              "net_payment_amount":{
                "currency":"INR",
                "value":1601952
              },
              "monthly_emi_amount":{
                "currency":"INR",
                "value":533984
              },
              "total_emi_amount":{
                "currency":"INR",
                "value":1601952
              },
              "interest_amount":{
                "currency":"INR",
                "value":51952
              },
              "interest_rate_percentage":20,
              "processing_fee_details":{
                "amount":{
                  "currency":"INR",
                  "value":19900
                }
              },
              "processing_fee_amount":{
                "currency":"INR",
                "value":19900
              },
              "emi_type":"STANDARD"
            }
          }
        },
        "error_detail":{
          "code":"INTERNAL_ERROR",
          "message":"Payment processor is unavailable"
        },
        "created_at":"2025-01-24T05:53:24.476Z",
        "updated_at":"2025-01-24T05:53:25.492Z"
      },
      {
        "id":"v1-250124055307-aa-6OZ8sm-ce-b",
        "merchant_payment_reference":"32e3ba62-bb95-41bb-be81-1b87ab96c0ed",
        "status":"PENDING",
        "payment_amount":{
          "value":1550000,
          "currency":"INR"
        },
        "payment_method":"CREDIT_EMI",
        "payment_option":{
          "card_data":{
            "card_type":"CREDIT",
            "network_name":"VISA",
            "issuer_name":"INTL HDQTRS-CENTER OWNED",
            "card_category":"Consumer",
            "country_code":"IND",
            "token_txn_type":"ALT_TOKEN",
            "save":false
          }
        },
        "acquirer_data":{
          "approval_code":"",
          "acquirer_reference":"",
          "rrn":"",
          "is_aggregator":true
        },
        "offer_data":{
          "offer_details":{
            "id":"6",
            "name":"HDFC CC",
            "issuer_type":"CC_BANK",
            "priority":1,
            "tenure":{
              "tenure_id":"1",
              "name":"3 Months",
              "tenure_type":"MONTH",
              "tenure_value":3,
              "issuer_offer_parameters":[
                {
                  "program_type":"BANK_EMI",
                  "offer_id":"1803",
                  "offer_parameter_id":"72559"
                },
                {
                  "program_type":"MERCHANT_BANK_OFFER",
                  "offer_id":"1523",
                  "offer_parameter_id":"63566"
                }
              ],
              "details":[
                
              ],
              "discount":{
                "discount_type":"INSTANT",
                "amount":{
                  "currency":"INR",
                  "value":50000
                },
                "breakup":{
                  "merchant":{
                    
                  },
                  "issuer":{
                    
                  },
                  "brand":{
                    
                  },
                  "dealer":{
                    
                  }
                }
              },
              "loan_amount":{
                "currency":"INR",
                "value":1550000
              },
              "total_discount_amount":{
                "currency":"INR",
                "value":50000
              },
              "net_payment_amount":{
                "currency":"INR",
                "value":1601952
              },
              "monthly_emi_amount":{
                "currency":"INR",
                "value":533984
              },
              "total_emi_amount":{
                "currency":"INR",
                "value":1601952
              },
              "interest_amount":{
                "currency":"INR",
                "value":51952
              },
              "interest_rate_percentage":20,
              "processing_fee_details":{
                "amount":{
                  "currency":"INR",
                  "value":19900
                }
              },
              "processing_fee_amount":{
                "currency":"INR",
                "value":19900
              },
              "emi_type":"STANDARD"
            }
          }
        },
        "created_at":"2025-01-24T05:53:58.092Z",
        "updated_at":"2025-01-24T05:53:59.679Z"
      }
    ],
    "created_at":"2025-01-24T05:53:07.740Z",
    "updated_at":"2025-01-24T05:53:59.680Z",
    "integration_mode":"SEAMLESS",
    "payment_retries_remaining":8
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/v3.0/reference/orders-cancel" target="_blank">Cancel Order API</a> documentation to learn more.
