---
title: "Python"
slug: "python"
excerpt: "Learn how to integrate and use Python SDKs with Pine Labs Plural APIs."
hidden: false
createdAt: "Fri Nov 15 2024 09:45:51 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Dec 03 2024 06:27:20 GMT+0000 (Coordinated Universal Time)"
---
This SDK provides an easy-to-use API for integrating Pine Labs services into your Python applications. It offers convenient methods for accepting and fetching orders, calculating EMIs, and verifying hashes.

Watch this video to learn how to integrate and use Python SDKs with Pine Labs Plural APIs. 

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FDd3sFpZ8Kco%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DDd3sFpZ8Kco&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FDd3sFpZ8Kco%2Fhqdefault.jpg&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=Dd3sFpZ8Kco",
  "title": "How to use Python SDKs with Pine Labs APIs",
  "favicon": "https://www.youtube.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/Dd3sFpZ8Kco/hqdefault.jpg",
  "provider": "youtube.com",
  "href": "https://www.youtube.com/watch?v=Dd3sFpZ8Kco",
  "typeOfEmbed": "youtube"
}
[/block]


<br />

> 📘 Download the Sampleapp
> 
> You can download the Sampleapp from the GitHub Link: <https://github.com/pluralonline/plural-python-sdk-sampleapp>.

## Installation

Follow the below steps for installing the SDK in your project:

1. Extract the SDK (ZIP file) to a location on your system. For example, the files can be extracted into a folder named python-sdk.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1f2dac9af56b972e0ca0f9de1b8ca48eb1a13effce5a881aafca92f257c1b4e5-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


2. Copy all files from the extracted folder to your Flask project or any Python framework you are using.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d4f802212da4fb7f79c053a5fcfab4f530af0d3f4c98dec69b0286b2ac95a5af-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


3. Import Files in Your Project:

   - In a sample setup, files are imported into a Flask project `(Flask_Sample_PineLab`) inside a newly created folder named `pinelabs`.
   - For this sample project, this step is already done, but in your own project, you will need to copy the files and organize them accordingly.

   [block:image]{"images":[{"image":["https://files.readme.io/c601262998dbffe5491602c46b49cf6c8de1b9f4781e3b04547904ff688f723e-image.png",null,""],"align":"center","sizing":"700px"}]}[/block]

   <br />
4. Ensure the folder structure in your IDE includes the SDK files alongside your main classes and packages.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/ab29a9c4adeb66da97269a94b15f221a6eaf15af94a4c41c7d895d59ed7b52b7-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


5. To use this SDK locally from a folder, copy the SDK folder into your project directory and import it into your Python file.

```python Python
from src.pinelabs import Pinelabs
```

## Implementation

- Refer to the <a href="https://github.com/pluralonline/plural-python-sdk" target="_blank">GitHub Document</a> for detailed instructions.

## Handle Payments

To know the status of the payment you can use the below options.

1. **<a href="<https://developer.pluralonline.com/v2.0/reference/payment-inquiry-refund" target="_blank">Inquiry API</a>**: Use this API to check transaction statuses.
2. **<a href="https://developer.pluralonline.com/v2.0/docs/developer-tools-webhook" target="_blank">Webhook Notification</a>**: We send Webhook notifications on the successful payment or any changes to the payment's response object.
