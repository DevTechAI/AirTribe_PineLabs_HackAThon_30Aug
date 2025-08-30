---
title: "Tokenized Card's Life Cycle ( delete saved vault )"
slug: "tokenized-cards-life-cycle-delete-saved-vault"
excerpt: ""
hidden: true
createdAt: "Mon Jul 11 2022 12:50:04 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:54:24 GMT+0000 (Coordinated Universal Time)"
---
**Response Body** 

[block:parameters]
{
  "data": {
    "h-0": "Parameter Name",
    "h-1": "",
    "h-2": "",
    "h-3": "Type",
    "h-4": "Length",
    "h-5": "Description",
    "h-6": "M/O",
    "0-0": "response",
    "0-1": "",
    "0-2": "",
    "0-3": "Complex object type",
    "0-4": "",
    "0-5": "",
    "0-6": "M",
    "1-0": "",
    "1-1": "code",
    "1-2": "",
    "1-3": "string",
    "1-4": "Max Length 6",
    "1-5": "Status code indicating the success of the API call  \nEx :‘S-100'",
    "1-6": "M",
    "2-0": "",
    "2-1": "message",
    "2-2": "",
    "2-3": "string",
    "2-4": "Max Length 150",
    "2-5": "Description of the API call response.",
    "2-6": "M",
    "3-0": "\\_links",
    "3-1": "",
    "3-2": "",
    "3-3": "Complex object type",
    "3-4": "",
    "3-5": "",
    "3-6": "M",
    "4-0": "",
    "4-1": "tokenInfo",
    "4-2": "",
    "4-3": "",
    "4-4": "",
    "4-5": "",
    "4-6": "M",
    "5-0": "",
    "5-1": "",
    "5-2": "href",
    "5-3": "string",
    "5-4": "",
    "5-5": "Fetch registered card metadata URL",
    "5-6": "M"
  },
  "cols": 7,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left",
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


**Failure Response Body** 

| Field    |         | Data Type           | Length         | Description                                          | M/O |
| :------- | :------ | :------------------ | :------------- | :--------------------------------------------------- | :-- |
| response |         | Complex object type |                | Error object in case of failure                      | M   |
|          | code    | string              | Max Length 6   | Error response code                                  | M   |
|          | message | string              | Max length 200 | Error response message which shows problem statement | M   |
