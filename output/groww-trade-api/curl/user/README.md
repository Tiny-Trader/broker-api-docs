---
source: https://groww.in/trade-api/docs/curl/user
scraped: true
---
[](https://groww.in/)[![Groww Logo](https://groww.in/favicon32x32-groww.ico)Groww API](https://groww.in/trade-api)
[](https://groww.in/)[![Groww Logo](https://groww.in/favicon32x32-groww.ico)Groww API](https://groww.in/trade-api)
cURL Docs
Documentation for cURL
`⌘``K`
[Documentation](https://groww.in/trade-api/docs)
[Introduction](https://groww.in/trade-api/docs/curl)[Instruments](https://groww.in/trade-api/docs/curl/instruments)[Orders](https://groww.in/trade-api/docs/curl/orders)[Smart Orders](https://groww.in/trade-api/docs/curl/smart-orders)[Portfolio](https://groww.in/trade-api/docs/curl/portfolio)[Margin](https://groww.in/trade-api/docs/curl/margin)[Live Data](https://groww.in/trade-api/docs/curl/live-data)[Historical Data](https://groww.in/trade-api/docs/curl/historical-data)[Backtesting](https://groww.in/trade-api/docs/curl/backtesting)[User](https://groww.in/trade-api/docs/curl/user)[Annexures](https://groww.in/trade-api/docs/curl/annexures)[Changelog](https://groww.in/trade-api/docs/curl/changelog)
Get User Profile
# User
Get user profile information
## [Get User Profile](https://groww.in/trade-api/docs/curl/user#get-user-profile)
`GET https://api.groww.in/v1/user/detail`
This API retrieves the user's profile information including their unique identifiers, trading capabilities across exchanges, enabled segments, and DDPI status.
### [Request](https://groww.in/trade-api/docs/curl/user#request)
```
# You can also use wget
curl -X GET https://api.groww.in/v1/user/detail \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

### [Response](https://groww.in/trade-api/docs/curl/user#response)
```
{
  "status": "SUCCESS",
  "payload": {
    "vendor_user_id": "d86890d1-c60d-4ebd-9730-4f451670",
    "ucc": "924189",
    "nse_enabled": true,
    "bse_enabled": true,
    "ddpi_enabled": false,
    "active_segments": [
      "CASH",
      "FNO",
      "COMMODITY"
    ]
  }
}
```

#### [Response Schema](https://groww.in/trade-api/docs/curl/user#response-schema)
Name | Type | Description
---|---|---
status | string | SUCCESS if request is processed successfully, FAILURE if the request failed

vendor_user_id | string | Unique identifier of the user

ucc | string | Unique Client Code (UCC) of the user

nse_enabled | boolean | Whether trading is enabled on National Stock Exchange (NSE) for this user

bse_enabled | boolean | Whether trading is enabled on Bombay Stock Exchange (BSE) for this user

ddpi_enabled | boolean | DDPI (Demat Debit and Pledge Instruction) status. When enabled, allows the broker to debit securities from the user's Demat account for transactions like selling shares or pledging them for margin, without requiring TPIN and OTP authorization for each transaction

active_segments | array[string] | List of trading [Segment](https://groww.in/trade-api/docs/curl/annexures#segment) active for the user.

[Previous Backtesting](https://groww.in/trade-api/docs/curl/backtesting)[Next Annexures](https://groww.in/trade-api/docs/curl/annexures)
[Get User Profile](https://groww.in/trade-api/docs/curl/user#get-user-profile)

