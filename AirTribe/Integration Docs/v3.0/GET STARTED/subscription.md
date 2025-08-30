---
title: "Subscription"
slug: "subscription"
excerpt: "Learn how to integrate with Plural Subscription using Plural APIs to allow your users to make recurring payments."
hidden: false
createdAt: "Thu Feb 27 2025 05:56:01 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Apr 17 2025 05:11:17 GMT+0000 (Coordinated Universal Time)"
---
A subscription is a recurring billing model where customers pay an amount at pre-defined intervals (monthly, annually, etc.) for access to your product or service. This creates a predictable revenue stream for your business and fosters long-term customer relationships. These are automated payments on schedule that are pre-defined by you.

## Use Cases

1. **OTT Platforms**: Streaming services offer subscriptions for on-demand movies, series, and exclusive content. With different payment method, you can set up recurring payments for their monthly or annual subscriptions, ensuring uninterrupted access to entertainment without the hassle of manual renewals.
2. **E-Learning Platforms**: Online learning platforms provide subscriptions for courses, certifications, and exclusive materials. Subscriptions streamline access to content, with periodic payments enabling continuous learning without disruptions.
3. **E-commerce Subscriptions**: E-commerce platforms provide subscription models for curated product deliveries, such as beauty boxes or groceries. Customers can choose a subscription plan, enabling automatic periodic payments and deliveries without needing to reorder each time.

## Key Features

1. **Create Plan**

Our Create Plan API enables you to set up flexible subscription plans by defining essential details such as the plan name, duration (start and end date), billing frequency, amount, maximum limit, and the number of users allowed. This helps in creating tailored subscription models to meet your business needs. Additionally, the Get Plans API allows you to retrieve a complete list of all the plans you have created, providing a clear overview for efficient management and quick access to plan details.

2. **Trial Period**

- You can offer a trial period for your subscriptions. During this trial, no charges will be deducted from the end-user's account.
- Simply define the desired trial period duration (in days).
- Debits will be triggered automatically at the end of the trial period.
- While in the trial state, the customer's approved mandate will remain in the TRIAL state.
- Upon a successful debit, the mandate's status will automatically change from CREATED to ACTIVE.
- Trial Period is not applicable for OT frequency

3. **Billing Frequency**  
   Our system allows you to easily define the debit frequency for your subscriptions. Select from the following options to determine how often the customer needs to be charged:

[block:parameters]
{
  "data": {
    "h-0": "Frequency",
    "h-1": "Parameters and Definition",
    "0-0": "Daily",
    "0-1": "1 (Every day)",
    "1-0": "Weekly",
    "1-1": "1 (Every Week)",
    "2-0": "Monthly",
    "2-1": "1 (Once every month)",
    "3-0": "Yearly",
    "3-1": "4 (Once every quarter)  \n2 (Once every half year)  \n1 (Once every year)",
    "4-0": "AS",
    "4-1": "As-Presented (anytime during the subscription period)",
    "5-0": "OT",
    "5-1": "One-Time (Anytime but once during the subscription period)"
  },
  "cols": 2,
  "rows": 6,
  "align": [
    "left",
    "left"
  ]
}
[/block]


4. **Pre-Debit Notification**  
   Your customer will receive a notification 24 hours before any debit is made from their account. This notification is mandatory as per RBI regulations and informs the customer about the scheduled debit for the following day.  
   Plural automatically triggers and transmits this notification on your behalf. You don’t need to take any action. The notification is sent via the customer’s registered PSP, as specified during the mandate setup.

> 📘 Note:
> 
> For a One-Time Mandate, sending a PDN is not required

5. **Presentation**  
   With the "**As-Presented**" frequency for subscriptions, you have control over when debits occur. This feature allows you to schedule debits flexibly according to your preferences. The debit amount can range from Re. 1 up to the maximum amount specified for the plan tied to the active subscription. In line with RBI guidelines, a pre-debit notification will be automatically sent to the customer 24 hours before the scheduled debit.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2e9fc4fade97f1e40a2324a431d6127e42b47a0a560518dc029ed536a24a6dec-Presentation_FINAL_RELEASED_03-03-2025.jpg",
        null,
        "Figure: Presentation Status"
      ],
      "align": "center",
      "sizing": "700px",
      "border": true,
      "caption": "Figure: Presentation Status"
    }
  ]
}
[/block]


<br />

The table below list the various states of a Presentation.

| Status          | Description                                                                                                                                                                                                 |
| :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PDN SCHEDULED   | Pre-Debit Notification is scheduled. Only applicable if debit date is more than 48hrs from current timestamp.                                                                                               |
| PDN INITIATED   | Pre-Debit Notification is initiated.                                                                                                                                                                        |
| PDN SUCCESS     | Pre-Debit Notification is successful                                                                                                                                                                        |
| PDN FAILED      | Pre-Debit Notification has failed. Our system will trigger internal retries.                                                                                                                                |
| DEBIT SCHEDULED | Debit is scheduled. Only applicable when debit date is more than 48hrs from current timestamp.                                                                                                              |
| DEBIT INITIATED | Debit is initiated.                                                                                                                                                                                         |
| DEBIT SUCCESS   | Debit is successful.                                                                                                                                                                                        |
| DEBIT FAILED    | Debit has failed. Post this it will follow the failed debit retries mechanism.                                                                                                                              |
| EXPIRED         | Presentation scheduled is expired. Can happen if debit scheduled is less that 48hrs of current timestamp, missed Debit/ Pre-Debit Notification because of subscription being in debit Failed/ Halted state. |
| CANCELLED       | Scheduled presentation is cancelled.                                                                                                                                                                        |

6. **Debit Failed Retries**  
   If a debit execution fails due to insufficient funds in the customer’s account or server issues, Plural will automatically attempt two internal retries at specified intervals. The first retry is triggered 10 minutes after the failure, followed by a second retry 1 hour later.  
   If the debit remains unsuccessful after the internal retries, merchants have the option to initiate external retries. A maximum of three external retry attempts are allowed.  
   If the mandate is in a "**Debit Failed**" state and no external retries are attempted, the debit will remain in the failed state and will not transition to a "**Halted**" state. Subsequent executions will not be impacted.
7. **Resume Halted Mandates**  
   If a mandate enters the **Halted** state, you can use the Resume API to reactivate it. Once the Resume API is triggered, a debit will be attempted on the mandate. If the debit is successful, the subscription status will change to **Active**.
8. **Third Party Verification**  
   You are provided with the ability to verify the customer's Virtual Payment Address (VPA). This feature allows for confirmation that the VPA provided during mandate creation is linked to the bank account information supplied by the end-user. To facilitate verification, both the VPA and the customer's account details must be submitted to Plural.
9. **Non-revocable Mandates**  
   You, as a merchant under the category code 7322, can create non-revocable UPI Autopay mandates through our Plural platform. When setting up a mandate for registration, you must specify whether you want to create non-revocable mandates by passing the appropriate value in the request field. If you belong to an MCC other than 7322, the mandate will not be registered.
