---
title: "Error Codes (COPY)"
slug: "error-codes-copy"
excerpt: "Learn about the HTTP error responses returned from Plural APIs."
hidden: true
createdAt: "Fri Jul 26 2024 12:18:44 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Fri Jul 26 2024 12:18:44 GMT+0000 (Coordinated Universal Time)"
---
Plural aims to process all the API requests successfully to provide the optimal user experience. Each API request can either return a successful response or a failed response. Successful API responses are indicated by an HTTP status code in the 2XX range. Any status code outside of the 2XX range signifies a failed request. Common reasons for API call failures include human input errors, network issues, and intermittent connectivity problems.

The error response helps to:

- Identify and examine the causes of failure.
- Identifying measures to resolve the unsuccessful response.

The table below lists the various HTTP response codes we return to indicate successful or failed API calls.

[block:parameters]
{
  "data": {
    "h-0": "HTTP Status Code",
    "h-1": "Description",
    "h-2": "Next Step",
    "0-0": "2XX",
    "0-1": "Successful API request.",
    "0-2": "",
    "1-0": "4XX",
    "1-1": "Failed API Request.  \n  \nThis is because of the error in the information provided by you.  \n  \nExample: <ul><li>`Bad request`</li><li>`Invalid path`</li><li>`Invalid method`",
    "1-2": "When these error messages are returned check and correct the information passed in the API request.",
    "2-0": "5XX",
    "2-1": "Failed API request.  \n  \nThis is returned when:<ul><li>Plural server return errors.</li><li>Plural service provider's system error.",
    "2-2": "Try after some time."
  },
  "cols": 3,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Error Structure

The error response contains the `code` and `message` parameters in the error response. These parameters helps to identify reasons for the error.

Shown below are the sample error response for different non 2XX HTTP status code.

```json 401 Authentication Error
{
    "message": "Unauthorized"
}
```
```json 422 Invalid Request Error
{
    "code": "DUPLICATE_REQUEST",
    "message": "Duplicate Merchant Reference ID received"
}
```

### Common Error Codes

The below table lists all the possible error codes returned in our API responses.

| Error Code                     | Error Category  | Error Description                                                                                                                        |
| :----------------------------- | :-------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| `INTERNAL_ERROR`               | `system`        | Internal server error. The request cannot be processed at this time.                                                                     |
| `INVALID_REQUEST`              | `request`       | The request does not the expected contract and cannot be processed. This may be due to malformed request, invalid or missing parameters. |
| `UNAUTHORIZED`                 | `request`       | The client is not authorized to perform this operation.                                                                                  |
| `DUPLICATE_REQUEST`            | `request`       | The request has already been processed.                                                                                                  |
| `API_RATE_LIMIT`               | `request`       | The request was rejected because the client has sent too many requests in a given time window.                                           |
| `PAYMENT_METHOD_NOT_ENABLED`   | `validation`    | The specified payment method is not enabled for the merchant.                                                                            |
| `OPERATION_NOT_ALLOWED`        | `validation`    | The specified operation cannot be made because required precondition has failed.                                                         |
| `ORDER_NOT_FOUND`              | `validation`    | No order with specified order-id exists in the system.                                                                                   |
| `ORDER_CANCELLED`              | `validation`    | The order has already been cancelled and cannot be modified further.                                                                     |
| `PAYMENT_NOT_AUTHORIZED`       | `payment error` | The payment requires authorization before it can be processed.                                                                           |
| `PAYMENT_PENDING`              | `payment error` | The payment is pending and requires authorization before it can be processed.                                                            |
| `PAYMENT_EXPIRED`              | `payment error` | The payment has expired and cannot be modified further.                                                                                  |
| `PAYMENT_DECLINED`             | `payment error` | The payment was declined by the acquirer.                                                                                                |
| `PAYMENT_RATE_LIMIT`           | `payment error` | The payment was declined because too many payments were attempted using the specified payment option.                                    |
| `INVALID_INSTRUMENT`           | `instrument`    | The payment instrument details are not valid.                                                                                            |
| `RISK_CHECK_FAILED`            | `instrument`    | The payment was declined after a risk check.                                                                                             |
| `ISSUER_NOT_SUPPORTED`         | `instrument`    | The specified issuer is not supported for this operation.                                                                                |
| `INSUFFICIENT_FUNDS`           | `instrument`    | Insufficient funds to proceed with payment using the specified payment option.                                                           |
| `AMOUNT_LIMIT_EXCEEDED`        | `instrument`    | The transaction was declined because the specified amount exceeds allowed limits.                                                        |
| `INVALID_CARDHOLDER`           | `card`          | Invalid card holder specified on the card payment option.                                                                                |
| `CARD_VERIFICATION_FAILED`     | `card`          | Invalid CVV specified on the card payment option.                                                                                        |
| `CARD_NOT_ALLOWED`             | `card`          | Specified card is not allowed for this transaction.                                                                                      |
| `CARD_STOLEN`                  | `card`          | Specified card is not allowed for this transaction because it was flagged as stolen.                                                     |
| `CARD_LOST`                    | `card`          | Specified card is not allowed for this transaction because it was flagged as lost.                                                       |
| `CARD_EXPIRED`                 | `card`          | Specified card is not allowed for this transaction because it has expired.                                                               |
| `CARD_NOT_ENROLLED`            | `card`          | Specified card is not allowed for this transaction because it is not enrolled for 3DS                                                    |
| `UNKNOWN_ERROR`                | `misc`          | Unknown error. The request cannot be processed at this time.                                                                             |
| `HOTLISTED_USER`               | `misc`          | The user is not eligible for relevant transaction.                                                                                       |
| `INVALID_USER_ACCOUNT`         | `misc`          | The user account is not eligible for relevant transaction.                                                                               |
| `USER_AUTHENTICATION_REQUIRED` | `misc`          | User authentication has failed.                                                                                                          |
| `USER_AUTHENTICATION_FAILED`   | `misc`          | User authentication has failed.                                                                                                          |
| `TIMED_OUT`                    | `misc`          | The request has timed out.                                                                                                               |
