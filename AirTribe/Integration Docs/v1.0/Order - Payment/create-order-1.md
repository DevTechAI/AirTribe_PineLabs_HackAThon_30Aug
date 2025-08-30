---
title: "Create Order"
slug: "create-order-1"
excerpt: "This API Help to create an Order Token."
hidden: false
metadata: 
  image: []
  robots: "index"
createdAt: "Thu Feb 03 2022 09:06:55 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Feb 14 2023 07:02:39 GMT+0000 (Coordinated Universal Time)"
---
**Request Parameters:** 

[block:parameters]
{
  "data": {
    "h-0": "Attribute",
    "h-1": "Type",
    "h-2": "Details",
    "h-3": "",
    "h-4": "",
    "0-0": "merchant_id\\*",
    "0-1": "integer",
    "0-2": "merchant_id is the unique identifier of the merchant.",
    "0-3": "",
    "0-4": "",
    "1-0": "merchant_access  \n\\_code\\*",
    "1-1": "string  \n(Length = 50 Characters)",
    "1-2": "Merchant unique identification id provided by Plural.",
    "1-3": "",
    "1-4": "",
    "2-0": "merchant_return  \n\\_url\\*",
    "2-1": "string  \n(Length=500 Characters)",
    "2-2": "Merchant url is the url to be provided by the merchant.",
    "2-3": "",
    "2-4": "",
    "3-0": "merchant_order_id\\*",
    "3-1": "string  \n(Length = 200 Characters)",
    "3-2": "Unique Order id of transaction maintained at Merchant end",
    "3-3": "",
    "3-4": "",
    "4-0": "amount\\*",
    "4-1": "long",
    "4-2": "The amount of the order in paise.",
    "4-3": "",
    "4-4": "",
    "5-0": "currency_code\\*",
    "5-1": "string",
    "5-2": "Currency code in which in the payment is intended. The currency code for Indian rupee is 'INR'.",
    "5-3": "",
    "5-4": "",
    "6-0": "order_desc",
    "6-1": "string",
    "6-2": "The decription of the order.",
    "6-3": "",
    "6-4": "",
    "7-0": "country_code\\*",
    "7-1": "string  \n(Length = 10 Characters)",
    "7-2": "The country code of the mobile number.",
    "7-3": "",
    "7-4": "",
    "8-0": "mobile_number\\*",
    "8-1": "string  \n(Length = 20 Characters)",
    "8-2": "Mobile number of the customer.",
    "8-3": "",
    "8-4": "",
    "9-0": "email_id\\*",
    "9-1": "string  \n(Length = 100 Characters)",
    "9-2": "Email id of the cusotmer.",
    "9-3": "",
    "9-4": "",
    "10-0": "billing_address  \n\\_data",
    "10-1": "{}",
    "10-2": "",
    "10-3": "",
    "10-4": "",
    "11-0": "first_name",
    "11-1": "string  \n(Length=50 Characters)",
    "11-2": "biller address First name.",
    "11-3": "",
    "11-4": "",
    "12-0": "last_name",
    "12-1": "string  \n(Length=50 Characters)",
    "12-2": "biller address Last name.",
    "12-3": "",
    "12-4": "",
    "13-0": "address1",
    "13-1": "string  \n(Length=200 Characters)",
    "13-2": "First line of the biller address .",
    "13-3": "",
    "13-4": "",
    "14-0": "address2",
    "14-1": "string  \n(Length=100 Characters)",
    "14-2": "Second line of the biller address.",
    "14-3": "",
    "14-4": "",
    "15-0": "address3",
    "15-1": "string  \n(Length=100 Characters)",
    "15-2": "Third line of the biller address.",
    "15-3": "",
    "15-4": "",
    "16-0": "pin_code",
    "16-1": "string  \n(Length=50 Characters)",
    "16-2": "PIN Code",
    "16-3": "",
    "16-4": "",
    "17-0": "city",
    "17-1": "string  \n(Length=50 Characters)",
    "17-2": "City",
    "17-3": "",
    "17-4": "",
    "18-0": "state",
    "18-1": "string  \n(Length=50 Characters)",
    "18-2": "State",
    "18-3": "",
    "18-4": "",
    "19-0": "country",
    "19-1": "string  \nstring  \n(Length=50 Characters)",
    "19-2": "Country",
    "19-3": "",
    "19-4": "",
    "20-0": "shipping_address  \n\\_data",
    "20-1": "{}",
    "20-2": "",
    "20-3": "",
    "20-4": "",
    "21-0": "first_name",
    "21-1": "string  \n(Length=50 Characters)",
    "21-2": "shipping address First name.",
    "21-3": "",
    "21-4": "",
    "22-0": "last_name",
    "22-1": "string  \n(Length=50 Characters)",
    "22-2": "shipping address Last name.",
    "22-3": "",
    "22-4": "",
    "23-0": "address1",
    "23-1": "string  \n(Length=200 Characters)",
    "23-2": "shipping address1.",
    "23-3": "",
    "23-4": "",
    "24-0": "address2",
    "24-1": "string  \n(Length=100 Characters)",
    "24-2": "shipping address 2.",
    "24-3": "",
    "24-4": "",
    "25-0": "address3",
    "25-1": "string  \n(Length=100 Characters)",
    "25-2": "shipping address 3.",
    "25-3": "",
    "25-4": "",
    "26-0": "pin_code",
    "26-1": "string  \n(Length=50 Characters)",
    "26-2": "Pincode",
    "26-3": "",
    "26-4": "",
    "27-0": "city",
    "27-1": "string  \n(Length=50 Characters)",
    "27-2": "city",
    "27-3": "",
    "27-4": "",
    "28-0": "state",
    "28-1": "string  \n(Length=50 Characters)",
    "28-2": "state",
    "28-3": "",
    "28-4": "",
    "29-0": "country",
    "29-1": "string  \n(Length=50 Characters)",
    "29-2": "country",
    "29-3": "",
    "29-4": "",
    "30-0": "product_info  \n\\_data",
    "30-1": "product_details\\[]  \n(Array of Product Details which)",
    "30-2": "Need to send for Implementing Brand EMI",
    "30-3": "",
    "30-4": "",
    "31-0": "product_details",
    "31-1": "()",
    "31-2": "",
    "31-3": "",
    "31-4": "",
    "32-0": "product_code\\*",
    "32-1": "string",
    "32-2": "Product code of the products added in the order. This code is to be provided in case of offers applied on these products.",
    "32-3": "",
    "32-4": "",
    "33-0": "product_amount\\*",
    "33-1": "long",
    "33-2": "The product amount in paise.",
    "33-3": "",
    "33-4": "",
    "34-0": "additional\\_  \ninfo_data",
    "34-1": "()",
    "34-2": "",
    "34-3": "",
    "34-4": "",
    "35-0": "rfu1",
    "35-1": "string  \n(Length=200 Characters)",
    "35-2": "RFU value is allowed as alpha-numeric with “#”, \"\\_\" and “-”",
    "35-3": "",
    "35-4": "",
    "36-0": "rfu2",
    "36-1": "string  \n(Length=200 Characters)",
    "36-2": "RFU value is allowed as alpha-numeric with “#”, \"\\_\" and “-”",
    "36-3": "",
    "36-4": "",
    "37-0": "rfu4",
    "37-1": "string  \n(Length=200 Characters)",
    "37-2": "RFU value is allowed as alpha-numeric with “#”, \"\\_\" and “-”",
    "37-3": "",
    "37-4": "",
    "38-0": "rfu5",
    "38-1": "string  \n(Length=200 Characters)",
    "38-2": "RFU value is allowed as alpha-numeric with “#”, \"\\_\" and “-”",
    "38-3": "",
    "38-4": "",
    "39-0": "rfu6",
    "39-1": "string  \n(Length=200 Characters)",
    "39-2": "RFU value is allowed as alpha-numeric with “#”, \"\\_\" and “-”",
    "39-3": "",
    "39-4": "",
    "40-0": "rfu7",
    "40-1": "string  \n(Length=200 Characters)",
    "40-2": "RFU value is allowed as alpha-numeric with “#”, \"\\_\" and “-”",
    "40-3": "",
    "40-4": "",
    "41-0": "rfu8",
    "41-1": "string  \n(Length=200 Characters)",
    "41-2": "RFU value is allowed as alpha-numeric with “#”, \"\\_\" and “-”",
    "41-3": "",
    "41-4": "",
    "42-0": "rfu9",
    "42-1": "string  \n(Length=200 Characters)",
    "42-2": "RFU value is allowed as alpha-numeric with “#”, \"\\_\" and “-”",
    "42-3": "",
    "42-4": "",
    "43-0": "rfu10",
    "43-1": "string  \n(Length=200 Characters)",
    "43-2": "RFU value is allowed as alpha-numeric with “#”, \"\\_\" and “-”",
    "43-3": "",
    "43-4": "",
    "44-0": "subscription_data",
    "44-1": "",
    "44-2": "{}",
    "44-3": "",
    "44-4": "",
    "45-0": "",
    "45-1": "plan_details",
    "45-2": "{}",
    "45-3": "",
    "45-4": "",
    "46-0": "",
    "46-1": "merchantId",
    "46-2": "string",
    "46-3": "",
    "46-4": "",
    "47-0": "",
    "47-1": "startDate",
    "47-2": "string(UTC time format  \nexample: 2023-01-31T18:30:00Z )",
    "47-3": "",
    "47-4": "",
    "48-0": "",
    "48-1": "endDate",
    "48-2": "string(UTC time format  \nexample: 2023-02-15T18:30:00Z)",
    "48-3": "",
    "48-4": "",
    "49-0": "",
    "49-1": "plan",
    "49-2": "{}",
    "49-3": "",
    "49-4": "",
    "50-0": "",
    "50-1": "",
    "50-2": "planId",
    "50-3": "string",
    "50-4": "required only for plural maintained plan",
    "51-0": "",
    "51-1": "",
    "51-2": "merchantPlanId",
    "51-3": "string",
    "51-4": "required only for merchant maintained plan",
    "52-0": "",
    "52-1": "",
    "52-2": "planName",
    "52-3": "string",
    "52-4": "required only for merchant maintained plan",
    "53-0": "",
    "53-1": "",
    "53-2": "frequencyType",
    "53-3": "",
    "53-4": "required only for merchant maintained plan",
    "54-0": "",
    "54-1": "",
    "54-2": "amount",
    "54-3": "{}",
    "54-4": "required only for merchant maintained plan",
    "55-0": "",
    "55-1": "",
    "55-2": "",
    "55-3": "value",
    "55-4": "string",
    "56-0": "",
    "56-1": "",
    "56-2": "",
    "56-3": "currency",
    "56-4": "string",
    "57-0": "",
    "57-1": "",
    "57-2": "maxLimitAmount",
    "57-3": "{}",
    "57-4": "required only for merchant maintained plan",
    "58-0": "",
    "58-1": "",
    "58-2": "",
    "58-3": "value",
    "58-4": "string",
    "59-0": "",
    "59-1": "",
    "59-2": "",
    "59-3": "currency",
    "59-4": "string",
    "60-0": "payment_category_type",
    "60-1": "string",
    "60-2": "",
    "60-3": "",
    "60-4": "",
    "61-0": "",
    "61-1": "",
    "61-2": "",
    "61-3": "",
    "61-4": ""
  },
  "cols": 5,
  "rows": 62,
  "align": [
    "left",
    "left",
    "left",
    "left",
    "left"
  ]
}
[/block]


**Request Body payload:** 

```json Sample payload for Base64
{
  "merchant_data": {
    "merchant_id": "11565",
    "merchant_access_code": "709ebcf1-3171-4b0a-891d-394fa259c63b",
    "merchant_return_url": "http://192.168.101.205:9073/chargingrespnew.aspx",
    "merchant_order_id": "MICROS"
  },
  "payment_info_data": {
    "amount": 500,
    "currency_code": "INR",
    "order_desc": "Test Order"
  },
  "customer_data": {
    "country_code": "91",
    "mobile_number": "xxx",
    "email_id": "balwant.singh@pinelabs.com"
  },
  "billing_address_data": {
    "first_name": "Balwant",
    "last_name": "Singh",
    "address1": "Hisar",
    "address2": "Hisar",
    "address3": "Hisar",
    "pin_code": "125005",
    "city": "Hisar",
    "state": "Haryana",
    "country": "India"
  },
  "shipping_address_data": {
    "first_name": "Balwant",
    "last_name": "Singh",
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
        "product_amount": 500
      }
    ]
  },
  "additional_info_data": {
    "rfu1": "123"
  },
    "subscription_data": {
    "plan_details": {
			"merchantId": "3004",
  		"startDate": "2023-02-06T18:30:00Z",
		  "endDate": "2023-02-10T18:30:00Z",
  "plan": {
    "planId": "4",
    "merchantPlanId": "merch007",
    "planName": "MPPlanDayNT",
    "frequencyType": "Day",
    "amount": {
      "value": 220,
      "currency": "INR"
    },
    "maxLimitAmount": {
      "value": 220,
      "currency": "INR"
    }
  }
    }
  },
  "payment_category_type": "RECURRANCE"

}
```

**Request Base64 Body payload:** 

```json Sample Request
{
    "request": "ewogICJtZXJjaGFudF9kYXRhIjogewogICAgIm1lcmNoYW50X2lkIjogIjMwMDAwMDQiLAogICAgIm1lcmNoYW50X2FjY2Vzc19jb2RlIjogImUwZGE3Mzk1LTllNWEtNDhkMS1iMDExLTAxMjdlYzk1MWUiLAogICAgIm1lcmNoYW50X3JldHVybl91cmwiOiAiaHR0cDovLzEwLjIwOC44LjEzOTo5MDIwL2NoYXJnaW5ncmVzcG5ldy5hc3B4IiwKICAgICJtZXJjaGFudF9vcmRlcl9pZCI6ICJmZWIxMzAxIgogIH0sCiAgInBheW1lbnRfaW5mb19kYXRhIjogewogICAgImFtb3VudCI6IDEwMCwKICAgICJjdXJyZW5jeV9jb2RlIjogIklOUiIsCiAgICAib3JkZXJfZGVzYyI6ICJUZXN0IFN1YnNjcmlwdGlvbiBPcmRlciBjcmVhdGlvbiIKICB9LAogICJjdXN0b21lcl9kYXRhIjogewogICAgImNvdW50cnlfY29kZSI6ICI5MSIsCiAgICAibW9iaWxlX251bWJlciI6ICI5NDQ0NjAwNjkzIiwKICAgICJlbWFpbF9pZCI6ICJrLmRoYWtzaGluYW1vb3J0aHlAcGluZWxhYnMuY29tIgogIH0sCiAgImJpbGxpbmdfYWRkcmVzc19kYXRhIjogewogICAgImZpcnN0X25hbWUiOiAiRGhha3NoaW4iLAogICAgImxhc3RfbmFtZSI6ICJLcmlzaCIsCiAgICAiYWRkcmVzczEiOiAiQ2hlbm5haSIsCiAgICAiYWRkcmVzczIiOiAiQ2hlbm5haSIsCiAgICAiYWRkcmVzczMiOiAiQ2hlbm5haSIsCiAgICAicGluX2NvZGUiOiAiNjAwMDA0IiwKICAgICJjaXR5IjogIkNoZW5uYWkiLAogICAgInN0YXRlIjogIlRhbWlsTmFkdSIsCiAgICAiY291bnRyeSI6ICJJbmRpYSIKICB9LAogICJzaGlwcGluZ19hZGRyZXNzX2RhdGEiOiB7CiAgICAiZmlyc3RfbmFtZSI6ICJEaGFrc2hpbiIsCiAgICAibGFzdF9uYW1lIjogIktyaXNoIiwKICAgICJhZGRyZXNzMSI6ICJDaGVubmFpIiwKICAgICJhZGRyZXNzMiI6ICJDaGVubmFpIiwKICAgICJhZGRyZXNzMyI6ICJDaGVubmFpIiwKICAgICJwaW5fY29kZSI6ICI2MDAwMDQiLAogICAgImNpdHkiOiAiQ2hlbm5haSIsCiAgICAic3RhdGUiOiAiVGFtaWxOYWR1IiwKICAgICJjb3VudHJ5IjogIkluZGlhIgogIH0sCiAgInByb2R1Y3RfaW5mb19kYXRhIjogewogICAgInByb2R1Y3RfZGV0YWlscyI6IFsKICAgICAgewogICAgICAgICJwcm9kdWN0X2NvZGUiOiAidGVzdCIsCiAgICAgICAgInByb2R1Y3RfYW1vdW50IjogMTAwCiAgICAgIH0KICAgIF0KICB9LAogICJhZGRpdGlvbmFsX2luZm9fZGF0YSI6IHsKICAgICJyZnUxIjogIiIsCiAgICAicmZ1MiI6ICIiLAogICAgInJmdTMiOiAiIiwKICAgICJyZnU0IjogIiIsCiAgICAicmZ1NSI6ICIiCiAgfSwKICAidHB2X2RhdGEiOiB7CiAgICAiYWNjb3VudF9udW1iZXIiOiAiIgogIH0sCiAgInN1YnNjcmlwdGlvbl9kYXRhIjogewogICAgInBsYW5fZGV0YWlscyI6IHsKICAgICAgIm1lcmNoYW50SWQiOiAiMzAwNCIsCiAgICAgICJzdGFydERhdGUiOiAiMjAyMy0wMi0xM1QxODozMDowMFoiLAogICAgICAiZW5kRGF0ZSI6ICIyMDIzLTAyLTE1VDE4OjMwOjAwWiIsCiAgICAgICJwbGFuIjogewogICAgICAgICJwbGFuSWQiOiAiMTAwIgogICAgICB9CiAgICB9CiAgfSwKICAicGF5bWVudF9jYXRlZ29yeV90eXBlIjogIlJFQ1VSUkFOQ0UiCn0="
}
```

**Response Payload:** 

```json 200 Success
{
    "token": "VKbSh6LbRRCoJmw31hBQI6ISeb%2Bl43FUki9CjQGIQcs%3D",
    "plural_order_id": "33902"
}
```
```json 400 Bad Request
{
    "error_code": "1160",
    "error_message": "SECURE_HASH_RETURNED_FROM_MERCHANT_NOT_MATCH"
}
```
```json Duplicate order
{
    "error_code": "1130",
    "error_message": "DUPLICATE_ORDER_RECEIVED_ON_MERCHANT"
}
```

**Response Parameters** 

| Parameter Name  | Type   | Description                                 |
| :-------------- | :----- | :------------------------------------------ |
| token           | string | create order token to pass for payment url. |
| plural_order_id | string | unique order id.                            |

| Parameter Name | Type   | Description            |
| :------------- | :----- | :--------------------- |
| error_code     | string | Response error code    |
| error_message  | string | Response error message |
