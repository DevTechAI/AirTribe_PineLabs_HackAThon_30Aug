---
title: "Object"
slug: "plans-object"
excerpt: "Overview of the Plan APIs response object."
hidden: false
createdAt: "Tue Feb 25 2025 06:58:34 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Apr 14 2025 07:19:50 GMT+0000 (Coordinated Universal Time)"
---
The table below lists the response objects received for the different Plan APIs.

| Plan API          | Object                            |
| :---------------- | :-------------------------------- |
| Create Plan       | Create Plan Response Object       |
| Get All Plan      | Get All Plan Response Object      |
| Get Specific Plan | Get Specific Plan Response Object |
| Update Plan       | Update Plan Response Object       |

## Create Plan Object

Shown below is a sample response returned through our Create Plan API.

```json Create Plan Response Object
{
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
}
```

The table below lists the various parameters returned in the `Create Plan API` response.

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
    "5-2": "An object that contains the amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/plans-object#amount-child-object\" >Learn more about the `amount` child object.</a>",
    "6-0": "max_limit_amount",
    "6-1": "`object`",
    "6-2": "An object that contains the maximum limit amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/plans-object#max-limit-amount-child-object\" >Learn more about the `max_limi_amount` child object.</a>",
    "7-0": "trial_period_in_days",
    "7-1": "`integer`",
    "7-2": "When a trial period is offered for the plan, this defines the duration of the trial period.  \n  \nExample: `1`  \n  \n`Note`: The trial period is always measured in days.",
    "8-0": "start_date",
    "8-1": "`string`",
    "8-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan is active and available for use.  \n  \nExample: `2022-02-01T17:32:28Z`",
    "9-0": "end_date",
    "9-1": "`string`",
    "9-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan expires and can no longer be used for new subscriptions.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "10-0": "merchant_metadata",
    "10-1": "`object`",
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


### Max Limit Amount [Child Object]

The table below lists the various parameters in the `max_limit_amount` child object. This is part of the `create plan response` object.

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


## Get All Plan

Shown below is a sample response returned through our Get All Plan API.

```json Get All Plan Response Object
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
  "plans": [
    {
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
    }
  ]
}
```

The table below lists the various parameters returned in the `Get All Plan API` response.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "links",
    "0-1": "`Object`",
    "0-2": "An object that contains pagination links for navigation.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-3#links-child-object\" >Learn more about the `links` child object.</a>",
    "1-0": "page",
    "1-1": "`object`",
    "1-2": "An object that contains the page information.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-3#page-child-object\" >Learn more about the `page` child object.</a>",
    "2-0": "plans",
    "2-1": "`Array of Objects`",
    "2-2": "An array of object that contain plan details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-3#plans-child-object\" >Learn more about the `Plans` child object.</a>"
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

The table below lists the various parameters in the `links` child object. This is part of the `Get All Plan response` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "first",
    "0-1": "`object`",
    "0-2": "An object that contains the URL information of the first page.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/plans-object#first-child-object\" >Learn more about the `first` child object.</a>",
    "1-0": "self",
    "1-1": "`object`",
    "1-2": "An object that contains the URL information of the current page.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/plans-object#self-child-object\" >Learn more about the `self` child object.</a>",
    "2-0": "next",
    "2-1": "`object`",
    "2-2": "An object that contains the URL information of the current page.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/plans-object#next-child-object\" >Learn more about the `next` child object.</a>",
    "3-0": "last",
    "3-1": "`object`",
    "3-2": "An object that contains the URL information of the current page.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/plans-object#last-child-object\" >Learn more about the `last` child object.</a>"
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
    "0-2": "URL of the first page.  \n  \nExample: `https://api.pluralpay.in/api/v1/public/plans/?size=10&page=0&sort=id,asc`"
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
    "0-2": "URL of the current page.  \n  \nExample: `\"https://api.pluralpay.in/api/v1/public/plans/?size=10&page=0&sort=id,asc\"`"
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
    "0-2": "URL of the next page.  \n  \nExample: `\"https://api.pluralpay.in/api/v1/public/plans/?size=10&page=0&sort=id,asc\"`"
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
    "0-2": "URL of the last page.  \n  \nExample: `\"https://api.pluralpay.in/api/v1/public/plans/?size=10&page=0&sort=id,asc\"`"
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

The table below lists the various parameters in the `page` child object. This is part of the `Get All Plan response` object.

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


### Plans [Child Object]

The table below lists the various parameters in the `plans` child object. This is part of the `Get All Plan response` object

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
    "5-2": "An object that contains the amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/plans-object#amount-child-object-1\" >Learn more about the `amount` child object.</a>",
    "6-0": "max_limit_amount",
    "6-1": "`object`",
    "6-2": "An object that contains the maximum limit amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/plans-object#max-limit-amount\" >Learn more about the `max_limi_amount` child object.</a>",
    "7-0": "trial_period_in_days",
    "7-1": "`integer`",
    "7-2": "When a trial period is offered for the plan, this defines the duration of the trial period.  \n  \nExample: `1`  \n  \n`Note`: The trial period is always measured in days.",
    "8-0": "start_date",
    "8-1": "`string`",
    "8-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan is active and available for use.  \n  \nExample: `2022-02-01T17:32:28Z`",
    "9-0": "end_date",
    "9-1": "`string`",
    "9-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan expires and can no longer be used for new subscriptions.  \n  \nExample: `2022-09-21T17:32:28Z`",
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


#### Max limit amount

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


## Get Specific Plan

Shown below is a sample response returned through our Get Specific Plan API.

```json Get Specific Plan Response Object
{
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
}
```
```json Update Plan Response Object
{
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
}
```

The table below lists the various parameters returned in the `Get Specific Plan API & Update Plan API` response.

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
    "5-2": "An object that contains the amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/plans-object#amount-child-object-2\" >Learn more about the `amount` child object.</a>",
    "6-0": "max_limit_amount",
    "6-1": "`object`",
    "6-2": "An object that contains the maximum limit amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/plans-object#max-limit-amount-1\" >Learn more about the `max_limi_amount` child object.</a>",
    "7-0": "trial_period_in_days",
    "7-1": "`integer`",
    "7-2": "When a trial period is offered for the plan, this defines the duration of the trial period.  \n  \nExample: `1`  \n  \n`Note`: The trial period is always measured in days.",
    "8-0": "start_date",
    "8-1": "`string`",
    "8-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan is active and available for use.  \n  \nExample: `2022-02-01T17:32:28Z`",
    "9-0": "end_date",
    "9-1": "`string`",
    "9-2": "The ISO 8601 UTC Timestamp is the date when the subscription plan expires and can no longer be used for new subscriptions.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "10-0": "merchant_metadata",
    "10-1": "`object`",
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


### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `Get Specific Plan API & Update Plan API` response object.

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


### Max limit amount [Child Object]

The table below lists the various parameters in the `max_limit_amount` child object. This is part of the `Get Specific  Plan & Update Plan API` response object.

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
