---
title: "Test_Subscription request parameter"
slug: "test_introduction"
excerpt: ""
hidden: true
createdAt: "Thu Feb 27 2025 11:27:02 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Apr 14 2025 07:24:53 GMT+0000 (Coordinated Universal Time)"
---
## 1. Generate Token API

The table below lists the request parameters of our Generate Token API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "client_id`*`",
    "0-1": "`string`",
    "0-2": "Unique client identifier in the Plural database.  \n  \nExample: `a17ce30e-f88e-4f81-ada1-c3b4909ed232`  \n  \nNote: The Onboarding team has provided you with this information as part of the onboarding process.",
    "1-0": "client_secret`*`",
    "1-1": "`string`",
    "1-2": "Unique client secret key provided while onboarding.  \n  \nExample: `fgwei7egyhuggwp39w8rh`  \n  \n**Note**: The Onboarding team has provided you with this information as part of the onboarding process.",
    "2-0": "grant_type`*`",
    "2-1": "`string`",
    "2-2": "The grant type to generate a access token.  \n  \nAccepted value: `client_credentials`"
  },
  "cols": 3,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## 2. Create Plan

The table below lists the request parameters of our Create Plan API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "plan_name",
    "0-1": "`string`",
    "0-2": "Subscription plan name.  \n  \nExample: `Monthly Plan`",
    "1-0": "plan_description",
    "1-1": "`string`",
    "1-2": "Corresponding description for a plan.  \n  \nExample: `Diwali dhammaka plan intended to attract customers on diwali time`",
    "2-0": "notes",
    "2-1": "`string`",
    "2-2": "The note you want to show against an plan.  \n  \nExample: `Order1`",
    "3-0": "frequency_count`*`",
    "3-1": "`integer`",
    "3-2": "The total number of times your customer will be charged.  \n  \nExample:`1`",
    "4-0": "frequency`*`",
    "4-1": "`string`",
    "4-2": "Frequency of recurring transactions for this particular plan.<ul><li>Day</li><li>Week</li><li>Month</li><li>Year</li><li>AS</li><li>OT</li><li>Not Applicable</li> </ul>Example:`Day`",
    "5-0": "amount`*`",
    "5-1": "`object`",
    "5-2": "An object that contains the amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/docs/test_introduction#amount-child-object\" >Learn more about the `amount` child object.</a>",
    "6-0": "max_limit_amount`*`",
    "6-1": "`object`",
    "6-2": "An object that contains the maximum limit amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/docs/test_introduction#max-limit-amount-child-object\" >Learn more about the `max_limit_amount` child object.</a>",
    "7-0": "trial_period_in_days",
    "7-1": "`integer`",
    "7-2": "When a trial period is offered for the plan, this defines the duration of the trial period.  \n  \nExample: `1`",
    "8-0": "start_date",
    "8-1": "`string`",
    "8-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan is active and available for use.  \n  \nExample: `2022-02-01T17:32:28Z`",
    "9-0": "end_date`*`",
    "9-1": "`string`",
    "9-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan expires and can no longer be used for new subscriptions.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "10-0": "merchant_metadata",
    "10-1": "`object`",
    "10-2": "An object of key value pair that can be used to store additional information.<ul><li>Each pair cannot exceed `256` characters.</li><li>Maximum `10` key-value pairs.</ul></li>Example: `\"key1\": \"DD\"`",
    "11-0": "merchant_order_reference`*`",
    "11-1": "`string`",
    "11-2": "Unique identifier of the merchant order reference entered while creating a plan.<ul><li>Minimum: 1 characters.</li><li>Maximum: 50 characters</ul></li>Example: `1234567890`<br><br>Supported characters:<ul><li>`A-Z`</li><li>`a-z`</li><li>`-`</li><li>`_`</ul></li>"
  },
  "cols": 3,
  "rows": 12,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `create plan response` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value`*`",
    "0-1": "`integer`",
    "0-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`",
    "1-0": "currency`*`",
    "1-1": "`String`",
    "1-2": "Type of currency.  \n  \nExample: INR"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Max Limit Amount [Child Object]

The table below lists the various parameters in the `max_limit_amount` child object. This is part of the `create plan response` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value`*`",
    "0-1": "`integer`",
    "0-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`",
    "1-0": "currency`*`",
    "1-1": "`String`",
    "1-2": "Type of currency.  \n  \nExample: INR"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## 3. Get All Plan

The table below lists the request parameters of our Get All Plan API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "plan_id",
    "0-1": "`string`",
    "0-2": "Unique identifier for the subscription plan in the Plural database.  \n  \nExample: `v1-plan-4405071524-aa-qlAtAf`",
    "1-0": "start_date",
    "1-1": "`string`",
    "1-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan is active and available for use.  \n  \nExample: `2022-02-01T17:32:28Z`",
    "2-0": "end_date",
    "2-1": "`string`",
    "2-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan expires and can no longer be used for new subscriptions.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "3-0": "amount",
    "3-1": "`object`",
    "3-2": "An object that contains the amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/docs/test_introduction#amount-child-object\" >Learn more about the `amount` child object.</a>",
    "4-0": "amount_range",
    "4-1": "`string`",
    "4-2": "Range amount.  \n  \nExample: `500-1000`",
    "5-0": "frequency",
    "5-1": "`string`",
    "5-2": "Frequency of recurring transactions for this particular plan.<ul><li>Day</li><li>Week</li><li>Month</li><li>Year</li><li>AS</li><li>OT</li><li>Not Applicable</li> </ul>Example:`Day`",
    "6-0": "size",
    "6-1": "`integer`",
    "6-2": "Page number.  \n  \nExample: `2`",
    "7-0": "page",
    "7-1": "`integer`",
    "7-2": "Number of items per page.  \n  \nExample: `10`",
    "8-0": "sort",
    "8-1": "`string`",
    "8-2": "Sorting order for results.  \n  \nExample: `frequency_type,asc`"
  },
  "cols": 3,
  "rows": 9,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `create plan response` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value",
    "0-1": "`integer`",
    "0-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`",
    "1-0": "currency",
    "1-1": "`String`",
    "1-2": "Type of currency.  \n  \nExample: INR"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## 4. Create subscription

The table below lists the request parameters of our Create subscription API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant_order_reference",
    "0-1": "`string`",
    "0-2": "Unique identifier of the merchant order reference entered while creating a plan.<ul><li>Minimum: 1 characters.</li><li>Maximum: 50 characters</ul></li>Example: `1234567890`<br><br>Supported characters:<ul><li>`A-Z`</li><li>`a-z`</li><li>`-`</li><li>`_`</ul></li>",
    "1-0": "enable_notification",
    "1-1": "`boolean`",
    "1-2": "Indicates if notifications are enabled.<br><br>Example: `true`",
    "2-0": "plan_id",
    "2-1": "`string`",
    "2-2": "Unique identifier for the subscription plan in the Plural database.  \n  \nExample: `v1-plan-4405071524-aa-qlAtAf`",
    "3-0": "webhook_url",
    "3-1": "`string`",
    "3-2": "Webhook url for the subscription.<br><br>Example: `https://www.subscription-url-webhook.com`",
    "4-0": "quantity",
    "4-1": "`integer`",
    "4-2": "The quantity of the subscription for the selected plan, should be greater than 0.<br><br>Example: `1`",
    "5-0": "start_date",
    "5-1": "`string`",
    "5-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan is active and available for use.  \n  \nExample: `2022-02-01T17:32:28Z`",
    "6-0": "end_date",
    "6-1": "`string`",
    "6-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan expires and can no longer be used for new subscriptions.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "7-0": "customer_id",
    "7-1": "`string`",
    "7-2": "Unique identifier of the customer in the Plural database.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 19 characters.</ul></li>Example: `123456`",
    "8-0": "payment_mode",
    "8-1": "`string`",
    "8-2": "Payment methods allowed for subscription.<br>Accepted values:<ul><li>`CARD`</li><li>`UPI`</ul></li>Example: `UPI`",
    "9-0": "integration_mode",
    "9-1": "`string`",
    "9-2": "The integration mode for the subscription.Accepted values:<ul><li>`SEAMLESS`</ul></li>   Example: `SEAMLESS`",
    "10-0": "merchant_metadata",
    "10-1": "`object`",
    "10-2": "An object of key value pair that can be used to store additional information.<ul><li>Each pair cannot exceed `256` characters.</li><li>Maximum `10` key-value pairs.</ul></li>Example: `\"key1\": \"DD\"`",
    "11-0": "is_tpv_enabled",
    "11-1": "`boolean`",
    "11-2": "Indicates if Third-Party Validation (TPV) is enabled.<br><br>Example: `true`",
    "12-0": "bank_account",
    "12-1": "`object`",
    "12-2": "An object that contains bank account details.  \n  \nLearn more about our `bank_account` array of objects."
  },
  "cols": 3,
  "rows": 13,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Bank Account [Child Object]

The table below lists the various parameters in the `bank_account` child object. This object is part of the `Create subscription` request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "account_number<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Customer's bank account number.<ul><li>Minimum length: 1 characters</li><li>Maximum length: 50 characters.</ul></li>Example: `04992990009595`",
    "1-0": "name<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Name of Customer.<br><br>Example: `Kevin Bob`",
    "2-0": "ifsc<sup>`*`</sup>",
    "2-1": "`string`",
    "2-2": "IFSC code of the bank account.<ul><li>Minimum: 11 characters</li><li>Maximum: 11 characters</ul></li>Example: `HDFC0001234`</li>Supported Characters:<ul><li>A-Z (Uppercase letters)</li><li>0-9 (Digits)</li></ul>"
  },
  "cols": 3,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## 5. Create Payment

## Create UPI Collect

The table below lists the path parameter of our Create UPI Collect API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "order_id<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Unique identifier of the order in the Plural database.  \n  \nExample: `v1-5757575757-aa-hU1rUd`"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


The table below lists the request parameters of our Create UPI Collect API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "Payments<sup>`*`</sup>",
    "0-1": "`array of objects`",
    "0-2": "An array of objects that contains the payment details.  \n  \nLearn more about our `payments` array of objects."
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Payments [Child Object]

The table below lists the various parameters in the `payments` child object. This object is part of the `create upi collect` request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "payment_method<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Type of payment method you want to use to accept a payment.  \n  \nAccepted value: `UPI`  \n  \nExample: `UPI`",
    "1-0": "merchant_payment_reference<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Unique Payment Reference id sent by merchant.  \n  \nExample: `008cf04b-a770-4777-854e-b1e6c1230609`",
    "2-0": "payment_amount<sup>`*`</sup>",
    "2-1": "`object`",
    "2-2": "An object that contains the details of the payment amount.  \n  \nLearn more about our `payment_amount` array of objects.",
    "3-0": "payment_option<sup>`*`</sup>",
    "3-1": "`object`",
    "3-2": "An object that contains the details of the payment options.  \n  \nLearn more about our `payment_option` array of objects.",
    "4-0": "mandate_info<sup>`*`</sup>",
    "4-1": "`object`",
    "4-2": "An object that contains mandate info details.  \n  \nLearn more about our `mandate_info` array of objects."
  },
  "cols": 3,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Payment Amount [Child Object]

The table below lists the various parameters in the `payment_amount` child object. This object is part of the `payments` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value<sup>`*`</sup>",
    "0-1": "`integer`",
    "0-2": "The split amount is Paisa.<ul><li>Minimum value: `100` (₹1).</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
    "1-0": "currency<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Type of currency.  \n  \nExample: `INR`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Payment Option [Child Object]

The table below lists the various parameters in the `payment_option` child object. This object is part of the `payments` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "upi_details<sup>`*`</sup>",
    "0-1": "`object`",
    "0-2": "An object that contains the UPI details.  \n  \nLearn more about our `upi_details` array of objects."
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### UPI Details [Child Object]

The table below lists the various parameters in the `upi_details` child object. This object is part of the `payment_option` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "txn_mode<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "The transaction mode in which you want to accept payment.  \n  \nAccepted value: `COLLECT`",
    "1-0": "payer<sup>`*`</sup>",
    "1-1": "`object`",
    "1-2": "An object that contains the payer VPA handle details.  \n  \nLearn more about our `payer` array of objects."
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Payer [Child Object]

The table below lists the various parameters in the `payer` child object. This object is part of the `upi_details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "vpa<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "VPA handle of your customer from whom you want to accept payment.<ul><li>Minimum length: `2` characters.</li><li>Maximum length: `256` characters.</ul></li>Example: `kevin.bob@examplebank.com`<br><br>Supported characters:<ul><li>`A-Z`</li><li>`a-z`</li><li>`0-9`</li><li>`@`</li><li>`$`</ul></li>",
    "1-0": "phone_number<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Customer's phone number.<br><ul><li>Minimum length: 9 character.</li><li>Maximum length: 20 characters.</ul></li>Example: `9876543210`<br><br>Supported characters: <ul><li>`0-9`</li><li>`+`</ul></li>"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Manadate Info [Child Object]

The table below lists the various parameters in the `mandate_info` child object. This object is part of the `payments` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "subscription_id<sup>`*`</sup>",
    "0-1": "`integer`",
    "0-2": "Unique identifier for the subscription plan in the plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `v1-plan-4405071524-aa-qlAtAf`",
    "1-0": "request_type<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "The type of action to be performed on a mandate. <br><br>Accepted value:<ul> <li>Creation</li> <li>Execution</li> <li>Notification</li> <li>Update</li> </ul>"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Create UPI Intent

The table below lists the path parameter of our Create UPI Intent API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "order_id<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Unique identifier of the order in the Plural database.  \n  \nExample: `v1-5757575757-aa-hU1rUd`"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


The table below lists the request parameters of our Create UPI Intent API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "Payments<sup>`*`</sup>",
    "0-1": "`array of objects`",
    "0-2": "An array of objects that contains the payment details.  \n  \nLearn more about our `payments` array of objects."
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Payments [Child Object]

The table below lists the various parameters in the `payments` child object. This object is part of the `create upi intent` request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "payment_method<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Type of payment method you want to use to accept a payment.  \n  \nAccepted value: `UPI`  \n  \nExample: `UPI`",
    "1-0": "merchant_payment_reference<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Unique Payment Reference id sent by merchant.  \n  \nExample: `008cf04b-a770-4777-854e-b1e6c1230609`",
    "2-0": "payment_amount<sup>`*`</sup>",
    "2-1": "`object`",
    "2-2": "An object that contains the details of the payment amount.  \n  \nLearn more about our `payment_amount` array of objects.",
    "3-0": "payment_option<sup>`*`</sup>",
    "3-1": "`object`",
    "3-2": "An object that contains the details of the payment options.  \n  \nLearn more about our `payment_option` array of objects.",
    "4-0": "mandate_info<sup>`*`</sup>",
    "4-1": "`object`",
    "4-2": "An object that contains mandate info details.  \n  \nLearn more about our `mandate_info` array of objects."
  },
  "cols": 3,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Payment Amount [Child Object]

The table below lists the various parameters in the `payment_amount` child object. This object is part of the `payments` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value<sup>`*`</sup>",
    "0-1": "`integer`",
    "0-2": "The split amount is Paisa.<ul><li>Minimum value: `100` (₹1).</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
    "1-0": "currency<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Type of currency.  \n  \nExample: `INR`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Payment Option [Child Object]

The table below lists the various parameters in the `payment_option` child object. This object is part of the `payments` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "upi_details<sup>`*`</sup>",
    "0-1": "`object`",
    "0-2": "An object that contains the UPI details.  \n  \nLearn more about our `upi_details` array of objects."
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### UPI Details [Child Object]

The table below lists the various parameters in the `upi_details` child object. This object is part of the `payment_option` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "txn_mode<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "The transaction mode in which you want to accept payment.  \n  \nAccepted value: `INTENT`"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Manadate Info [Child Object]

The table below lists the various parameters in the `mandate_info` child object. This object is part of the `payments` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "subscription_id<sup>`*`</sup>",
    "0-1": "`integer`",
    "0-2": "Unique identifier for the subscription plan in the plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `v1-plan-4405071524-aa-qlAtAf`",
    "1-0": "request_type<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "The type of action to be performed on a mandate. <br><br>Accepted value:<ul> <li>Creation</li> <li>Execution</li> <li>Notification</li> <li>Update</li> </ul>"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]
