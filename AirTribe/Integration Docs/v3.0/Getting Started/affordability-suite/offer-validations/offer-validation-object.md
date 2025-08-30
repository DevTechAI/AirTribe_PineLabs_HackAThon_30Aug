---
title: "Object"
slug: "offer-validation-object"
excerpt: "Overview of the Offer Validation API response object."
hidden: false
createdAt: "Wed Jan 22 2025 15:35:03 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jan 28 2025 13:32:01 GMT+0000 (Coordinated Universal Time)"
---
Shown below is a sample response returned through our Offer Validation API.

```json Offer Validation Response
{
  "code": "ELIGIBLE",
  "message": "Offer is Eligible"
}
```

Shown below is a sample response returned through our Offer Validation API.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "code",
    "0-1": "`String`",
    "0-2": "Validation status of the offer.  \n  \nPossible values:<ul><li>`NOT_ELIGIBLE`</li><li>`ELIGIBLE`</ul></li>",
    "1-0": "message",
    "1-1": "`String`",
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
