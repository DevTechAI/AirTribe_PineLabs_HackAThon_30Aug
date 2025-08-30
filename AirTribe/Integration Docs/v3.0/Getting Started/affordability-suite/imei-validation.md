---
title: "IMEI Validation"
slug: "imei-validation"
excerpt: "Learn how you can validate the IMEI number using Plural API."
hidden: false
createdAt: "Tue Jan 21 2025 13:58:34 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Mar 20 2025 09:22:09 GMT+0000 (Coordinated Universal Time)"
---
Integrating with Plural, you can now include an IMEI verification flow, enabling merchants to verify product IMEI or serial numbers during the payment. This feature ensures compliance and enhances efficiency by integrating IMEI verification.

You can use this Plural IMEI Validation API to `Unblock` and `Block`.

Integrating with IMEI validations allows you to secure operations in EMI or loan-based purchases. IMEI validation ensures that the device associated with the payment is accurately identified and secured. Businesses use IMEI validation to manage processes like unblocking devices during returns or blocking them in cases of payment default.

> 📘 Note:
> 
> - Once the refund request is successfully processed, the product IMEI will also be blocked in the backend.
> - For a full refund, all IMEIs linked to the product are automatically blocked. For a partial refund, you must provide the `product_imei` that needs to be blocked.
