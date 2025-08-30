---
title: "Integration Best Practices (COPY)"
slug: "integration-best-practices-copy"
excerpt: "Learn the best practices to follow before beginning with the integration."
hidden: true
createdAt: "Thu Dec 12 2024 10:44:54 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Dec 12 2024 10:44:54 GMT+0000 (Coordinated Universal Time)"
---
1. **Verify Signature to Avoid Data Tampering**: We recommend this as a Mandatory step to confirm the authenticity of the details returned to you on the return URL for successful payments. Refer to our signature verification documentation to learn more.
2. **Check Payment Status**: Use our Inquiry API from the backend to check the payment status before providing service to the customers. Refer to our life cycle documentation to learn more about Plural payment statuses.
3. **Configure Webhooks**: Contact our integration teams to configure webhook events to avoid callback failures. Refer to our webhook documentation to learn more.
4. **TLS Version**: We recommend you to, use "TLS_v_1.2" or the higher TLS versions to avoid any transaction failures.
5. **Conduct Sanity Testing**: Before fully implementing TLS 1.2 and updating the cipher suites, perform application testing to confirm seamless communication across systems and applications within your environment.
6. **Implement Strong Cipher Suites**: Configure TLS-enabled services to use only strong cipher suites with robust encryption algorithms and key exchange mechanisms. A list of recommended cipher suites is provided below. All other ciphers should be disabled.

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
- `Late Auth`

> 📘 Note:
> 
> - You can only test Credit/Debit Cards, Net Banking (via IDBI), and EMI in the UAT environment.
> - Production credentials will be shared with you after UAT sign-off to test all flows in the soft production environment before going live.
> - Please share the Return and webhook URL for configuration and whitelisting before going Live.
