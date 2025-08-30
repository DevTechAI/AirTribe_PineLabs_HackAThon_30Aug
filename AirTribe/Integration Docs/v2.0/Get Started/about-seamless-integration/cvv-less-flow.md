---
title: "CVV-Less Flow"
slug: "cvv-less-flow"
excerpt: "Learn how you can save card details as tokens and enable CVV-less payment flow for customers via Plural."
hidden: false
createdAt: "Fri Oct 18 2024 06:57:07 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Nov 27 2024 05:10:45 GMT+0000 (Coordinated Universal Time)"
---
A CVV-less transaction allows your customers to process a payment without requiring their card's CVV [Card Verification Value]. This can be used for saved cards as tokens, where CVV is not necessary for repeated transactions, such as tokenized payments or card-on-file services. 

CVV-less transactions enhance customer convenience by simplifying the payment process for recurring or saved card transactions. This improves the customer experience by reducing friction during checkout. While still maintaining security through tokenization and other robust verification methods. This balance enhances convenience without compromising safety.

## Supported Networks:

- Visa 
- Mastercard 

> 📘 NOTE:
> 
> - This feature is only supported for seamless card transactions.
> - You can implement a CVV-less flow for processing payments on your systems, provided that the token type used is `NETWORK_TOKEN_TXN`.
> - For Visa and Mastercard tokenized transactions, the cvv parameter can be omitted.

## Tokenized Card Payment without CVV

Use our Process Payment via Card Token API to process a tokenized card payment without CVV[Card Verification Value].

Use the below endpoint to process a payment via card token.

```text UAT Endpoint
POST: https://pinepg.in/api/v2/process/payment/card/tokenize?token=S01Hl%2b7P02sv6hpCa6kaY4Uf3%2fcFl3vC5aauslCa%2b7EX9U%3
```
```text PROD Endpoint
POST: https://pinepg.in/api/v2/process/payment/card/tokenize
```

Shown below is a sample request and sample response for a Tokenized Card Payment.

```json Sample Request
{
  "tokenize_card_data": {
    "token": "4895379990484220",
    "expiration_month": "11",
    "expiration_year": "2023",
    "cryptogram": "qE5juRwDzAUFBAkEHuWW9PiBkWv=",
    "token_transaction_type": "NETWORK_TOKEN_TXN",
    "par": "22sfsdfsd33ewr332",
    "cvv" : "123" // cvv parameter can be omitted for Visa and Mastercard tokenized payments
  },
  "card_meta_data": {
    "issuer_name": "HDFC",
    "scheme_name": "VISA",
    "card_type": "CREDIT"
  }
}
```
```json Sample Response
{
  "response_code": 1,
  "response_message": "SUCCESS",
  "redirect_url": "http://hostname:port/pinepg/v2/process/payment?token=848RFsu%2bRnNcSsaZdzEgkeosvCc2o5lKTV4uKJF%2fcjE%3d"
}
```

Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/v2.0/reference/process-payment-via-card-token" target="_blank">Process Payment via Card Token API</a> to learn more.

> 📘 NOTE:
> 
> CVV-less can only be tested on Production environment.
