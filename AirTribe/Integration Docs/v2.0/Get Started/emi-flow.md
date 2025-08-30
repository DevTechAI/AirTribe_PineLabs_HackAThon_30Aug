---
title: "Steps for EMI Integration"
slug: "emi-flow"
excerpt: "Follow these steps to offer bank and brand EMI offers to your customers"
hidden: true
createdAt: "Mon Oct 04 2021 04:59:53 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:58:55 GMT+0000 (Coordinated Universal Time)"
---
Plural helps the merchant to offer no-cost, low-cost EMI on their products by bringing issuing bank and OEMs on the same platform.

We offer two types of EMI programs:

- Bank EMI
- Brand EMI

Following steps are involved in the seamless integration of the EMI transactions:

- Get EMI offers
- Validate Scheme
- Create Order
- Process Payment
- Check Status
- IMEI validation (Applicable only for Brand EMI and for brands which have this as a mandatory requirement)

## Get EMI Offers

Merchant can call EMI calculator API to show all EMI offers applicable on a given product. This is generally shown on the product listing page of the merchant's website. EMI Calculator as the name suggests provides a platform /API information exchange to display various EMI offers details on the product display page of the merchant website.

#### Curl for EMI Calculator API

```curl
curl --request POST \
     --url https://api-staging.pluralonline.com/api/v1/emi/calculator \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/json' \
     --data '
{
     "merchant_data": {
          "merchant_id": 11607
     },
     "payment_data": {
          "amount_in_paisa": 2000000
     },
     "product_details": [
          {
               "product_code": "2000",
               "product_amount": 2000000
          }
     ]
}
'
```

## Scheme Validation API

Merchant is required to integrate this API to check the applicability of EMI plans on a customer card. This API should be called once the customer enters the credit card number to validate if the selected EMI offer is applicable on the given card or not. Merchant needs to integrate with this API only in the Seamless mode. 

> 📘 Scheme Parameters
> 
> In this API call merchant also passes scheme parameters to be applied for the given transaction

#### Curl for Scheme Validation API

```curl
curl --request POST \
     --url https://api-staging.pluralonline.com/api/v1/emi/scheme/validation \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/json' \
     --data '
{
     "merchant_data": {
          "merchant_id": 11607
     },
     "payment_data": {
          "amount_in_paisa": 2000000
     },
     "card_data": {
          "card_number": "4012001037141112"
     },
     "emi_data": {
          "offer_scheme": {
               "product_details": [
                    {
                         "schemes": [
                              {
                                   "scheme_id": "46921",
                                   "program_type": 106,
                                   "is_scheme_valid": true
                              }
                         ],
                         "product_code": "2000",
                         "product_name": "2000",
                         "product_amount": 2000000,
                         "subvention_cashback_discount": 40000,
                         "product_discount": 0,
                         "subvention_cashback_discount_percentage": 20000,
                         "product_discount_percentage": 0,
                         "subvention_type": 2,
                         "bank_interest_rate_percentage": 50000,
                         "bank_interest_rate": 53468
                    }
               ],
               "emi_scheme": null
          },
          "tenure_id": "12",
          "tenure_in_month": "12",
          "monthly_installment": 167789,
          "bank_interest_rate": 50000,
          "interest_pay_to_bank": 53468,
          "total_offerred_discount_cashback_amount": 40000,
          "loan_amount": 1960000,
          "auth_amount": 1960000
     },
     "acquirer_data": {
          "acquirerId": 8004
     }
}
'
```

## Create Order

Order represents the shopping cart in a payment journey. Order plays a central part in the payment flow as the subsequent transactions such as payment, refund, get status are linked to it. For this, an order must be identified uniquely and to do so you can create and assign a random and unique order_id to an order. This order_id can be used for any subsequently linked transactions to the order.

An order comprises of the following details:

- Order Identifier - Order Id
- Payment details - Amount, Currency and Preferred PG
- Customer details - Customer Id, Customer Email, Customer Mobile.
- Product details - Product Id
- Address - Billing Address and Shipping Address
- Other details

#### Sample request body for Create Order

```curl
{
   "merchant_data":{
      "merchant_id":"11607",
      "merchant_access_code":"25ca9633-3ac2-484a-a632-a067ac6c0eed",
      "merchant_return_url":"http://10.200.146.139:9020/chargingrespnew.aspx",
      "merchant_order_id":"API-DEMO-DOC-2"
   },
   "payment_info_data":{
      "amount":200,
      "currency_code":"INR",
      "order_desc":"Test Order"
   },
   "customer_data":{
      "country_code":"91",
      "mobile_number":"9121004028",
      "email_id":"john.doe@gmail.com"
   },
   "billing_address_data":{
      "first_name":"John",
      "last_name":"Doe",
      "address1":"House No. 123",
      "address2":"Road XYZ",
      "address3":"Bengaluru",
      "pin_code":"111111",
      "city":"Bengaluru",
      "state":"Karnataka",
      "country":"India"
   },
   "shipping_address_data":{
      "first_name":"John",
      "last_name":"Doe",
      "address1":"House No. 123",
      "address2":"Road XYZ",
      "address3":"Bengaluru",
      "pin_code":"111111",
      "city":"Bengaluru",
      "state":"Karnataka",
      "country":"India"
   },
   "product_info_data":{
      "product_details":[
         {
            "product_code":"40",
            "product_amount":200
         }
      ]
   },
   "additional_info_data":{
      "rfu1":"123"
   }
}
```

Once you have created the request body, it has to be encoded in base64 format. Also a `x-verify` header is needed which would be a SHA256 hash of the encoded request using your SHA key.

#### Curl for Create order with encoded request body and x-verify header.

```curl
curl --request POST \
     --url https://api-staging.pluralonline.com/api/v1/order/create \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/json' \
     --header 'cache-control: no-cache' \
     --header 'x-verify: 09F7992D0B503D95551CD5D0571F50BAC77F161B72679967765623DC645972CC' \
     --data '
{
     "request": "ewogICAibWVyY2hhbnRfZGF0YSI6ewogICAgICAibWVyY2hhbnRfaWQiOiIxMTYwNyIsCiAgICAgICJtZXJjaGFudF9hY2Nlc3NfY29kZSI6IjI1Y2E5NjMzLTNhYzItNDg0YS1hNjMyLWEwNjdhYzZjMGVlZCIsCiAgICAgICJtZXJjaGFudF9yZXR1cm5fdXJsIjoiaHR0cDovLzEwLjIwMC4xNDYuMTM5OjkwMjAvY2hhcmdpbmdyZXNwbmV3LmFzcHgiLAogICAgICAibWVyY2hhbnRfb3JkZXJfaWQiOiJBUEktREVNTy1ET0MtMSIKICAgfSwKICAgInBheW1lbnRfaW5mb19kYXRhIjp7CiAgICAgICJhbW91bnQiOjIwMCwKICAgICAgImN1cnJlbmN5X2NvZGUiOiJJTlIiLAogICAgICAib3JkZXJfZGVzYyI6IlRlc3QgT3JkZXIiCiAgIH0sCiAgICJjdXN0b21lcl9kYXRhIjp7CiAgICAgICJjb3VudHJ5X2NvZGUiOiI5MSIsCiAgICAgICJtb2JpbGVfbnVtYmVyIjoiOTEyMTAwNDAyOCIsCiAgICAgICJlbWFpbF9pZCI6ImpvaG4uZG9lQGdtYWlsLmNvbSIKICAgfSwKICAgImJpbGxpbmdfYWRkcmVzc19kYXRhIjp7CiAgICAgICJmaXJzdF9uYW1lIjoiSm9obiIsCiAgICAgICJsYXN0X25hbWUiOiJEb2UiLAogICAgICAiYWRkcmVzczEiOiJIb3VzZSBOby4gMTIzIiwKICAgICAgImFkZHJlc3MyIjoiUm9hZCBYWVoiLAogICAgICAiYWRkcmVzczMiOiJCZW5nYWx1cnUiLAogICAgICAicGluX2NvZGUiOiIxMTExMTEiLAogICAgICAiY2l0eSI6IkJlbmdhbHVydSIsCiAgICAgICJzdGF0ZSI6Ikthcm5hdGFrYSIsCiAgICAgICJjb3VudHJ5IjoiSW5kaWEiCiAgIH0sCiAgICJzaGlwcGluZ19hZGRyZXNzX2RhdGEiOnsKICAgICAgImZpcnN0X25hbWUiOiJKb2huIiwKICAgICAgImxhc3RfbmFtZSI6IkRvZSIsCiAgICAgICJhZGRyZXNzMSI6IkhvdXNlIE5vLiAxMjMiLAogICAgICAiYWRkcmVzczIiOiJSb2FkIFhZWiIsCiAgICAgICJhZGRyZXNzMyI6IkJlbmdhbHVydSIsCiAgICAgICJwaW5fY29kZSI6IjExMTExMSIsCiAgICAgICJjaXR5IjoiQmVuZ2FsdXJ1IiwKICAgICAgInN0YXRlIjoiS2FybmF0YWthIiwKICAgICAgImNvdW50cnkiOiJJbmRpYSIKICAgfSwKICAgInByb2R1Y3RfaW5mb19kYXRhIjp7CiAgICAgICJwcm9kdWN0X2RldGFpbHMiOlsKICAgICAgICAgewogICAgICAgICAgICAicHJvZHVjdF9jb2RlIjoiNDAiLAogICAgICAgICAgICAicHJvZHVjdF9hbW91bnQiOjIwMAogICAgICAgICB9CiAgICAgIF0KICAgfSwKICAgImFkZGl0aW9uYWxfaW5mb19kYXRhIjp7CiAgICAgICJyZnUxIjoiMTIzIgogICB9Cn0="
}
'
```

#### Sample successful response for Create Order API call

```json
{
  "token": "8MLlV%2Fpl1MG1Enbv2W6snVvIXuyCX0Ym6i5Ie1AA1fs%3D",
  "plural_order_id": "106853"
}
```

## Process Payment

Once the order is created successfully, an order reference id (`plural_order_id`) is returned which the merchant needs to save in his database for future reference of the created order along with an order token. Also an order `token` is returned which needs to be sent in the next Payment Processing API call along with Payment details.

#### Curl for Process Payment API

```curl
curl --request POST \
     --url 'https://api-staging.pluralonline.com/api/v1/emi/process/payment?token=xqt8c5x37u%2BNrL8PLswbYcdcGNy%2FScq%2FG9HGkv5Cdmk%3D' \
     --header 'Accept: application/json' \
     --header 'Content-Type: application/json' \
     --header 'checkoutmode: SEAMLESS' \
     --data '
{
     "merchant_data": {
          "merchant_id": 11607
     },
     "card_data": {
          "card_number": "4012001037141112",
          "card_expiry_year": "2023",
          "card_expiry_month": "11",
          "card_holder_name": "John",
          "cvv": "123",
          "is_card_to_be_saved": true
     },
     "customer_data": {
          "country_code": "91",
          "mobile_number": "9582492811",
          "email_id": "john.doe@gmail.com",
          "customer_token": "AGxVyLz65ucoJrx+w1u1xQ=="
     },
     "emi_data": {
          "offer_scheme": {
               "product_details": [
                    {
                         "schemes": [
                              {
                                   "scheme_id": "46921",
                                   "program_type": 106,
                                   "is_scheme_valid": true
                              }
                         ],
                         "product_code": "2000",
                         "product_name": "2000",
                         "product_amount": 2000000,
                         "subvention_cashback_discount": 40000,
                         "product_discount": 0,
                         "subvention_cashback_discount_percentage": 20000,
                         "product_discount_percentage": 0,
                         "subvention_type": 2,
                         "bank_interest_rate_percentage": 50000,
                         "bank_interest_rate": 53468
                    }
               ],
               "emi_scheme": null
          },
          "tenure_id": "12",
          "tenure_in_month": "12",
          "monthly_installment": 167789,
          "bank_interest_rate": 50000,
          "interest_pay_to_bank": 53468,
          "total_offerred_discount_cashback_amount": 40000,
          "loan_amount": 1960000,
          "auth_amount": 1960000
     },
     "acquirer_data": {
          "acquirerId": 8004
     }
}
'
```

## Check Status

To get the latest status of the order or transaction, merchant can call Inquiry APIs. There are 4 types of Inquiry calls which a merchant can call, which are as follows:

- Fetch status of a specific payment

#### Curl for Status Inquiry API

```curl
curl --request GET \
     --url https://api-staging.pluralonline.com/api/v1/inquiry/order/{order_id} \
     --header 'Accept: application/json'
```

#### Response from Status Inquiry call

```json
{
  "merchant_data": {
    "merchant_id": 11435,
    "order_id": "2626L31LB41P9BS"
  },
  "order_data": {
    "order_status": "CHARGED",
    "plural_order_id": 105771,
    "amount": 1000,
    "order_desc": "One shirt",
    "refund_amount": "0"
  },
  "payment_info_data": {
    "acquirer_name": "RazorPay",
    "auth_code": "NA",
    "captured_amount_in_paisa": "1000",
    "card_holder_name": "NA",
    "masked_card_number": "NA",
    "merchant_return_url": "http://192.168.101.205:9073/chargingrespnew.aspx,https://www.google.com,",
    "mobile_no": "NA",
    "payment_completion_date_time": "2021-09-15T10:43:55.673Z",
    "payment_id": "431723",
    "payment_status": "CAPTURED",
    "payment_response_code": 1,
    "payment_response_message": "NA",
    "product_code": "NA",
    "rrn": "NA",
    "refund_amount_in_paisa": "0",
    "salted_card_hash": "NA",
    "udf_field_1": "NA",
    "udf_field_2": "NA",
    "udf_field_3": "NA",
    "udf_field_4": "NA",
    "payment_mode": "NETBANKING",
    "issuer_name": "NONE",
    "gateway_payment_id": "pay_HxcaJfiAUV5bOL"
  }
}
```

Next step is to encode the above JSON into base64 format. [Then generate SHA256 hash according to this logic ](https://developer.pluralonline.com/docs/hash-generation-logic) and then verify this hash with `x-verify` received in the response of Status Inquiry call

> 🚧 Important
> 
> Verifying the SHA with `x-verify` is an important step and should not be skipped to prevent any security issues.

## IMEI Validation API

IMEI validation is a process to ensure that the product belongs to the OEM who is subventing the EMI transaction.
