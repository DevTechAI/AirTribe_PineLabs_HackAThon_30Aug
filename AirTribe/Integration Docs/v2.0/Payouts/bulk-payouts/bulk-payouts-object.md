---
title: "Object"
slug: "bulk-payouts-object"
excerpt: "Overview of bulk payouts sample response object."
hidden: false
createdAt: "Wed Oct 09 2024 05:14:13 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Oct 10 2024 14:44:07 GMT+0000 (Coordinated Universal Time)"
---
Shown below is a sample response returned for a Upload file API.

```json Upload File Sample Response Object
{
  "requestReferenceId": "req-1b980dd2c75b456782bc1a3acff481a0",
  "status": "PENDING",
  "message": "",
  "_links": [
    {
      "rel": "status",
      "href": "http://pluralqa.pinepg.in:8000/payouts/v2/payments?requestReferenceId=req-1b980dd2c75b456782bc1a3acff481a0"
    }
  ]
}
```

The table below lists the various parameters returned in the upload file sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "requestReferenceId",
    "0-1": "`string`",
    "0-2": "Unique identifier of the payout request in Plural database.  \n  \nExample: `req-1b980dd2c75b456782bc1a3acff481a0`",
    "1-0": "status",
    "1-1": "`string`",
    "1-2": "Payout status.  \n  \nExample: `PENDING`",
    "2-0": "message",
    "2-1": "`string`",
    "2-2": "Corresponding message to the status.  \n  \nExample: `Payment instruction pending to be executed`",
    "3-0": "\\_links",
    "3-1": "`object`",
    "3-2": "An object that contains the payment link details."
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


### \_Links [Child Object]

The table below lists the various parameters in the links child object. This object is part of the update scheduled payout sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "rel",
    "0-1": "`string`",
    "0-2": "Relationship to the resource.  \n  \nExample: `status`",
    "1-0": "href",
    "1-1": "`string`",
    "1-2": "Link to access the resource.  \n  \nExample: `http://pluralqa.pinepg.in:8000/payouts/v2/payments?paymentReferenceId=txn-a9304bb5bdd6444782466575afd023e4`"
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
