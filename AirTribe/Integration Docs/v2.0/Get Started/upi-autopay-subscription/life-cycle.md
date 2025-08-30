---
title: "Life Cycle"
slug: "life-cycle"
excerpt: "Learn about the different states a Plural UPI Autopay Subscription can have during its life cycle."
hidden: true
createdAt: "Tue Dec 10 2024 09:56:40 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Feb 27 2025 11:23:19 GMT+0000 (Coordinated Universal Time)"
---
The figure below shows the States of the Subscription.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/5bf80388335d05251de508b79e06ad0e15cf2ea7143d46ca5915e756f5362821-SUBSCRIPTION_FLOW_CHART_RELEASED_11-12.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "700px"
    }
  ]
}
[/block]


## Subscription States

The table below list the various states of a Subscription.

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
