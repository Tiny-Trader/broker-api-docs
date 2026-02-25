---
source: https://upstox.com/developer/api-documentation/instruments
scraped: true
---
  * [](https://upstox.com/developer/api-documentation/)

  * The [BOD Instruments](https://upstox.com/developer/api-documentation/instruments#json-files) section provides a list of all instruments available at the beginning of the day.
  * The [MTF Instruments](https://upstox.com/developer/api-documentation/instruments#mtf-instruments) section provides the list of MTF instruments in JSON format.
  * The [MIS Instruments](https://upstox.com/developer/api-documentation/instruments#mis-instruments) section provides the list of MIS instruments in JSON format.
  * The [Suspended instruments](https://upstox.com/developer/api-documentation/instruments#suspended-instruments) section provides the list of Suspended instruments in JSON format.

  * Use `instrument_key` for uniquely identifying instruments, as it remains unique for each instrument. Conversely, `exchange_token` may be reused by the exchange for a different instrument after its expiry.
  * Use Instruments data in JSON format instead of CSV, as its structure has been designed for enhanced robustness and future scalability, making programmatic processing easier.



## JSON files[​](https://upstox.com/developer/api-documentation/instruments/#json-files "Direct link to heading")
These URLs provide access to the complete list of BOD contracts available for trading on Upstox in JSON format.
  * [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.json.gz)
  * [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.json.gz)
  * [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.json.gz)
  * [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.json.gz)



## Suspended Instruments[​](https://upstox.com/developer/api-documentation/instruments/#suspended-instruments "Direct link to heading")
This URL provides access to the list of suspended instruments that are not available for trading on Upstox.
  * [Suspended](https://assets.upstox.com/market-quote/instruments/exchange/suspended-instrument.json.gz)



## MTF Instruments[​](https://upstox.com/developer/api-documentation/instruments/#mtf-instruments "Direct link to heading")
This URL provides access to the list of instruments that are available for Margin Trading Facility (MTF) on Upstox.
  * [MTF](https://assets.upstox.com/market-quote/instruments/exchange/MTF.json.gz)



## MIS Instruments[​](https://upstox.com/developer/api-documentation/instruments/#mis-instruments "Direct link to heading")
This URL provides access to the list of instruments that are available for Margin Intraday Square-off (MIS) on Upstox.
  * [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE_MIS.json.gz)
  * [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE_MIS.json.gz)



### Sample JSON Object[​](https://upstox.com/developer/api-documentation/instruments/#sample-json-object "Direct link to heading")
  * The first four tabs (EQ, Futures, Options, and Index) are all included in the [BOD json file](https://upstox.com/developer/api-documentation/instruments#json-files).

  * EQ
  * Futures
  * Options
  * INDEX
  * Suspended
  * MTF
  * MIS

```
{
  "segment": "NSE_EQ",
  "name": "JOCIL LIMITED",
  "exchange": "NSE",
  "isin": "INE839G01010",
  "instrument_type": "EQ",
  "instrument_key": "NSE_EQ|INE839G01010",
  "lot_size": 1,
  "freeze_quantity": 100000.0,
  "exchange_token": "16927",
  "tick_size": 5.0,
  "trading_symbol": "JOCIL",
  "short_name": "JOCIL",
  "security_type": "NORMAL"
}

```

  * When you're searching for instrument keys within an instrument JSON file, you can employ the `segment` and `instrument_type` parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Equity, specify the `segment` as `NSE_EQ` and the `instrument_type` as `EQ`, excluding other segments and instrument types from your search criteria.

###  Field Description
Field Name | Type | Description
---|---|---
segment | string | Segment to which the instrument is associated.
Possible values: `NSE_EQ`, `NSE_INDEX`, `NSE_FO`, `NCD_FO`, `BSE_EQ`, `BSE_INDEX`, `BSE_FO`, `BCD_FO`, `MCX_FO`, `NSE_COM`
name | string | The name of the equity.
exchange | string | Exchange to which the instrument is associated.
Possible values: `NSE`, `BSE`, `MCX`
isin | string | The International Securities Identification Number.
instrument_type | string | The instrument types for NSE are present at
instrument_key | string | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](https://upstox.com/developer/api-documentation/appendix/field-pattern).
lot_size | number | The size of one lot of the equity.
freeze_quantity | number | The maximum quantity that can be frozen.
exchange_token | string | The exchange-specific token for the equity.
tick_size | number | The minimum price movement of the equity.
trading_symbol | string | Trading symbol of the instrument.
short_name | string | A shorter or abbreviated name of the equity.
security_type | string | Identifies the classification or status of a security within the market. Valid security types can be found in the [Security Type Appendix](https://upstox.com/developer/api-documentation/appendix/equity-security-type)
```
{
  "weekly": false,
  "segment": "NSE_FO",
  "name": "071NSETEST",
  "exchange": "NSE",
  "expiry": 2111423399000,
  "instrument_type": "FUT",
  "underlying_symbol": "071NSETEST",
  "instrument_key": "NSE_FO|36702",
  "lot_size": 50,
  "freeze_quantity": 100000.0,
  "exchange_token": "36702",
  "minimum_lot": 50,
  "underlying_key": "NSE_EQ|DUMMYSAN011",
  "tick_size": 5.0,
  "underlying_type": "EQUITY",
  "trading_symbol": "071NSETEST FUT 27 NOV 36",
  "strike_price": 0.0
}

```

  * When you're searching for instrument keys within an instrument JSON file, you can employ the `segment` and `instrument_type` parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Future, specify the `segment` as `NSE_FO` and the `instrument_type` as `FUT`, excluding other segments and instrument types from your search criteria.

###  Field Description
Field Name | Type | Description
---|---|---
weekly | boolean | Indicates if the future is weekly.
segment | string | Segment to which the instrument is associated. Possible values: `NSE_EQ`, `NSE_INDEX`, `NSE_FO`, `NCD_FO`, `BSE_EQ`, `BSE_INDEX`, `BSE_FO`, `BCD_FO`, `MCX_FO`, `NSE_COM`
name | string | The name of the future.
exchange | string | Exchange to which the instrument is associated. Possible values: `NSE`, `BSE`, `MCX`
expiry | date | The expiry date of the future.
instrument_type | string | The type of the future instrument. Possible values: `FUT`
underlying_symbol | string | The symbol of the underlying asset.
instrument_key | string | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](https://upstox.com/developer/api-documentation/appendix/field-pattern).
lot_size | number | The size of one lot of the future.
freeze_quantity | number | The maximum quantity that can be frozen.
exchange_token | string | The exchange-specific token for the future.
minimum_lot | number | The minimum lot size for the future.
underlying_key | string | The `instrument_key` for the underlying asset.
tick_size | number | The minimum price movement of the future.
underlying_type | string | The type of the underlying asset. Possible values: `COM`, `INDEX`, `EQUITY`, `CUR`, `IRD`
trading_symbol | string | The symbol used for trading the future. Format: `<underlying_symbol> FUT <expiry in dd MMM yy>`
```
{
  "weekly": false,
  "segment": "NSE_FO",
  "name": "VODAFONE IDEA LIMITED",
  "exchange": "NSE",
  "expiry": 1706207399000,
  "instrument_type": "CE",
  "underlying_symbol": "IDEA",
  "instrument_key": "NSE_FO|36708",
  "lot_size": 80000,
  "freeze_quantity": 1600000.0,
  "exchange_token": "36708",
  "minimum_lot": 80000,
  "underlying_key": "NSE_EQ|INE669E01016",
  "tick_size": 5.0,
  "underlying_type": "EQUITY",
  "trading_symbol": "IDEA 22 CE 25 JAN 24",
  "strike_price": 22.0
}

```

  * When you're searching for instrument keys within an instrument JSON file, you can employ the `segment` and `instrument_type` parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Call Option, specify the `segment` as `NSE_FO` and the `instrument_type` as `CE`, excluding other segments and instrument types from your search criteria. If you want to search for Put Option then set `instrument_type` as `PE`.

###  Field Description
Field Name | Type | Description
---|---|---
weekly | boolean | Indicates if the option is weekly.
segment | string | The market segment of the option. Possible values: `NSE_EQ`, `NSE_INDEX`, `NSE_FO`, `NCD_FO`, `BSE_EQ`, `BSE_INDEX`, `BSE_FO`, `BCD_FO`, `MCX_FO`, `NSE_COM`
name | string | The name of the option.
exchange | string | Exchange to which the instrument is associated. Possible values: `NSE`, `BSE`, `MCX`
expiry | date | The expiry date of the option.
instrument_type | string | The type of the option instrument. Possible values: `CE`, `PE`
underlying_symbol | string | The symbol of the underlying asset.
instrument_key | string | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](https://upstox.com/developer/api-documentation/appendix/field-pattern).
strike_price | number | The strike price for the option.
lot_size | number | The size of one lot of the option.
freeze_quantity | number | The maximum quantity that can be frozen.
exchange_token | string | The exchange-specific token for the option.
minimum_lot | number | The minimum lot size for the option.
underlying_key | string | The `instrument_key` for the underlying asset.
tick_size | number | The minimum price movement of the option.
underlying_type | string | The type of the underlying asset. Possible values: `COM`, `INDEX`, `EQUITY`, `CUR`, `IRD`
trading_symbol | string | The symbol used for trading the option. Format: `<underlying_symbol> <strike_price> <CE/PE> <expiry in dd MMM yy>`
```
{
  "segment": "BSE_INDEX",
  "name": "AUTO",
  "exchange": "BSE",
  "instrument_type": "INDEX",
  "instrument_key": "BSE_INDEX|AUTO",
  "exchange_token": "13",
  "trading_symbol": "AUTO"
}

```

  * When you're searching for instrument keys within an instrument JSON file, you can employ the `segment` and `instrument_type` parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for NSE Index, specify the `segment` as `NSE_INDEX` and the `instrument_type` as `INDEX`, excluding other segments and instrument types from your search criteria.

### Field Description[​](https://upstox.com/developer/api-documentation/instruments/#field-description "Direct link to heading")
Field Name | Type | Description
---|---|---
segment | string | Segment to which the instrument is associated.
Possible values: `NSE_EQ`, `NSE_INDEX`, `NSE_FO`, `NCD_FO`, `BSE_EQ`, `BSE_INDEX`, `BSE_FO`, `BCD_FO`, `MCX_FO`, `NSE_COM`
name | string | The name of the index.
exchange | string | Exchange to which the instrument is associated.
Possible values: `NSE`, `BSE`, `MCX`
instrument_type | string | The type of the option instrument.
Possible values: `INDEX`
instrument_key | string | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](https://upstox.com/developer/api-documentation/appendix/field-pattern).
exchange_token | number | The numerical identifier issued by the exchange representing the instrument.
trading_symbol | string | Trading symbol for the index.
```
{
  "segment": "NSE_EQ",
  "name": "JOCIL LIMITED",
  "exchange": "NSE",
  "isin": "INE839G01010",
  "instrument_type": "BE",
  "instrument_key": "NSE_EQ|INE839G01010",
  "lot_size": 1,
  "freeze_quantity": 100000.0,
  "exchange_token": "16931",
  "tick_size": 1.0,
  "trading_symbol": "JOCIL",
  "qty_multiplier": 1.0
}

```

  * When you're searching for instrument keys within an instrument JSON file, you can employ the `segment` and `instrument_type` parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for a suspended instrument, check the instrument type and segment to identify it in the suspended instruments list.

###  Field Description
Field Name | Type | Description
---|---|---
segment | string | Segment to which the instrument is associated.
Possible values: `NSE_EQ`, `NSE_INDEX`, `NSE_FO`, `NCD_FO`, `BSE_EQ`, `BSE_INDEX`, `BSE_FO`, `BCD_FO`, `MCX_FO`, `NSE_COM`
name | string | The name of the suspended instrument.
exchange | string | Exchange to which the instrument is associated.
Possible values: `NSE`, `BSE`, `MCX`
isin | string | The International Securities Identification Number.
instrument_type | string | The instrument types for NSE are present at
instrument_key | string | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](https://upstox.com/developer/api-documentation/appendix/field-pattern).
lot_size | number | The size of one lot of the instrument.
freeze_quantity | number | The maximum quantity that can be frozen.
exchange_token | string | The exchange-specific token for the instrument.
tick_size | number | The minimum price movement of the instrument.
trading_symbol | string | Trading symbol of the instrument.
qty_multiplier | number | Quantity multiplier for the instrument.
```
{
  "segment": "NSE_EQ",
  "name": "RELIANCE INDUSTRIES LTD",
  "exchange": "NSE",
  "isin": "INE002A01018",
  "instrument_type": "EQ",
  "instrument_key": "NSE_EQ|INE002A01018",
  "lot_size": 1,
  "freeze_quantity": 100000.0,
  "exchange_token": "2885",
  "tick_size": 5.0,
  "trading_symbol": "RELIANCE",
  "short_name": "Reliance Industries",
  "mtf_enabled": true,
  "mtf_bracket": 26.5,
  "security_type": "NORMAL"
}

```

  * When you're searching for instrument keys within an instrument JSON file, you can employ the `segment` and `instrument_type` parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Equity, specify the `segment` as `NSE_EQ` and the `instrument_type` as `EQ`, excluding other segments and instrument types from your search criteria.

###  Field Description
Field Name | Type | Description
---|---|---
segment | string | Segment to which the instrument is associated.
Possible values: `NSE_EQ`
name | string | The name of the equity.
exchange | string | Exchange to which the instrument is associated.
Possible values: `NSE`
isin | string | The International Securities Identification Number.
instrument_type | string | The instrument types for NSE are present at
instrument_key | string | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](https://upstox.com/developer/api-documentation/appendix/field-pattern).
lot_size | number | The size of one lot of the equity.
freeze_quantity | number | The maximum quantity that can be frozen.
exchange_token | string | The exchange-specific token for the equity.
tick_size | number | The minimum price movement of the equity.
trading_symbol | string | Trading symbol of the instrument.
short_name | string | A shorter or abbreviated name of the equity.
mtf_enabled | boolean | Indicates whether the MTF is enabled for this particular instrument.
mtf_bracket | string | Represents the margin multiplier or leverage factor available for this security under MTF.
security_type | string | Identifies the classification or status of a security within the market. Valid security types can be found in the [Security Type Appendix](https://upstox.com/developer/api-documentation/appendix/equity-security-type)
```
{
  "segment": "NSE_EQ",
  "name": "RELIANCE INDUSTRIES LTD",
  "exchange": "NSE",
  "isin": "INE002A01018",
  "instrument_type": "EQ",
  "instrument_key": "NSE_EQ|INE002A01018",
  "lot_size": 1,
  "freeze_quantity": 100000,
  "exchange_token": "2885",
  "tick_size": 10,
  "trading_symbol": "RELIANCE",
  "short_name": "Reliance Industries",
  "qty_multiplier": 1,
  "security_type": "NORMAL",
  "intraday_margin": 20,
  "intraday_leverage": 5
}

```

  * When you're searching for instrument keys within an instrument JSON file, you can employ the `segment` and `instrument_type` parameters to refine and narrow down the list of instrument keys. For instance, if you're looking for the instrument key for Reliance Equity, specify the `segment` as `NSE_EQ` and the `instrument_type` as `EQ`, excluding other segments and instrument types from your search criteria.

###  Field Description
Field Name | Type | Description
---|---|---
segment | string | Segment to which the instrument is associated.
Possible values: `NSE_EQ`
name | string | The name of the equity.
exchange | string | Exchange to which the instrument is associated.
Possible values: `NSE`
isin | string | The International Securities Identification Number.
instrument_type | string | The instrument types for NSE are present at
instrument_key | string | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](https://upstox.com/developer/api-documentation/appendix/field-pattern).
lot_size | number | The size of one lot of the equity.
freeze_quantity | number | The maximum quantity that can be frozen.
exchange_token | string | The exchange-specific token for the equity.
tick_size | number | The minimum price movement of the equity.
trading_symbol | string | Trading symbol of the instrument.
short_name | string | A shorter or abbreviated name of the equity.
security_type | string | Identifies the classification or status of a security within the market. Valid security types can be found in the [Security Type Appendix](https://upstox.com/developer/api-documentation/appendix/equity-security-type)
intraday_margin | number | Percentage of LTP at which you can buy the stock for intraday trades.
intraday_leverage | number | Factor by which your trading capacity is increased for intraday trades.


  * The files undergo daily refresh at around 6 AM, and they are only refreshed as needed during the day, which is a seldom occurrence.
  * The BOD instrument for the next trading day will not include delisted stocks or expired contracts.



  * **The CSV format for instruments files is being deprecated.** Switch to the JSON format for improved performance. Details at [CSV Instruments File Deprecation Notice](https://upstox.com/developer/api-documentation/announcements/instruments-csv-deprecation-notice).

## CSV Files Deprecated[​](https://upstox.com/developer/api-documentation/instruments/#csv-files-deprecated "Direct link to heading")
These URLs provide access to the complete list of BOD contracts available for trading on Upstox in CSV format.
  * [Complete](https://assets.upstox.com/market-quote/instruments/exchange/complete.csv.gz)
  * [NSE](https://assets.upstox.com/market-quote/instruments/exchange/NSE.csv.gz)
  * [BSE](https://assets.upstox.com/market-quote/instruments/exchange/BSE.csv.gz)
  * [MCX](https://assets.upstox.com/market-quote/instruments/exchange/MCX.csv.gz)



### Sample CSV Record[​](https://upstox.com/developer/api-documentation/instruments/#sample-csv-record "Direct link to heading")
instrument_key | exchange_token | tradingsymbol | name | last_price | expiry | strike | tick_size | lot_size | instrument_type | option_type | exchange
---|---|---|---|---|---|---|---|---|---|---|---
NSE_FO|164693 | 164693 | RELIANCE24JAN1840CE | RELIANCE INDUSTRIES LTD | 424.8 | 2024-01-25 | 1840.0 | 0.05 | 250 | OPTSTK | CE | NSE_FO
### Field Description[​](https://upstox.com/developer/api-documentation/instruments/#field-description-1 "Direct link to heading")
Name | Type | Description
---|---|---
instrument_key | string | The unique identifier used across Upstox APIs for instrument identification. For the regex pattern applicable to this field, see the [Field Pattern Appendix](https://upstox.com/developer/api-documentation/appendix/field-pattern).
exchange_token | number | The numerical identifier issued by the exchange representing the instrument.
tradingsymbol | string | Shows the trading symbol which could be a combination of symbol name, instrument, expiry date etc. The format of this value may vary between weekly and monthly contracts, leading to inconsistencies. These inconsistencies have been resolved in the JSON version.
name | string | Name of the company (for equity instruments).
last_price | number | Last traded price.
expiry | string | Expiry date (for derivatives). Data format is `yyyy-MM-dd`
strike | number | Indicates the predetermined price at which an option can be bought or sold when it's exercised.
tick_size | number | Measure of the minimum upward or downward movement in the price of an instrument.
lot_size | number | Minimum size in which the stock futures or index futures can be traded.
instrument_type | string | Instrument type of a particular contract.
Possible values: `FUTSTK`, `OPTSTK`, `OPTIDX` etc.
option_type | string | Option type of the option contracts (applicable only for options contract).
Possible values: `CE`, `PE`
exchange | string | Exchange to which the order is associated.
Possible values: `NSE_EQ`, `NSE_FO`, `NCD_FO`, `NSE_INDEX`, `BSE_EQ`, `BSE_FO`, `BCD_FO`, `BSE_INDEX`, `MCX_FO`, `NSE_COM` etc.


[Previous MCP Integration](https://upstox.com/developer/api-documentation/mcp-integration)[Next Expired Instruments](https://upstox.com/developer/api-documentation/expired-instruments)
  * [JSON files](https://upstox.com/developer/api-documentation/instruments/#json-files)
  * [Suspended Instruments](https://upstox.com/developer/api-documentation/instruments/#suspended-instruments)
  * [MTF Instruments](https://upstox.com/developer/api-documentation/instruments/#mtf-instruments)
  * [MIS Instruments](https://upstox.com/developer/api-documentation/instruments/#mis-instruments)
    * [Sample JSON Object](https://upstox.com/developer/api-documentation/instruments/#sample-json-object)
    * [Field Description](https://upstox.com/developer/api-documentation/instruments/#field-description)
  * [CSV Files Deprecated](https://upstox.com/developer/api-documentation/instruments/#csv-files-deprecated)
    * [Sample CSV Record](https://upstox.com/developer/api-documentation/instruments/#sample-csv-record)
    * [Field Description](https://upstox.com/developer/api-documentation/instruments/#field-description-1)

[Contact us](https://upstox.com/contact-us/)·[About us](https://upstox.com/about/)·[FAQ](https://help.upstox.com/support/solutions/folders/278252)·[API Community](https://community.upstox.com/c/developer-api/15)
Made with ❤️ in India | Copyright © 2026, Upstox. Built with

