---
source: https://kite.trade/docs/connect/v3/postbacks/
scraped: true
---
Postbacks / WebHooks

 Kite Connect 3 / API documentation

# Postback (WebHooks)[¶](https://kite.trade/docs/connect/v3/postbacks/#postback-webhooks "Permanent link")
The Postback API sends a `POST` request with a JSON payload to the registered `postback_url` of your app when an order's status changes. This enables you to get arbitrary updates to your orders reliably, irrespective of when they happen (`COMPLETE`, `CANCEL`, `REJECTED`, `UPDATE`). An `UPDATE` postback is triggered when an open order is modified or when there's a partial fill. This can be used to track trades.
Note
This Postback API is meant for platforms and public apps where a single api_key will place orders for multiple users. Only orders placed using the app's `api_key` are notified.
For individual developers, Postbacks over [WebSocket](https://kite.trade/docs/connect/v3/websocket/) is recommended, where, orders placed for a particular user anywhere, for instance, web, mobile, or desktop platforms, are sent.
The JSON payload is posted as a raw HTTP POST body. You will have to read the raw body and then decode it.
> Sample payload
```
{
    "user_id": "AB1234",
    "unfilled_quantity": 0,
    "app_id": 1234,
    "checksum": "2011845d9348bd6795151bf4258102a03431e3bb12a79c0df73fcb4b7fde4b5d",
    "placed_by": "AB1234",
    "order_id": "220303000308932",
    "exchange_order_id": "1000000001482421",
    "parent_order_id": null,
    "status": "COMPLETE",
    "status_message": null,
    "status_message_raw": null,
    "order_timestamp": "2022-03-03 09:24:25",
    "exchange_update_timestamp": "2022-03-03 09:24:25",
    "exchange_timestamp": "2022-03-03 09:24:25",
    "variety": "regular",
    "exchange": "NSE",
    "tradingsymbol": "SBIN",
    "instrument_token": 779521,
    "order_type": "MARKET",
    "transaction_type": "BUY",
    "validity": "DAY",
    "product": "CNC",
    "quantity": 1,
    "disclosed_quantity": 0,
    "price": 0,
    "trigger_price": 0,
    "average_price": 470,
    "filled_quantity": 1,
    "pending_quantity": 0,
    "cancelled_quantity": 0,
    "market_protection": 0,
    "meta": {},
    "tag": null,
    "guid": "XXXXXX"
}

```

### Checksum[¶](https://kite.trade/docs/connect/v3/postbacks/#checksum "Permanent link")
The JSON payload comes with a `checksum`, which is the SHA-256 hash of (`order_id` + `order_timestamp` + `api_secret`). For every Postback you receive, you should compute this checksum at your end and match it with the checksum in the payload. This is to ensure that the update is being POSTed by Kite Connect and not by an unauthorised entity, as only Kite Connect can generate a checksum that contains your `api_secret`.
### Payload attributes[¶](https://kite.trade/docs/connect/v3/postbacks/#payload-attributes "Permanent link")
attribute |
---|---
`order_id`string | Unique order ID
`exchange_order_id`null, string | Exchange generated order id. Orders that don't reach the exchange have null ids
`parent_order_id`null, string | Order ID of the parent order (only applicable in case of multi-legged orders like CO)
`placed_by`string | ID of the user that placed the order. This may different from the user's id for orders placed outside of Kite, for instance, by dealers at the brokerage using dealer terminals.
`app_id`int64 | Your kiteconnect app ID
`status`null, string | Current status of the order. The possible values are COMPLETE, REJECTED, CANCELLED, and UPDATE.
`status_message`null, string | Textual description of the order's status. Failed orders come with human readable explanation
`status_message_raw`null, string | Raw textual description of the failed order's status, as received from the OMS
`tradingsymbol`string | Exchange tradingsymbol of the of the instrument
`instrument_token`uint32 | The numerical identifier issued by the exchange representing the instrument
`exchange`string | Exchange
`order_type`string | Order type (MARKET, LIMIT etc.)
`transaction_type`string | BUY or SELL
`validity`string | Order validity
`variety`string | Order variety (regular, amo, co etc.)
`product`string | Margin product to use for the order
`average_price`float64 | Average price at which the order was executed (only for COMPLETE orders)
`disclosed_quantity`int64 | Quantity to be disclosed (may be different from actual quantity) to the public exchange orderbook. Only for equities
`price`float64 | Price at which the order was placed (LIMIT orders)
`quantity`int64 | Quantity ordered
`filled_quantity`int64 | Quantity that has been filled
`unfilled_quantity`int64 | Quantity that has not filled
`pending_quantity`int64 | Pending quantity for open order
`cancelled_quantity`int64 | Quantity that had been cancelled
`trigger_price`float64 | Trigger price (for SL, SL-M, CO orders)
`user_id`string | ID of the user for whom the order was placed.
`order_timestamp`string | Timestamp at which the order was registered by the API
`exchange_update_timestamp`string | Timestamp at which an order's state changed at the exchange
`exchange_timestamp`string | Timestamp at which the order was registered by the exchange. Orders that don't reach the exchange have null timestamps
`checksum`string | SHA-256 hash of (order_id + timestamp + api_secret)
`meta`{}, string | Map of arbitrary fields that the system may attach to an order
`tag`null, string | An optional tag to apply to an order to identify it (alphanumeric, max 20 chars)
Note
Postback API works even when the user is not logged in. Just make sure you validate the checksum value to ensure that the update is indeed coming from Kite Connect.
Copyright © 2015 - 2025, Zerodha Technology Pvt. Ltd.
Made with

