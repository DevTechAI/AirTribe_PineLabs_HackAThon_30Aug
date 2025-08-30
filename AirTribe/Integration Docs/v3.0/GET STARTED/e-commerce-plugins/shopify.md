---
title: "Shopify"
slug: "shopify"
excerpt: "Plural Payment Plugin Installation Guide for Shopify Store"
hidden: false
createdAt: "Fri Oct 18 2024 07:07:04 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Mar 12 2025 10:13:58 GMT+0000 (Coordinated Universal Time)"
---
This guide provides a step-by-step walkthrough for integrating Plural as a payment provider with your Shopify store.  By integrating with Plural, you can streamline checkout, easily handle multiple payment methods, and enhance the overall customer experience.

Learn how to integrate your Shopify store with the Plural Payment Gateway. Watch the video tutorial below for a step-by-step guide.

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FWRxba4Fg4vw%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DWRxba4Fg4vw&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FWRxba4Fg4vw%2Fhqdefault.jpg&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=WRxba4Fg4vw",
  "title": "How to integrate your Shopify Store | Plural Payment Gateway",
  "favicon": "https://www.youtube.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/WRxba4Fg4vw/hqdefault.jpg",
  "provider": "youtube.com",
  "href": "https://www.youtube.com/watch?v=WRxba4Fg4vw",
  "typeOfEmbed": "youtube"
}
[/block]


## Integration Steps

Follow the below steps to integrate with Plural Shopify plugin.

1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/shopify#step-1-installation" >Installation</a>
2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/shopify#step-2-configuration" >Configuration</a>
3. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/shopify#step-3-payment-settings-and-activation" >Payment Settings and Activation</a>

### Step 1: Installation

1. To begin the setup process, log in to your Shopify account and select the store where you want to set up the Plural provider.
2. Navigate to Shopify app store [here](https://apps.shopify.com/plural) and click on** Install**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/120654cad2cc35935420b09cdaaf5a7a48af8ea5a89fc3df8bd53f6964f655d8-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


### Step 2: Configuration

1. After installing the app, you will be taken to the Plural app configuration page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0b875ece5e6fb402894d452efd1c7c1aed1a6364bea547eb70316c5092f1119a-Configuration.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


2. Set up the following details:

- Merchant ID (MID)
- Access Code
- Security Code

> 📘 Note:
> 
> Contact the support team to obtain details about your MID, Access Code, and Security Code.

3. Select the payment method you want to offer, such as Credit/Debit Cards, Net Banking, UPI, Wallet, and EMI. These options will be available to customers during checkout.
4. Then click on **Submit**.

### Step 3: Payment Settings and Activation

1. After configuring the credentials, navigate to **Payments** from the **Settings** tab in your Shopify store.
2. Then, select Plural as a supported payment method.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0e1399ecac5d0fd737bc64b2ada0068099707792d5074b5ed425e9918e4ca77f-Payment_setting.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


3. After selecting payment method, it will be redirected to the activation page. Click on **Activate** located at the bottom right corner. Before activating Plural, make sure that the **Test Mode** option is unchecked.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bb53d1939c187dec697c21ffc8802b950435339d270eb21ed5256a33ca13a51a-Activation_1.PNG",
        "",
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


> 📘 Note:
> 
> Enable Test Mode only when testing with the UAT API credentials.

## Payment Checkout

- Plural by Pine Labs now appear as a payment gateway on your Shopify store checkout.
- To initiate a transaction using Plural by Pine Labs, navigate to your Shopify stores, then add an item to the cart and proceed to checkout.
- During checkout, select the Pine Labs payment option and complete the payment.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8fd0b670ba471c644cc30b7558ee5b06ce52f264e82485976149dde039b3ba23-Checkout.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


## Manage Transactions

- Once the payment is successfully processed, verify the transaction on your<a style="text-decoration:underline;" href="https://developer.pluralonline.com/v3.0/reference/orders-capture" target="_blank">Plural by Pine Labs Dashboard</a>, to check the status of the transaction along with the Pine Labs Order ID.
- You can also go to **Orders** in your Shopify admin portal to view the transaction. The transaction details will automatically recorded, allowing you to track and manage all transactions for reporting and reconciliation purposes.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e6a36d95362331b100d91c80b6d2ac5e2a86de70dfb60c1515ce41ceecd6c937-Transaction.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "7px"
    }
  ]
}
[/block]
