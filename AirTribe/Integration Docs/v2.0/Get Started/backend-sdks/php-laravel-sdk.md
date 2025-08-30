---
title: "PHP"
slug: "php-laravel-sdk"
excerpt: "Learn how to integrate and use Plural PHP SDK with your PHP based website to accept payments."
hidden: false
createdAt: "Fri Nov 15 2024 09:41:33 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Dec 03 2024 06:27:20 GMT+0000 (Coordinated Universal Time)"
---
This document provides a step-by-step guide for integrating the Plural's PHP Laravel SDK. It offers convenient methods for accepting and fetching orders, calculating EMIs, and verifying hashes.

Watch this video to learn how to integrate Plural PHP Laravel SDK for your PHP applications. 

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2F8n43-5REBQY%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D8n43-5REBQY&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2F8n43-5REBQY%2Fhqdefault.jpg&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=8n43-5REBQY",
  "title": "How to integrate PHP Laravel SDK for PHP applications",
  "favicon": "https://www.youtube.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/8n43-5REBQY/hqdefault.jpg",
  "provider": "youtube.com",
  "href": "https://www.youtube.com/watch?v=8n43-5REBQY",
  "typeOfEmbed": "youtube"
}
[/block]


> 📘 Download the Sampleapp
> 
> You can download the Sampleapp from the GitHub Link: <https://github.com/pluralonline/plural-php-laravel-sdk-sampleapp>.

## Prerequisites

Before integrating the SDK into your Project, make sure the following requirements are met:

1. PHP version 7.4 or higher, up to 8.1.
2. Composer installed in your project.

> 📘 Note:
> 
> TLS 1.2 information:
> 
> - For PHP 5.5.19 and above should have TLS version 1.2.
> - For PHP 7 and above, TLS version 1.2 is typically available.

## Installation

If your project uses Composer for managing dependencies, you can easily install the PHP library by  
following these steps:

1. Open your terminal or command prompt.
2. Navigate to your project's root directory where your`composer.json` file is located.
3. Run the below Composer command to install the PHP library:

```json Use Composer Command
composer require pinelabs/php
```

To locally add a PHP library to your `composer.json` file, follow these steps:

1. Download the PHP library and place it in a directory within your project. You can obtain the  
   library files from a source like GitHub, or by downloading a release archive.
2. In your PHP library, make sure it has an autoloading mechanism defined, usually within a  
   `composer.json` file. This is important to ensure that Composer can autoload the library's classes.  
   An example `composer.json` file for the library might look like this:

```json Json
{
  "name": "vendor-name/library-name",
  "autoload": {
    "psr-4": {
      "VendorName\\LibraryName\\": "src/"
    }
  }
}
```

3. Open your project's composer.json file and add a reference to the locally downloaded library. To  
   do this, you can use the path repository type. Add a repositories section and specify the local  
   path to the library, like this:

```json Json
{
  "repositories": [
    {
      "type": "path",
      "url": "relative/path/to/library"
    }
  ],
  "require": {
    "vendor-name/library-name": "*"
  }
}
```

Example file using Pine Labs SDK:

```json Json
{
  "repositories": [
    {
      "type": "path",
      "url": "./pinelab-sdk"
    }
  ],
  "require": {
    "pinelabs/php":"@dev"
  }
}
```

Replace `relative/path/to/library` with the actual path to the directory where the library is  
located within your project.

4. After updating your project's `composer.json` file, open your terminal or command prompt,  
   navigate to your project's root directory (where the `composer.json` file is located), and run:

```json Command
composer update
```

> 📘 Note:
> 
> 1. Use Composer Install or Composer Update to ensure you have the latest version of the library.
> 2. The SDK is namespaced under `Pinelabs\Php`.
> 3. The API returns errors instead of throwing exceptions.
> 4. Options are passed as an array instead of multiple arguments, wherever applicable, to ensure greater flexibility and easier configuration.

## Implementation

- Refer to the <a href="https://github.com/pluralonline/plural-php-laravel-sdk?tab=readme-ov-file#php-laravel-sdk" target="_blank">GitHub Document</a> for detailed instructions.

## Handle Payments

To know the status of the payment you can use the below options.

1. **<a href="<https://developer.pluralonline.com/v2.0/reference/payment-inquiry-refund" target="_blank">Inquiry API</a>**: Use this API to check transaction statuses.
2. **<a href="https://developer.pluralonline.com/v2.0/docs/developer-tools-webhook" target="_blank">Webhook Notification</a>**: We send Webhook notifications on the successful payment or any changes to the payment's response object.
