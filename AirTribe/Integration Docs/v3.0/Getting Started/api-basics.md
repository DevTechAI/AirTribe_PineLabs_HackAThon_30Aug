---
title: "API Basics"
slug: "api-basics"
excerpt: "Overview of Plural APIs and their components."
hidden: false
createdAt: "Tue Jun 25 2024 06:26:19 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Thu Oct 17 2024 15:13:16 GMT+0000 (Coordinated Universal Time)"
---
Plural APIs are RESTful APIs. A RESTful API is an application programming interface that confirms to the constraints of REST architectural style and allows for interaction with RESTful web services. REST stands for "representational state transfer".

# What is an REST API?

APIs are mechanisms that enable two software components to communicate with each other using a set of definitions and protocols. An API consists of an API endpoint, HTTP method, parameters, headers and HTTP status codes.

## API endpoint

An API endpoint is the server URL that facilitates interaction between the client and servers.

```Text Example API Endpoint
https://pluraluat.v2.pinepg.in/api/pay/v1
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

## HTTP Headers

HTTP headers are crucial in shaping server and client behavior throughout the request and response process. The client sends request headers to the server, containing information and instructions about the requested resource. In return, the server sends response headers to the client, providing metadata, instructions, and additional details about the response.

### Request Headers

Request headers are part of an HTTP request which includes information about the request to the server. This information helps the server to customize the response to the request. You can include the following request headers with your API request:

- `Content-Type`
- `Authorization`
- `Request-Timestamp`
- `Request-ID`

[block:parameters]
{
  "data": {
    "h-0": "Header",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "Content-Type",
    "0-1": "`string`",
    "0-2": "The type of content included in the HTTP message body.  \n  \nAccepted value: `application/json`",
    "1-0": "Authorization",
    "1-1": "`string`",
    "1-2": "The HTTP header where you can include your secret token for authentication.  \n  \nExample: `Bearer <access_token>`  \n  \n**Note**: Use the access token generated using our <a href=\"https://developer.pluralonline.com/v3.0/reference/generate-token\" target=\"_blank\">Generate Token API</a>.",
    "2-0": "Request-Timestamp",
    "2-1": "`string`",
    "2-2": "Use ISO 8601 UTC Timestamp, to create a timestamp when the generate token is requested.  \n  \nExample: `2024-07-09T07:57:08.022056Z`",
    "3-0": "Request-ID",
    "3-1": "`string`",
    "3-2": "Use a global unique identifier [GUID] for the request.<ul><li>Minimum: 1 characters.</li><li>Maximum: 50 characters.</ul></li>Example: `c17ce30f-f88e-4f81-ada1-c3b4909ed235`"
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


### Response Headers

Response headers are text-based components sent with an HTTP response that provide details about the response sent or instructions on how the client should handle it. You will receive the following response headers along with the API response.

- `Strict-Transport-Security`
- `X-Content-Type-Options`
- `Content-Security-Policy`
- `Cache-Control`

[block:parameters]
{
  "data": {
    "h-0": "Header",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "Strict-Transport-Security",
    "0-1": "`string`",
    "0-2": "This header ensures that a browser connects to a website using HTTPS, and not HTTP.  \n  \nExample: `max-age=31536000; includeSubDomains; preload`",
    "1-0": "X-Content-Type-Options",
    "1-1": "`string`",
    "1-2": "Security feature that tells browsers to follow the MIME types declared in the Content-Type headers, instead of guessing them.  \n  \nExample: `nosniff`",
    "2-0": "Content-Security-Policy",
    "2-1": "`string`",
    "2-2": "Helps to protect websites from attacks by limiting which resources can be loaded on a page.  \n  \nExample: `default-src 'self'; script-src 'self'; img-src 'self';`",
    "3-0": "Cache-Control",
    "3-1": "`string`",
    "3-2": "Controls how a browser caches resources and when to send requests to a server for fresh resources.  \n  \nExample: `no-store, no-cache`"
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


## HTTPS Status Codes

HTTP response status codes indicates weather a specific HTTP request is successfully completed. Responses are grouped into five classes.

1. Informational Responses (100-199)
2. Successful Responses (200-299)
3. Redirection Messages (300-399)
4. Client Error Responses (400-499)
5. Server Error Responses (500-599)

To know more about status codes refer to <a style="text-decoration:underline;" href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Status" target="_blank">Mozilla docs</a>.
