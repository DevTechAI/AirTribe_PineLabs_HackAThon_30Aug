---
title: "Redirect Checkout"
slug: "redirection-checkout"
excerpt: "Learn how to integrate with payment APIs for accepting payments via redirect checkout."
hidden: true
createdAt: "Thu Jun 27 2024 05:20:39 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Jun 27 2024 11:22:13 GMT+0000 (Coordinated Universal Time)"
---
Integrating with our Redirect Checkout is simple. It enables you to accept payments directly from your website. 

Plural handles the entire payment process, and you can customize payment options. Additionally, you can easily create a secure hosted checkout link through Plural. Once payments are successful, your customers are redirected back to your website.

## Workflow

Using Plural APIs you can start accepting payments on your website in two steps.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0acab87-Group_14.png",
        "",
        "Figure: Redirect Checkout Workflow"
      ],
      "align": "center",
      "caption": "Figure: Redirect Checkout Workflow"
    }
  ]
}
[/block]


1. **Prerequisite**:  
   First, convert the JSON into a Base64 Encode. Use the Base64 Encode and the secret keys to generate a HashMap using the SHS256 algorithm.
2. **Generate Payment Link**: Use the HashMap generated as the authorization header of our Accept Payment API. Additionally, pass the encoded Base64 in the request body and trigger our Accept Payments API. In response to that request, we send you the generated payment link to start accepting your payment.
3. **Accept Payment**: Redirect your customers to the payment link returned in the API response to accept payments. Once the payment is completed we return your customer back to your website.

## Use Cases
