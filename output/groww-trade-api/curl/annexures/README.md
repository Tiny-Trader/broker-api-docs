---
source: https://groww.in/trade-api/docs/curl/annexures
scraped: true
---
[](https://groww.in/)[![Groww Logo](https://groww.in/favicon32x32-groww.ico)Groww API](https://groww.in/trade-api)
[](https://groww.in/)[![Groww Logo](https://groww.in/favicon32x32-groww.ico)Groww API](https://groww.in/trade-api)
cURL Docs
Documentation for cURL
`⌘``K`
[Documentation](https://groww.in/trade-api/docs)
[Introduction](https://groww.in/trade-api/docs/curl)[Instruments](https://groww.in/trade-api/docs/curl/instruments)[Orders](https://groww.in/trade-api/docs/curl/orders)[Smart Orders](https://groww.in/trade-api/docs/curl/smart-orders)[Portfolio](https://groww.in/trade-api/docs/curl/portfolio)[Margin](https://groww.in/trade-api/docs/curl/margin)[Live Data](https://groww.in/trade-api/docs/curl/live-data)[Historical Data](https://groww.in/trade-api/docs/curl/historical-data)[Backtesting](https://groww.in/trade-api/docs/curl/backtesting)[User](https://groww.in/trade-api/docs/curl/user)[Annexures](https://groww.in/trade-api/docs/curl/annexures)[Changelog](https://groww.in/trade-api/docs/curl/changelog)
Order Status
# Annexures
The SDK uses several fixed parameters to represent various trading parameters.
## [Order Status](https://groww.in/trade-api/docs/curl/annexures#order-status)
Value | Description
---|---
NEW | Order is newly created and pending for further processing
ACKED | Order has been acknowledged by the system
TRIGGER_PENDING | Order is waiting for a trigger event to be executed
APPROVED | Order has been approved and is ready for execution
REJECTED | Order has been rejected by the system
FAILED | Order execution has failed
EXECUTED | Order has been successfully executed
DELIVERY_AWAITED | Order has been executed and waiting for delivery
CANCELLED | Order has been cancelled
CANCELLATION_REQUESTED | Request to cancel the order has been initiated
MODIFICATION_REQUESTED | Request to modify the order has been initiated
COMPLETED | Order has been completed
## [After Market Order Status](https://groww.in/trade-api/docs/curl/annexures#after-market-order-status)
Value | Description
---|---
NA | Status not available
PENDING | Order is pending for execution
DISPATCHED | Order has been dispatched for execution
PARKED | Order is parked for later execution
PLACED | Order has been placed in the market
FAILED | Order execution has failed
MARKET | Order is a market order
## [Exchange](https://groww.in/trade-api/docs/curl/annexures#exchange)
Value | Description
---|---
BSE | Bombay Stock Exchange - Asia's oldest exchange, known for SENSEX index
NSE | National Stock Exchange - India's largest exchange by trading volume
MCX | Multi Commodity Exchange - India's largest commodity derivatives exchange
## [Segment](https://groww.in/trade-api/docs/curl/annexures#segment)
Value | Description
---|---
CASH | Regular equity market for trading stocks with delivery option
FNO | Futures and Options segment for trading derivatives contracts
COMMODITY | Commodity derivatives segment for trading commodity futures and options on MCX
## [Order Type](https://groww.in/trade-api/docs/curl/annexures#order-type)
Value | Description
---|---
LIMIT | Specify exact price, may not get filled immediately but ensures price control
MARKET | Immediate execution at best available price, no price guarantee
SL | Stop Loss - Protection order that triggers at specified price to limit losses
SL_M | Stop Loss Market - Market order triggered at specified price to limit losses
## [Product](https://groww.in/trade-api/docs/curl/annexures#product)
Value | Description
---|---
CNC | Cash and Carry - For delivery-based equity trading with full upfront payment
MIS | Margin Intraday Square-off - Higher leverage but must close by day end
NRML | Regular margin trading allowing overnight positions with standard leverage
## [Transaction Type](https://groww.in/trade-api/docs/curl/annexures#transaction-type)
Value | Description
---|---
BUY | Long position - Profit from price increase, loss from price decrease
SELL | Short position - Profit from price decrease, loss from price increase
## [Validity](https://groww.in/trade-api/docs/curl/annexures#validity)
Value | Description
---|---
DAY | Valid until market close on the same trading day
## [Candle Interval](https://groww.in/trade-api/docs/curl/annexures#candle-interval)
Value | Description
---|---
1minute | 1 minute interval
2minute | 2 minute interval
3minute | 3 minute interval
5minute | 5 minute interval
10minute | 10 minute interval
15minute | 15 minute interval
30minute | 30 minute interval
1hour | 1 hour interval
4hour | 4 hour interval
1day | 1 day interval
1week | 1 week interval
1month | 1 month interval
## [Instrument Type](https://groww.in/trade-api/docs/curl/annexures#instrument-type)
Value | Description
---|---
EQ | Equity - Represents ownership in a company
IDX | Index - Composite value of a group of stocks representing a market
FUT | Futures - Derivatives contract to buy/sell an asset at a future date
CE | Call Option - Derivatives contract giving the right to buy an asset
PE | Put Option - Derivatives contract giving the right to sell an asset
[Previous User](https://groww.in/trade-api/docs/curl/user)[Next Changelog](https://groww.in/trade-api/docs/curl/changelog)
[Order Status](https://groww.in/trade-api/docs/curl/annexures#order-status)[After Market Order Status](https://groww.in/trade-api/docs/curl/annexures#after-market-order-status)[Exchange](https://groww.in/trade-api/docs/curl/annexures#exchange)[Segment](https://groww.in/trade-api/docs/curl/annexures#segment)[Order Type](https://groww.in/trade-api/docs/curl/annexures#order-type)[Product](https://groww.in/trade-api/docs/curl/annexures#product)[Transaction Type](https://groww.in/trade-api/docs/curl/annexures#transaction-type)[Validity](https://groww.in/trade-api/docs/curl/annexures#validity)[Candle Interval](https://groww.in/trade-api/docs/curl/annexures#candle-interval)[Instrument Type](https://groww.in/trade-api/docs/curl/annexures#instrument-type)

