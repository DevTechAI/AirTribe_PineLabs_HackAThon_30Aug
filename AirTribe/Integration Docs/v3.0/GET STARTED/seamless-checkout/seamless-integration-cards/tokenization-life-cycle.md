---
title: "Tokenization Life Cycle"
slug: "tokenization-life-cycle"
excerpt: "Learn about the different status of token."
hidden: true
createdAt: "Mon Feb 10 2025 09:18:47 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Feb 18 2025 10:04:30 GMT+0000 (Coordinated Universal Time)"
---
[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/90464c58c304422b4c187462acb9c605df89de7645796ee232efb2333eab38d7-Token_Management_3.jpg",
        "",
        "Figure: Token Management"
      ],
      "align": "center",
      "caption": "Figure: Token Management"
    }
  ]
}
[/block]


1. **Token**  
   The table below list the various statuses of token can have during its life cycle.

[block:parameters]
{
  "data": {
    "h-0": "Status",
    "h-1": "Description",
    "0-0": "`Initiated`",
    "0-1": "It's a token's initial state, indicating that Plural is working with token service providers to generate it.  \n`Note`: The token may take a few seconds to transition to the active state.",
    "1-0": "`Active`",
    "1-1": "It's a token's active state, achieved when the service_provider_token status is marked as active by the network token service providers.",
    "2-0": "`Suspended`",
    "2-1": "The token status changes to suspended when:  \n  \n•   The status is not active for any token service provider.  \n•   The token is marked as suspended by network token service providers.  \n  \n`Note`: A suspended token cannot be used for payment processing.",
    "3-0": "`Failed`",
    "3-1": "The token status changes to failed if it is marked as failed by all service providers.",
    "4-0": "`Deactivated`",
    "4-1": "Status will be deactivated when:  \n•\tStatus is not active or suspended for all the token service providers.  \n•\tStatus of the token is deactivated for at network token service providers.  \n  \n`Note`: A deactivated token cannot be used for payment processing."
  },
  "cols": 2,
  "rows": 5,
  "align": [
    "left",
    "left"
  ]
}
[/block]


2. **Service provider token. **

A service provider token will not have the `Initiated` state. This is because the service provider token is created only when a token is successfully created.

The table below list the various statuses of Service provider token can have during its life cycle.

[block:parameters]
{
  "data": {
    "h-0": "Status",
    "h-1": "Description",
    "0-0": "`Active`",
    "0-1": "The service_provider_token will have an active status once the token is successfully created by the token service providers (card networks). A service_provider_token in an active status can be used for payment processing.",
    "1-0": "`Suspended`",
    "1-1": "The service_provider_token status changes to suspended when the token is temporarily suspended by the network. The token may be reactivated by the token provider.  \n`Note`: A suspended token cannot be used for payment processing.",
    "2-0": "`Failed`",
    "2-1": "Plural failed to create the token with token service provider due to:  \n•\tThe card not being eligible.  \n•\tThe issue not being supported.  \n•\tAn invalid card number.",
    "3-0": "`Deactivated`",
    "3-1": "The service_provider_token status changes to deactivated for the following reasons:  \n  \n•    The service_provider_token has been deleted.  \n•    The service_provider_token has expired.  \n•    The service_provider_token has been deactivated by the bank.  \n  \nThe specific reason for deactivation is provided in the status_reason parameter, with possible values:  \n  \n•    Expired  \n•    Deactivated_by_bank  \n  \n`Note`: A deactivated token cannot be reactivated and cannot be used for payment processing."
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]
