---
title: "Life Cycle"
slug: "plural-hosted-checkout-life-cycle"
excerpt: "Learn about the different status a Plural hosted checkout can have during its life cycle."
hidden: false
createdAt: "Thu Jun 27 2024 06:13:41 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Sep 20 2024 09:24:21 GMT+0000 (Coordinated Universal Time)"
---
You can use the key values of `ppc_Parent_TxnStatus` and `ppc_ParentTxnResponseCode` to know the states of your payments.

The table below list the statuses of a third party validation flow.

| Transaction State                             | ppc_Parent_TxnStatus | ppc_ParentTxnResponseCode | Description                                |
| :-------------------------------------------- | :------------------- | :------------------------ | :----------------------------------------- |
| `SUCCESS`                                     | `4`                  | `1`                       | When the payment is successful.            |
| `FAILED`                                      | `1`                  | `-1`                      | When the payment gets failed.              |
| `INITIATED`                                   | `1`                  | `1`                       | When the payment is initiated.             |
| `SUCCESS` [Refund Initiated]                  | `1`                  | `2`                       | When the refund is successfully Initiated. |
| `SUCCESS` [Full Refunds]                      | `6`                  | `1`                       | When full refund is successful.            |
| `SUCCESS` [Partial Refunds]                   | `9`                  | `1`                       | When partial refund is successful.         |
| `FAILED` [Payment/Full Refund/Partial Refund] | `-7`                 | Any code                  | When the transaction is failed.            |

> 📘 Note:
> 
> - We return the `ppc_Parent_TxnStatus` and `ppc_ParentTxnResponseCode` parameter values in our Inquiry API. Use them to map and determine the real-time status of the transaction.
