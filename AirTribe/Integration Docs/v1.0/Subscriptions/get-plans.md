---
title: "Get Plans"
slug: "get-plans"
excerpt: ""
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Wed Jul 26 2023 10:24:54 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Jul 26 2023 11:36:33 GMT+0000 (Coordinated Universal Time)"
---
**Authorization**  
For Authorization use Basic Auth, where:

- _Username:_ Plural MerchantId
- _Password:_ Merchant Access token

**Request Body**

| Parameter Name | Type          | Description                                |                                    |    |
| :------------- | :------------ | :----------------------------------------- | :--------------------------------- | :- |
| merchantId     | string        | Plural MerchantId                          |                                    |    |
| planName       | string        | Plan name                                  |                                    |    |
| planId         | string        | PlanId generated the time of plan creation |                                    |    |
| fromDate       | string        | Filter by From Date                        |                                    |    |
| toDate         | string        | Filter by To Date                          |                                    |    |
| amount         | integer       | Filter by amount                           |                                    |    |
| amountRange    | string (Enum) | Filter by Amount Range Enum                | isMore/isLess/isEqual              |    |
| frequency      | integer       | Frequency recurrance                       |                                    |    |
| frequencyType  | string (Enum) | Filter by Frequency Type Enum              | Day/Week/Month/Year/Not Applicable |    |
| \*size         | integer       | Number of plans in a single page           |                                    |    |
| \*page         | integer       | Number of pages expected in result         |                                    |    |
| sort           | string        | Sort the result by property                | frequencyType, asc                 |    |
