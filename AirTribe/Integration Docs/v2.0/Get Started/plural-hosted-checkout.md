---
title: "Plural Hosted Checkout"
slug: "plural-hosted-checkout"
excerpt: "Learn how to integrate with Plural Hosted Checkout to accept payments."
hidden: false
createdAt: "Thu Jun 27 2024 05:20:39 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Sep 30 2024 07:27:42 GMT+0000 (Coordinated Universal Time)"
---
Integrating with Plural checkout is simple. It enables you to accept payments directly from Plural hosted checkout. 

Plural handles the entire payment process, and you can customize payment options. Additionally, you can easily create a secure hosted checkout link through Plural. Once payments are successful, your customers are redirected back to your website.

## Workflow

Using Plural APIs you can start accepting payments on Plural hosted checkout in two steps.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4a854afafc68d7e518605814a5b035643344832767af70ca1197fd10113a5957-Group_81_1.png",
        "",
        "Figure: Redirect Checkout Workflow"
      ],
      "align": "center",
      "border": true,
      "caption": "Figure: Plural Hosted Checkout Workflow"
    }
  ]
}
[/block]


Follow the below steps to start accepting payment using Plural hosted checkout.

1. **Accept Payment**: Use the HashMap generated as the authorization header of our Accept Payment API. Additionally, pass the encoded Base64 in the request body and trigger our Accept Payments API. In response to that request, we send you the generated payment link to start accepting your payment.
2. **Handle Payment**: Redirect your customers to the payment link returned in the API response to accept payments. Once the payment is completed we return your customer back to your website.

## Advantages

- **Security and Reliability**: Plural Payment Gateway creates a secure pathway between your customers and your business, safeguarding sensitive financial data through robust encryption protocols. This security extends to both sides of the transaction, ensuring peace of mind for both you and your customers.
- **Versatile Payment Options**: Accept payments through a variety of methods including credit and debit cards, UPI, net banking, wallets, and our Affordability Suite, providing flexibility to your customers and enhancing their purchasing power.
- **Advanced Transaction Management**: Manage your transactions effectively with our intuitive dashboard. Track payment statuses, manage refunds, handle disputes, and analyze your business performance—all from a single interface. Send payment links directly to customers, facilitating easy payments without the need for full integration.
- **Affordability Suite**: Big purchases made possible with Plural’s Affordability Suite. Get the widest range of payment options including debit card EMIs, credit card EMIs, low-cost EMIs, and more. This feature allows your customers to make significant purchases more manageable, spreading the cost over time with flexible payment solutions.

## Card Transaction Flow

The flow diagram shows the typical flow of a card transaction using the Plural checkout.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bd2bd2a490b9df53b862a26f32720233fcf2ebd7aa740a71372c4d949ea45bf4-Screenshot_2024-08-28_at_5.05.48_PM.png",
        "",
        "Figure: Card Transaction Flow"
      ],
      "align": "center",
      "caption": "Figure: Card Transaction Flow"
    }
  ]
}
[/block]
