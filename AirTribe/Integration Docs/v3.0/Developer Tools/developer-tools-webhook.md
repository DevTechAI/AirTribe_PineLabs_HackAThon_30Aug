---
title: "Webhooks"
slug: "developer-tools-webhook"
excerpt: "Listen for the callback events Plural triggers, so your integration can automatically trigger reactions."
hidden: false
createdAt: "Tue Aug 13 2024 07:14:53 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 27 2024 09:07:32 GMT+0000 (Coordinated Universal Time)"
---
Webhooks are a method of communication between two applications in real time. They enable merchants to receive notifications or trigger actions automatically when certain events occur in the payment system.

We use webhooks to notify you about the important events on your account. These webhooks contain details of the event such as changes in the transaction status and the resource impacted by the change.

We send webhooks as an HTTP POST call to a URL configured while Onboarding. The webhook payload uses the JSON format.

> 📘 Note:
> 
> - Contact our <a href="mailto:pgsupport@pinelabs.com" target="_blank">support team</a> to set up a URL to receive webhooks from Plural.

By integrating with webhooks, merchants can automate various tasks, such as updating order statuses, sending confirmation emails, or updating inventory levels, without manual intervention.

> 👍 Good to Know
> 
> - Webhooks are asynchronous, so for time-sensitive actions, we recommend polling our API.
> - We attempt to send webhook events up to three times if the initial delivery to the merchant fails. Please wait for 5 seconds while we complete these retries. If the webhook event is still not received within this period, it is recommended to use the Get Order API to obtain the updated order status.

## IP Address for Webhook

To ensure your integration is secure, configure your servers to accept webhooks only from the following IP range and address.

- **IP range**: `13.201.195.80/28`
- **IP adress**: `13.200.147.61`
