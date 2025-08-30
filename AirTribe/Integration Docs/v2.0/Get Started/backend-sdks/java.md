---
title: "Java"
slug: "java"
excerpt: "Learn how to integrate and use Java SDK with Pine Labs Plural APIs."
hidden: false
createdAt: "Fri Nov 15 2024 09:44:05 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Dec 03 2024 06:27:20 GMT+0000 (Coordinated Universal Time)"
---
This document provides a step-by-step guide for integrating the Java SDK. It offers convenient methods for accepting and fetching orders, calculating EMIs, and verifying hashes.

Watch this video to learn how to integrate and use Java SDK with Pine Labs Plural APIs. 

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2Fq_Gct5Haynw%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dq_Gct5Haynw&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2Fq_Gct5Haynw%2Fhqdefault.jpg&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=q_Gct5Haynw",
  "title": "How to use Java SDKs with Pine Labs APIs",
  "favicon": "https://www.youtube.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/q_Gct5Haynw/hqdefault.jpg",
  "provider": "youtube.com",
  "href": "https://www.youtube.com/watch?v=q_Gct5Haynw",
  "typeOfEmbed": "youtube"
}
[/block]


> 📘 Download the Sampleapp
> 
> You can download the Sampleapp from the GitHub Link: <https://github.com/pluralonline/plural-java-sdk-sampleapp>.

## Prerequisites

Before integrating the SDK into your Project, make sure the following requirement is met:

- JDK version 17 or higher (recommended).
- Maven version 3 or higher (Recommended).

> 📘 Note:
> 
> TLS 1.2 information:
> 
> - For Java 17 and above should have TLS version 1.2.

## Installation

Follow the below steps for installing the SDK in your project:

1. Extract the SDK (Zip File) in any desired location on your system. For example, extracted it into a folder named `Sdk_PineLabs`(Sdk Folder: java-sdk).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/7e28ec56ca442de94eef1ab0b6ab2b45f20892ea214dace83c48b406b4211c5a-Screenshot_20-11-2024_19256_.jpeg",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


2. Navigate to the path `src/main/java/com/pine_lab/api` inside the `java-sdk` folder. And in that you’ll be  
   able to locate all the necessary classes, copy all the classes from this folder, except `App.java` (Testing Class), into your existing project’s repository or package.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/82496de3e91dc1a3ba0ea9bbb348ba8752b616bc250bccaf1811c44b0dcb118c-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


3. In your project, create a new package, such as `pine_lab/api`. Import all the SDK classes into this package. For instance, in a sample Spring Boot project (`Java_Pine_Labs`), you can create the package and inject the SDK classes into it.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/200899f72a56ebf49dd2632282bfe5bbfe789036b65b30ed4fff7cc512a13a26-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


4. In your IDE, the project structure should show the SDK files in the package `com/pine_lab/api`, while your main classes are in other packages (e.g., `com/pine_labs`). Ensure this structure is reflected correctly.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f16b49f962c5ce61685efc8ce53d06f1b696cb34ddea8dbf72ad455ecef6f283-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


5. In your main controller class, import the required SDK classes. For example, in the sample Spring Boot project, you can include an import statement like:

```java Java
import com.pine_lab.api.Api;
```

Follow a similar process for importing other classes as needed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/610695c0374122c70a444869dc4dd9723b20ca2d9c7e28da9341f665e7fad50d-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


6. Copy all the dependencies from the SDK’s `pom.xml` file and add them to your project’s` pom.xml`. Below reference image shows xml file of SDK.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a539530399f6d357aca6b2bb3126fc9602bc10167138ad557fdad013b77406d6-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


## Implementation

- Refer to the <a href="https://github.com/pluralonline/plural-java-sdk" target="_blank">GitHub Document</a> for detailed instructions.

## Handle Payments

To know the status of the payment you can use the below options.

1. **<a href="<https://developer.pluralonline.com/v2.0/reference/payment-inquiry-refund" target="_blank">Inquiry API</a>**: Use this API to check transaction statuses.
2. **<a href="https://developer.pluralonline.com/v2.0/docs/developer-tools-webhook" target="_blank">Webhook Notification</a>**: We send Webhook notifications on the successful payment or any changes to the payment's response object.
