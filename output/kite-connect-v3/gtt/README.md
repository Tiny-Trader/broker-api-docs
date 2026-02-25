---
source: https://kite.trade/docs/connect/v3/gtt/
scraped: true
---
GTT orders

 Kite Connect 3 / API documentation

# GTT - Good Till Triggered orders[¶](https://kite.trade/docs/connect/v3/gtt/#gtt-good-till-triggered-orders "Permanent link")
The GTT APIs allow you to place, modify and manage GTTs.
type | endpoint |
---|---|---
POST | [/gtt/triggers](https://kite.trade/docs/connect/v3/gtt/#placing-triggers) | Place a GTT
GET | [/gtt/triggers](https://kite.trade/docs/connect/v3/gtt/#retrieving-triggers) | Retrieve a list of all GTTs visible in GTT order book
GET | [/gtt/triggers/:id](https://kite.trade/docs/connect/v3/gtt/#retrieve-trigger) | Retrieve an individual trigger
PUT | [/gtt/triggers/:id](https://kite.trade/docs/connect/v3/gtt/#modify-trigger) | Modify an active GTT
DELETE | [/gtt/triggers/:id](https://kite.trade/docs/connect/v3/gtt/#delete-trigger) | Delete an active GTT
## Placing triggers[¶](https://kite.trade/docs/connect/v3/gtt/#placing-triggers "Permanent link")
```
curl https://api.kite.trade/gtt/triggers \
    -H 'X-Kite-Version: 3' \
    -H 'Authorization: token api_key:access_token' \
    -d 'type=single' \
    -d 'condition={"exchange":"NSE", "tradingsymbol":"INFY", "trigger_values":[702.0], "last_price": 798.0}' \
    -d 'orders=[{"exchange":"NSE", "tradingsymbol": "INFY", "transaction_type": "BUY", "quantity": 1, "order_type": "LIMIT","product": "CNC", "price": 702.5}]'

```

```
{"status":"success","data":{"trigger_id":123}}

```

### Order parameters[¶](https://kite.trade/docs/connect/v3/gtt/#order-parameters "Permanent link")
parameter |
---|---
type | The [type](https://kite.trade/docs/connect/v3/gtt/#type) of GTT
condition | The [condition parameters](https://kite.trade/docs/connect/v3/gtt/#condition-parameters) (json object)
orders | The [orders](https://kite.trade/docs/connect/v3/gtt/#orders-list) to be placed (json array).
#### Condition parameters[¶](https://kite.trade/docs/connect/v3/gtt/#condition-parameters "Permanent link")
The API expects the following parameters encoded as json in the condition post parameter.
parameter |
---|---
exchange | Name of the exchange
tradingsymbol | Trading symbol of the instrument
trigger_values | Trigger values (json array)
last_price | Last price of the instrument at the time of placement
#### Orders list[¶](https://kite.trade/docs/connect/v3/gtt/#orders-list "Permanent link")
The API expects a list of orders encoded as a json array. The index of the order is used by API to determine which order is executed when a trigger value is reached.
The order object inside the list expects the following parameters.
parameter |
---|---
exchange | Name of the exchange
tradingsymbol | Trading symbol of the instrument
transaction_type |  `BUY` or `SELL`
quantity | Quantity to transact
order_type | `LIMIT`
product | Margin product to use for the order
price | The min or max price to execute the order at (for LIMIT orders)
Sample order:
```
{
  "exchange": "NSE",
  "tradingsymbol": "INFY",
  "transaction_type": "BUY",
  "quantity": 1,
  "order_type": "LIMIT",
  "product": "CNC",
  "price": 702.5
}

```

#### Type[¶](https://kite.trade/docs/connect/v3/gtt/#type "Permanent link")
The GTT API supports the following type of GTTs. The `type` in the post parameter is used to parse the `condition` passed to it. The following types are supported by GTT API.
#####  `single`[¶](https://kite.trade/docs/connect/v3/gtt/#single "Permanent link")
The single leg trigger type expects a single trigger value, and executes the first order that is in the `orders` array when the trigger value is reached.
Sample `condition`:
```
{
  "exchange": "NSE",
  "tradingsymbol": "INFY",
  "trigger_values": [702.0],
  "last_price": 798.0
}

```

Note
This trigger type expects only one trigger value inside the `trigger_values`
Sample `orders`:
```
[
  {
    "exchange": "NSE",
    "tradingsymbol": "INFY",
    "transaction_type": "BUY",
    "quantity": 1,
    "order_type": "LIMIT",
    "product": "CNC",
    "price": 702.5
  }
]

```

#####  `two-leg`[¶](https://kite.trade/docs/connect/v3/gtt/#two-leg "Permanent link")
The `two-leg` trigger implements the OCO (One Cancels Other) order. It expects two trigger values and executes the corresponding order in the `orders` array when either of the trigger value is reached, the other order is lain dormant.
Sample `condition`:
```
{
  "exchange": "NSE",
  "tradingsymbol": "INFY",
  "trigger_values": [702.0, 798.0],
  "last_price": 742.0
}

```

Note
This trigger type expects two trigger value inside the `trigger_values`
Sample `orders`:
```
[
  {
    "exchange": "NSE",
    "tradingsymbol": "INFY",
    "transaction_type": "SELL",
    "quantity": 1,
    "order_type": "LIMIT",
    "product": "CNC",
    "price": 702.5
  },
  {
    "exchange": "NSE",
    "tradingsymbol": "INFY",
    "transaction_type": "SELL",
    "quantity": 1,
    "order_type": "LIMIT",
    "product": "CNC",
    "price": 798.5
  }
]

```

## Retrieving triggers[¶](https://kite.trade/docs/connect/v3/gtt/#retrieving-triggers "Permanent link")
Active GTTs and GTTs in others states (previous 7 days) can be obtained by a GET API call to the `/triggers/gtt` endpoint.
```
curl  "https://api.kite.trade/gtt/triggers" \
    -H "X-Kite-Version: 3" \
    -H "Authorization: token api_key:access_token"

```

```
{
    "status": "success",
    "data": [
        {
            "id": 112127,
            "user_id": "XX0000",
            "parent_trigger": null,
            "type": "single",
            "created_at": "2019-09-12 13:25:16",
            "updated_at": "2019-09-12 13:25:16",
            "expires_at": "2020-09-12 13:25:16",
            "status": "active",
            "condition": {
                "exchange": "NSE",
                "last_price": 798,
                "tradingsymbol": "INFY",
                "trigger_values": [
                    702
                ],
                "instrument_token": 408065
            },
            "orders": [
                {
                    "exchange": "NSE",
                    "tradingsymbol": "INFY",
                    "product": "CNC",
                    "order_type": "LIMIT",
                    "transaction_type": "BUY",
                    "quantity": 1,
                    "price": 702.5,
                    "result": null
                }
            ],
            "meta": {}
        },
        {
            "id": 105099,
            "user_id": "XX0000",
            "parent_trigger": null,
            "type": "two-leg",
            "created_at": "2019-09-09 15:13:22",
            "updated_at": "2019-09-09 15:15:08",
            "expires_at": "2020-01-01 12:00:00",
            "status": "triggered",
            "condition": {
                "exchange": "NSE",
                "last_price": 102.6,
                "tradingsymbol": "RAIN",
                "trigger_values": [
                    102.0,
                    103.7
                ],
                "instrument_token": 3926273
            },
            "orders": [
                {
                    "exchange": "NSE",
                    "tradingsymbol": "RAIN",
                    "product": "CNC",
                    "order_type": "LIMIT",
                    "transaction_type": "SELL",
                    "quantity": 1,
                    "price": 1,
                    "result": null
                },
                {
                    "exchange": "NSE",
                    "tradingsymbol": "RAIN",
                    "product": "CNC",
                    "order_type": "LIMIT",
                    "transaction_type": "SELL",
                    "quantity": 1,
                    "price": 1,
                    "result": {
                        "account_id": "XX0000",
                        "exchange": "NSE",
                        "tradingsymbol": "RAIN",
                        "validity": "DAY",
                        "product": "CNC",
                        "order_type": "LIMIT",
                        "transaction_type": "SELL",
                        "quantity": 1,
                        "price": 1,
                        "meta": "{\"app_id\":12617,\"gtt\":105099}",
                        "timestamp": "2019-09-09 15:15:08",
                        "triggered_at": 103.7,
                        "order_result": {
                            "status": "failed",
                            "order_id": "",
                            "rejection_reason": "Your order price is lower than the current lower circuit limit of 70.65. Place an order within the daily range."
                        }
                    }
                }
            ],
            "meta": null
        }
    ]
}

```

## Retrieve trigger[¶](https://kite.trade/docs/connect/v3/gtt/#retrieve-trigger "Permanent link")
Given a GTT ID, the GET API call to this endpoint will return details of the trigger irrespective of the age or [status](https://kite.trade/docs/connect/v3/gtt/#status) of the GTT.
```
curl https://api.kite.trade/gtt/triggers/123 \
    -H 'X-Kite-Version: 3' \
    -H 'Authorization: token api_key:access_token'

```

```
{
    "status": "success",
    "data": {
        "id": 123,
        "user_id": "XX0000",
        "parent_trigger": null,
        "type": "two-leg",
        "created_at": "2019-09-09 15:13:22",
        "updated_at": "2019-09-09 15:15:08",
        "expires_at": "2020-01-01 12:00:00",
        "status": "triggered",
        "condition": {
            "exchange": "NSE",
            "last_price": 102.6,
            "tradingsymbol": "RAIN",
            "trigger_values": [
                102.0,
                103.7
            ],
            "instrument_token": 3926273
        },
        "orders": [
            {
                "exchange": "NSE",
                "tradingsymbol": "RAIN",
                "product": "CNC",
                "order_type": "LIMIT",
                "transaction_type": "SELL",
                "quantity": 1,
                "price": 1,
                "result": null
            },
            {
                "exchange": "NSE",
                "tradingsymbol": "RAIN",
                "product": "CNC",
                "order_type": "LIMIT",
                "transaction_type": "SELL",
                "quantity": 1,
                "price": 1,
                "result": {
                    "account_id": "XX0000",
                    "exchange": "NSE",
                    "tradingsymbol": "RAIN",
                    "validity": "DAY",
                    "product": "CNC",
                    "order_type": "LIMIT",
                    "transaction_type": "SELL",
                    "quantity": 1,
                    "price": 1,
                    "meta": "{\"app_id\":12617,\"gtt\":105099}",
                    "timestamp": "2019-09-09 15:15:08",
                    "triggered_at": 103.7,
                    "order_result": {
                        "status": "failed",
                        "order_id": "",
                        "rejection_reason": "Your order price is lower than the current lower circuit limit of 70.65. Place an order within the daily range."
                    }
                }
            }
        ],
        "meta": null
    }
}

```

### Status[¶](https://kite.trade/docs/connect/v3/gtt/#status "Permanent link")
GTTs can be in the following state
status |
---|---
active | indicates that the trigger is active.
triggered | indicates that the trigger was triggered by core.
disabled | indicates that the trigger is disabled and action is expected from the user.
expired | indicates that the trigger has expired based on its expiry date.
cancelled | indicates that the trigger has been cancelled by our system.
rejected | indicates that the trigger has been rejected by our system.
deleted | indicates that the trigger was deleted by the user.
## Modify trigger[¶](https://kite.trade/docs/connect/v3/gtt/#modify-trigger "Permanent link")
To modify a GTT you need to send a PUT call with updated parameters.
```
curl --request PUT https://api.kite.trade/gtt/triggers/123 \
    -H 'X-Kite-Version: 3' \
    -H 'Authorization: token api_key:access_token' \
    -d 'type=single' \
    -d 'condition={"exchange":"NSE", "tradingsymbol":"INFY", "trigger_values":[701.0], "last_price": 798.0}' \
    -d 'orders=[{"exchange":"NSE", "tradingsymbol": "INFY", "transaction_type": "BUY", "quantity": 1, "order_type": "LIMIT","product": "CNC", "price": 702.5}]'

```

```
{"status":"success","data":{"trigger_id":123}}

```

Note
It is recommended to fetch the trigger using [trigger ID](https://kite.trade/docs/connect/v3/gtt/#retrieve-trigger) and modify the values and send that to the modify endpoint.
## Delete trigger[¶](https://kite.trade/docs/connect/v3/gtt/#delete-trigger "Permanent link")
```
curl --request DELETE https://api.kite.trade/gtt/triggers/123 \
    -H 'X-Kite-Version: 3' \
    -H 'Authorization: token api_key:access_token' \

```

```
{"status":"success","data":{"trigger_id":123}}

```

Copyright © 2015 - 2025, Zerodha Technology Pvt. Ltd.
Made with

