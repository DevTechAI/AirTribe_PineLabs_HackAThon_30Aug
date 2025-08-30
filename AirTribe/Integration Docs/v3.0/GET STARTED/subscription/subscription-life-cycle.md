---
title: "Life Cycle"
slug: "subscription-life-cycle"
excerpt: "Learn about the list of states of a Subscription and their significance."
hidden: false
createdAt: "Thu Feb 27 2025 11:04:38 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Apr 21 2025 04:25:55 GMT+0000 (Coordinated Universal Time)"
---
The figure below shows the life cycle of the Subscription.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/d7986240aeb2c3f8c54ec3a84977b3e33ba9ec5c45922cf96725566c06b33429-SUBSCRIPTION_FLOW_CHART_RELEASED_08-04-25_V03.png",
        null,
        "Figure: Subscription Status"
      ],
      "align": "center",
      "sizing": "700px",
      "border": true,
      "caption": "Figure: Subscription Life Cycle"
    }
  ]
}
[/block]


<br />

## Subscription States

The table below list the various statuses that our Subscription can have during its life cycle.

[block:parameters]
{
  "data": {
    "h-0": "Status",
    "h-1": "Description",
    "0-0": "MANDATE REGISTRATION",
    "0-1": "Authorizes automatic recurring payments for a subscription.",
    "1-0": "CREATED",
    "1-1": "Subscription is created after receiving approval from the end-user.",
    "2-0": "EXPIRED",
    "2-1": "The subscription moves to this state if no callback is received from the bank after mandate creation.",
    "3-0": "TRIAL",
    "3-1": "Subscription starts in a trial state; after mandate approval, it transitions to this state.",
    "4-0": "INACTIVE",
    "4-1": "The mandate creation fails due to a failure response from the bank.",
    "5-0": "ACTIVE",
    "5-1": "Subscription is in an active state and can be presented to the customer.",
    "6-0": "DEBIT SCHEDULED",
    "6-1": "Debit is scheduled. Only applicable when debit date is more than 48hrs from current timestamp.  \n  \n`Note`: If the initial debit attempt fails, Plural will automatically retry the transaction. If all retry attempts are exhausted without a successful debit, the status will change to 'Debit Failed.' The process will then resume.",
    "7-0": "DEBIT FAILED",
    "7-1": "Plural's retries for debit execution fail twice, moving the subscription to this state.",
    "8-0": "HALTED",
    "8-1": "After exhausting all retry attempts by both the merchant and Plural, the subscription enters the HALTED state. No further actions can be performed while in this state.",
    "9-0": "RESUMING",
    "9-1": "Intermediate stage where a subscription transitions from PAUSED or HALTED to RESUMED.",
    "10-0": "RESUMED",
    "10-1": "The subscription transitions to this state when either the merchant or the customer resumes it from a PAUSED or HALTED status.",
    "11-0": "REVOKE INTIATED",
    "11-1": "The merchant or customer initiates the cancellation of the mandate.",
    "12-0": "CANCELLED",
    "12-1": "The subscription is successfully cancelled after receiving a callback confirmation from the bank.",
    "13-0": "COMPLETED",
    "13-1": "Upon reaching the subscription's end period, the mandate transitions to this final state."
  },
  "cols": 2,
  "rows": 14,
  "align": [
    "left",
    "left"
  ]
}
[/block]
