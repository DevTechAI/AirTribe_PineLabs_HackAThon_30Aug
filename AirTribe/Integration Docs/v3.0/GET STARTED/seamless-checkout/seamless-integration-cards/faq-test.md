---
title: "FAQ Test"
slug: "faq-test"
excerpt: ""
hidden: true
createdAt: "Tue Jan 14 2025 05:38:03 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Mar 28 2025 10:31:12 GMT+0000 (Coordinated Universal Time)"
---
<details><summary><b>1. What is CVV?</b></summary><br>CVV is a 3 or 4-digit code, typically located on the back of a card, used to verify the cardholder's identity during card-based transactions.</details>

***

2. **What is the SwiftPay - NoCVV feature**?  
   SwiftPay - NoCVV eliminates the need for the CVV during tokenized transactions. This feature enhances the payment experience by allowing users to complete payments with saved cards without entering the CVV. The overall payment flow remains the same, aside from not needing to input the CVV.
3. **What is Tokenization**?  
   Tokenization is the process of replacing a card number with a unique identifier called a token. This token is specific to the merchant, customer, and token requestor, providing a secure payment method.
4. **Does using this feature compromise security**?  
   No, this feature doesn’t compromise security. OTP is still required to authenticate the CVV-less transaction. The card token is created using user consent, CVV, and OTP, ensuring secure transactions without the need for CVV entry in future payments. The feature is fully secure and compliant with RBI guidelines.
5. **Is there a transaction limit with this feature**?  
   There is no specific transaction limit imposed by this feature. Payments can be made up to the limit set by existing constraints such as card limits and account types.
6. **Does this feature support guest checkout journeys**?  
   No, the CVV-less feature applies only to tokenized transactions. For new or guest checkout users or repeat transactions using the card number (PAN), entering the CVV is still mandatory. If the CVV field is omitted, the transaction will fail.
7. **Do all cards support this feature**?  
   The CVV-less flow is gaining traction and depends on support from Card Networks and Payment Gateways. Currently, the feature is available for seamless merchant integration (redirect coming soon) with credit and debit cards: full swipe, EMI, full swipe with offers, and EMI with offers on VISA and MasterCard, with Rupay support coming soon.
8. **Will this feature impact other products**?  
   No, the SwiftPay - NoCVV feature will not affect existing products like Payouts, Subscriptions, Offers, EMIs, etc.

<br />

### 4.4. Process Payment on another PA/PG with token created on Plural

To process a payment on another PA/PG with the token created on Plural you have to generate the cryptogram.

Below are the sample requests and sample response for a Generate Cryptogram API.

```curl cURL - UAT
curl --request POST \
--url https://pluraluat.v2.pinepg.in/api/v1/tokens/token_id/token-transactional-data \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
--header 'Content-Type: application/json' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'accept: application/json' \
     --data '
{
  "merchant_unique_reference": "dx98b63e-c74g-5ac4-632e-346d6c7bdwka",
  "service_provider_token_id": "tp-v1-0811030624-aa-RBDgpR"
}
'
```
```curl cURL - PROD
curl --request POST \
--url https://api.pluralpay.in/api/v1/tokens/token_id/token-transactional-data \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
--header 'Content-Type: application/json' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'accept: application/json' \
     --data '
{
  "merchant_unique_reference": "dx98b63e-c74g-5ac4-632e-346d6c7bdwka",
  "service_provider_token_id": "tp-v1-0811030624-aa-RBDgpR"
}
'
```
```json Sample Response
{
  "token_id": "token-v1-0811030624-aa-RBDgpR",
  "merchant_token_reference": "ec71b52e-c21f-4ac5-8624-385d6b6bdccc",
  "service_provider_token_id": "tp-v1-0811030624-aa-RBDgpR",
  "token_data": {
    "cryptogram": "/wAAAAAAl9SX1HsAmWKSgqwAAAA=",
    "token_reference": "sas7wqaoidasdfssdjjk",
    "payment_account_reference": "8324ssdas7wqaoidassdjjk",
    "token_expiry_month": 5,
    "token_expiry_year": 2030
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/reference/generate-cryptogram" target="_blank">Generate Cryptogram API</a> documentation to learn more.

[block:html]
{
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>Dynamic Tabs</title>\n    <style>\n        body {\n            font-family: Arial, sans-serif;\n            margin: 20px;\n        }\n        .tab {\n            display: inline-block;\n            padding: 10px 20px;\n            cursor: pointer;\n            border-bottom: 2px solid transparent;\n        }\n        .tab.active {\n            font-weight: bold;\n            border-bottom: 2px solid #5A0083;\n        }\n        .tab-content {\n            display: none;\n            padding: 20px;\n            border: 1px solid #ddd;\n            margin-top: 10px;\n        }\n        .tab-content.active {\n            display: block;\n        }\n    </style>\n</head>\n<body>\n    <div>\n        <div class=\"tab active\" onclick=\"\n            document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));\n            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));\n            this.classList.add('active');\n            document.getElementById('tab1').classList.add('active');\n        \">Request Parameters</div>\n        <div class=\"tab\" onclick=\"\n            document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));\n            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));\n            this.classList.add('active');\n            document.getElementById('tab2').classList.add('active');\n        \">Response Parameters</div>\n    </div>\n\n    <div id=\"tab1\" class=\"tab-content active\">\n      <h2>Request Parameters</h2>\n        <p>Content for Request Parameters.</p>\n    </div>\n    <div id=\"tab2\" class=\" tab-content\">\n        <h2>Response Parameters</h2>\n        <p>Content for Response Parameters.</p>\n    </div>\n</body>\n</html>\n"
}
[/block]


[block:html]
{
  "html": "<!DOCTYPE html>\n<html>\n<head>\n    <title>Card Issuer Table</title>\n    <style>\n        table {\n            width: 100%;\n            border-collapse: collapse;\n        }\n        th, td {\n            border: 1px solid black;\n            padding: 10px;\n            text-align: center;\n        }\n        th {\n            background-color: #f2f2f2;\n        }\n    </style>\n</head>\n<body>\n    <table>\n        <tr>\n            <th rowspan=\"2\">Card Issuer</th>\n            <th colspan=\"3\">NETWORK</th>\n        </tr>\n        <tr>\n            <th>VISA</th>\n            <th>MASTERCARD</th>\n            <th>RUPAY</th>\n        </tr>\n        <tr>\n            <td>ICICI Credit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td></td>\n        </tr>\n        <tr>\n            <td>ICICI Debit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td></td>\n        </tr>\n        <tr>\n            <td>HDFC Credit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n        </tr>\n        <tr>\n            <td>HDFC Debit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td></td>\n        </tr>\n        <tr>\n            <td>AXIS Credit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td></td>\n        </tr>\n        <tr>\n            <td>AXIS Debit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td></td>\n        </tr>\n        <tr>\n            <td>SBI Credit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n        </tr>\n        <tr>\n            <td>SBI Debit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td></td>\n        </tr>\n        <tr>\n            <td>KOTAK Credit Card</td>\n            <td>&#10004;</td>\n            <td></td>\n            <td></td>\n        </tr>\n        <tr>\n            <td>KOTAK Debit Card</td>\n            <td>&#10004;</td>\n            <td></td>\n            <td></td>\n        </tr>\n        <tr>\n            <td>YESBANK Credit Card</td>\n            <td>&#10004;</td>\n            <td>&#10004;</td>\n            <td></td>\n        </tr>\n    </table>\n</body>\n</html>\n"
}
[/block]
