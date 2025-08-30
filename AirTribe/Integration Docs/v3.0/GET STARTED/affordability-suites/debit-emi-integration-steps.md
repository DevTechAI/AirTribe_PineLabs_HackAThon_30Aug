---
title: "Debit EMI - Integration Steps"
slug: "debit-emi-integration-steps"
excerpt: "Learn how to integrate the Plural Affordability Suite to provide your merchants with a seamless shopping experience."
hidden: false
createdAt: "Wed Jan 29 2025 09:02:39 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Apr 23 2025 06:56:02 GMT+0000 (Coordinated Universal Time)"
---
Follow the below steps to integrate with Plural affordability suite in your application.

1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/debit-emi-integration-steps#1-prerequisite-generate-token" >\[Prerequisite] Generate Token</a>
2. <a href="https://developer.pluralonline.com/docs/debit-emi-integration-steps#2-offer-discovery" >Offer Discovery</a>
3. <a href="https://developer.pluralonline.com/docs/debit-emi-integration-steps#3-offer-validation" >Offer Validation</a>
4. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/debit-emi-integration-steps#4-create-order" >Create Order</a>
5. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/debit-emi-integration-steps#5-create-payment" >Create Payment</a>
6. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/debit-emi-integration-steps#6-handle-payment" >Handle Payment</a>
   1. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/debit-emi-integration-steps#61-store-payment-details-on-your-server" >Store Payment Details on Your Server</a>
   2. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/debit-emi-integration-steps#62-verify-payment-signature" >Verify Payment Signature</a>
7. <a style="text-decoration:underline;" href ="https://developer.pluralonline.com/docs/debit-emi-integration-steps#7-get-order-by-order-id" >Get Order by Order ID</a>

> 📘 Note
> 
> - Ensure you store your Client ID and Secret in your Backend securely.
> - Integrate our APIs on your backend system.
> - We strictly recommend not to call our APIs from the frontend.

> 🚧 Watch Out
> 
> - To Integrate with Plural seamless checkout flow you must have a PCI compliance certificate.

## 1. [Prerequisite] Generate Token

Integrate our Generate Token API in your backend servers to generate the access token. Use the token generated to authenticate Plural APIs.

Below are the sample requests and response for the Generate Token API.

```curl cURL – UAT
curl --location 'https://pluraluat.v2.pinepg.in/api/auth/v1/token' \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--data '
{
  "client_id": "a17ce30e-f88e-4f81-ada1-c3b4909ed232",
  "client_secret": "fgwei7egyhuggwp39w8rh",
  "grant_type": "client_credentials"
}
'
```
```curl cURL – PROD
curl --location 'https://api.pluralpay.in/api/auth/v1/token' \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
--header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
--data '
{
  "client_id": "a17ce30e-f88e-4f81-ada1-c3b4909ed232",
  "client_secret": "fgwei7egyhuggwp39w8rh",
  "grant_type": "client_credentials"
}
'
```
```json Sample Response
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
  "expires_in": 3600
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/v3.0/reference/generate-token" target="_blank">Generate Token API</a> documentation to learn more.

## 2. Offer Discovery

Use this API to check the offers and calculate the EMI.

Below are the sample requests and response for the Offer Discovery API.

#### **Bank EMI**

```curl cURL - UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/affordability/v1/offer/discovery \
     --compressed \
     --header 'Accept-Encoding: gzip' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "order_amount": {
    "currency": "INR",
    "value": 1200000
  }
}
'
```
```curl cURL - PROD
curl --request POST \
     --url https://api.pluralpay.in/api/affordability/v1/offer/discovery \
     --compressed \
     --header 'Accept-Encoding: gzip' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "order_amount": {
    "currency": "INR",
    "value": 1200000
  }
}
'
```
```json Sample Response
{
  "issuers": [
    {
      "id": "23",
      "name": "INDUSIND CC",
      "issuer_type": "CC_BANK",
      "priority": 1,
      "tenures": [
        {
          "tenure_id": "1",
          "name": "3 Months",
          "tenure_type": "MONTH",
          "tenure_value": 3,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1232139
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 410713
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1232139
          },
          "interest_amount": {
            "currency": "INR",
            "value": 32139
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "2",
          "name": "6 Months",
          "tenure_type": "MONTH",
          "tenure_value": 6,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1256616
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 209436
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1256616
          },
          "interest_amount": {
            "currency": "INR",
            "value": 56616
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "3",
          "name": "9 Months",
          "tenure_type": "MONTH",
          "tenure_value": 9,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1281411
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 142379
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1281411
          },
          "interest_amount": {
            "currency": "INR",
            "value": 81411
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "4",
          "name": "12 Months",
          "tenure_type": "MONTH",
          "tenure_value": 12,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1306524
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 108877
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1306524
          },
          "interest_amount": {
            "currency": "INR",
            "value": 106524
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "5",
          "name": "18 Months",
          "tenure_type": "MONTH",
          "tenure_value": 18,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1357686
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 75427
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1357686
          },
          "interest_amount": {
            "currency": "INR",
            "value": 157686
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "6",
          "name": "24 Months",
          "tenure_type": "MONTH",
          "tenure_value": 24,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "discount": {},
          "loan_amount": {
            "currency": "INR",
            "value": 1200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1410120
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 58755
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1410120
          },
          "interest_amount": {
            "currency": "INR",
            "value": 210120
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        }
      ],
      "issuer_data": {}
    }
  ]
}
```

#### **Brand EMI**

```curl cURL - UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/affordability/v1/offer/discovery \
     --compressed \
     --header 'Accept-Encoding: gzip' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "order_amount": {
    "currency": "INR",
    "value": 1200000
  },
  "product_details": [
    {
      "product_code": "xyz",
      "product_amount": {
        "currency": "INR",
        "value": 1200000
      },
      "product_coupon_discount_amount": {
        "currency": "INR",
        "value": 1200000
      }
    }
  ],
  "cart_coupon_discount_amount": {
    "currency": "INR",
    "value": 1200000
  }
}
'
```
```curl cURL - PROD
curl --request POST \
     --url https://api.pluralpay.in/api/affordability/v1/offer/discovery \
     --compressed \
     --header 'Accept-Encoding: gzip' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "order_amount": {
    "currency": "INR",
    "value": 1200000
  },
  "product_details": [
    {
      "product_code": "xyz",
      "product_amount": {
        "currency": "INR",
        "value": 1200000
      },
      "product_coupon_discount_amount": {
        "currency": "INR",
        "value": 1200000
      }
    }
  ],
  "cart_coupon_discount_amount": {
    "currency": "INR",
    "value": 1200000
  }
}
'
```
```json Sample Response
{
  "issuers": [
    {
      "id": "25",
      "name": "PNB CC",
      "issuer_type": "CC_BANK",
      "priority": 1,
      "tenures": [
        {
          "tenure_id": "1",
          "name": "3 Months",
          "tenure_type": "MONTH",
          "tenure_value": 3,
          "issuer_offer_parameters": [
            {
              "program_type": "BRAND_EMI",
              "offer_id": "309",
              "offer_parameter_id": "20"
            }
          ],
          "details": [
            {
              "product_code": "redmi_1",
              "brand_id": "3",
              "product_offer_parameters": [
                {
                  "program_type": "BRAND_OFFER",
                  "offer_id": "309",
                  "offer_parameter_id": "20"
                }
              ],
              "product_amount": {
                "currency": "INR",
                "value": 2000000
              },
              "subvention": {
                "subvention_type": "INSTANT",
                "percentage": 5,
                "amount": {
                  "currency": "INR",
                  "value": 85714
                },
                "breakup": {
                  "brand": {
                    "amount": {
                      "currency": "INR",
                      "value": 85714
                    }
                  }
                }
              },
              "discount": {
                "discount_type": "INSTANT",
                "percentage": 10,
                "amount": {
                  "currency": "INR",
                  "value": 200000
                },
                "breakup": {
                  "merchant": {
                    "amount": {
                      "currency": "INR",
                      "value": 100000
                    }
                  },
                  "brand": {
                    "amount": {
                      "currency": "INR",
                      "value": 100000
                    }
                  }
                }
              }
            }
          ],
          "discount": {
            "discount_type": "INSTANT",
            "percentage": 10,
            "amount": {
              "currency": "INR",
              "value": 200000
            },
            "breakup": {
              "merchant": {
                "amount": {
                  "currency": "INR",
                  "value": 100000
                }
              },
              "brand": {
                "amount": {
                  "currency": "INR",
                  "value": 100000
                }
              }
            }
          },
          "loan_amount": {
            "currency": "INR",
            "value": 1714286
          },
          "total_discount_amount": {
            "currency": "INR",
            "value": 200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1760202
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 586734
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1760202
          },
          "interest_amount": {
            "currency": "INR",
            "value": 45916
          },
          "total_subvention_amount": {
            "currency": "INR",
            "value": 85714
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "NO_COST"
        },
        {
          "tenure_id": "12",
          "name": "36 Months",
          "tenure_type": "MONTH",
          "tenure_value": 36,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1562",
              "offer_parameter_id": "63812"
            }
          ],
          "details": [],
          "loan_amount": {
            "currency": "INR",
            "value": 2000000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 2531304
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 70314
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 2531304
          },
          "interest_amount": {
            "currency": "INR",
            "value": 531304
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "2",
          "name": "6 Months",
          "tenure_type": "MONTH",
          "tenure_value": 6,
          "issuer_offer_parameters": [
            {
              "program_type": "BRAND_EMI",
              "offer_id": "309",
              "offer_parameter_id": "20"
            }
          ],
          "details": [
            {
              "product_code": "redmi_1",
              "brand_id": "3",
              "product_offer_parameters": [
                {
                  "program_type": "BRAND_OFFER",
                  "offer_id": "309",
                  "offer_parameter_id": "20"
                }
              ],
              "product_amount": {
                "currency": "INR",
                "value": 2000000
              },
              "subvention": {
                "subvention_type": "POST",
                "percentage": 5,
                "amount": {
                  "currency": "INR",
                  "value": 90000
                },
                "breakup": {
                  "brand": {
                    "amount": {
                      "currency": "INR",
                      "value": 90000
                    }
                  }
                }
              },
              "discount": {
                "discount_type": "INSTANT",
                "percentage": 10,
                "amount": {
                  "currency": "INR",
                  "value": 200000
                },
                "breakup": {
                  "merchant": {
                    "amount": {
                      "currency": "INR",
                      "value": 100000
                    }
                  },
                  "brand": {
                    "amount": {
                      "currency": "INR",
                      "value": 100000
                    }
                  }
                }
              }
            }
          ],
          "discount": {
            "discount_type": "INSTANT",
            "percentage": 10,
            "amount": {
              "currency": "INR",
              "value": 200000
            },
            "breakup": {
              "merchant": {
                "amount": {
                  "currency": "INR",
                  "value": 100000
                }
              },
              "brand": {
                "amount": {
                  "currency": "INR",
                  "value": 100000
                }
              }
            }
          },
          "loan_amount": {
            "currency": "INR",
            "value": 1800000
          },
          "total_discount_amount": {
            "currency": "INR",
            "value": 200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1884924
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 314154
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1884924
          },
          "interest_amount": {
            "currency": "INR",
            "value": 84924
          },
          "total_subvention_amount": {
            "currency": "INR",
            "value": 90000
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "NO_COST"
        },
        {
          "tenure_id": "3",
          "name": "9 Months",
          "tenure_type": "MONTH",
          "tenure_value": 9,
          "issuer_offer_parameters": [
            {
              "program_type": "BRAND_EMI",
              "offer_id": "309",
              "offer_parameter_id": "20"
            }
          ],
          "details": [
            {
              "product_code": "redmi_1",
              "brand_id": "3",
              "product_offer_parameters": [
                {
                  "program_type": "BRAND_OFFER",
                  "offer_id": "309",
                  "offer_parameter_id": "20"
                }
              ],
              "product_amount": {
                "currency": "INR",
                "value": 2000000
              },
              "subvention": {
                "subvention_type": "POST",
                "percentage": 5,
                "amount": {
                  "currency": "INR",
                  "value": 90000
                },
                "breakup": {
                  "brand": {
                    "amount": {
                      "currency": "INR",
                      "value": 90000
                    }
                  }
                }
              },
              "discount": {
                "discount_type": "INSTANT",
                "percentage": 10,
                "amount": {
                  "currency": "INR",
                  "value": 200000
                },
                "breakup": {
                  "merchant": {
                    "amount": {
                      "currency": "INR",
                      "value": 100000
                    }
                  },
                  "brand": {
                    "amount": {
                      "currency": "INR",
                      "value": 100000
                    }
                  }
                }
              }
            }
          ],
          "discount": {
            "discount_type": "INSTANT",
            "percentage": 10,
            "amount": {
              "currency": "INR",
              "value": 200000
            },
            "breakup": {
              "merchant": {
                "amount": {
                  "currency": "INR",
                  "value": 100000
                }
              },
              "brand": {
                "amount": {
                  "currency": "INR",
                  "value": 100000
                }
              }
            }
          },
          "loan_amount": {
            "currency": "INR",
            "value": 1800000
          },
          "total_discount_amount": {
            "currency": "INR",
            "value": 200000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 1922112
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 213568
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 1922112
          },
          "interest_amount": {
            "currency": "INR",
            "value": 122112
          },
          "total_subvention_amount": {
            "currency": "INR",
            "value": 90000
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 29900
            }
          },
          "emi_type": "LOW_COST"
        },
        {
          "tenure_id": "4",
          "name": "12 Months",
          "tenure_type": "MONTH",
          "tenure_value": 12,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "loan_amount": {
            "currency": "INR",
            "value": 2000000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 2177532
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 181461
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 2177532
          },
          "interest_amount": {
            "currency": "INR",
            "value": 177532
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "5",
          "name": "18 Months",
          "tenure_type": "MONTH",
          "tenure_value": 18,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1595",
              "offer_parameter_id": "63850"
            }
          ],
          "details": [],
          "loan_amount": {
            "currency": "INR",
            "value": 2000000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 2262816
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 125712
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 2262816
          },
          "interest_amount": {
            "currency": "INR",
            "value": 262816
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        },
        {
          "tenure_id": "6",
          "name": "24 Months",
          "tenure_type": "MONTH",
          "tenure_value": 24,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "1563",
              "offer_parameter_id": "63813"
            }
          ],
          "details": [],
          "loan_amount": {
            "currency": "INR",
            "value": 2000000
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 2350224
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 97926
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 2350224
          },
          "interest_amount": {
            "currency": "INR",
            "value": 350224
          },
          "interest_rate_percentage": 16,
          "processing_fee_details": {
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        }
      ],
      "issuer_data": {}
    }
  ]
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/offer-discovery-create" target="_blank">Offer Discovery API</a> documentation to learn more.

## 3. Offer Validation

Use this API for validating applied offers.

Below are the sample requests and response for the Offer Validation API.

```curl cURL - UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/affordability/v1/offer/validate \
     --compressed \
     --header 'Accept-Encoding: gzip' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "order_amount": {
    "value": 2000000,
    "currency": "INR"
  },
  "payment_amount": {
    "value": 1950000,
    "currency": "INR"
  },
  "offer_data": {
    "offer_details": {
      "tenure": {
        "loan_amount": {
          "currency": "INR",
          "value": 1950000
        },
        "total_discount_amount": {
          "currency": "INR",
          "value": 50000
        },
        "net_payment_amount": {
          "currency": "INR",
          "value": 2015358
        },
        "monthly_emi_amount": {
          "currency": "INR",
          "value": 671786
        },
        "total_emi_amount": {
          "currency": "INR",
          "value": 2015358
        },
        "interest_amount": {
          "currency": "INR",
          "value": 65358
        },
        "processing_fee_details": {
          "amount": {
            "currency": "INR",
            "value": 19900
          }
        },
        "tenure_id": "1",
        "name": "3 Months",
        "tenure_type": "MONTH",
        "tenure_value": 3,
        "issuer_offer_parameters": [
          {
            "program_type": "BANK_EMI",
            "offer_id": "1564",
            "offer_parameter_id": "63814"
          },
          {
            "program_type": "MERCHANT_BANK_OFFER",
            "offer_id": "1523",
            "offer_parameter_id": "63566"
          }
        ],
        "discount": {
          "discount_type": "INSTANT",
          "amount": {
            "currency": "INR",
            "value": 50000
          }
        },
        "interest_rate_percentage": 20,
        "emi_type": "STANDARD"
      },
      "id": "6",
      "name": "HDFC CC",
      "issuer_type": "CC_BANK",
      "priority": 1
    }
  },
  "payment_method": "CREDIT_EMI",
  "payment_option": {
    "card_details": {
      "card_number": "4690000046910000"
    }
  }
}
'
```
```curl cURL - PROD
curl --request POST \
     --url https://api.pluralpay.in/api/affordability/v1/offer/validate \
     --compressed \
     --header 'Accept-Encoding: gzip' \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "order_amount": {
    "value": 2000000,
    "currency": "INR"
  },
  "payment_amount": {
    "value": 1950000,
    "currency": "INR"
  },
  "offer_data": {
    "offer_details": {
      "tenure": {
        "loan_amount": {
          "currency": "INR",
          "value": 1950000
        },
        "total_discount_amount": {
          "currency": "INR",
          "value": 50000
        },
        "net_payment_amount": {
          "currency": "INR",
          "value": 2015358
        },
        "monthly_emi_amount": {
          "currency": "INR",
          "value": 671786
        },
        "total_emi_amount": {
          "currency": "INR",
          "value": 2015358
        },
        "interest_amount": {
          "currency": "INR",
          "value": 65358
        },
        "processing_fee_details": {
          "amount": {
            "currency": "INR",
            "value": 19900
          }
        },
        "tenure_id": "1",
        "name": "3 Months",
        "tenure_type": "MONTH",
        "tenure_value": 3,
        "issuer_offer_parameters": [
          {
            "program_type": "BANK_EMI",
            "offer_id": "1564",
            "offer_parameter_id": "63814"
          },
          {
            "program_type": "MERCHANT_BANK_OFFER",
            "offer_id": "1523",
            "offer_parameter_id": "63566"
          }
        ],
        "discount": {
          "discount_type": "INSTANT",
          "amount": {
            "currency": "INR",
            "value": 50000
          }
        },
        "interest_rate_percentage": 20,
        "emi_type": "STANDARD"
      },
      "id": "6",
      "name": "HDFC CC",
      "issuer_type": "CC_BANK",
      "priority": 1
    }
  },
  "payment_method": "CREDIT_EMI",
  "payment_option": {
    "card_details": {
      "card_number": "4690000046910000"
    }
  }
}
'
```
```json Sample Response
{
  "code": "ELIGIBLE",
  "message": "Offer is Eligible"
}
```

Refer to our <a style="text-decoration:underline" href="https://developer.pluralonline.com/reference/offer-validation-create" target="_blank">Offer Validation API</a> documentation to learn more.

## 4. Create Order

To create an Order, use our Create Order API, for authentication use the generated access token in the headers of the API request.

Below are the sample requests and response for a Create Order API.

```curl cURL - UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/orders \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_order_reference":112345,
  "order_amount":{
    "value":1100,
    "currency":"INR"
  },
  "pre_auth":false,
  "allowed_payment_methods":[
    "CARD",
    "UPI",
    "NETBANKING",
    "POINTS",
    "WALLET"
  ],
  "notes":"order1",
  "callback_url":"https://sample-callback-url",
  "failure_callback_url": "https://sample-failure-callback-url",
  "purchase_details":{
    "customer":{
      "email_id":"kevin.bob@example.com",
      "first_name":"Kevin",
      "last_name":"Bob",
      "customer_id":"123456",
      "mobile_number":"9876543210",
      "billing_address":{
        "address1":"10 Downing Street Westminster London",
        "address2":"Oxford Street Westminster London",
        "address3":"Baker Street Westminster London",
        "pincode":"51524036",
        "city":"Westminster",
        "state":"Westminster",
        "country":"London"
      },
      "shipping_address":{
        "address1":"10 Downing Street Westminster London",
        "address2":"Oxford Street Westminster London",
        "address3":"Baker Street Westminster London",
        "pincode":"51524036",
        "city":"Westminster",
        "state":"Westminster",
        "country":"London"
      }
    },
    "merchant_metadata":{
      "key1":"DD",
      "key2":"XOF"
    }
  },
  "cart_coupon_discount_amount":{
    "value":100,
    "currency":"INR"
  }
}
'
```
```curl cURL - PROD
curl --request POST \
     --url https://api.pluralpay.in/api/pay/v1/orders \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_order_reference":112345,
  "order_amount":{
    "value":1100,
    "currency":"INR"
  },
  "pre_auth":false,
  "allowed_payment_methods":[
    "CARD",
    "UPI",
    "NETBANKING",
    "POINTS",
    "WALLET"
  ],
  "notes":"order1",
  "callback_url":"https://sample-callback-url",
  "failure_callback_url": "https://sample-failure-callback-url",
  "purchase_details":{
    "customer":{
      "email_id":"kevin.bob@example.com",
      "first_name":"Kevin",
      "last_name":"Bob",
      "customer_id":"123456",
      "mobile_number":"9876543210",
      "billing_address":{
        "address1":"10 Downing Street Westminster London",
        "address2":"Oxford Street Westminster London",
        "address3":"Baker Street Westminster London",
        "pincode":"51524036",
        "city":"Westminster",
        "state":"Westminster",
        "country":"London"
      },
      "shipping_address":{
        "address1":"10 Downing Street Westminster London",
        "address2":"Oxford Street Westminster London",
        "address3":"Baker Street Westminster London",
        "pincode":"51524036",
        "city":"Westminster",
        "state":"Westminster",
        "country":"London"
      }
    },
    "merchant_metadata":{
      "key1":"DD",
      "key2":"XOF"
    }
  },
  "cart_coupon_discount_amount":{
    "value":100,
    "currency":"INR"
  }
}
'
```
```json Sample Response
{
  "data":{
    "order_id":"v1-4405071524-aa-qlAtAf",
    "merchant_order_reference":"112345",
    "type":"CHARGE",
    "status":"CREATED",
    "merchant_id":"104359",
    "order_amount":{
      "value":1100,
      "currency":"INR"
    },
    "pre_auth":false,
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
    "notes":"order1",
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "purchase_details":{
      "customer":{
        "email_id":"kevin.bob@example.com",
        "first_name":"Kevin",
        "last_name":"Bob",
        "customer_id":"123456",
        "mobile_number":"9876543210",
        "billing_address":{
          "address1":"10 Downing Street Westminster London",
          "address2":"Oxford Street Westminster London",
          "address3":"Baker Street Westminster London",
          "pincode":"51524036",
          "city":"Westminster",
          "state":"Westminster",
          "country":"London"
        },
        "shipping_address":{
          "address1":"10 Downing Street Westminster London",
          "address2":"Oxford Street Westminster London",
          "address3":"Baker Street Westminster London",
          "pincode":"51524036",
          "city":"Westminster",
          "state":"Westminster",
          "country":"London"
        }
      },
      "merchant_metadata":{
        "key1":"DD",
        "key2":"XOF"
      }
    },
    "payments":[
      
    ],
    "created_at":"2024-07-15T05:44:51.174Z",
    "updated_at":"2024-07-15T05:44:51.174Z",
    "cart_coupon_discount_amount":{
      "value":100,
      "currency":"INR"
    }
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/reference/affordability-suite-orders-create" target="_blank">Create Order API</a> documentation to learn more.

> 📘 Note:
> 
> When the pre-authorization is set to true you can capture the payment after successful delivery or service.

## 5. Create Payment

To create a payment, use our Create Payment API, use the `order_id` returned in the response of a Create Order API to link the payment against an order.

Below are the sample requests and sample response for distinct Acquirers for Create Payment API.

#### **HDFC DEBIT EMI**

```curl cURL - UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/payments \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "payments": [
    {
      "merchant_payment_reference": "5419190411211587",
      "payment_method": "DEBIT_EMI",
      "payment_amount": {
        "value": 219900,
        "currency": "INR"
      },
      "payment_option": {
        "card_details": {
          "name": "John Doe",
          "card_number": "5419190411211587",
          "registered_mobile_number": "9582223917"
        }
      },
      "offer_data": {
        "offer_details": {
          "id": "7",
          "name": "HDFC DC",
          "display_name": "HDFC BANK",
          "issuer_type": "DC_BANK",
          "priority": 1,
          "tenure": {
            "tenure_id": "6",
            "name": "24 Months",
            "tenure_type": "MONTH",
            "tenure_value": 24,
            "issuer_offer_parameters": [
              {
                "program_type": "BANK_EMI",
                "offer_id": "3498",
                "offer_parameter_id": "199796"
              },
              {
                "program_type": "MERCHANT_BANK_OFFER",
                "offer_id": "3678",
                "offer_parameter_id": "203706"
              }
            ],
            "details": [
              {
                "product_code": "xyz",
                "product_display_name": "Redmi Note 13 5G",
                "brand_name": "Xiaomi",
                "product_amount": {
                  "currency": "INR",
                  "value": 219900
                },
                "interest_amount": {
                  "currency": "INR",
                  "value": 38508
                },
                "interest_rate": 16
              }
            ],
            "loan_amount": {
              "currency": "INR",
              "value": 219900
            },
            "net_payment_amount": {
              "currency": "INR",
              "value": 258408
            },
            "monthly_emi_amount": {
              "currency": "INR",
              "value": 10767
            },
            "total_emi_amount": {
              "currency": "INR",
              "value": 258408
            },
            "interest_amount": {
              "currency": "INR",
              "value": 38508
            },
            "interest_rate_percentage": 16,
            "emi_type": "STANDARD"
          }
        }
      }
    }
  ]
}
'
```
```curl cURL - PROD
curl --request POST \
     --url https://api.pluralpay.in/api/pay/v1/orders/{order_id}/payments \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "payments": [
    {
      "merchant_payment_reference": "5419190411211587",
      "payment_method": "DEBIT_EMI",
      "payment_amount": {
        "value": 219900,
        "currency": "INR"
      },
      "payment_option": {
        "card_details": {
          "name": "John Doe",
          "card_number": "5419190411211587",
          "registered_mobile_number": "9582223917"
        }
      },
      "offer_data": {
        "offer_details": {
          "id": "7",
          "name": "HDFC DC",
          "display_name": "HDFC BANK",
          "issuer_type": "DC_BANK",
          "priority": 1,
          "tenure": {
            "tenure_id": "6",
            "name": "24 Months",
            "tenure_type": "MONTH",
            "tenure_value": 24,
            "issuer_offer_parameters": [
              {
                "program_type": "BANK_EMI",
                "offer_id": "3498",
                "offer_parameter_id": "199796"
              },
              {
                "program_type": "MERCHANT_BANK_OFFER",
                "offer_id": "3678",
                "offer_parameter_id": "203706"
              }
            ],
            "details": [
              {
                "product_code": "xyz",
                "product_display_name": "Redmi Note 13 5G",
                "brand_name": "Xiaomi",
                "product_amount": {
                  "currency": "INR",
                  "value": 219900
                },
                "interest_amount": {
                  "currency": "INR",
                  "value": 38508
                },
                "interest_rate": 16
              }
            ],
            "loan_amount": {
              "currency": "INR",
              "value": 219900
            },
            "net_payment_amount": {
              "currency": "INR",
              "value": 258408
            },
            "monthly_emi_amount": {
              "currency": "INR",
              "value": 10767
            },
            "total_emi_amount": {
              "currency": "INR",
              "value": 258408
            },
            "interest_amount": {
              "currency": "INR",
              "value": 38508
            },
            "interest_rate_percentage": 16,
            "emi_type": "STANDARD"
          }
        }
      }
    }
  ]
}
'
```
```json Sample Response
{
  "data":{
    "order_id":"v1-250129053005-aa-imFYK2",
    "merchant_order_reference":"27bd048a-302f-4f3a-84ad-8c3de6bb2876",
    "type":"CHARGE",
    "status":"PENDING",
    "challenge_url":"https://dnf6nfqyquvyr.cloudfront.net/debit-acs/?args=8vQdan5O8xdw%2FUwqnMM9Q0O%2BKw%2FxQsh6wHg3wX8WSYw%3D",
    "merchant_id":"122333",
    "order_amount":{
      "value":1200000,
      "currency":"INR"
    },
    "pre_auth":false,
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
    "purchase_details":{
      "customer":{
        "email_id":"kevin.bob@gmail.com",
        "first_name":"Kevin",
        "last_name":"Bob",
        "customer_id":"192212",
        "mobile_number":"9876543210",
        "country_code":"91",
        "billing_address":{
          
        },
        "shipping_address":{
          "address1":"H.No 15, Sector 17",
          "pincode":"160036",
          "city":"CHANDIGARH",
          "state":"PUNJAB",
          "country":"INDIA"
        },
        "is_edit_customer_details_allowed":false
      }
    },
    "payments":[
      {
        "id":"v1-250129053005-aa-imFYK2-de-a",
        "merchant_payment_reference":"b75ee911-6750-40c3-a2ba-378b288ccd92",
        "status":"PENDING",
        "payment_amount":{
          "value":1200000,
          "currency":"INR"
        },
        "payment_method":"DEBIT_EMI",
        "acquirer_data":{
          "approval_code":"",
          "acquirer_reference":"",
          "rrn":"",
          "is_aggregator":true
        },
        "offer_data":{
          "offer_details":{
            "id":"7",
            "name":"HDFC DC",
            "issuer_type":"DC_BANK",
            "priority":1,
            "tenure":{
              "tenure_id":"1",
              "name":"3 Months",
              "tenure_type":"MONTH",
              "tenure_value":3,
              "issuer_offer_parameters":[
                {
                  "program_type":"BANK_EMI",
                  "offer_id":"1562",
                  "offer_parameter_id":"63812"
                }
              ],
              "details":[
                
              ],
              "loan_amount":{
                "currency":"INR",
                "value":1200000
              },
              "net_payment_amount":{
                "currency":"INR",
                "value":1232142
              },
              "monthly_emi_amount":{
                "currency":"INR",
                "value":410714
              },
              "total_emi_amount":{
                "currency":"INR",
                "value":1232142
              },
              "interest_amount":{
                "currency":"INR",
                "value":32142
              },
              "interest_rate_percentage":16,
              "processing_fee_details":{
                "amount":{
                  "currency":"INR",
                  "value":19900
                }
              },
              "processing_fee_amount":{
                "currency":"INR",
                "value":19900
              },
              "emi_type":"STANDARD"
            }
          }
        },
        "created_at":"2025-01-29T05:30:13.738Z",
        "updated_at":"2025-01-29T05:30:25.917Z"
      }
    ],
    "created_at":"2025-01-29T05:30:05.738Z",
    "updated_at":"2025-01-29T05:30:25.918Z",
    "integration_mode":"SEAMLESS",
    "payment_retries_remaining":9
  }
}
```

#### **ICICI DEBIT EMI**

```curl cURL - UAT
curl --request POST \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/payments \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "payments": [
    {
      "merchant_payment_reference": "6000000060200000",
      "payment_method": "DEBIT_EMI",
      "payment_amount": {
        "value": 1200000,
        "currency": "INR"
      },
      "payment_option": {
        "card_details": {
          "card_number": "6000000060200000",
          "registered_mobile_number": "9876543210",
          "name": "Kevin Bob",
          "cvv": "123",
          "expiry_month": "12",
          "expiry_year": "2026"
        }
      },
      "offer_data": {
        "offer_details": {
          "id": "2",
          "name": "ICICI DC",
          "issuer_type": "DC_BANK",
          "priority": 1,
          "tenure": {
            "tenure_id": "12",
            "name": "36 Months",
            "tenure_type": "MONTH",
            "tenure_value": 36,
            "issuer_offer_parameters": [
              {
                "program_type": "BANK_EMI",
                "offer_id": "1562",
                "offer_parameter_id": "63812"
              }
            ],
            "details": [],
            "loan_amount": {
              "currency": "INR",
              "value": 1200000
            },
            "net_payment_amount": {
              "currency": "INR",
              "value": 1518768
            },
            "monthly_emi_amount": {
              "currency": "INR",
              "value": 42188
            },
            "total_emi_amount": {
              "currency": "INR",
              "value": 1518768
            },
            "interest_amount": {
              "currency": "INR",
              "value": 318768
            },
            "interest_rate_percentage": 16,
            "processing_fee_details": {
              "amount": {
                "currency": "INR",
                "value": 19900
              }
            },
            "emi_type": "STANDARD"
          }
        }
      }
    }
  ]
}
'
```
```curl cURL - PROD
curl --request POST \
     --url https://api.pluralpay.in/api/pay/v1/orders/{order_id}/payments \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "payments": [
    {
      "merchant_payment_reference": "6000000060200000",
      "payment_method": "DEBIT_EMI",
      "payment_amount": {
        "value": 1200000,
        "currency": "INR"
      },
      "payment_option": {
        "card_details": {
          "card_number": "6000000060200000",
          "registered_mobile_number": "9876543210",
          "name": "Kevin Bob",
          "cvv": "123",
          "expiry_month": "12",
          "expiry_year": "2026"
        }
      },
      "offer_data": {
        "offer_details": {
          "id": "2",
          "name": "ICICI DC",
          "issuer_type": "DC_BANK",
          "priority": 1,
          "tenure": {
            "tenure_id": "12",
            "name": "36 Months",
            "tenure_type": "MONTH",
            "tenure_value": 36,
            "issuer_offer_parameters": [
              {
                "program_type": "BANK_EMI",
                "offer_id": "1562",
                "offer_parameter_id": "63812"
              }
            ],
            "details": [],
            "loan_amount": {
              "currency": "INR",
              "value": 1200000
            },
            "net_payment_amount": {
              "currency": "INR",
              "value": 1518768
            },
            "monthly_emi_amount": {
              "currency": "INR",
              "value": 42188
            },
            "total_emi_amount": {
              "currency": "INR",
              "value": 1518768
            },
            "interest_amount": {
              "currency": "INR",
              "value": 318768
            },
            "interest_rate_percentage": 16,
            "processing_fee_details": {
              "amount": {
                "currency": "INR",
                "value": 19900
              }
            },
            "emi_type": "STANDARD"
          }
        }
      }
    }
  ]
}
'
```
```json Sample Response
{
  "data":{
    "order_id":"v1-250129063239-aa-SytJOT",
    "merchant_order_reference":"2ec9bf09-4c52-4625-a737-abb69826cd93",
    "type":"CHARGE",
    "status":"PENDING",
    "challenge_url":"https://pluraldev.v2.pinepg.in/web/auth/landing/?token=S50QPKm4BXDi4E77gduxkDTtMZWLyBGgTmbTfL0ybpNtm6guh%2FsdActrAGM%2FW3NzUW4",
    "merchant_id":"122333",
    "order_amount":{
      "value":1200000,
      "currency":"INR"
    },
    "pre_auth":false,
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
    "purchase_details":{
      "customer":{
        "email_id":"kevin.bob@gmail.com",
        "first_name":"Kevin",
        "last_name":"Bob",
        "mobile_number":"9876543210",
        "country_code":"91",
        "billing_address":{
          
        },
        "shipping_address":{
          "address1":"H.No 15, Sector 17",
          "pincode":"160036",
          "city":"CHANDIGARH",
          "state":"PUNJAB",
          "country":"INDIA"
        },
        "is_edit_customer_details_allowed":false
      }
    },
    "payments":[
      {
        "id":"v1-250129063239-aa-SytJOT-de-a",
        "merchant_payment_reference":"63466860-0772-410a-a6c5-5ff6581eb264",
        "status":"PENDING",
        "payment_amount":{
          "value":1200000,
          "currency":"INR"
        },
        "payment_method":"DEBIT_EMI",
        "acquirer_data":{
          "approval_code":"",
          "acquirer_reference":"",
          "rrn":"",
          "is_aggregator":true
        },
        "offer_data":{
          "offer_details":{
            "id":"2",
            "name":"ICICI DC",
            "issuer_type":"DC_BANK",
            "priority":1,
            "tenure":{
              "tenure_id":"12",
              "name":"36 Months",
              "tenure_type":"MONTH",
              "tenure_value":36,
              "issuer_offer_parameters":[
                {
                  "program_type":"BANK_EMI",
                  "offer_id":"1562",
                  "offer_parameter_id":"63812"
                }
              ],
              "details":[
                
              ],
              "loan_amount":{
                "currency":"INR",
                "value":1200000
              },
              "net_payment_amount":{
                "currency":"INR",
                "value":1518768
              },
              "monthly_emi_amount":{
                "currency":"INR",
                "value":42188
              },
              "total_emi_amount":{
                "currency":"INR",
                "value":1518768
              },
              "interest_amount":{
                "currency":"INR",
                "value":318768
              },
              "interest_rate_percentage":16,
              "processing_fee_details":{
                "amount":{
                  "currency":"INR",
                  "value":19900
                }
              },
              "processing_fee_amount":{
                "currency":"INR",
                "value":19900
              },
              "emi_type":"STANDARD"
            }
          }
        },
        "created_at":"2025-01-29T06:32:54.668Z",
        "updated_at":"2025-01-29T06:33:07.191Z"
      }
    ],
    "created_at":"2025-01-29T06:32:39.043Z",
    "updated_at":"2025-01-29T06:33:07.191Z",
    "integration_mode":"SEAMLESS",
    "payment_retries_remaining":9
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/reference/affordability-suite-create-payment" target="_blank">Create Payment API</a> documentation to learn more.

## 6. Handle Payment

In create payment API response we return a `challenge_url`, use this challenge url to navigate your customers to the checkout page to accept payment.

> 📘 Note:
> 
> - On successful payment we send the webhook event `ORDER_AUTHORIZED` and the status of the payment is updated to `authorized`.
> - You can capture or cancel an order only when the order status is `authorized`.

### 6.1 Store Payment Details on Your Server

On a successful and failed payment we return the following fields to the return url.

- We recommend you to store the payment details on your server.
- You must validate the authenticity of the payment details returned. You can authenticate by verifying the signature.

```json Success Callback Response
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "status": "AUTHORIZED",
  "signature": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
}
```
```json Failure Callbak Response
{
  "order_id": "v1-4405071524-aa-qlAtAf",
  "status": "AUTHORIZED",
  "error_code": "USER_AUTHENTICATION_REQUIRED",
  "error_message": "Consumer Authentication Required",
  "signature": "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
}
```

### 6.2 Verify Payment Signature

Ensure you follow this as a mandatory step to verify the authenticity of the details returned to the checkout form for successful payments.

Follow the below steps to verify the signature.

1. Create a signature on your server using the following parameters using the SHA256 algorithm.
   1. `order_id`: Unique Identifier generated for an order request on Plural database.
   2. `payment_status`: Payment status.
   3. `error_code`: Short code for the error returned.
   4. `error_message`: Corresponding error message for the code.
   5. `secret_key`: The Onboarding team has provided you with this information as part of the onboarding process.

Use the below sample code to construct HashMap signature using the SHA256 algorithm.

```java Java
import java.io.UnsupportedEncodingException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
 
public class hash {
    public static void main(String[] args) {
        // Test the GenerateHash method
        String input = "<string>";
        String secretKey = "<secret_key>";  // Example key in hex
 
        String hash = GenerateHash(input, secretKey);
        System.out.println("Generated Hash: " + hash);
    }
    public static String GenerateHash(String input, String strSecretKey) {
        String strHash = "";
        try {
            if (!isValidString(input) || !isValidString(strSecretKey)) {
                return strHash;
            }
            byte[] convertedHashKey = new byte[strSecretKey.length() / 2];
 
            for (int i = 0; i < strSecretKey.length() / 2; i++) {
                convertedHashKey[i] =
                        (byte)Integer.parseInt(strSecretKey.substring(i * 2, (i*2)+2),16); //hexNumber radix
            }
            strHash = hmacDigest(input.toString(), convertedHashKey,
                    "HmacSHA256");
        } catch (Exception ex) {
            strHash = "";
        }
        return strHash.toUpperCase();
    }
    private static String hmacDigest(String msg, byte[] keyString, String algo) {
        String digest = null;
        try {
            SecretKeySpec key = new SecretKeySpec(keyString, algo);
            Mac mac = Mac.getInstance(algo);
            mac.init(key);
            byte[] bytes = mac.doFinal(msg.getBytes("UTF-8"));
            StringBuffer hash = new StringBuffer();
            for (int i = 0; i < bytes.length; i++) {
                String hex = Integer.toHexString(0xFF & bytes[i]);
                if (hex.length() == 1) {
                    hash.append('0');
                }
                hash.append(hex);
            }
            digest = hash.toString();
        } catch (UnsupportedEncodingException e) {
// logger.error("Exception occured in hashing the pine payment gateway request"+e);
        } catch (InvalidKeyException e) {
// logger.error("Exception occured in hashing the pine payment gateway request"+e);
        } catch (NoSuchAlgorithmException e) {
// logger.error("Exception occured in hashing the pine payment gateway request"+e);
        }
        return digest;
    }
    public static boolean isValidString(String str){
        if(str != null && !"".equals(str.trim())){
            return true;
        }
        return false;
    }
}
```

> 📘 Note:
> 
> To create a request string, format the key-value pairs of data returned to the return URL. The pairs are separated by `&` and arranged in ascending order based on a lexicographical comparison of the keys.

Shown below is a example to create a request string.

```text Success
"key1=value1&key2=value2", ["order_id=random_order_id&status=AUTHORIZED"]
```
```text Failed
"key1=value1&key2=value2&key3=value3&key4=value4", ["error_code=USER_AUTHENTICATION_FAILED&error_message=Consumer Authentication required&order_id=<order_id>&status=FAILED"]
```

2. If the signature generated on your server matches the Plural signature returned in the return URL, it confirms that the payment details are from Plural.
3. Capture the status returned on your database. Once the payment status is `AUTHORIZED` you can either capture or cancel an order.

## 7. Get Order by Order ID

Use this API to retrieve the order by order ID.

Use the below endpoint to capture the payment against the order.

```text Get Order by Order ID Endpoint for UAT
GET: https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}
```
```text Get Order by Order ID Endpoint for PROD
GET: https://api.pluralpay.in/api/pay/v1/orders/{order_id}
```

Shown below is a sample request and sample response for a Get Order by Order ID API.

```json Sample Response
{
  "data":{
    "order_id":"v1-250129053005-aa-imFYK2",
    "merchant_order_reference":"27bd048a-302f-4f3a-84ad-8c3de6bb2876",
    "type":"CHARGE",
    "status":"PENDING",
    "challenge_url":"https://dnf6nfqyquvyr.cloudfront.net/debit-acs/?args=8vQdan5O8xdw%2FUwqnMM9Q0O%2BKw%2FxQsh6wHg3wX8WSYw%3D",
    "merchant_id":"122333",
    "order_amount":{
      "value":1200000,
      "currency":"INR"
    },
    "pre_auth":false,
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
    "purchase_details":{
      "customer":{
        "email_id":"kevin.bob@gmail.com",
        "first_name":"Kevin",
        "last_name":"Bob",
        "customer_id":"192212",
        "mobile_number":"9876543210",
        "country_code":"91",
        "billing_address":{
          
        },
        "shipping_address":{
          "address1":"H.No 15, Sector 17",
          "pincode":"160036",
          "city":"CHANDIGARH",
          "state":"PUNJAB",
          "country":"INDIA"
        },
        "is_edit_customer_details_allowed":false
      }
    },
    "payments":[
      {
        "id":"v1-250129053005-aa-imFYK2-de-a",
        "merchant_payment_reference":"b75ee911-6750-40c3-a2ba-378b288ccd92",
        "status":"PENDING",
        "payment_amount":{
          "value":1200000,
          "currency":"INR"
        },
        "payment_method":"DEBIT_EMI",
        "acquirer_data":{
          "approval_code":"",
          "acquirer_reference":"",
          "rrn":"",
          "is_aggregator":true
        },
        "offer_data":{
          "offer_details":{
            "id":"7",
            "name":"HDFC DC",
            "issuer_type":"DC_BANK",
            "priority":1,
            "tenure":{
              "tenure_id":"1",
              "name":"3 Months",
              "tenure_type":"MONTH",
              "tenure_value":3,
              "issuer_offer_parameters":[
                {
                  "program_type":"BANK_EMI",
                  "offer_id":"1562",
                  "offer_parameter_id":"63812"
                }
              ],
              "details":[
                
              ],
              "loan_amount":{
                "currency":"INR",
                "value":1200000
              },
              "net_payment_amount":{
                "currency":"INR",
                "value":1232142
              },
              "monthly_emi_amount":{
                "currency":"INR",
                "value":410714
              },
              "total_emi_amount":{
                "currency":"INR",
                "value":1232142
              },
              "interest_amount":{
                "currency":"INR",
                "value":32142
              },
              "interest_rate_percentage":16,
              "processing_fee_details":{
                "amount":{
                  "currency":"INR",
                  "value":19900
                }
              },
              "processing_fee_amount":{
                "currency":"INR",
                "value":19900
              },
              "emi_type":"STANDARD"
            }
          }
        },
        "created_at":"2025-01-29T05:30:13.738Z",
        "updated_at":"2025-01-29T05:30:25.917Z"
      }
    ],
    "created_at":"2025-01-29T05:30:05.738Z",
    "updated_at":"2025-01-29T05:30:25.918Z",
    "integration_mode":"SEAMLESS",
    "payment_retries_remaining":9
  }
}
```

Refer to our <a style="text-decoration:none;" href="https://developer.pluralonline.com/reference/orders-get-by-order-id" target="_blank">Get Order by Order ID API</a> documentation to learn more.

## To Know Your Payment Status

To check your payment status, you can either rely on Webhook events or use our **Get Orders** APIs for real-time updates.

1. **Webhook Notification**: We send Webhook notifications on the successful payment or any changes to the payments object. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/reference/developer-tools-webhook" target="_blank">Webhooks</a> documentation to learn more.
2. **Get Orders API**: Use our Get Orders API to know the real time status of the payment. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/order-manage#3-get-order-by-order-id" target="_blank">Manage Orders</a> documentation to learn more.
3. **Refunds**: Plural processes refund directly to the customer's original payment method to prevent chargebacks. Refer to our <a style="text-decoration:underline;" href="https://developer.pluralonline.com/docs/payment-refund" target="_blank">Refunds</a> documentation to learn more.

## Pre Authorization Flow - Credit EMI

Our Orders API includes an optional **pre-authorization** feature. When pre-authorization is enabled (`pre_auth` = true), you can capture payment for an order after successful delivery, ensuring that settlement remains on hold until then.

Once pre-authorization is enabled and the payment is successfully processed, you have the following options:

**Capture Order**: Utilize the plural capture order API in your backend to capture the payment against an order.

**Cancel Order**: Use the plural cancel order API in your backend to cancel the payment against an order.

> 📘 Note:
> 
> - On successful payment we send the webhook event `ORDER_AUTHORIZED` and the status of the payment is updated to `authorized`.
> - You can capture or cancel an order only when the order status is `authorized`.

### 1. Capture Order

Use this API to capture the payment against an order. On successful capture of an order the order status is updated as `processed`.

Shown below are the sample requests and sample response for a Capture Order API.

```curl cURL - UAT
curl --request PUT \
     --url https://pluraluat.v2.pinepg.in/api/pay/v1/orders/order_id/capture \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_capture_reference": "merchant-capture-ref-r4y",
  "capture_amount": {
    "value": 4000,
    "currency": "INR"
  }
}
'
```
```curl cURL - PROD
curl --request PUT \
     --url https://api.pluralpay.in/api/pay/v1/orders/order_id/capture \
     --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' \
     --header 'Content-Type: application/json' \
     --header 'Request-ID: c17ce30f-f88e-4f81-ada1-c3b4909ed235' \
     --header 'Request-Timestamp: 2024-07-09T07:57:08.022Z' \
     --header 'accept: application/json' \
     --data '
{
  "merchant_capture_reference": "merchant-capture-ref-r4y",
  "capture_amount": {
    "value": 4000,
    "currency": "INR"
  }
}
'
```
```json Sample Response
{
  "data":{
    "order_id":"v1-5757575757-aa-hU1rUd",
    "merchant_order_reference":"f4548bbf-a029-43d3-9209-e3385c80b1e9",
    "type":"CHARGE",
    "status":"PROCESSED",
    "merchant_id":"123456",
    "order_amount":{
      "value":1100,
      "currency":"INR"
    },
    "pre_auth":true,
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
    "notes":"order1",
    "purchase_details":{
      "customer":{
        "email_id":"kevin.bob@example.com",
        "first_name":"Kevin",
        "last_name":"Bob",
        "customer_id":"232323",
        "mobile_number":"9876543210",
        "billing_address":{
          "address1":"H.No 15, Sector 17",
          "address2":"",
          "address3":"",
          "pincode":"61232112",
          "city":"CHANDIGARH",
          "state":"PUNJAB",
          "country":"INDIA"
        },
        "shipping_address":{
          "address1":"H.No 15, Sector 17",
          "address2":"string",
          "address3":"string",
          "pincode":"144001123",
          "city":"CHANDIGARH",
          "state":"PUNJAB",
          "country":"INDIA"
        }
      },
      "merchant_metadata":{
        "key1":"DD",
        "key2":"XOF"
      }
    },
    "payments":[
      {
        "id":"v1-1111071924-aa-zzSkOA-cc-G",
        "status":"PROCESSED",
        "payment_amount":{
          "value":1100,
          "currency":"INR"
        },
        "payment_method":"CARD",
        "payment_option":{
          "card_data":{
            "card_type":"CREDIT",
            "network_name":"VISA",
            "issuer_name":"NONE",
            "card_category":"CONSUMER",
            "country_code":"IND",
            "token_txn_type":"ALT_TOKEN"
          }
        },
        "acquirer_data":{
          "approval_code":"000000",
          "acquirer_reference":"202456643801053",
          "rrn":"420145000226"
        },
        "capture_data":[
          {
            "merchant_capture_reference":"f31d8c60-0dc8-4788-a577-5ced930cc175",
            "capture_amount":{
              "value":1100,
              "currency":"INR"
            },
            "created_at":"2024-07-19T11:13:21.523Z"
          }
        ],
        "created_at":"2024-07-19T11:11:48.944Z",
        "updated_at":"2024-07-19T11:13:23.962Z"
      }
    ],
    "created_at":"2024-07-19T11:11:48.944Z",
    "updated_at":"2024-07-19T11:13:23.962Z"
  }
}
```

Refer to our <a style="text-decoration:none;" href="https://developer.pluralonline.com/v3.0/reference/orders-capture" target="_blank">Capture Order API</a> documentation to learn more.

### 2. Cancel Order

Use this API to cancel the payment against an order.

Use the below endpoint to cancel the payment against the order.

```text Cancel Order Endpoint for UAT
PUT: https://pluraluat.v2.pinepg.in/api/pay/v1/orders/{order_id}/cancel
```
```text Cancel Order Endpoint for PROD
PUT: https://api.pluralpay.in/api/pay/v1/orders/{order_id}/cancel
```

Shown below is a sample request and sample response for a Cancel Order API.

```json Sample Response
{
  "data":{
    "order_id":"v1-250129053005-aa-imFYK2",
    "merchant_order_reference":"27bd048a-302f-4f3a-84ad-8c3de6bb2876",
    "type":"CHARGE",
    "status":"CANCELLED",
    "challenge_url":"https://dnf6nfqyquvyr.cloudfront.net/debit-acs/?args=8vQdan5O8xdw%2FUwqnMM9Q0O%2BKw%2FxQsh6wHg3wX8WSYw%3D",
    "merchant_id":"122333",
    "order_amount":{
      "value":1200000,
      "currency":"INR"
    },
    "pre_auth":false,
    "callback_url":"https://sample-callback-url",
    "failure_callback_url": "https://sample-failure-callback-url",
    "allowed_payment_methods":[
      "CARD",
      "UPI",
      "NETBANKING",
      "POINTS",
      "WALLET"
    ],
    "purchase_details":{
      "customer":{
        "email_id":"kevin.bob@gmail.com",
        "first_name":"Kevin",
        "last_name":"Bob",
        "customer_id":"192212",
        "mobile_number":"9876543210",
        "country_code":"91",
        "billing_address":{
          
        },
        "shipping_address":{
          "address1":"H.No 15, Sector 17",
          "pincode":"160036",
          "city":"CHANDIGARH",
          "state":"PUNJAB",
          "country":"INDIA"
        },
        "is_edit_customer_details_allowed":false
      }
    },
    "payments":[
      {
        "id":"v1-250129053005-aa-imFYK2-de-a",
        "merchant_payment_reference":"b75ee911-6750-40c3-a2ba-378b288ccd92",
        "status":"PENDING",
        "payment_amount":{
          "value":1200000,
          "currency":"INR"
        },
        "payment_method":"DEBIT_EMI",
        "acquirer_data":{
          "approval_code":"",
          "acquirer_reference":"",
          "rrn":"",
          "is_aggregator":true
        },
        "offer_data":{
          "offer_details":{
            "id":"7",
            "name":"HDFC DC",
            "issuer_type":"DC_BANK",
            "priority":1,
            "tenure":{
              "tenure_id":"1",
              "name":"3 Months",
              "tenure_type":"MONTH",
              "tenure_value":3,
              "issuer_offer_parameters":[
                {
                  "program_type":"BANK_EMI",
                  "offer_id":"1562",
                  "offer_parameter_id":"63812"
                }
              ],
              "details":[
                
              ],
              "loan_amount":{
                "currency":"INR",
                "value":1200000
              },
              "net_payment_amount":{
                "currency":"INR",
                "value":1232142
              },
              "monthly_emi_amount":{
                "currency":"INR",
                "value":410714
              },
              "total_emi_amount":{
                "currency":"INR",
                "value":1232142
              },
              "interest_amount":{
                "currency":"INR",
                "value":32142
              },
              "interest_rate_percentage":16,
              "processing_fee_details":{
                "amount":{
                  "currency":"INR",
                  "value":19900
                }
              },
              "processing_fee_amount":{
                "currency":"INR",
                "value":19900
              },
              "emi_type":"STANDARD"
            }
          }
        },
        "created_at":"2025-01-29T05:30:13.738Z",
        "updated_at":"2025-01-29T05:30:25.917Z"
      }
    ],
    "created_at":"2025-01-29T05:30:05.738Z",
    "updated_at":"2025-01-29T05:30:25.918Z",
    "integration_mode":"SEAMLESS",
    "payment_retries_remaining":9
  }
}
```

Refer to our <a style="text-decoration:none" href="https://developer.pluralonline.com/v3.0/reference/orders-cancel" target="_blank">Cancel Order API</a> documentation to learn more.
