---
title: "API Basics"
slug: "api-basics"
excerpt: "Overview of Plural APIs and their components."
hidden: true
createdAt: "Tue Jun 25 2024 06:26:19 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Wed Jun 26 2024 08:00:12 GMT+0000 (Coordinated Universal Time)"
---
Plural APIs are RESTful APIs. A RESTful API is an application programming interface that conforms to the constraints of REST architectural style and allows for interaction with RESTful web services. REST stands for "representational state transfer".

# What is an REST API?

APIs are mechanisms that enable two software components to communicate with each other using a set of definitions and protocols. An API consists of an API endpoint, HTTP method, parameters, and HTTP status codes.

## API endpoint

An API endpoint is the server URL that facilitates interaction between the client and servers.

```Text Example API Endpoint
https://uat.pinepg.in/api/v2/accept/payment
```

## HTTP Methods

HTTP defines a set of request methods such as GET, POST, PUT, PATCH, and DELETE to indicate the desired action for the given resource.

The table below list the methods most commonly used by Plural APIs.

| Method   | Description                                                                                 |
| :------- | :------------------------------------------------------------------------------------------ |
| `GET`    | Retrieve the specific resource for the given input. GET requests should only retrieve data. |
| `POST`   | Creates a new resource within the specified source.                                         |
| `PUT`    | Updates an existing resource with new request resource.                                     |
| `DELETE` | Deletes the specified resource.                                                             |
| `PATCH`  | Applies partial modification to the specified resource.                                     |

## Parameters

Parameters are the options you can send within the request to influence the response. There are four types of parameters.

**Path Parameters**: Path parameters are part of the endpoint and are mandatory parameters.

**Query Parameters**: Query parameters are also part of the endpoint that appears after the question mark (?) in the endpoint. Each query parameters are separated using an ampersand (&) within them.

**Request Parameters**: Request parameters are included in the request body and are used to send data through an API.

**Response Parameters**: Response parameters represents the response to a request.

## HTTPS Status Codes

HTTP response status codes indicates weather a specific HTTP request is successfully completed. Responses are grouped into five classes.

1. Informational Responses (100-199)
2. Successful Responses (200-299)
3. Redirection Messages (300-399)
4. Client Error Responses (400-499)
5. Server Error Responses (500-599)

To know more about status codes refer to <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Status" target="_blank">Mozilla docs</a>.
