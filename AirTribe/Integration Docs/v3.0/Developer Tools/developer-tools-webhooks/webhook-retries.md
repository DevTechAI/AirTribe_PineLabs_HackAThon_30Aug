---
title: "Webhook Retries"
slug: "webhook-retries"
excerpt: "Learn how we handle different webhook scenarios."
hidden: false
createdAt: "Fri Dec 06 2024 06:14:59 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Dec 06 2024 06:53:36 GMT+0000 (Coordinated Universal Time)"
---
Learn how to handle different scenarios when working with webhooks and suggest ways to ensure your webhooks work seamlessly with your integrations.

## Built-in Retries

To mark a webhook as delivered, Plural by Pine Labs expects an HTTP 2XX response code from your endpoint within 5 seconds of the event delivery. We consider any other response code, or no response code, a failed delivery. When this happens, we retry the delivery.

- A webhook delivery attempt is retried at increasing intervals: immediately, after 5 seconds, 5 minutes, 30 minutes, 2 hours, 5 hours, and two additional retries after 10 hours each. This ensures multiple opportunities for successful delivery.

## Order of Events

While webhooks are triggered in a particular order, we recommend you not expect that the webhook will reach you in the same order. This could be due to webhook retries, network delays, or other technical reasons.

- For example, you might get the `ORDER_PROCESSED` event before the `ORDER_AUTHORIZED` event.
- Ensure you configure your webhook endpoint URL to handle these scenarios.
