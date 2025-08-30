---
title: "Integration Best Practices"
slug: "integration-best-practices-copy-2"
excerpt: "Learn the best practices to follow before beginning with the integration."
hidden: true
createdAt: "Wed Apr 30 2025 13:14:19 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon May 12 2025 05:46:07 GMT+0000 (Coordinated Universal Time)"
---
1. **Verify Signature to Avoid Data Tampering**: We recommend this as a Mandatory step to confirm the authenticity of the details returned to you on the return URL for successful payments. Refer to our <a href="https://developer.pluralonline.com/docs/webhook-signature-verification" target="_blank">signature verification</a> documentation to learn more. documentation to learn more.
2. **Check Order Status**: Use our <a href="https://developer.pluralonline.com/reference/orders-get-by-order-id" target="_blank" >Get Orders API</a> from the backend to check the order/payment status before providing service to the customers. Refer to our life cycle documentation to learn more about <a href="https://developer.pluralonline.com/docs/payment-life-cycle" target="_blank">Plural payment statuses</a>.
3. **Configure Webhooks**: Contact our <a href="mailto:pgsupport@pinelabs.com" target="_blank">support team</a> to configure webhook events to avoid callback failures. Refer to our <a href="https://developer.pluralonline.com/docs/developer-tools-webhooks" target="_blank" >webhook</a> documentation to learn more.
4. **Implement Flexible JSON Parsing**:  We recommend designing your systems to gracefully ignore any additional or unknown fields in the JSON payload during integration. 
   - This ensures **forward compatibility** as our platform evolves or introduces new optional fields.
   - Aligns with industry-standard **robust API design principles**, preventing integration issues from unexpected data.  
     **Example**: Flexible JSON Handling

```json Incoming Request Example
json  
{  
  "transactionId": "TXN123456",  
  "amount": 10000,  
  "currency": "INR",  
  "extraField": "IgnoreThisNode"  
}
```

**Expected Handling**: You should process the known fields (`transactionId`, `amount`, `currency`) and gracefully ignore the `extraField`.

5. **Avoid Hardcoding Parameters**: To ensure a scalable integration, do not hardcode values such as API keys, environment flags, or identifiers in your system while integrating.
   - Hardcoded values increase the risk of **failures** when changes occur on the platform.
   - Using **configuration files or environment variables** makes your integration easier to maintain and adapt across environments (e.g., sandbox vs production).
6. **TLS Version**: We recommend you to, use "TLS_v_1.2" or the higher TLS versions to avoid any transaction failures.
7. **Conduct Sanity Testing**: Before fully implementing TLS 1.2 and updating the cipher suites, perform application testing to confirm seamless communication across systems and applications within your environment.
8. **Implement Strong Cipher Suites**: Configure TLS-enabled services to use only strong cipher suites with robust encryption algorithms and key exchange mechanisms. A list of recommended cipher suites is provided below. All other ciphers should be disabled.

**List of accepted Ciphers**:

- `TLS_AES_128_CCM_8_SHA256`
- `TLS_AES_128_CCM_SHA256`
- `TLS_ECCPWD_WITH_AES_128_CCM_SHA256`
- `TLS_ECCPWD_WITH_AES_256_CCM_SHA384`
- `TLS_ECDHE_ECDSA_WITH_AES_128_CCM`
- `TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8`
- `TLS_ECDHE_ECDSA_WITH_AES_256_CCM`
- `TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8`
- `TLS_ECDHE_PSK_WITH_AES_128_CCM_8_SHA256`
- `TLS_ECDHE_PSK_WITH_AES_128_CCM_SHA256`
- `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`
- `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`
- `TLS_ECDHE_RSA_WITH_ARIA_128_GCM_SHA256`
- `TLS_ECDHE_RSA_WITH_ARIA_256_GCM_SHA384`
- `TLS_ECDHE_RSA_WITH_CAMELLIA_128_GCM_SHA256`
- `TLS_ECDHE_RSA_WITH_CAMELLIA_256_GCM_SHA384`
- `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`

> 📘 Note:
> 
> - You can only test Credit/Debit Cards, Net Banking (via SBI),Cross Border & Pay by Points on UAT/Staging Environment.
> - Production credentials will be shared with you after UAT sign-off, to test all flows in the soft production environment before going live.
> - Please share the Return and webhook URL for configuration and whitelisting before going Live.
> - For any incremental updates or support related to integration, please contact our <a href="[pgintegration@pinelabs.com](mailto:pgintegration@pinelabs.com)" target="_blank" >`Integration team`</a>.
