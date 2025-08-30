---
title: "FAQs and Troubleshooting"
slug: "faqs-and-troubleshooting"
excerpt: ""
hidden: true
createdAt: "Fri Sep 24 2021 09:27:43 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 11:00:22 GMT+0000 (Coordinated Universal Time)"
---
How do I configure Merchant Payment Return URL not configured in Dashboard?  
Ans: Configure from Setting->General->Payment Return URL

How do I configure Payment Gateway on Console?  
Ans: On Merchant Dashboard. Smart Routing --> Create Gateway

When is No Acquirer Found error thrown?  
Ans: When no Payment Gateway is configured. Please configure a payment gateway by going to Smart Routing --> Create Gateway

How to add multiple merchant url on merchant dashboard?  
Ans: Configure from Setting->General->Payment Return URL separated by comma(,)without any spaces.

How to add one or multiple Gateways in Dashboard?  
Ans: Create Gateways-> Select gateway from dropdown->Configure gateway credentials->create

How to set Routing Scores for bin, issuer, card brand?  
Ans: Create route->enter required details->create

How to set routing preference for gateways?  
Ans: Gateway->ROUTES SCORES->Please specify the routing preference of gateways in a comma-separated manner 

How to set custom priority logic?  
Ans: Gateway->PRIORITY LOGICS->enable tom priority logic option

How to create user and role?  
Ans: User->create user->fill required details->click create user button.

How to get plural credentials for transaction?  
Ans : Go to Settings --> Credentials. You will find your MID, Secret Key and Access code

How to set webhook url on dashboard?  
Ans: Go to Settings --> Webhooks --> Enter url --> Enable webhook events --> Update
