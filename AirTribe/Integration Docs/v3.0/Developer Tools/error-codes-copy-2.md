---
title: "Error Codes"
slug: "error-codes-copy-2"
excerpt: "Learn about the HTTP error responses returned from Plural APIs."
hidden: true
createdAt: "Mon May 05 2025 08:31:45 GMT+0000 (Coordinated Universal Time)"
updatedAt: "Tue May 06 2025 07:11:03 GMT+0000 (Coordinated Universal Time)"
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

The table below gives a brief description of the various parameters returned in the error message with all non-2XX HTTP status codes.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Type",
    "h-2": "Description",
    "0-0": "code",
    "0-1": "`string`",
    "0-2": "Short code for the error returned.  \n  \nPossible values:<ul><li>`INVALID_REQUEST`</li><li>`PAYMENT_RATE_LIMIT`</li><li>`CARD_EXPIRED`</li><li>`RISK_CHECK_FAILED`</li><li>`INTERNAL_ERROR`</ul></li>",
    "1-0": "message",
    "1-1": "`string`",
    "1-2": "Corresponding error message for the code.  \n  \nExample: `Amount must be an Integer value greater than or equal to 1`"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


Shown below are the sample error response for 400 HTTP status code.

```json 400 - INVALID_REQUEST
{
  "code": "INVALID_REQUEST",
  "message": "Amount must be an Integer value greater than or equal to 1"
}
```
```json 400 - INVALID_REQUEST
{
  "code": "INVALID_REQUEST",
  "message": "Amount must be an Integer value less than or equal to 100000000"
}
```
```json 400 - INVALID_REQUEST
{
  "code": "INVALID_REQUEST",
  "message": "Merchant Order Reference must not be empty"
}
```
```json 400 - INVALID_REQUEST
{
  "code": "INVALID_REQUEST",
  "message": "Merchant Order Reference must be less than or equal to 50 characters"
}
```
```json 400 - INVALID_REQUEST
{
  "code": "INVALID_REQUEST",
  "message": "Payment method is missing/invalid"
}
```
```json 400-INVALID_REQUEST
{
  "code": "INVALID_REQUEST",
  "message": "No matching records found for the inquiry"
}
```

Shown below are the sample error response for 401 HTTP status code.

```json 401 - Authentication Error
{
  "code":"UNAUTHORIZED",
  "message":"Unauthorized"
}
```

Shown below are the sample error response for 422 HTTP status code.

```json 422 - PAYMENT_RATE_LIMIT
{
  "code": "PAYMENT_RATE_LIMIT",
  "message": "Failure due to request velocity or limit checks"
}
```
```json 422 - CARD_EXPIRED
{
  "code": "CARD_EXPIRED",
  "message": "Payment Instrument has expired"
}
```
```json 422 - CARD_VERIFICATION_FAILED
{
  "code": "CARD_VERIFICATION_FAILED",
  "message": "Invalid CVV specified on the card payment option"
}
```
```json 422 - CARD_STOLEN
{
  "code": "CARD_STOLEN",
  "message": "Specified card is not allowed for this transaction because it was flagged as stolen."
}
```
```json 422 - CARD_NOT_ENROLLED
{
  "code": "CARD_NOT_ENROLLED",
  "message": "Specified card is not allowed for this transaction because it is not enrolled for 3DS"
}
```
```json 422 - CARD_LOST
{
  "code": "CARD_LOST",
  "message": "Specified card is not allowed for this transaction because it was flagged as lost."
}
```
```json 422 - RISK_CHECK_FAILED
{
  "code": "RISK_CHECK_FAILED",
  "message": "Payment Instrument suspected to be used fraudulently"
}
```
```json 422 - PAYMENT_METHOD_NOT_ENABLED
{
  "code": "PAYMENT_METHOD_NOT_ENABLED",
  "message": "The specified payment method is not enabled for the merchant"
}
```
```json 422 - OPERATION_NOT_ALLOWED
{
  "code": "OPERATION_NOT_ALLOWED",
  "message": "The specified operation cannot be made because required precondition has failed"
}
```
```json 422 - ORDER_NOT_FOUND
{
  "code": "ORDER_NOT_FOUND",
  "message": "No order with specified order-id exists in the system"
}
```
```json 422 - PAYMENT_NOT_AUTHORIZED
{
  "code": "PAYMENT_NOT_AUTHORIZED",
  "message": "The payment requires authorization before it can be processed"
}
```
```json 422 - DUPLICATE_REQUEST
{
  "code": "DUPLICATE_REQUEST",
  "message": "The request has already been processed"
}
```

Shown below are the sample error response for 429 HTTP status code.

```json 429 - PAYMENT_RATE_LIMIT
{
  "code": "PAYMENT_RATE_LIMIT",
  "message": "The payment was declined because too many payments were attempted using the specified payment option"
}
```
```json 429 - PAYMENT_RATE_LIMIT
{
  "code": "PAYMENT_RATE_LIMIT",
  "message": "Failure due to request velocity or limit checks"
}
```
```json 429 - API_RATE_LIMIT
{
  "code": "API_RATE_LIMIT",
  "message": "The request was rejected because the client has sent too many requests in a given time window"
}
```

Shown below are the sample error response for 500 HTTP status code.

```json 500 - INTERNAL_ERROR
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Server Error"
}
```
```json 500 - INTERNAL_ERROR
{
    "code": "INTERNAL_ERROR",
    "message": "Payment processor is unavailable"
}
```
```json 500 - INTERNAL_ERROR
{
  "code": "INTERNAL_ERROR",
  "message": "Internal Technical Issue related to certificate, encryption or signing"
}
```
```json 500-UNKNOWN_ERROR
{
  "code": "UNKNOWN_ERROR",
  "message": "Failure due to Unknown reason"
}
```

Shown below are the sample error response for 504 HTTP status code.

```json 504 - INVALID_USER_ACCOUNT
{
  "code": "INVALID_USER_ACCOUNT",
  "message": "Relevant User Account not active/valid"
}
```
```json 504 - TIMED_OUT
{
    "code": "TIMED_OUT",
    "message": "The request timed out. Please try again later"
}
```

### Common Error Codes

The below table lists all the possible error codes returned in our API responses.

| Status Code | Error Code                   | Error Category  | Error Description                                                                                                                        |
| :---------- | :--------------------------- | :-------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| 500         | `INTERNAL_ERROR`             | `system`        | Internal server error. The request cannot be processed at this time.                                                                     |
| 500         | `INTERNAL_ERROR`             | `system`        | Internal Technical Issue related to certificate, encryption or signing.                                                                  |
| 500         | `UNKNOWN_ERROR`              | `system`        | Failure due to Unknown reason.                                                                                                           |
| 429         | `API_RATE_LIMIT`             | `system`        | The request was rejected because the client has sent too many requests in a given time window.                                           |
| 504         | `TIMED_OUT`                  | `system`        | The request timed out. Please try again later.                                                                                           |
| 504         | `INVALID_USER_ACCOUNT`       | `system`        | Relevant User Account not active/valid.                                                                                                  |
| 400         | `INVALID_REQUEST`            | `request`       | The request does not the expected contract and cannot be processed. This may be due to malformed request, invalid or missing parameters. |
| 400         | `INVALID_REQUEST`            | `request`       | No matching records found for the inquiry.                                                                                               |
| 422         | `INVALID_REQUEST`            | `request`       | Routing Error.                                                                                                                           |
| 422         | `INVALID_REQUEST`            | `request`       | Invalid Request Parameters.                                                                                                              |
| 422         | `DUPLICATE_REQUEST`          | `request`       | The request has already been processed.                                                                                                  |
| 422         | `API_RATE_LIMIT`             | `request`       | The request was rejected because the client has sent too many requests in a given time window.                                           |
| 429         | `PAYMENT_RATE_LIMIT`         | `request`       | Failure due to request velocity or limit checks.                                                                                         |
| 422         | `PAYMENT_METHOD_NOT_ENABLED` | `validation`    | The specified payment method is not enabled for the merchant.                                                                            |
| 422         | `OPERATION_NOT_ALLOWED`      | `validation`    | The specified operation cannot be made because required precondition has failed.                                                         |
| 404         | `ORDER_NOT_FOUND`            | `validation`    | No order with specified order-id exists in the system.                                                                                   |
| 422         | `ORDER_CANCELLED`            | `validation`    | The order has already been cancelled and cannot be modified further.                                                                     |
| 422         | `INVALID_USER_ACCOUNT`       | `validation`    | Relevant User Account not active/valid.                                                                                                  |
| 422         | `USER_AUTHENTICATION_FAILED` | `validation`    | Consumer Authentication failed.                                                                                                          |
| 422         | `CARD_LOST`                  | `validation`    | Payment Instrument is reported as lost.                                                                                                  |
| 422         | `INSUFFICIENT_FUNDS`         | `validation`    | Insufficient Funds.                                                                                                                      |
| 422         | `AMOUNT_LIMIT_EXCEEDED`      | `validation`    | Amount exceeds allowed limit.                                                                                                            |
| 422         | `CARD_NOT_ALLOWED`           | `validation`    | Payment Instrument is reported as picked up.                                                                                             |
| 422         | `ISSUER_NOT_SUPPORTED`       | `validation`    | Issuer not supported.                                                                                                                    |
| 422         | `DUPLICATE_REQUEST`          | `validation`    | Duplicate Transaction.                                                                                                                   |
| 422         | `RISK_CHECK_FAILED`          | `validation`    | Payment Instrument suspected to be used fraudulently.                                                                                    |
| 422         | `PAYMENT_NOT_AUTHORIZED`     | `payment error` | The payment requires authorization before it can be processed.                                                                           |
| 422         | `PAYMENT_PENDING`            | `payment error` | The payment is pending and requires authorization before it can be processed.                                                            |
| 422         | `PAYMENT_EXPIRED`            | `payment error` | The payment has expired and cannot be modified further.                                                                                  |
| 422         | `PAYMENT_DECLINED`           | `payment error` | The payment was declined by the acquirer.                                                                                                |
| 429         | `PAYMENT_RATE_LIMIT`         | `payment error` | The payment was declined because too many payments were attempted using the specified payment option.                                    |
| 429         | `PAYMENT_RATE_LIMIT`         | `payment error` | Failure due to request velocity or limit checks                                                                                          |
| 422         | `RISK_CHECK_FAILED`          | `instrument`    | The payment was declined after a risk check.                                                                                             |
| 422         | `ISSUER_NOT_SUPPORTED`       | `instrument`    | The specified issuer is not supported for this operation.                                                                                |
| 422         | `INSUFFICIENT_FUNDS`         | `instrument`    | Insufficient funds to proceed with payment using the specified payment option.                                                           |
| 422         | `AMOUNT_LIMIT_EXCEEDED`      | `instrument`    | The transaction was declined because the specified amount exceeds allowed limits.                                                        |
| 422         | `CARD_VERIFICATION_FAILED`   | `card`          | Invalid CVV specified on the card payment option.                                                                                        |
| 422         | `CARD_NOT_ALLOWED`           | `card`          | Specified card is not allowed for this transaction.                                                                                      |
| 422         | `CARD_STOLEN`                | `card`          | Specified card is not allowed for this transaction because it was flagged as stolen.                                                     |
| 422         | `CARD_LOST`                  | `card`          | Specified card is not allowed for this transaction because it was flagged as lost.                                                       |
| 422         | `CARD_EXPIRED`               | `card`          | Specified card is not allowed for this transaction because it has expired.                                                               |
| 422         | `CARD_NOT_ENROLLED`          | `card`          | Specified card is not allowed for this transaction because it is not enrolled for 3DS                                                    |

> 📘 Note:
> 
> - For the unstructured error returned from Plural, the response may not always include a corresponding code and message. In such cases, refer to the HTTP status codes to determine the status of the API request.
