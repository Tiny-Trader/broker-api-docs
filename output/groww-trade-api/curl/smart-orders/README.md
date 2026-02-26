---
source: https://groww.in/trade-api/docs/curl/smart-orders
scraped: true
---
[](https://groww.in/)[![Groww Logo](https://groww.in/favicon32x32-groww.ico)Groww API](https://groww.in/trade-api)
[](https://groww.in/)[![Groww Logo](https://groww.in/favicon32x32-groww.ico)Groww API](https://groww.in/trade-api)
cURL Docs
Documentation for cURL
`⌘``K`
[Documentation](https://groww.in/trade-api/docs)
[Introduction](https://groww.in/trade-api/docs/curl)[Instruments](https://groww.in/trade-api/docs/curl/instruments)[Orders](https://groww.in/trade-api/docs/curl/orders)[Smart Orders](https://groww.in/trade-api/docs/curl/smart-orders)[Portfolio](https://groww.in/trade-api/docs/curl/portfolio)[Margin](https://groww.in/trade-api/docs/curl/margin)[Live Data](https://groww.in/trade-api/docs/curl/live-data)[Historical Data](https://groww.in/trade-api/docs/curl/historical-data)[Backtesting](https://groww.in/trade-api/docs/curl/backtesting)[User](https://groww.in/trade-api/docs/curl/user)[Annexures](https://groww.in/trade-api/docs/curl/annexures)[Changelog](https://groww.in/trade-api/docs/curl/changelog)
Create GTT
# Smart Orders
Create, modify, cancel, get and list Smart Orders using simple cURL recipes.
Smart Orders help you automate entries/exits with minimal code. Two types are supported today:
  * GTT (Good Till Triggered): Triggers a single order when price crosses your trigger
  * OCO (One Cancels the Other): Places target and stop-loss together; execution of one cancels the other

**Note:** The `COMMODITY` segment is not supported for Smart Orders. OCO orders for `CASH` segment are currently not supported.
## [Create GTT](https://groww.in/trade-api/docs/curl/smart-orders#create-gtt)
`POST https://api.groww.in/v1/order-advance/create`
Create a GTT that arms a single order when your trigger condition is met.
### [Request](https://groww.in/trade-api/docs/curl/smart-orders#request)
```
curl -X POST https://api.groww.in/v1/order-advance/create \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

#### [Body parameter](https://groww.in/trade-api/docs/curl/smart-orders#body-parameter)
```
{
  "reference_id": "sref-unique-123",
  "smart_order_type": "GTT",
  "segment": "CASH",
  "trading_symbol": "TCS",
  "quantity": 10,
  "trigger_price": "3985.00",
  "trigger_direction": "DOWN",
  "order": {"order_type": "LIMIT", "price": "3990.00", "transaction_type": "BUY"},
  "product_type": "CNC",
  "exchange": "NSE",
  "duration": "DAY"
}
```

#### [Request schema](https://groww.in/trade-api/docs/curl/smart-orders#request-schema)
Name | Type | Description
---|---|---
reference_id `*` | string | User-provided alphanumeric string (8-20 characters) that serves as an idempotency key, with at most two hyphens (-) allowed.
smart_order_type `*` | string | Set to `GTT` to create a Good‑Till‑Triggered smart order. Example: `GTT`.
segment `*` | string | Segment for which the order will be placed. See [Segment](https://groww.in/trade-api/docs/curl/annexures#segment). Examples: `CASH`, `FNO`.
trading_symbol `*` | string | Trading Symbol of the instrument as defined by the exchange
quantity `*` | integer | Quantity for the post‑trigger order. For FNO, must respect lot size. Examples: `10`, `50`.
trigger_price `*` | string | Trigger price as a decimal string. Example: `3985.00`.
trigger_direction `*` | string | Direction to monitor relative to the trigger price. Examples: `UP`, `DOWN`.
order.order_type `*` | string | Post‑trigger execution order type. See [Order type](https://groww.in/trade-api/docs/curl/annexures#order-type). Examples: `LIMIT`, `SL`.
order.price | string | Post‑trigger limit price (required if `order.order_type` is `LIMIT` or `SL`). Example: `3990.00`.
order.transaction_type `*` | string | Post‑trigger transaction type. See [Transaction type](https://groww.in/trade-api/docs/curl/annexures#transaction-type). Examples: `BUY`, `SELL`.
child_legs | object | Optional child legs for bracket orders (target/stop‑loss).
product_type `*` | string | Product for the post‑trigger order. See [Product type](https://groww.in/trade-api/docs/curl/annexures#product). Examples: `CNC`, `MIS`.
exchange `*` | string | Exchange where the instrument is traded. See [Exchange](https://groww.in/trade-api/docs/curl/annexures#exchange). Examples: `NSE`.
duration `*` | string | Validity of the post‑trigger order. See [Validity](https://groww.in/trade-api/docs/curl/annexures#validity). Example: `DAY`.
`*`required parameters
### [Response (201)](https://groww.in/trade-api/docs/curl/smart-orders#response-201)
```
{
  "status": "SUCCESS",
  "payload": {
    "smart_order_id": "gtt_91a7f4",
    "smart_order_type": "GTT",
    "status": "ACTIVE",
    "trading_symbol": "TCS",
    "exchange": "NSE",
    "quantity": 10,
    "product_type": "CNC",
    "duration": "DAY",
    "order": {"order_type": "LIMIT", "price": "3990.00", "transaction_type": "BUY"},
    "trigger_direction": "DOWN",
    "trigger_price": "3985.00",
    "is_cancellation_allowed": true,
    "is_modification_allowed": true,
    "created_at": "2025-09-30T07:00:00",
    "expire_at": "2026-09-30T07:00:00",
    "triggered_at": null,
    "updated_at": "2025-09-30T07:00:00"
  }
}
```

Schema reference: [Smart Order Response (GTT)](https://groww.in/trade-api/docs/curl/smart-orders#smart-order-response-gtt).
## [Create OCO](https://groww.in/trade-api/docs/curl/smart-orders#create-oco)
`POST https://api.groww.in/v1/order-advance/create`
Create an OCO to protect or exit positions with target and stop-loss.
### [Request](https://groww.in/trade-api/docs/curl/smart-orders#request-1)
```
curl -X POST https://api.groww.in/v1/order-advance/create \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

#### [Body parameter](https://groww.in/trade-api/docs/curl/smart-orders#body-parameter-1)
```
{
  "reference_id": "sref-unique-456",
  "smart_order_type": "OCO",
  "segment": "FNO",
  "trading_symbol": "NIFTY25OCT24000CE",
  "quantity": 50,
  "net_position_quantity": 50,
  "transaction_type": "SELL",
  "target": {"trigger_price": "120.50", "order_type": "LIMIT", "price": "121.00"},
  "stop_loss": {"trigger_price": "95.00", "order_type": "SL_M", "price": null},
  "product_type": "MIS",
  "exchange": "NSE",
  "duration": "DAY"
}
```

#### [Request schema](https://groww.in/trade-api/docs/curl/smart-orders#request-schema-1)
Name | Type | Description
---|---|---
reference_id `*` | string | User-provided alphanumeric string (8-20 characters) that serves as an idempotency key, with at most two hyphens (-) allowed.
smart_order_type `*` | string | Set to `OCO` to create a One‑Cancels‑Other smart order (target + stop‑loss). Example: `OCO`.
segment `*` | string | Segment for which the order will be placed. See [Segment](https://groww.in/trade-api/docs/curl/annexures#segment). Examples: `FNO`, `CASH`.
trading_symbol `*` | string | Trading Symbol of the instrument as defined by the exchange
quantity `*` | integer | Total quantity for both legs. Must be ≤ `abs(net_position_quantity)`. Example: `50`.
net_position_quantity `*` | integer | Your current net position in this symbol. Used to derive leg directions and validate quantity. Example: `50`.
transaction_type `*` | string | Direction of protection/exit for your position. See [Transaction type](https://groww.in/trade-api/docs/curl/annexures#transaction-type). Examples: `BUY`, `SELL`.
target.trigger_price `*` | string | Take‑profit trigger price (decimal string). Example: `120.50`.
target.order_type `*` | string | Order type for the target leg. See [Order type](https://groww.in/trade-api/docs/curl/annexures#order-type). Examples: `LIMIT`, `MARKET`.
target.price | string | Target leg limit price (required if `target.order_type` = `LIMIT`). Example: `121.00`.
stop_loss.trigger_price `*` | string | Stop‑loss trigger price (decimal string). Example: `95.00`.
stop_loss.order_type `*` | string | Order type for the stop‑loss leg. See [Order type](https://groww.in/trade-api/docs/curl/annexures#order-type). Examples: `SL`, `SL_M`.
stop_loss.price | string | Stop‑loss leg limit price (required if `stop_loss.order_type` = `SL`). Example: `94.50`.
product_type `*` | string | Product for the OCO. See [Product type](https://groww.in/trade-api/docs/curl/annexures#product). Note: For OCO in cash segment, only `MIS` is supported currently.
exchange `*` | string | Exchange for this instrument. See [Exchange](https://groww.in/trade-api/docs/curl/annexures#exchange). Example: `NSE`.
duration `*` | string | Validity for both legs. See [Validity](https://groww.in/trade-api/docs/curl/annexures#validity). Example: `DAY`.
`*`required parameters
### [Response (201)](https://groww.in/trade-api/docs/curl/smart-orders#response-201-1)
```
{
  "status": "SUCCESS",
  "payload": {
    "smart_order_id": "oco_a12bc3",
    "smart_order_type": "OCO",
    "status": "ACTIVE",
    "trading_symbol": "NIFTY25OCT24000CE",
    "exchange": "NSE",
    "quantity": 50,
    "product_type": "MIS",
    "duration": "DAY",
    "target": {"trigger_price": "120.50", "order_type": "LIMIT", "price": "121.00"},
    "stop_loss": {"trigger_price": "95.00", "order_type": "SL_M", "price": null},
    "created_at": "2025-09-30T07:00:00",
    "expire_at": null,
    "triggered_at": null,
    "updated_at": "2025-09-30T07:00:00"
  }
}
```

Schema reference: [Smart Order Response (OCO)](https://groww.in/trade-api/docs/curl/smart-orders#smart-order-response-oco).
### [Notes](https://groww.in/trade-api/docs/curl/smart-orders#notes)
  * `quantity` must be ≤ `abs(net_position_quantity)`.
  * If a leg executes, the other cancels automatically.

## [Modify Smart Order](https://groww.in/trade-api/docs/curl/smart-orders#modify-smart-order)
`PUT https://api.groww.in/v1/order-advance/modify/{smart_order_id}`
Modify contracts differ by flow. Only the fields listed below are honoured; everything else is ignored or rejected. Use cancel + create when you need changes outside of these lists.
### [Modifiable Fields - GTT](https://groww.in/trade-api/docs/curl/smart-orders#modifiable-fields---gtt)
  * `quantity` - Updated order quantity
  * `trigger_price` - Updated trigger price threshold
  * `trigger_direction` - Updated direction
  * `order.order_type` - Updated order type
  * `order.price` - Updated limit price (required for `LIMIT`/`SL` types; set to `null` for `MARKET`/`SL_M`)
  * `child_legs` - Updated bracket order legs (optional; all child leg fields are modifiable if provided)

### [Modifiable Fields - OCO](https://groww.in/trade-api/docs/curl/smart-orders#modifiable-fields---oco)
  * `quantity` - Updated order quantity
  * `duration` - Updated validity
  * `product_type` - Updated product (e.g., MIS ↔ NRML for FNO; CASH OCO only supports MIS)
  * `target.trigger_price` - Updated profit target trigger price
  * `stop_loss.trigger_price` - Updated stop-loss trigger price

### [Request (GTT)](https://groww.in/trade-api/docs/curl/smart-orders#request-gtt)
```
curl -X PUT https://api.groww.in/v1/order-advance/modify/gtt_91a7f4 \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

#### [Body parameter (GTT)](https://groww.in/trade-api/docs/curl/smart-orders#body-parameter-gtt)
```
{
  "smart_order_type": "GTT",
  "segment": "CASH",
  "quantity": 12,
  "trigger_price": "3980.00",
  "trigger_direction": "DOWN",
  "order": {"order_type": "LIMIT", "price": "3985.00", "transaction_type": "BUY"}
}
```

#### [Request schema (GTT)](https://groww.in/trade-api/docs/curl/smart-orders#request-schema-gtt)
Name | Type | Description
---|---|---
smart_order_type `*` | string | Set to `GTT` to modify a Good‑Till‑Triggered smart order. Example: `GTT`.
segment `*` | string | Segment of the order (for routing). See [Segment](https://groww.in/trade-api/docs/curl/annexures#segment). Examples: `CASH`, `FNO`.
quantity | integer | Updated quantity.
trigger_price | string | Updated trigger price (decimal string).
trigger_direction | string | Updated trigger direction. Examples: `UP`, `DOWN`.
order.order_type | string | Updated order type. See [Order type](https://groww.in/trade-api/docs/curl/annexures#order-type).
order.price | string | Updated limit price (required if `order.order_type` is `LIMIT` or `SL`).
order.transaction_type | string | Transaction type (required but not modifiable). See [Transaction type](https://groww.in/trade-api/docs/curl/annexures#transaction-type).
child_legs | object | Updated child legs for bracket orders (target/stop‑loss).
`*`required parameters
### [Request (OCO)](https://groww.in/trade-api/docs/curl/smart-orders#request-oco)
```
curl -X PUT https://api.groww.in/v1/order-advance/modify/oco_a12bc3 \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

#### [Body parameter (OCO)](https://groww.in/trade-api/docs/curl/smart-orders#body-parameter-oco)
```
{
  "smart_order_type": "OCO",
  "segment": "FNO",
  "duration": "DAY",
  "quantity": 40,
  "product_type": "MIS",
  "target": { "trigger_price": "122.00" },
  "stop_loss": { "trigger_price": "97.50" }
}
```

#### [Request schema (OCO)](https://groww.in/trade-api/docs/curl/smart-orders#request-schema-oco)
Name | Type | Description
---|---|---
smart_order_type `*` | string | Set to `OCO` to modify a One‑Cancels‑Other smart order. Example: `OCO`.
segment `*` | string | Segment of the order (for routing). See [Segment](https://groww.in/trade-api/docs/curl/annexures#segment). Examples: `FNO`, `CASH`.
duration | string | Updated validity. See [Validity](https://groww.in/trade-api/docs/curl/annexures#validity). Modifiable for OCO.
quantity | integer | Updated total quantity.
product_type | string | Updated product. See [Product type](https://groww.in/trade-api/docs/curl/annexures#product). Modifiable for OCO.
target.trigger_price | string | Updated target trigger price (decimal string).
stop_loss.trigger_price | string | Updated stop‑loss trigger price (decimal string).
`*`required parameters
### [Response (202)](https://groww.in/trade-api/docs/curl/smart-orders#response-202)
```
{
  "status": "SUCCESS",
  "payload": { "smart_order_id": "oco_a12bc3", "smart_order_type": "OCO", "status": "ACTIVE", "quantity": 40 }
}
```

Schema reference: [Smart Order Response (GTT)](https://groww.in/trade-api/docs/curl/smart-orders#smart-order-response-gtt) or [Smart Order Response (OCO)](https://groww.in/trade-api/docs/curl/smart-orders#smart-order-response-oco).
### [Modify vs Cancel-Create](https://groww.in/trade-api/docs/curl/smart-orders#modify-vs-cancel-create)
What you need to change | GTT | OCO | Action
---|---|---|---
Quantity | ✅ Modify | ✅ Modify | Use modify
Trigger price | ✅ Modify | ✅ Modify (both legs) | Use modify
Trigger direction | ✅ Modify | N/A | Use modify
Order type | ✅ Modify | ❌ Not modifiable | GTT: modify; OCO: cancel+create
Limit price | ✅ Modify | ❌ Not modifiable | GTT: modify; OCO: cancel+create
Duration/validity | ❌ Not modifiable | ✅ Modify | OCO: modify; GTT: cancel+create
Product type | ❌ Not modifiable | ✅ Modify | OCO: modify; GTT: cancel+create
Symbol/contract | ❌ Not modifiable | ❌ Not modifiable | Cancel + create
Exchange | ❌ Not modifiable | ❌ Not modifiable | Cancel + create
Segment | ❌ Not modifiable | ❌ Not modifiable | Cancel + create
Smart order type (GTT ↔ OCO) | ❌ Not modifiable | ❌ Not modifiable | Cancel + create
> **Note:** When a field is marked as "Not modifiable" (❌), you must cancel the existing smart order and create a new one with the desired changes. The "N/A" designation indicates that the feature does not apply to that smart order type.
## [Cancel Smart Order](https://groww.in/trade-api/docs/curl/smart-orders#cancel-smart-order)
`POST https://api.groww.in/v1/order-advance/cancel/{segment}/{smart_order_type}/{smart_order_id}`
Cancel any active smart order.
### [Request](https://groww.in/trade-api/docs/curl/smart-orders#request-2)
```
curl -X POST https://api.groww.in/v1/order-advance/cancel/CASH/GTT/gtt_91a7f4 \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

#### [Request schema](https://groww.in/trade-api/docs/curl/smart-orders#request-schema-2)
Name | Type | Description
---|---|---
segment `*` | string | Segment of the smart order to cancel. See [Segment](https://groww.in/trade-api/docs/curl/annexures#segment). Examples: `CASH`, `FNO`.
smart_order_type `*` | string | Smart order type. Examples: `GTT`, `OCO`.
smart_order_id `*` | string | Smart order identifier. Example: `gtt_91a7f4`.
`*`required parameters
### [Response (202)](https://groww.in/trade-api/docs/curl/smart-orders#response-202-1)
```
{
  "status": "SUCCESS",
  "payload": { "smart_order_id": "gtt_91a7f4", "smart_order_type": "GTT", "status": "CANCELLED" }
}
```

Schema reference: [Smart Order Response (GTT)](https://groww.in/trade-api/docs/curl/smart-orders#smart-order-response-gtt) or [Smart Order Response (OCO)](https://groww.in/trade-api/docs/curl/smart-orders#smart-order-response-oco).
#### [Response Schema](https://groww.in/trade-api/docs/curl/smart-orders#response-schema)
Name | Type | Description
---|---|---
status | string | SUCCESS if processed successfully, FAILURE otherwise
smart_order_id | string | Smart order identifier
smart_order_type | string | Smart order type. Examples: `GTT`, `OCO`.
status | string |  `CANCELLED` on success
## [Get Smart Order](https://groww.in/trade-api/docs/curl/smart-orders#get-smart-order)
`GET https://api.groww.in/v1/order-advance/status/{segment}/{smart_order_type}/internal/{smart_order_id}`
### [Request](https://groww.in/trade-api/docs/curl/smart-orders#request-3)
```
curl -X GET \
  'https://api.groww.in/v1/order-advance/status/CASH/GTT/internal/gtt_91a7f4' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

#### [Request schema](https://groww.in/trade-api/docs/curl/smart-orders#request-schema-3)
Name | Type | Description
---|---|---
segment `*` | string | Segment of the smart order to fetch. See [Segment](https://groww.in/trade-api/docs/curl/annexures#segment). Examples: `CASH`, `FNO`.
smart_order_type `*` | string | Smart order type. Examples: `GTT`, `OCO`.
smart_order_id `*` | string | Smart order identifier. Example: `gtt_91a7f4`.
`*`required parameters
### [Response (200)](https://groww.in/trade-api/docs/curl/smart-orders#response-200)
```
{
  "status": "SUCCESS",
  "payload": { /* Full smart order object: see schema below */ }
}
```

Schema reference: [Smart Order Response (GTT)](https://groww.in/trade-api/docs/curl/smart-orders#smart-order-response-gtt) or [Smart Order Response (OCO)](https://groww.in/trade-api/docs/curl/smart-orders#smart-order-response-oco).
## [List Smart Orders](https://groww.in/trade-api/docs/curl/smart-orders#list-smart-orders)
`GET https://api.groww.in/v1/order-advance/list`
Filter by type, segment, status and a time window. Pagination is supported.
### [Request](https://groww.in/trade-api/docs/curl/smart-orders#request-4)
```
curl -X GET \
  'https://api.groww.in/v1/order-advance/list?segment=FNO&smart_order_type=OCO&status=ACTIVE&page=0&page_size=10&start_date_time=2025-01-16T09:15:00&end_date_time=2025-01-16T15:30:00' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

#### [Request schema](https://groww.in/trade-api/docs/curl/smart-orders#request-schema-4)
Name | Type | Description
---|---|---
segment | string | Segment to list smart orders for. See [Segment](https://groww.in/trade-api/docs/curl/annexures#segment). Examples: `FNO`, `CASH`.
smart_order_type | string | Smart order type to create/list. Examples: `OCO`, `GTT`. Default: `OCO`.
status | string | Current state filter (live vs past). Examples: `ACTIVE`, `CANCELLED`, `COMPLETED`. Default: `ACTIVE`.
page | integer | Page number starting from 0. Use with `page_size` to paginate long lists. Examples: `0`, `1`. Min: `0`, Max: `500`. Default: `0`.
page_size | integer | Number of records per page. Tune this for your UI/export. Examples: `10`, `25`. Min: `1`, Max: `50`. Default: `10`.
start_date_time | string | Inclusive start of the time window in ISO8601 (`YYYY-MM-DDThh:mm:ss`). Defaults to start of today (server timezone). Examples: `2025-01-16T09:15:00`, `2025-01-16T00:00:00`.
end_date_time | string | Inclusive end of the time window in ISO8601. Must not be before `start_date_time`. Defaults to start of next day (server timezone). Examples: `2025-01-16T15:30:00`, `2025-01-16T23:59:59`.
Validations:
  * `end_date_time` must not be before `start_date_time`.
  * Date range between `start_date_time` and `end_date_time` must not exceed one month.

### [Response (200)](https://groww.in/trade-api/docs/curl/smart-orders#response-200-1)
```
{
  "status": "SUCCESS",
  "payload": {
    "orders": [
      { "smart_order_id": "gtt_91a7f4", "smart_order_type": "GTT", "status": "ACTIVE" }
    ]
  }
}
```

#### [Response Schema](https://groww.in/trade-api/docs/curl/smart-orders#response-schema-1)
Name | Type | Description
---|---|---
status | string | SUCCESS if processed successfully, FAILURE otherwise
orders | array | List of smart orders
orders[] | object | Smart order item (GTT or OCO). See [Smart Order Response (GTT)](https://groww.in/trade-api/docs/curl/smart-orders#smart-order-response-gtt) or [Smart Order Response (OCO)](https://groww.in/trade-api/docs/curl/smart-orders#smart-order-response-oco)
## [Quick Tips](https://groww.in/trade-api/docs/curl/smart-orders#quick-tips)
  * Use a unique `reference_id` per new smart order to avoid accidental duplicates.
  * For symbol/segment/type changes: cancel the old smart order and create a new one.
  * For OCO, ensure `quantity` ≤ `abs(net_position_quantity)`. The leg directions are derived from your net position.

## [Schemas](https://groww.in/trade-api/docs/curl/smart-orders#schemas)
### [Smart Order Response (GTT)](https://groww.in/trade-api/docs/curl/smart-orders#smart-order-response-gtt)
Name | Type | Description
---|---|---
status | string | SUCCESS if processed successfully, FAILURE otherwise
smart_order_id | string | Smart order identifier
smart_order_type | string | Smart order type. Example: `GTT`.
status | string | Smart order status (e.g., `ACTIVE`)
trading_symbol | string | Trading Symbol of the instrument as defined by the exchange
exchange | string | [Stock exchange](https://groww.in/trade-api/docs/curl/annexures#exchange)
quantity | integer | Quantity
product_type | string | [Product type](https://groww.in/trade-api/docs/curl/annexures#product)
duration | string | [Validity](https://groww.in/trade-api/docs/curl/annexures#validity)
order.order_type | string | Order type. See [Order type](https://groww.in/trade-api/docs/curl/annexures#order-type). Examples: `LIMIT`, `SL`.
order.price | string | Price for LIMIT/SL
order.transaction_type | string | See [Transaction type](https://groww.in/trade-api/docs/curl/annexures#transaction-type). Examples: `BUY`, `SELL`.
ltp | number | Last traded price of the instrument
trigger_direction | string | Trigger direction. Examples: `UP`, `DOWN`.
trigger_price | string | Trigger price (decimal string)
segment | string | Market segment
remark | string | Remark or status message
display_name | string | Display name for the instrument
child_legs | object | Child legs for bracket orders (target/stop‑loss)
is_cancellation_allowed | boolean | Whether cancellation is allowed
is_modification_allowed | boolean | Whether modification is allowed
created_at | string | Creation time (ISO 8601)
expire_at | string | Expiry time (ISO 8601)
triggered_at | string | Trigger time (ISO 8601)
updated_at | string | Last updated time (ISO 8601)
### [Smart Order Response (OCO)](https://groww.in/trade-api/docs/curl/smart-orders#smart-order-response-oco)
Name | Type | Description
---|---|---
status | string | SUCCESS if processed successfully, FAILURE otherwise
smart_order_id | string | Smart order identifier
smart_order_type | string | Smart order type. Example: `OCO`.
status | string | Smart order status (e.g., `ACTIVE`)
trading_symbol | string | Trading Symbol of the instrument as defined by the exchange
exchange | string | [Stock exchange](https://groww.in/trade-api/docs/curl/annexures#exchange)
quantity | integer | Quantity of the order to be placed
product_type | string | [Product type](https://groww.in/trade-api/docs/curl/annexures#product)
duration | string | [Validity](https://groww.in/trade-api/docs/curl/annexures#validity)
target.trigger_price | string | Target trigger price (decimal string)
target.order_type | string | Order type. See [Order type](https://groww.in/trade-api/docs/curl/annexures#order-type). Examples: `LIMIT`, `MARKET`.
target.price | string | Target limit price
stop_loss.trigger_price | string | Stop-loss trigger price (decimal string)
stop_loss.order_type | string | Order type. See [Order type](https://groww.in/trade-api/docs/curl/annexures#order-type). Examples: `SL`, `SL_M`.
stop_loss.price | string | Stop-loss limit price
is_cancellation_allowed | boolean | Whether cancellation is allowed
is_modification_allowed | boolean | Whether modification is allowed
created_at | string | Creation time (ISO 8601)
expire_at | string | Expiry time (ISO 8601)
triggered_at | string | Trigger time (ISO 8601)
updated_at | string | Last updated time (ISO 8601)
[Previous Orders](https://groww.in/trade-api/docs/curl/orders)[Next Portfolio](https://groww.in/trade-api/docs/curl/portfolio)
[Create GTT](https://groww.in/trade-api/docs/curl/smart-orders#create-gtt)[Create OCO](https://groww.in/trade-api/docs/curl/smart-orders#create-oco)[Modify Smart Order](https://groww.in/trade-api/docs/curl/smart-orders#modify-smart-order)[Cancel Smart Order](https://groww.in/trade-api/docs/curl/smart-orders#cancel-smart-order)[Get Smart Order](https://groww.in/trade-api/docs/curl/smart-orders#get-smart-order)[List Smart Orders](https://groww.in/trade-api/docs/curl/smart-orders#list-smart-orders)[Quick Tips](https://groww.in/trade-api/docs/curl/smart-orders#quick-tips)[Schemas](https://groww.in/trade-api/docs/curl/smart-orders#schemas)

