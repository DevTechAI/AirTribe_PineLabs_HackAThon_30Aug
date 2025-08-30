---
title: "Object"
slug: "imei-validation-object"
excerpt: "Overview of the IMEI Vaalidation API response object."
hidden: false
createdAt: "Tue Jan 21 2025 14:01:16 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jan 28 2025 14:37:30 GMT+0000 (Coordinated Universal Time)"
---
Shown below is a sample response returned through our IMEI Validation API.

```json IMEI Validation Response
{
  "merchant_product_imei_reference": "merchant-ref-786",
  "request_type": "BLOCKING",
  "products": [
    {
      "product_code": "xyz",
      "dealer_code": "DLR100",
      "state_code": "NY",
      "product_imei": "SN1234567863",
      "product_imei_status": "BLOCKED",
      "product_brand_response": {}
    }
  ]
}
```

The table below lists the various parameters returned in the IMEI Validation response objects.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant_product_imei_reference",
    "0-1": "`string`",
    "0-2": "Merchant product IMEI reference.  \n  \nExample: `sample`",
    "1-0": "request_type",
    "1-1": "`string`",
    "1-2": "IMEI request type.  \n  \nAccepted values:<ul><li>`BLOCKING`: To block the IMEI number.</li><li>UNBLOCKED: To unblock the IMEI number.</ul></li>",
    "2-0": "products",
    "2-1": "`array of object`",
    "2-2": "An object that contains the product information details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/imei-validation-object#products\" >Learn more about our `products` child object</a>."
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


### Products

The table below lists the various parameters in the `products` object. This is part of the IMEI Validation API response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "product_code",
    "0-1": "`string`",
    "0-2": "Unique Product identifier of the product.  \n  \nExample: `redmi_1`",
    "1-0": "dealer_code",
    "1-1": "`string`",
    "1-2": "Unique identifier for the dealer.  \n  \nExample: `DLR100`",
    "2-0": "state_code",
    "2-1": "`string`",
    "2-2": "State code passed in the request parameter.  \n  \nExample: `23`",
    "3-0": "product_imei",
    "3-1": "`string`",
    "3-2": "The unique IMEI number of the product.  \n  \nExample: `SN1234567892`",
    "4-0": "product_imei_status",
    "4-1": "`string`",
    "4-2": "Product IMEI status.<ul><li>`BLOCKED`</li><li>`UNBLOCKED`</ul></li>",
    "5-0": "product_brand_response",
    "5-1": "`object`",
    "5-2": "An object that contains the product brand response details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/imei-validation-object#product-brand-response-child-object\" >Learn more about the `product_brand_response` child object.</a>"
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


#### Product Brand Response [Child Object]

The table below lists the various parameters in the `product_brand_response` child object. This is part of the `products` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "code",
    "0-1": "`string`",
    "0-2": "Code returned from brand in case of failure",
    "1-0": "message",
    "1-1": "`string`",
    "1-2": "Message corresponding to the validation status.  \n  \nExample: `Offer is Eligible`"
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
