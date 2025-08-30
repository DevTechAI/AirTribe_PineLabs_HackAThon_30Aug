---
title: "Life Cycle"
slug: "third-party-validations-life-cycle"
excerpt: "Learn about the different statuses a third party validation can have during it's life cycle."
hidden: true
createdAt: "Fri Jul 05 2024 07:00:21 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 27 2024 16:31:06 GMT+0000 (Coordinated Universal Time)"
---
You can use the key values of `ppc_Parent_TxnStatus` and `ppc_ParentTxnResponseCode` to know the states of your payments.

The table below list the statuses of a third party validation flow.

| Transaction State            | ppc_Parent_TxnStatus | ppc_ParentTxnResponseCode | Description                                |
| :--------------------------- | :------------------- | :------------------------ | :----------------------------------------- |
| `SUCCESS`                    | `4`                  | `1`                       | When the payment is successful.            |
| `FAILED`                     | `1`                  | `-1`                      | When the payment gets failed.              |
| `INITIATED`                  | `1`                  | `1`                       | When the payment is initiated.             |
| `SUCCESS` [Refund Initiated] | `1`                  | `2`                       | When the refund is successfully Initiated. |
| `SUCCESS` [Full Refunds]     | `6`                  | `1`                       | When full refund is successful.            |
| `SUCCESS` [Partial Refunds]  | `9`                  | `1`                       | When partial refund is successful.         |
| `FAILED` [Refund]            | `-7`                 | Any code                  | When the refund is failed.                 |

> 📘 Note:
> 
> - We return the `ppc_Parent_TxnStatus` and `ppc_ParentTxnResponseCode` parameter values in our Inquiry API. Use them to map and determine the real-time status of the transaction.
