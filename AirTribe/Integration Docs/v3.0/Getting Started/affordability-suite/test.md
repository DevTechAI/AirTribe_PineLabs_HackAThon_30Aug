---
title: "Hidden Offer Discovery objects"
slug: "test"
excerpt: ""
hidden: true
createdAt: "Wed Jan 22 2025 09:55:18 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jan 28 2025 13:32:05 GMT+0000 (Coordinated Universal Time)"
---
#### Split EMI Amount [Child Object]

The table below lists the various parameters in the `split_emi_amount` child object. This is part of the `tenures` object.

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
    "0-1": "",
    "0-2": "Calculated convenience fee, after applying all offers.  \n  \nExample: ",
    "1-0": "fee_amount",
    "1-1": "\\`",
    "1-2": "",
    "2-0": "tax_amount",
    "2-1": "",
    "2-2": "",
    "3-0": "additional_fee_amount",
    "3-1": "",
    "3-2": "",
    "4-0": "maximum_fee_amount",
    "4-1": "",
    "4-2": "",
    "5-0": "applicable_fee_amount",
    "5-1": "",
    "5-2": ""
  },
  "cols": 3,
  "rows": 6,
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
    "13-0": "advance_emi_months",
    "13-1": "`integer`",
    "13-2": "List of months for which the EMI is paid in advance.  \n  \nExample: ",
    "14-0": "split_emi_amount",
    "14-1": "`object`",
    "14-2": "An object that contains the split emi amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#split-emi-amount-child-object\" >Learn more about the `split_emi_amount` child object.</a>",
    "15-0": "split_emi_percentage",
    "15-1": "`double`",
    "15-2": "Split EMI percentage for the tenure.  \n  \nExample: ",
    "16-0": "total_subvention_amount",
    "16-1": "`object`",
    "16-2": "An object that contains the total subvention amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#total-subvention-amount-child-object\" >Learn more about the `total_subvention_amount` child object.</a>",
    "17-0": "interest_rate_percentage",
    "17-1": "`float`",
    "17-2": "Interest rate percentage for the tenure.  \n  \nExample: `16.90`",
    "18-0": "processing_fee_details",
    "18-1": "`object`",
    "18-2": "An object that contains the processing fee details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#processing-fee-details-child-object\" >Learn more about the `processing_fee_details` child object.</a>",
    "19-0": "total_down_payment_amount",
    "19-1": "`object`",
    "19-2": "An object that contains the total down payment amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#total-down-payment-amount-child-object\" >Learn more about the `total_down_payment_amount` child object.</a>",
    "20-0": "dealer_charges_percentage",
    "20-1": "`double`",
    "20-2": "The dealer's charge percentage for the NBFC.  \n  \nExample: `2000`",
    "21-0": "net_dealer_disbursement_amount",
    "21-1": "`object`",
    "21-2": "An object that contains the processing fee details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#net-dealer-disbursement-amount\" >Learn more about the `net_dealer_disbursement_amount` child object.</a>",
    "22-0": "convenience_fee_breakdown",
    "22-1": "`object`",
    "22-2": "An object that contains the convenience fee breakdown details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#convenience-fee-breakdown-child-object\" >Learn more about the `convenience_fee_breakdown` child object.</a>",
    "23-0": "cart_coupon_discount_amount",
    "23-1": "`object`",
    "23-2": "An object that contains the processing fee details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/object-3#cart-coupon-discount-amount-child-object\" >Learn more about the `cart_coupon_discount_amount` child object.</a>",
    "24-0": "emi_type",
    "24-1": "`strings`",
    "24-2": "Type of EMI.  \n  \nExample: `STANDARD`  \n  \nAccepted values: <ul><li>`LOW_COST`</li><li>`NO_COST`</li><li>`STANDARD`</ul></li>"
  },
  "cols": 3,
  "rows": 25,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Total Down Payment Amount [Child Object]

The table below lists the various parameters in the `total_down_payment_amount` child object. This is part of the `tenures` object.

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


#### Net Dealer Disbursement Amount

The table below lists the various parameters in the `net_dealer_disbursement_amount` child object. This is part of the `tenures` object.

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


## Offer Discovery Cardless

<br />

Shown below is a sample response returned through our Offer Discovery Cardless API.

```json Offer Discovery Cardless Response
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

The table below lists the various parameters returned in the offer discovery cardless response object.

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
    "2-0": "issuer_type",
    "2-1": "`String`",
    "2-2": "The type of the Issuer offering the offer.  \n  \nAccepted values: <ul><li>`Credit`</li><li>`Debit`</li><li>`Cardless`</li><li>`NBFC`</ul></li>.",
    "3-0": "priority",
    "3-1": "`integer`",
    "3-2": "The priority of the issuer providing the offer.  \n  \nExample: `1`",
    "4-0": "tenures",
    "4-1": "`array of objects`",
    "4-2": "An array of objects that contains the tenures details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#tenures-child-object\" >Learn more about the `tenures` child object.</a>",
    "5-0": "issuer_data",
    "5-1": "`objects`",
    "5-2": "An object that contains the issuer data details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#issuer-data\" >Learn more about the `issuer_data` child object.</a>"
  },
  "cols": 3,
  "rows": 6,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Tenures [Child Object]

The table below lists the various parameters in the `tenures` object. This is part of the offer discovery cardless response object.

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
    "4-2": "An array of objects that contains the `issuer_offer_parameters` details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#issuer-offer-parameters-child-object\" >Learn more about the `issuer_offer_parameters` child object.</a>",
    "5-0": "details",
    "5-1": "`array of objects`",
    "5-2": "An array of objects that contains the `product details`.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#details-child-object\" >Learn more about the `details` child object.</a>",
    "6-0": "discount",
    "6-1": "`object`",
    "6-2": "An object that contains the discount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#discount-child-object\" >Learn more about the `discount` child object.</a>",
    "7-0": "loan_amount",
    "7-1": "`object`",
    "7-2": "An object that contains the loan amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#loan-amount-child-object\" >Learn more about the `loan_amount` child object.</a>",
    "8-0": "total_discount_amount",
    "8-1": "`object`",
    "8-2": "An object that contains the total discount amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#total-discount-amount-child-object\" >Learn more about the `total_discount_amount` child object.</a>",
    "9-0": "net_payment_amount",
    "9-1": "`object`",
    "9-2": "An object that contains the net payment amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#net-payment-amount-child-object\" >Learn more about the `net_payment_amount` child object.</a>",
    "10-0": "monthly_emi_amount",
    "10-1": "`object`",
    "10-2": "An object that contains the monthly EMI amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#monthly-emi-amount-child-object\" >Learn more about the `monthly_emi_amount` child object.</a>",
    "11-0": "total_emi_amount",
    "11-1": "`object`",
    "11-2": "An object that contains the total EMI amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#total-emi-amount-child-object\" >Learn more about the `total_emi_amount` child object.</a>",
    "12-0": "interest_amount",
    "12-1": "`object`",
    "12-2": "An object that contains the interest amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#interest-amount-child-object\" >Learn more about the `interest_amount` child object.</a>",
    "13-0": "advance_emi_months",
    "13-1": "`integer`",
    "13-2": "List of months for which the EMI is paid in advance.  \n  \nExample: ",
    "14-0": "split_emi_amount",
    "14-1": "`object`",
    "14-2": "An object that contains the split emi amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#split-emi-amount-child-object\" >Learn more about the `split_emi_amount` child object.</a>",
    "15-0": "split_emi_percentage",
    "15-1": "`double`",
    "15-2": "Split EMI percentage for the tenure.  \n  \nExample: ",
    "16-0": "total_subvention_amount",
    "16-1": "`object`",
    "16-2": "An object that contains the total subvention amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#total-subvention-amount-child-object\" >Learn more about the `total_subvention_amount` child object.</a>",
    "17-0": "interest_rate_percentage",
    "17-1": "`float`",
    "17-2": "Interest rate percentage for the tenure.  \n  \nExample: `16.90`",
    "18-0": "processing_fee_details",
    "18-1": "`object`",
    "18-2": "An object that contains the processing fee details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#processing-fee-details-child-object\" >Learn more about the `processing_fee_details` child object.</a>",
    "19-0": "total_down_payment_amount",
    "19-1": "`object`",
    "19-2": "An object that contains the total down payment amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#total-down-payment-amount-child-object\" >Learn more about the `total_down_payment_amount` child object.</a>",
    "20-0": "dealer_charges_percentage",
    "20-1": "`double`",
    "20-2": "The dealer's charge percentage for the NBFC.  \n  \nExample: `2000`",
    "21-0": "net_dealer_disbursement_amount",
    "21-1": "`object`",
    "21-2": "An object that contains the processing fee details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#net-dealer-disbursement-amount\" >Learn more about the `net_dealer_disbursement_amount` child object.</a>",
    "22-0": "convenience_fee_breakdown",
    "22-1": "`object`",
    "22-2": "An object that contains the convenience fee breakdown details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#convenience-fee-breakdown-child-object\" >Learn more about the `convenience_fee_breakdown` child object.</a>",
    "23-0": "cart_coupon_discount_amount",
    "23-1": "`object`",
    "23-2": "An object that contains the processing fee details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#cart-coupon-discount-amount-child-object\" >Learn more about the `cart_coupon_discount_amount` child object.</a>",
    "24-0": "emi_type",
    "24-1": "`strings`",
    "24-2": "Type of EMI.  \n  \nExample: `STANDARD`  \n  \nAccepted values: <ul><li>`LOW_COST`</li><li>`NO_COST`</li><li>`STANDARD`</ul></li>"
  },
  "cols": 3,
  "rows": 25,
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
    "1-0": "brand_id",
    "1-1": "`String`",
    "1-2": "Unique brand identifier of the product.  \n  \nExample: `3`",
    "2-0": "product_offer_parameters",
    "2-1": "`array of objects`",
    "2-2": "An array of objects that contains the product offer schemes for the product EMI details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#product-offer-parameters-child-object\" >Learn more about the `product_offer_parameters` child object.</a>",
    "3-0": "product_amount",
    "3-1": "`object`",
    "3-2": "An object that contains the product amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#product-amount-child-object\" >Learn more about the `product_amount` child object.</a>",
    "4-0": "subvention",
    "4-1": "`object`",
    "4-2": "An object that contains the subvention details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#subvention-child-object\" >Learn more about the `subvention` child object.</a>",
    "5-0": "discount",
    "5-1": "`object`",
    "5-2": "An object that contains the product discount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#discount-child-object\" >Learn more about the `discount` child object.</a>"
  },
  "cols": 3,
  "rows": 6,
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
    "0-2": "Type of currency.  \n  \nExample: INR",
    "1-0": "percentage",
    "1-1": "`integer`",
    "1-2": "Transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `1000`",
    "2-0": "amount",
    "2-1": "`object`",
    "2-2": "An object that contains the subvention amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#amount-child-object\" >Learn more about the `amount` child object.</a>",
    "3-0": "breakup",
    "3-1": "`object`",
    "3-2": "An object that contains the subvention breakup details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#breakup-child-object\" >Learn more about the `breakup` child object.</a>"
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
    "0-2": "An object that contains the breakup details of the brand.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#brand-child-object\" >Learn more about the `brand` child object.</a>"
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
    "0-2": "An object that contains the breakup amount details of the brand.  \n  \n<a href=\"https://developer.pluralonline.com/reference/offer-discovery-cardless-object#amount-child-object-1\" >Learn more about the `amount` child object.</a>"
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
    "1-0": "percentage",
    "1-1": "`Double`",
    "1-2": "The discount percentage provided by the offering entity.  \n  \nExample: `16.90`",
    "2-0": "amount",
    "2-1": "`string`",
    "2-2": "Discount amount.  \n  \nExample: `2000`",
    "3-0": "discount_deferred_duration_value",
    "3-1": "`integer`",
    "3-2": "The duration value for the deferred discount.  \n  \nExample: ",
    "4-0": "discount_deferred_duration_type",
    "4-1": "`string`",
    "4-2": "Discount duration type deferred.  \n  \nPossible values: <ul><li>`DAY`</li><li>`MONTH`</ul></li>",
    "5-0": "breakup",
    "5-1": "`object`",
    "5-2": "An object that contains the product offer details with breakup.  \n  \nLearn more about the `breakup` child object."
  },
  "cols": 3,
  "rows": 6,
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


#### Split EMI Amount [Child Object]

The table below lists the various parameters in the `split_emi_amount` child object. This is part of the `tenures` object.

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


#### Total Down Payment Amount [Child Object]

The table below lists the various parameters in the `total_down_payment_amount` child object. This is part of the `tenures` object.

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


#### Net Dealer Disbursement Amount

The table below lists the various parameters in the `net_dealer_disbursement_amount` child object. This is part of the `tenures` object.

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
    "0-1": "",
    "0-2": "Calculated convenience fee, after applying all offers.  \n  \nExample: ",
    "1-0": "fee_amount",
    "1-1": "",
    "1-2": "",
    "2-0": "tax_amount",
    "2-1": "",
    "2-2": "",
    "3-0": "additional_fee_amount",
    "3-1": "",
    "3-2": "",
    "4-0": "maximum_fee_amount",
    "4-1": "",
    "4-2": "",
    "5-0": "applicable_fee_amount",
    "5-1": "",
    "5-2": ""
  },
  "cols": 3,
  "rows": 6,
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


### Issuer Data [Child Object]

The table below lists the various parameters in the `issure_data` object. This is part of the offer discovery cardless response object.

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


<br />

## EMITenureDetails

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "tenure_id",
    "0-1": "`String`",
    "0-2": "The ID of the Tenure.",
    "1-0": "name",
    "1-1": "`String`",
    "1-2": "The name of the Tenure.",
    "2-0": "tenure_type",
    "2-1": "`String`",
    "2-2": "Type of the tenure.",
    "3-0": "tenure_value",
    "3-1": "`integer`",
    "3-2": "The value of the tenure.",
    "4-0": "issuer_offer_parameters",
    "4-1": "",
    "4-2": "List of Offer Schemes for the tenure.",
    "5-0": "details",
    "5-1": "",
    "5-2": "Product Offer details for the tenure.",
    "6-0": "discount",
    "6-1": "",
    "6-2": "Discount details applicable for the tenure.",
    "7-0": "loan_amount",
    "7-1": "`Amount`",
    "7-2": "Loan amount for the tenure.",
    "8-0": "total_discount_amount",
    "8-1": "`Amount`",
    "8-2": "Total discount amount for the tenure.",
    "9-0": "net_payment_amount",
    "9-1": "`Amount`",
    "9-2": "Net payment amount for the tenure.",
    "10-0": "monthly_emi_amount",
    "10-1": "`Amount`",
    "10-2": "Monthly EMI amount for the tenure.",
    "11-0": "total_emi_amount",
    "11-1": "`Amount`",
    "11-2": "Total EMI amount for the tenure.",
    "12-0": "interest_amount",
    "12-1": "`Amount`",
    "12-2": "Interest amount for the tenure.",
    "13-0": "advance_emi_months",
    "13-1": "",
    "13-2": "List of months for which EMI is paid in advance.",
    "14-0": "split_emi_amount",
    "14-1": "`Amount`",
    "14-2": "EMI split the amount for the tenure.",
    "15-0": "split_emi_percentage",
    "15-1": "",
    "15-2": "Split EMI percentage for the tenure.",
    "16-0": "total_subvention_amount",
    "16-1": "`Amount`",
    "16-2": "Total subvention amount for the tenure.",
    "17-0": "interest_rate_percentage",
    "17-1": "",
    "17-2": "Interest rate percentage for the tenure.",
    "18-0": "processing_fee_details",
    "18-1": "",
    "18-2": "Processing fee details for the tenure.",
    "19-0": "total_down_payment_amount",
    "19-1": "`Amount`",
    "19-2": "Total down payment amount for the tenure.",
    "20-0": "dealer_charges_percentage",
    "20-1": "",
    "20-2": "Dealer charges percentage for NBFC.",
    "21-0": "net_dealer_disbursement_amount",
    "21-1": "`Amount`",
    "21-2": "Net dealer disbursement amount for the tenure.",
    "22-0": "convenience_fee_breakdown",
    "22-1": "",
    "22-2": "Convenience fee applied on the offer",
    "23-0": "cart_coupon_discount_amount",
    "23-1": "`Amount`",
    "23-2": "Coupon discount applied on the cart",
    "24-0": "emi_type",
    "24-1": "",
    "24-2": "EMI type for the tenure  \n(e.g., \"LOW_COST\",  \n\"NO_COST\",  \n\"STANDARD\")."
  },
  "cols": 3,
  "rows": 25,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## OfferScheme

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "program_type",
    "0-1": "`String`",
    "0-2": "Type of the program  \n(BRAND_EMI, BANK_EMI,  \nMERCHANT_BRAND_OFFER,  \nMERCHANT_BANK_OFFER,  \nBRAND_OFFER, MY_EMI)",
    "1-0": "offer_id",
    "1-1": "`String`",
    "1-2": "The Offer ID.",
    "2-0": "offer_parameter_id",
    "2-1": "`String`",
    "2-2": "The Offer Parameter ID of the Offer."
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


## ConvenienceFeeBreakdown

| Parameter                | Type     | Description                                                    |
| :----------------------- | :------- | :------------------------------------------------------------- |
| fee_calculated_on_amount | `Amount` | Convenience fee calculated on amount after applying all offers |
| fee_amount               | `Amount` | Actual Convenience fee applied                                 |
| tax_amount               | `Amount` | GST amount applied on fee amount                               |
| additional_fee_amount    | `Amount` | Additional fee on top of convenience fee if any                |
| maximum_fee_amount       | `Amount` | Max fee can be applied                                         |
| applicable_fee_amount    | `Amount` | Total convenience fee                                          |

## EMIProductDetail

| Parameter                      | Type     | Description                                              |
| :----------------------------- | :------- | :------------------------------------------------------- |
| product_code                   | `String` | Product Id of the Product.                               |
| product_display_name           | `String` | Product Display name                                     |
| brand_id                       |          | Brand ID of the Product.                                 |
| product_offer_parameters       |          | List of Product Offer Scheme for the Product EMI Detail. |
| product_amount                 | `Amount` | Amount for the product.                                  |
| product_coupon_discount_amount | `Amount` | Amount for the product coupon discount                   |
| subvention                     |          | Subvention details for the product.                      |
| discount                       |          | Discount details for the product.                        |

## ProcessingFeeDetails

| Parameter  | Type     | Description                                               |
| :--------- | :------- | :-------------------------------------------------------- |
| percentage |          | Processing fee percentage offered by the offering entity. |
| amount     | `Amount` | Processing fee amount.                                    |

## SubventionDetail

| Parameter       | Type     | Description                                           |
| :-------------- | :------- | :---------------------------------------------------- |
| subvention_type | `String` | Type of the subvention (INSTANT, POST)                |
| offer_type      |          | Type of the EMI offer (LOW_COST, NO_COST, STANDARD)   |
| percentage      |          | Subvention percentage offered by the offering entity. |
| amount          | `Amount` | Subvention amount.                                    |
| breakup         |          | Breakup details for the product EMI detail.           |

## DiscountDetail

| Parameter                        | Type      | Description                                         |
| :------------------------------- | :-------- | :-------------------------------------------------- |
| discount_type                    | `String`  | Type of discount (INSTANT, DEFERRED)                |
| percentage                       |           | Discount percentage offered by the offering entity. |
| amount                           | `Amount`  | Discount amount.                                    |
| discount_deferred_duration_value | `Integer` | The value of the discount deferred duration.        |
| discount_deferred_duration_type  | `String`  | Type of the tenure for the discount (DAY, MONTH).   |
| breakup                          |           | Breakup details for the product offer detail.       |

## Breakup

| Parameter | Type | Description                      |
| :-------- | :--- | :------------------------------- |
| merchant  |      | Breakup detail for the merchant. |
| issuer    |      | Breakup detail for the issuer.   |
| brand     |      | Breakup detail for the brand.    |
| dealer    |      | Breakup detail for the dealer.   |

## BreakupDetail

| Parameter | Type     | Description                    |
| :-------- | :------- | :----------------------------- |
| amount    | `Amount` | Amount for the breakup detail. |

## 2. Offer Discovery Cardless

Shown below is a sample response returned through our Offer Discovery Cardless API.

```Text Offer Discovery Cardless

```

The table below lists the various parameters returned in the response objects.

## OfferDiscoveryIssuerDetail

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "id",
    "0-1": "`String`",
    "0-2": "Issuer Id",
    "1-0": "name",
    "1-1": "`String`",
    "1-2": "Issuer Name",
    "2-0": "display_name",
    "2-1": "`String`",
    "2-2": "Display Name of the Issuer  \noffering the Offer",
    "3-0": "issuer_type",
    "3-1": "`String`",
    "3-2": "Type of Issuer (e.g., Credit,  \nDebit ,Cardless, NBFC).",
    "4-0": "priority",
    "4-1": "`integer`",
    "4-2": "Priority of the Issuer offering the  \nOffer",
    "5-0": "tenures",
    "5-1": "",
    "5-2": " List of Tenures available for the  \nOffer.",
    "6-0": "issuer_data",
    "6-1": "",
    "6-2": "Data related to the Issuer (OTP,  \nconsent, etc.)."
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


## IssuerData

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "otp_length",
    "0-1": "`integer`",
    "0-2": "Length of the OTP.",
    "1-0": "otp_time_in_sec",
    "1-1": "`integer`",
    "1-2": "OTP validity time in seconds.",
    "2-0": "otp_retry_count",
    "2-1": "`integer`",
    "2-2": "Maximum retry count for OTP",
    "3-0": "is_consent_page_required",
    "3-1": "`Boolean`",
    "3-2": "Whether consent page is required.",
    "4-0": "consent_data",
    "4-1": "`String`",
    "4-2": "Consent data for the transaction.",
    "5-0": "terms_and_conditions",
    "5-1": "`String`",
    "5-2": "Terms and conditions data for the transaction.",
    "6-0": "show_key_fact_statement",
    "6-1": "`Boolean`",
    "6-2": "Whether the key fact statement should be shown.",
    "7-0": "auth_type",
    "7-1": "`String`",
    "7-2": "Authentication type (PENNY_DROP or OTP).",
    "8-0": "penny_transaction_amount",
    "8-1": "`Amount`",
    "8-2": "Amount for penny transaction (if applicable).",
    "9-0": "is_tokenized_transaction_supported",
    "9-1": "`Boolean`",
    "9-2": "Whether tokenized transactions are supported.",
    "10-0": "pan_number_last_digit_count",
    "10-1": "`String`",
    "10-2": "Last digit count of PAN",
    "11-0": "offer_validation_parameters_required",
    "11-1": "`String`",
    "11-2": "Params required in offer  \nvalidation API(  \ncard_details\\_\\_registered_  \nmobile_number,  \ncardless_details**registered_mobile_number,  \ncardless_details**pan_la  \nst_digits,  \ncard_details\\_\\_card_number,  \ncard_token_details**token,  \ncard_token_details**toke  \nn_id)  \n\\_\\_(double underscore)  \nmeans nested property  \nof parent object"
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


## EMITenureDetails

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "tenure_id",
    "0-1": "`String`",
    "0-2": "The ID of the Tenure.",
    "1-0": "name",
    "1-1": "`String`",
    "1-2": "The name of the Tenure.",
    "2-0": "tenure_type",
    "2-1": "`String`",
    "2-2": "Type of the tenure.",
    "3-0": "tenure_value",
    "3-1": "`integer`",
    "3-2": "The value of the tenure.",
    "4-0": "issuer_offer_parameters",
    "4-1": "",
    "4-2": "List of Offer Schemes for the tenure.",
    "5-0": "details",
    "5-1": "",
    "5-2": "Product Offer details for the tenure.",
    "6-0": "discount",
    "6-1": "",
    "6-2": "Discount details applicable for the tenure.",
    "7-0": "loan_amount",
    "7-1": "`Amount`",
    "7-2": "Loan amount for the tenure.",
    "8-0": "total_discount_amount",
    "8-1": "`Amount`",
    "8-2": "Total discount amount for the tenure.",
    "9-0": "net_payment_amount",
    "9-1": "`Amount`",
    "9-2": "Net payment amount for the tenure.",
    "10-0": "monthly_emi_amount",
    "10-1": "`Amount`",
    "10-2": "Monthly EMI amount for the tenure.",
    "11-0": "total_emi_amount",
    "11-1": "`Amount`",
    "11-2": "Total EMI amount for the tenure.",
    "12-0": "interest_amount",
    "12-1": "`Amount`",
    "12-2": "Interest amount for the tenure.",
    "13-0": "advance_emi_months",
    "13-1": "",
    "13-2": "List of months for which EMI is paid in advance.",
    "14-0": "split_emi_amount",
    "14-1": "`Amount`",
    "14-2": "EMI split the amount for the tenure.",
    "15-0": "split_emi_percentage",
    "15-1": "",
    "15-2": "Split EMI percentage for the tenure.",
    "16-0": "total_subvention_amount",
    "16-1": "`Amount`",
    "16-2": "Total subvention amount for the tenure.",
    "17-0": "interest_rate_percentage",
    "17-1": "",
    "17-2": "Interest rate percentage for the tenure.",
    "18-0": "processing_fee_details",
    "18-1": "",
    "18-2": "Processing fee details for the tenure.",
    "19-0": "total_down_payment_amount",
    "19-1": "`Amount`",
    "19-2": "Total down payment amount for the tenure.",
    "20-0": "dealer_charges_percentage",
    "20-1": "",
    "20-2": "Dealer charges percentage for NBFC.",
    "21-0": "net_dealer_disbursement_amount",
    "21-1": "`Amount`",
    "21-2": "Net dealer disbursement amount for the tenure.",
    "22-0": "convenience_fee_breakdown",
    "22-1": "",
    "22-2": "Convenience fee applied on the offer",
    "23-0": "cart_coupon_discount_amount",
    "23-1": "`Amount`",
    "23-2": "Coupon discount applied on the cart",
    "24-0": "emi_type",
    "24-1": "",
    "24-2": "EMI type for the tenure  \n(e.g., \"LOW_COST\",  \n\"NO_COST\",  \n\"STANDARD\")."
  },
  "cols": 3,
  "rows": 25,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## OfferScheme

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "program_type",
    "0-1": "`String`",
    "0-2": "Type of the program  \n(BRAND_EMI, BANK_EMI,  \nMERCHANT_BRAND_OFFER,  \nMERCHANT_BANK_OFFER,  \nBRAND_OFFER, MY_EMI)",
    "1-0": "offer_id",
    "1-1": "`String`",
    "1-2": "The Offer ID.",
    "2-0": "offer_parameter_id",
    "2-1": "`String`",
    "2-2": "The Offer Parameter ID of the Offer."
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


## ConvenienceFeeBreakdown

| Parameter                | Type     | Description                                                    |
| :----------------------- | :------- | :------------------------------------------------------------- |
| fee_calculated_on_amount | `Amount` | Convenience fee calculated on amount after applying all offers |
| fee_amount               | `Amount` | Actual Convenience fee applied                                 |
| tax_amount               | `Amount` | GST amount applied on fee amount                               |
| additional_fee_amount    | `Amount` | Additional fee on top of convenience fee if any                |
| maximum_fee_amount       | `Amount` | Max fee can be applied                                         |
| applicable_fee_amount    | `Amount` | Total convenience fee                                          |

## EMIProductDetail

| Parameter                      | Type     | Description                                              |
| :----------------------------- | :------- | :------------------------------------------------------- |
| product_code                   | `String` | Product Id of the Product.                               |
| product_display_name           | `String` | Product Display name                                     |
| brand_id                       |          | Brand ID of the Product.                                 |
| product_offer_parameters       |          | List of Product Offer Scheme for the Product EMI Detail. |
| product_amount                 | `Amount` | Amount for the product.                                  |
| product_coupon_discount_amount | `Amount` | Amount for the product coupon discount                   |
| subvention                     |          | Subvention details for the product.                      |
| discount                       |          | Discount details for the product.                        |

## ProcessingFeeDetails

| Parameter  | Type     | Description                                               |
| :--------- | :------- | :-------------------------------------------------------- |
| percentage |          | Processing fee percentage offered by the offering entity. |
| amount     | `Amount` | Processing fee amount.                                    |

## SubventionDetail

| Parameter       | Type     | Description                                           |
| :-------------- | :------- | :---------------------------------------------------- |
| subvention_type | `String` | Type of the subvention (INSTANT, POST)                |
| offer_type      |          | Type of the EMI offer (LOW_COST, NO_COST, STANDARD)   |
| percentage      |          | Subvention percentage offered by the offering entity. |
| amount          | `Amount` | Subvention amount.                                    |
| breakup         |          | Breakup details for the product EMI detail.           |

## DiscountDetail

| Parameter                        | Type      | Description                                         |
| :------------------------------- | :-------- | :-------------------------------------------------- |
| discount_type                    | `String`  | Type of discount (INSTANT, DEFERRED)                |
| percentage                       |           | Discount percentage offered by the offering entity. |
| amount                           | `Amount`  | Discount amount.                                    |
| discount_deferred_duration_value | `Integer` | The value of the discount deferred duration.        |
| discount_deferred_duration_type  | `String`  | Type of the tenure for the discount (DAY, MONTH).   |
| breakup                          |           | Breakup details for the product offer detail.       |

## Breakup

| Parameter | Type | Description                      |
| :-------- | :--- | :------------------------------- |
| merchant  |      | Breakup detail for the merchant. |
| issuer    |      | Breakup detail for the issuer.   |
| brand     |      | Breakup detail for the brand.    |
| dealer    |      | Breakup detail for the dealer.   |

## BreakupDetail

| Parameter | Type     | Description                    |
| :-------- | :------- | :----------------------------- |
| amount    | `Amount` | Amount for the breakup detail. |

## 3. Offer Validation

Shown below is a sample response returned through our Offer Validation API.

```json Offer validation_Bank EMI(CREDIT_EMI)
{
   "code": "ELIGIBLE",
   "message": "Offer is Eligible"
}

```
```json Offer validation_Brand EMI(CREDIT_EMI)
{
   "code": "ELIGIBLE",
   "message": "Offer is Eligible"
}

```
```json Ofer validation_Bank EMI(DEBIT_EMI)
{
   "code": "ELIGIBLE",
   "message": "Offer is Eligible"
}

```

The table below lists the various parameters returned in the response objects.

## OfferDiscoveryIssuerDetail

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "id",
    "0-1": "`String`",
    "0-2": "Issuer Id",
    "1-0": "name",
    "1-1": "`String`",
    "1-2": "Issuer Name",
    "2-0": "display_name",
    "2-1": "`String`",
    "2-2": "Display Name of the Issuer  \noffering the Offer",
    "3-0": "issuer_type",
    "3-1": "`String`",
    "3-2": "Type of Issuer (e.g., Credit,  \nDebit ,Cardless, NBFC).",
    "4-0": "priority",
    "4-1": "`integer`",
    "4-2": "Priority of the Issuer offering the  \nOffer",
    "5-0": "tenures",
    "5-1": "",
    "5-2": " List of Tenures available for the  \nOffer.",
    "6-0": "issuer_data",
    "6-1": "",
    "6-2": "Data related to the Issuer (OTP,  \nconsent, etc.)."
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


## IssuerData

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "otp_length",
    "0-1": "`integer`",
    "0-2": "Length of the OTP.",
    "1-0": "otp_time_in_sec",
    "1-1": "`integer`",
    "1-2": "OTP validity time in seconds.",
    "2-0": "otp_retry_count",
    "2-1": "`integer`",
    "2-2": "Maximum retry count for OTP",
    "3-0": "is_consent_page_required",
    "3-1": "`Boolean`",
    "3-2": "Whether consent page is required.",
    "4-0": "consent_data",
    "4-1": "`String`",
    "4-2": "Consent data for the transaction.",
    "5-0": "terms_and_conditions",
    "5-1": "`String`",
    "5-2": "Terms and conditions data for the transaction.",
    "6-0": "show_key_fact_statement",
    "6-1": "`Boolean`",
    "6-2": "Whether the key fact statement should be shown.",
    "7-0": "auth_type",
    "7-1": "`String`",
    "7-2": "Authentication type (PENNY_DROP or OTP).",
    "8-0": "penny_transaction_amount",
    "8-1": "`Amount`",
    "8-2": "Amount for penny transaction (if applicable).",
    "9-0": "is_tokenized_transaction_supported",
    "9-1": "`Boolean`",
    "9-2": "Whether tokenized transactions are supported.",
    "10-0": "pan_number_last_digit_count",
    "10-1": "`String`",
    "10-2": "Last digit count of PAN",
    "11-0": "offer_validation_parameters_required",
    "11-1": "`String`",
    "11-2": "Params required in offer  \nvalidation API(  \ncard_details\\_\\_registered_  \nmobile_number,  \ncardless_details**registered_mobile_number,  \ncardless_details**pan_la  \nst_digits,  \ncard_details\\_\\_card_number,  \ncard_token_details**token,  \ncard_token_details**toke  \nn_id)  \n\\_\\_(double underscore)  \nmeans nested property  \nof parent object"
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


## EMITenureDetails

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "tenure_id",
    "0-1": "`String`",
    "0-2": "The ID of the Tenure.",
    "1-0": "name",
    "1-1": "`String`",
    "1-2": "The name of the Tenure.",
    "2-0": "tenure_type",
    "2-1": "`String`",
    "2-2": "Type of the tenure.",
    "3-0": "tenure_value",
    "3-1": "`integer`",
    "3-2": "The value of the tenure.",
    "4-0": "issuer_offer_parameters",
    "4-1": "",
    "4-2": "List of Offer Schemes for the tenure.",
    "5-0": "details",
    "5-1": "",
    "5-2": "Product Offer details for the tenure.",
    "6-0": "discount",
    "6-1": "",
    "6-2": "Discount details applicable for the tenure.",
    "7-0": "loan_amount",
    "7-1": "`Amount`",
    "7-2": "Loan amount for the tenure.",
    "8-0": "total_discount_amount",
    "8-1": "`Amount`",
    "8-2": "Total discount amount for the tenure.",
    "9-0": "net_payment_amount",
    "9-1": "`Amount`",
    "9-2": "Net payment amount for the tenure.",
    "10-0": "monthly_emi_amount",
    "10-1": "`Amount`",
    "10-2": "Monthly EMI amount for the tenure.",
    "11-0": "total_emi_amount",
    "11-1": "`Amount`",
    "11-2": "Total EMI amount for the tenure.",
    "12-0": "interest_amount",
    "12-1": "`Amount`",
    "12-2": "Interest amount for the tenure.",
    "13-0": "advance_emi_months",
    "13-1": "",
    "13-2": "List of months for which EMI is paid in advance.",
    "14-0": "split_emi_amount",
    "14-1": "`Amount`",
    "14-2": "EMI split the amount for the tenure.",
    "15-0": "split_emi_percentage",
    "15-1": "",
    "15-2": "Split EMI percentage for the tenure.",
    "16-0": "total_subvention_amount",
    "16-1": "`Amount`",
    "16-2": "Total subvention amount for the tenure.",
    "17-0": "interest_rate_percentage",
    "17-1": "",
    "17-2": "Interest rate percentage for the tenure.",
    "18-0": "processing_fee_details",
    "18-1": "",
    "18-2": "Processing fee details for the tenure.",
    "19-0": "total_down_payment_amount",
    "19-1": "`Amount`",
    "19-2": "Total down payment amount for the tenure.",
    "20-0": "dealer_charges_percentage",
    "20-1": "",
    "20-2": "Dealer charges percentage for NBFC.",
    "21-0": "net_dealer_disbursement_amount",
    "21-1": "`Amount`",
    "21-2": "Net dealer disbursement amount for the tenure.",
    "22-0": "convenience_fee_breakdown",
    "22-1": "",
    "22-2": "Convenience fee applied on the offer",
    "23-0": "cart_coupon_discount_amount",
    "23-1": "`Amount`",
    "23-2": "Coupon discount applied on the cart",
    "24-0": "emi_type",
    "24-1": "",
    "24-2": "EMI type for the tenure  \n(e.g., \"LOW_COST\",  \n\"NO_COST\",  \n\"STANDARD\")."
  },
  "cols": 3,
  "rows": 25,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## OfferScheme

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "program_type",
    "0-1": "`String`",
    "0-2": "Type of the program  \n(BRAND_EMI, BANK_EMI,  \nMERCHANT_BRAND_OFFER,  \nMERCHANT_BANK_OFFER,  \nBRAND_OFFER, MY_EMI)",
    "1-0": "offer_id",
    "1-1": "`String`",
    "1-2": "The Offer ID.",
    "2-0": "offer_parameter_id",
    "2-1": "`String`",
    "2-2": "The Offer Parameter ID of the Offer."
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


## ConvenienceFeeBreakdown

| Parameter                | Type     | Description                                                    |
| :----------------------- | :------- | :------------------------------------------------------------- |
| fee_calculated_on_amount | `Amount` | Convenience fee calculated on amount after applying all offers |
| fee_amount               | `Amount` | Actual Convenience fee applied                                 |
| tax_amount               | `Amount` | GST amount applied on fee amount                               |
| additional_fee_amount    | `Amount` | Additional fee on top of convenience fee if any                |
| maximum_fee_amount       | `Amount` | Max fee can be applied                                         |
| applicable_fee_amount    | `Amount` | Total convenience fee                                          |

## EMIProductDetail

| Parameter                      | Type     | Description                                              |
| :----------------------------- | :------- | :------------------------------------------------------- |
| product_code                   | `String` | Product Id of the Product.                               |
| product_display_name           | `String` | Product Display name                                     |
| brand_id                       |          | Brand ID of the Product.                                 |
| product_offer_parameters       |          | List of Product Offer Scheme for the Product EMI Detail. |
| product_amount                 | `Amount` | Amount for the product.                                  |
| product_coupon_discount_amount | `Amount` | Amount for the product coupon discount                   |
| subvention                     |          | Subvention details for the product.                      |
| discount                       |          | Discount details for the product.                        |

## ProcessingFeeDetails

| Parameter  | Type     | Description                                               |
| :--------- | :------- | :-------------------------------------------------------- |
| percentage |          | Processing fee percentage offered by the offering entity. |
| amount     | `Amount` | Processing fee amount.                                    |

## SubventionDetail

| Parameter       | Type     | Description                                           |
| :-------------- | :------- | :---------------------------------------------------- |
| subvention_type | `String` | Type of the subvention (INSTANT, POST)                |
| offer_type      |          | Type of the EMI offer (LOW_COST, NO_COST, STANDARD)   |
| percentage      |          | Subvention percentage offered by the offering entity. |
| amount          | `Amount` | Subvention amount.                                    |
| breakup         |          | Breakup details for the product EMI detail.           |

## DiscountDetail

| Parameter                        | Type      | Description                                         |
| :------------------------------- | :-------- | :-------------------------------------------------- |
| discount_type                    | `String`  | Type of discount (INSTANT, DEFERRED)                |
| percentage                       |           | Discount percentage offered by the offering entity. |
| amount                           | `Amount`  | Discount amount.                                    |
| discount_deferred_duration_value | `Integer` | The value of the discount deferred duration.        |
| discount_deferred_duration_type  | `String`  | Type of the tenure for the discount (DAY, MONTH).   |
| breakup                          |           | Breakup details for the product offer detail.       |

## Breakup

| Parameter | Type | Description                      |
| :-------- | :--- | :------------------------------- |
| merchant  |      | Breakup detail for the merchant. |
| issuer    |      | Breakup detail for the issuer.   |
| brand     |      | Breakup detail for the brand.    |
| dealer    |      | Breakup detail for the dealer.   |

## BreakupDetail

| Parameter | Type     | Description                    |
| :-------- | :------- | :----------------------------- |
| amount    | `Amount` | Amount for the breakup detail. |
