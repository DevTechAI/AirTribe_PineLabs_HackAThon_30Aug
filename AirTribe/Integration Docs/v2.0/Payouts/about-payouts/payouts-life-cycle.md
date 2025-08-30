---
title: "Life Cycle"
slug: "payouts-life-cycle"
excerpt: "Learn about the different status a Payout can have during its life cycle."
hidden: false
createdAt: "Fri Oct 04 2024 07:03:39 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Oct 10 2024 14:36:47 GMT+0000 (Coordinated Universal Time)"
---
The figure below shows the life cycle of Payouts.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/a3ff1f867bf5f980e9b5b66fde109eed7d18239b6408d97eb8d913fde8c3e1b0-Group_1171279962.png",
        "",
        "Figure: Payouts Life Cycle"
      ],
      "align": "center",
      "sizing": "700px",
      "caption": "Figure: Payouts Life Cycle"
    }
  ]
}
[/block]


The table below list the various statuses of a payout.

| Status     | Description                                                                                                                              |
| :--------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| CREATED    | When Plural receive the payout request.                                                                                                  |
| SCHEDULED  | When you create a schedule payout request successfully.                                                                                  |
| CANCELED   | When you canceled a schedule payout.                                                                                                     |
| PENDING    | When the payout request is pending for processing. This status can be acquired when the payout account has insufficient account balance. |
| PROCESSING | When we receive the response from the acquirer bank for the payout created.                                                              |
| PROCESSED  | When the payout is successfully processed.                                                                                               |
| SUCCESS    | When the payout is successful. The money is debit from your payout account and credited to your beneficiary bank account.                |
| FAILED     | When the payout is failed.                                                                                                               |
