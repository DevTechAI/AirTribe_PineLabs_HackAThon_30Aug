---
title: "Steps for Redirect Integration"
slug: "steps-for-redirect-integration"
excerpt: "Redirect the customer to payment page rendered by Plural Console"
hidden: true
createdAt: "Wed Jan 12 2022 08:56:22 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:58:45 GMT+0000 (Coordinated Universal Time)"
---
For merchants who are not [PCI DSS compliant,](https://www.pcisecuritystandards.org/pci_security/maintaining_payment_security) the merchant can also choose to redirect the customer to Plural console payment page. 

The following are the main steps needed for an Redirect integration

- Create Order
- Call Redirect URL
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
     --header 'x-verify: 4CBD59DCEE294A6547C0DC942605EE8637426B11783626FB9CC831E37F5B0271' \
     --data '
{
     "request": "ewogICJtZXJjaGFudF9kYXRhIjogewogICAgIm1lcmNoYW50X2lkIjogIjExNzIwIiwKICAgICJtZXJjaGFudF9hY2Nlc3NfY29kZSI6ICIwMjAyYTg3ZC1jNDc0LTRkYWQtYWMzOC1jMWY2MWIyMmQyMDciLAogICAgIm1lcmNoYW50X3JldHVybl91cmwiOiAiaHR0cDovLzEwLjIwMC4xNDYuMTM5OjkwMjAvY2hhcmdpbmdyZXNwbmV3LmFzcHgiLAogICAgIm1lcmNoYW50X29yZGVyX2lkIjogIk1WUF9QTFVSQUxfMDA0IgogIH0sCiAgInBheW1lbnRfaW5mb19kYXRhIjogewogICAgImFtb3VudCI6IDYwMCwKICAgICJjdXJyZW5jeV9jb2RlIjogIklOUiIsCiAgICAib3JkZXJfZGVzYyI6ICJUZXN0IE9yZGVyIgogIH0sCiAgImN1c3RvbWVyX2RhdGEiOiB7CiAgICAiY291bnRyeV9jb2RlIjogIjkxIiwKICAgICJtb2JpbGVfbnVtYmVyIjogIjkwNTAxNTc5NzgiLAogICAgImVtYWlsX2lkIjogImJhbHdhbnQuc2luZ2hAcGluZWxhYnMuY29tIgogIH0sCiAgImJpbGxpbmdfYWRkcmVzc19kYXRhIjogewogICAgImZpcnN0X25hbWUiOiAiQmFsd2FudCIsCiAgICAibGFzdF9uYW1lIjogIlNpbmdoIiwKICAgICJhZGRyZXNzMSI6ICJIaXNhciIsCiAgICAiYWRkcmVzczIiOiAiSGlzYXIiLAogICAgImFkZHJlc3MzIjogIkhpc2FyIiwKICAgICJwaW5fY29kZSI6ICIxMjUwMDUiLAogICAgImNpdHkiOiAiSGlzYXIiLAogICAgInN0YXRlIjogIkhhcnlhbmEiLAogICAgImNvdW50cnkiOiAiSW5kaWEiCiAgfSwKICAic2hpcHBpbmdfYWRkcmVzc19kYXRhIjogewogICAgImZpcnN0X25hbWUiOiAiQmFsd2FudCIsCiAgICAibGFzdF9uYW1lIjogIlNpbmdoIiwKICAgICJhZGRyZXNzMSI6ICJIaXNhciIsCiAgICAiYWRkcmVzczIiOiAiSGlzYXIiLAogICAgImFkZHJlc3MzIjogIkhpc2FyIiwKICAgICJwaW5fY29kZSI6ICIxMjUwMDUiLAogICAgImNpdHkiOiAiSGlzYXIiLAogICAgInN0YXRlIjogIkhhcnlhbmEiLAogICAgImNvdW50cnkiOiAiSW5kaWEiCiAgfSwKICAicHJvZHVjdF9pbmZvX2RhdGEiOiB7CiAgICAicHJvZHVjdF9kZXRhaWxzIjogWwogICAgICB7CiAgICAgICAgInByb2R1Y3RfY29kZSI6ICIyMDAiLAogICAgICAgICJwcm9kdWN0X2Ftb3VudCI6IDYwMAogICAgICB9CiAgICBdCiAgfSwKICAiYWRkaXRpb25hbF9pbmZvX2RhdGEiOiB7CiAgICAicmZ1MSI6ICIxMjMiCiAgfQp9"
}
'
```

#### Sample successful response for Create Order API call

```json
{
  "token": "W00w76Hvu1Olp2c45TvCT2E5%2BNtYmSrHZppSS5IZvQk%3D",
    "plural_order_id": "110256"
}
```

## Call redirect URL

Merchant will get a token in a create order API response which needs to be appended in the below redirect URL. The customer will complete the transaction on this checkout page.

<https://checkout-staging.pluralonline.com/?orderToken=W00w76Hvu1Olp2c45TvCT2E5%2BNtYmSrHZppSS5IZvQk%3D&paymentMode=ALL&cardCategoryType=CC&showSavedCardsFeature=true>

## Implement Return Function (Success and Failure Handlers)

In the order flow as soon as there is a response from the acquirer, return URL will be called and response parameters of the payment are passed into it.

- The Success callback is called only once 
- The Failure callback can be called multiple times for each failure in a given transaction
- After success callback make status inquiry call (server to server)

#### Sample Success Response

```json
{
payment_id: "43343", plural_order_id: "434252"
}
```

#### Sample Failure Response

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
