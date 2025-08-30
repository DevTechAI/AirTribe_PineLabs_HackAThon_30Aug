---
title: "Object"
slug: "subscriptions-object"
excerpt: "Overview of the Subscription APIs response object."
hidden: false
createdAt: "Tue Feb 25 2025 12:15:33 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Apr 14 2025 07:19:51 GMT+0000 (Coordinated Universal Time)"
---
The table below lists the response objects received for the different Subscription APIs.

| Plan API                  | Object                                    |
| :------------------------ | :---------------------------------------- |
| Create Subscription       | Create Subscription Response Object       |
| Get All Subscription      | Get All Subscription Response Object      |
| Get Specific Subscription | Get Specific Subscription Response Object |
| Pause Subscription        | Pause Subscription Response Object        |
| Resume Subscription       | Resume Subscription Response Object       |

## Create Subscription Object

Shown below is a sample response returned through our Create Subscription API.

```json Create Subscription Response Object
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "merchant_subscription_reference": "1234567890",
  "enable_notification": true,
  "plan_details": {
    "plan_id": "v1-plan-4405071524-aa-qlAtAf",
    "status": "ACTIVE",
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
    "merchant_plan_reference": "1234567890",
    "created_at": "2022-10-21T17:32:28Z",
    "modified_at": "2022-10-21T17:32:28Z"
  },
  "quantity": 1,
  "start_date": "2022-07-21T17:32:28Z",
  "end_date": "2022-09-21T17:32:28Z",
  "customer_id": "123456",
  "payment_mode": "UPI",
  "allowed_payment_methods": [
    "UPI"
  ],
  "integration_mode": "SEAMLESS",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "status": "ACTIVE",
  "is_tpv_enabled": true,
  "bank_account": {
    "account_number": "123456789012345",
    "name": "Gaurav Kumar",
    "ifsc": "123456789012345"
  },
  "created_at": "2022-10-21T17:32:28Z",
  "modified_at": "2022-10-21T17:32:28Z",
  "callback_url": "https://www.example.com",
  "failure_callback_url": "https://www.example.com",
  "redirect_url": "https://api-staging.pluralonline.com/api/v3/checkout-bff/redirect/checkout?token=V3_D7LwszJqF2XRiFq46uOXQr0sQn8XbObLh7WM9YF8OAxQDYRnCMbhYgHbgFf4vCjJ%22&subscription_id=v1-sub-4405071524-aa-qlAtAf"
}
```

The table below lists the various parameters returned in the Create Subscription API response. This is part of the `Create Subscription response` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "order_id",
    "0-1": "",
    "0-2": "Unique identifier of the order in the Plural database.  \n  \nExample: `v1-4405071524-aa-qlAtAf`",
    "1-0": "subscription_id",
    "1-1": "`string`",
    "1-2": "Unique identifier for the subscription plan in the plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `v1-sub-4405071524-aa-qlAtAf`",
    "2-0": "merchant_subscription_reference",
    "2-1": "`string`",
    "2-2": "Unique identifier of the merchant subscription reference entered while creating a subscription.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `1234567890`",
    "3-0": "enable_notification",
    "3-1": "`Boolean`",
    "3-2": "Indicates if notifications are enabled.  \n  \nExample: `true`",
    "4-0": "plan_details",
    "4-1": "`Array of Objects`",
    "4-2": "An array of object that contain plan details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#plan-details-child-object\" >Learn more about the `plan details` child object.</a>",
    "5-0": "quantity",
    "5-1": "`integer`",
    "5-2": "The quantity of the subscription for the selected plan, should be greater than 0.  \n  \nExample: `1`",
    "6-0": "start_date",
    "6-1": "`string`",
    "6-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan is active and available for use.  \n  \nExample: `2022-02-01T17:32:28Z`",
    "7-0": "end_date",
    "7-1": "`string`",
    "7-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan expires and can no longer be used for new subscriptions.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "8-0": "customer_id",
    "8-1": "`string`",
    "8-2": "Unique identifier of the customer in the Plural database.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 19 characters.</ul></li>Example: `123456`",
    "9-0": "payment_mode",
    "9-1": "`string`",
    "9-2": "Payment methods allowed for subscription.  \n  \nAccepted values:<ul><li>`CARD`</li><li>`UPI`</ul></li>Example: `UPI`",
    "10-0": "allowed_payment_methods",
    "10-1": "",
    "10-2": "The type of payment methods you want to offer customers.<br><br>Accepted values:<ul><li>`CARD`</li><li>`UPI`</li><li>`POINTS`</li><li>`NETBANKING`</li><li>`WALLET`</li></ul></li>Example: `UPI`",
    "11-0": "integration_mode",
    "11-1": "`string`",
    "11-2": "Type of integration.  \n  \nAccepted values:<ul><li>`SEAMLESS`</ul></li>  \nExample: `SEAMLESS`",
    "12-0": "callback_url",
    "12-1": "`string`",
    "12-2": "Use this URL to redirect your customers to specific success or failure pages based on the order or product details.  \n  \nExample: `https\\://sample-callback-url>/td>`",
    "13-0": "merchant_metadata",
    "13-1": "`object`",
    "13-2": "An object of key-value pair that can be used to store additional information.<ul><li>Each pair cannot exceed `256` characters.</li><li>Maximum `10` key-value pairs.</ul></li>Example: `\"key1\": \"DD\"`",
    "14-0": "status",
    "14-1": "`string`",
    "14-2": "Status of the Subscription.<br><br>Possible values:<ul><li>`ACTIVE`: When the subscription is currently active and payments are being processed as per the billing cycle. </li><li>`INACTIVE`: When the subscription has been created but is not yet activated.</li><li>`CREATED`: When the subscription has been successfully created but is not yet active.</li><li>`REGISTERED`: When the subscription has been registered successfully.</li><li>`CANCELLED_BY_CUSTOMER_DURING_PRE_DEBIT_NOTIFICATION`: When the customer canceled the subscription during the pre-debit notification stage.</li><li>`ARCHIVED`: When the subscription has been archived and is no longer active.</li><li>`CANCELLED_BY_CUSTOMER_DURING_MANDATE_CREATION`: When the customer canceled the subscription while setting up the payment mandate.</li><li>`CANCELLED_BY_MERCHANT`: When the subscription was canceled by the merchant.</li><li>`DEBIT_FAILED`: When the scheduled payment for the subscription failed.</li><li>`PAUSED`: When the subscription has been temporarily paused.</li><li>`CANCELLED`: When the subscription has been canceled and is no longer active.</li><li>`TRIAL`: When the subscription is in its trial period before regular billing starts.</li><li>`REVOKE_INITIATED`: When a request to revoke the subscription has been initiated.</li><li>`COMPLETED`: When the subscription has successfully completed its billing cycle.</li><li>`CANCELLED_BY_CUSTOMER`: When the customer has canceled the subscription.</li><li>`PAUSED_BY_CUSTOMER`: When the customer has temporarily paused the subscription.</li><li>`RESUMED_BY_CUSTOMER`: When the customer has resumed a previously paused subscription.</li><li>`EXPIRED`: When the subscription has reached its end date and expired.</li><li>`HALTED`: When the subscription has been stopped due to an issue or external intervention.</li><li>`RESUMED`: When the subscription has been resumed after being paused or halted.</ul></li>",
    "15-0": "is_tpv_enabled",
    "15-1": "`Boolean`",
    "15-2": "Indicates if Third-Party Validation (TPV) is enabled.  \n  \nExample: `true`",
    "16-0": "bank_account",
    "16-1": "`object`",
    "16-2": "An object that contains bank account details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#bank-account\" >Learn more about the `bank account` child object.</a>",
    "17-0": "created_at",
    "17-1": "`string`",
    "17-2": "The ISO 8601 UTC Timestamp, when the create plan request was received by Plural.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "18-0": "modified_at",
    "18-1": "`string`",
    "18-2": "The ISO 8601 UTC Timestamp, when the plan object is updated.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "19-0": "callback_url",
    "19-1": "`string`",
    "19-2": "Use this URL to redirect your customers to specific success or failure pages based on the order or product details.  \n  \nExample: `https\\://sample-callback-url`",
    "20-0": "failure_callback_url",
    "20-1": "`string`",
    "20-2": "The URL specifically used to redirect customers to a failure page based on the order or product details.  \n  \nExample: `https://sample-failure-callback-url`  \n  \n**Note**:<ul><li>If the `failure_callback_url` is not provided, customers will be redirected to the `callback_url` for both successful and failed transactions.</li><li>If the `failure_callback_url` is provided, the `callback_url` will be used exclusively for successful transactions, while the `failure_callback_url` will be used for failed transactions.</li><li>If neither URL is provided, the default URL configured during merchant onboarding will be used.</ul></li>",
    "21-0": "redirect_url",
    "21-1": "`string`",
    "21-2": "URL for redirection after checkout.  \n  \nExample: `https://api-staging.pluralonline.com/api/v3/checkout-bff/redirect/checkout?...subscription_id=v1-sub-4405071524-aa-qlAtAf`"
  },
  "cols": 3,
  "rows": 22,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Plan details [Child Object]

The table below lists the various parameters in the `plan details` child object. This is part of the `Create Subscription response` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "plan_id",
    "0-1": "`string`",
    "0-2": "Unique identifier for the subscription plan in the Plural database.  \n  \nExample: `v1-plan-4405071524-aa-qlAtAf`",
    "1-0": "status",
    "1-1": "`string`",
    "1-2": "Status of the plan.<br><br>Possible values:<ul><li>`ACTIVE`: When the plan creation request is successfully completed and the plan's start time has already passed.</li><li>`INACTIVE`: When the plan is either disabled and cannot be used for new subscriptions, or when it has exceeded its validity period and is no longer available.</li><li>`CREATED`: When the plan creation request is successfully completed and the plan's start time is set for the future.</li></ul>",
    "2-0": "plan_name",
    "2-1": "`string`",
    "2-2": "Subscription plan name.  \n  \nExample: `Monthly Plan`",
    "3-0": "plan_description",
    "3-1": "`string`",
    "3-2": "Corresponding description for a plan.  \n  \nExample: `Diwali dhammaka plan intended to attract customers on diwali time`",
    "4-0": "frequency",
    "4-1": "`string`",
    "4-2": "Frequency of recurring transactions for this particular plan.<ul><li>Day</li><li>Week</li><li>Month</li><li>Year</li><li>Bi-Monthly</li><li>Quarterly</li><li>Half-Yearly</li><li>AS</li><li>OT</li><li>Not Applicable</li> </ul>Example:`Day`",
    "5-0": "amount",
    "5-1": "`object`",
    "5-2": "An object that contains the amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#amount-child-object\" >Learn more about the `amount` child object.</a>",
    "6-0": "max_limit_amount",
    "6-1": "`object`",
    "6-2": "An object that contains the maximum limit amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#max-limit-amount\" >Learn more about the `max_limi_amount` child object.</a>",
    "7-0": "trial_period_in_days",
    "7-1": "`integer`",
    "7-2": "When a trial period is offered for the plan, this defines the duration of the trial period.  \n  \nExample: `1`  \n  \n`Note`: The trial period is always measured in days.",
    "8-0": "start_date",
    "8-1": "`string`",
    "8-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan is active and available for use.  \n  \nExample: `2022-02-01T17:32:28Z`  \n  \n**Note**: On ignoring this field plan start date will be considered as start date.",
    "9-0": "end_date",
    "9-1": "`string`",
    "9-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan expires and can no longer be used for new subscriptions.  \n  \nExample: `2022-09-21T17:32:28Z`  \n  \n**Note**: On ignoring this field, the plan will be on Active state unless there is a manual update.",
    "10-0": "merchant_metadata",
    "10-1": "`string`",
    "10-2": "An object of key-value pair that can be used to store additional information.<ul><li>Each pair cannot exceed `256` characters.</li><li>Maximum `10` key-value pairs.</ul></li>Example: `\"key1\": \"DD\"`",
    "11-0": "merchant_plan_reference",
    "11-1": "`string`",
    "11-2": "Unique identifier of the merchant plan reference entered while creating a plan.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `1234567890`",
    "12-0": "created_at",
    "12-1": "`string`",
    "12-2": "The ISO 8601 UTC Timestamp, when the create plan request was received by Plural.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "13-0": "modified_at",
    "13-1": "`string`",
    "13-2": "The ISO 8601 UTC Timestamp, when the plan object is updated.  \n  \nExample: `2022-09-21T17:32:28Z`"
  },
  "cols": 3,
  "rows": 14,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `plan` object.

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


#### Max limit amount

The table below lists the various parameters in the `max_limit_amount` child object. This is part of the `plan` object.

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


### Bank account

The table below lists the various parameters in the `bank account` child object. This is part of the `Create Subscription response` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "account_number",
    "0-1": "`string`",
    "0-2": "Bank account number.<ul><li>Minimum length: 1 characters</li><li>Maximum length: 50 characters.</ul></li>Example: `12345678912345`",
    "1-0": "name",
    "1-1": "`String`",
    "1-2": "Name of Customer.  \n  \nExample: `Kevin Bob`  ",
    "2-0": "ifsc",
    "2-1": "`String`",
    "2-2": "IFSC code of the bank account.<ul><li>Minimum: 11 characters</li><li>Maximum: 11 characters</ul></li>Example: `HDFC0001234`</li>  \n  \nSupported Characters:<ul><li>A-Z (Uppercase letters)</li><li>0-9 (Digits)</li></ul>"
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


## Get All Subscription Object

Shown below is a sample response returned through our Get All Subscription API.

```json Create Plan Response Object
{
  "links": {
    "first": {
      "href": "https://api.pluralpay.in/api/v1/public /{resource}/?size=10&page=0&sort=id,asc"
    },
    "self": {
      "href": "https://api.pluralpay.in/api/v1/public /{resource}/?size=10&page=0&sort=id,asc"
    },
    "next": {
      "href": "https://api.pluralpay.in/api/v1/public /{resource}/?size=10&page=0&sort=id,asc"
    },
    "last": {
      "href": "https://api.pluralpay.in/api/v1/public /{resource}/?size=10&page=0&sort=id,asc"
    }
  },
  "page": {
    "size": 10,
    "total_elements": 50,
    "total_pages": 5,
    "number": 1
  },
  "subscriptions": [
    {
      "order_id": "v1-4405071524-aa-qlAtAf",
      "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
      "merchant_subscription_reference": "1234567890",
      "enable_notification": true,
      "plan_details": {
        "plan_id": "v1-plan-4405071524-aa-qlAtAf",
        "status": "ACTIVE",
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
        "merchant_plan_reference": "1234567890",
        "created_at": "2022-10-21T17:32:28Z",
        "modified_at": "2022-10-21T17:32:28Z"
      },
      "quantity": 1,
      "start_date": "2022-07-21T17:32:28Z",
      "end_date": "2022-09-21T17:32:28Z",
      "customer_id": "123456",
      "payment_mode": "UPI",
      "allowed_payment_methods": [
        "UPI"
      ],
      "integration_mode": "SEAMLESS",
      "merchant_metadata": {
        "key1": "DD",
        "key2": "XOF"
      },
      "status": "ACTIVE",
      "is_tpv_enabled": true,
      "bank_account": {
        "account_number": "123456789012345",
        "name": "Gaurav Kumar",
        "ifsc": "123456789012345"
      },
      "created_at": "2022-10-21T17:32:28Z",
      "modified_at": "2022-10-21T17:32:28Z"
    }
  ]
}
```

The table below lists the various parameters returned in the Get All Subscription API response.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "links",
    "0-1": "`Object`",
    "0-2": "An object that contains pagination links for navigation.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#links-child-object\" >Learn more about the `links` child object.</a>",
    "1-0": "page",
    "1-1": "`object`",
    "1-2": "An page object.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#page-child-object\" >Learn more about the `Page` child object.</a>",
    "2-0": "subscriptions",
    "2-1": "`Array of Objects`",
    "2-2": "An array of object that contain subscriptions details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#subscriptions\" >Learn more about the `Subscriptions` child object.</a>"
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


### links [Child object]

The table below lists the various parameters in the `links` child object. This is part of the `Get All Subscription response` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "first",
    "0-1": "`object`",
    "0-2": "An object that contains the URL information of the first page.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#first-child-object\" >Learn more about the `first` child object.</a>",
    "1-0": "self",
    "1-1": "`object`",
    "1-2": "An object that contains the URL information of the current page.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#self-child-object\" >Learn more about the `self` child object.</a>",
    "2-0": "next",
    "2-1": "`object`",
    "2-2": "An object that contains the URL information of the current page.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#next-child-object\" >Learn more about the `next` child object.</a>",
    "3-0": "last",
    "3-1": "`object`",
    "3-2": "An object that contains the URL information of the current page.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#last-child-object\" >Learn more about the `last` child object.</a>"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### First [Child Object]

The table below lists the various parameters in the `first` child object. This is part of the `links` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "href",
    "0-1": "`string`",
    "0-2": "URL of the first page.  \n  \nExample: `<https://api.pluralpay.in/api/v1/public> /{resource}/?size=10&page=0&sort=id,asc`"
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


#### Self [Child Object]

The table below lists the various parameters in the `self` child object. This is part of the `links` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "href",
    "0-1": "`string`",
    "0-2": "URL of the current page.  \n  \nExample: `\"<https://api.pluralpay.in/api/v1/public> /{resource}/?size=10&page=0&sort=id,asc\"`"
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


#### Next [Child Object]

The table below lists the various parameters in the `next` child object. This is part of the `links` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "href",
    "0-1": "`string`",
    "0-2": "URL of the next page.  \n  \nExample: `\"<https://api.pluralpay.in/api/v1/public> /{resource}/?size=10&page=0&sort=id,asc\"`"
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


#### Last [Child Object]

The table below lists the various parameters in the `last` child object. This is part of the `links` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "href",
    "0-1": "`string`",
    "0-2": "URL of the last page.  \n  \nExample: `\"<https://api.pluralpay.in/api/v1/public> /{resource}/?size=10&page=0&sort=id,asc\"`"
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


### Page [Child Object]

The table below lists the various parameters in the `page` child object. This is part of the `Get All Subscription response` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "size",
    "0-1": "`Integer`",
    "0-2": "Number of items per page.  \n  \nExample: `10`",
    "1-0": "total_elements",
    "1-1": "`Integer`",
    "1-2": "Total number of elements.  \n  \nExample: `50`",
    "2-0": "total_pages",
    "2-1": "`Integer`",
    "2-2": "Total number of pages.  \n  \nExample: `5`",
    "3-0": "number",
    "3-1": "`Integer`",
    "3-2": "Page number.  \n  \nExample: `1`"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Subscriptions

The table below lists the various parameters in the `subscriptions` child object. This is part of the `Get All Subscription response` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "subscription_id",
    "0-1": "`string`",
    "0-2": "Unique identifier for the subscription plan in the plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `v1-sub-4405071524-aa-qlAtAf`",
    "1-0": "merchant_subscription_reference",
    "1-1": "`string`",
    "1-2": "Unique identifier of the merchant subscription reference entered while creating a subscrition.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `1234567890`",
    "2-0": "enable_notification",
    "2-1": "`Boolean`",
    "2-2": "Indicates if notifications are enabled.  \n  \nExample: `true`",
    "3-0": "plan_details",
    "3-1": "`Array of Objects`",
    "3-2": "An array of object that contain plan details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#plan-details-child-object-1\" >Learn more about the `Plan Details` child object.</a>",
    "4-0": "quantity",
    "4-1": "`integer`",
    "4-2": "The quantity of the subscription for the selected plan, should be greater than 0.  \n  \nExample: `1`",
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
    "8-2": "Payment methods allowed for subscription.  \n  \nAaccepted values:<ul><li>`CARD`</li><li>`UPI`</ul></li>Example: `UPI`",
    "9-0": "allowed_payment_methods",
    "9-1": "`string`",
    "9-2": "The type of payment methods you want to offer customers.<br><br>Accepted values:<ul><li>`CARD`</li><li>`UPI`</li><li>`POINTS`</li><li>`NETBANKING`</li><li>`WALLET`</li></ul></li>Example: `UPI`",
    "10-0": "integration_mode",
    "10-1": "`string`",
    "10-2": "Type of integration.  \n  \nAccepted values:<ul><li>`SEAMLESS`</ul></li>  \n  \nExample: `SEAMLESS`",
    "11-0": "callback_url",
    "11-1": "`string`",
    "11-2": "Use this URL to redirect your customers to specific success or failure pages based on the order or product details.  \n  \nExample: `https\\://sample-callback-url>/td>`",
    "12-0": "merchant_metadata",
    "12-1": "`object`",
    "12-2": "An object of key-value pair that can be used to store additional information.<ul><li>Each pair cannot exceed `256` characters.</li><li>Maximum `10` key-value pairs.</ul></li>Example: `\"key1\": \"DD\"`",
    "13-0": "status",
    "13-1": "`string`",
    "13-2": "Status of the Subscription.<br><br>Possible values:<ul><li>`ACTIVE`: When the subscription is currently active and payments are being processed as per the billing cycle. </li><li>`INACTIVE`: When the mandate creation fails or the scheduled payment for the subscription fails more than three times.</li><li>`CREATED`: When the subscription has been successfully created but is not yet active.</li><li>`DEBIT_FAILED`: When the scheduled payment for the subscription failed less than 3 times.</li><li>`PAUSED`: When the subscription has been temporarily paused, it needs to be in an active, inactive, trial, or resumed state to pause it again.</li><li>`TRIAL`: When the subscription is in its trial period before regular billing starts.</li><li>`COMPLETED`: When the subscription has successfully completed its billing cycle.</li><li>`RESUMING`: Intermediate stage where a subscription transitions from PAUSED or HALTED to RESUMED.</li><li>`EXPIRED`: When the subscription has reached its end date and expired.</li><li>`RESUMED`: When the subscription has been resumed after being paused or halted.</ul></li>",
    "14-0": "bank_account",
    "14-1": "`object`",
    "14-2": "An object that contains bank account details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#bank-account-child-object\" >Learn more about the `Bank Account` child object.</a>",
    "15-0": "is_tpv_enabled",
    "15-1": "`Boolean`",
    "15-2": "Indicates if Third-Party Validation (TPV) is enabled.  \n  \nExample: `true`",
    "16-0": "created_at",
    "16-1": "`string`",
    "16-2": "The ISO 8601 UTC Timestamp, when the create plan request was received by Plural.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "17-0": "modified_at",
    "17-1": "`string`",
    "17-2": "The ISO 8601 UTC Timestamp, when the plan object is updated.  \n  \nExample: `2022-09-21T17:32:28Z`"
  },
  "cols": 3,
  "rows": 18,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Plan details [Child Object]

The table below lists the various parameters in the `plan details` child object. This is part of the `Subscription` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "plan_id",
    "0-1": "`string`",
    "0-2": "Unique identifier for the subscription plan in the Plural database.  \n  \nExample: `v1-plan-4405071524-aa-qlAtAf`",
    "1-0": "status",
    "1-1": "`string`",
    "1-2": "Status of the plan.<br><br>Possible values:<ul><li>`ACTIVE`: When the plan creation request is successfully completed and the plan's start time has already passed.</li><li>`INACTIVE`: When the plan is either disabled and cannot be used for new subscriptions, or when it has exceeded its validity period and is no longer available.</li><li>`CREATED`: When the plan creation request is successfully completed and the plan's start time is set for the future.</li></ul>",
    "2-0": "plan_name",
    "2-1": "`string`",
    "2-2": "Subscription plan name.  \n  \nExample: `Monthly Plan`",
    "3-0": "plan_description",
    "3-1": "`string`",
    "3-2": "Corresponding description for a plan.  \n  \nExample: `Diwali dhammaka plan intended to attract customers on diwali time`",
    "4-0": "frequency",
    "4-1": "`string`",
    "4-2": "Frequency of recurring transactions for this particular plan.<ul><li>Day</li><li>Week</li><li>Month</li><li>Year</li><li>Bi-Monthly</li><li>Quarterly</li><li>Half-Yearly</li><li>AS</li><li>OT</li><li>Not Applicable</li> </ul>Example:`Day`",
    "5-0": "amount",
    "5-1": "`object`",
    "5-2": "An object that contains the amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#amount-child-object-1\" >Learn more about the `amount` child object.</a>",
    "6-0": "max_limit_amount",
    "6-1": "`object`",
    "6-2": "An object that contains the maximum limit amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#max-limit-amount-child-object\" >Learn more about the `max_limi_amount` child object.</a>",
    "7-0": "trial_period_in_days",
    "7-1": "`integer`",
    "7-2": "When a trial period is offered for the plan, this defines the duration of the trial period.  \n  \nExample: `1`  \n  \n`Note`: The trial period is always measured in days.",
    "8-0": "start_date",
    "8-1": "`string`",
    "8-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan is active and available for use.  \n  \nExample: `2022-02-01T17:32:28Z`  \n  \n**Note**: On ignoring this field plan start date will be considered as start date.",
    "9-0": "end_date",
    "9-1": "`string`",
    "9-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan expires and can no longer be used for new subscriptions.  \n  \nExample: `2022-09-21T17:32:28Z`  \n  \n**Note**: On ignoring this field, the plan will be on Active state unless there is a manual update.",
    "10-0": "merchant_metadata",
    "10-1": "`string`",
    "10-2": "An object of key-value pair that can be used to store additional information.<ul><li>Each pair cannot exceed `256` characters.</li><li>Maximum `10` key-value pairs.</ul></li>Example: `\"key1\": \"DD\"`",
    "11-0": "merchant_plan_reference",
    "11-1": "`string`",
    "11-2": "Unique identifier of the merchant plan reference entered while creating a plan.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `1234567890`",
    "12-0": "created_at",
    "12-1": "`string`",
    "12-2": "The ISO 8601 UTC Timestamp, when the create plan request was received by Plural.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "13-0": "modified_at",
    "13-1": "`string`",
    "13-2": "The ISO 8601 UTC Timestamp, when the plan object is updated.  \n  \nExample: `2022-09-21T17:32:28Z`"
  },
  "cols": 3,
  "rows": 14,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `Plans` object.

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


#### Max limit amount [Child Object]

The table below lists the various parameters in the `max_limit_amount` child object. This is part of the `Plans` object.

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


### Bank account [Child Object]

The table below lists the various parameters in the `bank account` child object. This is part of the `Subscription` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "account_number",
    "0-1": "`string`",
    "0-2": "Bank account number.<ul><li>Minimum length: 1 characters</li><li>Maximum length: 50 characters.</ul></li>Example: `04992990009595`",
    "1-0": "name",
    "1-1": "`String`",
    "1-2": "Name of Customer.  \n  \nExample: `Kevin Bob`",
    "2-0": "ifsc",
    "2-1": "`String`",
    "2-2": "IFSC code of the bank account.<ul><li>Minimum: 11 characters</li><li>Maximum: 11 characters</ul></li>Example: `HDFC0001234`</li>  \n  \nSupported Characters:<ul><li>A-Z (Uppercase letters)</li><li>0-9 (Digits)</li></ul>"
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


## Get Specific Subscription, Pause Subscription, Resume Subscription Objects

Shown below are the sample responses returned through our `Get Specific Subscription`, `Pause Subscription`, `Resume Subscription` APIs.

```json Get Specific Subscription Response Object
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "merchant_subscription_reference": "1234567890",
  "enable_notification": true,
  "plan_details": {
    "plan_id": "v1-plan-4405071524-aa-qlAtAf",
    "status": "ACTIVE",
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
    "merchant_plan_reference": "1234567890",
    "created_at": "2022-10-21T17:32:28Z",
    "modified_at": "2022-10-21T17:32:28Z"
  },
  "quantity": 1,
  "start_date": "2022-07-21T17:32:28Z",
  "end_date": "2022-09-21T17:32:28Z",
  "customer_id": "123456",
  "payment_mode": "UPI",
  "allowed_payment_methods": [
    "UPI"
  ],
  "integration_mode": "SEAMLESS",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "status": "ACTIVE",
  "is_tpv_enabled": true,
  "bank_account": {
    "account_number": "123456789012345",
    "name": "Gaurav Kumar",
    "ifsc": "123456789012345"
  },
  "created_at": "2022-10-21T17:32:28Z",
  "modified_at": "2022-10-21T17:32:28Z"
}
```
```json Pause Subscription Response Object
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "merchant_subscription_reference": "1234567890",
  "enable_notification": true,
  "plan_details": {
    "plan_id": "v1-plan-4405071524-aa-qlAtAf",
    "status": "ACTIVE",
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
    "merchant_plan_reference": "1234567890",
    "created_at": "2022-10-21T17:32:28Z",
    "modified_at": "2022-10-21T17:32:28Z"
  },
  "quantity": 1,
  "start_date": "2022-07-21T17:32:28Z",
  "end_date": "2022-09-21T17:32:28Z",
  "customer_id": "123456",
  "payment_mode": "UPI",
  "allowed_payment_methods": [
    "UPI"
  ],
  "integration_mode": "SEAMLESS",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "status": "PAUSED",
  "is_tpv_enabled": true,
  "bank_account": {
    "account_number": "123456789012345",
    "name": "Gaurav Kumar",
    "ifsc": "123456789012345"
  },
  "created_at": "2022-10-21T17:32:28Z",
  "modified_at": "2022-10-21T17:32:28Z"
}
```
```json Resume Subscription Response Object
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "merchant_subscription_reference": "1234567890",
  "enable_notification": true,
  "plan_details": {
    "plan_id": "v1-plan-4405071524-aa-qlAtAf",
    "status": "ACTIVE",
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
    "merchant_plan_reference": "1234567890",
    "created_at": "2022-10-21T17:32:28Z",
    "modified_at": "2022-10-21T17:32:28Z"
  },
  "quantity": 1,
  "start_date": "2022-07-21T17:32:28Z",
  "end_date": "2022-09-21T17:32:28Z",
  "customer_id": "123456",
  "payment_mode": "UPI",
  "allowed_payment_methods": [
    "UPI"
  ],
  "integration_mode": "SEAMLESS",
  "merchant_metadata": {
    "key1": "DD",
    "key2": "XOF"
  },
  "status": "RESUMING",
  "is_tpv_enabled": true,
  "bank_account": {
    "account_number": "123456789012345",
    "name": "Gaurav Kumar",
    "ifsc": "123456789012345"
  },
  "created_at": "2022-10-21T17:32:28Z",
  "modified_at": "2022-10-21T17:32:28Z"
}
```

The table below lists the various parameters returned in the Get Specific Subscription, Pause Subscription, Resume Subscription API responses.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "subscription_id",
    "0-1": "`string`",
    "0-2": "Unique identifier for the subscription plan in the plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `v1-sub-4405071524-aa-qlAtAf`",
    "1-0": "order_id",
    "1-1": "`string`",
    "1-2": "Unique identifier of the order in the Plural database.  \n  \nExample: `v1-4405071524-aa-qlAtAf`",
    "2-0": "merchant_subscription_reference",
    "2-1": "`string`",
    "2-2": "Unique identifier of the merchant subscription reference entered while creating a subscription.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `1234567890`",
    "3-0": "enable_notification",
    "3-1": "`Boolean`",
    "3-2": "Indicates if notifications are enabled.  \n  \nExample: `true`",
    "4-0": "plan_details",
    "4-1": "`Array of Objects`",
    "4-2": "An array of object that contain plan details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#plan-details-child-object-2\" >Learn more about the `plan details` child object.</a>",
    "5-0": "quantity",
    "5-1": "`integer`",
    "5-2": "The quantity of the subscription for the selected plan, should be greater than 0.  \n  \nExample: `1`",
    "6-0": "start_date",
    "6-1": "`string`",
    "6-2": "The ISO 8601 UTC Timestamp, the date when the subscription plan becomes active and available for use.  \n  \nExample: `2022-02-01T17:32:28Z`",
    "7-0": "end_date",
    "7-1": "`string`",
    "7-2": "The ISO 8601 UTC Timestamp, the date when the subscription plan expires and can no longer be used for new subscriptions.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "8-0": "customer_id",
    "8-1": "`string`",
    "8-2": "Unique identifier of the customer in the Plural database.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 19 characters.</ul></li>Example: `123456`",
    "9-0": "payment_mode",
    "9-1": "`string`",
    "9-2": "Payment methods allowed for subscription.  \n  \nAaccepted values:<ul><li>`CARD`</li><li>`UPI`</ul></li>Example: `UPI`",
    "10-0": "allowed_payment_methods",
    "10-1": "`string`",
    "10-2": "The type of payment methods you want to offer customers.<br><br>Accepted values:<ul><li>`CARD`</li><li>`UPI`</li><li>`POINTS`</li><li>`NETBANKING`</li><li>`WALLET`</li></ul></li>Example: `UPI`",
    "11-0": "integration_mode",
    "11-1": "`string`",
    "11-2": "Type of integration.  \n  \nAccepted values:<ul><li>`SEAMLESS`</ul></li>  \nExample: `SEAMLESS`",
    "12-0": "callback_url",
    "12-1": "`string`",
    "12-2": "Use this URL to redirect your customers to specific success or failure pages based on the order or product details.  \n  \nExample: `https\\://sample-callback-url>/td>`",
    "13-0": "merchant_metadata",
    "13-1": "`object`",
    "13-2": "An object of key-value pair that can be used to store additional information.<ul><li>Each pair cannot exceed `256` characters.</li><li>Maximum `10` key-value pairs.</ul></li>Example: `\"key1\": \"DD\"`",
    "14-0": "status",
    "14-1": "`string`",
    "14-2": "Status of the Subscription.<br><br>Possible values:<ul><li>`ACTIVE`: When the subscription is currently active and payments are being processed as per the billing cycle. </li><li>`INACTIVE`: When the mandate creation fails or the scheduled payment for the subscription fails more than three times.</li><li>`CREATED`: When the subscription has been successfully created but is not yet active.</li><li>`DEBIT_FAILED`: When the scheduled payment for the subscription failed less than 3 times.</li><li>`PAUSED`: When the subscription has been temporarily paused, it needs to be in an active, inactive, trial, or resumed state to pause it again.</li><li>`TRIAL`: When the subscription is in its trial period before regular billing starts.</li><li>`COMPLETED`: When the subscription has successfully completed its billing cycle.</li><li>`RESUMING`: Intermediate stage where a subscription transitions from PAUSED or HALTED to RESUMED.</li><li>`EXPIRED`: When the subscription has reached its end date and expired.</li><li>`RESUMED`: When the subscription has been resumed after being paused or halted.</ul></li>",
    "15-0": "bank_account",
    "15-1": "`object`",
    "15-2": "An object that contains bank account details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#bank-account-child-object-1\" >Learn more about the `bank account` child object.</a>",
    "16-0": "is_tpv_enabled",
    "16-1": "`Boolean`",
    "16-2": "Indicates if Third-Party Validation (TPV) is enabled.  \n  \nExample: `true`",
    "17-0": "created_at",
    "17-1": "`string`",
    "17-2": "The ISO 8601 UTC Timestamp, when the create plan request was received by Plural.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "18-0": "modified_at",
    "18-1": "`string`",
    "18-2": "The ISO 8601 UTC Timestamp, when the plan object is updated.  \n  \nExample: `2022-09-21T17:32:28Z`"
  },
  "cols": 3,
  "rows": 19,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Plan details [Child Object]

The table below lists the various parameters in the `Plan Details` child object. This is part of `Get Specific Subscription`, `Pause Subscription`, and `Resume Subscription` API responses object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "plan_id",
    "0-1": "`string`",
    "0-2": "Unique identifier for the subscription plan in the Plural database.  \n  \nExample: `v1-plan-4405071524-aa-qlAtAf`",
    "1-0": "status",
    "1-1": "`string`",
    "1-2": "Status of the plan.<br><br>Possible values:<ul><li>`ACTIVE`: When the plan creation request is successfully completed and the plan's start time has already passed.</li><li>`INACTIVE`: When the plan is either disabled and cannot be used for new subscriptions, or when it has exceeded its validity period and is no longer available.</li><li>`CREATED`: When the plan creation request is successfully completed and the plan's start time is set for the future.</li></ul>",
    "2-0": "plan_name",
    "2-1": "`string`",
    "2-2": "Subscription plan name.  \n  \nExample: `Monthly Plan`",
    "3-0": "plan_description",
    "3-1": "`string`",
    "3-2": "Corresponding description for a plan.  \n  \nExample: `Diwali dhammaka plan intended to attract customers on diwali time`",
    "4-0": "frequency",
    "4-1": "`string`",
    "4-2": "Frequency of recurring transactions for this particular plan.<ul><li>Day</li><li>Week</li><li>Month</li><li>Year</li><li>Bi-Monthly</li><li>Quarterly</li><li>Half-Yearly</li><li>AS</li><li>OT</li><li>Not Applicable</li> </ul>Example:`Day`",
    "5-0": "amount",
    "5-1": "`object`",
    "5-2": "An object that contains the amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#amount-child-object-2\" >Learn more about the `amount` child object.</a>",
    "6-0": "max_limit_amount",
    "6-1": "`object`",
    "6-2": "An object that contains the maximum limit amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-4#max-limit-amount-child-object-1\" >Learn more about the `max_limi_amount` child object.</a>",
    "7-0": "trial_period_in_days",
    "7-1": "`integer`",
    "7-2": "When a trial period is offered for the plan, this defines the duration of the trial period.  \n  \nExample: `1`  \n  \n`Note`: The trial period is always measured in days.",
    "8-0": "start_date",
    "8-1": "`string`",
    "8-2": "The ISO 8601 UTC Timestamp, the date when the subscription plan becomes active and available for use.  \n  \nExample: `2022-02-01T17:32:28Z`  \n  \n**Note**: On ignoring this field plan start date will be considered as start date.",
    "9-0": "end_date",
    "9-1": "`string`",
    "9-2": "The ISO 8601 UTC Timestamp, the date when the subscription plan expires and can no longer be used for new subscriptions.  \n  \nExample: `2022-09-21T17:32:28Z`  \n  \n**Note**: On ignoring this field, the plan will be on Active state unless there is a manual update.",
    "10-0": "merchant_metadata",
    "10-1": "`string`",
    "10-2": "An object of key-value pair that can be used to store additional information.<ul><li>Each pair cannot exceed `256` characters.</li><li>Maximum `10` key-value pairs.</ul></li>Example: `\"key1\": \"DD\"`",
    "11-0": "merchant_plan_reference",
    "11-1": "`string`",
    "11-2": "Unique identifier of the merchant plan reference entered while creating a plan.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `1234567890`",
    "12-0": "created_at",
    "12-1": "`string`",
    "12-2": "The ISO 8601 UTC Timestamp, when the create plan request was received by Plural.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "13-0": "modified_at",
    "13-1": "`string`",
    "13-2": "The ISO 8601 UTC Timestamp, when the plan object is updated.  \n  \nExample: `2022-09-21T17:32:28Z`"
  },
  "cols": 3,
  "rows": 14,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `plan` object.

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


#### Max limit amount [Child Object]

The table below lists the various parameters in the `max_limit_amount` child object. This is part of the `plan` object.

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


### Bank account [Child Object]

The table below lists the various parameters in the `bank account` child object. This is part of `Get Specific Subscription`, `Pause Subscription`, and `Resume Subscription` API responses object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "account_number",
    "0-1": "`string`",
    "0-2": "Bank account number.<ul><li>Minimum length: 1 characters</li><li>Maximum length: 50 characters.</ul></li>Example: `04992990009595`",
    "1-0": "name",
    "1-1": "`String`",
    "1-2": "Name of Customer.  \n  \nExample: `Kevin Bob`  ",
    "2-0": "ifsc",
    "2-1": "`String`",
    "2-2": "IFSC code of the bank account.<ul><li>Minimum: 11 characters</li><li>Maximum: 11 characters</ul></li>Example: `HDFC0001234`</li>  \n  \nSupported Characters:<ul><li>A-Z (Uppercase letters)</li><li>0-9 (Digits)</li></ul>"
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
