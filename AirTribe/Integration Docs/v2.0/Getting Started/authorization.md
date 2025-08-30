---
title: "Authorization"
slug: "authorization"
excerpt: "Learn about the type of authorization used by us and how to generate your authorization keys."
hidden: true
createdAt: "Wed Jun 26 2024 07:56:39 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Mon Aug 12 2024 08:57:21 GMT+0000 (Coordinated Universal Time)"
---
When processing an API, it is important to know who is sending the request and if they have permission to perform the action. API Authorization helps us identify who is making the call, if they have the required permissions, and ensure you securely access the requested data.

Plural uses bearer tokens to authorize our API calls. All API calls must include an authorization header in the request.

> 📘 API Calls via Server Only
> 
> - All API calls should be requested from your backend server only.
> - Any API call made from an application frontend is rejected.

## Generate Keys

Use our Token API to generate a token which can be used to authenticate all the Plural APIs.

Use the below endpoint to generate a token.

```text Generate Token UAT Endpoint

```
```text Generate Token Prod Endpoint

```

Shown below is a sample request and sample response for a Generate Token API.

```json Sample Request
{
  "client_id": "123456",
  "client_secret": "fasdfghgwei7egyhuggwp39w8rh",
  "grant_type": "CLIENT_CREDENTIALS"
}
```
```json Sample Response
{
  "access_token": "wesrdtfyguhijnomkjuih8yg67ttgasdy",
  "token_type": "BEARER",
  "expires_in": 3600
}
```
