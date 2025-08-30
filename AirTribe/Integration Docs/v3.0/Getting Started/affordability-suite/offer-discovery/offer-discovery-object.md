---
title: "Object"
slug: "offer-discovery-object"
excerpt: "Overview of the Offer Discovery API response object."
hidden: false
createdAt: "Tue Jan 21 2025 13:59:23 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Apr 09 2025 09:59:58 GMT+0000 (Coordinated Universal Time)"
---
Shown below is a sample response returned through our Offer Discovery API.

```json Offer Discovery_Bank EMI
{
  "issuers": [
    {
      "id": "23",
      "name": "INDUSIND CC",
      "display_name": "INDUSIND",
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
      "issuer_data": {
        "otp_length": 5,
        "otp_time_in_sec": 180,
        "otp_retry_count": 5,
        "is_consent_page_required": true,
        "consent_data": "<div classname=concent-container><div classname=concentTitle>Consent Clause :</div><div classname=concentSection><div classname=concentText>I/We hereby expressly authorize and give consent to ICICI Bank to, disclose, transfer or part with any of my/our information, (including location), or any other device information when ICICI Bank considers such disclosure as necessary, with:{' '}</div></div><div classname=concentSection><div classname=concentText>A. Agents of ICICI Bank, ICICI Bank's group entities/in any jurisdiction;</div><div classname=concentText>B. Auditors, credit rating agencies/credit bureaus, statutory/regulatory authorities, governmental/administrative authorities, Central Know Your Customer (CKYC) registry or SEBI Know Your Client registration agency, having jurisdiction over ICICI Bank or its group entities;{' '}</div><div classname=concentText>{' '} C. Service providers, or such person with whom ICICI Bank contracts or proposes to contract; (Collectively referred to as “Permitted Persons”){' '}</div></div><div classname=concentSection><div classname=concentText>For the purposes of:</div><div classname=concentText>1. Provision of the facility and completion of on-boarding formalities; or{' '}</div><div classname=concentText>2. Complying with KYC requirements; or{' '}</div><div classname=concentText>{' '} 3. Compliance with applicable laws or any order (judicial or otherwise), statutory/regulatory requirement; or{' '}</div><div classname=concentText>{' '} 4. For credit review of facilities availed; or{' '}</div><div classname=concentText>5. Authentication or verification; or{' '}</div><div classname=concentText>6. Research or analysis, credit reporting & scoring, risk management, participation in any telecommunication; or{' '}</div><div classname=concentText>7. Electronic clearing network and for use or processing of the said information/data.{' '}</div><div classname=concentText>{' '} 8. Disclosing any default in payment, for the purposes of recovering such amounts.{' '}</div></div><div classname=concentText>D. For detailed Privacy Policy of the ICICI bank, please visit{' '} <a classname=concent-doc-link href=https://www.icicibank.com/privacy.page rel=noreferrer target=_blank><u>https://www.icicibank.com/privacy.page</u></a></div></div>",
        "terms_and_conditions": "Sample TNC",
        "show_key_fact_statement": true,
        "auth_type": "PENNY_DROP",
        "penny_transaction_amount": {
          "currency": "INR",
          "value": 100
        },
        "is_tokenized_transaction_supported": false
      }
    }
  ]
}
```
```json Offer Discovery_Brand EMI
{
  "issuers": [
    {
      "id": "19",
      "name": "KOTAK DC",
      "display_name": "KOTAK BANK",
      "issuer_type": "DC_BANK",
      "priority": 1,
      "tenures": [
        {
          "tenure_id": "7",
          "name": "No EMI Only Cashback",
          "tenure_type": "MONTH",
          "tenure_value": 0,
          "issuer_offer_parameters": [
            {
              "program_type": "BANK_EMI",
              "offer_id": "308",
              "offer_parameter_id": "19"
            },
            {
              "program_type": "MERCHANT_BANK_OFFER",
              "offer_id": "3491",
              "offer_parameter_id": "199672"
            }
          ],
          "details": [
            {
              "product_code": "redmi_1",
              "product_display_name": "Redmi Note 14 5G",
              "brand_name": "Xiaomi",
              "product_amount": {
                "currency": "INR",
                "value": 219900
              },
              "interest_rate": 0,
              "discount": {
                "discount_type": "DEFERRED",
                "discount_string": "You are eligible for a cashback of 10.0% upto Rs. 200, will be posted within 90 days. T&C applied.",
                "percentage": 10,
                "amount": {
                  "currency": "INR",
                  "value": 200
                },
                "max_amount": {
                  "currency": "INR",
                  "value": 200
                },
                "discount_deferred_duration_value": 90,
                "discount_deferred_duration_type": "DAY"
              }
            }
          ],
          "discount": {
            "discount_type": "DEFERRED",
            "discount_string": "You are eligible for a cashback of 10.0% upto Rs. 200, will be posted within 90 days. T&C applied.",
            "percentage": 10,
            "amount": {
              "currency": "INR",
              "value": 200
            },
            "max_amount": {
              "currency": "INR",
              "value": 200
            },
            "discount_deferred_duration_value": 90,
            "discount_deferred_duration_type": "DAY"
          },
          "loan_amount": {
            "currency": "INR",
            "value": 219900
          },
          "total_discount_amount": {
            "currency": "INR",
            "value": 200
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 219700
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 219900
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 219900
          },
          "interest_rate_percentage": 0,
          "processing_fee_details": {
            "percentage": 0,
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
              "offer_id": "308",
              "offer_parameter_id": "19"
            }
          ],
          "details": [
            {
              "product_code": "redmi_1",
              "product_display_name": "Redmi Note 14 5G",
              "brand_name": "Xiaomi",
              "product_amount": {
                "currency": "INR",
                "value": 219900
              },
              "interest_amount": {
                "currency": "INR",
                "value": 34548
              },
              "interest_rate": 19
            }
          ],
          "loan_amount": {
            "currency": "INR",
            "value": 219900
          },
          "net_payment_amount": {
            "currency": "INR",
            "value": 254448
          },
          "monthly_emi_amount": {
            "currency": "INR",
            "value": 14136
          },
          "total_emi_amount": {
            "currency": "INR",
            "value": 254448
          },
          "interest_amount": {
            "currency": "INR",
            "value": 34548
          },
          "interest_rate_percentage": 19,
          "processing_fee_details": {
            "percentage": 0,
            "amount": {
              "currency": "INR",
              "value": 19900
            }
          },
          "emi_type": "STANDARD"
        }
      ],
      "issuer_data": {
        "otp_length": 6,
        "otp_time_in_sec": 30,
        "otp_retry_count": 3,
        "is_consent_page_required": false,
        "consent_data": "Sample Consent",
        "terms_and_conditions": "Sample TNC",
        "show_key_fact_statement": true,
        "auth_type": "OTP",
        "is_tokenized_transaction_supported": false
      }
    }
  ]
}
```

The table below lists the various parameters returned in the offer discovery response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "id",
    "0-1": "`String`",
    "0-2": "Unique identifier of the issuer id in the Plural database.  \n  \nExample: `23`",
    "1-0": "name",
    "1-1": "`String`",
    "1-2": "Name of the Issuer.  \n  \nExample: `INDUSIND CC`",
    "2-0": "display_name",
    "2-1": "`string`",
    "2-2": "Name of the issuer offering the offer.  \n  \nExample: `INDUSIND`",
    "3-0": "issuer_type",
    "3-1": "`String`",
    "3-2": "The type of the Issuer offering the offer.  \n  \nAccepted values: <ul><li>`CC_BANK`</li><li>`DC_BANK`</ul></li>.",
    "4-0": "priority",
    "4-1": "`integer`",
    "4-2": "The priority of the issuer providing the offer.  \n  \nExample: `1`",
    "5-0": "tenures",
    "5-1": "`array of objects`",
    "5-2": "An array of objects that contains the tenures details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#tenures-child-object\" >Learn more about the `tenures` child object.</a>",
    "6-0": "issuer_data",
    "6-1": "`objects`",
    "6-2": "An object that contains the issuer data details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#issuer-data\" >Learn more about the `issuer_data` child object.</a>"
  },
  "cols": 3,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Tenures [Child Object]

The table below lists the various parameters in the `tenures` object. This is part of the offer discovery response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "tenure_id",
    "0-1": "`String`",
    "0-2": "Tenure id in the Plural database.  \n  \nExample: `1`",
    "1-0": "name",
    "1-1": "`String`",
    "1-2": "The name of the Issuer offering the offer..  \n  \nExample: `3 Months`",
    "2-0": "tenure_type",
    "2-1": "`String`",
    "2-2": "The type of the Tenure.  \n  \nAccepted values: <ul><li>`MONTH`</ul></li>.",
    "3-0": "tenure_value",
    "3-1": "`integer`",
    "3-2": "The value of the tenure.  \n  \nExample: `3`",
    "4-0": "issuer_offer_parameters",
    "4-1": "`array of objects`",
    "4-2": "An array of objects that contains the `issuer_offer_parameters` details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#issuer-offer-parameters-child-object\" >Learn more about the `issuer_offer_parameters` child object.</a>",
    "5-0": "details",
    "5-1": "`array of objects`",
    "5-2": "An array of objects that contains the `product details`.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#details-child-object\" >Learn more about the `details` child object.</a>",
    "6-0": "discount",
    "6-1": "`object`",
    "6-2": "An object that contains the discount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#discount-child-object\" >Learn more about the `discount` child object.</a>",
    "7-0": "loan_amount",
    "7-1": "`object`",
    "7-2": "An object that contains the loan amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#loan-amount-child-object\" >Learn more about the `loan_amount` child object.</a>",
    "8-0": "total_discount_amount",
    "8-1": "`object`",
    "8-2": "An object that contains the total discount amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#total-discount-amount-child-object\" >Learn more about the `total_discount_amount` child object.</a>",
    "9-0": "net_payment_amount",
    "9-1": "`object`",
    "9-2": "An object that contains the net payment amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#net-payment-amount-child-object\" >Learn more about the `net_payment_amount` child object.</a>",
    "10-0": "monthly_emi_amount",
    "10-1": "`object`",
    "10-2": "An object that contains the monthly EMI amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#monthly-emi-amount-child-object\" >Learn more about the `monthly_emi_amount` child object.</a>",
    "11-0": "total_emi_amount",
    "11-1": "`object`",
    "11-2": "An object that contains the total EMI amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#total-emi-amount-child-object\" >Learn more about the `total_emi_amount` child object.</a>",
    "12-0": "interest_amount",
    "12-1": "`object`",
    "12-2": "An object that contains the interest amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#interest-amount-child-object\" >Learn more about the `interest_amount` child object.</a>",
    "13-0": "total_subvention_amount",
    "13-1": "`object`",
    "13-2": "An object that contains the total subvention amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#total-subvention-amount-child-object\" >Learn more about the `total_subvention_amount` child object.</a>",
    "14-0": "interest_rate_percentage",
    "14-1": "`float`",
    "14-2": "Interest rate percentage for the tenure.  \n  \nExample: `16.90`",
    "15-0": "processing_fee_details",
    "15-1": "`object`",
    "15-2": "An object that contains the processing fee details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#processing-fee-details-child-object\" >Learn more about the `processing_fee_details` child object.</a>",
    "16-0": "convenience_fee_breakdown",
    "16-1": "`object`",
    "16-2": "An object that contains the convenience fee breakdown details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#convenience-fee-breakdown-child-object\" >Learn more about our `convenience_fee_breakdown` child object.</a>",
    "17-0": "cart_coupon_discount_amount",
    "17-1": "`object`",
    "17-2": "An object that contains the cart coupon discount amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#cart-coupon-discount-amount-child-object\" >Learn more about our `cart_coupon_discount_amount` child object.</a>",
    "18-0": "total_coupon_discount",
    "18-1": "`object`",
    "18-2": "An object that contains the total coupon discount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#total-coupon-discount-child-object\" >Learn more about our `total_coupon_discount` child object.</a>",
    "19-0": "emi_type",
    "19-1": "`strings`",
    "19-2": "Type of EMI.  \n  \nExample: `STANDARD`  \n  \nAccepted values: <ul><li>`LOW_COST`</li><li>`NO_COST`</li><li>`STANDARD`</ul></li>"
  },
  "cols": 3,
  "rows": 20,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Issuer Offer Parameters [Child Object]

The table below lists the various parameters in the `issuer_offer_parameters` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "program_type",
    "0-1": "`String`",
    "0-2": "Unique identifier of the issuer id in the Plural database.  \n  \nExample: `23`",
    "1-0": "offer_id",
    "1-1": "`String`",
    "1-2": "Name of the Issuer.  \n  \nExample: `INDUSIND CC`",
    "2-0": "offer_parameter_id",
    "2-1": "`String`",
    "2-2": "The type of the Issuer offering the offer.  \n  \nAccepted values: <ul><li>`Credit`</li><li>`Debit`</li><li>`Cardless`</li><li>`NBFC`</ul></li>."
  },
  "cols": 3,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Details [Child Object]

The table below lists the various parameters in the `details` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "product_code",
    "0-1": "`String`",
    "0-2": "Unique Product identifier of the product.  \n  \nExample: `redmi_1`",
    "1-0": "product_display_name",
    "1-1": "`string`",
    "1-2": "Name of the Product.  \n  \nExample: `Oneplus 13R`",
    "2-0": "brand_id",
    "2-1": "`String`",
    "2-2": "Unique brand identifier of the product.  \n  \nExample: `3`",
    "3-0": "product_offer_parameters",
    "3-1": "`array of objects`",
    "3-2": "An array of objects that contains the product offer schemes for the product EMI details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#product-offer-parameters-child-object\" >Learn more about the `product_offer_parameters` child object.</a>",
    "4-0": "product_amount",
    "4-1": "`object`",
    "4-2": "An object that contains the product amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#product-amount-child-object\" >Learn more about the `product_amount` child object.</a>",
    "5-0": "product_coupon_discount_amount",
    "5-1": "`object`",
    "5-2": "An object that contains the product coupon discount amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#product-coupon-discount-amount-child-object\" >Learn more about the `product_coupon_discount_amount` child object.</a>",
    "6-0": "subvention",
    "6-1": "`object`",
    "6-2": "An object that contains the subvention details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#subvention-child-object\" >Learn more about the `subvention` child object.</a>",
    "7-0": "discount",
    "7-1": "`object`",
    "7-2": "An object that contains the product discount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#discount-child-object\" >Learn more about the `discount` child object.</a>",
    "8-0": "brand_name",
    "8-1": "`string`",
    "8-2": "Name of the Brand.  \n  \nExample: `Oneplus`",
    "9-0": "interest_amount",
    "9-1": "`object`",
    "9-2": "An object that contains the interest amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#interest-amount-child-object\" >Learn more about the `interest_amount` child object.</a>",
    "10-0": "interest_rate",
    "10-1": "`double`",
    "10-2": "Rate of interest applied on the product.  \n  \nExample: `2`",
    "11-0": "cart_coupon_discount_product_share",
    "11-1": "`object`",
    "11-2": "An object that contains the cart coupon discount product share details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#cart-coupon-discount-product-share-child-object\" >Learn more about the `cart_coupon_discount_product_share` child object.</a>"
  },
  "cols": 3,
  "rows": 12,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Product Offer Parameters [Child Object]

The table below lists the various parameters in the `product_offer_parameters` child object. This is part of the `details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "program_type",
    "0-1": "`String`",
    "0-2": "Type of the Program.  \n  \nExample: `BRAND_EMI`  \n  \nAccepted values: <ul><li>`BRAND_EMI`</li><li>`BANK_EMI`</li><li>`MERCHANT_BRAND_OFFER`</li><li>`MERCHANT_BANK_OFFER`</li><li>`BRAND_OFFER`</li><li>`MY_EMI`</ul></li>",
    "1-0": "offer_id",
    "1-1": "`string`",
    "1-2": "Unique identifier of the offer.  \n  \nExample: `309`",
    "2-0": "offer_parameter_id",
    "2-1": "`string`",
    "2-2": "Unique offer parameter identifier.  \n  \nExample: `20` "
  },
  "cols": 3,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Product Amount [Child Object]

The table below lists the various parameters in the `product_amount` child object. This is part of the `details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Product Coupon Discount Amount [Child Object]

The table below lists the various parameters in the `product_coupon_discount_amount` child object. This is part of the `details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Subvention [Child Object]

The table below lists the various parameters in the `subvention` child object. This is part of the `details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "subvention_type",
    "0-1": "`String`",
    "0-2": "Type of subvention.  \n  \nExample: `INSTANT`  \n  \nAccepted values:<ul><li>`INSTANT`</li><li>`POST`</ul></li>",
    "1-0": "offer_type",
    "1-1": "`string`",
    "1-2": "Type of the offer.  \n  \nAccepted values: <ul><li>`LOW_COST`</li><li>`NO_COST`</li><li>`STANDARD`</ul></li>",
    "2-0": "percentage",
    "2-1": "`integer`",
    "2-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`",
    "3-0": "amount",
    "3-1": "`object`",
    "3-2": "An object that contains the subvention amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object\" >Learn more about the `amount` child object.</a>",
    "4-0": "breakup",
    "4-1": "`object`",
    "4-2": "An object that contains the subvention breakup details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#breakup-child-object\" >Learn more about the `breakup` child object.</a>",
    "5-0": "max_amount",
    "5-1": "`object`",
    "5-2": "An object that contains the maximum subvention amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#max-amount-child-object\" >Learn more about the `max_amount` child object.</a>",
    "6-0": "min_amount",
    "6-1": "`object`",
    "6-2": "An object that contains the minimum subvention amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#min-amount-child-object\" >Learn more about the `min_amount` child object.</a>"
  },
  "cols": 3,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


###### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `subvention` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


###### Breakup [Child Object]

The table below lists the various parameters in the `breakup` child object. This is part of the `subvention` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "brand",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup details of the brand.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#brand-child-object\" >Learn more about the `brand` child object.</a>"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


###### Brand [Child Object]

The table below lists the various parameters in the `brand` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup amount details of the brand.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object-1\" >Learn more about the `amount` child object.</a>"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


###### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `brand` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Max Amount [Child Object]

The table below lists the various parameters in the `max_amount` child object. This is part of the `subvention` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Min Amount [Child Object]

The table below lists the various parameters in the `min_amount` child object. This is part of the `subvention` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Discount [Child Object]

The table below lists the various parameters in the `discount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "discount_type",
    "0-1": "`String`",
    "0-2": "Type of discount.  \n  \nPossible values:<ul><li>`INSTANT`</li><li>`DEFERRED`</ul></li>",
    "1-0": "discount_string",
    "1-1": "`string`",
    "1-2": "The additional discount provided by the offering entity after a specific period.  \n  \nExample: `1000`",
    "2-0": "percentage",
    "2-1": "`Double`",
    "2-2": "The discount percentage provided by the offering entity.  \n  \nExample: `16.90`",
    "3-0": "amount",
    "3-1": "`string`",
    "3-2": "Discount amount.  \n  \nExample: `2000`",
    "4-0": "max_amount",
    "4-1": "`object`",
    "4-2": "An object that contains the maximum discount amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#max-amount-child-object-1\" >Learn more about the `max_amount` child object.</a>",
    "5-0": "min_amount",
    "5-1": "`object`",
    "5-2": "An object that contains the minimum discount amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#min-amount-child-object-1\" >Learn more about the `min_amount` child object.</a>",
    "6-0": "discount_deferred_duration_value",
    "6-1": "`integer`",
    "6-2": "The duration value for the deferred discount.  \n  \nExample: ",
    "7-0": "discount_deferred_duration_type",
    "7-1": "`string`",
    "7-2": "Discount duration type deferred.  \n  \nPossible values: <ul><li>`DAY`</li><li>`MONTH`</ul></li>",
    "8-0": "breakup",
    "8-1": "`object`",
    "8-2": "An object that contains the product offer details with breakup.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#breakup-child-object-1\" >Learn more about the `breakup` child object.</a>"
  },
  "cols": 3,
  "rows": 9,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Max Amount [Child Object]

The table below lists the various parameters in the `max_amount` child object. This is part of the `discount` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Min Amount [Child Object]

The table below lists the various parameters in the `min_amount` child object. This is part of the `discount` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Breakup [Child Object]

The table below lists the various parameters in the `breakup` child object. This is part of the `discount` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "merchant",
    "0-1": "`object`",
    "0-2": "An object that contains the merchant breakup details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#merchant-child-object\" >Learn more about the `merchant` child object.</a>",
    "1-0": "issuer",
    "1-1": "`object`",
    "1-2": "An object that contains the issure breakup details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#issuer-child-object\" >Learn more about the `issuer` child object.</a>",
    "2-0": "brand",
    "2-1": "`object`",
    "2-2": "An object that contains the brand breakup details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#brand-child-object-1\" >Learn more about the `brand` child object.</a>",
    "3-0": "dealer",
    "3-1": "`object`",
    "3-2": "An object that contains the dealer breakup details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#dealer-child-object\" >Learn more about the `dealer` child object.</a>"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


###### Merchant [Child Object]

The table below lists the various parameters in the `merchant` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object-2\" >Learn more about the `amount` child object.</a>"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


###### Issuer [Child Object]

The table below lists the various parameters in the `issure` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object-2\" >Learn more about the `amount` child object.</a>"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


###### Brand [Child Object]

The table below lists the various parameters in the `brand` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object-2\" >Learn more about the `amount` child object.</a>"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


###### Dealer [Child Object]

The table below lists the various parameters in the `dealer` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "amount",
    "0-1": "`object`",
    "0-2": "An object that contains the breakup amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#amount-child-object-2\" >Learn more about the `amount` child object.</a>"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This is part of the `breakup` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Interest Amount [Child Object]

The table below lists the various parameters in the `interest_amount` child object. This is part of the `details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Cart Coupon Discount Product Share [Child Object]

The table below lists the various parameters in the `cart_coupon_discount_product_share` child object. This is part of the `details` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Loan Amount [Child Object]

The table below lists the various parameters in the `loan_amount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Total Discount Amount [Child Object]

The table below lists the various parameters in the `total_discount_amount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Net Payment Amount [Child Object]

The table below lists the various parameters in the `net_payment_amount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Monthly EMI Amount [Child Object]

The table below lists the various parameters in the `monthly_emi_amount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Total EMI Amount [Child Object]

The table below lists the various parameters in the `total_emi_amount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Interest Amount [Child Object]

The table below lists the various parameters in the `interest_amount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Total Subvention Amount [Child Object]

The table below lists the various parameters in the `total_subvention_amount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Processing Fee Details [Child Object]

The table below lists the various parameters in the `processing_fee_details` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Convenience Fee Breakdown [Child Object]

The table below lists the various parameters in the `convenience_fee_breakdown` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "fee_calculated_on_amount",
    "0-1": "`object`",
    "0-2": "An object that contains the fee calculation amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#fee-calculated-on-amount-child-object\" >Learn more about the `fee_calculated_on_amount` child object.</a>",
    "1-0": "fee_amount",
    "1-1": "`object`",
    "1-2": "An object that contains the fee amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#fee-amount-child-object\" >Learn more about the `fee_amount` child object.</a>",
    "2-0": "tax_amount",
    "2-1": "`object`",
    "2-2": "An object that contains the tax amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#tax-amount-child-object\" >Learn more about the `tax_amount` child object.</a>",
    "3-0": "additional_fee_amount",
    "3-1": "`object`",
    "3-2": "An object that contains the additional fee amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#additional-fee-amount-child-object\" >Learn more about the `additional_fee_amount` child object.</a>",
    "4-0": "maximum_fee_amount",
    "4-1": "`object`",
    "4-2": "An object that contains the maximum fee amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#maximum-fee-amount-child-object\" >Learn more about the `maximum_fee_amount` child object.</a>",
    "5-0": "applicable_fee_amount",
    "5-1": "`object`",
    "5-2": "An object that contains the applicable fee amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#applicable-fee-amount-child-object\" >Learn more about the `applicable_fee_amount` child object.</a>",
    "6-0": "subvented_fee_amount",
    "6-1": "`object`",
    "6-2": "An object that contains the subvented fee amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-object#subvented-fee-amount-child-object\" >Learn more about the `subvented_fee_amount` child object.</a>"
  },
  "cols": 3,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Fee Calculated on Amount [Child Object]

The table below lists the various parameters in the `fee_calculated_on_amount` child object. This is part of the `convenience_fee_breakdown` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Fee Amount [Child Object]

The table below lists the various parameters in the `fee_amount` child object. This is part of the `convenience_fee_breakdown` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Tax Amount [Child Object]

The table below lists the various parameters in the `tax_amount` child object. This is part of the `convenience_fee_breakdown` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Additional Fee Amount [Child Object]

The table below lists the various parameters in the `additional_fee_amount` child object. This is part of the `convenience_fee_breakdown` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Maximum Fee Amount [Child Object]

The table below lists the various parameters in the `maximum_fee_amount` child object. This is part of the `convenience_fee_breakdown` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Applicable Fee Amount [Child Object]

The table below lists the various parameters in the `applicable_fee_amount` child object. This is part of the `convenience_fee_breakdown` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


##### Subvented Fee Amount [Child Object]

The table below lists the various parameters in the `subvented_fee_amount` child object. This is part of the `convenience_fee_breakdown` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Cart Coupon Discount Amount [Child Object]

The table below lists the various parameters in the `cart_coupon_discount_amount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Total Coupon Discount [Child Object]

The table below lists the various parameters in the `total_coupon_discount` child object. This is part of the `tenures` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "currency",
    "0-1": "`String`",
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "value",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Issuer Data [Child Object]

The table below lists the various parameters in the `issure_data` object. This is part of the offer discovery response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "otp_length",
    "0-1": "`integer`",
    "0-2": "Length of the OTP.  \n  \nExample: `4`",
    "1-0": "otp_time_in_sec",
    "1-1": "`integer`",
    "1-2": "OTP validity time in seconds.  \n  \nExample: `120`",
    "2-0": "otp_retry_count",
    "2-1": "`integer`",
    "2-2": "Maximum OTP retry count.  \n  \nExample:",
    "3-0": "is_consent_page_required",
    "3-1": "`Boolean`",
    "3-2": "Status of the required consent page.<ul><li>`true`: When the consent page is required.</li><li>`false`: When the consent page is not required.</ul></li>",
    "4-0": "consent_data",
    "4-1": "`String`",
    "4-2": "Transaction consent data.  \n  \nExample: ",
    "5-0": "terms_and_conditions",
    "5-1": "`String`",
    "5-2": "Transaction terms and conditions.  \n  \nExample: ",
    "6-0": "show_key_fact_statement",
    "6-1": "`Boolean`",
    "6-2": "Key fact statement status.<ul><li>`true`: When the key fact statement need to be displayed.</li><li>`false`: When the key fact statement is not required to be displayed.</ul></li>",
    "7-0": "auth_type",
    "7-1": "`String`",
    "7-2": "Authentication type.  \n  \nAccepted values: <ul><li>`PENNY_DROP`</li><li>`OTP`</ul></li>",
    "8-0": "penny_transaction_amount",
    "8-1": "`string`",
    "8-2": "Applicable amount for penny transaction.  \n  \nExample: `100`",
    "9-0": "is_tokenized_transaction_supported",
    "9-1": "`Boolean`",
    "9-2": "Tokenized transactions support status.<ul><li>`true`: Tokenized transaction is supported.</li><li>`false`: Tokenized transaction is not supported.</ul></li>",
    "10-0": "pan_number_last_digit_count",
    "10-1": "`String`",
    "10-2": "Last digit count of PAN.",
    "11-0": "offer_validation_parameters_required",
    "11-1": "`String`",
    "11-2": "Parameters required in offer validation API."
  },
  "cols": 3,
  "rows": 12,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]
