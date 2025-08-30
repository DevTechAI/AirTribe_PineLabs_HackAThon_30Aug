---
title: "WooCommerce"
slug: "woocommerce"
excerpt: "Learn how to Install Plural Plugin on WooCommerce platform."
hidden: false
createdAt: "Tue Oct 22 2024 04:27:47 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Mar 12 2025 10:15:24 GMT+0000 (Coordinated Universal Time)"
---
**Platform**: WordPress  
**Supported Versions**: 3.6.3v to 7.2.2v

Integrating with the Plural WooCommerce Plugin enables seamless payment processing through credit cards, debit cards, and EMI options via the PinePG Edge platform. Below is a simple, step-by-step guide to help you install and configure the PinePG Edge Plugin on your WordPress site for smooth transactions.

Learn how to integrate your WooCommerce site with the Plural Payment Gateway. Watch the video tutorial below for a step-by-step guide.

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FYh5bWPbWbHM%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DYh5bWPbWbHM&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FYh5bWPbWbHM%2Fhqdefault.jpg&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=Yh5bWPbWbHM",
  "title": "How to integrate the Plural Payment Gateway with WooCommerce",
  "favicon": "https://www.youtube.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/Yh5bWPbWbHM/hqdefault.jpg",
  "provider": "youtube.com",
  "href": "https://www.youtube.com/watch?v=Yh5bWPbWbHM",
  "typeOfEmbed": "youtube"
}
[/block]


## Integration Steps

The figure below shows the steps involved to Instal Plural plugin.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0fd553d62631a19ab551e3574b434b2acc4f01e20840dd127884f6c47429f82a-Group_1171279975_2.png",
        "",
        "Figure: WooCommerce Integration Steps"
      ],
      "align": "center",
      "sizing": "500px",
      "border": true,
      "caption": "Figure: WooCommerce Integration Steps"
    }
  ]
}
[/block]


### 1. Download the Extension

1. Navigate <a style="text-decoration:underline" href="https://github.com/plural-pinelabs/woocommerce-plugin" target="_blank">here</a> to download the extension file.
2. Click on `Code`, then select `Download ZIP` to download the extension file.

### 2. Plugin Installation

You can install the plugin using one of the methods outlined below.

#### 2.1. WordPress Plugin Installer:

Follow the below steps to install the plugin using WordPress Plugin Installer:

1. Log in to your <a href="https://login.wordpress.org/wp-login.php" target="_blank">WordPress</a> account with admin privileges.
2. Go to the **Plugins** tab in the dashboard.
3. Click on the **Add New Plugin** button.
4. Then, select the **Upload Plugin** option.
5. Click on **Choose File** and upload the previously downloaded zip file.
6. Once the file is uploaded, click the **Install Now** button.
7. After installation, click **Activate**.
8. Once activated, you will see a confirmation message, and the plugin will appear under the name "Edge by Pine Labs for WooCommerce" in your installed plugins list.

#### 2.2. Manual Installation:

1. Unzip the downloaded file and locate the folder inside.
2. Copy this folder and paste it into the `<wordpress root>/wp-content/plugins` directory of your WordPress installation.
3. Log in to the **WooCommerce** admin panel and go to the Plugins section.
4. Find the Edge Plugin and click **Activate**.

### 3. Plugin Configuration

Configuring a plugin involves setting up and fine-tuning its settings to ensure it functions effectively. Follow the below steps to configure the WooCommerce Plugin.

1. Navigate to WooCommerce > **Settings**.
2. Go to the **Payments** tab.
3. Click on the Edge plugin to configure it.
4. Confirm that the payment method provided by the plugin appears in the list. If it’s listed, the installation was successful and is ready to use.
5. Fill in the required fields:
   1. **Merchant Key, Access Code, Merchant Secret**: Enter the information provided for the selected environment.
   2. **Enable**: Select `Yes` to enable the module.
   3. **Cart System**: Choose `Single Cart` or `Multi-Cart` depending on your configuration credentials.
   4. **Description**: Provide a description to display during checkout.
   5. **Gateway Mode**: You can set it to `Sandbox` while testing the plugin or `Production` to start live payments from your platform.
   6. **Merchant ID**: Enter the merchant ID based on the selected environment (Test / Live).
   7. **Merchant Access Code and Merchant Secret**: Provide the credentials specific to the chosen environment.
   8. **Payment Mode**: Select the active payment mode for your merchant account.
   9. **Return Page**: Set to "My Account" by default, or select a custom page to display after payment completion. Custom pages should include the necessary WordPress/WooCommerce code for any special messages. Consult the WordPress/WooCommerce development guide for more on custom page setup.  
      Once completed, click on the save changes button.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/bf06b515fc1c4277b99f245e1cab22008a92e5f32cdeed68ae62ba5c9ce3c8bc-Screenshot_2024-10-28_at_4.08.24_PM.png",
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


6. After successfully installing the extension, you can see the payment method for your extension on your Checkout Page.  
   For example, when you click Place Order you will see the payment gateway window where you must choose your payment options.
7. After completing the payment successfully you will be redirected to the transaction `Success` page or a `Failure` page.

> 📘 Note:
> 
> - Plural Plugins do not apply shipping fees or any additional charges. Therefore, the cart value should match the product value.
> - Please note that any additional fees, such as TDR, GST, or others, are not managed by our plugins and must be handled manually by the merchant.
