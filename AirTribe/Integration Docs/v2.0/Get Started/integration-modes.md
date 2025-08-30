---
title: "Integration Modes"
slug: "integration-modes"
excerpt: "Introduction to types of integrations available"
hidden: true
createdAt: "Sun Sep 19 2021 09:05:05 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jun 25 2024 10:58:24 GMT+0000 (Coordinated Universal Time)"
---
Merchant can integrate in the following three modes.

1. Seamless
2. iFrame
3. Redirect

## Seamless

If a merchant is [PCI DSS compliant](https://www.pcisecuritystandards.org/pci_security/maintaining_payment_security) then they can integrate in the seamless mode. In this mode a merchant can accept card instrument details on their own website and call Plural's APIs in S2S mode.

## iFrame

For merchants who are not [PCI DSS compliant,](https://www.pcisecuritystandards.org/pci_security/maintaining_payment_security) iFrame mode is the right choice. The iFrame checkout screen comes up as a seamless pop-up on the merchant website (as shown below) giving the user a good payment experience.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/0657933-Screenshot_2021-09-15_at_8.47.35_AM.png",
        "Screenshot 2021-09-15 at 8.47.35 AM.png",
        2870
      ],
      "align": "center",
      "caption": "iFrame Checkout"
    }
  ]
}
[/block]
