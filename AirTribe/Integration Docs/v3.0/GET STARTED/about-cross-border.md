---
title: "International Payments"
slug: "about-cross-border"
excerpt: "Plural's International payments allow merchants to accept secure international transactions"
hidden: false
createdAt: "Fri Sep 13 2024 08:48:28 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Oct 30 2024 10:45:56 GMT+0000 (Coordinated Universal Time)"
---
## Overview

Plural has integrated with PayGlocal to enable international payments for our merchants. With a DCC enabled TID now merchants can allow payments from foreign issued cards on our platform. With over **40+ currencies supported **and a **robust FRM engine**, we help the merchant in expanding their user base and run their business globally.

## Product Features

1. **DCC checkout flow**

- Plural checkout, which is on both **seamless** and **redirect** flow, will ask for the card details from the end-users.
- Once the end-user proceeds to pay, they will be routed to our **DCC checkout**, where they will be given the option to pay in the currency their card was issued in.
- In DCC Checkout page, pincode is requested to enter only for USA, UK and Canada cards
- This flow however will charge a currency change mark-up from the end-user which is agreed upon at the time of onboarding.
- Once the customer selects their preferred currency, they will proceed to their authentication page. After the completion of payment journey, they will be redirected to the merchant’s redirect URL, which will be collected in the API request parameter.
- International payments is **supported for both Debit and Credit card issued by Mastercard and Visa.**

<br />

2. **FRM (Fraud & Risk Management)**

- We collect end-user’s details from the merchants. Details like address, pin code, card details, which are sent to PayGlocal’s risk engine.
- If the risk engine detects a high threat on the transaction initiated, they stop the payment from going through, with an appropriate error code in response. The benefit of this FRM system is enhanced security by preventing fraudulent transactions. By analyzing end-user details, the system detects potential threats in real time and blocks risky payments, reducing fraud and protecting both merchants and customers.

***

## Supported Currencies

| Currency Code | Currency                    |
| :------------ | :-------------------------- |
| INR           | Indian Rupee                |
| USD           | United States Dollar        |
| EUR           | Euro                        |
| ZAR           | South African Rand          |
| TWD           | New Taiwan Dollar           |
| MYR           | Malaysian Ringgit           |
| AZN           | Azerbaijani Manat           |
| OMR           | Omani Rial                  |
| KES           | Kenyan Shilling             |
| SEK           | Swedish Krona               |
| QAR           | Qatari Riyal                |
| CNY           | Chinese Yuan Renminbi       |
| THB           | Thai Baht                   |
| BDT           | Bangladeshi Taka            |
| KWD           | Kuwaiti Dinar               |
| MXN           | Mexican Peso                |
| PHP           | Philippine Peso             |
| SGD           | Singapore Dollar            |
| CHF           | Swiss Franc                 |
| AUD           | Australian Dollar           |
| ILS           | Israeli New Shekel          |
| TRY           | Turkish Lira                |
| TJS           | Tajikistani Somoni          |
| JOD           | Jordanian Dinar             |
| HKD           | Hong Kong Dollar            |
| AED           | United Arab Emirates Dirham |
| SCR           | Seychelles Rupee            |
| DKK           | Danish Krone                |
| CAD           | Canadian Dollar             |
| NOK           | Norwegian Krone             |
| MUR           | Mauritian Rupee             |
| LKR           | Sri Lankan Rupee            |
| CZK           | Czech Koruna                |
| BHD           | Bahraini Dinar              |
| KZT           | Kazakhstani Tenge           |
| SAR           | Saudi Riyal                 |
| MVR           | Maldivian Rufiyaa           |
| KRW           | South Korean Won            |
| JPY           | Japanese Yen                |
| PLN           | Polish Zloty                |
| GBP           | Pound Sterling              |
| NZD           | New Zealand Dollar          |
| BRL           | Brazilian Real              |

***

> 📘 Note:
> 
> - RRN and Auth code for the transaction initiated on merchant’s platform will be sent to the merchant with consolidated MPR in t+1 days.
> - You can use our Seamless or Plural Hosted Checkout to initiate a international transaction. Currently, we support international payments for card payment method.
