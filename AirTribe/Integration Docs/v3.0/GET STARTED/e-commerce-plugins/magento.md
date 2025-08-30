---
title: "Magento"
slug: "magento"
excerpt: "Learn how to Install Plural Plugin on Magento platform."
hidden: false
createdAt: "Tue Oct 29 2024 07:23:26 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Feb 27 2025 06:48:04 GMT+0000 (Coordinated Universal Time)"
---
**Platform**: Magento  
**Supported Versions**: 2.3.4v to 2.4.5v

Integrating with the Plural Magento Plugin enables seamless payment processing through credit cards, debit cards, and EMI options via the PinePG Edge platform. Below is a simple, step-by-step guide to help you install and configure the PinePG Edge Plugin on your Magento site for smooth transactions.

## Integration Steps

### 1. Download the Extension

1. Navigate <a style="text-decoration:underline" href="https://github.com/plural-pinelabs/magento-plugin" target="_blank">here</a> to download the extension file.
2. Click on `Code`, then select `Download ZIP` to download the extension file.

### 2. Move Files to Magento Directory

1. Unzip the downloaded file.
2. Move the unzipped folder to the `app/code` directory in your Magento installation, where custom code and extensions are stored.

**Note**: If the code folder does not exist within `<root>/app`, create it.

### 3. Run Terminal Commands

- Open a terminal and navigate to your Magento root directory (where the bin directory and command-line tools are located).
- Run the following commands to enable the extension:

```text Terminal Commands
php bin/magento module:enable Pinelabs_PinePGGateway
php bin/magento setup:upgrade
php bin/magento setup:static-content:deploy
php bin/magento cache:clean
```

- These commands activate the extension and make it available in Magento.

### 4. Configure the Extension:

1. Log in to your **Magento** backend.
2. Go to Stores and Configuration.
3. Under Sales choose Payment Methods, you’ll find a list of available payment methods.
4. Locate and select the payment method provided by the extension.
5. Fill in the below following details:
   1. **Enable**: Select 'Yes' to enable the module.
   2. **Title**: Enter a name to display on the checkout page.
   3. **Select Cart Type**: Choose between Single and Multi-Cart options based on your credentials.
   4. **Merchant Id**: Enter the ID for the chosen Payment Environment (Test or Live).
   5. **Merchant Access Code**: Add the Access Code for the selected Payment Environment.
   6. **Merchant Secret**: Enter the Secret for the selected Payment Environment.
   7. **Merchant Payment Mode**: Specify the payment mode activated for your account.
   8. **Environment**: Choose 'Test' for testing or 'Live' for actual payments.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/da453e8ecb27a652275c3829ee8acafc25f491fbadd1854f407c0bdd5fbc59dd-Screenshot_2024-10-29_at_2.45.05_PM.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "70000px",
      "border": true
    }
  ]
}
[/block]


6. After configuration, check the extension on your checkout page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2518937505b14fd8e0d3008ca74ec6be1dcad94fd2ac45a8cfb98ad00a0763cc-Screenshot_2024-10-29_at_3.16.20_PM.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "700px",
      "border": true
    }
  ]
}
[/block]


7. Click `Place Order` to see the payment gateway options.
8. Upon successful payment, you’ll be redirected to a success page; otherwise, a failure page will appear.

> 📘 Note:
> 
> - Pine plugins do not handle shipping or additional charges (example: `TDR`, `GST`). 
> - Ensure that your cart value matches the product value, as any extra charges must be managed manually at the merchant end.
