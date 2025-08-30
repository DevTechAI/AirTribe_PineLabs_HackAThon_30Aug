---
title: "Life Cycle"
slug: "workflow"
excerpt: "Learn about the different status a Plural Subscription can have during its life cycle."
hidden: true
createdAt: "Mon Nov 25 2024 09:43:47 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Dec 10 2024 06:23:39 GMT+0000 (Coordinated Universal Time)"
---
The figure below shows the Status of the Subscription.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/8b65e0befd76a8e6c5dd607ae1720e726e7185c4a15d4caeb8561b30a8455087-Subscription_Lifecycle.png",
        "",
        ""
      ],
      "align": "left",
      "sizing": "700px",
      "border": true
    }
  ]
}
[/block]


<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

<br />

## Subscription Status

The table below list the various statuses of a Subscription.

| Status          | Description                                                                                                                 |
| :-------------- | :-------------------------------------------------------------------------------------------------------------------------- |
| CREATED         | Subscription is created after receiving approval from the end-user.                                                         |
| TRIAL           | Subscription starts in a trial state; after mandate approval, it transitions to this state.                                 |
| ACTIVE          | Subscription is in an active state and can be presented to the customer.                                                    |
| INACTIVE        | The mandate creation fails due to a failure response from the bank.                                                         |
| DEBIT_FAILED    | Plural's retries for debit execution fail twice, moving the subscription to this state.                                     |
| HALTED          | After exhausting all retry attempts, the subscription is moved to this state; no further actions can occur while in HALTED. |
| RESUMED         | The subscription transitions to this state when resumed by the merchant or customer from PAUSED or HALTED.                  |
| REVOKE INTIATED | The merchant or customer initiates the cancellation of the mandate.                                                         |
| CANCELLED       | The subscription is successfully cancelled after receiving a callback confirmation from the bank.                           |
| EXPIRED         | The subscription moves to this state if no callback is received from the bank after mandate creation.                       |
| COMPLETED       | Upon reaching the subscription's end period, the mandate transitions to this final state.                                   |
