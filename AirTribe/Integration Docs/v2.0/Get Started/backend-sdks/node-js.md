---
title: "Node.js"
slug: "node-js"
excerpt: "Learn how to integrate and use Node.js SDK with Pine Labs Plural APIs."
hidden: false
createdAt: "Fri Nov 15 2024 09:45:13 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Dec 03 2024 06:27:20 GMT+0000 (Coordinated Universal Time)"
---
This SDK provides an easy-to-use API for integrating Pine Labs services into your Node applications. It offers convenient methods for accepting and fetching orders, calculating EMIs, and verifying hashes.

Watch this video to learn how to integrate and use Node.js SDK with Pine Labs Plural APIs. 

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FnW4Axoz292c%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DnW4Axoz292c&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FnW4Axoz292c%2Fhqdefault.jpg&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=nW4Axoz292c",
  "title": "How to use Node SDK",
  "favicon": "https://www.youtube.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/nW4Axoz292c/hqdefault.jpg",
  "provider": "youtube.com",
  "href": "https://www.youtube.com/watch?v=nW4Axoz292c",
  "typeOfEmbed": "youtube"
}
[/block]


> 📘 Download the Sampleapp
> 
> You can download the Sampleapp from the GitHub Link: <https://github.com/pluralonline/plural-nodejs-sdk-sampleapp>.

## Prerequisites

Before integrating the SDK into your Project, make sure the following requirement is met:

1. NODE version 18.17.1 or higher.
2. NPM version 9.6.7 or higher.

> 📘 Note:
> 
> TLS 1.2 information:
> 
> - For NODE version 18.17.1 and above should have TLS version 1.2.

## Installation

To install this SDK locally from your folder, run the following command. This will link and integrate the SDK into your Node.js project.

```node Command
npm link "../path-to-sdk-folder"
npm install "../path-to-sdk-folder"
```

## Implementation

- Refer to the <a href="https://github.com/pluralonline/plural-nodejs-sdk" target="_blank">GitHub Document>/a> for detailed instructions.

## Handle Payments

To know the status of the payment you can use the below options.

1. **<a href="<https://developer.pluralonline.com/v2.0/reference/payment-inquiry-refund" target="_blank">Inquiry API</a>**: Use this API to check transaction statuses.
2. **<a href="https://developer.pluralonline.com/v2.0/docs/developer-tools-webhook" target="_blank">Webhook Notification</a>**: We send Webhook notifications on the successful payment or any changes to the payment's response object.
