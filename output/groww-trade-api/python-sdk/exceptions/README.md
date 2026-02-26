---
source: https://groww.in/trade-api/docs/python-sdk/exceptions
scraped: true
---
[](https://groww.in/)[![Groww Logo](https://groww.in/favicon32x32-groww.ico)Groww API](https://groww.in/trade-api)
[](https://groww.in/)[![Groww Logo](https://groww.in/favicon32x32-groww.ico)Groww API](https://groww.in/trade-api)
Python SDK Docs
Documentation for Python SDK
`⌘``K`
[Documentation](https://groww.in/trade-api/docs)
[Introduction](https://groww.in/trade-api/docs/python-sdk)[Instruments](https://groww.in/trade-api/docs/python-sdk/instruments)[Orders](https://groww.in/trade-api/docs/python-sdk/orders)[Smart Orders](https://groww.in/trade-api/docs/python-sdk/smart-orders)[Portfolio](https://groww.in/trade-api/docs/python-sdk/portfolio)[Margin](https://groww.in/trade-api/docs/python-sdk/margin)[Live Data](https://groww.in/trade-api/docs/python-sdk/live-data)[Historical Data](https://groww.in/trade-api/docs/python-sdk/historical-data)[Backtesting](https://groww.in/trade-api/docs/python-sdk/backtesting)[Feed](https://groww.in/trade-api/docs/python-sdk/feed)[User](https://groww.in/trade-api/docs/python-sdk/user)[Annexures](https://groww.in/trade-api/docs/python-sdk/annexures)[Exceptions](https://groww.in/trade-api/docs/python-sdk/exceptions)[Changelog](https://groww.in/trade-api/docs/python-sdk/changelog)
GrowwBaseException
# Exceptions
The SDK provides custom exceptions to handle various error scenarios.
Below are the custom exceptions and their business context. These exceptions are located in the `growwapi.groww.exceptions` module.
## [GrowwBaseException](https://groww.in/trade-api/docs/python-sdk/exceptions#growwbaseexception)
This is the base class for all exceptions in the Groww SDK. It captures the general error message.
Expect this exception as a generic catch-all for errors that do not fall into more specific categories.
**Attributes:**
  * `msg` (str): The error message associated with the exception.

## [GrowwAPIException](https://groww.in/trade-api/docs/python-sdk/exceptions#growwapiexception)
This exception is raised for client-related errors, such as invalid requests or authentication failures.
Expect this exception to handle errors related to client-side issues, such as invalid API keys or malformed requests.
**Attributes:**
  * `msg` (str): The error message.
  * `code` (str): The error code.

### [GrowwAPIAuthenticationException](https://groww.in/trade-api/docs/python-sdk/exceptions#growwapiauthenticationexception)
This exception is raised when authentication with the Groww API fails.
Expect this exception to handle scenarios where the SDK fails to authenticate with the Groww API, indicating issues with the API key or authentication process.
**Attributes:**
  * `msg` (str): The error message.
  * `code` (str): The error code.

### [GrowwAPIAuthorisationException](https://groww.in/trade-api/docs/python-sdk/exceptions#growwapiauthorisationexception)
This exception is raised when authorization with the Groww API fails.
Expect this exception to handle scenarios where the SDK fails to authorize with the Groww API, indicating issues with the API key or access permissions.
**Attributes:**
  * `msg` (str): The error message.
  * `code` (str): The error code.

### [GrowwAPIBadRequestException](https://groww.in/trade-api/docs/python-sdk/exceptions#growwapibadrequestexception)
This exception is raised when a bad request is made to the Groww API.
Expect this exception to handle scenarios where the SDK sends a malformed request to the API, indicating issues with the request payload or parameters.
**Attributes:**
  * `msg` (str): The error message.
  * `code` (str): The error code.

### [GrowwAPINotFoundException](https://groww.in/trade-api/docs/python-sdk/exceptions#growwapinotfoundexception)
This exception is raised when the requested resource is not found on the Groww API.
Expect this exception to handle scenarios where the SDK requests a resource that does not exist, indicating a logical error in the code or an outdated reference.
**Attributes:**
  * `msg` (str): The error message.
  * `code` (str): The error code.

### [GrowwAPIRateLimitException](https://groww.in/trade-api/docs/python-sdk/exceptions#growwapiratelimitexception)
This exception is raised when the rate limit for the Groww API is exceeded.
Expect this exception to handle scenarios where the SDK makes too many requests to the API within a short period, indicating a need to throttle the request rate.
**Attributes:**
  * `msg` (str): The error message.
  * `code` (str): The error code.

### [GrowwAPITimeoutException](https://groww.in/trade-api/docs/python-sdk/exceptions#growwapitimeoutexception)
This exception is raised when a request to the Groww API times out.
Expect this exception to handle scenarios where the API request takes too long to respond, indicating potential network issues or server overload.
**Attributes:**
  * `msg` (str): The error message.
  * `code` (str): The error code.

## [GrowwFeedException](https://groww.in/trade-api/docs/python-sdk/exceptions#growwfeedexception)
This exception is raised for errors related to the Groww feed.
Expect this exception to handle errors related to the feed, such as connection issues or subscription failures.
**Attributes:**
  * `msg` (str): The error message.

## [GrowwFeedConnectionException](https://groww.in/trade-api/docs/python-sdk/exceptions#growwfeedconnectionexception)
This exception is raised when a connection to the Groww feed fails.
Expect this exception to handle errors related to establishing or maintaining a connection to the Groww feed, which is crucial for receiving live market data and updates.
**Attributes:**
  * `msg` (str): The error message.

## [GrowwFeedNotSubscribedException](https://groww.in/trade-api/docs/python-sdk/exceptions#growwfeednotsubscribedexception)
This exception is raised when trying to access data from a feed that has not been subscribed to. A subscription is required to receive data from the feed.
Expect this exception to handle scenarios where the SDK attempts to retrieve data from a feed that has not been subscribed to, indicating a logical error in the code.
**Attributes:**
  * `msg` (str): The error message.
  * `topic` (str): The topic that must be subscribed to receive messages.

[Previous Annexures](https://groww.in/trade-api/docs/python-sdk/annexures)[Next Changelog](https://groww.in/trade-api/docs/python-sdk/changelog)
[GrowwBaseException](https://groww.in/trade-api/docs/python-sdk/exceptions#growwbaseexception)[GrowwAPIException](https://groww.in/trade-api/docs/python-sdk/exceptions#growwapiexception)[GrowwFeedException](https://groww.in/trade-api/docs/python-sdk/exceptions#growwfeedexception)[GrowwFeedConnectionException](https://groww.in/trade-api/docs/python-sdk/exceptions#growwfeedconnectionexception)[GrowwFeedNotSubscribedException](https://groww.in/trade-api/docs/python-sdk/exceptions#growwfeednotsubscribedexception)

