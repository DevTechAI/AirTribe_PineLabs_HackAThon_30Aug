---
title: "Dot Net"
slug: "dot-net"
excerpt: "Learn how to integrate and use .NET SDK with Pine Labs Plural APIs."
hidden: false
createdAt: "Fri Nov 15 2024 09:44:42 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Dec 03 2024 06:27:20 GMT+0000 (Coordinated Universal Time)"
---
This SDK provides an easy-to-use API for integrating Pine Labs services into your .NET applications. It offers convenient methods for accepting and fetching orders, calculating EMIs, and verifying hashes.

Watch this video to learn how to integrate and use .NET SDK with Pine Labs Plural APIs. 

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FmlkoTTYKe5Q%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DmlkoTTYKe5Q&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FmlkoTTYKe5Q%2Fhqdefault.jpg&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=mlkoTTYKe5Q",
  "title": "Dot Net Integration: A step-by-step tutorial of Plural by Pine Labs SDK integration",
  "favicon": "https://www.youtube.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/mlkoTTYKe5Q/hqdefault.jpg",
  "provider": "youtube.com",
  "href": "https://www.youtube.com/watch?v=mlkoTTYKe5Q",
  "typeOfEmbed": "youtube"
}
[/block]


> 📘 Download the Sampleapp
> 
> You can download the Sampleapp from the GitHub Link: <https://github.com/pluralonline/plural-dotnet-sdk-sampleapp>.

## Installation

Follow these below steps to install and integrate the Pine Labs SDKs into your project:

**Step 1**: Download the Pine Labs SDK and extract the content to a folder on your system.

**Step 2**: Open an existing project or set up a new project in your system.

**Step 3**: Add SDKs reference:

- Navigate to the extracted SDK folder: `SDK\bin\Debug\net7.0\PineLabsSdk.dll`.
- Add a reference to this DLL file in your project.

**Step 4**: Update the project File:

- Open your `.csproj` file in a text editor.
- Add the following reference configuration:

```java Reference configuration
<ItemGroup>
    <Reference Include="PineLabsSdk">
        <HintPath>SDK\bin\Debug\net7.0\PineLabsSdk.dll</HintPath>
    </Reference>
</ItemGroup>
```

- The SDK is now integrated into your project and ready for use.

## Implementation

- Refer to the <a href="https://github.com/pluralonline/plural-dotnet-sdk" target="_blank"> GitHub Document</a> for detailed instructions.

## Handle Payments

To know the status of the payment you can use the below options.

1. **<a href="<https://developer.pluralonline.com/v2.0/reference/payment-inquiry-refund" target="_blank">Inquiry API</a>**: Use this API to check transaction statuses.
2. **<a href="https://developer.pluralonline.com/v2.0/docs/developer-tools-webhook" target="_blank">Webhook Notification</a>**: We send Webhook notifications on the successful payment or any changes to the payment's response object.
