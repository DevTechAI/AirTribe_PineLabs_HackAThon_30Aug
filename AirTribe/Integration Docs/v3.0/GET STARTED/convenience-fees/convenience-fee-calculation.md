---
title: "Convenience Fee Calculation"
slug: "convenience-fee-calculation"
excerpt: "Learn about the convenience fee calculation login."
hidden: false
createdAt: "Thu Dec 12 2024 07:15:58 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Dec 16 2024 13:10:06 GMT+0000 (Coordinated Universal Time)"
---
The logic to calculate the convenience fee for a merchant is as follows, with all amounts represented in the smallest currency unit (e.g., paise):

### Merchant Backend Configuration

You can configure the Flat fee, Percentage fee, Additional fee, and Maximum fee you would like to charge to your customers for processing a payment. For example;

- Flat fee: 600 (equivalent to ₹6)
- Percentage fee: 1%
- Additional fee: 500 (equivalent to ₹5)
- Maximum fee: 15000 (equivalent to ₹150)

### Original Payment Amount

- The payment amount for this calculation is ₹10000.

### Step-by-Step Calculation

#### 1. Percentage Fee Component

Calculate 1% of the payment amount:

Percentage Fee = 1% × 10000 = 100 (₹1)

#### 2. Fee Amount

Add the flat fee and percentage fee:

Fee Amount = Flat Fee + Percentage Fee = 600 + 100 = 700 (₹7)

#### 3. Additional Fee

Use the configured additional fee directly:

Additional Fee = 500 (₹5)

#### 4. Tax Amount

Tax is 18% of the sum of the fee amount and additional fee:

Tax Amount = 18% × (Fee Amount + Additional Fee) = 18% × (700 + 500) = 216 (₹2.16)

#### 5. Maximum Fee Amount

Taken directly from the configuration:

Maximum Fee Amount = 15000 (₹150)

#### 6. Applicable Fee Amount

- The final fee applied is the sum of all components:

Applicable Fee Amount = Fee Amount + Additional Fee + Tax Amount = 700 + 500 + 216 = 1416 (₹14.16)

- Check if this value exceeds the maximum fee allowed:

Applicable Fee Amount = min (1416, Maximum Fee Amount)  
In this case, ₹14.16 is less than the maximum fee of ₹150, so ₹14.16 is the final fee applied.

This ensures the fee is calculated within predefined constraints, incorporating flexibility for percentage-based fees, additional charges, taxes, and upper limits.
