---
title: "Pay By Points"
slug: "pay-by-points-about"
excerpt: "Learn how to Integrate with Plural pay by points to redeem seamless loyalty points for Instant purchases."
hidden: false
createdAt: "Tue Sep 10 2024 09:08:13 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Oct 18 2024 03:09:45 GMT+0000 (Coordinated Universal Time)"
---
## Overview

**Pay by Points** allows your customers to redeem their loyalty or reward points as a form of currency, giving them more flexibility than traditional reward catalogs offered by banks or issuing brands. This feature enables your customers to use their points for purchases with any merchant or business, offering a convenient and rewarding shopping experience.

With **Plural Pay by Points**, your customers can seamlessly apply their reward points to online transactions processed, enhancing their overall shopping experience. This feature not only encourages higher conversions and satisfaction but also gives your customers a competitive advantage.

Our solution effectively integrates loyalty programs with payment options, driving customer engagement and satisfaction while giving your business an edge in the market.

## Integration Types

You can integrate Pay by Points using either Plural Hosted Checkout or Seamless Checkout Integration. 

1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/plural-hosted-checkout" >**Plural Hosted Checkout : ** </a> Integrating with Plural Hosted Checkout, you can effortlessly accept payments through reward points. To enable this feature, you must first be configured for **Pay by Points** and contact our Plural team to get configured. Once configured, you can begin accepting point-based payments without any additional setup.

Below are the sample screens generated for a payment via pay by points through Plural Hosted Checkout.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2d59bdcd972ce7741795b023d4ebe41284ca0da3dfde282c459f18db5b107efc-Screenshot_2024-09-03_at_4.04.18_PM.png",
        "",
        "User Interaction with Pay By Points"
      ],
      "align": "center",
      "caption": "Plural Hosted Checkout - User Interaction with Pay By Points"
    }
  ]
}
[/block]


2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/pay-by-points-integration-steps" >**Seamless Checkout : ** </a> Integrating with Seamless checkout, allows you to tailor the user experience for your customers. Follow the step-by-step procedure outlined in the Seamless Checkout integration guide for a smooth implementation.

> 🚧 Watch Out
> 
> - To Integrate with Plural seamless checkout flow you must have a PCI compliance certificate.

***

## PBP Flow

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/380791349f364f657f0786362acb5518d68567e211be8879b49c302355fe467d-image.png",
        null,
        "Figure: PBP Functional Flow"
      ],
      "align": "center",
      "border": true,
      "caption": "Figure: PBP Functional Flow"
    }
  ]
}
[/block]


## Product Features

1. **Real-time Point Balance**:

- Customers can view their point balance before finalising the transaction.
- Point-to-INR conversion rates available via API call to ensure transparency.

2. **Seamless integration/ Server-to-Server (S2S) payment processing:**

- Pay by Points is integrated into Plural’s Seamless platform, allowing you to plug and play using the same APIs easily.
- Instant discount realisation at product page and seamless payment with points at checkout.

3. **Efficient Settlements:**

- Merchants can enjoy efficient reconciliation with settlement options available within T+2.

***

## List of Supported Banks

Your business can offer customers the enticing option to pay with Credit card and debit card points issued by 14 Indian banks across 15 reward programs.

| List of Supported banks   |
| :------------------------ |
| State Bank of India (SBI) |
| Yes Bank                  |
| Federal Bank              |
| Canara Bank               |
| Punjab National Bank      |
| Union Bank of India       |
| Bank of India             |
| Karur Vysya Bank          |
| South Indian Bank         |
| Central Bank of India     |
| Indian Bank               |
| DBI Bank                  |
| AU Small Finance Bank     |
| IDFC First Bank           |

***

## Refunds

Use our refunds API to refund the payment against an order. This typically happens when a customer returns a product, cancels a service, or faces an issue with their purchase. The purpose is to reverse the original transaction and return the funds to the customer.

With Plural refund API, you can initiate a refund as listed below.

1. **Full Refund**: To refund the complete order amount.
2. **Partial Refund**: To refund the specific amount against an order.

> 👍 Refunds of expired points:
> 
> - Refunds to your customers are not allowed for the corresponding amounts to expired points. However, we will ensure to settle you with the equivalent amount for the expired points.
> - When you try to process a refund for a points transaction, we display the following message on the Merchant dashboard. **Points that have expired cannot be refunded to the customer, but they will be refunded to you. Please use your discretion in managing this amount with your customers**.
