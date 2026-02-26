---
source: https://groww.in/trade-api/docs/curl/historical-data
scraped: true
---
[](https://groww.in/)[![Groww Logo](https://groww.in/favicon32x32-groww.ico)Groww API](https://groww.in/trade-api)
[](https://groww.in/)[![Groww Logo](https://groww.in/favicon32x32-groww.ico)Groww API](https://groww.in/trade-api)
cURL Docs
Documentation for cURL
`⌘``K`
[Documentation](https://groww.in/trade-api/docs)
[Introduction](https://groww.in/trade-api/docs/curl)[Instruments](https://groww.in/trade-api/docs/curl/instruments)[Orders](https://groww.in/trade-api/docs/curl/orders)[Smart Orders](https://groww.in/trade-api/docs/curl/smart-orders)[Portfolio](https://groww.in/trade-api/docs/curl/portfolio)[Margin](https://groww.in/trade-api/docs/curl/margin)[Live Data](https://groww.in/trade-api/docs/curl/live-data)[Historical Data](https://groww.in/trade-api/docs/curl/historical-data)[Backtesting](https://groww.in/trade-api/docs/curl/backtesting)[User](https://groww.in/trade-api/docs/curl/user)[Annexures](https://groww.in/trade-api/docs/curl/annexures)[Changelog](https://groww.in/trade-api/docs/curl/changelog)
Get Historical Data
# Historical Data
Fetch historical data of instruments easily using Groww APIs
## [Get Historical Data](https://groww.in/trade-api/docs/curl/historical-data#get-historical-data)
> **Note**
> This API request is deprecated and will NOT work in the future. Use [Get Historical Candle Data](https://groww.in/trade-api/docs/curl/backtesting#get-historical-candle-data) instead.
`GET https://api.groww.in/v1/historical/candle/range`
This API can be used to get the historical data of an instrument for a given time range. It provides the historical candles for a given interval.
### [Request](https://groww.in/trade-api/docs/curl/historical-data#request)
```
# You can also use wget
curl -X GET https://api.groww.in/v1/historical/candle/range?exchange=NSE&segment=CASH&trading_symbol=WIPRO&start_time=2021-01-01 09:15:00&end_time=2021-01-01 15:15:00 \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer {ACCESS_TOKEN}' \
  -H 'X-API-VERSION: 1.0'
```

#### [Request schema](https://groww.in/trade-api/docs/curl/historical-data#request-schema)
Name | Type | Description
---|---|---
exchange `*` | string |  [Stock exchange](https://groww.in/trade-api/docs/curl/annexures#exchange)

segment `*` | string |  [Segment](https://groww.in/trade-api/docs/curl/annexures#segment) of the instrument such as CASH, FNO etc.

trading_symbol `*` | string | Trading Symbol of the instrument as defined by the exchange

start_time `*` | string | Time in yyyy-MM-dd HH:mm:ss or epoch seconds format from which data is required

end_time `*` | string | Time in yyyy-MM-dd HH:mm:ss or epoch seconds format from which data is required

interval_in_minutes | string | Interval in minutes for which data is required

`*`required parameters
### [Response](https://groww.in/trade-api/docs/curl/historical-data#response)
All prices in rupees.
```
{
  "status": "SUCCESS",
  "payload": {
    "candles": [
      [
        1633072800, // candle timestamp in epoch second
        150.1,  // open price
        155.0,  // high price
        145.0,  // low price
        152.4,  // close price
        10000   // volume
      ]
    ],
    "start_time": 2025-01-01 15:30:00,
    "end_time": 2025-01-01 15:30:00,
    "interval_in_minutes": 5
  }
}
```

#### [Response Schema](https://groww.in/trade-api/docs/curl/historical-data#response-schema)
Name | Type | Description
---|---|---
candles | array[array] | This contains the list of candles. Each candle has candle timestamp (epoch second), open (float), high (float), low (float), close (float) , volume (int) in that order.

start_time | string | Start time in yyyy-MM-dd HH:mm:ss

end_time | string | End time in yyyy-MM-dd HH:mm:ss

interval_in_minutes | int | Interval in minutes

Candle Interval | Max Duration per Request | Historical Data Available
---|---|---
**1 min** | 7 days | Last 3 months
**5 min** | 15 days | Last 3 months
**10 min** | 30 days | Last 3 months
**1 hour (60 min)** | 150 days | Last 3 months
**4 hours (240 min)** | 365 days | Last 3 months
**1 day (1440 min)** | 1080 days (~3 years) | Full history
**1 week (10080 min)** | No Limit | Full history
[Previous Live Data](https://groww.in/trade-api/docs/curl/live-data)[Next Backtesting](https://groww.in/trade-api/docs/curl/backtesting)
[Get Historical Data](https://groww.in/trade-api/docs/curl/historical-data#get-historical-data)

