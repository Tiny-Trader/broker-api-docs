---
source: https://groww.in/trade-api/docs/curl/portfolio
scraped: true
---
[](https://groww.in/)[![Groww Logo](https://groww.in/favicon32x32-groww.ico)Groww API](https://groww.in/trade-api)
[](https://groww.in/)[![Groww Logo](https://groww.in/favicon32x32-groww.ico)Groww API](https://groww.in/trade-api)
cURL Docs
Documentation for cURL
`⌘``K`
[Documentation](https://groww.in/trade-api/docs)
[Introduction](https://groww.in/trade-api/docs/curl)[Instruments](https://groww.in/trade-api/docs/curl/instruments)[Orders](https://groww.in/trade-api/docs/curl/orders)[Smart Orders](https://groww.in/trade-api/docs/curl/smart-orders)[Portfolio](https://groww.in/trade-api/docs/curl/portfolio)[Margin](https://groww.in/trade-api/docs/curl/margin)[Live Data](https://groww.in/trade-api/docs/curl/live-data)[Historical Data](https://groww.in/trade-api/docs/curl/historical-data)[Backtesting](https://groww.in/trade-api/docs/curl/backtesting)[User](https://groww.in/trade-api/docs/curl/user)[Annexures](https://groww.in/trade-api/docs/curl/annexures)[Changelog](https://groww.in/trade-api/docs/curl/changelog)
Get Holdings
# Portfolio
Get detailed information about your holdings and positions.
## [Get Holdings](https://groww.in/trade-api/docs/curl/portfolio#get-holdings)
`GET https://api.groww.in/v1/holdings/user`
This API can be used to retrieve the current stock holdings of the user stored in the user's DEMAT account
### [Request](https://groww.in/trade-api/docs/curl/portfolio#request)
```
# You can also use wget
curl -X GET https://api.groww.in/v1/holdings/user \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

### [Response](https://groww.in/trade-api/docs/curl/portfolio#response)
```
{
  "status": "SUCCESS",
  "payload": {
    "holdings": [
      {
        "isin": "INE545U01014",
        "trading_symbol": "RELIANCE",
        "quantity": 10,
        "average_price": 100,
        "pledge_quantity": 2,
        "demat_locked_quantity": 1,
        "groww_locked_quantity": 1.5,
        "repledge_quantity": 0.5,
        "t1_quantity": 3,
        "demat_free_quantity": 5,
        "corporate_action_additional_quantity": 1,
        "active_demat_transfer_quantity": 1
      }
    ]
  }
}
```

#### [Response Schema](https://groww.in/trade-api/docs/curl/portfolio#response-schema)
Name | Type | Description
---|---|---
status | string | SUCCESS if request is processed successfully, FAILURE if the request failed

isin | string | The ISIN (International Securities Identification number) of the symbol

trading_symbol | string | The trading symbol of the holding

quantity | integer | The net quantity of the holding

average_price | decimal | The average price of the holding in Rupees

pledge_quantity | decimal | The pledged quantity of the holding

demat_locked_quantity | decimal | The demat locked quantity of the holding

groww_locked_quantity | decimal | The Groww locked quantity of the holding

repledge_quantity | decimal | The repledged quantity of the holding

t1_quantity | decimal | The T1 quantity of the holding

demat_free_quantity | decimal | The demat free quantity of the holding

corporate_action_additional_quantity | integer | The corporate action additional quantity of the holding

active_demat_transfer_quantity | integer | The active demat transfer quantity of the holding

## [Get Position for User](https://groww.in/trade-api/docs/curl/portfolio#get-position-for-user)
`GET https://api.groww.in/v1/positions/user`
This API can be used to get the positions of the user. Positions are the assets that the user holds in his/her account.
### [Request](https://groww.in/trade-api/docs/curl/portfolio#request-1)
```
# You can also use wget
curl -X GET https://api.groww.in/v1/positions/user \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

#### [Request schema](https://groww.in/trade-api/docs/curl/portfolio#request-schema)
Name | Type | Description
---|---|---
segment | string |  [Segment](https://groww.in/trade-api/docs/curl/annexures#segment) of the instrument such as CASH, FNO, COMMODITY etc.
`CASH` `FNO` `COMMODITY`
`*`required parameters
### [Response](https://groww.in/trade-api/docs/curl/portfolio#response-1)
```
{
  "status": "SUCCESS",
  "payload": {
    "positions": [
      {
        "trading_symbol": "RELIANCE",
        "credit_quantity": 10,
        "credit_price": 12500,
        "debit_quantity": 5,
        "debit_price": 12000,
        "carry_forward_credit_quantity": 8,
        "carry_forward_credit_price": 12300,
        "carry_forward_debit_quantity": 3,
        "carry_forward_debit_price": 11800,
        "exchange": "NSE",
        "symbol_isin": "INE123A01016",
        "quantity": 15,
        "product": "CNC",
        "net_carry_forward_quantity": 10,
        "net_price": 12400,
        "net_carry_forward_price": 12200,
        "realised_pnl": 500
      }
    ]
  }
}
```

#### [Response Schema](https://groww.in/trade-api/docs/curl/portfolio#response-schema-1)
Name | Type | Description
---|---|---
status | string | SUCCESS if request is processed successfully, FAILURE if the request failed

trading_symbol | string | Trading symbol of the instrument

segment | string |  [Segment](https://groww.in/trade-api/docs/curl/annexures#segment) of the instrument such as CASH, FNO, COMMODITY etc.
credit_quantity | int | Quantity of credited instruments

credit_price | int | Average price in rupees of credited instruments

debit_quantity | int | Quantity of debited instruments

debit_price | int | Average price in rupees of debited instruments

carry_forward_credit_quantity | int | Quantity of carry forward credited instruments

carry_forward_credit_price | int | Average price in rupees of carry forward credited instruments

carry_forward_debit_quantity | int | Quantity of carry forward debited instruments

carry_forward_debit_price | int | Average price in rupees of carry forward debited instruments

exchange | string |  [Stock exchange](https://groww.in/trade-api/docs/curl/annexures#exchange)

symbol_isin | string | ISIN (International Securities Identification number) of the symbol

quantity | int | Net quantity of instruments

product | string |  [Product type](https://groww.in/trade-api/docs/curl/annexures#product)

net_carry_forward_quantity | int | Net carry forward quantity of instruments

net_price | int | Net average price in rupees of instruments

net_carry_forward_price | int | Net average price in rupees of carry forward instruments

realised_pnl | int | Realised profit and loss in rupees for the instrument

## [Get Position for trading Symbol](https://groww.in/trade-api/docs/curl/portfolio#get-position-for-trading-symbol)
`GET https://api.groww.in/v1/positions/trading-symbol`
This API can be used to get the positions of the user for a particular instrument.
### [Request](https://groww.in/trade-api/docs/curl/portfolio#request-2)
```
# You can also use wget
curl -X GET https://api.groww.in/v1/positions/trading-symbol?trading_symbol=string&segment=CASH \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

#### [Request schema](https://groww.in/trade-api/docs/curl/portfolio#request-schema-1)
Name | Type | Description
---|---|---
status | string | SUCCESS if request is processed successfully, FAILURE if the request failed

trading_symbol `*` | string | Trading Symbol of the instrument as defined by the exchange

segment | string |  [Segment](https://groww.in/trade-api/docs/curl/annexures#segment) of the instrument such as CASH, FNO, COMMODITY etc.
`CASH` `FNO` `COMMODITY`
`*`required parameters
### [Response](https://groww.in/trade-api/docs/curl/portfolio#response-2)
```
{
  "status": "SUCCESS",
  "payload": {
    "positions": [
      {
        "trading_symbol": "RELIANCE",
        "credit_quantity": 10,
        "credit_price": 12500,
        "debit_quantity": 5,
        "debit_price": 12000,
        "carry_forward_credit_quantity": 8,
        "carry_forward_credit_price": 12300,
        "carry_forward_debit_quantity": 3,
        "carry_forward_debit_price": 11800,
        "exchange": "NSE",
        "symbol_isin": "INE123A01016",
        "quantity": 15,
        "product": "CNC",
        "net_carry_forward_quantity": 10,
        "net_price": 12400,
        "net_carry_forward_price": 12200,
        "realised_pnl": 500
      }
    ]
  }
}
```

#### [Response Schema](https://groww.in/trade-api/docs/curl/portfolio#response-schema-2)
Name | Type | Description
---|---|---
trading_symbol | string | Trading symbol of the instrument.

segment | string |  [Segment](https://groww.in/trade-api/docs/curl/annexures#segment) of the instrument such as CASH, FNO, COMMODITY etc.
credit_quantity | int | Quantity of credited instruments

credit_price | int | Average price in rupees of credited instruments

debit_quantity | int | Quantity of debited instruments

debit_price | int | Average price in rupees of debited instruments

carry_forward_credit_quantity | int | Quantity of carry forward credited instruments

carry_forward_credit_price | int | Average price in rupees of carry forward credited instruments

carry_forward_debit_quantity | int | Quantity of carry forward debited instruments

carry_forward_debit_price | int | Average price in rupees of carry forward debited instruments

exchange | string |  [Stock exchange](https://groww.in/trade-api/docs/curl/annexures#exchange)

symbol_isin | string | ISIN (International Securities Identification number) of the symbol

quantity | int | Net quantity of instruments

product | string |  [Product type](https://groww.in/trade-api/docs/curl/annexures#product)

net_carry_forward_quantity | int | Net carry forward quantity of instruments

net_price | int | Net average price in rupees of instruments

net_carry_forward_price | int | Net average price in rupees of carry forward instruments

realised_pnl | int | Realised profit and loss in rupees for the instrument

[Previous Smart Orders](https://groww.in/trade-api/docs/curl/smart-orders)[Next Margin](https://groww.in/trade-api/docs/curl/margin)
[Get Holdings](https://groww.in/trade-api/docs/curl/portfolio#get-holdings)[Get Position for User](https://groww.in/trade-api/docs/curl/portfolio#get-position-for-user)[Get Position for trading Symbol](https://groww.in/trade-api/docs/curl/portfolio#get-position-for-trading-symbol)

