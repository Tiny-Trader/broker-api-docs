---
source: https://kite.trade/docs/connect/v3/user/
scraped: true
---
User


# User[¶](https://kite.trade/docs/connect/v3/user/#user "Permanent link")
## Login flow[¶](https://kite.trade/docs/connect/v3/user/#login-flow "Permanent link")
The login flow starts by navigating to the public Kite login endpoint.
> **`https://kite.zerodha.com/connect/login?v=3&api_key=xxx`**
A successful login comes back with a `request_token` as a URL query parameter to the redirect URL registered on the developer console for that `api_key`. This `request_token`, along with a `checksum` (SHA-256 of `api_key + request_token + api_secret`) is POSTed to the token API to obtain an `access_token`, which is then used for signing all subsequent requests. In summary:
  1. Navigate to the Kite Connect login page with the api_key
  2. A successful login comes back with a `request_token` to the registered redirect URL
  3. POST the `request_token` and `checksum` (SHA-256 of `api_key + request_token + api_secret`) to `/session/token`
  4. Obtain the `access_token` and use that with all subsequent requests

> An optional `redirect_params` param can be appended to public Kite login endpoint, that will be sent back to the redirect URL. The value is URL encoded query params string, eg: `some=X&more=Y`). eg: `https://kite.zerodha.com/connect/login?v=3&api_key=xxx&redirect_params=some%3DX%26more%3DY`
![Kite Connect handshake flow](https://kite.trade/docs/connect/v3/images/kite-connect-flow.png)
Warning
Never expose your `api_secret` by embedding it in a mobile app or a client side application. Do not expose the `access_token` you obtain for a session to the public either.
type | endpoint |
---|---|---
POST | [/session/token](https://kite.trade/docs/connect/v3/user/#authentication-and-token-exchange) | Authenticate and obtain the access_token after the login flow
GET | [/user/profile](https://kite.trade/docs/connect/v3/user/#user-profile) | Retrieve the user profile
GET | [/user/margins/:segment](https://kite.trade/docs/connect/v3/user/#funds-and-margins) | Retrieve detailed funds and margin information
DELETE | [/session/token](https://kite.trade/docs/connect/v3/user/#logout) | Logout and invalidate the API session and access_token
## Authentication and token exchange[¶](https://kite.trade/docs/connect/v3/user/#authentication-and-token-exchange "Permanent link")
Once the `request_token` is obtained from the login flow, it should be POSTed to `/session/token` to complete the token exchange and retrieve the `access_token`.
```
curl https://api.kite.trade/session/token \
   -H "X-Kite-Version: 3" \
   -d "api_key=xxx" \
   -d "request_token=yyy" \
   -d "checksum=zzz"

```

```
{
    "status": "success",
    "data": {
        "user_type": "individual",
        "email": "XXXXXX",
        "user_name": "Kite Connect",
        "user_shortname": "Connect",
        "broker": "ZERODHA",
        "exchanges": [
            "NSE",
            "NFO",
            "BFO",
            "CDS",
            "BSE",
            "MCX",
            "BCD",
            "MF"
        ],
        "products": [
            "CNC",
            "NRML",
            "MIS",
            "BO",
            "CO"
        ],
        "order_types": [
            "MARKET",
            "LIMIT",
            "SL",
            "SL-M"
        ],
        "avatar_url": "abc",
        "user_id": "XX0000",
        "api_key": "XXXXXX",
        "access_token": "XXXXXX",
        "public_token": "XXXXXXXX",
        "enctoken": "XXXXXX",
        "refresh_token": '',
        "silo": '',
        "login_time": "2021-01-01 16:15:14",
        "meta": {
            "demat_consent": "physical"
        }
    }
}

```

### Request parameters[¶](https://kite.trade/docs/connect/v3/user/#request-parameters "Permanent link")
parameter |
---|---
`api_key` | The public API key
`request_token` | The one-time token obtained after the login flow. This token's lifetime is only a few minutes and it is meant to be exchanged for an `access_token` immediately after being obtained
`checksum` | SHA-256 hash of (api_key + request_token + api_secret)
### Response attributes[¶](https://kite.trade/docs/connect/v3/user/#response-attributes "Permanent link")
attribute |
---|---
`user_id`string | The unique, permanent user id registered with the broker and the exchanges
`user_name`string | User's real name
`user_shortname`string | Shortened version of the user's real name
`email`string | User's email
`user_type`string | User's registered role at the broker. This will be `individual` for all retail users
`broker`string | The broker ID
`exchanges`string[] | Exchanges enabled for trading on the user's account
`products`string[] | Margin product types enabled for the user
`order_types`string[] | Order types enabled for the user
`api_key`string | The API key for which the authentication was performed
`access_token`string | The authentication token that's used with every subsequent request Unless this is [invalidated using the API](https://kite.trade/docs/connect/v3/user/#logout), or invalidated by a master-logout from the Kite Web trading terminal, it'll expire at `6 AM` on the next day (regulatory requirement)
`public_token`string | A token for public session validation where requests may be exposed to the public
`refresh_token`string | A token for getting long standing read permissions. This is only available to certain approved platforms
`login_time`string | User's last login time
`meta`map |  `demat_consent`: empty, consent or physical
`avatar_url`string | Full URL to the user's avatar (PNG image) if there's one
### Signing requests[¶](https://kite.trade/docs/connect/v3/user/#signing-requests "Permanent link")
Once the authentication is complete, all requests should be signed with the HTTP `Authorization` header with `token` as the authorisation scheme, followed by a space, and then the `api_key:access_token` combination. For example:
```
curl -H "Authorization: token api_key:access_token"
curl -H "Authorization: token xxx:yyy"

```

## User profile[¶](https://kite.trade/docs/connect/v3/user/#user-profile "Permanent link")
While a successful token exchange returns the full user profile, it's possible to retrieve it any point of time with the `/user/profile` API. Do note that the profile API does not return any of the tokens.
```
curl https://api.kite.trade/user/profile \
   -H "X-Kite-Version: 3" \
   -H "Authorization: token api_key:access_token"

```

```
{
  "status": "success",
  "data": {
    "user_id": "AB1234",
    "user_type": "individual",
    "email": "xxxyyy@gmail.com",
    "user_name": "AxAx Bxx",
    "user_shortname": "AxAx",
    "broker": "ZERODHA",
    "exchanges": [
      "BFO",
      "MCX",
      "NSE",
      "CDS",
      "BSE",
      "BCD",
      "MF",
      "NFO"
    ],
    "products": [
      "CNC",
      "NRML",
      "MIS",
      "BO",
      "CO"
    ],
    "order_types": [
      "MARKET",
      "LIMIT",
      "SL",
      "SL-M"
    ],
    "avatar_url": null,
    "meta": {
      "demat_consent": "physical"
    }
  }
}

```

### Response attributes[¶](https://kite.trade/docs/connect/v3/user/#response-attributes_1 "Permanent link")
attribute |
---|---
`user_id`string | The unique, permanent user id registered with the broker and the exchanges
`user_name`string | User's real name
`user_shortname`string | Shortened version of the user's real name
`email`string | User's email
`user_type`string | User's registered role at the broker. This will be `individual` for all retail users
`broker`string | The broker ID
`exchanges`string[] | Exchanges enabled for trading on the user's account
`products`string[] | Margin product types enabled for the user
`order_types`string[] | Order types enabled for the user
`meta`map |  `demat_consent`: empty, consent or physical
`avatar_url`string | Full URL to the user's avatar (PNG image) if there's one
## Funds and margins[¶](https://kite.trade/docs/connect/v3/user/#funds-and-margins "Permanent link")
A GET request to `/user/margins` returns funds, cash, and margin information for the user for equity and commodity segments.
A GET request to `/user/margins/:segment` returns funds, cash, and margin information for the user. `segment` in the URI can be either `equity` or `commodity`.
```
curl "https://api.kite.trade/user/margins" \
    -H "X-Kite-Version: 3" \
    -H "Authorization: token api_key:access_token"

```

```
{
    "status": "success",
    "data": {
      "equity": {
        "enabled": true,
        "net": 99725.05000000002,
        "available": {
          "adhoc_margin": 0,
          "cash": 245431.6,
          "opening_balance": 245431.6,
          "live_balance": 99725.05000000002,
          "collateral": 0,
          "intraday_payin": 0
        },
        "utilised": {
          "debits": 145706.55,
          "exposure": 38981.25,
          "m2m_realised": 761.7,
          "m2m_unrealised": 0,
          "option_premium": 0,
          "payout": 0,
          "span": 101989,
          "holding_sales": 0,
          "turnover": 0,
          "liquid_collateral": 0,
          "stock_collateral": 0,
          "delivery": 0
        }
      },
      "commodity": {
        "enabled": true,
        "net": 100661.7,
        "available": {
          "adhoc_margin": 0,
          "cash": 100661.7,
          "opening_balance": 100661.7,
          "live_balance": 100661.7,
          "collateral": 0,
          "intraday_payin": 0
        },
        "utilised": {
          "debits": 0,
          "exposure": 0,
          "m2m_realised": 0,
          "m2m_unrealised": 0,
          "option_premium": 0,
          "payout": 0,
          "span": 0,
          "holding_sales": 0,
          "turnover": 0,
          "liquid_collateral": 0,
          "stock_collateral": 0,
          "delivery": 0
        }
      }
    }
  }

```

### Response attributes[¶](https://kite.trade/docs/connect/v3/user/#response-attributes_2 "Permanent link")
attribute |
---|---
`enabled`bool | Indicates whether the segment is enabled for the user
`net`float64 | Net cash balance available for trading (`intraday_payin` + `adhoc_margin` + `collateral`)
`available.cash`float64 | Raw cash balance in the account available for trading (also includes `intraday_payin`)
`available.opening_balance`float64 | Opening balance at the day start
`available.live_balance`float64 | Current available balance
`available.intraday_payin`float64 | Amount that was deposited during the day
`available.adhoc_margin`float64 | Additional margin provided by the broker
`available.collateral`float64 | Margin derived from pledged stocks
`utilised.m2m_unrealised`float64 | Un-booked (open) intraday profits and losses
`utilised.m2m_realised`float64 | Booked intraday profits and losses
`utilised.debits`float64 | Sum of all utilised margins (unrealised M2M + realised M2M + SPAN + Exposure + Premium + Holding sales)
`utilised.span`float64 | SPAN margin blocked for all open F&O positions
`utilised.option_premium`float64 | Value of options premium received by shorting
`utilised.holding_sales`float64 | Value of holdings sold during the day
`utilised.exposure`float64 | Exposure margin blocked for all open F&O positions
`utilised.liquid_collateral`float64 | Margin utilised against pledged liquidbees ETFs and liquid mutual funds
`utilised.delivery`float64 | Margin blocked when you sell securities (20% of the value of stocks sold) from your demat or T1 holdings
`utilised.stock_collateral`float64 | Margin utilised against pledged stocks/ETFs
`utilised.turnover`float64 | Utilised portion of the maximum turnover limit (only applicable to certain clients)
`utilised.payout`float64 | Funds paid out or withdrawn to bank account during the day
## Logout[¶](https://kite.trade/docs/connect/v3/user/#logout "Permanent link")
This call invalidates the access_token and destroys the API session. After this, the user should be sent through a new login flow before further interactions. This does not log the user out of the official Kite web or mobile applications.
```
curl --request DELETE \
  -H "X-Kite-Version: 3" \
  "https://api.kite.trade/session/token?api_key=xxx&access_token=yyy"

```

```
{
  "status": "success",
  "data": true
}

```

Copyright © 2015 - 2025, Zerodha Technology Pvt. Ltd.
Made with

