---
title: "Integration Steps (COPY)"
slug: "integration-steps-copy-1"
excerpt: "Learn how to integrate subscription APIs to automate plan creation, subscription management, and scheduled payments."
hidden: true
createdAt: "Wed Mar 05 2025 11:12:44 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Apr 14 2025 07:24:47 GMT+0000 (Coordinated Universal Time)"
---
**Auto-debit flow integration Steps**  
Follow the below steps to integrate with Plural subscription APIs.

1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#1-prerequisite-generate-token" >\[Prerequisite] Generate Token</a>
2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#2-create-plan" >Create Plan</a>
3. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#4-create-subscription" >Create Subscription</a>
4. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#5-create-payment" >Create Payment</a>
5. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#6-handle-payment" >Handle Payment</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#61-store-payment-details-on-your-server" >Store Payment Details on Your Server</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/integration-steps-1#62-verify-payment-signature" >Verify Payment Signature</a>

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

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/v3.0/reference/generate-token" target="_blank">Generate Token API</a> documentation to learn more.

<details><summary>Click here for request and response parameter information.</summary>

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid #5A0083;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n    </style>\n</head>\n<body>\n    <div class=\"tab-container\">\n        <div class=\"tab active\" data-target=\"tab1\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Request Parameters</div>\n\n        <div class=\"tab\" data-target=\"tab2\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Response Parameters</div>\n\n    <div id=\"tab1\" class=\"tab-content active\">\n      \n      <p>The table below lists the request parameters of our Generate Token API.</p>\n\n<table>\n    <thead>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td>client_id*</td>\n          <td><code>string</code></td>\n            <td>\n                Unique client identifier in the Plural database.<br><br>\n              Example: <code>a17ce30e-f88e-4f81-ada1-c3b4909ed232</code><br><br>\n                <strong>Note:</strong> The Onboarding team has provided you with this information as part of the onboarding process.\n            </td>\n        </tr>\n        <tr>\n            <td>client_secret*</td>\n          <td><code>string</code></td>\n            <td>\n                Unique client secret key provided while onboarding.<br><br>\n              Example: <code>fgwei7egyhuggwp39w8rh</code><br><br>\n                <strong>Note:</strong> The Onboarding team has provided you with this information as part of the onboarding process.\n            </td>\n        </tr>\n        <tr>\n            <td>grant_type*</td>\n          <td><code>string</code></td>\n            <td>\n                The grant type to generate an access token.<br><br>\n              Accepted value: <code>client_credentials</code>\n            </td>\n        </tr>\n    </tbody>\n</table>\n\n      \n    </div>\n    <div id=\"tab2\" class=\" tab-content\">\n      \n      <p style=\"\">The table below lists the response parameters of our Generate Token API.</p> \n      <table>\n    <thead>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th> <!-- Ensure this is present -->\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td>access_token</td>\n            <td><code>string</code></td>\n            <td>\n                The access token generated by the system.<br><br>\n                • Minimum length: 1 character.<br>\n                • Maximum length: 8192 characters.<br><br>\n                Example: <code>eyJhbGciOiJIUzI1NiIsIn</code><br><br>\n                <strong>Note:</strong> Use this token in the authorization headers to authenticate Plural APIs.\n            </td>\n        </tr>\n        <tr>\n            <td>expires_at</td>\n            <td><code>string</code></td>\n            <td>\n                Access duration timestamp.<br><br>\n                Example: <code>2024-06-28T13:26:06.909140Z</code>\n            </td>\n        </tr>\n    </tbody>\n</table>\n\n      \n    </div>\n</body>\n</html>\n"
}
[/block]


</details>

## 2. Create Plan

Use this API to Create a Plan.

To authenticate this API, use the generated access token in the Authorization headers of the API request.

Below are the sample requests and response for the Create Plan API.

```curl cURL – UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/v1/public/plans \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "plan_name": "Monthly Plan",
  "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
  "frequency": "Day",
  "amount": {
    "value": 100,
    "currency": "INR"
  },
  "max_limit_amount": {
    "value": 100,
    "currency": "INR"
  },
  "trial_period_in_days": 1,
  "start_date": "2022-02-01T17:32:28Z",
  "end_date": "2022-10-21T17:32:28Z",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "merchant_plan_reference": "1234567890"
}
'
```
```curl cURL – PROD
curl --request POST \
     --url https://api.pluralpay.in/api/v1/public/plans \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "plan_name": "Monthly Plan",
  "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
  "notes": "string",
  "frequency_count": 1,
  "frequency": "Day",
  "amount": {
    "value": 100,
    "currency": "INR"
  },
  "max_limit_amount": {
    "value": 100,
    "currency": "INR"
  },
  "trial_period_in_days": 1,
  "start_date": "2022-02-01T17:32:28Z",
  "end_date": "2022-10-21T17:32:28Z",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "merchant_order_reference": "1234567890"
}
'
```
```json Sample Response
{
  "plan_id": "v1-plan-4405071524-aa-qlAtAf",
  "status": "ACTIVE",
  "plan_name": "Monthly Plan",
  "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
  "notes": "string",
  "frequency_count": 1,
  "frequency": "Day",
  "amount": {
    "value": 100,
    "currency": "INR"
  },
  "max_limit_amount": {
    "value": 100,
    "currency": "INR"
  },
  "trial_period_in_days": 1,
  "start_date": "2022-02-01T17:32:28Z",
  "end_date": "2022-10-21T17:32:28Z",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "merchant_order_reference": "1234567890",
  "created_at": "2022-10-21T17:32:28Z",
  "modified_at": "2022-10-21T17:32:28Z"
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/create-plan" target="_blank">Create Plan API</a> documentation to learn more.

<details><summary>Click here for request and response parameter information.</summary>

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid #5A0083;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n    </style>\n</head>\n<body>\n    <div class=\"tab-container\">\n        <div class=\"tab active\" data-target=\"tab3\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Request Parameters</div>\n\n        <div class=\"tab\" data-target=\"tab4\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Response Parameters</div>\n\n    <div id=\"tab3\" class=\"tab-content active\">\n      \n      \n      <body>\n    <p>The table below lists the request parameters of our Create Plan API.</p>\n    <table>\n        <thead>\n            <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td>plan_name*</td>\n            <td><code>string</code></td>\n            <td>Subscription plan name.<br><br>\n                Example: <code>Monthly Plan</code>\n            </td>\n        </tr>\n        <tr>\n            <td>plan_description</td>\n            <td><code>string</code></td>\n            <td>Corresponding description for a plan.<br><br>\n                Example: <code>Diwali Dhammaka plan intended to attract customers on Diwali time</code>\n            </td>\n        </tr>\n        <tr>\n            <td>frequency*</td>\n            <td><code>string</code></td>\n            <td>Frequency of recurring transactions for this particular plan.<br><br>\n                Possible values:<ul>\n                    <li><code>Day</code></li>\n                    <li><code>Week</code></li>\n                    <li><code>Month</code></li>\n                    <li><code>Year</code></li>\n                    <li><code>AS</code></li>\n                    <li><code>OT</code></li>\n                    <li><code>Not Applicable</code></li>\n                </ul>\n                Example: <code>Day</code>\n            </td>\n        </tr>\n        <tr>\n            <td>amount*</td>\n            <td><code>object</code></td>\n            <td>An object that contains the amount details.<br><br>Learn more about the <code>amount</code> child object.\n                </a>\n            </td>\n        </tr>\n        <tr>\n            <td>max_limit_amount*</td>\n            <td><code>object</code></td>\n            <td>An object that contains the maximum limit amount details.<br><br>Learn more about the <code>max_limit_amoun</code> child object.\n                </a>\n            </td>\n        </tr>\n        <tr>\n            <td>trial_period_in_days</td>\n            <td><code>integer</code></td>\n            <td>When a trial period is offered for the plan, this defines the duration of the trial period.<br><br>\n                Example: <code>1</code>\n            </td>\n        </tr>\n        <tr>\n            <td>start_date</td>\n            <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp is the date when the subscription plan is active and available for use.<br><br>\n                Example: <code>2022-02-01T17:32:28Z</code>\n            </td>\n        </tr>\n        <tr>\n            <td>end_date*</td>\n            <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp is the date when the subscription plan expires and can no longer be used for new subscriptions.<br><br>\n                Example: <code>2022-09-21T17:32:28Z</code>\n            </td>\n        </tr>\n        <tr>\n            <td>merchant_metadata</td>\n            <td><code>object</code></td>\n            <td>An object of key-value pairs that can be used to store additional information.<br><br>\n                Constraints:<ul>\n                    <li>Each pair cannot exceed <code>256</code> characters.</li>\n                    <li>Maximum <code>10</code> key-value pairs.</li>\n                </ul>\n                Example: <code>\"key1\": \"DD\"</code>\n            </td>\n        </tr>\n        <tr>\n            <td>merchant_plan_reference*</td>\n            <td><code>string</code></td>\n            <td>Unique identifier of the merchant plan reference entered while creating a plan.<br><br>\n                Constraints:<ul>\n                    <li>Minimum: 1 character.</li>\n                    <li>Maximum: 50 characters.</li>\n                </ul>\n                Example: <code>1234567890</code><br><br>\n                Supported characters:<ul>\n                    <li><code>A-Z</code></li>\n                    <li><code>a-z</code></li>\n                    <li><code>0-9</code></li>\n                    <li><code>-</code></li>\n                    <li><code>_</code></li>\n                </ul>\n            </td>\n        </tr>\n    </tbody>\n</table>\n    <h2>Amount [Child Object]</h2>\n        <p> The table below lists the various parameters in the <code>amount</code> child object. This object is part of the <code>create plan</code> request object.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value*</td>\n                <td><code>integer</code></td>\n                <td>\n                    Transaction amount in Paisa.<br><br><ul><li>\n                  Minimum value: <code>100</code> (₹1).</li><li>\n                  Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>\n          Example: <code>1000</code>\n                </td>\n            </tr>\n            <tr>\n                <td>currency*</td>\n                <td><code>string</code></td>\n                <td>\n                    Type of currency.<br><br>\n                  Example: <code>INR</code>\n                </td>\n            </tr>\n        </tbody>\n    </table>\n\t\t<h2>Max limit amount [Child Object]</h2>\n\t\t<p>The table below lists the various parameters in the <code>max_limit_amount</code> child object. This object is part of the <code>create plan</code> request object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>value*</td>\n          <td><code>integer</code></td>\n          <td>Transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1).</li><li>Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>Example: <code>100</td>\n        </tr>\n        <tr>\n            <td>currency</td>\n          <td><code>string</code></td>\n          <td>Type of currency*.<br><br>Example: <code>INR</code></td>\n        </tr>\n    </table>\n\n         \n    </div>\n    <div id=\"tab4\" class=\" tab-content\">\n      \n      \n        <body>\n          <p>The table below lists the various parameters returned in the Create Plan response objects.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n\t\t\t<td>plan_id</td>\n            <td><code>string</code></td>\n            <td>\n                Unique identifier for the subscription plan in the Plural database.<br><br>\n                Example: <code>v1-plan-4405071524-aa-qlAtAf</code>\n            </td>\n        </tr>\n      <tr>\n            <td>status</td>\n            <td><code>string</code></td>\n            <td>\n                Status of the plan.<br><br>\n                Possible values:<ul>\n                    <li><code>ACTIVE</code>: When the create plan request is successfully created.</li>\n                    <li><code>INACTIVE</code>: When the plan is disabled and cannot be used for new subscriptions.</li>\n                    <li><code>CREATED</code>: When the plan setup is completed but not yet activated.</li>\n                    <li><code>EXPIRED</code>: When the plan has surpassed its validity period and is no longer available.</li>\n                    <li><code>PAUSED</code>: When the plan is temporarily halted and can be resumed later.</li>\n                    <li><code>ARCHIVED</code>: When the plan is permanently deactivated and stored for record-keeping.</li>\n                </ul>\n            </td>\n        </tr>\n        <tr>\n            <td>plan_name</td>\n            <td><code>string</code></td>\n            <td>\n                Subscription plan name.<br><br>\n                Example: <code>Monthly Plan</code>\n            </td>\n        </tr>\n        <tr>\n            <td>plan_description</td>\n            <td><code>string</code></td>\n            <td>\n                Corresponding description for a plan.<br><br>\n                Example: <code>Diwali dhammaka plan intended to attract customers on diwali time</code>\n            </td>\n        </tr>\n        <tr>\n            <td>frequency</td>\n            <td><code>string</code></td>\n            <td>\n                Frequency of recurring transactions for this particular plan.<br><br>\n                Possible values:<ul>\n                    <li><code>Day</code></li>\n                    <li><code>Week</code></li>\n                    <li><code>Month</code></li>\n                    <li><code>Year</code></li>\n                    <li><code>AS</code></li>\n                    <li><code>OT</code></li>\n                    <li><code>Not Applicable</code></li>\n                </ul>\n                Example: <code>Day</code>\n            </td>\n        </tr>\n        <tr>\n            <td>amount</td>\n            <td><code>object</code></td>\n            <td>\n                An object that contains the amount details.<br><br>\n                Learn more about the <code>amount</code> child object.\n            </td>\n        </tr>\n        <tr>\n            <td>max_limit_amount</td>\n            <td><code>object</code></td>\n            <td>\n                An object that contains the maximum limit amount details.<br><br>\n                Learn more about the <code>max_limit_amount</code> child object.\n            </td>\n        </tr>\n        <tr>\n            <td>trial_period_in_days</td>\n            <td><code>integer</code></td>\n            <td>\n                When a trial period is offered for the plan, this defines the duration of the trial period.<br><br>\n                Example: <code>1</code><br><br>\n                <strong>Note:</strong> The trial period is always measured in days.\n            </td>\n        </tr>\n        <tr>\n            <td>start_date</td>\n            <td><code>string</code></td>\n            <td>\n                The ISO 8601 UTC Timestamp is the date when the subscription plan is active and available for use.<br><br>\n                Example: <code>2022-02-01T17:32:28Z</code>\n            </td>\n        </tr>\n        <tr>\n            <td>end_date</td>\n            <td><code>string</code></td>\n            <td>\n                The ISO 8601 UTC Timestamp is the date when the subscription plan expires and can no longer be used for new subscriptions.<br><br>\n                Example: <code>2022-09-21T17:32:28Z</code>\n            </td>\n        </tr>\n      <tr>\n            <td>merchant_metadata</td>\n            <td><code>object</code></td>\n            <td>\n                An object of key-value pair that can be used to store additional information.<br><br>\n                <ul>\n                    <li>Each pair cannot exceed <code>256</code> characters.</li>\n                    <li>Maximum <code>10</code> key-value pairs.</li>\n                </ul>\n                Example: <code>\"key1\": \"DD\"</code>\n            </td>\n        </tr>\n        <tr>\n            <td>merchant_plan_reference</td>\n            <td><code>string</code></td>\n            <td>\n                Unique identifier of the merchant plan reference entered while creating a plan.<br><br>\n                <ul>\n                    <li>Minimum length: 1 character.</li>\n                    <li>Maximum length: 50 characters.</li>\n                </ul>\n                Example: <code>1234567890</code>\n            </td>\n        </tr>\n        <tr>\n            <td>created_at</td>\n            <td><code>string</code></td>\n            <td>\n                The ISO 8601 UTC Timestamp, when the create plan request was received by Plural.<br><br>\n                Example: <code>2022-09-21T17:32:28Z</code>\n            </td>\n        </tr>\n        <tr>\n            <td>modified_at</td>\n            <td><code>string</code></td>\n            <td>\n                The ISO 8601 UTC Timestamp, when the plan object is updated.<br><br>\n                Example: <code>2022-09-21T17:32:28Z</code>\n            </td>\n        </tr>\n        \n        \n    </tbody>\n</table>\n<h2>Amount [Child Object]</h2>\n        <p> The table below lists the various parameters in the <code>amount</code> child object. This object is part of the <code>create plan</code> response object.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value*</td>\n                <td><code>integer</code></td>\n                <td>\n                    Transaction amount in Paisa.<br><br><ul><li>\n                  Minimum value: <code>100</code> (₹1).</li><li>\n                  Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>\n          Example: <code>1000</code>\n                </td>\n            </tr>\n            <tr>\n                <td>currency*</td>\n                <td><code>string</code></td>\n                <td>\n                    Type of currency.<br><br>\n                  Example: <code>INR</code>\n                </td>\n            </tr>\n        </tbody>\n    </table>\n\t\t<h2>Max limit amount [Child Object]</h2>\n\t\t<p>The table below lists the various parameters in the <code>max_limit_amount</code> child object. This object is part of the <code>create plan</code> response object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>value</td>\n          <td><code>integer</code></td>\n          <td>The transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1).</li><li>Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>Example: <code>100</td>\n        </tr>\n        <tr>\n            <td>currency</td>\n          <td><code>string</code></td>\n          <td>Type of currency.<br><br>\n            Example: <code>INR</code>\n          </td>\n        </tr>\n    </table>\n   </div>\n</body>\n</html>\n"
}
[/block]


</details>

## 3. Create Subscription

To Create Subscription, use our Create subscription API, use the `plan_id `returned in the response of a Create Plan API to link the subscription with a plan.

For authentication use the generated access token in the headers of the API request.

Below are the sample requests and response for the Create subscription API.

```curl cURL – UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/v1/public/subscriptions \
     --header 'Authorization: Bearer https://pluraluat.v2.pinepg.in/api/v1/public/plans' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_subscription_reference": "1234567890",
  "enable_notification": true,
  "plan_id": "v1-plan-4405071524-aa-qlAtAf",
  "callback_url": "https://www.example.com",
  "quantity": 1,
  "start_date": "2022-07-21T17:32:28Z",
  "end_date": "2022-09-21T17:32:28Z",
  "customer_id": "123456",
  "allowed_payment_methods": [
    "UPI"
  ],
  "integration_mode": "SEAMLESS",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "is_tpv_enabled": false,
  "bank_account": {
    "account_number": "123456789012345",
    "name": "Gaurav Kumar",
    "ifsc": "123456789012345"
  }
}
'
```
```curl cURL – PROD
curl --request POST \
     --url https://api.pluralpay.in/api/v1/public/subscriptions \
     --header 'Authorization: Bearer https://pluraluat.v2.pinepg.in/api/v1/public/plans' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_order_reference": "1234567890",
  "enable_notification": true,
  "plan_id": "v1-plan-4405071524-aa-qlAtAf",
  "webhook_url": "https://www.subscription-url-webhook.com",
  "quantity": 1,
  "start_date": "2022-07-21T17:32:28Z",
  "end_date": "2022-09-21T17:32:28Z",
  "customer_id": "123456",
  "payment_mode": [
    "UPI"
  ],
  "integration_mode": "SEAMLESS",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "is_tpv_enabled": true,
  "bank_account": {
    "account_number": "123456789012345",
    "name": "Gaurav Kumar",
    "ifsc": "123456789012345"
  }
}
'
```
```json Sample Response
{
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "merchant_order_reference": "1234567890",
  "enable_notification": true,
  "plan_details": {
    "plan_id": "v1-plan-4405071524-aa-qlAtAf",
    "status": "ACTIVE",
    "plan_name": "Monthly Plan",
    "plan_description": "Diwali dhammaka plan intended to attract customers on diwali time",
    "notes": "string",
    "frequency_count": 1,
    "frequency": "Day",
    "amount": {
      "value": 100,
      "currency": "INR"
    },
    "max_limit_amount": {
      "value": 100,
      "currency": "INR"
    },
    "trial_period_in_days": 1,
    "start_date": "2022-02-01T17:32:28Z",
    "end_date": "2022-10-21T17:32:28Z",
    "merchant_metadata": {
      "key1": "DD",
      "key2": "XOF"
    },
    "merchant_order_reference": "1234567890",
    "created_at": "2022-10-21T17:32:28Z",
    "modified_at": "2022-10-21T17:32:28Z"
  },
  "quantity": 1,
  "start_date": "2022-07-21T17:32:28Z",
  "end_date": "2022-09-21T17:32:28Z",
  "customer_id": "123456",
  "payment_mode": [
    "UPI"
  ],
  "integration_mode": "SEAMLESS",
  "webhook_url": "https://www.subscription-url-webhook.com",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "status": "ACTIVE",
  "bank_account": {
    "account_number": "123456789012345",
    "name": "Gaurav Kumar",
    "ifsc": "123456789012345"
  },
  "is_tpv_enabled": true,
  "created_at": "2022-10-21T17:32:28Z",
  "modified_at": "2022-10-21T17:32:28Z",
  "order_id": "v1-4405071524-aa-qlAtAf",
  "redirect_url": "https://api-staging.pluralonline.com/api/v3/checkout-bff/redirect/checkout?token=V3_D7LwszJqF2XRiFq46uOXQr0sQn8XbObLh7WM9YF8OAxQDYRnCMbhYgHbgFf4vCjJ%22&subscription_id=v1-sub-4405071524-aa-qlAtAf"
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/create-subscription" target="_blank">Create subscription API</a> documentation to learn more.

<details><summary>Click here for request and response parameter information.</summary>

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid #5A0083;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n    </style>\n</head>\n<body>\n    <div class=\"tab-container\">\n        <div class=\"tab active\" data-target=\"tab5\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Request Parameters</div>\n\n        <div class=\"tab\" data-target=\"tab6\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Response Parameters</div>\n\n    <div id=\"tab5\" class=\"tab-content active\">\n      \n      \n      <body>\n    <p>The table below lists the request parameters of our Create Subscription API.</p>\n    <table>\n        <thead>\n            <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n    </thead>\n    <tbody>\n      <tr>\n            <td>merchant_subscription_reference*</td>\n            <td><code>string</code></td>\n            <td>Unique identifier of the merchant order reference entered while creating a plan.<br><br>\n                Constraints:<ul>\n                    <li>Minimum: 1 character.</li>\n                    <li>Maximum: 50 characters.</li>\n                </ul>\n                Example: <code>1234567890</code><br><br>\n                Supported characters:<ul>\n                    <li><code>A-Z</code></li>\n                    <li><code>a-z</code></li>\n                    <li><code>0-9</code></li>\n                    <li><code>-</code></li>\n                    <li><code>_</code></li>\n                </ul>\n            </td>\n        </tr>\n      <tr>\n        <td>enable_notification</td>\n        <td><code>boolean</code></td>\n        <td>Indicates if notifications are enabled.<br><br>Example: <code>true</code></td>\n      </tr>\n      <tr>\n\t\t\t<td>plan_id*</td>\n            <td><code>string</code></td>\n            <td>\n                Unique identifier for the subscription plan in the Plural database.<br><br>\n                Example: <code>v1-plan-4405071524-aa-qlAtAf</code>\n            </td>\n        </tr>\n        <tr>\n            <td>callback_url</td>\n            <td><code>string</code></td>\n            <td>Use this URL to redirect your customers to specific success or failure pages based on the order or product details.<br><br>Example: <code>https\\://sample-callback-url>/td></code>\n            </td>\n        </tr>\n        <tr>\n            <td>quantity</td>\n            <td><code>integer</code></td>\n            <td>The quantity of the subscription for the selected plan, should be greater than 0.<br><br>Example: <code>1</code>\n            </td>\n        </tr>\n       <tr>\n            <td>start_date*</td>\n            <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp is the date when the subscription plan is active and available for use.<br><br>\n                Example: <code>2022-02-01T17:32:28Z</code>\n            </td>\n        </tr>\n        <tr>\n            <td>end_date*</td>\n            <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp is the date when the subscription plan expires and can no longer be used for new subscriptions.<br><br>\n                Example: <code>2022-09-21T17:32:28Z</code>\n            </td>\n        </tr>\n        <tr>\n            <td>customer_id*</td>\n            <td><code>string</code></td>\n            <td>Unique identifier of the customer in the Plural database.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 19 characters.</ul></li>Example: <code>123456</code>\n            </td>\n        </tr>\n        <tr>\n            <td>allowed_payment_methods</td>\n            <td><code>string</code></td>\n            <td>The type of payment methods you want to offer customers.<br><br>                   Accepted values:<ul><li><code>CARD</code></li><li><code>UPI</code></li><li><code>POINTS</code></li><li><code>NETBANKING</code></li><li><code>WALLET</code></li></ul></li>Example: <code>UPI</code></td>\n        </tr>\n        <tr>\n            <td>integration_mode*</td>\n            <td><code>string</code></td>\n            <td>The integration mode for the subscription.<br><br>Accepted values:<ul><li><code>SEAMLESS</code></ul></li>Example: <code>SEAMLESS</code>\n            </td>\n\t\t\t\t</tr>\n        <tr>\n            <td>merchant_metadata</td>\n            <td><code>object</code></td>\n            <td>An object of key-value pairs that can be used to store additional information.<br><br>\n                Constraints:<ul>\n                    <li>Each pair cannot exceed <code>256</code> characters.</li>\n                    <li>Maximum <code>10</code> key-value pairs.</li>\n                </ul>\n                Example: <code>\"key1\": \"DD\"</code>\n            </td>\n  \t\t\t</tr>\n<tr>\n  <td>is_tpv_enabled</td>\n  <td><code>boolean</code></td>\n  <td>Indicates if Third-Party Validation (TPV) is enabled.<br><br>Example: <code>true</code></td>\n</tr>\n<tr>\n  <td>bank_account</td>\n  <td><code>object</code></td>\n            <td>\n                An object that contains the bank amount details.<br><br>\n              Learn more about the <code>bank_account</code>child object.</td>\n</tr>\n    </tbody>\n</table>\n    <h2>Bank Account [Child Object]</h2>\n        <p> The table below lists the various parameters in the <code>bank_account</code> child object. This object is part of the <code>Create subscription</code> request object.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>account_number*</td>\n                <td><code>string</code></td>\n                <td>Customer's bank account number.<ul><li>Minimum length: 1 characters</li><li>Maximum length: 50 characters.</ul></li>Example: <code>04992990009595</code>      \n                </td>\n</tr>\n<tr>\n  <td>name*</td>\n   <td><code>string</code></td>\n<td>Name of Customer.<br><br>Example: <code>Kevin Bob</code></td>\n</tr>\n<tr>\n<td>ifsc*</td>\n<td><code>string</code></td>\n<td>IFSC code of the bank account.<ul><li>Minimum: 11 characters</li><li>Maximum: 11 characters</ul></li>Example: <code>HDFC0001234</code></li><br><br>Supported Characters:<ul><li>A-Z (Uppercase letters)</li><li>0-9 (Digits)</li></ul></td>\n</tr>\n</table>\n\n         \n    </div>\n    <div id=\"tab6\" class=\" tab-content\">\n      \n      \n        <body>\n          <p>The table below lists the various parameters returned in the Create Subscription response objects.</p>\n    <table>\n      <wrap>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n\t\t\t<td>subscription_id</td>\n            <td><code>string</code></td>\n            <td> Unique identifier for the subscription plan in the plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: <code>v1-sub-4405071524-aa-qlAtAf</code></td>\n        </tr>\n          <tr>\n            <td>order_id</td>\n            <td><code>string</code></td>\n            <td>Unique identifier of the order in the Plural database.<br><br>Example: <code>v1-4405071524-aa-qlAtAf</code></td>\n          </tr>\n        <tr>\n            <td>merchant_subscription_reference</td>\n            <td><code>string</code></td>\n            <td>Unique identifier of the merchant subscription reference entered while creating a suscription.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: <code>1234567890</code></td>\n        </tr>\n        <tr>\n            <td>enable_notification</td>\n            <td><code>boolean</code></td>\n          <td>Indicates if notifications are enabled.<br><br>Example: <code>true</code></td>\n        </tr>\n        <tr>\n            <td>plan_details</td>\n            <td><code>Array of Objects</code></td>\n            <td>An array of object that contain plan details.<br><br>\n              Learn more about the <code>plan details</code> child object.</a></td>\n        </tr>\n        <tr>\n            <td>quantity</td>\n            <td><code>integer</code></td>\n            <td>The quantity of the subscription for the selected plan, should be greater than 0.<br><br>Example: <code>1</code></td>\n        </tr>\n        <tr>\n            <td>start_date</td>\n            <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp is the date when the subscription plan is active and available for use.<br><br>Example: <code>2022-02-01T17:32:28Z</code></td>\n        </tr>\n        <tr>\n            <td>end_date</td>\n            <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp is the date when the subscription plan expires and can no longer be used for new subscriptions.<br><br>\n                Example: <code>2022-09-21T17:32:28Z</code></td>\n        </tr>\n        <tr>\n            <td>customer_id</td>\n            <td><code>string</code></td>\n            <td>Unique identifier of the customer in the Plural database.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 19 characters.</ul></li>Example: <code>123456</code></td>\n        </tr>\n        <tr>\n            <td>payment_mode</td>\n            <td><code>string</code></td>\n            <td>Payment methods allowed for subscription.<br>Accepted values:<ul><li><code>CARD</code></li><li><code>UP</code></ul></li>Example: <code>UPI</code></td>\n        </tr>\n<tr>\n            <td>allowed_payment_methods</td>\n            <td><code>string</code></td>\n            <td>The type of payment methods you want to offer customers.<br><br>                   Accepted values:<ul><li><code>CARD</code></li><li><code>UPI</code></li><li><code>POINTS</code></li><li><code>NETBANKING</code></li><li><code>WALLET</code></li></ul></li>Example: <code>UPI</code></td>\n        </tr>\n        <tr>\n            <td>integration_mode</td>\n            <td><code>string</code></td>\n            <td>The integration mode for the subscription.<br><br>Accepted values:<ul><li><code>SEAMLESS</code></ul></li>Example: <code>SEAMLESS</code> </td>\n</tr>\n<tr>\n  <td>callback_url</td>\n  <td><code>string</code></td>\n  <td>Use this URL to redirect your customers to specific success or failure pages based on the order or product details.<br><br>Example: <code>https\\://sample-callback-url>/td></code></td>\n           </tr>\n<tr>\n            <td>merchant_metadata</td>\n            <td><code>object</code></td>\n            <td>An object of key-value pairs that can be used to store additional information.<br><br>\n                Constraints:<ul><li>Each pair cannot exceed <code>256</code> characters.</li>\n              <li>Maximum <code>10</code> key-value pairs.</li> </ul>Example: <code>\"key1\": \"DD</code></td>\n  </tr>\n<tr>\n  <td>status</td>\n  <td><code>string</code></td>\n  <td>Status of the Subscription.<br><br>Possible values:<ul><li><code>ACTIVE</code>: When the subscription is currently active and payments are being processed as per the billing cycle.</li><li><code>INACTIVE</code>: When the subscription has been created but is not yet activated.</li><li><code>CREATED</code>: When the subscription has been successfully created but is not yet active.</li><li><code>REGISTERED</code>: When the subscription has been registered successfully.</li><li><span style=\"word-break: break-word;\"><code>CANCELLED_BY_CUSTOMER_DURING_PRE_DEBIT_NOTIFICATION</span></code>: When the customer canceled the subscription during the pre-debit notification stage.</li><li><code>ARCHIVED</code>: When the subscription has been archived and is no longer active.</li><li><code>CANCELLED_BY_CUSTOMER_DURING_MANDATE_CREATION</code>: When the customer canceled the subscription while setting up the payment mandate.</li><li><code>CANCELLED_BY_MERCHANT</code>: When the subscription was canceled by the merchant.</li><li><code>DEBIT_FAILED</code>: When the scheduled payment for the subscription failed.</li><li><code>PAUSED</code>: When the subscription has been temporarily paused.</li><li><code>CANCELLED</code>: When the subscription has been canceled and is no longer active.</li><li><code>TRIAL</code>: When the subscription is in its trial period before regular billing starts.</li><li><code>REVOKE_INITIATED</code>: When a request to revoke the subscription has been initiated.</li><li><code>COMPLETED</code>: When the subscription has successfully completed its billing cycle.</li><li><code>CANCELLED_BY_CUSTOME</code>`: When the customer has canceled the subscription.</li><li><code>PAUSED_BY_CUSTOMER</code>: When the customer has temporarily paused the subscription.</li><li><code>RESUMED_BY_CUSTOMER</code>: When the customer has resumed a previously paused subscription.</li><li><code>EXPIRED</code>: When the subscription has reached its end date and expired.</li><li><code>HALTED</code>: When the subscription has been stopped due to an issue or external intervention.</li><li><code>RESUMED</code>: When the subscription has been resumed after being paused or halted.</ul></li></td>\n</tr>\n<tr>\n  <td>bank_account</td>\n  <td><code>object</code></td>\n            <td>An object that contains the bank amount details.<br><br>Learn more about the <code>bank_account</code>child object.</td>\n</tr>\n<tr>\n  <td>is_tpv_enabled</td>\n  <td><code>boolean</code></td>\n  <td>Indicates if Third-Party Validation (TPV) is enabled.<br><br>Example: <code>true</code></td>\n</tr>\n<tr>\n  <td>created_at</td>\n  <td><code>string</code></td>\n  <td>The ISO 8601 UTC Timestamp, when the create plan request was received by Plural.<br><br>Example: <code>2022-09-21T17:32:28Z</code></td>\n</tr>\n<tr>\n  <td>modified_at</td>\n  <td><code>string</code></td>\n  <td>The ISO 8601 UTC Timestamp, when the plan object is updated.<br><br>Example: <code>2022-09-21T17:32:28Z</code></td>\n</tr>\n<tr>\n  <td>redirect_url</td>\n  <td><code>string</code></td>\n  <td>URL for redirection after checkout.<br><br>Example: <code>https://api-staging.pluralonline.com/api/v3/checkout-bff/redirect/checkout?...subscription_id=v1-sub-4405071524-aa-qlAtAf></code></td>\n</tr>\n    </tbody>\n</wrap>\n</table>\n<h2>Plan details [Child Object]</h2>\n        <p> The table below lists the various parameters in the <code>plan details</code> child object. This object is part of the <code>Create Subscription</code> response object.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n\t\t\t<td>plan_id</td>\n            <td><code>string</code></td>\n            <td>Unique identifier for the subscription plan in the Plural database.<br><br>\n                Example: <code>v1-plan-4405071524-aa-qlAtAf</code></td>\n        </tr>\n          <tr>\n            <td>status</td>\n            <td><code>string</code></td>\n            <td>Status of the plan.<br><br>\n                Possible values:<ul>\n                    <li><code>ACTIVE</code>: When the create plan request is successfully created.</li>\n                    <li><code>INACTIVE</code>: When the plan is disabled and cannot be used for new subscriptions.</li>\n                    <li><code>CREATED</code>: When the plan setup is completed but not yet activated.</li>\n                    <li><code>EXPIRED</code>: When the plan has surpassed its validity period and is no longer available.</li>\n                    <li><code>PAUSED</code>: When the plan is temporarily halted and can be resumed later.</li>\n                    <li><code>ARCHIVED</code>: When the plan is permanently deactivated and stored for record-keeping.</li>\n                </ul></td>\n        </tr>\n        <tr>\n            <td>plan_name</td>\n            <td><code>string</code></td>\n            <td>Subscription plan name.<br><br>Example: <code>Monthly Plan</code></td>\n        </tr>\n        <tr>\n            <td>plan_description</td>\n            <td><code>string</code></td>\n            <td>Corresponding description for a plan.<br><br>\n                Example: <code>Diwali dhammaka plan intended to attract customers on diwali time</code></td>\n          </tr>\n        <tr>\n            <td>frequency</td>\n            <td><code>string</code></td>\n            <td>Frequency of recurring transactions for this particular plan.<br><br>\n                Possible values:<ul>\n                    <li><code>Day</code></li>\n                    <li><code>Week</code></li>\n                    <li><code>Month</code></li>\n                    <li><code>Year</code></li>\n                    <li><code>AS</code></li>\n                    <li><code>OT</code></li>\n                    <li><code>Not Applicable</code></li>\n                </ul>\n              Example: <code>Day</code></td>\n        </tr>\n        <tr>\n            <td>amount</td>\n            <td><code>object</code></td>\n            <td> An object that contains the amount details.<br><br>\n                Learn more about the <code>amount</code> child object.</td>\n        </tr>\n        <tr>\n            <td>max_limit_amount</td>\n            <td><code>object</code></td>\n            <td> An object that contains the maximum limit amount details.<br><br>\n                Learn more about the <code>max_limit_amount</code> child object.</td>\n        </tr>\n        <tr>\n            <td>trial_period_in_days</td>\n            <td><code>integer</code></td>\n            <td>When a trial period is offered for the plan, this defines the duration of the trial period.<br><br>Example: <code>1</code> <br><br><strong>Note:</strong> The trial period is always measured in days.</td>\n        </tr>\n        <tr>\n            <td>start_date</td>\n            <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp is the date when the subscription plan is active and available for use.<br><br>Example: <code>2022-02-01T17:32:28Z</code></td>\n        </tr>\n        <tr>\n            <td>end_date</td>\n            <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp is the date when the subscription plan expires and can no longer be used for new subscriptions.<br><br>Example: <code>2022-09-21T17:32:28Z</code></td>\n        </tr>\n          <tr>\n            <td>merchant_metadata</td>\n            <td><code>object</code></td>\n            <td> An object of key-value pair that can be used to store additional information.<br><br>\n                <ul>\n                    <li>Each pair cannot exceed <code>256</code> characters.</li>\n                    <li>Maximum <code>10</code> key-value pairs.</li>\n                </ul>\n                Example: <code>\"key1\": \"DD\"</code></td>\n        </tr>\n        <tr>\n            <td>merchant_plan_reference</td>\n            <td><code>string</code></td>\n            <td>Unique identifier of the merchant plan reference entered while creating a plan.<br><br> <ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</li></ul>Example: <code>1234567890</code></td>\n        </tr>\n        <tr>\n            <td>created_at</td>\n            <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp, when the create plan request was received by Plural.<br><br>Example: <code>2022-09-21T17:32:28Z</code></td>\n        </tr>\n        <tr>\n            <td>modified_at</td>\n            <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp, when the plan object is updated.<br><br>\n                Example: <code>2022-09-21T17:32:28Z</code></td>\n        </tr>\n    </tbody>\n</table>\n<h3>Amount [Child Object]</h3>\n        <p> The table below lists the various parameters in the <code>amount</code> child object. This object is part of the <code>create plan</code> response object.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value</td>\n                <td><code>integer</code></td>\n                <td>Transaction amount in Paisa.<br><br><ul><li>\n                  Minimum value: <code>100</code> (₹1).</li><li>\n                  Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>\n          Example: <code>1000</code></td>\n            </tr>\n            <tr>\n                <td>currency</td>\n                <td><code>string</code></td>\n                <td> Type of currency.<br><br> Example: <code>INR</code></td>\n            </tr>\n        </tbody>\n    </table>\n\t\t<h3>Max limit amount [Child Object]</h3>\n\t\t<p>The table below lists the various parameters in the <code>max_limit_amount</code> child object. This object is part of the <code>create plan</code> response object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>value</td>\n          <td><code>integer</code></td>\n          <td>The transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1).</li><li>Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>Example: <code>100</td>\n        </tr>\n        <tr>\n            <td>currency</td>\n          <td><code>string</code></td>\n          <td>Type of currency.<br><br> Example: <code>INR</code></td>\n        </tr>\n    </table>\n    <h2>Bank Account [Child Object]</h2>\n        <p> The table below lists the various parameters in the <code>bank_account</code> child object. This object is part of the <code>Create subscription</code> request object.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>account_number</td>\n                <td><code>string</code></td>\n                <td>Customer's bank account number.<ul><li>Minimum length: 1 characters</li><li>Maximum length: 50 characters.</ul></li>Example: <code>04992990009595</code></td>\n</tr>\n<tr>\n<td>name</td>\n<td><code>string</code></td>\n<td>Name of Customer.<br><br>Example: <code>Kevin Bob</code></td>\n</tr>\n<tr>\n<td>ifsc</td>\n<td><code>string</code></td>\n<td>IFSC code of the bank account.<ul><li>Minimum: 11 characters</li><li>Maximum: 11 characters</ul></li>Example: <code>HDFC0001234</code></li><br><br>Supported Characters:<ul><li>A-Z (Uppercase letters)</li><li>0-9 (Digits)</li></ul></td>\n</tr>  \n</table>\n   </div>\n</body>\n</html>\n           "
}
[/block]


</details>

## 4. Create Payment

To create a payment, use our Create Payment API, use the `order_id` returned in the response of a Create Subscription API to link the payment against an order.

Below are the sample requests and sample response for a Create Payment API via Intent Flow.

```curl cURL - UAT
curl --location 'https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/payments' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
--header 'Content-Type: application/json' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'accept: application/json' \
--data '
{
  "payments": [
    {
      "payment_method": "UPI",
      "merchant_payment_reference": "108cf506-c6a1-4535-9e7f-3af9c6d3d90c",
      "payment_amount": {
        "value": 100,
        "currency": "INR"
      },
      "payment_option": {
        "upi_details": {
          "txn_mode": "INTENT"
        }
      },
      "mandate_info": {
        "subscription_id": "v1-sub-250225165137-aa-Ukzs80",
        "request_type": "CREATE_MANDATE"
      }
    }
  ]
}
'
```
```curl cURL - PROD
curl --location 'https://api.pluralpay.in/api/pay/v1/orders/{order_id}/payments' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
--header 'Content-Type: application/json' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'accept: application/json' \
--data '
{
  "payments": [
    {
      "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
      "payment_method": "UPI",
      "payment_amount": {
        "value": 1100,
        "currency": "INR"
      },
      "payment_option": {
        "upi_details": {
          "txn_mode": "INTENT"
        }
      }
    }
  ]
}
'
```
```json Sample Response
{
  "data": {
    "order_id": "v1-240820090251-aa-xwuI7J",
    "merchant_order_reference": "8200c7f7-4490-4970-b6bb-40ffa05d47e5",
    "type": "CHARGE",
    "status": "PENDING",
    "challenge_url": "upi://pay?mode=04&pa=pinelabs.24092@hdfcbank&pn=Pine%20Test&mc=6012&cu=INR&am=1.00&tr=68706&tn=Payment%20for%20v1",
    "merchant_id": "110047",
    "order_amount": {
      "value": 100,
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
    "callback_url": "https://sample-callback-url",
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
    },
    "payments": [
      {
        "id": "v1-240820090251-aa-xwuI7J-up-6",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PENDING",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "UPI",
        "payment_option": {
          "upi_details": {
            "txn_mode": "INTENT"
          }
        },
        "acquirer_data": {
          "approval_code": "",
          "acquirer_reference": "",
          "rrn": "",
          "is_aggregator": true
        },
        "created_at": "2024-08-20T09:02:51.265Z",
        "updated_at": "2024-08-20T09:03:01.208Z"
      }
    ],
    "created_at": "2024-08-20T09:02:51.265Z",
    "updated_at": "2024-08-20T09:03:01.208Z"
  }
}
```

<details><summary>Click here for request and response parameter information.</summary>

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid #5A0083;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n    </style>\n</head>\n<body>\n    <div class=\"tab-container\">\n        <div class=\"tab active\" data-target=\"tab7\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Request Parameters</div>\n\n        <div class=\"tab\" data-target=\"tab8\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Response Parameters</div>\n\n    <div id=\"tab7\" class=\"tab-content active\">\n\n      <body>\n    \n     <h2>Path Parameters</h2>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>order_id<sup>*</sup></td>\n            <td><code>string</code></td>\n            <td>Unique identifier of the order in the Plural database.<br><br>Example: <code>v1-5757575757-aa-hU1rUd</code></td>\n        </tr>\n    </table>\n\n    <h2>Request Parameters</h2>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>Payments</td>\n            <td><code>array of objects</code></td>\n            <td>An array of objects that contains the payment details.<br><br>Learn more about our <code>payments</code> array of objects.</td>\n        </tr>\n    </table>\n\n    <h3>Payments [Child Object]</h3>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>payment_method<sup>*</sup></td>\n            <td><code>string</code></td>\n            <td>Type of payment method. Accepted value: <code>UPI</code><br>Example: <code>UPI</code></td>\n        </tr>\n        <tr>\n            <td>merchant_payment_reference<sup>*</sup></td>\n            <td><code>string</code></td>\n            <td>Unique Payment Reference ID sent by the merchant.<br>Example: <code>008cf04b-a770-4777-854e-b1e6c1230609</code></td>\n        </tr>\n        <tr>\n            <td>payment_amount<sup>*</sup></td>\n            <td><code>object</code></td>\n            <td>An object that contains the details of the <code>payment amount<code>.<br><br>Learn more about <code>payment_amount</code> child object.</td>\n        </tr>\n        <tr>\n            <td>payment_option<sup>*</sup></td>\n            <td><code>object</code></td>\n          <td>An object that contains the details of the <code>payment options</code>.<br><br> Learn more about the <code>payment_option</code> child object.</td>\n        </tr>\n        <tr>\n            <td>mandate_info<sup>*</sup></td>\n            <td><code>object</code></td>\n            <td>An object that contains mandate info details.</td>\n        </tr>\n    </table>\n\n    <h3>Payment Amount [Child Object]</h3>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>value<sup>*</sup></td>\n            <td><code>integer</code></td>\n            <td>The transaction amount is in Paisa.<br>Minimum value: <code>100</code> (₹1).<br>Maximum value: <code>100000000</code> (₹10 lakh).<br>Example: <code>100</code></td>\n        </tr>\n        <tr>\n            <td>currency<sup>*</sup></td>\n            <td><code>string</code></td>\n            <td>Type of currency.<br>Example: <code>INR</code></td>\n        </tr>\n    </table>\n\n    <h3>Payment Option [Child Object]</h3>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>upi_details<sup>*</sup></td>\n            <td><code>object</code></td>\n            <td>An object that contains the UPI details.</td>\n        </tr>\n    </table>\n\n    <h4>UPI Details [Child Object]</h4>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>txn_mode<sup>*</sup></td>\n            <td><code>string</code></td>\n            <td>The transaction mode in which you want to accept payment.<br>Accepted value: <code>INTENT</code></td>\n        </tr>\n    </table>\n\n    <h3>Mandate Info [Child Object]</h3>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>subscription_id<sup>*</sup></td>\n            <td><code>integer</code></td>\n            <td>Unique identifier for the subscription plan.<br>Maximum length: 50 characters.<br>Example: <code>v1-plan-4405071524-aa-qlAtAf</code></td>\n        </tr>\n        <tr>\n            <td>request_type<sup>*</sup></td>\n            <td><code>string</code></td>\n            <td>The type of action to be performed on a mandate.<br>Accepted values: <ul><li>Creation</li><li>Execution</li><li>Notification</li><li>Update</li></ul></td>\n        </tr>\n    </table>\n\n</body>\n            \n    </div>\n\n    <div id=\"tab8\" class=\" tab-content\">\n      \n      \n        <body>\n    <h2>Response Object</h2>\n          <p>The table below lists the various parameters returned in the Create Payment API response objects.</p>\n    <table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>order_id</td>\n      <td><code>string</code></td>\n      <td>Unique identifier of the order in the Plural database.<br><br>Example: <code>v1-5757575757-aa-hU1rUd</code></td>\n    </tr>\n    <tr>\n      <td>merchant_order_reference</td>\n      <td><code>string</code></td>\n      <td>Unique identifier entered while creating an order.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</li></ul>Example: <code>82d57572-057c-4826-5775-385a52150554</code></td>\n    </tr>\n    <tr>\n      <td>type</td>\n      <td><code>string</code></td>\n      <td>Payment type.<br><br>Possible values:<ul><li><code>CHARGE</code></li><li><code>REFUND</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>status</td>\n      <td><code>string</code></td>\n      <td>Order status.<br><br>Possible values:<ul><li><code>CREATED</code>: When the order is successfully created.</li><li><code>PENDING</code>: When the order is linked against a payment request.</li><li><code>PROCESSED</code>: When the payment is received successfully.</li><li><code>AUTHORIZED</code>: <strong>Only when <code>pre_auth</code> is <code>true</code></strong>. When the payment is ready for authorization.</li><li><code>CANCELLED</code>: When the payment gets cancelled.</li><li><code>ATTEMPTED</code>: When the payment is unsuccessful due to incorrect OTP. You can retry OTP verification until the payment gets failed.</li><li><code>FAILED</code>: Payment acceptance failed for reasons such as cancel transactions, maximum retries for OTP verification etc.</li><li><code>FULLY_REFUNDED</code>: When the payment is completely refunded.</li><li><code>PARTIALLY_REFUNDED</code>: When the partial refund is successful.</li></ul></td>\n    </tr>\n    <tr>\n      <td>challenge_url</td>\n      <td><code>string</code></td>\n      <td>Use the generated <code>challenge_url</code> URL to navigate your users to the checkout page.</td>\n    </tr>\n    <tr>\n      <td>merchant_id</td>\n      <td><code>string</code></td>\n      <td>Unique identifier of the merchant in Plural database.<br><br>Example: <code>123456</code></td>\n    </tr>\n    <tr>\n      <td>order_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the transaction amount details.<br><br>Learn more about our <code>order_amount</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>pre_auth</td>\n      <td><code>boolean</code></td>\n      <td>The pre-authorization type.<br><br>Possible values:<ul><li><code>true</code>: When pre-authorization is needed.</li><li><code>false</code>: When pre-authorization is not required.</li></ul>Example: <code>false</code><br><br>Learn more about our pre-authorization.</a></td>\n    </tr>\n    <tr>\n      <td>allowed_payment_methods</td>\n      <td><code>array of strings</code></td>\n      <td>The type of payment methods you want to offer your customers to accept payments.<br><br>Accepted values:<ul><li><code>CARD</code></li><li><code>UPI</code></li><li><code>POINTS</code></li><li><code>NETBANKING</code></li><li><code>WALLET</code></li><li><code>CREDIT_EMI</code></li><li><code>DEBIT_EMI</code></li></ul>Example: <code>UPI</code><br><br><strong>Note</strong>: Before selecting a payment method, ensure it is configured for you.</td>\n    </tr>\n    <tr>\n      <td>notes</td>\n      <td><code>string</code></td>\n      <td>The note you want to show against an order.<br><br>Example: <code>Order1</code></td>\n    </tr>\n    <tr>\n      <td>callback_url</td>\n      <td><code>string</code></td>\n      <td>Use this URL to redirect your customers to specific success or failure pages based on the order or product details.<br><br>Example: <code>https://sample-callback-url</code></td>\n    </tr>\n    <tr>\n      <td>purchase_details</td>\n      <td><code>object</code></td>\n      <td>An object that contains the purchase details.<br><br>Learn more about our <code>purchase_details</code> child object</a>.<br><br><strong>Note</strong>: The presence of the key-values pairs in this object depends on the Input request.</td>\n    </tr>\n    <tr>\n      <td>payments</td>\n      <td><code>array of objects</code></td>\n      <td>An array of objects that contains the payment details.<br><br>Learn more about our <code>payments</code> child object</a>.<br><br><strong>Note</strong>: Payments response object can vary based on the payment methods and payment status.</td>\n    </tr>\n    <tr>\n      <td>created_at</td>\n      <td><code>string</code></td>\n      <td>The ISO 8601 UTC Timestamp, when the create order request was received by Plural.<br><br>Example: <code>2024-07-09T07:57:08.022Z</code></td>\n    </tr>\n    <tr>\n      <td>updated_at</td>\n      <td><code>string</code></td>\n      <td>The ISO 8601 UTC Timestamp, when the order response object is updated.<br><br>Example: <code>2024-07-09T07:57:08.022Z</code></td>\n    </tr>\n  </tbody>\n</table>\n</body>\n<h2>Order Amount [Child Object]</h2>\n<p>The table below lists the various parameters in the <code>order_amount</code> child object. This object is part of the payments sample response object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>The transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>100</code></td>\n    </tr>\n    <tr>\n      <td>currency</td>\n      <td><code>string</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n  </tbody>\n</table>\n<h2>Purchase Details [Child Object]</h2>\n<p>The table below lists the various parameters in the <code>purchase_details</code> child object. This object is part of the payments sample response object.</p>\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>customer</td>\n      <td><code>Object</code></td>\n      <td>An object that contains the customer details.<br><br>Learn more about our <code>customer</code> child object</a>.</td>\n    </tr>\n    <tr>\n      <td>merchant_metadata</td>\n      <td><code>object</code></td>\n      <td>An object of key-value pair that can be used to store additional information.<br><br>Example: <code>\"key1\": \"DD\"</code></td>\n    </tr>\n  </tbody>\n</table>  \n    <h4>Customer [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>customer</code> child object. This is part of the <code>purchase_details</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>email_id</td>\n          <td><code>string</code></td>\n          <td>Customer's email address.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>kevin.bob@example.com</code></td>\n        </tr>\n        <tr>\n            <td>first_name</td>\n          <td><code>string</code></td>\n          <td>Customer's first name.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>Kevin</code></td>\n        </tr>\n        <tr>\n            <td>last_name</td>\n          <td><code>string</code></td>\n          <td>Customer's last name.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>Bob</code></td>\n    </tr>\n        <tr>\n            <td>customer_id</td>\n          <td><code>string</code></td>\n            <td>Unique identifier of the customer in the Plural database.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>19</code> characters.</ul></li>Example: <code>123456</code></td>\n        </tr>\n        <tr>\n            <td>mobile_number</td>\n          <td><code>string</code></td>\n          <td>Customer's mobile number.<ul><li>Minimum length: <code>9</code> characters.</li><li>Maximum length: <code>20</code> characters.</ul></li>Example: <code>9876543210</code></td>\n        </tr>\n        <tr>\n            <td>billing_address</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the billing address.<br><br>Learn more about our <code>billing_address</code> child object.</td>\n        </tr>\n        <tr>\n            <td>shipping_address</td>\n          <td><code>object</code></td>\n            <td>An object that contains the shipping address details.<br><br>Learn more about our <code>shipping_address</code> child object.</td>\n        </tr>\n    </table>\n<h5>Billing Address [Child Object]</h5>\n  <p>The table below lists the various parameters in the <code>billing_address</code> child object. This is part of the <code>customer</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr><td>address1</td><td><code>string</code></td><td>Customer's billing address1.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>10 Downing Street Westminster London</code></td></tr>\n        <tr><td>address2</td><td><code>string</code></td><td>Customer's billing address2.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Oxford Street Westminster London</code></td></tr>\n        <tr><td>address3</td><td><code>string</code></td><td>Customer's billing address3.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Baker Street Westminster London</code></td></tr>\n        <tr><td>pincode</td><td><code>string</code></td><td>Pincode of the billing address.<ul><li>Min length: <code>6</code> characters.</li><li>Max length: <code>10</code> characters.</ul></li>Example: <code>51524036</code></td></tr>\n        <tr><td>city</td><td><code>string</code></td><td>City of the billing address. <ul><li>Max length: <code>50</code> characters. </ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>state</td><td><code>string</code></td><td>State of the billing address. <ul><li>Max length: <code>50<code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>country</td><td><code>string</code></td><td>Country of the billing address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>London</code></td></tr>\n    </table>\n\n    <h5>Shipping Address [Child Object]</h5>\n  <p>The table below lists the various parameters in the <code>shipping_address</code> child object. This is part of the <code>customer</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr><td>address1</td><td><code>string</code></td><td>Customer's shipping address1.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>10 Downing Street Westminster London</code></td></tr>\n        <tr><td>address2</td><td><code>string</code></td><td>Customer's shipping address2.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Oxford Street Westminster London</code></td></tr>\n        <tr><td>address3</td><td><code>string</code></td><td>Customer's shipping address3.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Baker Street Westminster London</code></td></tr>\n        <tr><td>pincode</td><td><code>string</code></td><td>Pincode of the shipping address.<ul><li>Min length: <code>6</code> characters</li><li>Max length: <code>10</code> characters.</ul></li>Example: <code>51524036</code></td></tr>\n        <tr><td>city</td><td><code>string</code></td><td>City of the shipping address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>state</td><td><code>string</code></td><td>State of the shipping address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>country</td><td><code>string</code></td><td>Country of the shipping address. <ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>London</code></td></tr>\n    </table>\n<h2>Payments [Child Object]</h2>\n<p>The table below lists the various parameters in the <code>payments</code> child object. This object is part of the <code>payments</code> sample response object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>id</td>\n          <td><code>string</code></td>\n            <td>Unique identifier of the payment in the Plural database.<ul><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>v1-5206071124-aa-mpLhF3-cc-l</code></td>\n        </tr>\n        <tr>\n            <td>merchant_payment_reference</td>\n          <td><code>string</code></td>\n            <td>A unique Payment Reference id sent by merchant.<br><br>Example: <code>008cf04b-a770-4777-854e-b1e6c1230609</code></td>\n        </tr>\n        <tr>\n            <td>status</td>\n          <td><code>string</code></td>\n          <td>Payment status.<br><br>Possible values:<ul></li><code>PENDING</code>: When the create payment API request is successfully received by Plural.</li><li><code>AUTHORIZED</code>: <strong>Only when <code>pre_auth</code> is true</strong>. When the payment is ready for authorization.</li><li><code>CANCELLED</code>: When the payment gets cancelled.</li><li><code>PROCESSED</code>: When the payment is successfully received by Plural.</li><li><code>FAILED</code>: When the payment fails, this can be for many reasons such as canceling payments, etc.</ul></li>Example: <code>PENDING</code></td>\n        </tr>\n        <tr>\n            <td>payment_amount</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the payment amount.<br><br>Learn more about our <code>payment_amount</code> child object.</td>\n        </tr>\n        <tr>\n            <td>payment_method</td>\n          <td><code>string</code></td>\n          <td>Type of payment method.<br><br>Accepted values:<ul><li><code>CARD</code></li><li><code>UPI</code></li><li><code>POINTS</code></ul></li>Example: <code>UPI</code></td>\n        </tr>\n        <tr>\n            <td>payment_option</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the payment options.<br><br>Learn more about our <code>payment_option</code> child object.</td>\n        </tr>\n        <tr>\n            <td>acquirer_data</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the acquirer data.<br><br>Learn more about our <code>acquirer_data</code> child object.</td>\n        </tr>\n        <tr>\n            <td>created_at</td>\n          <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp, when the create payment request was received by Plural.<br><br>Example: <code>2024-07-11T06:52:12.484Z</code></td>\n        </tr>\n        <tr>\n            <td>updated_at</td>\n          <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp, when the payment response object is updated.<br><br>Example: <code>2024-07-11T06:59:38.260Z</code></td>\n        </tr>\n    </table>\n\n<h3>Payment Amount [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>payment_amount</code> child object. This object is part of the <code>payments</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>value</td>\n          <td><code>integer</code></td>\n          <td>The transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1).</li><li>Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>Example: <code>100</code></td>\n        </tr>\n        <tr>\n            <td>currency</td>\n          <td><code>string</code></td>\n          <td>Type of currency.<br><br>Example: <code>INR</code></td>\n        </tr>\n    </table>\n<h3>Payment Option [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>payment_option</code> child object. This object is part of the <code>payments</code> object.</p>\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>upi_details</td>\n      <td><code>object</code></td>\n      <td>An object that contains the UPI details.<br><br>Learn more about our <code>upi_details</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n<h4>UPI Details [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>upi_details</code> child object. This object is part of the <code>payment_option</code> object.</p>\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>txn_mode</td>\n      <td><code>string</code></td>\n      <td>Type of UPI transaction.<br><br>Accepted values:<ul><li><code>COLLECT</code></li><li><code>INTENT</code></li></ul>Example: <code>INTENT</code></td>\n    </tr>\n  </tbody>\n</table>\n<h4>Acquirer Data [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>acquirer_data</code> child object. This object is part of the <code>payments</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>approval_code</td>\n          <td><code>string</code></td>\n            <td>Authorization code returned from acquirer against the payment.<br><br>Example: <code>030376</code></td>\n        </tr>\n        <tr>\n            <td>acquirer_reference</td>\n          <td><code>string</code></td>\n            <td>Unique reference returned from acquirer for the payment.<br><br>Example: <code>202455840588334</code></td>\n        </tr>\n        <tr>\n            <td>rrn</td>\n          <td><code>string</code></td>\n            <td>Retrieval reference number returned from acquirer for the payment.<br><br>Example: <code>419335023601</code></td>\n        </tr>\n        <tr>\n            <td>is_aggregator</td>\n          <td><code>boolean</code></td>\n          <td>The selected aggregator model type.<br><br>Accepted values:<ul><li><code>true</code> - Plural is responsible for settling funds related to this payment.</li><li><code>false</code> - Plural is not responsible for settling funds related to this payment.</ul></li><strong>Note</strong>:<ul><li>When is_aggregator is set to true, Plural acts as the acquirer on behalf of merchants, receiving funds from banks into a designated \"Nodal Account\".</li><li>When is_aggregator is set to false, the Merchant has a direct relationship with the bank, and the responsibility for settlement of funds lies with both of those parties.</ul></li></td>\n        </tr>\n    </table>\n        <tr>\n            <td>created_at</td>\n          <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp, when the amount was captured.<br><br>Example: <code>2024-07-11T11:52:12.484105Z</code></td>\n        </tr>\n<tr>\n            <td>updated_at</td>\n          <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp, when the payment response object is updated.<br><br>Example: <code>2024-07-11T06:59:38.260Z</code></td>\n        </tr>\n    </table>\n</body>    \n    </div>\n</body>\n</html>"
}
[/block]


</details>

Below are the sample requests and sample response for a Create Payment API via Collect Flow.

```curl cURL - UAT
curl --location 'https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/payments' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
--header 'Content-Type: application/json' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'accept: application/json' \
--data '
{
    "payments": [
        {
            "payment_method": "UPI",
            "merchant_payment_reference": "56d3cd91-9bb1-459c-8358-d92ef62d38ee",
            "payment_amount": {
                "value": 100,
                "currency": "INR"
            },
            "payment_option": {
                "upi_details": {
                    "txn_mode": "COLLECT",
                    "payer": {
                        "vpa": "9280850298@oksbi",
                        "phone_number": "9876543210"
                    }
                }
            },
            "mandate_info": {
                "subscription_id": "v1-sub-250225165137-aa-Ukzs80",
                "request_type": "CREATE_MANDATE"
            }
        }
    ]
}
'
```
```curl cURL - PROD
curl --location 'https://api.pluralpay.in/api/pay/v1/orders/{order_id}/payments' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
--header 'Content-Type: application/json' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'accept: application/json' \
--data '
{
  "payments": [
    {
      "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
      "payment_method": "UPI",
      "payment_amount": {
        "value": 100,
        "currency": "INR"
      },
      "payment_option": {
        "upi_details": {
          "txn_mode": "COLLECT",
          "payer": {
            "vpa": "kevin.bob@examplebank.com"
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
  "data": {
    "order_id": "v1-240820090251-aa-xwuI7J",
    "merchant_order_reference": "8200c7f7-4490-4970-b6bb-40ffa05d47e5",
    "type": "CHARGE",
    "status": "PENDING",
    "challenge_url": "upi://pay?mode=04&pa=pinelabs.24092@hdfcbank&pn=Pine%20Test&mc=6012&cu=INR&am=1.00&tr=68706&tn=Payment%20for%20v1",
    "merchant_id": "110047",
    "order_amount": {
      "value": 100,
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
    "callback_url": "https://sample-callback-url",
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
    },
    "payments": [
      {
        "id": "v1-240820090251-aa-xwuI7J-up-6",
        "merchant_payment_reference": "008cf04b-a770-4777-854e-b1e6c1230609",
        "status": "PENDING",
        "payment_amount": {
          "value": 100,
          "currency": "INR"
        },
        "payment_method": "UPI",
        "payment_option": {
          "upi_details": {
            "txn_mode": "COLLECT",
            "payer": {
              "vpa": "kevinbob@example"
            }
          },
          "acquirer_data": {
            "approval_code": "",
            "acquirer_reference": "",
            "rrn": "",
            "is_aggregator": true
          },
          "created_at": "2024-08-20T09:02:51.265Z",
          "updated_at": "2024-08-20T09:03:01.208Z"
        }
      }
    ],
    "created_at": "2024-08-20T09:02:51.265Z",
    "updated_at": "2024-08-20T09:03:01.208Z"
  }
}
```

<details><summary>Click here for request and response parameter information.</summary>

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid #5A0083;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n    </style>\n</head>\n<body>\n    <div class=\"tab-container\">\n        <div class=\"tab active\" data-target=\"tab9\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Request Parameters</div>\n\n        <div class=\"tab\" data-target=\"tab10\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Response Parameters</div>\n\n    <div id=\"tab9\" class=\"tab-content active\">\n\n      <body>\n    \n     <h2>Path Parameters</h2>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>order_id<sup>*</sup></td>\n            <td><code>string</code></td>\n            <td>Unique identifier of the order in the Plural database.<br><br>Example: <code>v1-5757575757-aa-hU1rUd</code></td>\n        </tr>\n    </table>\n\n    <h2>Request Parameters</h2>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>Payments</td>\n            <td><code>array of objects</code></td>\n            <td>An array of objects that contains the payment details.<br><br>Learn more about our <code>payments</code> array of objects.</td>\n        </tr>\n    </table>\n\n    <h3>Payments [Child Object]</h3>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>payment_method<sup>*</sup></td>\n            <td><code>string</code></td>\n            <td>Type of payment method. Accepted value: <code>UPI</code><br>Example: <code>UPI</code></td>\n        </tr>\n        <tr>\n            <td>merchant_payment_reference<sup>*</sup></td>\n            <td><code>string</code></td>\n            <td>Unique Payment Reference ID sent by the merchant.<br>Example: <code>008cf04b-a770-4777-854e-b1e6c1230609</code></td>\n        </tr>\n        <tr>\n            <td>payment_amount<sup>*</sup></td>\n            <td><code>object</code></td>\n            <td>An object that contains the details of the payment amount.</td>\n        </tr>\n        <tr>\n            <td>payment_option<sup>*</sup></td>\n            <td><code>object</code></td>\n            <td>An object that contains the details of the payment options.</td>\n        </tr>\n        <tr>\n            <td>mandate_info<sup>*</sup></td>\n            <td><code>object</code></td>\n            <td>An object that contains mandate info details.</td>\n        </tr>\n    </table>\n\n    <h3>Payment Amount [Child Object]</h3>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>value<sup>*</sup></td>\n            <td><code>integer</code></td>\n            <td>The transaction amount is in Paisa.<br>Minimum value: <code>100</code> (₹1).<br>Maximum value: <code>100000000</code> (₹10 lakh).<br>Example: <code>100</code></td>\n        </tr>\n        <tr>\n            <td>currency<sup>*</sup></td>\n            <td><code>string</code></td>\n            <td>Type of currency.<br>Example: <code>INR</code></td>\n        </tr>\n    </table>\n\n    <h3>Payment Option [Child Object]</h3>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>upi_details<sup>*</sup></td>\n            <td><code>object</code></td>\n            <td>An object that contains the UPI details.</td>\n        </tr>\n    </table>\n\n    <h4>UPI Details [Child Object]</h4>\n    <table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>txn_mode<sup>*</sup></td>\n      <td><code>string</code></td>\n      <td>The transaction mode in which you want to accept payment.<br><br>Accepted value: <code>COLLECT</code></td>\n    </tr>\n    <tr>\n      <td>payer<sup>*</sup></td>\n      <td><code>object</code></td>\n      <td>An object that contains the payer VPA handle details.<br><br>Learn more about our <code>payer</code> array of objects.</td>\n    </tr>\n  </tbody>\n</table>\n        <h5>Payer [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>payer</code> child object. This object is part of the <code>upi_details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>vpa<sup>*</sup></td>\n      <td><code>string</code></td>\n      <td>VPA handle of your customer from whom you want to accept payment.<ul><li>Minimum length: <code>2</code> characters.</li><li>Maximum length: <code>256</code> characters.</li></ul>Example: <code>kevin.bob@examplebank.com</code><br><br>Supported characters:<ul><li><code>A-Z</code></li><li><code>a-z</code></li><li><code>0-9</code></li><li><code>@</code></li><li><code>$</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>phone_number</td>\n      <td><code>string</code></td>\n      <td>Customer's phone number.<br><ul><li>Minimum length: 9 characters.</li><li>Maximum length: 20 characters.</li></ul>Example: <code>9876543210</code><br><br>Supported characters:<ul><li><code>0-9</code></li><li><code>+</code></li></ul></td>\n    </tr>\n  </tbody>\n</table>\n<h3>Mandate Info [Child Object]</h3>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>subscription_id<sup>*</sup></td>\n            <td><code>integer</code></td>\n            <td>Unique identifier for the subscription plan.<br>Maximum length: 50 characters.<br>Example: <code>v1-plan-4405071524-aa-qlAtAf</code></td>\n        </tr>\n        <tr>\n            <td>request_type<sup>*</sup></td>\n            <td><code>string</code></td>\n            <td>The type of action to be performed on a mandate.<br>Accepted values: <ul><li>Creation</li><li>Execution</li><li>Notification</li><li>Update</li></ul></td>\n        </tr>\n    </table>\n\n</body>\n            \n    </div>\n\n    <div id=\"tab10\" class=\" tab-content\">\n      \n      \n        <body>\n    <h2>Response Object</h2>\n          <p>The table below lists the various parameters returned in the Create Payment API response objects.</p>\n    <table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>order_id</td>\n      <td><code>string</code></td>\n      <td>Unique identifier of the order in the Plural database.<br><br>Example: <code>v1-5757575757-aa-hU1rUd</code></td>\n    </tr>\n    <tr>\n      <td>merchant_order_reference</td>\n      <td><code>string</code></td>\n      <td>Unique identifier entered while creating an order.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</li></ul>Example: <code>82d57572-057c-4826-5775-385a52150554</code></td>\n    </tr>\n    <tr>\n      <td>type</td>\n      <td><code>string</code></td>\n      <td>Payment type.<br><br>Possible values:<ul><li><code>CHARGE</code></li><li><code>REFUND</code></li></ul></td>\n    </tr>\n    <tr>\n      <td>status</td>\n      <td><code>string</code></td>\n      <td>Order status.<br><br>Possible values:<ul><li><code>CREATED</code>: When the order is successfully created.</li><li><code>PENDING</code>: When the order is linked against a payment request.</li><li><code>PROCESSED</code>: When the payment is received successfully.</li><li><code>AUTHORIZED</code>: <strong>Only when <code>pre_auth</code> is <code>true</code></strong>. When the payment is ready for authorization.</li><li><code>CANCELLED</code>: When the payment gets cancelled.</li><li><code>ATTEMPTED</code>: When the payment is unsuccessful due to incorrect OTP. You can retry OTP verification until the payment gets failed.</li><li><code>FAILED</code>: Payment acceptance failed for reasons such as cancel transactions, maximum retries for OTP verification etc.</li><li><code>FULLY_REFUNDED</code>: When the payment is completely refunded.</li><li><code>PARTIALLY_REFUNDED</code>: When the partial refund is successful.</li></ul></td>\n    </tr>\n    <tr>\n      <td>challenge_url</td>\n      <td><code>string</code></td>\n      <td>Use the generated <code>challenge_url</code> URL to navigate your users to the checkout page.</td>\n    </tr>\n    <tr>\n      <td>merchant_id</td>\n      <td><code>string</code></td>\n      <td>Unique identifier of the merchant in Plural database.<br><br>Example: <code>123456</code></td>\n    </tr>\n    <tr>\n      <td>order_amount</td>\n      <td><code>object</code></td>\n      <td>An object that contains the transaction amount details.<br><br>Learn more about our <code>order_amount</code> child object.</td>\n    </tr>\n    <tr>\n      <td>pre_auth</td>\n      <td><code>boolean</code></td>\n      <td>The pre-authorization type.<br><br>Possible values:<ul><li><code>true</code>: When pre-authorization is needed.</li><li><code>false</code>: When pre-authorization is not required.</li></ul>Example: <code>false</code><br><br>Learn more about our pre-authorization.</a></td>\n    </tr>\n    <tr>\n      <td>allowed_payment_methods</td>\n      <td><code>array of strings</code></td>\n      <td>The type of payment methods you want to offer your customers to accept payments.<br><br>Accepted values:<ul><li><code>CARD</code></li><li><code>UPI</code></li><li><code>POINTS</code></li><li><code>NETBANKING</code></li><li><code>WALLET</code></li><li><code>CREDIT_EMI</code></li><li><code>DEBIT_EMI</code></li></ul>Example: <code>UPI</code><br><br><strong>Note</strong>: Before selecting a payment method, ensure it is configured for you.</td>\n    </tr>\n    <tr>\n      <td>notes</td>\n      <td><code>string</code></td>\n      <td>The note you want to show against an order.<br><br>Example: <code>Order1</code></td>\n    </tr>\n    <tr>\n      <td>callback_url</td>\n      <td><code>string</code></td>\n      <td>Use this URL to redirect your customers to specific success or failure pages based on the order or product details.<br><br>Example: <code>https://sample-callback-url</code></td>\n    </tr>\n    <tr>\n      <td>purchase_details</td>\n      <td><code>object</code></td>\n      <td>An object that contains the purchase details.<br><br>Learn more about our <code>purchase_details</code> child object.<br><br><strong>Note</strong>: The presence of the key-values pairs in this object depends on the Input request.</td>\n    </tr>\n    <tr>\n      <td>payments</td>\n      <td><code>array of objects</code></td>\n      <td>An array of objects that contains the payment details.<br><br>Learn more about our <code>payments</code> child object.<br><br><strong>Note</strong>: Payments response object can vary based on the payment methods and payment status.</td>\n    </tr>\n    <tr>\n      <td>created_at</td>\n      <td><code>string</code></td>\n      <td>The ISO 8601 UTC Timestamp, when the create order request was received by Plural.<br><br>Example: <code>2024-07-09T07:57:08.022Z</code></td>\n    </tr>\n    <tr>\n      <td>updated_at</td>\n      <td><code>string</code></td>\n      <td>The ISO 8601 UTC Timestamp, when the order response object is updated.<br><br>Example: <code>2024-07-09T07:57:08.022Z</code></td>\n    </tr>\n  </tbody>\n</table>\n</body>\n<h2>Order Amount [Child Object]</h2>\n<p>The table below lists the various parameters in the <code>order_amount</code> child object. This object is part of the payments sample response object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>value</td>\n      <td><code>integer</code></td>\n      <td>The transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1)</li><li>Maximum value: <code>100000000</code> (₹10 lakh)</li></ul>Example: <code>100</code></td>\n    </tr>\n    <tr>\n      <td>currency</td>\n      <td><code>string</code></td>\n      <td>Type of currency.<br><br>Example: <code>INR</code></td>\n    </tr>\n  </tbody>\n</table>\n<h2>Purchase Details [Child Object]</h2>\n<p>The table below lists the various parameters in the <code>purchase_details</code> child object. This object is part of the payments sample response object.</p>\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>customer</td>\n      <td><code>Object</code></td>\n      <td>An object that contains the customer details.<br><br>Learn more about our <code>customer</code> child object.</td>\n    </tr>\n    <tr>\n      <td>merchant_metadata</td>\n      <td><code>object</code></td>\n      <td>An object of key-value pair that can be used to store additional information.<br><br>Example: <code>\"key1\": \"DD\"</code></td>\n    </tr>\n  </tbody>\n</table>  \n    <h4>Customer [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>customer</code> child object. This is part of the <code>purchase_details</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>email_id</td>\n          <td><code>string</code></td>\n          <td>Customer's email address.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>kevin.bob@example.com</code></td>\n        </tr>\n        <tr>\n            <td>first_name</td>\n          <td><code>string</code></td>\n          <td>Customer's first name.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>Kevin</code></td>\n        </tr>\n        <tr>\n            <td>last_name</td>\n          <td><code>string</code></td>\n          <td>Customer's last name.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>Bob</code></td>\n    </tr>\n        <tr>\n            <td>customer_id</td>\n          <td><code>string</code></td>\n            <td>Unique identifier of the customer in the Plural database.<ul><li>Minimum length: <code>1</code> character.</li><li>Maximum length: <code>19</code> characters.</ul></li>Example: <code>123456</code></td>\n        </tr>\n        <tr>\n            <td>mobile_number</td>\n          <td><code>string</code></td>\n          <td>Customer's mobile number.<ul><li>Minimum length: <code>9</code> characters.</li><li>Maximum length: <code>20</code> characters.</ul></li>Example: <code>9876543210</code></td>\n        </tr>\n        <tr>\n            <td>billing_address</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the billing address.<br><br>Learn more about our <code>billing_address</code> child object.</td>\n        </tr>\n        <tr>\n            <td>shipping_address</td>\n          <td><code>object</code></td>\n            <td>An object that contains the shipping address details.<br><br>Learn more about our <code>shipping_address</code> child object.</td>\n        </tr>\n    </table>\n<h5>Billing Address [Child Object]</h5>\n  <p>The table below lists the various parameters in the <code>billing_address</code> child object. This is part of the <code>customer</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr><td>address1</td><td><code>string</code></td><td>Customer's billing address1.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>10 Downing Street Westminster London</code></td></tr>\n        <tr><td>address2</td><td><code>string</code></td><td>Customer's billing address2.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Oxford Street Westminster London</code></td></tr>\n        <tr><td>address3</td><td><code>string</code></td><td>Customer's billing address3.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Baker Street Westminster London</code></td></tr>\n        <tr><td>pincode</td><td><code>string</code></td><td>Pincode of the billing address.<ul><li>Min length: <code>6</code> characters.</li><li>Max length: <code>10</code> characters.</ul></li>Example: <code>51524036</code></td></tr>\n        <tr><td>city</td><td><code>string</code></td><td>City of the billing address. <ul><li>Max length: <code>50</code> characters. </ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>state</td><td><code>string</code></td><td>State of the billing address. <ul><li>Max length: <code>50<code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>country</td><td><code>string</code></td><td>Country of the billing address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>London</code></td></tr>\n    </table>\n\n    <h5>Shipping Address [Child Object]</h5>\n  <p>The table below lists the various parameters in the <code>shipping_address</code> child object. This is part of the <code>customer</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr><td>address1</td><td><code>string</code></td><td>Customer's shipping address1.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>10 Downing Street Westminster London</code></td></tr>\n        <tr><td>address2</td><td><code>string</code></td><td>Customer's shipping address2.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Oxford Street Westminster London</code></td></tr>\n        <tr><td>address3</td><td><code>string</code></td><td>Customer's shipping address3.<ul><li>Max length: <code>100</code> characters.</ul></li>Example: <code>Baker Street Westminster London</code></td></tr>\n        <tr><td>pincode</td><td><code>string</code></td><td>Pincode of the shipping address.<ul><li>Min length: <code>6</code> characters</li><li>Max length: <code>10</code> characters.</ul></li>Example: <code>51524036</code></td></tr>\n        <tr><td>city</td><td><code>string</code></td><td>City of the shipping address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>state</td><td><code>string</code></td><td>State of the shipping address.<ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>Westminster</code></td></tr>\n        <tr><td>country</td><td><code>string</code></td><td>Country of the shipping address. <ul><li>Max length: <code>50</code> characters.</ul></li>Example: <code>London</code></td></tr>\n    </table>\n<h2>Payments [Child Object]</h2>\n<p>The table below lists the various parameters in the <code>payments</code> child object. This object is part of the <code>payments</code> sample response object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>id</td>\n          <td><code>string</code></td>\n            <td>Unique identifier of the payment in the Plural database.<ul><li>Maximum length: <code>50</code> characters.</ul></li>Example: <code>v1-5206071124-aa-mpLhF3-cc-l</code></td>\n        </tr>\n        <tr>\n            <td>merchant_payment_reference</td>\n          <td><code>string</code></td>\n            <td>A unique Payment Reference id sent by merchant.<br><br>Example: <code>008cf04b-a770-4777-854e-b1e6c1230609</code></td>\n        </tr>\n        <tr>\n            <td>status</td>\n          <td><code>string</code></td>\n          <td>Payment status.<br><br>Possible values:<ul></li><code>PENDING</code>: When the create payment API request is successfully received by Plural.</li><li><code>AUTHORIZED</code>: <strong>Only when <code>pre_auth</code> is true</strong>. When the payment is ready for authorization.</li><li><code>CANCELLED</code>: When the payment gets cancelled.</li><li><code>PROCESSED</code>: When the payment is successfully received by Plural.</li><li><code>FAILED</code>: When the payment fails, this can be for many reasons such as canceling payments, etc.</ul></li>Example: <code>PENDING</code></td>\n        </tr>\n        <tr>\n            <td>payment_amount</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the payment amount.<br><br>Learn more about our <code>payment_amount</code> child object.</td>\n        </tr>\n        <tr>\n            <td>payment_method</td>\n          <td><code>string</code></td>\n          <td>Type of payment method.<br><br>Accepted values:<ul><li><code>CARD</code></li><li><code>UPI</code></li><li><code>POINTS</code></ul></li>Example: <code>UPI</code></td>\n        </tr>\n        <tr>\n            <td>payment_option</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the payment options.<br><br>Learn more about our <code>payment_option</code> child object.</td>\n        </tr>\n        <tr>\n            <td>acquirer_data</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the acquirer data.<br><br>Learn more about our <code>acquirer_data</code> child object.</td>\n        </tr>\n        <tr>\n            <td>error_detail</td>\n          <td><code>object</code></td>\n            <td>An object that contains the error details.<br><br>Learn more about our <code>error_detail</code> child object.<br><br><strong>Note</strong>: This object is returned only for failed payments.</td>\n        </tr>\n        <tr>\n            <td>capture_data</td>\n          <td><code>object</code></td>\n            <td>An object that contains the details of the capture data.<br><br>Learn more about our <code>capture_data</code> child object.<br><br><strong>Note</strong>: The presence of the key-value pairs against this object depends on the pre-authorization type.</td>\n        </tr>\n        <tr>\n            <td>created_at</td>\n          <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp, when the create payment request was received by Plural.<br><br>Example: <code>2024-07-11T06:52:12.484Z</code></td>\n        </tr>\n        <tr>\n            <td>updated_at</td>\n          <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp, when the payment response object is updated.<br><br>Example: <code>2024-07-11T06:59:38.260Z</code></td>\n        </tr>\n    </table>\n\n<h3>Payment Amount [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>payment_amount</code> child object. This object is part of the <code>payments</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>value</td>\n          <td><code>integer</code></td>\n          <td>The transaction amount is Paisa.<ul><li>Minimum value: <code>100</code> (₹1).</li><li>Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>Example: <code>100</code></td>\n        </tr>\n        <tr>\n            <td>currency</td>\n          <td><code>string</code></td>\n          <td>Type of currency.<br><br>Example: <code>INR</code></td>\n        </tr>\n    </table>\n<h3>Payment Option [Child Object]</h3>\n<p>The table below lists the various parameters in the <code>payment_option</code> child object. This object is part of the <code>payments</code> object.</p>\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>upi_details</td>\n      <td><code>object</code></td>\n      <td>An object that contains the UPI details.<br><br>Learn more about our <code>upi_details</code> child object</a>.</td>\n    </tr>\n  </tbody>\n</table>\n<h4>UPI Details [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>upi_details</code> child object. This object is part of the <code>payment_option</code> object.</p>\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>txn_mode</td>\n      <td><code>string</code></td>\n      <td>Type of UPI transaction.<br><br>Accepted values:<ul><li><code>COLLECT</code></li><li><code>INTENT</code></li></ul>Example: <code>COLLECT</code></td>\n    </tr>\n    <tr>\n      <td>payer</td>\n      <td><code>object</code></td>\n      <td>An object that contains the payer details.<br><br>Learn more about our <code>payer</code> child object</a>.<br><br><strong>Note</strong>: Mandatory for UPI collect only.</td>\n    </tr>\n  </tbody>\n</table>\n<h4>Payer [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>payer</code> child object. This object is part of the <code>upi_details</code> object.</p>\n\n<table>\n  <thead>\n    <tr>\n      <th>Parameter</th>\n      <th>Type</th>\n      <th>Description</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>vpa</td>\n      <td><code>string</code></td>\n      <td>VPA handle of your customer from whom you want to accept payment.<ul><li>Minimum length: 2 characters.</li><li>Maximum length: 256 characters.</li></ul>Example: <code>kevinbob@example</code><br><br>Supported characters:<ul><li><code>A-Z</code></li><li><code>a-z</code></li><li><code>0-9</code></li><li><code>@</code></li><li><code>$</code></li></ul></td>\n    </tr>\n  </tbody>\n</table>\n  </tbody>\n</table>\n<h4>Acquirer Data [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>acquirer_data</code> child object. This object is part of the <code>payments</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>approval_code</td>\n          <td><code>string</code></td>\n            <td>Authorization code returned from acquirer against the payment.<br><br>Example: <code>030376</code></td>\n        </tr>\n        <tr>\n            <td>acquirer_reference</td>\n          <td><code>string</code></td>\n            <td>Unique reference returned from acquirer for the payment.<br><br>Example: <code>202455840588334</code></td>\n        </tr>\n        <tr>\n            <td>rrn</td>\n          <td><code>string</code></td>\n            <td>Retrieval reference number returned from acquirer for the payment.<br><br>Example: <code>419335023601</code></td>\n        </tr>\n        <tr>\n            <td>is_aggregator</td>\n          <td><code>boolean</code></td>\n          <td>The selected aggregator model type.<br><br>Accepted values:<ul><li><code>true</code> - Plural is responsible for settling funds related to this payment.</li><li><code>false</code> - Plural is not responsible for settling funds related to this payment.</ul></li><strong>Note</strong>:<ul><li>When is_aggregator is set to true, Plural acts as the acquirer on behalf of merchants, receiving funds from banks into a designated \"Nodal Account\".</li><li>When is_aggregator is set to false, the Merchant has a direct relationship with the bank, and the responsibility for settlement of funds lies with both of those parties.</ul></li></td>\n        </tr>\n    </table>\n\n<h4>Error Detail [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>error_detail</code> child object. This object is part of the <code>payments</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>code</td>\n          <td><code>string</code></td>\n          <td>The error short code.<br><br><r>Example: <code>PAYMENT_DECLINED</code></td>\n        </tr>\n        <tr>\n            <td>message</td>\n          <td><code>string</code></td>\n            <td>Error description explaining why the error occurred.<br><br>Example: <code>Transaction declined due to insufficient balance</code>.</td>\n        </tr>\n    </table>\n\n    <h4>Capture Data [Child Object]</h4>\n<p>The table below lists the various parameters in the <code>capture_data</code> child object. This object is part of the <code>payments</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>merchant_capture_reference</td>\n          <td><code>string</code></td>\n            <td>Unique identifier passed while creating the capture payment request.<br><br>Example: <code>5742ef1e-4606-4c11-5757-705f4d415b6d</code></td>\n        </tr>\n        <tr>\n            <td>capture_amount</td>\n          <td><code>object</code></td>\n            <td>An object that contains the capture amount details.<br><br>Learn more about our <code>capture_amount</code> child object.</td>\n        </tr>\n        <tr>\n            <td>created_at</td>\n          <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp, when the amount was captured.<br><br>Example: <code>2024-07-11T11:52:12.484105Z</code></td>\n        </tr>\n    </table>\n\n    <h5>Capture Amount [Child Object]</h5>\n<p>The table below lists the various parameters in the <code>capture_amount</code> child object. This object is part of the <code>capture_data</code> object.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>value</td>\n          <td><code>integer</code></td>\n          <td>The transaction amount is in Paisa.<ul><li>Minimum value: <code>100</code> (₹1). </li><li>Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>Example: <code>100</code></td>\n        </tr>\n        <tr>\n            <td>currency</td>\n          <td><code>string</code></td>\n          <td>Type of currency.<br><br>Example: <code>INR</code></td>\n        </tr>\n    </table>\n</body>    \n    </div>\n</body>\n</html>"
}
[/block]


</details>

## 5. Handle Payment

In create payment API response we return a `challenge_url`, use this challenge url to navigate your customers to the checkout page to accept payment.

> 📘 Note:
> 
> - On successful payment we send the webhook event `ORDER_AUTHORIZED` and the status of the payment is updated to `authorized`.
> - You can capture or cancel an order only when the order status is `authorized`.

### 5.1 Store Payment Details on Your Server

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

### 5.2 Verify Payment Signature

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

**NOTE:**If the Auto Debit payment is disabled, follow the steps to create a scheduled payment manually.

## Schedule Recurring Payment

### Create Presentation

To Create Presentation, use our Create Presentation API, use the `subscription_id` returned in the response of a Create subscription API to link the payment against a subscription.

For authentication use the generated access token in the headers of the API request.

Below are the sample requests and response for the Create Presentation API.

```curl cURL – UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/v1/public/subscriptions/subscription_id/presentations \
     --header 'Authorization: Bearer https://pluraluat.v2.pinepg.in/api/v1/public/plans' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "due_date": "2022-09-21T17:32:28Z",
  "amount": {
    "value": 100,
    "currency": "INR"
  },
  "merchant_presentation_reference": "1234567890",
  "customer_id": "123456",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  }
}
'
```
```curl cURL – PROD
curl --request POST \
     --url https://api.pluralpay.in/api/v1/public/subscriptions/subscription_id/presentations \
     --header 'Authorization: Bearer https://pluraluat.v2.pinepg.in/api/v1/public/plans' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "due_date": "2022-09-21T17:32:28Z",
  "amount": {
    "value": 100,
    "currency": "INR"
  },
  "merchant_presentation_reference": "1234567890",
  "customer_id": "123456",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  }
}
'
```
```json Sample Response
{
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "presentation_id": "v1-pre-4405071524-aa-qlAtAf",
  "due_date": "2022-09-21T17:32:28Z",
  "amount": {
    "value": 100,
    "currency": "INR"
  },
  "merchant_presentation_reference": "1234567890",
  "customer_id": "123456",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  }
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/create-presentation" target="_blank">Create Presentation API</a> documentation to learn more.

<details><summary>Click here for request and response parameter information.</summary>

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid #5A0083;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n    </style>\n</head>\n<body>\n    <div class=\"tab-container\">\n        <div class=\"tab active\" data-target=\"tab11\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Request Parameters</div>\n\n        <div class=\"tab\" data-target=\"tab12\" onclick=\"\n            var parent = this.closest('.tab-container');\n            parent.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));\n            parent.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));\n            this.classList.add('active');\n            parent.querySelector('#' + this.getAttribute('data-target')).classList.add('active');\n        \">Response Parameters</div>\n\n    <div id=\"tab11\" class=\"tab-content active\">\n      \n      \n      <body>\n    <p>The table below lists the request parameters of our Create Presentation API.</p>\n    <table>\n        <thead>\n            <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n    </thead>\n    <tbody>\n        <tr>\n            <td>subscription_id</td>\n            <td><code>string</code></td>\n            <td>Unique identifier for the subscription plan in the plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: <code>v1-sub-4405071524-aa-qlAtAf</code>\n            </td>\n        </tr>\n        <tr>\n            <td>due_date</td>\n            <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp is the date & time at which the payment is due.<br><br>\n                Example: <code>2022-09-21T17:32:28Z</code>\n            </td>\n        </tr>\n        <tr>\n            <td>amount</td>\n            <td><code>object</code></td>\n            <td>An object that contains the amount details.<br><br>Learn more about the <code>amount</code> child object.\n                </a>\n            </td>\n        </tr>\n  <tr>\n            <td>merchant_presentation_reference</td>\n            <td><code>string</code></td>\n             <td>Unique identifier of the merchant presentation reference entered while creating a presentation.<br><br> Constraints:<ul> <li>Minimum: 1 character.</li><li>Maximum: 50 characters.</li>\n                </ul>\n                Example: <code>1234567890</code><br><br>\n                Supported characters:<ul>\n                    <li><code>A-Z</code></li>\n                    <li><code>a-z</code></li>\n                    <li><code>0-9</code></li>\n                    <li><code>-</code></li>\n                    <li><code>_</code></li>\n                </ul>\n            </td>\n        </tr>\n  <tr>\n    <td>customer_id</td>\n    <td><code>string</code></td>\n    <td>Unique identifier of the customer in the Plural database.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 19 characters.</ul></li>Example: <code>123456</code>\n</td>\n</tr>\n  <tr>\n            <td>merchant_metadata</td>\n            <td><code>object</code></td>\n            <td>An object of key-value pairs that can be used to store additional information.<br><br>\n                Constraints:<ul>\n                    <li>Each pair cannot exceed <code>256</code> characters.</li>\n                    <li>Maximum <code>10</code> key-value pairs.</li>\n                </ul>\n                Example: <code>\"key1\": \"DD\"</code>\n            </td>\n        </tr>\n    </tbody>\n</table>\n    <h2>Amount [Child Object]</h2>\n        <p> The table below lists the various parameters in the <code>amount</code> child object. This object is part of the <code>Create Presentation</code> request object.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value*</td>\n                <td><code>integer</code></td>\n                <td>\n                    Transaction amount in Paisa.<br><br><ul><li>\n                  Minimum value: <code>100</code> (₹1).</li><li>\n                  Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>\n          Example: <code>1000</code>\n                </td>\n            </tr>\n            <tr>\n                <td>currency*</td>\n                <td><code>string</code></td>\n                <td>\n                    Type of currency.<br><br>\n                  Example: <code>INR</code>\n                </td>\n            </tr>\n    </table>\n       \n    </div>\n    <div id=\"tab12\" class=\" tab-content\">\n      \n      \n        <body>\n          <p>The table below lists the various parameters returned in the Create Presentation response objects.</p>\n    <table>\n        <tr>\n            <th>Parameter</th>\n            <th>Type</th>\n            <th>Description</th>\n        </tr>\n        <tr>\n            <td>subscription_id</td>\n            <td><code>string</code></td>\n            <td>Unique identifier for the subscription plan in the plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: <code>v1-sub-4405071524-aa-qlAtAf</code>\n            </td>\n        </tr>\n      <tr>\n        <td>presentation_id</td>\n        <td><code>string</code></td>\n        <td>A Unique identifier for the presentation provided by the Plural.<ul><li>Maximum length: 50 characters.</ul></li>Example: <code>v1-pre-4405071524-aa-qlAtAf</code></td>\n      </tr>\n        <tr>\n            <td>due_date</td>\n            <td><code>string</code></td>\n            <td>The ISO 8601 UTC Timestamp is the date & time at which the payment is due.<br><br>\n                Example: <code>2022-09-21T17:32:28Z</code>\n            </td>\n        </tr>\n        <tr>\n            <td>amount</td>\n            <td><code>object</code></td>\n            <td>An object that contains the amount details.<br><br>Learn more about the <code>amount</code> child object.\n                </a>\n            </td>\n        </tr>\n  <tr>\n            <td>merchant_presentation_reference</td>\n            <td><code>string</code></td>\n            <td> Unique identifier of the merchant presentation reference entered while creating a presentation.<br><br <ul> <li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</li></ul> Example: <code>1234567890</code>\n            </td>\n        </tr>\n  <tr>\n    <td>customer_id</td>\n    <td><code>string</code></td>\n    <td>Unique identifier of the customer in the Plural database.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 19 characters.</ul></li>Example: <code>123456</code>\n</td>\n</tr>\n  <tr>\n            <td>merchant_metadata</td>\n            <td><code>object</code></td>\n            <td>An object of key-value pairs that can be used to store additional information.<br><br>\n                Constraints:<ul>\n                    <li>Each pair cannot exceed <code>256</code> characters.</li>\n                    <li>Maximum <code>10</code> key-value pairs.</li>\n                </ul>\n                Example: <code>\"key1\": \"DD\"</code>\n            </td>\n        </tr>\n    </tbody>\n</table>\n    <h2>Amount [Child Object]</h2>\n        <p> The table below lists the various parameters in the <code>amount</code> child object. This object is part of the <code>Create Presentation</code> response object.</p>\n    <table>\n        <thead>\n            <tr>\n                <th>Parameter</th>\n                <th>Type</th>\n                <th>Description</th>\n            </tr>\n        </thead>\n        <tbody>\n            <tr>\n                <td>value</td>\n                <td><code>integer</code></td>\n                <td>\n                    Transaction amount in Paisa.<br><br><ul><li>\n                  Minimum value: <code>100</code> (₹1).</li><li>\n                  Maximum value: <code>100000000</code> (₹10 lakh).</ul></li>\n          Example: <code>1000</code>\n                </td>\n            </tr>\n            <tr>\n                <td>currency</td>\n                <td><code>string</code></td>\n                <td>\n                    Type of currency.<br><br>\n                  Example: <code>INR</code>\n                </td>\n        </tr>\n    </table>\n   </div>\n</body>\n</html>\n"
}
[/block]


</details>

## To Know Your Payment Status

To check your payment status, you can either rely on Webhook events or use our **Get Orders** APIs for real-time updates.

1. **Webhook Notification**: We send Webhook notifications on the successful payment or any changes to the payments object. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/developer-tools-webhook" target="_blank">Webhooks</a> documentation to learn more.
2. **Manage subscription**: To manage the subscription. Refer to our <a href="https://developer.pluralonline.com/docs/manage-subscription" >target="\_blank">Manage subscription</a> documentation to learn more.
