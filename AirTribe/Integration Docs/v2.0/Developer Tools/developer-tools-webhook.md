---
title: "Webhooks"
slug: "developer-tools-webhook"
excerpt: "Listen to the callback events triggered by Plural, allowing your integration to respond automatically."
hidden: false
createdAt: "Tue Sep 17 2024 09:41:20 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 27 2024 16:22:55 GMT+0000 (Coordinated Universal Time)"
---
Webhooks are a method of communication between two applications in real time. They enable merchants to receive notifications or trigger actions automatically when certain events occur in the payment system.

We use webhooks to notify you about the important events on your account. These webhooks contain details of the event such as changes in the transaction status and the resource impacted by the change.

We send webhooks as an HTTP POST call to a URL configured while Onboarding. The webhook payload uses the JSON format.

> 📘 Note:
> 
> - Contact our <a href="mailto:pgsupport@pinelabs.com" target="_blank">support team</a> to set up a URL to receive webhook events from Plural.

By integrating with webhooks, merchants can automate various tasks, such as updating order statuses, sending confirmation emails, or updating inventory levels, without manual intervention.

> 👍 Good to Know
> 
> - Webhooks are asynchronous, so for time-sensitive actions, we recommend polling our API.
