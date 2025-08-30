---
title: "Orders"
slug: "about-orders"
excerpt: "Learn how you can use Plural Orders."
hidden: false
createdAt: "Fri Sep 27 2024 06:29:27 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Oct 17 2024 15:11:14 GMT+0000 (Coordinated Universal Time)"
---
Order is a prerequisite step of the payment lifecycle at Plural. An order contains the total amount and the purchase details against an order. For every order, we generate a unique order ID. It ensures that each order can be identified, referenced, and accessed without confusion or ambiguity. This `order_id` must be used in our payments API to accept payment against an order.

Integrate our Orders API on your backend servers before initiating a payment. Our orders also support Pre-authorization as an option.

## Pre Authorization

In our orders API, we provide pre-authorization as an option. With pre-authorization set to true, you can capture or cancel a payment for an order. 

When `pre-auth` is set to true, and the payment is successfully created, you have the following options:

1. <a style="text-decoration:underline;" href="https://developer.pluralonline.com/v3.0/reference/orders-capture" target="_blank">Capture Order</a>: Utilize the plural capture order API in your backend to capture the payment against an order. You can only capture an order when the order status is `authorized`.
2. <a style="text-decoration:underline;" href="https://developer.pluralonline.com/v3.0/reference/orders-cancel" target="_blank">Cancel Order</a>: Use the plural cancel order API in your backend to cancel the payment against an order. You can only cancel an order when the order status is `authorized`.

Plural orders APIs can be used to create an order and retrieve the details of an order.

> 📘 Note:
> 
> - Currently, Pre-authorization is supported only for Cards and PayByPoints.
