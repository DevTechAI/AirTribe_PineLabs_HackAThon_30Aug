---
title: "Object"
slug: "convenience-fee-object"
excerpt: "Overview of the Convenience Fee response object."
hidden: false
createdAt: "Fri Dec 13 2024 06:41:32 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Dec 16 2024 13:09:30 GMT+0000 (Coordinated Universal Time)"
---
Shown below is a sample response of a Calculate Convenience Fee API.

```json Sample Response
{
  "data": [
    {
      "payment_method": "CARD",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 300,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 57,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 20,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 377,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 10377,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "UNKNOWN",
        "card_type": "CREDIT"
      }
    },
    {
      "payment_method": "CARD",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 360,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 101,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 205,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 666,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 10666,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "VISA",
        "card_type": "CREDIT"
      }
    },
    {
      "payment_method": "CARD",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 480,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 122,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 201,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 803,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 10803,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "MASTERCARD",
        "card_type": "CREDIT"
      }
    },
    {
      "payment_method": "NETBANKING",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 400,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 77,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 30,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 507,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 10507,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "UNKNOWN"
      }
    },
    {
      "payment_method": "UPI",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 600,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 117,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 50,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 767,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 10767,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "UNKNOWN"
      }
    },
    {
      "payment_method": "WALLET",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 700,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 136,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 60,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 896,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 10896,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "UNKNOWN"
      }
    },
    {
      "payment_method": "CARD",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 900,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 176,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 80,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 1156,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 11156,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "UNKNOWN",
        "card_type": "DEBIT"
      }
    },
    {
      "payment_method": "CARD",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 1100,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 351,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 850,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 2301,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 12301,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "MASTERCARD",
        "card_type": "DEBIT"
      }
    }
  ]
}
```
```json
{
  "data": [
    {
      "payment_method": "CARD",
      "fee_type": "PERCENTAGE",
      "amount": {
        "value": 10000,
        "currency": "INR"
      },
      "convenience_fee_breakdown": {
        "fee_amount": {
          "value": 300,
          "currency": "INR"
        },
        "tax_amount": {
          "value": 57,
          "currency": "INR"
        },
        "additional_fee_amount": {
          "value": 20,
          "currency": "INR"
        },
        "maximum_fee_amount": {
          "value": 1500000,
          "currency": "INR"
        },
        "applicable_fee_amount": {
          "value": 377,
          "currency": "INR"
        }
      },
      "payable_amount": {
        "value": 10377,
        "currency": "INR"
      },
      "payment_method_metadata": {
        "network_type": "UNKNOWN",
        "card_type": "CREDIT"
      }
    }
  ]
}
```

The table below lists the various parameters returned in the calculate convenience fee response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "payment_method",
    "0-1": "`string`",
    "0-2": "Type of payment method.  \n  \nAccepted values:<ul><li>`CARD`</li><li>`UPI`</li><li>`POINTS`</li><li>`NETBANKING`</li><li>`WALLETS`</ul></li>Example: `CARD`",
    "1-0": "fee_type",
    "1-1": "`string`",
    "1-2": "Convenience fee type.  \n  \nAccepted values:<ul><li>`AMOUNT`</li><li>`PERCENTAGE`",
    "2-0": "amount",
    "2-1": "`object`",
    "2-2": "An object that contains the order amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/convenience-fee-object#amount-child-object\" >Learn more about our payment_amount child object</a>.",
    "3-0": "convenience_fee_breakdown",
    "3-1": "`object`",
    "3-2": "An object that contains the convenience fee breakdown details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/convenience-fee-object#convenience-fee-breakdown-child-object\" >Learn more about our payment_amount child object</a>.",
    "4-0": "payable_amount",
    "4-1": "`object`",
    "4-2": "An object that contains the payable amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/convenience-fee-object#payable-amount-child-object\" >Learn more about our payment_amount child object</a>.",
    "5-0": "payment_method_metadata",
    "5-1": "`object`",
    "5-2": "An object that contains the payment method details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/convenience-fee-object#payment-method-metadata-child-object\" >Learn more about our payment_amount child object</a>."
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


## Amount [Child Object]

The table below lists the various parameters in the `amount` child object. This object is part of the calculate convenience fee sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value",
    "0-1": "`integer`",
    "0-2": "The transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
    "1-0": "currency",
    "1-1": "`string`",
    "1-2": "Type of currency.  \n  \nExample: `INR`"
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


## Convenience Fee Breakdown [Child Object]

The table below lists the various parameters in the `convenience_fee_breakdown` child object. This object is part of the calculate convenience fee sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "fee_amount",
    "0-1": "`object`",
    "0-2": "An object that contains the fee amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/convenience-fee-object#fee-amount-child-object\" >Learn more about our payment_amount child object</a>.",
    "1-0": "tax_amount",
    "1-1": "`object`",
    "1-2": "An object that contains the tax amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/convenience-fee-object#tax-amount-child-object\" >Learn more about our payment_amount child object</a>.",
    "2-0": "additional_fee_amount",
    "2-1": "`object`",
    "2-2": "An object that contains the additional fee amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/convenience-fee-object#additional-fee-amount-child-object\" >Learn more about our payment_amount child object</a>.",
    "3-0": "maximum_fee_amount",
    "3-1": "`object`",
    "3-2": "An object that contains the maximum fee amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/convenience-fee-object#maximum-fee-amount-child-object\" >Learn more about our payment_amount child object</a>.",
    "4-0": "applicable_fee_amount",
    "4-1": "`object`",
    "4-2": "An object that contains the applicable fee amount details.  \n  \n<a href=\"https://developer.pluralonline.com/reference/convenience-fee-object#applicable-fee-amount-child-object\" >Learn more about our payment_amount child object</a>."
  },
  "cols": 3,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Fee Amount [Child Object]

The table below lists the various parameters in the `fee_amount` child object. This object is part of the `convenience_fee_breakdown` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value",
    "0-1": "`integer`",
    "0-2": "The transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
    "1-0": "currency",
    "1-1": "`string`",
    "1-2": "Type of currency.  \n  \nExample: `INR`"
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


### Tax Amount [Child Object]

The table below lists the various parameters in the `tax_amount` child object. This object is part of the `convenience_fee_breakdown` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value",
    "0-1": "`integer`",
    "0-2": "The transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
    "1-0": "currency",
    "1-1": "`string`",
    "1-2": "Type of currency.  \n  \nExample: `INR`"
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


### Additional Fee Amount [Child Object]

The table below lists the various parameters in the `additional_fee_amount` child object. This object is part of the `convenience_fee_breakdown` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value",
    "0-1": "`integer`",
    "0-2": "The transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
    "1-0": "currency",
    "1-1": "`string`",
    "1-2": "Type of currency.  \n  \nExample: `INR`"
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


### Maximum Fee Amount [Child Object]

The table below lists the various parameters in the `maximum_fee_amount` child object. This object is part of the `convenience_fee_breakdown` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value",
    "0-1": "`integer`",
    "0-2": "The transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
    "1-0": "currency",
    "1-1": "`string`",
    "1-2": "Type of currency.  \n  \nExample: `INR`"
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


### Applicable Fee Amount [Child Object]

The table below lists the various parameters in the `applicable_fee_amount` child object. This object is part of the `convenience_fee_breakdown` object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value",
    "0-1": "`integer`",
    "0-2": "The transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
    "1-0": "currency",
    "1-1": "`string`",
    "1-2": "Type of currency.  \n  \nExample: `INR`"
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


## Payable Amount [Child Object]

The table below lists the various parameters in the `payable_amount` child object. This object is part of the calculate convenience fee sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "value",
    "0-1": "`integer`",
    "0-2": "The transaction amount is Paisa.<ul><li>Minimum value: `100` (₹1)</li><li>Maximum value: `100000000` (₹10 lakh).</ul></li>Example: `100`",
    "1-0": "currency",
    "1-1": "`string`",
    "1-2": "Type of currency.  \n  \nExample: `INR`"
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


## Payment Method Metadata [Child Object]

The table below lists the various parameters in the `payment_method_metadata` child object. This object is part of the calculate convenience fee sample response object.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "network_type",
    "0-1": "`integer`",
    "0-2": "Type of network.  \n  \nExample: `MASTERCARD`",
    "1-0": "card_type",
    "1-1": "`string`",
    "1-2": "Type of card.  \n  \nExample: `DEBIT`"
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
