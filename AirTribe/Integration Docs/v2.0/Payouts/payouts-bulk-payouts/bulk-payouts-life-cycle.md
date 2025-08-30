---
title: "Life Cycle"
slug: "bulk-payouts-life-cycle"
excerpt: "Learn about the different status a Bulk Payout can have during its life cycle."
hidden: false
createdAt: "Wed Oct 09 2024 11:24:59 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Oct 10 2024 14:37:49 GMT+0000 (Coordinated Universal Time)"
---
The figure below shows the life cycle of a bulk payout.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2f58edbf03dbc5feea2e69bfff70d6fb7166257aab41b061075bf30cda3caafc-Group_1171279969.png",
        "",
        "Figure: Bulk Payout Life Cycle"
      ],
      "align": "center",
      "sizing": "200px",
      "caption": "Figure: Bulk Payout Life Cycle"
    }
  ]
}
[/block]


The table below list the various statuses of a bulk payout.

| Status    | Description                                                                                                                              |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| PENDING   | When the payout request is pending for processing. This status can be acquired when the payout account has insufficient account balance. |
| FAILED    | When the payout is failed.                                                                                                               |
| PROCESSED | When the payout is successfully processed.                                                                                               |
| REJECTED  | When the file is rejected. This can happen when the file contains unsafe characters (CSV injection)                                      |
