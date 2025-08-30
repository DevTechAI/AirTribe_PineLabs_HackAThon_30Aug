---
title: "Request Tables"
slug: "request-tables"
excerpt: ""
hidden: true
createdAt: "Fri Feb 28 2025 10:36:39 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Apr 14 2025 07:48:51 GMT+0000 (Coordinated Universal Time)"
---
## Offer Discovery Bank EMI

The table below lists the request parameters of our Offer Discovery API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "order_amount<sup>`*`</sup>",
    "0-1": "`object`",
    "0-2": "An object that contains the transaction amount details.  \n  \nLearn more about our `order_amount` child object."
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


## Offer Discovery Brand EMI

The table below lists the request parameters of our Offer Discovery API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "order_amount<sup>`*`</sup>",
    "0-1": "`object`",
    "0-2": "An object that contains the transaction amount details.  \n  \nLearn more about our `order_amount` child object.",
    "1-0": "product_details",
    "1-1": "`object`",
    "1-2": "**Mandatory for Brand EMI**  \n  \nAn object that contains product details.  \n  \nLearn more about our `product_details` child object.",
    "2-0": "cart_coupon_discount_amount",
    "2-1": "`string`",
    "2-2": "An object that contains the cart coupon discount details.  \n  \nLearn more about our `cart_coupon_discount_amount` child object."
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


### Order Amount [Child Object]

The table below lists the various parameters in the `order_amount` child object. This object is part of the `offer Discovery Brand EMI` sample request object.

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


### Product Details [Child Object]

The table below lists the various parameters in the `product_details` child object. This is part of the `offer Discovery Brand EMI` sample request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "product_code",
    "0-1": "`String`",
    "0-2": "Unique Product identifier of the product.  \n  \nExample: `redmi_1`",
    "1-0": "product_amount",
    "1-1": "`object`",
    "1-2": "An object that contains the product amount details.  \n  \nLearn more about the `product_amount` child object.",
    "2-0": "product_coupon_discount_amount",
    "2-1": "`object`",
    "2-2": "An object that contains the product coupon discount details.  \n  \nLearn more about the `product_coupon_discount_amount` child object."
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

The table below lists the various parameters in the `product_amount` child object. This object is part of the `product_details`object.

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


#### Product Coupon Discount Amount [Child Object]

The table below lists the various parameters in the `product_coupon_discount_amount` child object. This object is part of the `product_details`object.

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


### Cart Coupon Discount Amount [Child Object]

The table below lists the various parameters in the `cart_coupon_discount_amount` child object. This object is part of the `offer Discovery Brand EMI` sample request object.

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
    "2-0": "issuer_type",
    "2-1": "`string`",
    "2-2": "The type of the Issuer offering the offer.  \n  \nExample:<ul><li>`CC_BANK`</li><li>`DC_BANK`</ul></li>",
    "3-0": "priority",
    "3-1": "`string`",
    "3-2": "The priority of the Issuer offering the offer.",
    "4-0": "tenure",
    "4-1": "`object`",
    "4-2": "The EMI tenure details related to the offer.  \n  \nLearn more about our `tenure` child object."
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


#### Tenure [Child Object]

The table below lists the various parameters in the `tenures` object. This is part of the `offer_details` request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "tenure_id<sup>`*`</sup>",
    "0-1": "`String`",
    "0-2": "Tenure id in the Plural database.  \n  \nExample: `1`",
    "1-0": "name<sup>`*`</sup>",
    "1-1": "`String`",
    "1-2": "The name of the Issuer offering the offer..  \n  \nExample: `3 Months`",
    "2-0": "tenure_type<sup>`*`</sup>",
    "2-1": "`String`",
    "2-2": "The type of the Tenure.  \n  \nAccepted values: <ul><li>`MONTH`</ul></li>.",
    "3-0": "tenure_value",
    "3-1": "`integer`",
    "3-2": "The value of the tenure.  \n  \nExample: `3`",
    "4-0": "issuer_offer_parameters<sup>`*`</sup>",
    "4-1": "`string`",
    "4-2": "List of Offer Schemes for the tenure.",
    "5-0": "details",
    "5-1": "`array of objects`",
    "5-2": "An array of objects that contains the `product details`.  \n  \nLearn more about the `details` child object.</a>",
    "6-0": "discount",
    "6-1": "`object`",
    "6-2": "An object that contains the discount details.  \n  \nLearn more about the `discount` child object.</a>",
    "7-0": "loan_amount",
    "7-1": "`object`",
    "7-2": "An object that contains the loan amount details.  \n  \nLearn more about the `loan_amount` child object.</a>",
    "8-0": "total_discount_amount",
    "8-1": "`object`",
    "8-2": "Total discount amount for the tenure.  \n  \nLearn more about the `total_discount_amount` child object.</a>",
    "9-0": "net_payment_amount",
    "9-1": "`object`",
    "9-2": "An object that contains the net payment amount details.  \n  \nLearn more about the `net_payment_amount` child object.</a>",
    "10-0": "monthly_emi_amount",
    "10-1": "`object`",
    "10-2": "An object that contains the monthly EMI amount details.  \n  \nLearn more about the `monthly_emi_amount` child object.</a>",
    "11-0": "total_emi_amount",
    "11-1": "`object`",
    "11-2": "An object that contains the total EMI amount details.  \n  \nLearn more about the `total_emi_amount` child object.</a>",
    "12-0": "interest_amount",
    "12-1": "`object`",
    "12-2": "An object that contains the interest amount details.  \n  \nLearn more about the `interest_amount` child object.</a>",
    "13-0": "total_subvention_amount",
    "13-1": "`object`",
    "13-2": "An object that contains the total subvention amount details.  \n  \nLearn more about the `total_subvention_amount` child object.</a>",
    "14-0": "interest_rate_percentage<sup>`*`</sup>",
    "14-1": "`integer`",
    "14-2": "Interest rate percentage for the tenure.",
    "15-0": "processing_fee_details",
    "15-1": "`object`",
    "15-2": "Processing fee details for the tenure.  \n  \nLearn more about the `processing_fee_details` child object.</a>",
    "16-0": "emi_type<sup>`*`</sup>",
    "16-1": "`strings`",
    "16-2": "Type of EMI.  \n  \nExample: `STANDARD`  \n  \nAccepted values: <ul><li>`LOW_COST`</li><li>`NO_COST`</li><li>`STANDARD`</ul></li>",
    "17-0": "convenience_fee_breakdown",
    "17-1": "`object`",
    "17-2": "An object that contains the convenience fee breakdown details.  \n  \nLearn more about the `convenience_fee_breakdown` child object.</a>",
    "18-0": "cart_coupon_discount_amount",
    "18-1": "`object`",
    "18-2": "An object that contains the cart coupon discount amount details.  \n  \nLearn more about the `cart_coupon_discount_amount` child object.</a>",
    "19-0": "total_coupon_discount",
    "19-1": "`object`",
    "19-2": "An object that contains the total coupon discount details.  \n  \nLearn more about the `total_coupon_discount` child object.</a>"
  },
  "cols": 3,
  "rows": 20,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


<br />

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
    "1-0": "product_display_name",
    "1-1": "`String`",
    "1-2": "Name of the Product.  \n  \nExample: Oneplus 13R",
    "2-0": "brand_id",
    "2-1": "`String`",
    "2-2": "Unique brand identifier of the product.  \n  \nExample: `3`",
    "3-0": "product_offer_parameters",
    "3-1": "`array of objects`",
    "3-2": "An array of objects that contains the product offer schemes for the product EMI details.  \n  \nLearn more about the `product_offer_parameters` child object.</a>",
    "4-0": "product_amount",
    "4-1": "`object`",
    "4-2": "An object that contains the product amount details.  \n  \nLearn more about the `product_amount` child object.</a>",
    "5-0": "product_coupon_discount_amount",
    "5-1": "`object`",
    "5-2": "An object that contains the product coupon discount amount details.  \n  \nLearn more about the `product_coupon_discount_amount` child object.</a>",
    "6-0": "subvention",
    "6-1": "`object`",
    "6-2": "An object that contains the subvention details.  \n  \nLearn more about the `subvention` child object.</a>",
    "7-0": "discount",
    "7-1": "`object`",
    "7-2": "An object that contains the product discount details.  \n  \nLearn more about the `discount` child object.</a>",
    "8-0": "brand_name",
    "8-1": "`string`",
    "8-2": "Name of the Brand.  \n  \nExample: Oneplus",
    "9-0": "interest_amount",
    "9-1": "`object`",
    "9-2": "An object that contains the interest amount details.  \n  \nLearn more about the `interest_amount` child object.</a>",
    "10-0": "interest_rate",
    "10-1": "`string`",
    "10-2": "Rate of interest applied on the product.  \n  \nExample: 19",
    "11-0": "cart_coupon_discount_product_share",
    "11-1": "`object`",
    "11-2": "An object that contains the cart coupon discount product share details.  \n  \nLearn more about the `cart_coupon_discount_product_share` child object.</a>"
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
    "0-0": "value<sup>`*`</sup>",
    "0-1": "`integer`",
    "0-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`",
    "1-0": "currency<sup>`*`</sup>",
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


##### Product Coupon Discount Amount [Child Object]

The table below lists the various parameters in the `product_coupon_discount_amount` child object. This is part of the `details` object.

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
    "1-0": "percentage",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`",
    "2-0": "amount",
    "2-1": "`object`",
    "2-2": "An object that contains the subvention amount details.  \n  \nLearn more about the `amount` child object.</a>",
    "3-0": "breakup",
    "3-1": "`object`",
    "3-2": "An object that contains the subvention breakup details.  \n  \nLearn more about the `breakup` child object.</a>",
    "4-0": "max_amount",
    "4-1": "`object`",
    "4-2": "An object that contains the maximum subvention amount details.  \n  \nLearn more about the `max_amount` child object.</a>",
    "5-0": "min_amount",
    "5-1": "`object`",
    "5-2": "An object that contains the minimum subvention amount details.  \n  \nLearn more about the `min_amount` child object.</a>"
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


###### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `subvention` object.

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
    "0-2": "An object that contains the breakup details of the brand.  \n  \nLearn more about the `brand` child object.</a>",
    "1-0": "merchant",
    "1-1": "`object`",
    "1-2": "An object that contains the breakup details of the merchant.  \n  \nLearn more about the `merchant` child object.</a>",
    "2-0": "issuer",
    "2-1": "`object`",
    "2-2": "An object that contains the breakup details of the issuer.  \n  \nLearn more about the `issuer` child object.</a>",
    "3-0": "dealer",
    "3-1": "`object`",
    "3-2": "An object that contains the breakup details of the dealer.  \n  \nLearn more about the `dealer` child object.</a>"
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
    "0-2": "An object that contains the breakup amount details of the brand.  \n  \nLearn more about the `amount` child object.</a>"
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
    "0-0": "value<sup>`*`</sup>",
    "0-1": "`integer`",
    "0-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`",
    "1-0": "currency<sup>`*`</sup>",
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
    "0-2": "An object that contains the breakup details of the merchant.  \n  \nLearn more about the `amount` child object.</a>"
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

The table below lists the various parameters in the `amount` child object. This is part of the `merchant` object.

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


###### Issuer [Child Object]

The table below lists the various parameters in the `issuer` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup details of the issuer.  \n  \nLearn more about the `amount` child object.</a>"
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

The table below lists the various parameters in the `amount` child object. This is part of the `issuer` object.

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
    "0-2": "An object that contains the breakup details of the dealer.  \n  \nLearn more about the `amount` child object.</a>"
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

The table below lists the various parameters in the `amount` child object. This is part of the `issuer` object.

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


###### Maximum Amount [Child Object]

The table below lists the various parameters in the `max_amount` child object. This is part of the `subvention` object.

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


###### Minimum Amount [Child Object]

The table below lists the various parameters in the `min_amount` child object. This is part of the `subvention` object.

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
    "1-0": "discount_string",
    "1-1": "`String`",
    "1-2": "The additional discount provided by the offering entity after a specific period.  \n  \nExample: 1000",
    "2-0": "percentage",
    "2-1": "`Double`",
    "2-2": "The discount percentage provided by the offering entity.  \n  \nExample: `16.90`",
    "3-0": "amount",
    "3-1": "`string`",
    "3-2": "Discount amount.  \n  \nExample: `2000`",
    "4-0": "max_amount",
    "4-1": "`object`",
    "4-2": "An object that contains the maximum discount amount details.  \n  \nLearn more about the `max_amount` child object.</a>",
    "5-0": "min_amount",
    "5-1": "`object`",
    "5-2": "An object that contains the minimum discount amount details.  \n  \nLearn more about the `min_amount` child object.</a>",
    "6-0": "discount_deferred_duration_value",
    "6-1": "`integer`",
    "6-2": "The duration value for the deferred discount.  \n  \nExample: ",
    "7-0": "discount_deferred_duration_type",
    "7-1": "`string`",
    "7-2": "Discount duration type deferred.  \n  \nPossible values: <ul><li>`DAY`</li><li>`MONTH`</ul></li>",
    "8-0": "breakup",
    "8-1": "`object`",
    "8-2": "An object that contains the product offer details with breakup.  \n  \nLearn more about the `breakup` child object.</a>"
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


###### Maximum Amount [Child Object]

The table below lists the various parameters in the `max_amount` child object. This is part of the `discount` object.

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


###### Minimum Amount [Child Object]

The table below lists the various parameters in the `min_amount` child object. This is part of the `discount` object.

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


##### Breakup [Child Object]

The table below lists the various parameters in the `breakup` child object. This is part of the `discount` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "brand",
    "0-1": "`object`",
    "0-2": "An object that contains the brand breakup details.  \n  \nLearn more about the `brand` child object.</a>",
    "1-0": "merchant",
    "1-1": "`object`",
    "1-2": "An object that contains the merchant breakup details.  \n  \nLearn more about the `merchant` child object.</a>",
    "2-0": "issuer",
    "2-1": "`object`",
    "2-2": "An object that contains the issure breakup details.  \n  \nLearn more about the `issuer` child object.</a>",
    "3-0": "dealer",
    "3-1": "`object`",
    "3-2": "An object that contains the dealer breakup details.  \n  \nLearn more about the `dealer` child object.</a>"
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
    "0-2": "An object that contains the breakup amount details.  \n  \nLearn more about the `amount `child object.</a>"
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
    "0-2": "An object that contains the breakup amount details.  \n  \nLearn more about the `amount `child object.</a>"
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
    "0-2": "An object that contains the breakup amount details.  \n  \nLearn more about the `amount `child object.</a>"
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
    "0-2": "An object that contains the breakup amount details.  \n  \nLearn more about the `amount `child object.</a>"
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
    "0-0": "value<sup>`*`</sup>",
    "0-1": "`integer`",
    "0-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`",
    "1-0": "currency<sup>`*`</sup>",
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


#### Loan Amount [Child Object]

The table below lists the various parameters in the `loan_amount` child object. This is part of the `tenures` object.

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


#### Total Discount Amount [Child Object]

The table below lists the various parameters in the `total_discount_amount` child object. This is part of the `tenures` object.

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


#### Net Payment Amount [Child Object]

The table below lists the various parameters in the `net_payment_amount` child object. This is part of the `tenures` object.

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


#### Monthly EMI Amount [Child Object]

The table below lists the various parameters in the `monthly_emi_amount` child object. This is part of the `tenures` object.

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


#### Total EMI Amount [Child Object]

The table below lists the various parameters in the `total_emi_amount` child object. This is part of the `tenures` object.

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


#### Interest Amount [Child Object]

The table below lists the various parameters in the `interest_amount` child object. This is part of the `tenures` object.

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


#### Total Subvention Amount [Child Object]

The table below lists the various parameters in the `total_subvention_amount` child object. This is part of the `tenures` object.

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


#### Processing Fee Details [Child Object]

The table below lists the various parameters in the `processing_fee_details` child object. This is part of the `tenures` object.

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


#### Convenience Fee Breakdown [Child Object]

The table below lists the various parameters in the `convenience_fee_breakdown` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "fee_calculated_on_amount",
    "0-1": "`object`",
    "0-2": "An object that contains the fee calculation amount details.  \n  \nLearn more about the `fee_calculated_on_amount`child object.</a>",
    "1-0": "fee_amount",
    "1-1": "`object`",
    "1-2": "An object that contains the fee amount details.  \n  \nLearn more about the `fee_amount`child object.</a>",
    "2-0": "tax_amount",
    "2-1": "`object`",
    "2-2": "An object that contains the tax amount details.  \n  \nLearn more about the `tax_amount`child object.</a>",
    "3-0": "additional_fee_amount",
    "3-1": "`object`",
    "3-2": "An object that contains the additional fee amount details.  \n  \nLearn more about the `additional_fee_amount`child object.</a>",
    "4-0": "maximum_fee_amount",
    "4-1": "`object`",
    "4-2": "An object that contains the maximum fee amount details.  \n  \nLearn more about the `maximum_fee_amount`child object.</a>",
    "5-0": "applicable_fee_amount",
    "5-1": "`object`",
    "5-2": "An object that contains the applicable fee amount details.  \n  \nLearn more about the `applicable_fee_amount`child object.</a>",
    "6-0": "subvented_fee_amount",
    "6-1": "`object`",
    "6-2": "An object that contains the subvented fee amount details.  \n  \nLearn more about the `subvented_fee_amount`child object.</a>"
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


##### Fee Calculated on Amount [Child Object]

The table below lists the various parameters in the `fee_calculated_on_amount` child object. This is part of the `convenience_fee_breakdown` object.

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


##### Fee Amount [Child Object]

The table below lists the various parameters in the `fee_amount` child object. This is part of the `convenience_fee_breakdown` object.

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


##### Tax Amount [Child Object]

The table below lists the various parameters in the `tax_amount` child object. This is part of the `convenience_fee_breakdown` object.

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


##### Additional Fee Amount [Child Object]

The table below lists the various parameters in the `additional_fee_amount` child object. This is part of the `convenience_fee_breakdown` object.

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


##### Maximum Fee Amount [Child Object]

The table below lists the various parameters in the `maximum_fee_amount` child object. This is part of the `convenience_fee_breakdown` object.

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


##### Applicable Fee Amount [Child Object]

The table below lists the various parameters in the `applicable_fee_amount` child object. This is part of the `convenience_fee_breakdown` object.

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


##### Subvented Fee Amount [Child Object]

The table below lists the various parameters in the `subvented_fee_amount` child object. This is part of the `convenience_fee_breakdown` object.

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


### Customer Details [Child Object]

The table below lists the various parameters in the `customer_details` object. This is part of the offer validation response object.

| Parameter   | Type     | Description                                                                    |
| :---------- | :------- | :----------------------------------------------------------------------------- |
| customer_id | `String` | Details related to the customer ID, required for Plural tokenized saved cards. |

## Generate Token API

The table below lists the request parameters of our Generate Token API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "client_id<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Unique client identifier in the Plural database.  \n  \nExample: `a17ce30e-f88e-4f81-ada1-c3b4909ed232`  \n  \nNote: The Onboarding team has provided you with this information as part of the onboarding process.",
    "1-0": "client_secret<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Unique client secret key provided while onboarding.  \n  \nExample: `fgwei7egyhuggwp39w8rh`  \n  \n**Note**: The Onboarding team has provided you with this information as part of the onboarding process.",
    "2-0": "grant_type<sup>`*`</sup>",
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


### Response Parameter

The table below lists the various parameters returned in our Generate Token API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "access_token",
    "0-1": "`string`",
    "0-2": "The access token generated by the system.<ul><li>Minimum length: 1 character.</li><li>Maximum length: 8192 characters.</ul></li>Example: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`  \n  \n**Note**: Use this token in the authorization headers to authenticate Plural APIs.",
    "1-0": "expires_at",
    "1-1": "`string`",
    "1-2": "Access duration timestamp.  \n  \nExample: `2024-06-28T13:26:06.909140Z`"
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


## Create Order API

The table below lists the request parameters of our Create Order API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant_order_reference<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Enter a unique identifier for the order request.<ul><li>Minimum: `1` characters.</li><li>Maximum: `50` characters.</ul></li>Example: `1234567890`<br><br>Supported characters:<ul><li>`A-Z`</li><li>`a-z`</li><li>`0-9`</li><li>`-`</li><li>`_`</ul></li>",
    "1-0": "order_amount<sup>`*`</sup>",
    "1-1": "`object`",
    "1-2": "An object that contains the transaction amount details.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#order-amount-child-object\" >Learn more about the `order_amount` child object</a>.",
    "2-0": "pre_auth",
    "2-1": "`boolean`",
    "2-2": "The pre-authorization type.  \n  \nPossible values:<ul><li>`false` (default): When pre-authorization is not required.</li><li>`true`: When pre-authorization is needed.</ul></li>",
    "3-0": "allowed_payment_methods",
    "3-1": "`array of strings`",
    "3-2": "The type of payment methods you want to offer your customers to accept payments.  \n  \nAccepted values:<ul><li>`CARD`</li><li>`UPI`</li><li>`POINTS`</li><li>`NETBANKING`</li><li>`WALLET`</li><li>`CREDIT_EMI`</li><li>`DEBIT_EMI`</ul></li>Example: `CARD`  \n  \n**Note**: Before selecting a payment method, ensure it is configured for you.",
    "4-0": "notes",
    "4-1": "`string`",
    "4-2": "The note you want to show against an order.  \n  \nExample: Order1",
    "5-0": "callback_url",
    "5-1": "`string`",
    "5-2": "URL to redirect your customers to specific success or failure pages based on the order or product details.  \n  \nExample: https\\://sample-callback-url",
    "6-0": "purchase_details",
    "6-1": "`object`",
    "6-2": "An object that contains the purchase details.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#purchase-details-child-object\" >Learn more about the `purchase_details` child object</a>."
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


### Order Amount [Child Object]

The table below lists the various parameters in the `order_amount` child object. This object is part of the `create orders` sample request object.

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


### Purchase Details [Child Object]

The table below lists the various parameters in the `purchase_details` child object. This object is part of the `create orders` sample request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "customer",
    "0-1": "`Object`",
    "0-2": "An object that contains the customer details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/docs/request-tables#customer-child-object\" >Learn more about the `customer` child object.</a>",
    "1-0": "merchant_metadata",
    "1-1": "`object`",
    "1-2": "An object of key-value pair that can be used to store additional information.  \n  \nExample: `\"key1\": \"DD\"`",
    "2-0": "split_info",
    "2-1": "`object`",
    "2-2": "An object that contains the split information details.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#split-info-child-object\" >Learn more about the `split_info` child object</a>."
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


#### Customer [Child Object]

The table below lists the various parameters in the `customer` child object. This is part of the `purchase_details` object.

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
    "4-2": "Customer's mobile number.<br><ul><li>Minimum length: 9 character.</li><li>Maximum length: 20 characters.</ul></li>Example: `9876543210`<br><br>Supported characters: <ul><li>`0-9`</li><li>`+`</ul></li>",
    "5-0": "billing_address",
    "5-1": "`object`",
    "5-2": "An object that contains the details of the billing address.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/docs/request-tables#billing-address-child-object\" >Learn more about the `billing_address` child object.</a>",
    "6-0": "shipping_address",
    "6-1": "`object`",
    "6-2": "An object that contains the shipping address details.  \n  \n<a style=\"text-decoration:underline;\" href=\"https://developer.pluralonline.com/docs/request-tables#shipping-address-child-object\" >Learn more about the `shipping_address` child object.</a>"
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


#### Split Info [Child Object]

The table below lists the various parameters in the `split_info` child object. This is part of the `purchase_details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "split_type",
    "0-1": "`string`",
    "0-2": "Type of split.<br><br>Example: `Amount`",
    "1-0": "split_details",
    "1-1": "`array of objects`",
    "1-2": "An array of objects that contains the split details.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#split-details-child-object\" >Learn more about `split_details` child object</a>."
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


##### Split Details [Child Object]

The table below lists the various parameters in the `split_details` child object. This is part of the `split_info` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "split_merchant_id",
    "0-1": "`string`",
    "0-2": "Partner merchant ID.  \n  \nExample: `123456`",
    "1-0": "merchant_settlement_reference",
    "1-1": "`string`",
    "1-2": "Unique identifier entered while creating a order in split.<ul><li>Maximum length: 50 characters.</ul></li>Example: `5206071124-aa-mpLhF3-cc-l`",
    "2-0": "amount",
    "2-1": "`object`",
    "2-2": "An object that contains the split amount details.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#amount-child-object\" >Learn more about \t`amount` child object.",
    "3-0": "on_hold",
    "3-1": "`boolean`",
    "3-2": "Indicate whether the settlement is on hold for future release.  \n  \nAccepted values:<ul><li>`true`: The settlement is placed on hold.</li><li>`false`: The settlement is processed immediately."
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


#### Amount \[Child Object]

The table below lists the various parameters in the `amount` child object. This object is part of the `split_details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value",
    "0-1": "`integer`",
    "0-2": "The split amount is Paisa.<ul><li>Minimum value: `100` (₹1).</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
    "1-0": "currency",
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


## Capture Order API

The table below lists the path parameter of our Capture Order API.

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


The table below lists the request parameter of our Capture Order API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant_capture_reference<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Enter a unique identifier for the capture order request.<ul><li>Maximum length: `50` characters.</li><li>Minimum length: `1` character.</ul></li>Example: `123456789`<br><br>Supported characters:<ul><li>`A-Z`</li><li>`a-z`</li><li>`0-9`</li><li>`-`</li><li>`\\`</li><li>`_`</ul></li>",
    "1-0": "capture_amount",
    "1-1": "`object`",
    "1-2": "**Mandatory for a partial capture request**.  \n  \nAn object that contains the capture amount details.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#capture-amount-child-object\" >Learn more about out `capture_amount` child object</a>."
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


### Capture Amount [Child Object]

The table below lists the various parameters in the `capture_amount` child object. This object is part of the `capture_order` request object.

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


## Cancel Order API

The table below lists the path parameter of our Cancel Order API.

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


## Get Order by Order ID API

The table below lists the path parameter of our Get Order by Order ID API.

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


## Get Order by Merchant Order Reference API

The table below lists the path parameter of our Get Order by Order ID API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant_order_reference<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Unique identifier of the merchant order reference entered while creating an Order.  \n  \nExample: `112345`"
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


## Create Card Payment API

The table below lists the path parameter of our Create Card Payment API.

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


The table below lists the request parameters of our Create Card Payment API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "Payments<sup>`*`</sup>",
    "0-1": "`array of objects`",
    "0-2": "An array of objects that contains the payment details.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#payments-child-object\" >Learn more about our `payments` array of objects</a>."
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

The table below lists the various parameters in the `payments` child object. This object is part of the `create card payment` request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant_payment_reference<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Unique Payment Reference id sent by merchant.  \n  \nExample: `008cf04b-a770-4777-854e-b1e6c1230609`",
    "1-0": "payment_method<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Type of payment method you want to use to accept a payment.  \n  \nAccepted value: `CARD`  \n  \nExample: `CARD`",
    "2-0": "payment_amount<sup>`*`</sup>",
    "2-1": "`object`",
    "2-2": "An object that contains the details of the payment amount.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#payment-amount-child-object\" >Learn more about our `payment_amount` child object</a>.",
    "3-0": "payment_option<sup>`*`</sup>",
    "3-1": "`object`",
    "3-2": "An object that contains the details of the payment options.  \n  \nYou can use either `card_details` or `card_token_details` as a payment option.  \n  \n**Note**: One object is mandatory to process the request.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#payment-option-child-object\" >Learn more about our `payment_option` child object</a>.",
    "4-0": "device_info",
    "4-1": "`object`",
    "4-2": "**Mandatory for Native OTP Flow (3D Secure Payments)**.  \n  \nAn object that contains the device information.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#device-info-child-object\" >Learn more about out `device_info` child object</a>."
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
    "0-0": "card_details",
    "0-1": "`object`",
    "0-2": "An object that contains the card details.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#card-details-child-object\" >Learn more about the `card_details` child object</a>.",
    "1-0": "card_token_details",
    "1-1": "`object`",
    "1-2": "An object that contains the card token details.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#card-token-details-child-object\" >Learn more about the `card_token_details` child object</a>."
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


#### Card Details [Child Object]

The table below lists the various parameters in the `card_details` child object. This object is part of the `payment_option` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "name<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Name on the card.<ul><li>Maximum length: `100` characters.</li><li>Minimum length: `1` characters.</ul></li>Example: `Kevin`",
    "1-0": "card_number<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Card Number.<ul><li>Maximum length: `23` characters.</li><li>Minimum length: `12` characters.</ul></li>Example: `123456789012`<br><br>Supported characters: `0-9`",
    "2-0": "cvv<sup>`*`</sup>",
    "2-1": "`string`",
    "2-2": "Card Verification Value [cvv] of the card.<ul><li>Maximum length: `4` digits.</li><li>Minimum length: `3` digits.</ul></li>Example: `123`<br><br>Supported characters: `0-9`",
    "3-0": "expiry_month<sup>`*`</sup>",
    "3-1": "`string`",
    "3-2": "Card expiry month as on the card.  \n  \nHas to be 2 digits.  \n  \nExample: `08`  \n  \nSupported characters: `0-9`",
    "4-0": "expiry_year<sup>`*`</sup>",
    "4-1": "`string`",
    "4-2": "Card expiry year as on the card.  \n  \nHas to be 4 digits.  \n  \nExample: `2024`  \n  \nSupported characters: `0-9`",
    "5-0": "registered_mobile_number",
    "5-1": "`string`",
    "5-2": "Card registered mobile number.<ul><li>Maximum length: `20` characters.</li><li>Minimum length: `9` characters.</ul></li>Example: `9876543210`<br><br>Supported characters: `0-9`",
    "6-0": "save",
    "6-1": "`boolean`",
    "6-2": "Save card transaction status.  \n  \nPossible values:<ul><li>`true`: Save card details.</li><li>`false`: Do not save card details.</ul></li>"
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


#### Card Token Details [Child Object]

The table below lists the various parameters in the `card_token_details` child object. This object is part of the `payment_option` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "name<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Name on the card.<ul><li>Maximum length: `100` characters.</li><li>Minimum length: `1` characters.</ul></li>Example: `Kevin`",
    "1-0": "cvv",
    "1-1": "`string`",
    "1-2": "**Mandatory when `token_txn_type` is `ALT_TOKEN` or `ISSUER_TOKEN`**.<br><br>Optional when `token_txn_type` is `NETWORK_TOKEN` for Visa and Mastercard (cvv-less flow).<br><br>Card Verification Value [cvv] of the card.<ul><li>Maximum length: `4` digits.</li><li>Minimum length: `3` digits.</ul></li>Example: `123`<br><br>Supported characters: `0-9`<br><br>**Note**: For RuPay, CVV is mandatory even when `token_txn_type` is `NETWORK_TOKEN`.",
    "2-0": "last4_digit<sup>`*`</sup>",
    "2-1": "`string`",
    "2-2": "The last four digits of your card number.  \n  \nHas to be 4 digits.  \n  \nExample: `1234`  \n  \nSupported characters: `0-9`",
    "3-0": "expiry_month<sup>`*`</sup>",
    "3-1": "`string`",
    "3-2": "Card expiry month as on the card.  \n  \nHas to be 2 digits.  \n  \nExample: `08`  \n  \nSupported characters: `0-9`",
    "4-0": "expiry_year<sup>`*`</sup>",
    "4-1": "`string`",
    "4-2": "Card expiry year as on the card.  \n  \nHas to be 4 digits.  \n  \nExample: `2030`  \n  \nSupported characters: `0-9`",
    "5-0": "token<sup>`*`</sup>",
    "5-1": "`string`",
    "5-2": "Unique identifier of the card as per the token transaction type.<ul><li>Minimum: `1` characters.</li><li>Maximum: `50` characters.</ul></li>Example: `0342ef1e0342ef1e`<br><br>Supported characters:<ul><li>`A-Z`</li><li>`a-z`</li><li>`0-9`</li><li>`.`</li><li>`/`</li><li>`\\`</li><li>`-`</li><li>`_`</li><li>`,`</li><li>`(`</li><li>`)`</li><li>`'`</ul></li>",
    "6-0": "cryptogram<sup>`*`</sup>",
    "6-1": "`string`",
    "6-2": "Unique encrypted text.<ul><li>Minimum: `1` characters.</li><li>Maximum: `50` characters.</ul></li>Example: `wAAAAAAl9SX1HsAmWKSgqwAAAA`",
    "7-0": "token_txn_type<sup>`*`</sup>",
    "7-1": "`string`",
    "7-2": "The type of token transaction.  \n  \nExample: `ALT_TOKEN`  \n  \nAccepted values: <ul><li>`ALT_TOKEN`</li><li>`NETWORK_TOKEN`</li><li>`ISSUER_TOKEN`</ul></li>",
    "8-0": "registered_mobile_number",
    "8-1": "`string`",
    "8-2": "Card registered mobile number.<ul><li>Maximum length: `20` characters.</li><li>Minimum length: `9` characters.</ul></li>Example: `9876543210`<br><br>Supported characters: `0-9`",
    "9-0": "diners_token_reference_id",
    "9-1": "`string`",
    "9-2": "Unique reference ID of a DINERS card.<ul><li>Minimum: `1` characters.</li><li>Maximum: `50` characters.</ul></li>Example: `AS123edf4567tyu890`<br><br>Supported characters:<ul><li>`A-Z`</li><li>`a-z`</li><li>`0-9`</ul></li>",
    "10-0": "diners_token_requester_merchant_id",
    "10-1": "`string`",
    "10-2": "Unique merchant ID of the token requester system.<ul><li>Minimum: `1` characters.</li><li>Maximum: `50` characters.</ul></li>Example: `1234567890`<br><br>Supported characters:<ul><li>`A-Z`</li><li>`a-z`</li><li>`-`</li><li>`_`</ul></li>",
    "11-0": "token_id",
    "11-1": "`string`",
    "11-2": "Unique identifier of the token in the Plural database.<ul><li>Maximum length: `50` characters.</ul></li>Example: `token-v1-0811030624-aa-RBDgpR`"
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


#### Device Info [Child Object]

The table below lists the various parameters in the `device_info` child object. This object is part of the `payment_option` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "browser_accept_header<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "The customer's browser accept header for processing payments via the selected pay mode.  \n  \nExample: `*/*`",
    "1-0": "browser_user_agent<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "The customer's browser user agent for processing payments via the selected pay mode.  \n  \nExample: `mozilla/5.0+x11;+ubuntu;+linux+x86_64;+rv:72.0)+gecko/20100101+firefox/72.0`",
    "2-0": "browser_language<sup>`*`</sup>",
    "2-1": "`string`",
    "2-2": "The customer's browser language for processing the payment via the selected pay mode.  \n  \nExample: `en`",
    "3-0": "browser_screen_height<sup>`*`</sup>",
    "3-1": "`string`",
    "3-2": "The customer's browser screen height for processing the payment via the selected pay mode.  \n  \nExample: `768`",
    "4-0": "browser_screen_width<sup>`*`</sup>",
    "4-1": "`string`",
    "4-2": "The customer's browser screen width for processing the payment via the selected pay mode.  \n  \nExample: `1366`",
    "5-0": "browser_timezone<sup>`*`</sup>",
    "5-1": "`string`",
    "5-2": "The customer's browser time for processing the payment via the selected pay mode.  \n  \nExample: `-330`",
    "6-0": "browser_window_size<sup>`*`</sup>",
    "6-1": "`string`",
    "6-2": "The customer's browser screen color depth for processing the payment via the selected pay mode.  \n  \nExample: `24`",
    "7-0": "browser_java_enabled_val<sup>`*`</sup>",
    "7-1": "`string`",
    "7-2": "The customer's browser Java enabled value for processing the payment via the selected pay mode.  \n  \nExample: `true`",
    "8-0": "browser_javascript_enabled_val<sup>`*`</sup>",
    "8-1": "`string`",
    "8-2": "The customer's browser javascript enabled value for processing the payment via the selected pay mode.  \n  \nExample: `true`",
    "9-0": "device_channel<sup>`*`</sup>",
    "9-1": "`string`",
    "9-2": "Payment Instrument details of the transactions.  \n  \nExample: `browser`"
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


## Get Card Details

The table below lists the request parameters of our Get Card Details API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`string`",
    "0-2": "The transaction amount you want to accept from your customers.<ul><li>Amount in Paisa.</li><li>Minimum value: `100` (₹1).</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
    "1-0": "card_details",
    "1-1": "`object`",
    "1-2": "An object that contains the card details.  \n  \nLearn more about our `card_details` child object."
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


### Card Details [Child Object]

The table below lists the various parameters in the `card_details` child object. This object is part of the `Get Card Details` request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "payment_identifier<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Card Number.<ul><li>Maximum length: `23` characters.</li><li>Minimum length: `12` characters.</ul></li>Example: `123456789012`<br><br>Supported characters: `0-9`",
    "1-0": "payment_reference_type<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Type of payment method you want to use to accept a payment.  \n  \nAccepted value: `CARD`  \n  \nExample: `CARD`"
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


## Send OTP

The table below lists the request parameters of our Send OTP API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "payment_id<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Unique identifier of the payment in the Plural database.<ul><li>Maximum length: `50` characters.</ul></li>Example: `v1-5206071124-aa-mpLhF3-cc-l`"
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


## Verify OTP

The table below lists the request parameters of our Send OTP API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "payment_id<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Unique identifier of the payment in the Plural database.<ul><li>Maximum length: `50` characters.</ul></li>Example: `v1-5206071124-aa-mpLhF3-cc-l`",
    "1-0": "otp<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Enter the OTP received on your registered mobile number.  \n  \nHas to be 4 digit.  \n  \nExample: `1234`"
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


## Resend OTP

The table below lists the request parameters of our Send OTP API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "payment_id<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Unique identifier of the payment in the Plural database.<ul><li>Maximum length: `50` characters.</ul></li>Example: `v1-5206071124-aa-mpLhF3-cc-l`"
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
    "0-0": "merchant_payment_reference<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Unique Payment Reference id sent by merchant.  \n  \nExample: `008cf04b-a770-4777-854e-b1e6c1230609`",
    "1-0": "payment_method<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Type of payment method you want to use to accept a payment.  \n  \nAccepted value: `UPI`  \n  \nExample: `UPI`",
    "2-0": "payment_amount<sup>`*`</sup>",
    "2-1": "`object`",
    "2-2": "An object that contains the details of the payment amount.  \n  \nLearn more about our `payment_amount` array of objects.",
    "3-0": "payment_option<sup>`*`</sup>",
    "3-1": "`object`",
    "3-2": "An object that contains the details of the payment options.  \n  \nLearn more about our `payment_option` array of objects."
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
    "0-2": "VPA handle of your customer from whom you want to accept payment.<ul><li>Minimum length: `2` characters.</li><li>Maximum length: `256` characters.</ul></li>Example: `kevin.bob@examplebank.com`<br><br>Supported characters:<ul><li>`A-Z`</li><li>`a-z`</li><li>`0-9`</li><li>`@`</li><li>`$`</ul></li>"
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
    "0-0": "merchant_payment_reference<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Unique Payment Reference id sent by merchant.  \n  \nExample: `008cf04b-a770-4777-854e-b1e6c1230609`",
    "1-0": "payment_method<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Type of payment method you want to use to accept a payment.  \n  \nAccepted value: `UPI`  \n  \nExample: `UPI`",
    "2-0": "payment_amount<sup>`*`</sup>",
    "2-1": "`object`",
    "2-2": "An object that contains the details of the payment amount.  \n  \nLearn more about our `payment_amount` array of objects.",
    "3-0": "payment_option<sup>`*`</sup>",
    "3-1": "`object`",
    "3-2": "An object that contains the details of the payment options.  \n  \nLearn more about our `payment_option` array of objects."
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


## Create UPI Intent QR

The table below lists the path parameter of our Create UPI Intent QR API.

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


The table below lists the request parameters of our Create UPI Intent QR API.

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

The table below lists the various parameters in the `payments` child object. This object is part of the `create upi intent qr` request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant_payment_reference<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Unique Payment Reference id sent by merchant.  \n  \nExample: `008cf04b-a770-4777-854e-b1e6c1230609`",
    "1-0": "payment_method<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Type of payment method you want to use to accept a payment.  \n  \nAccepted value: `UPI`  \n  \nExample: `UPI`",
    "2-0": "payment_amount<sup>`*`</sup>",
    "2-1": "`object`",
    "2-2": "An object that contains the details of the payment amount.  \n  \nLearn more about our `payment_amount` array of objects.",
    "3-0": "payment_option<sup>`*`</sup>",
    "3-1": "`object`",
    "3-2": "An object that contains the details of the payment options.  \n  \nLearn more about our `payment_option` array of objects."
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
    "0-2": "The transaction mode in which you want to accept payment.  \n  \nAccepted value: `INTENT`",
    "1-0": "upi_qr<sup>`*`</sup>",
    "1-1": "`object`",
    "1-2": "Indicates whether a UPI QR code is enabled for the payment.  \n  \nAccepted value: `True`  \n  \nPossible values: <ul><li>`true`: UPI QR code is enabled for the payment.</li><li>`false`: UPI QR code is not enabled for the payment.</ul></li>"
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


## Check Point Balance

The table below lists the request parameters of our Check Point Balance API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "payment_option<sup>`*`</sup>",
    "0-1": "`object`",
    "0-2": "An object that contains the payment option details.  \n  \nLearn more about our `payment_option` child object.",
    "1-0": "order_details<sup>`*`</sup>",
    "1-1": "`object`",
    "1-2": "An object that contains the order details.  \n  \nLearn more about our `order_details` child object."
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

The table below lists the various parameters in the `payment_option` child object. This object is part of the `check_point_balance` request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "points_card_details<sup>`*`</sup>",
    "0-1": "`object`",
    "0-2": "An object that contains the point card details.  \n  \nLearn more about our `points_card_details` child object."
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


#### Points Card Details [Child Object]

The table below lists the various parameters in the `points_card_details` child object. This object is part of the `payment_option` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "card_last4<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "The last four digits of your card number.  \n  \nHas to be 4 digits.  \n  \nExample: `1234`  \n  \nSupported characters: `0-9`",
    "1-0": "card_number<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Card Number.<ul><li>Maximum length: `23` characters.</li><li>Minimum length: `12` characters.</ul></li>Example: `123456789012`<br><br>Supported characters: `0-9`",
    "2-0": "registered_mobile_number<sup>`*`</sup>",
    "2-1": "`string`",
    "2-2": "Point card registered mobile number.<ul><li>Maximum length: `20` characters.</li><li>Minimum length: `9` characters.</ul></li>Example: `9876543210`<br><br>Supported characters:<ul><li>`0-9`</li><li>`+`</ul></li>"
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


### Order Details [Child Object]

The table below lists the various parameters in the `order_details` child object. This object is part of the `check_point_balance` request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "order_amount<sup>`*`</sup>",
    "0-1": "`object`",
    "0-2": "An object that contains the order amount details.  \n  \nLearn more about our `order_amount` child object."
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


#### Order Amount [Child Object]

The table below lists the various parameters in the `order_amount` child object. This object is part of the `order_details` object.

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


## Create Payment via Pay by Points

The table below lists the path parameter of our Create Payment via Pay by Points API.

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


The table below lists the request parameters of our Create Payment via Pay by Points API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "Payments<sup>`*`</sup>",
    "0-1": "`array of objects`",
    "0-2": "An array of objects that contains the payment details.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#payments-child-object\" >Learn more about our `payments` array of objects</a>."
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

The table below lists the various parameters in the `payments` child object. This object is part of the `create payment via pay by points` request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant_payment_reference<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Unique Payment Reference id sent by merchant.  \n  \nExample: `008cf04b-a770-4777-854e-b1e6c1230609`",
    "1-0": "payment_method<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Type of payment method you want to use to accept a payment.  \n  \nAccepted value: <ul><li>`CARD`</li><li>`POINTS`</ul></li>Example: `CARD`",
    "2-0": "payment_amount<sup>`*`</sup>",
    "2-1": "`object`",
    "2-2": "An object that contains the details of the payment amount.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#payment-amount-child-object\" >Learn more about our `payment_amount` child object</a>.",
    "3-0": "payment_option<sup>`*`</sup>",
    "3-1": "`object`",
    "3-2": "An object that contains the details of the payment options.  \n  \nNote:<ul><li>When the payment method is `CARD`, the `card_details` object is mandatory.</li><li>When the payment method is `POINTS`, the `points_card_details` object is mandatory."
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
    "0-0": "card_details",
    "0-1": "`object`",
    "0-2": "**Mandatory when `payment_method` is `CARD`**.  \n  \nAn object that contains the card details.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#card-details-child-object\" >Learn more about the `card_details` child object</a>.",
    "1-0": "points_card_details",
    "1-1": "`object`",
    "1-2": "**Mandatory when `payment_method` is `POINTS`**.  \n  \nAn object that contains the point card details.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#card-token-details-child-object\" >Learn more about the `card_token_details` child object</a>."
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


#### Card Details [Child Object]

The table below lists the various parameters in the `card_details` child object. This object is part of the `payment_option` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "name<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Name on the card.<ul><li>Maximum length: `100` characters.</li><li>Minimum length: `1` characters.</ul></li>Example: `Kevin`",
    "1-0": "card_number<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Card Number.<ul><li>Maximum length: `23` characters.</li><li>Minimum length: `12` characters.</ul></li>Example: `123456789012`<br><br>Supported characters: `0-9`",
    "2-0": "cvv<sup>`*`</sup>",
    "2-1": "`string`",
    "2-2": "Card Verification Value [cvv] of the card.<ul><li>Maximum length: `4` digits.</li><li>Minimum length: `3` digits.</ul></li>Example: `123`<br><br>Supported characters: `0-9`",
    "3-0": "expiry_month<sup>`*`</sup>",
    "3-1": "`string`",
    "3-2": "Card expiry month as on the card.  \n  \nHas to be 2 digits.  \n  \nExample: `08`  \n  \nSupported characters: `0-9`",
    "4-0": "expiry_year<sup>`*`</sup>",
    "4-1": "`string`",
    "4-2": "Card expiry year as on the card.  \n  \nHas to be 4 digits.  \n  \nExample: `2024`  \n  \nSupported characters: `0-9`",
    "5-0": "registered_mobile_number",
    "5-1": "`string`",
    "5-2": "Card registered mobile number.<ul><li>Maximum length: `20` characters.</li><li>Minimum length: `9` characters.</ul></li>Example: `9876543210`<br><br>Supported characters: `0-9`"
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


#### Points Card Details [Child Object]

The table below lists the various parameters in the `points_card_details` child object. This object is part of the `payment_option` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "card_last4<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "The last four digits of your card number.  \n  \nHas to be 4 digits.  \n  \nExample: `1234`  \n  \nSupported characters: `0-9`",
    "1-0": "card_number<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Card Number.<ul><li>Maximum length: `23` characters.</li><li>Minimum length: `12` characters.</ul></li>Example: `123456789012`  \n  \nSupported characters: `0-9`",
    "2-0": "registered_mobile_number",
    "2-1": "`string`",
    "2-2": "Card registered mobile number.<ul><li>Maximum length: `20` characters.</li><li>Minimum length: `10` characters.</ul></li>Example: `9876543210`<br><br>Supported characters: `0-9`"
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


## Create NetBanking Payment

The table below lists the path parameter of our Create NetBanking Payment API.

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


The table below lists the request parameters of our Create NetBanking Payment API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "Payments<sup>`*`</sup>",
    "0-1": "`array of objects`",
    "0-2": "An array of objects that contains the payment details.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#payments-child-object\" >Learn more about our `payments` array of objects</a>."
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

The table below lists the various parameters in the `payments` child object. This object is part of the `create payment via pay by points` request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant_payment_reference<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Unique Payment Reference id sent by merchant.  \n  \nExample: `008cf04b-a770-4777-854e-b1e6c1230609`",
    "1-0": "payment_method<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Type of payment method you want to use to accept a payment.  \n  \nAccepted value: <ul><li>`NETBANKING`</ul></li>Example: `NETBANKING`",
    "2-0": "payment_amount<sup>`*`</sup>",
    "2-1": "`object`",
    "2-2": "An object that contains the details of the payment amount.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#payment-amount-child-object\" >Learn more about our `payment_amount` child object</a>.",
    "3-0": "payment_option<sup>`*`</sup>",
    "3-1": "`object`",
    "3-2": "An object that contains the details of the payment options.  \n  \nLearn more about our `payment_option` child object."
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
    "0-0": "netbanking_details",
    "0-1": "`object`",
    "0-2": "An object that contains the Netbanking details.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#card-details-child-object\" >Learn more about the `netbanking_details` child object</a>."
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


#### NetBanking Details [Child Object]

The table below lists the various parameters in the `netbanking_details` child object. This object is part of the `payment_option` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "pay_code<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Bank code in the Plural database.  \n  \nExample: `NB1531`  \n  \nRefer to our Supported Banks to know more.",
    "1-0": "txn_mode<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Payment transaction mode.  \n  \nExample: `REDIRECT`  \n  \nAccepted values:<ul><li>`REDIRECT`</li><li>`QR`</li><li>`INTENT`</ul></li>"
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


## Create Wallet Payment

The table below lists the path parameter of our Create Wallet Payment API.

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


The table below lists the request parameters of our Create Wallet Payment API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "Payments<sup>`*`</sup>",
    "0-1": "`array of objects`",
    "0-2": "An array of objects that contains the payment details.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#payments-child-object\" >Learn more about our `payments` array of objects</a>."
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

The table below lists the various parameters in the `payments` child object. This object is part of the `create payment via pay by points` request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant_payment_reference<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Unique Payment Reference id sent by merchant.  \n  \nExample: `008cf04b-a770-4777-854e-b1e6c1230609`",
    "1-0": "payment_method<sup>`*`</sup>",
    "1-1": "`string`",
    "1-2": "Type of payment method you want to use to accept a payment.  \n  \nAccepted value: <ul><li>`WALLET`</ul></li>Example: `WALLET`",
    "2-0": "payment_amount<sup>`*`</sup>",
    "2-1": "`object`",
    "2-2": "An object that contains the details of the payment amount.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#payment-amount-child-object\" >Learn more about our `payment_amount` child object</a>.",
    "3-0": "payment_option<sup>`*`</sup>",
    "3-1": "`object`",
    "3-2": "An object that contains the details of the payment options.  \n  \nLearn more about our `payment_option` child object.  \n  \n**Note**: You can use wallet as a payment option."
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
    "0-0": "wallet_details",
    "0-1": "`object`",
    "0-2": "An object that contains the wallet details.  \n  \n<a href=\"https://developer.pluralonline.com/docs/request-tables#card-details-child-object\" >Learn more about the `wallet_details` child object</a>."
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


#### Wallet Details [Child Object]

The table below lists the various parameters in the `wallet_details` child object. This object is part of the `payment_option` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "wallet_code<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Unique code of the wallet.  \n  \nExample: `FRW`  \n  \nAccepted wallet codes:<ul><li>`ATL`: Airtel Payments Bank Ltd. (ATL_Wallet)</li><li>`AZP`: Amazon Pay (India) Pvt. Ltd.</li><li>`MBK`: One Mobikwik Systems Pvt. Ltd.</li><li>`ITZ`: Ebix Payment Services Pvt. Ltd. (ITZ Cash Card)</li><li>`PHW`: Phonepe Pvt. Ltd.</li><li>`PT2`: One97 Communications Ltd. (Card Gateway)</li><li>`FRW`: Accelyst Solutions Pvt. Ltd. (Card Gateway)</ul></li>"
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


# Generate Card Token API

The table below lists the request parameters of our Generate Card Token API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "customer_id<sup>`*`</sup>",
    "0-1": "`string`",
    "0-2": "Unique identifier of the customer in the Plural database.  \n  \nMaximum length: `50` characters.  \n  \nExample: `cust-v1-0811030624-aa-RBDgpR`",
    "1-0": "merchant_token_reference",
    "1-1": "`string`",
    "1-2": "Enter a unique identifier for the token request.<ul><li>Minimum: `1` characters.</li><li>Maximum: `50` characters.</ul></li>Example: `1234567890`  \n  \nSupported characters: <ul><li>`A-Z`</li><li>`a-z`</li><li>-`</li><li>`\\`</li><li>`_`</ul></li>",
    "2-0": "payment_method",
    "2-1": "`string`",
    "2-2": "Type of payment method you want to use to accept a payment.  \n  \nExample: `CARD`",
    "3-0": "payment_option",
    "3-1": "`object`",
    "3-2": "An object that contains the payment option details.  \n  \nLearn more about our `payment_option` child object.",
    "4-0": "payment",
    "4-1": "`object`",
    "4-2": "An object that contains the payment details.  \n  \nLearn more about our `payment` child object.",
    "5-0": "merchant_metadata",
    "5-1": "`object`",
    "5-2": "An object of key value pair that can be used to store additional information.<ul><li>Each pair cannot exceed `256` characters.</li><li>Maximum `10` key-value pairs.</ul></li>Example: \"key1\": \"DD\""
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


## Payment Option [Child Object]

The table below lists the various parameters in the `payment_option` child object. This object is part of the `Generate Card Token` request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "encrypted_card_details",
    "0-1": "`string`",
    "0-2": "Encrypted card details.<ul><li>Minimum: `1` characters.</li><li>Maximum: `50` characters.</ul></li>Example: `akdsdsdsh12k12h1k21h2khakshakh`"
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


## Payment [Child Object]

The table below lists the various parameters in the `payment` child object. This object is part of the `Generate Card Token` request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "acquirer_data",
    "0-1": "`object`",
    "0-2": "An object that contains the acquirer details.  \n  \nLearn more about our `acquirer_data` child object."
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


### Acquirer Data [Child Object]

The table below lists the various parameters in the `acquirer_data` child object. This object is part of the `payment` request object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "approval_code",
    "0-1": "`string`",
    "0-2": "Authorization code returned from acquirer against the payment.  \n  \nExample: `030376`",
    "1-0": "acquirer_reference",
    "1-1": "`string`",
    "1-2": "Unique reference returned from acquirer for the payment.  \n  \nExample: `202455840588334`",
    "2-0": "rrn",
    "2-1": "`string`",
    "2-2": "Retrieval reference number returned from acquirer for the payment.  \n  \nExample: `419335023601`",
    "3-0": "auth_reference",
    "3-1": "`string`",
    "3-2": "**Mandatory for rupay transaction**.  \n  \nA unique identifier linking the authorization request to the transaction.  \n  \nExample: `AUTH12345678`"
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
