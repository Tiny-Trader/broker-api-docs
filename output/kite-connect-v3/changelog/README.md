---
source: https://kite.trade/docs/connect/v3/changelog/
scraped: true
---
Changelog

# Changelog[¶](https://kite.trade/docs/connect/v3/changelog/#changelog "Permanent link")
## Kite Connect 3.1 — Changes[¶](https://kite.trade/docs/connect/v3/changelog/#kite-connect-31-changes "Permanent link")
### Orders[¶](https://kite.trade/docs/connect/v3/changelog/#orders "Permanent link")

### GTT orders[¶](https://kite.trade/docs/connect/v3/changelog/#gtt-orders "Permanent link")
  * Added support placing, updating, and deleting for [GTT orders](https://kite.trade/docs/connect/v3/gtt/)

### Quote Call[¶](https://kite.trade/docs/connect/v3/changelog/#quote-call "Permanent link")
  * Added [Circuit Limits](https://kite.trade/docs/connect/v3/market-quotes/#retrieving-full-market-quotes) to quote call response

### Historical Data[¶](https://kite.trade/docs/connect/v3/changelog/#historical-data "Permanent link")
  * Added [OI](https://kite.trade/docs/connect/v3/changelog/historical.md/#oi-data) to historical candle data response

## Kite Connect 3.0 — Changes[¶](https://kite.trade/docs/connect/v3/changelog/#kite-connect-30-changes "Permanent link")
The new APIs continue to be on the same route `api.kite.trade`, but to connect to the 3.0 backend, the header `X-Kite-Version: 3` should be sent with every HTTP request. This is illustrated throughout the documentation in the `curl` examples.
### API endpoint changes[¶](https://kite.trade/docs/connect/v3/changelog/#api-endpoint-changes "Permanent link")
Endpoint | Status |
---|---|---
[`/quote`](https://kite.trade/docs/connect/v3/market-quotes/) | New | Retrieve complete market quotes (including depth) for up to 500 instruments in one go
[`/quote/ohlc`](https://kite.trade/docs/connect/v3/market-quotes/) | New | Retrieve OHLC quotes for up to 1000 instruments in one go
[`/quote/ltp`](https://kite.trade/docs/connect/v3/market-quotes/) | New | Retrieve LTP (`last_price`) quotes for up to 1000 instruments in one go
[`/user/profile`](https://kite.trade/docs/connect/v3/user/#user-profile) | New | Retrieve user profile
`/market/instruments/:exchange/:tradingsymbol` | Removed | Replaced by the new `/quote` API
### Login[¶](https://kite.trade/docs/connect/v3/changelog/#login "Permanent link")
For obtaining a 3.0 login session, the query param **v=3** should be added to the initial login URL.
`https://kite.zerodha.com/connect/login?v=3&api_key=xxx`
### Authentication[¶](https://kite.trade/docs/connect/v3/changelog/#authentication "Permanent link")
In the previous version, request authentication was done by sending the `api_key` and `access_token` query parameters. In 3.0, this has been replaced by the `Authorization` header. This is evident in all the examples in this documentation.
All requests now have to be authenticated by sending the HTTP header:
```
Authorization: token api_key:access_token

```

### WebSocket[¶](https://kite.trade/docs/connect/v3/changelog/#websocket "Permanent link")

### Changes to API responses[¶](https://kite.trade/docs/connect/v3/changelog/#changes-to-api-responses "Permanent link")
Date | Change
---|---
`/session/token` | New fields:
`api_key`
`refresh_token`

Changed fields:
`order_type -> order_types`
`exchange -> exchanges`
`product -> products`

Removed fields:
`password_reset`
`member_id`
`/portfolio/positions` | New fields:
`day_buy_qty`
`day_buy_price`
`day_buy_value`
`day_sell_qty`
`day_sell_price`
`day_sell_value`
`/trades`
`/orders/:order_id/trades` | New fields:
`fill_timestamp`

Removed fields:
`order_timestamp`
### Changelog[¶](https://kite.trade/docs/connect/v3/changelog/#changelog_1 "Permanent link")
Date | Change
---|---
2025-06-12 | Added [Alerts API](https://kite.trade/docs/connect/v3/alerts/)
2025-01-17 | Added MTF orders
2023-07-18 | Added [virtual contract API](http://kite.trade/docs/connect/v3/margins/#virtual-contract-note)
2023-07-18 | Added [virtual contract API](http://kite.trade/docs/connect/v3/margins/#virtual-contract-note)
2023-07-11 | Added [basket margin API](https://kite.trade/docs/connect/v3/margins/#basket-margins)
2022-12-22 | Added [holdings auction list API](https://kite.trade/docs/connect/v3/portfolio/#holdings-auction-list) and auction order params
2022-03-19 | Added iceberg and TTL orders
2021-09-28 | Updated [new APIs rate limit](https://kite.trade/docs/connect/v3/exceptions/#api-rate-limit)
2021-03-12 | Added [holdings authorisation API](https://kite.trade/docs/connect/v3/portfolio/#holdings-authorisation)
2020-08-24 | Added [margin calculator APIs](https://kite.trade/docs/connect/v3/margins/#margin-calculation)
2019-12-10 | Released minor feature updates - Kite Connect 3.1
2018-01-17 | Major version upgrade to Kite Connect 3 from API [v1](https://kite.trade/docs/connect/v1).
2017-09-11 | Introduced bulk quote APIs
2016-05-07 |  `/orders` call and bracket order modification and cancellation now involve the new `parent_order_id` parameter
2016-07-02 | Several new fields added to the Webhooks payload (`exchange_timestamp`, `order_type`, `product`, `unfilled_quantity`, `validity`)
2017-09-11 | Added support for granular timestamp `from` and `to` queries to historical data APIs
2017-09-12 | Added bulk quote fetch APIs
2017-11-13 | Added support for 'UPDATE' Postbacks
Copyright © 2015 - 2025, Zerodha Technology Pvt. Ltd.
Made with

