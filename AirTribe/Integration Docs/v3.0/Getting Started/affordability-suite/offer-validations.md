---
title: "Offer Validation"
slug: "offer-validations"
excerpt: "Learn how to integrate with Plural offer validation API."
hidden: false
createdAt: "Wed Jan 22 2025 15:34:29 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jan 28 2025 13:31:57 GMT+0000 (Coordinated Universal Time)"
---
This API validates whether a specific offer is applicable for the customer’s selected payment method. It verifies conditions like order amount, offer eligibility, and payment method type (credit card EMI, debit card EMI, or cardless EMI).

This API is typically invoked at the payment stage to confirm that the selected offer can be applied with the chosen payment method, avoiding invalid transactions or user confusion.

**Key Features**

- Cross-checks the order details with the configured offer rules for eligibility.
- Validates the customer’s payment method against offer-specific restrictions.
