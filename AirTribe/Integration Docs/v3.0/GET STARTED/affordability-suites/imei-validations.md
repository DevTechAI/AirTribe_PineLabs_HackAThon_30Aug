---
title: "IMEI Validation"
slug: "imei-validations"
excerpt: "Learn how you can validate the IMEI number using Plural API."
hidden: false
createdAt: "Fri Jan 24 2025 07:11:40 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Mar 20 2025 09:23:51 GMT+0000 (Coordinated Universal Time)"
---
Integrating with Plural, you can now include an IMEI verification flow, enabling merchants to verify product IMEI or serial numbers during the payment. This feature ensures compliance and enhances efficiency by integrating IMEI verification.

You can use this Plural IMEI Validation API to `Block` and `Unblock`.

Integrating with IMEI validations allows you to secure operations in EMI or loan-based purchases. IMEI validation ensures that the device associated with the payment is accurately identified and secured. Businesses use IMEI validation to manage processes like unblocking devices during returns or blocking them in cases of payment default.

### IMEI Validation API

Use this API to `Unblock` and `Block` the IMEI number.

Below are the sample requests and sample responses for a IMEI Validation API.

```curl cURL - UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/affordability/v1/product/order_id/imei \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_product_imei_reference": "merchant-ref-786",
  "request_type": "BLOCKING",
  "products": [
    {
      "product_code": "xyz",
      "dealer_code": "DLR100",
      "state_code": "NY",
      "product_imei": "SN1234567863"
    }
  ]
}
'
```
```curl cURL - PROD
curl --request POST \
     --url https://api.pluralpay.in/api/affordability/v1/product/order_id/imei \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_product_imei_reference": "merchant-ref-786",
  "request_type": "BLOCKING",
  "products": [
    {
      "product_code": "xyz",
      "dealer_code": "DLR100",
      "state_code": "NY",
      "product_imei": "SN1234567863"
    }
  ]
}
'
```
```json Sample Response
{
  "merchant_product_imei_reference": "merchant-ref-786",
  "request_type": "BLOCKING",
  "products": [
    {
      "product_code": "xyz",
      "dealer_code": "DLR100",
      "state_code": "NY",
      "product_imei": "SN1234567863",
      "product_imei_status": "BLOCKED",
      "product_brand_response": {}
    }
  ]
}
```
```json Failure - Sample Response
{
  "merchant_product_imei_reference": "merchant-ref-786",
  "request_type": "BLOCKING",
  "products": [
    {
      "product_code": "xyz",
      "dealer_code": "DLR100",
      "state_code": "NY",
      "product_imei": "SN1234567863",
      "product_brand_response": {
        "code": "PRODUCT_ALREADY_BLOCKED",
        "message": "Product is already blocked"
      }
    }
  ]
}
```

> 📘 Note:
> 
> - Once the refund request is successfully processed, the product IMEI will also be blocked in the backend.
> - For a full refund, all IMEIs linked to the product are automatically blocked. For a partial refund, you must provide the `product_imei` that needs to be blocked.
