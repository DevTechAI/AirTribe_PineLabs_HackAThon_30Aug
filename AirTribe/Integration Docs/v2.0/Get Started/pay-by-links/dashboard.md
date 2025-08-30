---
title: "Dashboard"
slug: "dashboard"
excerpt: "Learn how to create a payment link via dashboard."
hidden: false
createdAt: "Mon Nov 11 2024 04:42:44 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Nov 21 2024 06:31:17 GMT+0000 (Coordinated Universal Time)"
---
Pay by Links offers a simple and efficient way to accept remote payments for goods and services without the need for a complex payment gateway integration. With this no-code solution, you can easily create customizable payment links directly from the Pine labs Dashboard. Once generated, these links can be shared with your customers via SMS and email, allowing them to complete transactions securely and swiftly.

## How to create a Payment Link?

To create a Payment Link using your product and customer details, follow these steps in the Pine Labs dashboard:

1. Log in to the Pine Labs Dashboard.
2. Navigate to the Payment Links section and click on **Create New Payment Link**.

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


3. Create Payment Link screen appears, enter the payment details.

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


4. Enter payment link details

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

Once the payment is successfully processed, verify the transaction on your Plural by Pine Labs Dashboard, to check the status of the transaction.

To know the status of the payment you can use the below option.

**<a href="https://developer.pluralonline.com/v2.0/docs/developer-tools-webhook" target="_blank">Webhook Notification</a>**: We send Webhook notifications on the successful payment or any changes to the payment's response object.
