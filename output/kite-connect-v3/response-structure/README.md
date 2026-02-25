---
source: https://kite.trade/docs/connect/v3/response-structure/
scraped: true
---
Response structure
 Kite Connect 3 / API documentation

# Response structure[¶](https://kite.trade/docs/connect/v3/response-structure/#response-structure "Permanent link")
All GET and DELETE request parameters go as query parameters, and POST and PUT parameters as form-encoded (`application/x-www-form-urlencoded`) parameters, responses from the API are always JSON.
### Successful request[¶](https://kite.trade/docs/connect/v3/response-structure/#successful-request "Permanent link")
```
HTTP/1.1 200 OK
Content-Type: application/json

{
    "status": "success",
    "data": {}
}

```

All responses from the API server are JSON with the content-type `application/json` unless explicitly stated otherwise. A successful `200 OK` response always has a JSON response body with a `status` key with the value `success`. The `data` key contains the full response payload.
### Failed request[¶](https://kite.trade/docs/connect/v3/response-structure/#failed-request "Permanent link")
```
HTTP/1.1 500 Server error
Content-Type: application/json

{
    "status": "error",
    "message": "Error message",
    "error_type": "GeneralException"
}

```

A failure response is preceded by the corresponding `40x` or `50x` HTTP header. The `status` key in the response envelope contains the value `error`. The `message` key contains a textual description of the error and `error_type` contains the name of the exception. There may be an optional `data` key with additional payload.
### Data types[¶](https://kite.trade/docs/connect/v3/response-structure/#data-types "Permanent link")
Values in JSON responses are of types string, int, float, or bool.
Timestamp (datetime) strings in the responses are represented in the form `yyyy-mm-dd hh:mm:ss`, set under the Indian timezone (IST) — UTC+5.5 hours.
A date string is represented in the form `yyyy-mm-dd`.
Copyright © 2015 - 2025, Zerodha Technology Pvt. Ltd.
Made with

