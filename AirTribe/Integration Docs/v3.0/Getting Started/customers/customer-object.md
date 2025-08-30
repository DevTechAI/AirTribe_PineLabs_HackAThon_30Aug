---
title: "Object"
slug: "customer-object"
excerpt: "Overview of Customers sample response object."
hidden: false
createdAt: "Mon Feb 10 2025 09:05:00 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Mar 24 2025 10:58:26 GMT+0000 (Coordinated Universal Time)"
---
Shown below are the sample response returned through our Customers APIs.

```json Customer Response Object
{
  "customer_id": "cust-v1-0811030624-aa-RBDgpR",
  "merchant_customer_reference": "",
  "first_name": "Kevin",
  "last_name": "Bob",
  "country_code": "91",
  "mobile_number": "9876543210",
  "email_id": "kevin.bob@example.com",
  "billing_address": {
    "address1": "10 Downing Street Westminster London",
    "address2": "Oxford Street Westminster London",
    "address3": "Baker Street Westminster London",
    "pincode": "51524036",
    "city": "Westminster",
    "state": "Westminster",
    "country": "London"
  },
  "shipping_address": {
    "address1": "10 Downing Street Westminster London",
    "address2": "Oxford Street Westminster London",
    "address3": "Baker Street Westminster London",
    "pincode": "51524036",
    "city": "Westminster",
    "state": "Westminster",
    "country": "London"
  },
  "gstin": "",
  "merchant_metadata": {
    "key1": "XX",
    "key2": "DOF"
  },
  "status": "INACTIVE",
  "created_at": "2024-10-04T13:11:29.645591Z",
  "updated_at": "2024-10-04T13:11:29.645657Z"
}
```

The table below lists the various parameters returned in the orders response objects.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "customer_id",
    "0-1": "`string`",
    "0-2": "Unique identifier of the customer in the Plural database.<ul><li>Maximum length: 50 characters.</ul></li>Example: `cust-v1-0811030624-aa-RBDgpR`",
    "1-0": "merchant_customer_reference",
    "1-1": "`string`",
    "1-2": "Unique identifier entered while creating a customer.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `82d57572-057c-4826-5775-385a52150554`",
    "2-0": "first_name",
    "2-1": "`string`",
    "2-2": "Customer's first name.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `Kevin`",
    "3-0": "last_name",
    "3-1": "`string`",
    "3-2": "Customer's last name.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `Bob`",
    "4-0": "country_code",
    "4-1": "`string`",
    "4-2": "Country code of the registered mobile number.  \n  \nExample: `91`",
    "5-0": "mobile_number",
    "5-1": "`string`",
    "5-2": "Customer's mobile number.<br><ul><li>Minimum length: `10` character.</li><li>Maximum length: `20` characters.</ul></li>Example: `9876543210`<br><br>Supported characters: <ul><li>`0-9`</ul></li>",
    "6-0": "billing_address",
    "6-1": "`object`",
    "6-2": "An object that contains the details of the billing address.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/customer-object#billing-address-child-object\" >Learn more about the `billing_address` child object.</a>",
    "7-0": "shipping_address",
    "7-1": "`object`",
    "7-2": "An object that contains the shipping address details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/customer-object#shipping-address-child-object\" >Learn more about the `shipping_address` child object.</a>",
    "8-0": "gstin",
    "8-1": "`boolean`",
    "8-2": "Customers unique GSTIN.  \n  \nExample: `28ABCDE1234F2Z6`",
    "9-0": "merchant_metadata",
    "9-1": "`object`",
    "9-2": "An object of key-value pair that can be used to store additional information.  \n  \nExample: `\"key1\": \"DD\"`",
    "10-0": "status",
    "10-1": "`object`",
    "10-2": "Customer status.<br><br>Possible values:<ul><li>`Inactive`: The customer profile is created but not yet activated.</li><li>`Active`: The customer is verified and can use saved tokens for transactions.</li><li>`Suspended`: The customer is temporarily restricted from transactions.</li><li>`Deleted`:  The customer profile is removed and cannot be reactivated.</ul></li>",
    "11-0": "created_at",
    "11-1": "`string`",
    "11-2": "The ISO 8601 UTC Timestamp, when the create customer request was received by Plural.  \n  \nExample: `2024-10-04T13:11:29.645591Z`",
    "12-0": "updated_at",
    "12-1": "`string`",
    "12-2": "The ISO 8601 UTC Timestamp, when the customer object is updated.  \n  \nExample: `2024-10-04T13:11:29.645657Z`"
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


## Billing Address [Child Object]

The table below lists the various parameters in the `billing_address` child object. This is part of the `customer` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "address1",
    "0-1": "`string`",
    "0-2": "Customer's billing address1.<br><ul><li>Maximum length: 100 characters.</ul></li>Example: `10 Downing Street Westminster London`",
    "1-0": "address2",
    "1-1": "`string`",
    "1-2": "Customer's billing address2.<br><ul><li>Maximum length: 100 characters.</ul></li>Example: `Oxford Street Westminster London`",
    "2-0": "address3",
    "2-1": "`string`",
    "2-2": "Customer's billing address3.<br><ul><li>Maximum length: 100 characters.</ul></li>Example: `Baker Street Westminster London`",
    "3-0": "pincode",
    "3-1": "`string`",
    "3-2": "Pincode of the billing address.<ul><li>Minimum length: 6 characters.</li><li>Maximum length: 10 characters.</ul></li>Example: `51524036`<br><br>Supported characters: <ul><li>`0-9`</ul></li>",
    "4-0": "city",
    "4-1": "`string`",
    "4-2": "City of the billing address.<br><ul><li>Maximum length: 50 characters.</ul></li>Example: `Westminster`",
    "5-0": "state",
    "5-1": "`string`",
    "5-2": "State of the billing address.<br><ul><li>Maximum length: 50 characters.</ul></li>Example: `Westminster`",
    "6-0": "country",
    "6-1": "`string`",
    "6-2": "Country of the billing address.<br><ul><li>Maximum length: 50 characters.</ul></li>Example: `London`"
  },
  "cols": 3,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Shipping Address [Child Object]

The table below lists the various parameters in the `shipping_address` child object. This is part of the `customer` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "address1",
    "0-1": "`string`",
    "0-2": "Customer's shipping address1.<br><ul><li>Maximum length: 100 characters.</ul></li>Example: `10 Downing Street Westminster London`",
    "1-0": "address2",
    "1-1": "`string`",
    "1-2": "Customer's shipping address2.<br><ul><li>Maximum length: 100 characters.</ul></li>Example: `Oxford Street Westminster London`",
    "2-0": "address3",
    "2-1": "`string`",
    "2-2": "Customer's shipping address3.<br><ul><li>Maximum length: 100 characters.</ul></li>Example: `Baker Street Westminster London`",
    "3-0": "pincode",
    "3-1": "`string`",
    "3-2": "Pincode of the shipping address.<ul><li>Minimum length: 6 characters.</li><li>Maximum length: 10 characters.</ul></li>Example: `51524036`<br><br>Supported characters: <ul><li>`0-9`</ul></li>",
    "4-0": "city",
    "4-1": "`string`",
    "4-2": "City of the shipping address.<br><ul><li>Maximum length: 50 characters.</ul></li>Example: `Westminster`",
    "5-0": "state",
    "5-1": "`string`",
    "5-2": "State of the shipping address.<br><ul><li>Maximum length: 50 characters.</ul></li>Example: `Westminster`",
    "6-0": "country",
    "6-1": "`string`",
    "6-2": "Country of the shipping address.<br><ul><li>Maximum length: 50 characters.</ul></li>Example: `London`"
  },
  "cols": 3,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]
