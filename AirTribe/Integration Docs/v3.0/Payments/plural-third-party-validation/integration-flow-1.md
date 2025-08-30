---
title: "Integration Flow"
slug: "integration-flow-1"
excerpt: "Learn how to integrate with Plural APIs to use Plural Third Party Validation."
hidden: true
createdAt: "Fri Jul 05 2024 07:07:40 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Jul 05 2024 08:08:09 GMT+0000 (Coordinated Universal Time)"
---
By Integrating with Plural's Third Party Validation (TPV), you can ensure transaction are made from the pre registered bank accounts through conditional validation checks. Seamlessly comply with SEBI guidelines for secure online payments. Provide seamless payment experience using UPI.

The figure below shows the step by step procedure for integrating with Plural Third Party Validation(TPV).

<br />

1. **Create Order**: Integrate our Create Order API in you Backend server and use this API to create an order.
2. **Generate TPV Link**: Integrate our Generate TPV Link API in your Backend and use this API to generate a TPV Link.
3. **Share Payment Details**: After generating the Link, share the link or QR code to receive payment using UPI.
4. **Handle Payments**:
