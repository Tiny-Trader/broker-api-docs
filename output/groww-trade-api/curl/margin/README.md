---
source: https://groww.in/trade-api/docs/curl/margin
scraped: true
---
[](https://groww.in/)[![Groww Logo](https://groww.in/favicon32x32-groww.ico)Groww API](https://groww.in/trade-api)
[](https://groww.in/)[![Groww Logo](https://groww.in/favicon32x32-groww.ico)Groww API](https://groww.in/trade-api)
cURL Docs
Documentation for cURL
`⌘``K`
[Documentation](https://groww.in/trade-api/docs)
[Introduction](https://groww.in/trade-api/docs/curl)[Instruments](https://groww.in/trade-api/docs/curl/instruments)[Orders](https://groww.in/trade-api/docs/curl/orders)[Smart Orders](https://groww.in/trade-api/docs/curl/smart-orders)[Portfolio](https://groww.in/trade-api/docs/curl/portfolio)[Margin](https://groww.in/trade-api/docs/curl/margin)[Live Data](https://groww.in/trade-api/docs/curl/live-data)[Historical Data](https://groww.in/trade-api/docs/curl/historical-data)[Backtesting](https://groww.in/trade-api/docs/curl/backtesting)[User](https://groww.in/trade-api/docs/curl/user)[Annexures](https://groww.in/trade-api/docs/curl/annexures)[Changelog](https://groww.in/trade-api/docs/curl/changelog)
Get Available User Margin
# Margin
This guide describes how to calculate required margin for orders and get available user margin using the SDK.
## [Get Available User Margin](https://groww.in/trade-api/docs/curl/margin#get-available-user-margin)
`GET https://api.groww.in/v1/margins/detail/user`
Easily retrieve your margin details using this API.
### [Request](https://groww.in/trade-api/docs/curl/margin#request)
```
# You can also use wget
curl -X GET https://api.groww.in/v1/margins/detail/user \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

### [Response](https://groww.in/trade-api/docs/curl/margin#response)
All prices in rupees.
```
{
  "status": "SUCCESS",
  "payload": {
    "clear_cash": 5000,
    "net_margin_used": 35000,
    "brokerage_and_charges": 200,
    "collateral_used": 3000,
    "collateral_available": 7000,
    "adhoc_margin": 1500,
    "fno_margin_details": {
      "net_fno_margin_used": 15000,
      "span_margin_used": 7000,
      "exposure_margin_used": 4000,
      "future_balance_available": 3000,
      "option_buy_balance_available": 11000,
      "option_sell_balance_available": 1000
    },
    "equity_margin_details": {
      "net_equity_margin_used": 10000,
      "cnc_margin_used": 5000,
      "mis_margin_used": 3000,
      "cnc_balance_available": 9000,
      "mis_balance_available": 1000
    },
    "commodity_margin_details": {
      "commodity_span_margin": 7000,
      "commodity_exposure_margin": 4000,
      "commodity_tender_margin": 2000,
      "commodity_special_margin": 1000,
      "commodity_additional_margin": 3000,
      "commodity_unrealised_m2m": 1500,
      "commodity_realised_m2m": 2500
    }
  }
}
```

#### [Response Schema](https://groww.in/trade-api/docs/curl/margin#response-schema)
Name | Type | Description
---|---|---
status | string | SUCCESS if request is processed successfully, FAILURE if the request failed

clear_cash | decimal | Clear cash available

net_margin_used | decimal | Net margin used

brokerage_and_charges | decimal | Brokerage and charges

collateral_used | decimal | Collateral used

collateral_available | decimal | Collateral available

adhoc_margin | decimal | Adhoc margin available

net_fno_margin_used | decimal | Net FnO margin used

span_margin_used | decimal | Span Margin Used

exposure_margin_used | decimal | Exposure Margin Used

future_balance_available | decimal | Future Balance Available

option_buy_balance_available | decimal | Option Buy Balance Available

option_sell_balance_available | decimal | Option Sell Balance Available

net_equity_margin_used | decimal | Net equity margin used

cnc_margin_used | decimal | CNC margin used

mis_margin_used | decimal | MIS margin used

cnc_balance_available | decimal | CNC balance available

mis_balance_available | decimal | MIS balance available

commodity_span_margin | decimal | Commodity Span Margin

commodity_exposure_margin | decimal | Commodity Exposure Margin

commodity_tender_margin | decimal | Commodity Tender Margin

commodity_special_margin | decimal | Commodity Special Margin

commodity_additional_margin | decimal | Commodity Additional Margin

commodity_unrealised_m2m | decimal | Commodity Unrealised Mark-to-Market

commodity_realised_m2m | decimal | Commodity Realised Mark-to-Market

## [Required Margin For Order](https://groww.in/trade-api/docs/curl/margin#required-margin-for-order)
`POST https://api.groww.in/v1/margins/detail/orders`
Calculate the required margin for a single order or basket of orders using this API. Basket orders are supported for `FNO` and `COMMODITY` segments.
### [Request](https://groww.in/trade-api/docs/curl/margin#request-1)
```
# You can also use wget
curl -X POST https://api.groww.in/v1/margins/detail/orders?segment=CASH \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

### [Body parameter](https://groww.in/trade-api/docs/curl/margin#body-parameter)
```
[
  {
    "trading_symbol": "WIPRO",
    "transaction_type": "BUY",
    "quantity": 1,
    "price": 100, // Optional: Price (include for limit orders; omit or adjust if not applicable).
    "order_type": "LIMIT",
    "product": "CNC",
    "exchange": "NSE"
  }
]
```

#### [Request schema](https://groww.in/trade-api/docs/curl/margin#request-schema)
Name | Type | Description
---|---|---
trading_symbol `*` | string | Trading Symbol of the instrument as defined by the exchange

quantity `*` | integer | Quantity of the instrument to order

price | decimal | Price of the instrument in rupees case of Limit order

exchange `*` | string |  [Stock exchange](https://groww.in/trade-api/docs/curl/annexures#exchange)

segment `*` | string |  [Segment](https://groww.in/trade-api/docs/curl/annexures#segment) of the instrument such as CASH, FNO, COMMODITY etc.

product `*` | string |  [Product type](https://groww.in/trade-api/docs/curl/annexures#product)

order_type `*` | string |  [Order type](https://groww.in/trade-api/docs/curl/annexures#order-type)

transaction_type `*` | string |  [Transaction type](https://groww.in/trade-api/docs/curl/annexures#transaction-type) of the trade
`*`required parameters
### [Response](https://groww.in/trade-api/docs/curl/margin#response-1)
All prices in rupees.
```
{
  "status": "SUCCESS",
  "payload": {
    "exposure_required": 1000,
    "span_required": 1000,
    "option_buy_premium": 140,
    "brokerage_and_charges": 15,
    "total_requirement": 2115,
    "cash_cnc_margin_required": 310,
    "cash_mis_margin_required": 800,
    "physical_delivery_margin_requirement": 100
  }
}
```

#### [Response Schema](https://groww.in/trade-api/docs/curl/margin#response-schema-1)
Name | Type | Description
---|---|---
status | string | SUCCESS if request is processed successfully, FAILURE if the request failed

exposure_required | decimal | Required exposure for the order

span_required | decimal | Required span margin for the order

option_buy_premium | decimal | Buy premium required for the order

brokerage_and_charges | decimal | Brokerage and Charges applied for the orders

total_requirement | decimal | Net margin required

cash_cnc_margin_required | decimal | Margin required applicable for CNC orders

cash_mis_margin_required | decimal | Margin required applicable for MIS orders

physical_delivery_margin_requirement | decimal | Physical delivery margin required if applicable

[Previous Portfolio](https://groww.in/trade-api/docs/curl/portfolio)[Next Live Data](https://groww.in/trade-api/docs/curl/live-data)
[Get Available User Margin](https://groww.in/trade-api/docs/curl/margin#get-available-user-margin)[Required Margin For Order](https://groww.in/trade-api/docs/curl/margin#required-margin-for-order)

