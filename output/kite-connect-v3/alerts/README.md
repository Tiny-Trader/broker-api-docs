---
source: https://kite.trade/docs/connect/v3/alerts/
scraped: true
---
Alerts

# Alerts[¶](https://kite.trade/docs/connect/v3/alerts/#alerts "Permanent link")
The Alerts API allows you to create, retrieve, update, and delete market price alerts for various instruments. It enables you to set up notifications that will be triggered when market prices reach specific conditions. The maximum number of active alerts allowed per user is 500.
type | endpoint |
---|---|---
POST | [/alerts](https://kite.trade/docs/connect/v3/alerts/#creating-alerts) | Create a new alert
GET | [/alerts](https://kite.trade/docs/connect/v3/alerts/#retrieving-alerts) | Retrieve all alerts for a user
GET | [/alerts/{uuid}](https://kite.trade/docs/connect/v3/alerts/#retrieve-alert) | Retrieve a specific alert
PUT | [/alerts/{uuid}](https://kite.trade/docs/connect/v3/alerts/#modify-alert) | Modify an existing alert
DELETE | [/alerts?uuid={uuid}](https://kite.trade/docs/connect/v3/alerts/#delete-alert) | Delete a specific alert
GET | [/alerts/{uuid}/history](https://kite.trade/docs/connect/v3/alerts/#retrieve-alert-history) | Retrieve the history of a specific alert
## Creating alerts[¶](https://kite.trade/docs/connect/v3/alerts/#creating-alerts "Permanent link")
### Simple alert[¶](https://kite.trade/docs/connect/v3/alerts/#simple-alert "Permanent link")
```
curl https://api.kite.trade/alerts \
    -H 'X-Kite-Version: 3' \
    -H 'Authorization: token api_key:access_token' \
    -d 'name=NIFTY 50' \
    -d 'lhs_exchange=INDICES' \
    -d 'lhs_tradingsymbol=NIFTY 50' \
    -d 'lhs_attribute=LastTradedPrice' \
    -d 'operator=>=' \
    -d 'rhs_type=constant' \
    -d 'type=simple' \
    -d 'rhs_constant=27000'

```

```
{
  "status": "success",
  "data": {
    "type": "simple",
    "user_id": "AB1234",
    "uuid": "550e8400-e29b-41d4-a716-446655440000",
    "name": "NIFTY 50",
    "status": "enabled",
    "disabled_reason": "",
    "lhs_attribute": "LastTradedPrice",
    "lhs_exchange": "INDICES",
    "lhs_tradingsymbol": "NIFTY 50",
    "operator": ">=",
    "rhs_type": "constant",
    "rhs_attribute": "",
    "rhs_exchange": "",
    "rhs_tradingsymbol": "",
    "rhs_constant": 27000,
    "alert_count": 0,
    "created_at": "2025-05-26 12:07:50",
    "updated_at": "2025-05-26 12:07:50"
  }
}

```

### ATO (Alert Triggers Order) alert[¶](https://kite.trade/docs/connect/v3/alerts/#ato-alert-triggers-order-alert "Permanent link")
```
curl https://api.kite.trade/alerts \
    -H 'X-Kite-Version: 3' \
    -H 'Authorization: token api_key:access_token' \
    -d 'name=NIFTY 50' \
    -d 'lhs_exchange=INDICES' \
    -d 'lhs_tradingsymbol=NIFTY 50' \
    -d 'lhs_attribute=LastTradedPrice' \
    -d 'operator=>=' \
    -d 'rhs_type=constant' \
    -d 'type=ato' \
    -d 'rhs_constant=27000' \
    -d 'basket={"name":"alerts-basket","type":"alert","tags":[],"items":[{"type":"insert","tradingsymbol":"RELIANCE","exchange":"NSE","weight":10000,"params":{"transaction_type":"BUY","product":"CNC","order_type":"MARKET","validity":"DAY","validity_ttl":1,"quantity":1,"price":0,"trigger_price":0,"disclosed_quantity":0,"last_price":0,"variety":"regular","tags":[],"squareoff":0,"stoploss":0,"trailing_stoploss":0,"iceberg_legs":0,"market_protection":0}}]}'

```

```
{
  "status": "success",
  "data": {
    "type": "ato",
    "user_id": "AB1234",
    "uuid": "a5a2b03d-4851-44b3-9d85-0123baa4a273",
    "name": "NIFTY 50",
    "status": "enabled",
    "disabled_reason": "",
    "lhs_attribute": "LastTradedPrice",
    "lhs_exchange": "INDICES",
    "lhs_tradingsymbol": "NIFTY 50",
    "operator": ">=",
    "rhs_type": "constant",
    "rhs_attribute": "",
    "rhs_exchange": "",
    "rhs_tradingsymbol": "",
    "rhs_constant": 27000,
    "alert_count": 0,
    "created_at": "2025-05-26 12:09:26",
    "updated_at": "2025-05-26 12:09:26"
  }
}

```

### Alert parameters[¶](https://kite.trade/docs/connect/v3/alerts/#alert-parameters "Permanent link")
parameter |
---|---
name | Name of the alert
type | The [type](https://kite.trade/docs/connect/v3/alerts/#alert-types) of alert
lhs_exchange | Name of the exchange for left-hand side (NSE, BSE, NFO, CDS, BCD, MCX, INDICES)
lhs_tradingsymbol | Trading symbol of the instrument for left-hand side
lhs_attribute | Attribute to monitor (e.g., `LastTradedPrice`)
operator | Comparison [operator](https://kite.trade/docs/connect/v3/alerts/#operator-types)
rhs_type | Type of the right-hand side (`constant` or `instrument`)
rhs_constant | Value to compare against (when `rhs_type` is `constant`)
rhs_exchange | Exchange for right-hand side (when `rhs_type` is `instrument`)
rhs_tradingsymbol | Trading symbol for right-hand side (when `rhs_type` is `instrument`)
rhs_attribute | Attribute for right-hand side (when `rhs_type` is `instrument`)
basket | JSON string containing basket configuration (required for ATO alerts)
#### Operator types[¶](https://kite.trade/docs/connect/v3/alerts/#operator-types "Permanent link")
The Alerts API supports the following operators for comparison:
operator |
---|---
`<=` | Less than or equal to
`>=` | Greater than or equal to
`<` | Less than
`>` | Greater than
`==` | Equal to
#### Alert types[¶](https://kite.trade/docs/connect/v3/alerts/#alert-types "Permanent link")
type |
---|---
`simple` | Standard price alert
`ato` | Alert Triggers Order - when triggered, automatically places an order
#### Basket structure for ATO alerts[¶](https://kite.trade/docs/connect/v3/alerts/#basket-structure-for-ato-alerts "Permanent link")
For ATO alerts, the `basket` parameter should be a JSON string containing:
```
{
  "name": "alerts-basket",
  "type": "alert",
  "tags": [],
  "items": [
    {
      "type": "insert",
      "tradingsymbol": "RELIANCE",
      "exchange": "NSE",
      "weight": 10000,
      "params": {
        "transaction_type": "BUY",
        "product": "CNC",
        "order_type": "MARKET",
        "validity": "DAY",
        "validity_ttl": 1,
        "quantity": 1,
        "price": 0,
        "trigger_price": 0,
        "disclosed_quantity": 0,
        "last_price": 0,
        "variety": "regular",
        "tags": [],
        "squareoff": 0,
        "stoploss": 0,
        "trailing_stoploss": 0,
        "iceberg_legs": 0,
        "market_protection": 0
      }
    }
  ]
}

```

## Retrieving alerts[¶](https://kite.trade/docs/connect/v3/alerts/#retrieving-alerts "Permanent link")
Active alerts and alerts in other states can be obtained by a GET API call to the `/alerts` endpoint.
```
curl "https://api.kite.trade/alerts" \
    -H "X-Kite-Version: 3" \
    -H "Authorization: token api_key:access_token"

```

```
{
  "status": "success",
  "data": [
    {
      "type": "simple",
      "user_id": "AB1234",
      "uuid": "550e8400-e29b-41d4-a716-446655440000",
      "name": "NIFTY 50",
      "status": "enabled",
      "disabled_reason": "",
      "lhs_attribute": "LastTradedPrice",
      "lhs_exchange": "INDICES",
      "lhs_tradingsymbol": "NIFTY 50",
      "operator": ">=",
      "rhs_type": "constant",
      "rhs_attribute": "",
      "rhs_exchange": "",
      "rhs_tradingsymbol": "",
      "rhs_constant": 27000,
      "alert_count": 0,
      "created_at": "2025-05-26 12:07:50",
      "updated_at": "2025-05-26 12:07:50"
    },
    {
      "type": "ato",
      "user_id": "AB1234",
      "uuid": "e888ed4a-6801-406f-bdc2-002db5a8411d",
      "name": "buy gold",
      "status": "disabled",
      "disabled_reason": "",
      "basket": {
        "items": [
          {
            "id": 275218517,
            "tradingsymbol": "GOLDBEES",
            "exchange": "NSE",
            "instrument_token": 3693569,
            "weight": 10000,
            "params": {
              "validity": "DAY",
              "validity_ttl": 0,
              "variety": "regular",
              "product": "CNC",
              "order_type": "LIMIT",
              "transaction_type": "BUY",
              "quantity": 10000,
              "disclosed_quantity": 0,
              "price": 72.22,
              "trigger_price": 0,
              "squareoff": 0,
              "stoploss": 0,
              "trailing_stoploss": 0,
              "gtt": {
                "target": 0,
                "stoploss": 0
              },
              "tags": []
            }
          }
        ]
      },
      "lhs_attribute": "LastTradedPrice",
      "lhs_exchange": "NSE",
      "lhs_tradingsymbol": "GOLDBEES",
      "operator": "<=",
      "rhs_type": "constant",
      "rhs_attribute": "",
      "rhs_exchange": "",
      "rhs_tradingsymbol": "",
      "rhs_constant": 71.8,
      "alert_count": 1,
      "created_at": "2025-02-17 08:24:10",
      "updated_at": "2025-02-17 09:15:20"
    }
  ]
}

```

### Query parameters[¶](https://kite.trade/docs/connect/v3/alerts/#query-parameters "Permanent link")
parameter |
---|---
`status` | Filter alerts by status (`enabled`, `disabled`, `deleted`)
`page` | Page number for pagination
`page_size` | Number of alerts per page
## Retrieve alert[¶](https://kite.trade/docs/connect/v3/alerts/#retrieve-alert "Permanent link")
Given an alert UUID, the GET API call to this endpoint will return details of the alert.
```
curl "https://api.kite.trade/alerts/550e8400-e29b-41d4-a716-446655440000" \
    -H "X-Kite-Version: 3" \
    -H "Authorization: token api_key:access_token"

```

```
{
  "status": "success",
  "data": {
    "type": "simple",
    "user_id": "AB1234",
    "uuid": "550e8400-e29b-41d4-a716-446655440000",
    "name": "NIFTY 50",
    "status": "enabled",
    "disabled_reason": "",
    "lhs_attribute": "LastTradedPrice",
    "lhs_exchange": "INDICES",
    "lhs_tradingsymbol": "NIFTY 50",
    "operator": ">=",
    "rhs_type": "constant",
    "rhs_attribute": "",
    "rhs_exchange": "",
    "rhs_tradingsymbol": "",
    "rhs_constant": 27000,
    "alert_count": 0,
    "created_at": "2025-05-26 12:07:50",
    "updated_at": "2025-05-26 12:07:50"
  }
}

```

### Status[¶](https://kite.trade/docs/connect/v3/alerts/#status "Permanent link")
Alerts can be in the following states:
status |
---|---
`enabled` | Indicates that the alert is active and being evaluated.
`disabled` | Indicates that the alert is disabled and not being evaluated.
`deleted` | Indicates that the alert has been soft-deleted by the user.
## Modify alert[¶](https://kite.trade/docs/connect/v3/alerts/#modify-alert "Permanent link")
To modify an alert, you need to send a PUT call with updated parameters.
```
curl "https://api.kite.trade/alerts/550e8400-e29b-41d4-a716-446655440000" \
    -X PUT \
    -H 'X-Kite-Version: 3' \
    -H 'Authorization: token api_key:access_token' \
    -d 'name=NIFTY 50' \
    -d 'lhs_exchange=INDICES' \
    -d 'lhs_tradingsymbol=NIFTY 50' \
    -d 'lhs_attribute=LastTradedPrice' \
    -d 'operator=>=' \
    -d 'rhs_type=constant' \
    -d 'type=simple' \
    -d 'rhs_constant=27500'

```

```
{
  "status": "success",
  "data": {
    "type": "simple",
    "user_id": "AB1234",
    "uuid": "550e8400-e29b-41d4-a716-446655440000",
    "name": "NIFTY 50",
    "status": "enabled",
    "disabled_reason": "",
    "lhs_attribute": "LastTradedPrice",
    "lhs_exchange": "INDICES",
    "lhs_tradingsymbol": "NIFTY 50",
    "operator": ">=",
    "rhs_type": "constant",
    "rhs_attribute": "",
    "rhs_exchange": "",
    "rhs_tradingsymbol": "",
    "rhs_constant": 27500,
    "alert_count": 0,
    "created_at": "2025-05-26 12:07:50",
    "updated_at": "2025-05-26 12:10:15"
  }
}

```

Note
It is recommended to fetch the alert using [alert UUID](https://kite.trade/docs/connect/v3/alerts/#retrieve-alert) and modify the values and send that to the modify endpoint.
## Delete alert[¶](https://kite.trade/docs/connect/v3/alerts/#delete-alert "Permanent link")
### Delete single alert[¶](https://kite.trade/docs/connect/v3/alerts/#delete-single-alert "Permanent link")
```
curl "https://api.kite.trade/alerts?uuid=550e8400-e29b-41d4-a716-446655440000" \
    -X DELETE \
    -H 'X-Kite-Version: 3' \
    -H 'Authorization: token api_key:access_token'

```

```
{
  "status": "success",
  "data": null
}

```

### Delete multiple alerts[¶](https://kite.trade/docs/connect/v3/alerts/#delete-multiple-alerts "Permanent link")
To delete multiple alerts, pass multiple `uuid` query parameters:
```
curl "https://api.kite.trade/alerts?uuid=550e8400-e29b-41d4-a716-446655440000&uuid=a5a2b03d-4851-44b3-9d85-0123baa4a273" \
    -X DELETE \
    -H 'X-Kite-Version: 3' \
    -H 'Authorization: token api_key:access_token'

```

```
{
  "status": "success",
  "data": null
}

```

## Retrieve alert history[¶](https://kite.trade/docs/connect/v3/alerts/#retrieve-alert-history "Permanent link")
This endpoint returns the history of when an alert was triggered, including market data at the time of trigger.
```
curl "https://api.kite.trade/alerts/550e8400-e29b-41d4-a716-446655440000/history" \
    -H "X-Kite-Version: 3" \
    -H "Authorization: token api_key:access_token"

```

```
{
  "status": "success",
  "data": [
    {
      "uuid": "550e8400-e29b-41d4-a716-446655440000",
      "type": "simple",
      "meta": [
        {
          "instrument_token": 270857,
          "tradingsymbol": "NIFTY NEXT 50",
          "timestamp": "2025-02-17 09:16:46",
          "last_price": 58288.05,
          "ohlc": {
            "open": 59221.95,
            "high": 59241.8,
            "low": 58283.7,
            "close": 59557.95
          },
          "net_change": -1269.9,
          "exchange": "INDICES",
          "last_trade_time": "0001-01-01 00:00:00",
          "last_quantity": 0,
          "buy_quantity": 0,
          "sell_quantity": 0,
          "volume": 0,
          "volume_tick": 0,
          "average_price": 0,
          "oi": 0,
          "oi_day_high": 0,
          "oi_day_low": 0,
          "lower_circuit_limit": 0,
          "upper_circuit_limit": 0
        }
      ],
      "condition": "LastTradedPrice(\"INDICES:NIFTY NEXT 50\") <= 58290.35",
      "created_at": "2025-02-17 09:16:46",
      "order_meta": null
    }
  ]
}

```

Copyright © 2015 - 2025, Zerodha Technology Pvt. Ltd.
Made with

