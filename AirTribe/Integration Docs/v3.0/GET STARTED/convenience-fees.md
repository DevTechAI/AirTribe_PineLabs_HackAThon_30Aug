---
title: "Convenience Fees"
slug: "convenience-fees"
excerpt: "Learn how you can collect convenience fees from your customers against an order."
hidden: false
createdAt: "Thu Dec 12 2024 06:35:15 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Dec 17 2024 04:28:33 GMT+0000 (Coordinated Universal Time)"
---
With the Plural Convenience Fee feature, you can configure fees for each payment made through Plural. This allows you to charge an additional amount to your customers, helping to recover costs such as online payment gateway charges. This can be implemented on all the payment methods we support on Plural. 

By Integrating with the Plural convenience fee feature you can aim to recover the costs you pay to Plural for processing a payment. This fee can be a fixed amount, a percentage, or a combination.

If a refund is initiated by the system, your customers receive both the convenience fee and the original payment amount. However, if a refund is initiated by your customers, they only receive the original payment amount, excluding the convenience fee.

**Pre-requisites**

To implement this feature, you must be configured with the following settings:

- The surcharge fee flag must be enabled on you merchant ID.
- Convenience fees should be defined for the specific payment methods you intend to use.

## Calculate Convenience Fee

You can use the Plural API to calculate the convenience fee charged for processing a payment. Refer to our Calculate Convenience Fee API to know more.
