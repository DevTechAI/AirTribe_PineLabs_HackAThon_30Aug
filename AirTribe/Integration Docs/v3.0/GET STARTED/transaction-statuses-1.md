---
title: "Order & Transaction Statuses"
slug: "transaction-statuses-1"
excerpt: ""
hidden: true
createdAt: "Mon Sep 20 2021 04:45:53 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:59:14 GMT+0000 (Coordinated Universal Time)"
---
## Order & Transaction status at each step

Please find below the statuses for a given order and payment transaction for each step of the transaction flow. 

[block:parameters]
{
  "data": {
    "h-0": "Step",
    "h-1": "Order Status",
    "h-2": "Transaction Status",
    "0-0": "When Order is created",
    "0-1": "ORDER CREATED",
    "0-2": "NA",
    "1-0": "_ If Seamless flow - Consume Token From Order Creation and call Process Payment API  \n  _ If Redirect flow - Hitting redirect URL",
    "1-1": "ORDER ATTEMPTED",
    "1-2": "TXN ATTEMPTED (No response from acquirer)",
    "2-0": "After successful OTP Verification (3DS)",
    "2-1": "CHARGED",
    "2-2": "CAPTURED",
    "3-0": "If no response from Acquirer",
    "3-1": "ORDER ATTEMPTED",
    "3-2": "PENDING (Got response from Acquirer but no response after S2S Inquiry call for dual verification)",
    "4-0": "After successful Partial Refund",
    "4-1": "PARTIAL REFUNDED",
    "4-2": "PARTIALLY REFUNDED",
    "5-0": "",
    "5-1": "",
    "5-2": "",
    "6-0": "After successful full Refund",
    "6-1": "REFUNDED",
    "6-2": "REFUNDED",
    "7-0": "Transaction was declined or failed due to any reason after Token consumption",
    "7-1": "FAILED",
    "7-2": "FAILURE/REJECTED",
    "8-0": "Inquiry made on a given order. For that order, a new transaction is created for the inquiry. The status for the new inquiry transaction will be QUERY_COMPLETED",
    "8-1": "Order status can change basis the state received post inquiry",
    "8-2": "Transaction status can change basis the state received post inquiry",
    "9-0": "When merchant initiates refund. For that order a new transaction is created for the refund. The status for the new refund transaction will be REFUND INITIATED",
    "9-1": "No change in Order Status till successful refund.",
    "9-2": "No change in parent Transaction Status till successful refund",
    "10-0": "For transaction marked is_reversal",
    "10-1": "NA (doesn't impact order status)",
    "10-2": "MARKED_FOR_AUTO_REFUND"
  },
  "cols": 3,
  "rows": 11,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]
