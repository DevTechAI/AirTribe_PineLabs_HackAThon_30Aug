---
title: "Steps for iFrame Integration"
slug: "iframe"
excerpt: "Embed iframe checkout on Merchant's website, Payment page is rendered by Plural Console."
hidden: true
createdAt: "Tue Sep 21 2021 12:25:14 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:58:36 GMT+0000 (Coordinated Universal Time)"
---
For merchants who are not [PCI DSS compliant,](https://www.pcisecuritystandards.org/pci_security/maintaining_payment_security) iFrame mode is the right choice. The iFrame checkout screen comes up as a seamless pop-up on the merchant website giving the user a good payment experience.

The following are the main steps needed for an iFrame integration

- Create Order
- Embed iFrame Checkout
- Implement Return Function
- Check Status

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

```json
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

## Embed iFrame Checkout

Merchant has to embed Plural Console's iframe checkout via a JS library. This will give access to call iframe functions from website code.

- Add script to website
- Make an object with `Order Id`, `Platform`
- Create an instance for Plural  `const objectname =  new Plural()`
- Call `Open` funtion to open iframe checkout.
- Signup/Signin function to be called based on whether returning customer or not
- Call `Close` function to close iframe

#### Script to be added on Merchant Website

```javascript
<script src="https://checkout-staging.pluralonline.com/v1/web-sdk-checkout.js"></script>
```

#### Script for Calling iFrame Web browser SDK (on click of Pay now button on Merchant site)

```javascript
const options = {
    theme: theme, // "default" or "black"
    orderToken: orderToken,
    channelId: channelId, // "APP" or "WEB"
    paymentMode: paymentMode,// comma separated - Example - 'CREDIT_DEBIT,NETBANKING,UPI,WALLET,EMI,DEBIT_EMI'
    countryCode: countryCode,// type = string, default "91"
    mobileNumber: mobileNumber, // type = string, default = null
    emailId: emailId, //default null
    showSavedCardsFeature: showSavedCardsFeature // type = boolean, default = true
   successHandler: async function(response) {
        // Handle success response
    },
    failedHandler: async function(response) {
        // Handle failure response
    }
  };
  const plural = new Plural(options);
  plural.open(options);
```

> 🚧 Skipping Login Page
> 
> If for your use case you are not using saved cards feature and will be sending `showSavedCardsFeature` value as `false` then the login page from Plural will be skipped. Please make sure the `mobileNumber` and `emailId` values are sent, given these are required by downstream acquirer gateways.

## Implement Callback Function (Success and Failure Handlers)

In the order flow as soon as there is a response from the acquirer, return function will be called and response parameters of the payment are passed into it.

- The Success callback is called only once 
- The Failure callback can be called multiple times for each failure in a given transaction
- After success CB make status inquiry s2s call

#### Sample Success Callback

```json
{
payment_id: "43343", plural_order_id: "434252"
}
```

#### Sample Failure Callback

```json
{
   "error_code":"401",
   "error_message":"Cancelled by user",
   "payment_id":"434343",
   "plural_order_id":"64764"
}
```

## Check Status

To get the latest status of the order or transaction, merchant can call Inquiry APIs. There are 3 types of Inquiry calls which a merchant can call, which are as follows:

- Fetch status of a specific payment

#### Curl for Status Inquiry API

```curl
curl --location 'https://api-staging.pluralonline.com/api/v1/inquiry/order/156096/payment/8069673' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic MTIyNzY6ZTAwZGYzYjItNWY1Ni00ZTZkLTgwY2UtZWI1NGVkNDBhNzJh'
```

#### Response from Status Inquiry

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
