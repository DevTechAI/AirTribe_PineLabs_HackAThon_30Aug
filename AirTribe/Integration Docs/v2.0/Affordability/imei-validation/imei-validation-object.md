---
title: "Object"
slug: "imei-validation-object"
excerpt: "Overview of the IMEI Validation response object."
hidden: false
createdAt: "Mon Dec 16 2024 06:03:43 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Jan 31 2025 07:10:55 GMT+0000 (Coordinated Universal Time)"
---
Shown below is a sample response of a IMEI Validation API.

```json IMEI Validation Object
{
  "product_imei_details": [
    {
      "product_code": "786",
      "imei_no": "9090999933332251",
      "state_code": "23",
      "imei_processing_status": {
        "response_code": 0,
        "response_message": "SUCCESS"
      }
    },
    {
      "product_code": "40",
      "imei_no": "9090999933332252",
      "imei_processing_status": {
        "response_code": 0,
        "response_message": "SUCCESS"
      }
    }
  ],
  "response_code": 0,
  "response_message": "SUCCESS"
}
```
```json Failure Object
{
  "response_code": 107,
  "response_message": "MERCHANT DATA IS NOT VALID"
}
```

The table below lists the various parameters returned in the payments response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "product_imei_details",
    "0-1": "`array of object`",
    "0-2": "An object that contains the information about each product code-wise IMEI details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/imei-validation-object#product-imei-details-child-object\" >Learn more about our `product_imei_details` child object</a>.",
    "1-0": "response_code",
    "1-1": "`integer`",
    "1-2": "Response code of the request.  \n  \nExample: `200`",
    "2-0": "response_message",
    "2-1": "`string`",
    "2-2": "Corresponding message to the response code.  \n  \nExample: `Order Creation Successful`"
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


## Product IMEI Details [Child Object]

The table below lists the various parameters in the `product_imei_details` child object. This object is part of the IMEI Validation sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "product_code",
    "0-1": "`string`",
    "0-2": "Product code passed in request parameter.  \n  \nExample: `40`",
    "1-0": "imei_no",
    "1-1": "`string`",
    "1-2": "IMEI passed in the request parameter.  \n  \nExample: `9090999933332251`",
    "2-0": "state_code",
    "2-1": "`string`",
    "2-2": "State code passed in the request parameter.  \n  \nExample: `23`",
    "3-0": "imei_processing_status",
    "3-1": "`object`",
    "3-2": "An object that contains the IMEI processing status details.  \n  \n<a href=\"https://developer.pluralonline.com/v2.0/reference/imei-validation-object#imei-processing-status-child-object\" >Learn more about our `product_imei_details` child object</a>."
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


### IMEI Processing Status [Child Object]

The table below lists the various parameters in the `imei_processing_status` child object. This object is part of the `product_imei_details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "response_code",
    "0-1": "`integer`",
    "0-2": "Response code of the request.  \n  \nExample: `200`",
    "1-0": "response_message",
    "1-1": "`string`",
    "1-2": "Corresponding message to the response code.  \n  \nExample: `Order Creation Successful`"
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
