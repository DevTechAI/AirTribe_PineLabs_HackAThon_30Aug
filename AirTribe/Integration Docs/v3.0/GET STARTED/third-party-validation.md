---
title: "Third Party Validation"
slug: "third-party-validation"
excerpt: ""
hidden: true
createdAt: "Fri Oct 28 2022 05:29:47 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 11:00:48 GMT+0000 (Coordinated Universal Time)"
---
## What is TPV?

TPV is the Third-Party Validation service to help Merchants validate user is performing payment transactions with their own authorized account (provided during registration/KYC at merchant end) 

![](https://files.readme.io/d06821e-TPV_User_guide.png "TPV User guide.png")

## Why is TPV needed at all?##

As per SEBI guidelines, merchants (which deals with investment from customers) need to perform TPV checks on the customer investments to ensure the investment is done only through the accounts for which Customer has registered or/and completed KYC.  

## Which Merchant categories need or are mandated by TPV? ##

All Investment (into securities/Mutual Funds etc) related merchants primarily following SEBI guidelines. Some examples as below 

- Broking business 
- Mutual Funds 

## Which payments modes are applicable for TPV? ##

Currently, TPV service is mostly applicable to only Net Banking and UPI pay modes primarily. Debit card can also be part of TPV service logically but the network or/and intermediate entities currently do not have proper mechanisms to enable this authentication comprehensively. Wallets technically can perform TPV checks but this will lead to bifurcation of balances basis bank accounts used to credit the wallet account and thus is more difficult. Other payment modes like Credit Card etc are not directly linked to customer bank account and thus are not relevant for account validations  

## Which payment mode Plural support for TPV currently? ##

Current Scope of TPV is only on Net banking. We have UPI based TPV support coming soon 

## Which banks are currently supported by Plural for TPV services? ##

Below banks are supported currently for TPV in Net banking mode 

| Bank Supported for TPV                     |
| :----------------------------------------- |
| Axis Bank                                  |
| Bank of Baroda Corporate & retail          |
| Bank of India- Retail & Corporate          |
| Bank of Maharashtra                        |
| Catholic Syrian Bank                       |
| City Union Bank- Retail & Corporate        |
| Deutsche Bank                              |
| Dhanlaxmi Bank                             |
| Federal Bank (Retail & Corporate)          |
| HDFC Bank                                  |
| ICICI Bank - Retail                        |
| IDBI Bank                                  |
| IDFC First                                 |
| Indian Bank                                |
| Indian Overseas Bank- (Retail & Corporate) |
| IndusInd Bank                              |
| Jammu and Kashmir Bank- Retail & Corporate |
| Karnataka Bank                             |
| Karur Vysya Bank- Retail & Corporate       |
| Kotak Mahindra Bank                        |
| Lakshmi Vilas Bank Net Banking             |
| PNB Corporate & Retail                     |
| Saraswat Bank                              |
| State Bank of India                        |
| Tamilnad Mercantile Bank                   |
| Yes Bank                                   |
| Union Bank of India - Retail               |

## How do I get started?

You can refer the following developer resource section for details on our standard integration documentations <https://developer.pluralonline.com/reference>  

## What are the additional changes needed by a merchant specifically for TPV?

Apart from the standard integration, the only change needed for TPV is passing account number in the ‘Create Order’ API. Sample details are as mentioned below 

## Request Parameters

|          |                |           |                            |                                                    |       |
| :------- | :------------- | :-------- | :------------------------- | :------------------------------------------------- | :---- |
| Data     | Sub Data       | Data Type | Length                     | Description                                        | M/O/C |
| tpv_data |                |           |                            |                                                    |       |
|          | account_number | string    | length varies from 9 to 18 | Mandatory field in case of TPV enabled on merchant | M     |

## Sample Additional request parameters

{  
  "tpv_data": {  
    "account_number": "1234567890123456"  
  }  
} 

## Request Payload Sample:

{  
  "merchant_data": {  
    "merchant_id": "73",  
    "merchant_access_code": "a439438c-b873-4217-adc6-da35a9f23hc0",  
    "merchant_return_url": "<http://10.200.146.039/chargingrespnew.aspx">,  
    "merchant_order_id": "Micro-334526677667712123"  
  },  
  "payment_info_data": {  
    "amount": 300,  
    "currency_code": "INR",  
    "order_desc": "Test Order"  
  },  
  "customer_data": {  
    "country_code": "91",  
    "mobile_number": "9055957978",  
    "email_id": "[john.doe@pinelabs.com](mailto:john.doe@pinelabs.com)"  
  },  
  "billing_address_data": {  
    "first_name": "John",  
    "last_name": "Doe",  
    "address1": "Hisar",  
    "address2": "Hisar",  
    "address3": "Hisar",  
    "pin_code": "125005",  
    "city": "Hisar",  
    "state": "Haryana",  
    "country": "India"  
  },  
  "shipping_address_data": {  
    "first_name": "John",  
    "last_name": "Doe",  
    "address1": "Hisar",  
    "address2": "Hisar",  
    "address3": "Hisar",  
    "pin_code": "125005",  
    "city": "Hisar",  
    "state": "Haryana",  
    "country": "India"  
  },  
  "product_info_data": {  
    "product_details": [  
      {  
        "product_code": "200",  
        "product_amount": 300  
      }  
    ]  
  },  
  "additional_info_data": {  
    "rfu1": "123"  
  }, 

"tpv_data":{  
    "account_number":"50100044483350"  
  }  
} 

## Successful Response:

{  
    "token": "z689WeKBsLx71hEV1mdlFuPh0hsTOkrYtzDNTqcMnOQ%3D",  
    "plural_order_id": "30908"  
} 

## Additional Response codes (specific for TPV use cases)

Use case: Failure reason in case of no tpv_data request parameter in Order Creation API. 

{  
    "error_code": "1320",  
    "error_message": "Customer account number not found"  
} 

Use case: Failure reason in case of invalid customer's account number is passed in Order Creation API. 

{  
    "error_code": "1330",  
    "error_message": "Invalid customer account number"  
} 

## How do we get to know the final status of the Transaction outcome

As part of our standard integration (refer link provided above), Plural has multiple mechanisms to relay the final state to merchants. The same are as below and also applicable for Transactions with Third Party Validations  

Return URL: 

Merchants provide us with return URL. Plural posts the appropriate response on the same when user/payee completes the transaction resulting in either success/failure 

Webhooks/Push Notifications 

Merchants also have an option to register for webhook events (Transaction & Refund Success/failures events). There is a need to provide a URL where Plural would push the event details when triggered and where merchant is expected to handle the same. This option is available to merchants on the Plural dashboard.  

Transaction Status Inquiry 

Plural additionally also provide Inquiry APIs to ensure latest status at our merchant’s end is always in sync with our system 
