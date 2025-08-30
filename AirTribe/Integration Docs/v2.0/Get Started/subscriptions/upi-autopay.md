---
title: "UPI AutoPay"
slug: "upi-autopay"
excerpt: "Learn how to use Plural Subscriptions to accept recurring payments from your customers via the UPI Autopay payment method."
hidden: true
createdAt: "Tue Nov 26 2024 04:56:03 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Dec 10 2024 06:32:23 GMT+0000 (Coordinated Universal Time)"
---
UPI Autopay is a recurring payment by enabling seamless subscription management through the Unified Payments Interface (UPI). With this feature, you can offer customers a convenient and secure way to automate recurring payments for products or services. Once authorized, payments are automatically deducted on the due date without requiring manual intervention, ensuring uninterrupted access to subscriptions. UPI Autopay supports flexible billing cycles and simplifies the payment experience, fostering customer retention and trust while reducing operational overhead for businesses.

## Key Features

1. **Create Plan**
   - Create Plan API enables you to design flexible subscription plans. Just provide details such as the plan name, duration (start and end date), frequency, amount, maximum amount, and the number of users allowed per plan.
   - **View All Your Plans at a Glance**: The Get Plans API easily displays all the plans you’ve created within the system.
2. **Trial Period**
   - You can offer a trial period for their subscriptions. During this trial, no charges will be deducted from the end-user's account.
   - Simply define the desired trial period duration (in days).
   - Debits will be triggered automatically at the end of the trial period.
   - While in the trial state, the customer's approved mandate will remain in the TRIAL state.
   - Upon a successful debit, the mandate's status will automatically change from CREATED to ACTIVE.
   - Trial Period is not applicable for OT frequency
3. **Billing Frequency**  
   Our system allows you to easily define the debit frequency for your subscriptions. Select from the following options to determine how often the customer needs to be charged:

   [block:parameters]{"data":{"h-0":"Frequency","h-1":"Parameters and Definition","0-0":"Daily","0-1":"1 (Every day)","1-0":"Weekly","1-1":"1 (Every Week)","2-0":"Monthly","2-1":"1 (Once every month)","3-0":"Yearly","3-1":"4 (Once every quarter)  \n2 (Once every half year)  \n1 (Once every year)","4-0":"AS","4-1":"As-Presented (anytime during the subscription period)","5-0":"OT","5-1":"One-Time (Anytime but once during the subscription period)"},"cols":2,"rows":6,"align":["left","left"]}[/block]
4. **Pre-Debit Notification**  
   You will receive a notification 24 hours before any debit is made from your customer's account. This notification is mandatory as per RBI regulations and informs the customer about the scheduled debit for the following day.  
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
        "https://files.readme.io/9d475e84bd464cbed7b4b3bb18bf2cfa10303a72ddf2936b61e36dc6f77ab7f9-PRESENTATION_FLOW_CHART_09-12.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


The table below list the various statuses of a Presentation.

| Status          | Description                                                                                                                                                                                                 |
| :-------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PDN SCHEDULED   | Pre-Debit Notification is scheduled. Only applicable if debit date is more than 48hrs from current timestamp.                                                                                               |
| PDN INITIATED   | Pre-Debit Notification is initiated.                                                                                                                                                                        |
| PDN SUCCESS     | Pre-Debit Notification is successful                                                                                                                                                                        |
| PDN FAILED      | Pre-Debit Notification has failed. Our system will trigger internal retries.                                                                                                                                |
| DEBIT SCHEDULED | Debit is scheduled. Only applicable when debit date is less than 48hrs from current timestamp.                                                                                                              |
| DEBIT INITIATED | Debit is initiated.                                                                                                                                                                                         |
| DEBIT SUCCESS   | Debit is successful.                                                                                                                                                                                        |
| DEBIT FAILED    | Debit has failed. Post this it will follow the failed debit retries mechanism.                                                                                                                              |
| EXPIRED         | Presentation scheduled is expired. Can happen if debit scheduled is less that 48hrs of current timestamp, missed Debit/ Pre-Debit Notification because of subscription being in debit Failed/ Halted state. |

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
