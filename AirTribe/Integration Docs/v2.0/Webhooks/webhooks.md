---
title: "Webhooks"
slug: "webhooks"
excerpt: "Listen to the callback events triggered by Plural, allowing your integration to respond automatically."
hidden: true
createdAt: "Thu Sep 19 2024 09:14:40 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Sep 19 2024 09:16:57 GMT+0000 (Coordinated Universal Time)"
---
Webhooks are a method of communication between two applications in real time. They enable merchants to receive notifications or trigger actions automatically when certain events occur in the payment system.

We use webhooks to notify you about the important events on your account. These webhooks contain details of the event such as changes in the transaction status and the resource impacted by the change.

We send webhooks as an HTTP POST call to a URL configured while Onboarding. The webhook payload uses the JSON format.

> 📘 Note:
> 
> - Contact Plural to set up a URL to receive webhook events from Plural.

By integrating with webhooks, merchants can automate various tasks, such as updating order statuses, sending confirmation emails, or updating inventory levels, without manual intervention.

> 👍 Good to Know
> 
> - Webhooks are asynchronous, so for time-sensitive actions, we recommend polling our API.
