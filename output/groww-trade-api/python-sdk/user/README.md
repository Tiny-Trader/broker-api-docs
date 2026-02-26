---
source: https://groww.in/trade-api/docs/python-sdk/user
scraped: true
---
[](https://groww.in/)[![Groww Logo](https://groww.in/favicon32x32-groww.ico)Groww API](https://groww.in/trade-api)
[](https://groww.in/)[![Groww Logo](https://groww.in/favicon32x32-groww.ico)Groww API](https://groww.in/trade-api)
Python SDK Docs
Documentation for Python SDK
`⌘``K`
[Documentation](https://groww.in/trade-api/docs)
[Introduction](https://groww.in/trade-api/docs/python-sdk)[Instruments](https://groww.in/trade-api/docs/python-sdk/instruments)[Orders](https://groww.in/trade-api/docs/python-sdk/orders)[Smart Orders](https://groww.in/trade-api/docs/python-sdk/smart-orders)[Portfolio](https://groww.in/trade-api/docs/python-sdk/portfolio)[Margin](https://groww.in/trade-api/docs/python-sdk/margin)[Live Data](https://groww.in/trade-api/docs/python-sdk/live-data)[Historical Data](https://groww.in/trade-api/docs/python-sdk/historical-data)[Backtesting](https://groww.in/trade-api/docs/python-sdk/backtesting)[Feed](https://groww.in/trade-api/docs/python-sdk/feed)[User](https://groww.in/trade-api/docs/python-sdk/user)[Annexures](https://groww.in/trade-api/docs/python-sdk/annexures)[Exceptions](https://groww.in/trade-api/docs/python-sdk/exceptions)[Changelog](https://groww.in/trade-api/docs/python-sdk/changelog)
Get User Profile
# User
This guide describes how to retrieve user profile information and account details using the SDK.
## [Get User Profile](https://groww.in/trade-api/docs/python-sdk/user#get-user-profile)
Retrieve detailed information about the authenticated user's trading account, including unique identifiers, exchange access permissions, enabled trading segments, and DDPI authorization status.
### [Python SDK Usage](https://groww.in/trade-api/docs/python-sdk/user#python-sdk-usage)
```
from growwapi import GrowwAPI

# Groww API Credentials (Replace with your actual credentials)
API_AUTH_TOKEN = "your_token"

# Initialize Groww API
groww = GrowwAPI(API_AUTH_TOKEN)

user_profile_response = groww.get_user_profile()
print(user_profile_response)
```

### [Response](https://groww.in/trade-api/docs/python-sdk/user#response)
```
{
  "vendor_user_id": "d86890d1-c60d-4ebd-9730-4feee5451670",
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
```

#### [Response Schema](https://groww.in/trade-api/docs/python-sdk/user#response-schema)
Name | Type | Description
---|---|---
vendor_user_id | string | Unique identifier of the user

ucc | string | Unique Client Code (UCC) of the user

nse_enabled | boolean | Whether trading is enabled on National Stock Exchange (NSE) for this user

bse_enabled | boolean | Whether trading is enabled on Bombay Stock Exchange (BSE) for this user

ddpi_enabled | boolean | DDPI (Demat Debit and Pledge Instruction) status. When enabled, allows the broker to debit securities from the user's Demat account for transactions like selling shares or pledging them for margin, without requiring TPIN and OTP authorization for each transaction

active_segments | array[string] | List of trading [segments](https://groww.in/trade-api/docs/python-sdk/annexures#segment) active for the user such as CASH, FNO, COMMODITY etc.

[Previous Feed](https://groww.in/trade-api/docs/python-sdk/feed)[Next Annexures](https://groww.in/trade-api/docs/python-sdk/annexures)
[Get User Profile](https://groww.in/trade-api/docs/python-sdk/user#get-user-profile)

