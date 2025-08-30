---
title: "Object"
slug: "pay-by-links-object"
excerpt: "Overview of the Pay by Link APIs response."
hidden: false
createdAt: "Tue Mar 18 2025 05:55:38 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri May 02 2025 07:57:08 GMT+0000 (Coordinated Universal Time)"
---
Shown below is a sample response returned through our Create Payment Link API.

```json Create Payment Link Response Object
{
  "payment_link": "https://shortener.v2.pinepg.in/PLUTUS/3rh4jtd",
  "payment_link_id": "pl-v1-250306082755-aa-uT0noy",
  "status": "CREATED",
  "amount": {
    "value": 100,
    "currency": "INR"
  },
  "amount_due": {
    "value": 100,
    "currency": "INR"
  },
  "order_id": "v1-250131113650-aa-TUzeRY",
  "merchant_payment_link_reference": "link_ref",
  "description": "Payment for order #12345",
  "expire_by": "2025-03-21T08:29Z",
  "allowed_payment_methods": [
    "NETBANKING"
  ],
  "customer": {
    "email_id": "kevin.bob@example.com",
    "first_name": "Kevin",
    "last_name": "Bob",
    "customer_id": "123456",
    "mobile_number": "9876543210",
    "country_code": "91",
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
    }
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
        "value": 0
      }
    }
  ],
  "cart_coupon_discount_amount": {
    "currency": "INR",
    "value": 0
  },
  "merchant_metadata": {
    "clientId": "DD",
    "transactionReferenceNo": "pine-1223",
    "merchantId": "1234",
    "tid": "9000990",
    "acquirerName": "HDFC_FSS",
    "isOfferDisplayRequired": "true",
    "OfferData": "UHJvZHVjdF9Db2RlPSIgIiZQcm9kdWN0X05hbWU9IiImUGF5bWVudF9Nb2RlPUJhbmsgRU1JJkNhcmRfVHlwZT1EZWJpdCBDYXJkJkJhbmtfTmFtZT1IREZDIERlYml0JkVNSV9UZW51cmU9NiZJbnRlcmVzdF9SYXRlPTkuMCZJbnRlcmVzdF9BbW91bnQ9MTM4MTQwJk1vbnRobHlfSW5zdGFsbWVudD04OTQ2OTAmQXV0aG9yaXphdGlvbl9BbW91bnQ9MTAwJkxvYW5fYm9va2luZ19BbW91bnQ9NTIzMDAwMCZJbnRlcmVzdF9DYXNoYmFja19BbW91bnQ9MCZJbnRlcmVzdF9DYXNoYmFja19UeXBlPURlZmVycmVkJkFkZGl0aW9uYWxfQ2FzaGJhY2s9IiImQWRkaXRpb25hbF9DYXNoYmFja19UeXBlPSIiJkRlc2NyaXB0aW9uPUJhbmsgRU1JJlByb2R1Y3RfVmFsdWU9NTIzMDAwMA",
    "tenant_id": "PGATPOS",
    "is_offer_validation_required": "true"
  },
  "created_at": "2025-03-06T08:27:55.881Z",
  "updated_at": "2025-03-06T08:27:55.881Z"
}
```

The table below lists the various parameters returned in our Create Payment Link API response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "payment_link",
    "0-1": "`string`",
    "0-2": "Payment link.  \n  \nExample: `https://shortener.v2.pinepg.in/PLUTUS/3rh4jtd`",
    "1-0": "payment_link_id",
    "1-1": "`string`",
    "1-2": "Unique identifier of the order in the Plural database.<ul><li>Maximum length: `50` characters.</ul></li>Example: `pl-v1-250306082755-aa-uT0noy`",
    "2-0": "status",
    "2-1": "`string`",
    "2-2": "Payment link status.  \n  \nPossible values:<ul><li>`CREATED`: When the create payment link request is successfully received by Plural. The payment link has been created and shared with the customer.</li><li>`CLICKED`: The customer has clicked on the payment link to initiate a payment.</li><li>`PAYMENT_INITIATED`: The customer has successfully accessed the payment link and completed the payment. We have submitted the payment request to the bank, waiting for the bank's confirmation.</li><li>`PROCESSED`: The payment is successfully processed. Here the money is debited from your customer account and credited to your account.</li><li>`PARTIAL_PROCESSED`: The partial payment is successfully processed. Here the money is debited from your customer account and credited to your account.</li><li>`EXPIRED`: The payment link has expired.</li><li>`CANCELLED`: The payment link is canelled.</li></ul>",
    "3-0": "amount",
    "3-1": "`object`",
    "3-2": "An object that contains the payment amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/pay-by-links-object#amount-child-object\" >Learn more about the `amount` child object</a>.",
    "4-0": "amount_due",
    "4-1": "`object`",
    "4-2": "An object that contains the payment amount due details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/pay-by-links-object#amount-due-child-object\" >Learn more about the `amount_due` child object</a>.",
    "5-0": "order_id",
    "5-1": "`string`",
    "5-2": "Unique identifier of the order in the Plural database.  \n  \nExample: `v1-250131113650-aa-TUzeRY`",
    "6-0": "merchant_payment_link_reference",
    "6-1": "`string`",
    "6-2": "Unique identifier entered while creating a payment link.<ul><li>Minimum length: `1` character.</li><li>Maximum length: `50` characters.</ul></li>Example: `link_ref`",
    "7-0": "description",
    "7-1": "`string`",
    "7-2": "Corresponding message against the payment link.  \n  \nExample: `Order Payment Link`",
    "8-0": "expire_by",
    "8-1": "`string`",
    "8-2": "Timestamp when the payment link get expired.  \n  \nExample: `2024-04-30T08:01:32Z`",
    "9-0": "allowed_payment_methods",
    "9-1": "`array of strings`",
    "9-2": "The type of payment methods you want to offer your customers to accept payments.  \n  \nAccepted values:<ul><li>`CARD`</li><li>`UPI`</li><li>`POINTS`</li><li>`NETBANKING`</li><li>`WALLET`</li><li>`CREDIT_EMI`</li><li>`DEBIT_EMI`</ul></li>Example: CARD  \n  \n**Note**: Before selecting a payment method, ensure it is configured for you.",
    "10-0": "customer",
    "10-1": "`object`",
    "10-2": "An object that contains the customer information details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/pay-by-links-object#customer-child-object\" >Learn more about the `customer` child object</a>.",
    "11-0": "product_details",
    "11-1": "`array of objects`",
    "11-2": "An array of objects, that contains the list of products associated with the payment details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/pay-by-links-object#product-details-child-object\" >Learn more about the `product_details` child object</a>.",
    "12-0": "cart_coupon_discount_amount",
    "12-1": "`object`",
    "12-2": "An object that contains the cart coupon discount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/pay-by-links-object#cart-coupon-discount-amount-child-object\" >Learn more about the `cart_coupon_discount_amount` child object</a>.",
    "13-0": "merchant_metadata",
    "13-1": "`object`",
    "13-2": "An object of key-value pair that can be used to store additional information.  \n  \nExample: `\"key1\": \"DD\"`",
    "14-0": "created_at",
    "14-1": "`string`",
    "14-2": "The ISO 8601 UTC Timestamp, when the create payment link request was received by Plural.  \n  \nExample: `2024-07-09T07:57:08.022Z`",
    "15-0": "updated_at",
    "15-1": "`string`",
    "15-2": "The ISO 8601 UTC Timestamp, when the create payment link response object is updated.  \n  \nExample: `2024-07-09T07:57:08.022Z`"
  },
  "cols": 3,
  "rows": 16,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This object is part of the `Create Payment Link API` response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
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


### Amount Due [Child Object]

The table below lists the various parameters in the `amount_due` child object. This object is part of the `Create Payment Link API` response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
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


### Customer [Child Object]

The table below lists the various parameters in the `customer` child object. This object is part of the `Create Payment Link API` response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "email_id",
    "0-1": "`string`",
    "0-2": "Customer's email address.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `kevin.bob@example.com`",
    "1-0": "first_name",
    "1-1": "`string`",
    "1-2": "Customer's first name.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `Kevin`",
    "2-0": "last_name",
    "2-1": "`string`",
    "2-2": "Customer's last name.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 50 characters.</ul></li>Example: `Bob`",
    "3-0": "customer_id",
    "3-1": "`string`",
    "3-2": "Unique identifier of the customer in the Plural database.<br><ul><li>Minimum length: 1 character.</li><li>Maximum length: 19 characters.</ul></li>Example: `123456`",
    "4-0": "mobile_number",
    "4-1": "`string`",
    "4-2": "Customer's mobile number.<br><ul><li>Minimum length: `10` character.</li><li>Maximum length: `20` characters.</ul></li>Example: `9876543210`<br><br>Supported characters: <ul><li>`0-9`</ul></li>",
    "5-0": "country_code",
    "5-1": "`string`",
    "5-2": "Country code of the mobile number.  \n  \nExample: `91`",
    "6-0": "billing_address",
    "6-1": "`object`",
    "6-2": "An object that contains the details of the billing address.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/pay-by-links-object#billing-address-child-object\" >Learn more about the `billing_address` child object.</a>",
    "7-0": "shipping_address",
    "7-1": "`object`",
    "7-2": "An object that contains the shipping address details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/reference/pay-by-links-object#shipping-address-child-object\" >Learn more about the `shipping_address` child object.</a>",
    "8-0": "merchant_customer_reference",
    "8-1": "`string`",
    "8-2": "Unique identifier of the customer for the request.<ul><li>Minimum length: `1` character.</li><li>Maximum length: `50` characters.</ul></li>Example: `customer_reference`",
    "9-0": "gstin",
    "9-1": "`string`",
    "9-2": "Customers GSTIN.  \n  \nExample: `27AAEPM1234C1Z5`"
  },
  "cols": 3,
  "rows": 10,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Billing Address [Child Object]

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


#### Shipping Address [Child Object]

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


### Product Details [Child Object]

The table below lists the various parameters in the `product_details` child object. This object is part of the `Create Payment Link API` response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "product_code",
    "0-1": "`string`",
    "0-2": "Unique Product identifier of the product.  \n  \nExample: `redmi_10`",
    "1-0": "product_amount",
    "1-1": "`object`",
    "1-2": "An object that contains the product amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/pay-by-links-object#product-amount-child-object\" >Learn more about the `product_amount` child object</a>.",
    "2-0": "product_coupon_discount_amount",
    "2-1": "`object`",
    "2-2": "An object that contains the product coupon discount amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/pay-by-links-object#product-coupon-discount-amount-child-object\" >Learn more about the `product_coupon_discount_amount` child object</a>."
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


#### Product Amount [Child Object]

The table below lists the various parameters in the `product_amount` child object. This object is part of the `product_details` response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
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


#### Product Coupon Discount Amount [Child Object]

The table below lists the various parameters in the `product_coupon_discount_amount` child object. This object is part of the `product_details` response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
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


### Cart Coupon Discount Amount [Child Object]

The table below lists the various parameters in the `cart_coupon_discount_amount` child object. This object is part of the `Create Payment Link API` response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
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
