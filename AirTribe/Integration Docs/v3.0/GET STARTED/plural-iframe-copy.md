---
title: "Plural iFrame (COPY)"
slug: "plural-iframe-copy"
excerpt: "Learn how to integrate the Plural payment gateway on your website with an embedded iFrame setup."
hidden: true
createdAt: "Fri Nov 08 2024 09:45:31 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Apr 09 2025 14:03:50 GMT+0000 (Coordinated Universal Time)"
---
Plural iFrame Integration is a method of embedding an external web page, service, or content into another webpage using an inline frame (iFrame) HTML element. This integration allows your business to embed a secure payment page directly within your site, enabling your customers to complete seamless transactions without being redirected to another site.

Plural iFrame integration reduces development complexity by minimizing the setup and maintenance requirements of your development team.

Follow the below steps to implement the necessary components to initiate and manage the payment process efficiently.

> 📘 Pre-requisite
> 
> - Ensure you have the Plural Web SDK imported into your website. You can do this, by including the following script tag in your `index.html` file.

<br />

## Offer Validation API

The table below lists the request parameters of our Offer Validation API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "payment_method<sup>`*`</sup>",
    "0-1": "`object`",
    "0-2": "Type of payment method you want to use to accept a payment.  \n  \nAccepted values:<ul><li>`CREDIT_EMI`</li><li>`DEBIT_EMI`</li><li>`CARDLESS_EMI`</ul></li>",
    "1-0": "order_amount<sup>`*`</sup>",
    "1-1": "`object`",
    "1-2": "An object that contains the transaction amount details.  \n  \nLearn more about our `order_amount` child object.",
    "2-0": "payment_amount<sup>`*`</sup>",
    "2-1": "`object`",
    "2-2": "An object that contains the payment amount details after the offer has been applied.  \n  \nLearn more about our `payment_amount` child object.",
    "3-0": "offer_data<sup>`*`</sup>",
    "3-1": "`object`",
    "3-2": "An object that contains details related to the offer.  \n  \nLearn more about our `offer_data` child object.",
    "4-0": "customer_details",
    "4-1": "`object`",
    "4-2": "An object that contains details related to the customer.  \n  \nLearn more about our `customer_details` child object."
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


### Order Amount [Child Object]

The table below lists the various parameters in the `order_amount` child object. This object is part of the `offer validation` sample request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value<sup>`*`</sup>",
    "0-1": "`integer`",
    "0-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`",
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


### Payment Amount [Child Object]

The table below lists the various parameters in the `payment_amount` child object. This object is part of the `offer validation` sample request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value<sup>`*`</sup>",
    "0-1": "`integer`",
    "0-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`",
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


### Offer Data [Child Object]

The table below lists the various parameters in the `offer_data` child object. This object is part of the `offer validation` sample request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "offer_details",
    "0-1": "`object`",
    "0-2": "An object that contains details related to the offer issuer.  \n  \nLearn more about our `offer_details` child object."
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


#### Offer Details [Child Object]

The table below lists the various parameters in the `offer_details` child object. This object is part of the `offer_data` sample request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "id",
    "0-1": "`string`",
    "0-2": "The ID of the Issuer offering the offer.",
    "1-0": "name",
    "1-1": "`string`",
    "1-2": "The name of the Issuer offering the offer.",
    "2-0": "display_name",
    "2-1": "`string`",
    "2-2": "Name of the bank displayed to the user during the payment flow.  \n  \nExample: HDFC BANK",
    "3-0": "issuer_type",
    "3-1": "`string`",
    "3-2": "The type of the Issuer offering the offer.  \n  \nExample:<ul><li>`CC_BANK`</li><li>`DC_BANK`</ul></li>",
    "4-0": "priority",
    "4-1": "`string`",
    "4-2": "The priority of the Issuer offering the offer.",
    "5-0": "tenure",
    "5-1": "`object`",
    "5-2": "The EMI tenure details related to the offer.  \n  \nLearn more about our `tenure` child object."
  },
  "cols": 3,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Tenure [Child Object]

The table below lists the various parameters in the `tenures` object. This is part of the `offer_details` request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "tenure_id",
    "0-1": "`String`",
    "0-2": "Tenure id in the Plural database.  \n  \nExample: `1`",
    "1-0": "name",
    "1-1": "`String`",
    "1-2": "The name of the Issuer offering the offer..  \n  \nExample: `3 Months`",
    "2-0": "tenure_type",
    "2-1": "`String`",
    "2-2": "The type of the Tenure.  \n  \nAccepted values: <ul><li>`MONTH`</ul></li>.",
    "3-0": "tenure_value",
    "3-1": "`integer`",
    "3-2": "The value of the tenure.  \n  \nExample: `3`",
    "4-0": "issuer_offer_parameters",
    "4-1": "`array of objects`",
    "4-2": "An array of objects that contains the `issuer_offer_parameters` details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#issuer-offer-parameters-child-object\" >Learn more about the `issuer_offer_parameters` child object.</a>",
    "5-0": "details",
    "5-1": "`array of objects`",
    "5-2": "An array of objects that contains the `product details`.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#details-child-object\" >Learn more about the `details` child object.</a>",
    "6-0": "discount",
    "6-1": "`object`",
    "6-2": "An object that contains the discount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#discount-child-object\" >Learn more about the `discount` child object.</a>",
    "7-0": "loan_amount",
    "7-1": "`object`",
    "7-2": "An object that contains the loan amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#loan-amount-child-object\" >Learn more about the `loan_amount` child object.</a>",
    "8-0": "total_discount_amount",
    "8-1": "`object`",
    "8-2": "An object that contains the total discount amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#total-discount-amount-child-object\" >Learn more about the `total_discount_amount` child object.</a>",
    "9-0": "net_payment_amount",
    "9-1": "`object`",
    "9-2": "An object that contains the net payment amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#net-payment-amount-child-object\" >Learn more about the `net_payment_amount` child object.</a>",
    "10-0": "monthly_emi_amount",
    "10-1": "`object`",
    "10-2": "An object that contains the monthly EMI amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#monthly-emi-amount-child-object\" >Learn more about the `monthly_emi_amount` child object.</a>",
    "11-0": "total_emi_amount",
    "11-1": "`object`",
    "11-2": "An object that contains the total EMI amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#total-emi-amount-child-object\" >Learn more about the `total_emi_amount` child object.</a>",
    "12-0": "interest_amount",
    "12-1": "`object`",
    "12-2": "An object that contains the interest amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#interest-amount-child-object\" >Learn more about the `interest_amount` child object.</a>",
    "13-0": "total_subvention_amount",
    "13-1": "`object`",
    "13-2": "An object that contains the total subvention amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#total-subvention-amount-child-object\" >Learn more about the `total_subvention_amount` child object.</a>",
    "14-0": "interest_rate_percentage",
    "14-1": "`float`",
    "14-2": "Interest rate percentage for the tenure.  \n  \nExample: `16.90`",
    "15-0": "processing_fee_details",
    "15-1": "`object`",
    "15-2": "An object that contains the processing fee details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#processing-fee-details-child-object\" >Learn more about the `processing_fee_details` child object.</a>",
    "16-0": "emi_type",
    "16-1": "`strings`",
    "16-2": "Type of EMI.  \n  \nExample: `STANDARD`  \n  \nAccepted values: <ul><li>`LOW_COST`</li><li>`NO_COST`</li><li>`STANDARD`</ul></li>"
  },
  "cols": 3,
  "rows": 17,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Issuer Offer Parameters [Child Object]

The table below lists the various parameters in the `issuer_offer_parameters` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "program_type",
    "0-1": "`String`",
    "0-2": "Unique identifier of the issuer id in the Plural database.  \n  \nExample: `23`",
    "1-0": "offer_id",
    "1-1": "`String`",
    "1-2": "Name of the Issuer.  \n  \nExample: `INDUSIND CC`",
    "2-0": "offer_parameter_id",
    "2-1": "`String`",
    "2-2": "The type of the Issuer offering the offer.  \n  \nAccepted values: <ul><li>`Credit`</li><li>`Debit`</li><li>`Cardless`</li><li>`NBFC`</ul></li>."
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


#### Details [Child Object]

The table below lists the various parameters in the `details` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "product_code",
    "0-1": "`String`",
    "0-2": "Unique Product identifier of the product.  \n  \nExample: `redmi_1`",
    "1-0": "brand_id",
    "1-1": "`String`",
    "1-2": "Unique brand identifier of the product.  \n  \nExample: `3`",
    "2-0": "product_offer_parameters",
    "2-1": "`array of objects`",
    "2-2": "An array of objects that contains the product offer schemes for the product EMI details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#product-offer-parameters-child-object\" >Learn more about the `product_offer_parameters` child object.</a>",
    "3-0": "product_amount",
    "3-1": "`object`",
    "3-2": "An object that contains the product amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#product-amount-child-object\" >Learn more about the `product_amount` child object.</a>",
    "4-0": "subvention",
    "4-1": "`object`",
    "4-2": "An object that contains the subvention details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#subvention-child-object\" >Learn more about the `subvention` child object.</a>",
    "5-0": "discount",
    "5-1": "`object`",
    "5-2": "An object that contains the product discount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#discount-child-object\" >Learn more about the `discount` child object.</a>"
  },
  "cols": 3,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Product Offer Parameters [Child Object]

The table below lists the various parameters in the `product_offer_parameters` child object. This is part of the `details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "program_type",
    "0-1": "`String`",
    "0-2": "Type of the Program.  \n  \nExample: `BRAND_EMI`  \n  \nAccepted values: <ul><li>`BRAND_EMI`</li><li>`BANK_EMI`</li><li>`MERCHANT_BRAND_OFFER`</li><li>`MERCHANT_BANK_OFFER`</li><li>`BRAND_OFFER`</li><li>`MY_EMI`</ul></li>",
    "1-0": "offer_id",
    "1-1": "`string`",
    "1-2": "Unique identifier of the offer.  \n  \nExample: `309`",
    "2-0": "offer_parameter_id",
    "2-1": "`string`",
    "2-2": "Unique offer parameter identifier.  \n  \nExample: `20` "
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


##### Product Amount [Child Object]

The table below lists the various parameters in the `product_amount` child object. This is part of the `details` object.

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


##### Subvention [Child Object]

The table below lists the various parameters in the `subvention` child object. This is part of the `details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "subvention_type",
    "0-1": "`String`",
    "0-2": "Type of subvention.  \n  \nExample: `INSTANT`  \n  \nAccepted values:<ul><li>`INSTANT`</li><li>`POST`</ul></li>",
    "1-0": "offer_type",
    "1-1": "`string`",
    "1-2": "Type of the offer.  \n  \nAccepted values: <ul><li>`LOW_COST`</li><li>`NO_COST`</li><li>`STANDARD`</ul></li>",
    "2-0": "percentage",
    "2-1": "`integer`",
    "2-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`",
    "3-0": "amount",
    "3-1": "`object`",
    "3-2": "An object that contains the subvention amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object\" >Learn more about the `amount` child object.</a>",
    "4-0": "breakup",
    "4-1": "`object`",
    "4-2": "An object that contains the subvention breakup details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#breakup-child-object\" >Learn more about the `breakup` child object.</a>"
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


###### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `subvention` object.

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


###### Breakup [Child Object]

The table below lists the various parameters in the `breakup` child object. This is part of the `subvention` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "brand",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup details of the brand.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#brand-child-object\" >Learn more about the `brand` child object.</a>"
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


###### Brand [Child Object]

The table below lists the various parameters in the `brand` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup amount details of the brand.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object-1\" >Learn more about the `amount` child object.</a>"
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


###### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `brand` object.

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


#### Discount [Child Object]

The table below lists the various parameters in the `discount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "discount_type",
    "0-1": "`String`",
    "0-2": "Type of discount.  \n  \nPossible values:<ul><li>`INSTANT`</li><li>`DEFERRED`</ul></li>",
    "1-0": "percentage",
    "1-1": "`Double`",
    "1-2": "The discount percentage provided by the offering entity.  \n  \nExample: `16.90`",
    "2-0": "amount",
    "2-1": "`string`",
    "2-2": "Discount amount.  \n  \nExample: `2000`",
    "3-0": "discount_deferred_duration_value",
    "3-1": "`integer`",
    "3-2": "The duration value for the deferred discount.  \n  \nExample: ",
    "4-0": "discount_deferred_duration_type",
    "4-1": "`string`",
    "4-2": "Discount duration type deferred.  \n  \nPossible values: <ul><li>`DAY`</li><li>`MONTH`</ul></li>",
    "5-0": "breakup",
    "5-1": "`object`",
    "5-2": "An object that contains the product offer details with breakup.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#breakup-child-object-1\" >Learn more about the `breakup` child object.</a>"
  },
  "cols": 3,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Breakup [Child Object]

The table below lists the various parameters in the `breakup` child object. This is part of the `discount` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant",
    "0-1": "`object`",
    "0-2": "An object that contains the merchant breakup details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#merchant-child-object\" >Learn more about the `breakup` child object.</a>",
    "1-0": "issuer",
    "1-1": "`object`",
    "1-2": "An object that contains the issure breakup details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#issuer-child-object\" >Learn more about the `breakup` child object.</a>",
    "2-0": "brand",
    "2-1": "`object`",
    "2-2": "An object that contains the brand breakup details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#brand-child-object-1\" >Learn more about the `breakup` child object.</a>",
    "3-0": "dealer",
    "3-1": "`object`",
    "3-2": "An object that contains the dealer breakup details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#dealer-child-object\" >Learn more about the `breakup` child object.</a>"
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


###### Merchant [Child Object]

The table below lists the various parameters in the `merchant` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object-2\" >Learn more about the amount child object.</a>"
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


###### Issuer [Child Object]

The table below lists the various parameters in the `issure` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object-2\" >Learn more about the amount child object.</a>"
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


###### Brand [Child Object]

The table below lists the various parameters in the `brand` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object-2\" >Learn more about the amount child object.</a>"
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


###### Dealer [Child Object]

The table below lists the various parameters in the `dealer` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object-2\" >Learn more about the amount child object.</a>"
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


#### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `breakup` object.

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


#### Loan Amount [Child Object]

The table below lists the various parameters in the `loan_amount` child object. This is part of the `tenures` object.

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


#### Total Discount Amount [Child Object]

The table below lists the various parameters in the `total_discount_amount` child object. This is part of the `tenures` object.

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


#### Net Payment Amount [Child Object]

The table below lists the various parameters in the `net_payment_amount` child object. This is part of the `tenures` object.

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


#### Monthly EMI Amount [Child Object]

The table below lists the various parameters in the `monthly_emi_amount` child object. This is part of the `tenures` object.

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


#### Total EMI Amount [Child Object]

The table below lists the various parameters in the `total_emi_amount` child object. This is part of the `tenures` object.

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


#### Interest Amount [Child Object]

The table below lists the various parameters in the `interest_amount` child object. This is part of the `tenures` object.

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


#### Total Subvention Amount [Child Object]

The table below lists the various parameters in the `total_subvention_amount` child object. This is part of the `tenures` object.

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


#### Processing Fee Details [Child Object]

The table below lists the various parameters in the `processing_fee_details` child object. This is part of the `tenures` object.

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


### Issuer Data [Child Object]

The table below lists the various parameters in the `issure_data` object. This is part of the offer discovery response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "otp_length",
    "0-1": "`integer`",
    "0-2": "Length of the OTP.  \n  \nExample: `4`",
    "1-0": "otp_time_in_sec",
    "1-1": "`integer`",
    "1-2": "OTP validity time in seconds.  \n  \nExample: `120`",
    "2-0": "otp_retry_count",
    "2-1": "`integer`",
    "2-2": "Maximum OTP retry count.  \n  \nExample:",
    "3-0": "is_consent_page_required",
    "3-1": "`Boolean`",
    "3-2": "Status of the required consent page.<ul><li>`true`: When the consent page is required.</li><li>`false`: When the consent page is not required.</ul></li>",
    "4-0": "consent_data",
    "4-1": "`String`",
    "4-2": "Transaction consent data.  \n  \nExample: ",
    "5-0": "terms_and_conditions",
    "5-1": "`String`",
    "5-2": "Transaction terms and conditions.  \n  \nExample: ",
    "6-0": "show_key_fact_statement",
    "6-1": "`Boolean`",
    "6-2": "Key fact statement status.<ul><li>`true`: When the key fact statement need to be displayed.</li><li>`false`: When the key fact statement is not required to be displayed.</ul></li>",
    "7-0": "auth_type",
    "7-1": "`String`",
    "7-2": "Authentication type.  \n  \nAccepted values: <ul><li>`PENNY_DROP`</li><li>`OTP`</ul></li>",
    "8-0": "penny_transaction_amount",
    "8-1": "`string`",
    "8-2": "Applicable amount for penny transaction.  \n  \nExample: `100`",
    "9-0": "is_tokenized_transaction_supported",
    "9-1": "`Boolean`",
    "9-2": "Tokenized transactions support status.<ul><li>`true`: Tokenized transaction is supported.</li><li>`false`: Tokenized transaction is not supported.</ul></li>",
    "10-0": "pan_number_last_digit_count",
    "10-1": "`String`",
    "10-2": "Last digit count of PAN.",
    "11-0": "offer_validation_parameters_required",
    "11-1": "`String`",
    "11-2": "Parameters required in offer validation API."
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
