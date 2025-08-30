---
title: "Order"
slug: "affordability-suite-orders"
excerpt: "Learn how to integrate with Plural orders API."
hidden: false
createdAt: "Wed Jan 22 2025 17:52:00 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue Jan 28 2025 13:31:57 GMT+0000 (Coordinated Universal Time)"
---
Order is an important step in plural payment life cycle. An order contains the total order amount and the purchase details. 

To use Plural order APIs and connect them to payments, follow these steps:

1. **Create an Order**: Use the Plural `create order` API to generate an order ID. In response this API will provide you with an `order_id`.
2. **Link with Payment**: Once you have the `order_id`, use it to associate the order with the payment.

## Pre Authorization

In our orders API, we provide pre-authorization as an option. With pre-authorization set to true, you can capture payment for an order after successful delivery. 

When `pre-auth` is set to true, and the payment is successfully created, you have the following options:

1. **Capture Order**: Utilize the plural capture order API in your backend to capture the payment against an order.
2. **Cancel Order**: Use the plural cancel order API in your backend to cancel the payment against an order.

Plural orders APIs can be used to create an order and retrieve the details of an order.
