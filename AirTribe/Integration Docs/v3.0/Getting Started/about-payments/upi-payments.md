---
title: "UPI Payments"
slug: "upi-payments"
excerpt: "Learn how you can use Plural APIs to start accepting payments using UPI."
hidden: false
createdAt: "Wed Sep 11 2024 11:58:17 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Sep 12 2024 16:22:29 GMT+0000 (Coordinated Universal Time)"
---
Unified Payments Interface (UPI) are real-time digital transactions that allow users to transfer money instantly between bank accounts using a mobile device. Developed by the National Payments Corporation of India (NPCI), UPI eliminates the need for traditional banking details like account number and IFSC code. Instead, users can transfer funds using a Virtual Payment Address (VPA), mobile number, or QR code. With Plural, you can accept payments using the collect and intent flow.

1. **UPI Collect Flow**: The UPI Collect feature allows businesses to request payments from customers by generating dynamic payment requests. This feature streamlines payment collection, eliminating the need for traditional methods like cash or card transactions.
   1. Customers initiate the process by entering their UPI ID or Virtual Payment Address (VPA).
   2. The UPI ID is validated to ensure accuracy.
   3. A collect notification is sent to the customer’s UPI app.
   4. The customer approves the payment request by entering their 4-digit UPI PIN.  
      This flow enables secure, real-time payments that benefit both merchants and customers by offering a simple and efficient payment experience.
2. **UPI Intent Flow**: The Intent Flow offers customers a frictionless checkout experience by allowing them to select their preferred UPI app for completing payments.
   1. Customers choose their preferred UPI app from a list.
   2. They are redirected to the selected app.
   3. Customers finalize the transaction by entering their 4-digit UPI PIN in the UPI app.  
      This flow provides users with control over their payment experience, offering a fast and intuitive process.
