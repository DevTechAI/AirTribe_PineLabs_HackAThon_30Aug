---
title: "Object"
slug: "presentation-object"
excerpt: "Overview of the Presentation APIs response object."
hidden: false
createdAt: "Tue Feb 25 2025 12:19:35 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Apr 14 2025 07:19:50 GMT+0000 (Coordinated Universal Time)"
---
The table below lists the response objects received for the Presentation APIs.

| Subscription APIs                   | Object                                              |
| :---------------------------------- | :-------------------------------------------------- |
| Create Presentation                 | Create Presentation Response Object                 |
| Get Presentation                    | Presentation Response Object                        |
| Get Presentation by Subscription Id | Get Presentation by Subscription Id Response Object |

## Create Presentation

Shown below is a sample response returned through our Create Presentation API.

```json Create Presentation Response Object
{
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "presentation_id": "v1-pre-4405071524-aa-qlAtAf",
  "due_date": "2022-09-21T17:32:28Z",
  "amount": {
    "value": 100,
    "currency": "INR"
  },
  "merchant_presentation_reference": "1234567890"
}
```

The table below lists the various parameters returned in the Create Presentation API response. This is part of the `Create Presentation response` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "subscription_id",
    "0-1": "`string`",
    "0-2": "Unique identifier for the subscription plan in the plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `v1-sub-4405071524-aa-qlAtAf`",
    "1-0": "presentation_id",
    "1-1": "`string`",
    "1-2": "A Unique identifier for the presentation provided by the Plural.<ul><li>Maximum length: 50 characters.</ul></li>Example: `v1-pre-4405071524-aa-qlAtAf`",
    "2-0": "due_date",
    "2-1": "`string`",
    "2-2": "The ISO 8601 UTC Timestamp is the date & time at which the payment is due.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "3-0": "amount",
    "3-1": "`object`",
    "3-2": "An object that contains the amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-3#amount-child-object\" >Learn more about the `amount` child object.</a>",
    "4-0": "merchant_presentation_reference",
    "4-1": "`string`",
    "4-2": "Unique identifier of the merchant presentation reference entered while creating a presentation.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `1234567890`"
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


### amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `Create Presentation response` object.

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


## Get Presentation

Shown below is a sample response returned through our Get Presentation API.

```json Get Presentation Response Object
{
  "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
  "presentation_id": "v1-pre-4405071524-aa-qlAtAf",
  "due_date": "2022-09-21T17:32:28Z",
  "amount": {
    "value": 100,
    "currency": "INR"
  },
  "merchant_presentation_reference": "1234567890"
}
```

The table below lists the various parameters returned in the Get Presentation API response. This is part of the `Get Presentation response` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "subscription_id",
    "0-1": "`string`",
    "0-2": "Unique identifier for the subscription plan in the plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `v1-sub-4405071524-aa-qlAtAf`",
    "1-0": "presentation_id",
    "1-1": "`string`",
    "1-2": "A Unique identifier for the presentation provided by the Plural.<ul><li>Maximum length: 50 characters.</ul></li>Example: `v1-pre-4405071524-aa-qlAtAf`",
    "2-0": "due_date",
    "2-1": "`string`",
    "2-2": " The ISO 8601 UTC timestamp indicating the date and time when the payment is due.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "3-0": "amount",
    "3-1": "`object`",
    "3-2": "An object that contains the amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-3#amount-child-object\" >Learn more about the `amount` child object.</a>",
    "4-0": "merchant_presentation_reference",
    "4-1": "`string`",
    "4-2": "Unique identifier of the merchant presentation reference entered while creating a presentation.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `1234567890`"
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


### amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `Get Presentation response` object.

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


## Get Presentation by Subscription Id

Shown below is a sample response returned through our Get Presentation by Subscription Id API.

```json Get Presentation by Subscription Id Response Object
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
  "presentations": [
    {
      "subscription_id": "v1-sub-4405071524-aa-qlAtAf",
      "presentation_id": "v1-pre-4405071524-aa-qlAtAf",
      "due_date": "2022-09-21T17:32:28Z",
      "amount": {
        "value": 100,
        "currency": "INR"
      },
      "merchant_presentation_reference": "1234567890"
    }
  ]
}
```

The table below lists the various parameters returned in the Get Presentation by Subscription Id API response. This is part of the `Get Presentation by Subscription Id` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "links",
    "0-1": "`Object`",
    "0-2": "An object that contains pagination links for navigation.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-5#links-child-object\" >Learn more about the `links` child object.</a>",
    "1-0": "page",
    "1-1": "`object`",
    "1-2": "An object that contains the page information.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-5#page-child-object\" >Learn more about the `page` child object.</a>",
    "2-0": "presentations",
    "2-1": "`Array of Objects`",
    "2-2": "An array of object that contain presentations details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-5#presentations-child-object\" >Learn more about the `presentations` child object.</a>"
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

The table below lists the various parameters in the `links` child object. This is part of the `Get Presentation by Subscription Id` response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "first",
    "0-1": "`object`",
    "0-2": "An object that contains the URL information of the first page.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-5#first-child-object\" >Learn more about the `first` child object.</a>",
    "1-0": "self",
    "1-1": "`object`",
    "1-2": "An object that contains the URL information of the current page.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-5#self-child-object\" >Learn more about the `self` child object.</a>",
    "2-0": "next",
    "2-1": "`object`",
    "2-2": "An object that contains the URL information of the current page.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-5#next-child-object\" >Learn more about the `next` child object.</a>",
    "3-0": "last",
    "3-1": "`object`",
    "3-2": "An object that contains the URL information of the current page.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-5#last-child-object\" >Learn more about the `last` child object.</a>"
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
    "0-2": "URL of the first page.  \n  \nExample: `https://api.pluralpay.in/api/v1/public/subscriptions/{subscription_id}/presentations?size=10&page=0&sort=id,asc`"
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
    "0-2": "URL of the current page.  \n  \nExample: `\"https://api.pluralpay.in/api/v1/public/subscriptions/{subscription_id}/presentations?size=10&page=0&sort=id,asc\"`"
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
    "0-2": "URL of the next page.  \n  \nExample: `\"https://api.pluralpay.in/api/v1/public/subscriptions/{subscription_id}/presentations?size=10&page=0&sort=id,asc\"`"
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
    "0-2": "URL of the last page.  \n  \nExample: `\"https://api.pluralpay.in/api/v1/public/subscriptions/{subscription_id}/presentations?size=10&page=0&sort=id,asc\"`"
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


### Presentations [Child Object]

The table below lists the various parameters in the `presentations` child object. This is part of the `Get Presentation by Subscription Id` response object

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "subscription_id",
    "0-1": "`string`",
    "0-2": "Unique identifier for the subscription plan in the plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: \\`v1-sub-4405071524-aa-qlAtAf",
    "1-0": "presentation_id",
    "1-1": "`string`",
    "1-2": "A Unique identifier for the presentation provided by the Plural.<ul><li>Maximum length: 50 characters.</ul></li>Example: `v1-pre-4405071524-aa-qlAtAf`",
    "2-0": "due_date",
    "2-1": "`string`",
    "2-2": "The ISO 8601 UTC timestamp indicating the date and time when the payment is due.  \n  \nExample: `2022-09-21T17:32:28Z`",
    "3-0": "amount",
    "3-1": "`object`",
    "3-2": "An object that contains the amount details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/object-5#amount-child-object-2\" >Learn more about the `amount` child object.</a>",
    "4-0": "merchant_presentation_reference",
    "4-1": "`string`",
    "4-2": "Unique identifier of the merchant presentation reference entered while creating a presentation.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `1234567890`"
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


#### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `presentations` object.

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
