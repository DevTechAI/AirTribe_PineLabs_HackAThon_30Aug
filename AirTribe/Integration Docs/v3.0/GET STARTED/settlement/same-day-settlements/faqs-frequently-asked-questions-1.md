---
title: "FAQs (Frequently Asked Questions)"
slug: "faqs-frequently-asked-questions-1"
excerpt: "Refer to frequently asked questions and answers about Same Day Settlements."
hidden: true
createdAt: "Tue Mar 25 2025 07:02:56 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Mar 25 2025 08:10:46 GMT+0000 (Coordinated Universal Time)"
---
<details><summary><b>1. How is it handled when payouts exceed the pre-funding amount for a specific batch?</b></summary><br>Pre-funding/funding is not specific to a batch or merchant.</details>

<details><summary><b>2. What error is given (if any), and how can these cases be identified?</b></summary><br>Timely communication is sent to stakeholders when such delays occur.</details>

<details><summary><b>3. Are merchants informed about such cases reactively?</b></summary><br>Delays due to fund unavailability are proactively communicated to Pine Labs stakeholders. For unprocessed transaction-related delays, a BAU (Business As Usual) is raised to the CCM (Customer Care Manager) for initial analysis at T+1 after receiving the MPR (Merchant Payment Report) and reconciliation. <br>This BAU is assigned to the relevant stakeholder by the CCM for resolution. The product team should provide an automated SDS (Same Day Settlement) unprocessed report after each SDS batch, marking all stakeholders on the email. This ensures proper action is taken by the action owner, and delay notifications are sent to merchants through the support team.</details>

<details><summary><b>4. When are transactions settled if SDS pre-funding is exhausted?</b></summary><br>Such batches are settled on the next working day once pre-funding/funding is replenished through bank settlement at T+1/next working day. The product team should address this issue by allowing partial settlement of funds to merchants up to the available pre-funding amount, instead of impacting the entire batch for the next day.</details>

<details><summary><b>5. How much funds are allocated specifically for Same Day Settlements?</b></summary><br>Funds are parked in a common pool, making it impossible to track their use specifically.</details>

<details><summary><b>6. When is the SDS MPR report shared, and with whom? Is this report specifically for SDS, as requested by the merchant?</b></summary><br>The system automatically generates and shares this MPR with merchants whenever a batch is created and payouts are initiated (applicable for all three nodals).<br> A consolidated MPR is shared again automatically by EoD for all five batches (for RBL and HDFC, containing UTR info).<br> For AXIS, the setops team uploads it on the SFTP (as mentioned in the SOP around 7-7:30), which the RPA team uses to share the info with the end merchant.</details>

<details><summary><b>7. How can RM/Sales access the same-day settlement data dump along with the associated amount?</b></summary><br>RM/Sales should be able to access this data after the 5th batch, including both the total amount and the dump. This information should be automatically triggered and sent to the merchant utilizing SDS. <br>After the 5th batch, a consolidated MPR is generated (for HDFC and RBL), containing all the mentioned data. It should be available on the SFTP for all three nodals (specifically for AXIS UTR and data dump, you can refer to the SFTP).</details>
