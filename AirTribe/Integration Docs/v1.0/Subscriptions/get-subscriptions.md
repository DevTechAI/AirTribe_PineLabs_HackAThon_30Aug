---
title: "Get Subscriptions"
slug: "get-subscriptions"
excerpt: ""
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Wed Jul 26 2023 10:17:35 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Jul 26 2023 11:26:40 GMT+0000 (Coordinated Universal Time)"
---
**Authorization**  
For Authorization use Basic Auth, where:

- _Username:_ Plural MerchantId
- _Password:_ Merchant Access token

**Request Body**

| Parameter Name | Type          | Description                                     |                                    |    |
| :------------- | :------------ | :---------------------------------------------- | :--------------------------------- | :- |
| merchantId     | string        | Plural MerchantId                               |                                    |    |
| planId         | integer       | PlanId using which the subscription was created |                                    |    |
| subscriptionId | integer       | Generated at the time of subscription creation  |                                    |    |
| paymentMethod  | string        | UPI                                             |                                    |    |
| planName       | string        | Name of plan                                    |                                    |    |
| paymentGateway | string        | EDGE                                            |                                    |    |
| status         | string        | Filter by status of subscription                |                                    |    |
| amount         | double        | Filter by amount                                |                                    |    |
| amountRange    | string (Enum) | Filter by Amount Range Enum                     | isMore/isLess/isEqual              |    |
| frequency      | integer       | Frequency recurrence                            |                                    |    |
| frequencyType  | string (Enum) | Filter by Frequency Type Enum                   | Day/Week/Month/Year/Not Applicable |    |
| fromDate       | string        | Filter by From Date                             |                                    |    |
| toDate         | string        | Filter by To Date                               |                                    |    |
| \*size         | integer       | Number of results in a single page              |                                    |    |
| \*page         | integer       | Number of pages                                 |                                    |    |
| sort           | string        | Sort the result                                 | amount, asc                        |    |
