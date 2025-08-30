---
title: "Late Authorization"
slug: "late-authorization"
excerpt: "Learn how you can handle late authorised payments with Plural."
hidden: false
createdAt: "Fri Sep 27 2024 16:18:31 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Oct 18 2024 09:25:48 GMT+0000 (Coordinated Universal Time)"
---
To maintain customer satisfaction and operational efficiency, timely and accurate payment processing is crucial in this fast-paced world of online transactions. The delays in receiving transaction statuses from the Acquirer Banks affect the ability to confirm the final payment status. These delays can negatively impact both your customer experience and your business operations.

For example consider a merchant who has set the late authorization time to 10 seconds. Here's how the payment status typically unfolds:

- **Payment Initiation**: The customer completes the payment and the payment status is in a `pending` state. If the bank's gateway doesn't return a response to Plural within the configured time, the payment status is marked as "failed."
- **Plural Validation**: If no response is received from the bank within the 10-second window, Plural automatically updates the payment status to "Failed" due to timeout.
- **Refund**: We initiate refunds for late authorised payments.

> 📘 Note:
> 
> Customers can retry to make a new payment against the order.

### Challenges on Payment Delays

1. **Customer Experience Degradation**: Delayed transaction status updates might cause customers to be stuck on the payment page, leaving them unsure about the status of their payment.  
   For example:
   - At airport duty-free shops, customers are often in a hurry and transact for a time.
   - When booking movie tickets online, where seat availability can change quickly.
2. **Double Charging Risk**: If a transaction is re-initiated due to a delayed response and the original transaction is eventually completed successfully, customers may be charged twice. This situation can result in:
   - Additional administrative work to process refunds.
   - Customers waiting for their refunds, potentially decreasing their satisfaction and trust in your services.
3. **Inventory and Resource Allocation**: When transaction confirmations are delayed:
   - Valuable inventory may be unnecessarily reserved, preventing sales to other interested customers.
   - Managing stock levels, particularly for limited or high-demand items, becomes challenging and uncertain.

### Handle Late Auth Transactions

When a customer's payment does not receive an immediate response from the bank, the transaction status is initially set to "Initiated." If there is no response within the designated timeout period, the status changes to "Failed" due to delayed authorization. Plural continues to poll the bank at regular intervals starting from the day the payment is created.

- If the bank eventually confirms a failure, we update the internal status to "Failed" and stop polling.
- If the bank eventually confirms success, we refund the customer to ensure transparency, even though the transaction remains in a "Failed" state.
- If there is no response or the response remains as "Initiated" or "Pending," we will continue polling until a terminal status is received.

By integrating with Plural, you can significantly reduce the risks associated with delayed transaction authorizations, ensuring high operational efficiency and customer satisfaction, even when external payment processing delays occur.

### Configure Late Authorization

Plural permits you to configure a Late Authorization timer based on your business needs. Please reach out to our <a href="mailto:pgsupport@pinelabs.com" target="_blank">support team</a> to set up late authorization for your business.
