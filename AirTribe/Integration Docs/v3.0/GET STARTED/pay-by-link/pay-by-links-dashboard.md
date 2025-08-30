---
title: "Dashboard"
slug: "pay-by-links-dashboard"
excerpt: "Learn how to create a payment link via Plural dashboard."
hidden: true
createdAt: "Tue Mar 18 2025 09:06:02 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri May 02 2025 11:13:02 GMT+0000 (Coordinated Universal Time)"
---
Pay by Links offers a simple and efficient way to accept remote payments for goods and services without the need for a complex payment gateway integration. With this no-code solution, you can easily create customizable payment links directly from the Plural Dashboard. Once generated, these links can be shared with your customers via SMS and email, allowing them to complete transactions securely and swiftly.

## Create a Payment Link

To create a Payment Link using your product and customer details, follow these steps in the Plural Dashboard:

1. Log in to the <a style="text-decoration:underline;" href="https://dashboardv2.pluralonline.com/login" target="_blank">Plural Dashboard</a>.
2. Navigate to the left-hand menu and select **Payment Links** under the **Other Products** section.
3. Click the **Create New Payment Link** button located at the top right corner of the page.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/42473bbbe7ba39317731f86fd21e5eac299650590f6543a84872b9b899ec70ad-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


3. Payment Link screen appears, enter the payment details.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/96a2005b4fdc9f53a0544f730cca828fbfe8885d88ad054ecb92c95ce8afce46-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


4. Enter Payment details

Fill in the required fields to configure your payment link:

- **Amount**: Enter the payment amount for the transaction (e.g., ₹500 for a product or service).
- **Description**: Add a short description of the payment purpose (e.g., "Monthly Gym Subscription" or "Product Purchase").
- **Product Code**: Merchant product code (required if brand EMI enabled).
- **Accepted Payment Modes**: Select the payment methods you want to accept through the link, such as UPI, credit/debit cards, wallets, or others.
- **Customer’s Email ID**: Add the customer’s email address if you want to send them an automatic receipt or payment reminder.
- **Customer Mobile No** (Optional): Add the customer’s mobile number if you want to send them an automatic receipt or payment reminder.
- **Expiry Date**: Set an expiry date for the payment link, which will automatically deactivate the link after the specified date.
- **Payment Link Settings**: You may have the option to enable or disable features like **Accept Payment in Parts** (e.g., partial payments or installment payments) if your plan supports such options.

5. Finally, click on **Create Payment Link**.  
   The payment link is created successfully and shared with your customers via email and SMS.

> 📘 **Note**:
> 
> **Link Expiration**: Set an expiration date for time-sensitive transactions to ensure that the payment link is only valid for a set period.

## Handle Payments

Once the payment is successfully processed, verify the transaction on your Plural Dashboard, to check the status of the transaction.

To know the status of the payment you can use the below option.

1. **Webhook Notification**: We send Webhook notifications on the successful payment or any changes to the payments object. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/developer-tools-webhook" target="_blank">Webhooks</a> documentation to learn more.
