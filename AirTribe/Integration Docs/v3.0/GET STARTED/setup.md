---
title: "Setup"
slug: "setup"
excerpt: "As you start the integration with Plural Console, these are some pre-requisites which you should do."
hidden: true
createdAt: "Sat Sep 25 2021 13:23:18 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:58:14 GMT+0000 (Coordinated Universal Time)"
---
## **API Endpoints**

| Environment | Endpoint                               |
| :---------- | :------------------------------------- |
| Staging     | <https://api-staging.pluralonline.com> |
| Production  | <https://api.pluralonline.com>         |

> 📘 Integration Tip
> 
> All mentioned APIs are server-side APIs and must be triggered from the merchant's backend.

## Step 1 : Signup

Sign up on Plural Console Dashboard in test environment. Click on the below link: 

[block:embed]
{
  "html": false,
  "url": "https://dashboard-staging.pluralonline.com/signup",
  "title": null,
  "favicon": null,
  "provider": "dashboard-staging.pluralonline.com",
  "href": "https://dashboard-staging.pluralonline.com/signup",
  "iframe": false
}
[/block]


## Step 2 : Save Credentials

Take note of Merchant credentials: [Dashboard → Settings → Credentials]

- MID
- Access Code
- Secret Key

![](https://files.readme.io/9e03aee-Screenshot_2021-10-13_at_6.29.25_PM.png "Screenshot 2021-10-13 at 6.29.25 PM.png")

## Step 3 : Add Payment Return URL

Configure Payment Return URL (This is necessary step to get the payment response.): [Dashboard->Setting->General->Payment Return URL ]

![](https://files.readme.io/ccbdeb3-Screenshot_2021-10-13_at_6.30.15_PM.png "Screenshot 2021-10-13 at 6.30.15 PM.png")

## Step 4 : Configure PG

Dashboard->Smart Routing->Create Gateway->Select Gateway->Configure Key_ID and Key_Secret

![](https://files.readme.io/f27ee82-Screenshot_2021-10-13_at_6.34.26_PM.png "Screenshot 2021-10-13 at 6.34.26 PM.png")

> 📘 Test Credentials
> 
> You should get test credentials from the Payment gateways (such as RazorPay, PayU) which you intend to configure.  
> For Edge test PG: 
> 
> - MID :106600
> - Password : Access Code (bcf441be-411b-46a1-aa88-c6e852a7d68c) 
> - Secret Key : Secret Key (9A7282D0556544C59AFE8EC92F5C85F6).
> 
> <Update before launch>

## Step 5 : Configure Payment Modes

Configure Payment Modes for the payment gateway you are configuring. 

![](https://files.readme.io/611fecd-Screenshot_2021-10-13_at_6.35.19_PM.png "Screenshot 2021-10-13 at 6.35.19 PM.png")
