---
title: "Error codes"
slug: "error-codes-1"
excerpt: "Learn about the HTTP error responses returned from Plural APIs."
hidden: false
createdAt: "Thu Oct 03 2024 04:56:51 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Nov 15 2024 05:30:18 GMT+0000 (Coordinated Universal Time)"
---
Pine Labs provides key parameters in both Inquiry and Webhook/Redirect responses to enable detailed error tracking and consistent transaction management. These parameters probide insights into transaction statuses and error details, helping streamline error-handling.

**Inquiry Response Parameters**

The following parameters will be sent in **Inquiry responses**:

1. **ppc_ParentTxnResponseCode**: Indicates the status code of the purchase transaction.
2. **ppc_ParentTxnResponseMessage**: Provides additional details about the status and corresponding response code.

**Webhook and Redirect Response Parameters**

The following parameters will be sent in **Webhook and Redirect responses**:

1. **txn_response_code**: Indicates the status code of the purchase transaction.
2. **txn_response_msg**: Provides additional details about the status and corresponding response code.

**Implementation Guidance**

When integrating Pine Labs APIs, capture these parameters in your error-handling logic. They enable you to manage transaction failures and display relevant information to the user.

> 📘 Note:
> 
> Avoid hard-coding error messages, as they may change over time. Instead, handle error messages dynamically by using ppc_ParentTxnResponseMessage or txn_response_msg to maintain adaptability and consistent error handling.
