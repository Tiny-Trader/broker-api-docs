---
source: https://kite.trade/docs/connect/v3/mutual-funds/
scraped: true
---
Mutual funds
 Kite Connect 3 / API documentation

# Mutual funds[¶](https://kite.trade/docs/connect/v3/mutual-funds/#mutual-funds "Permanent link")
The mutual fund APIs allow managing SIPs of mutual funds listed on Zerodha's
type | endpoint |
---|---|---
GET | [/mf/orders](https://kite.trade/docs/connect/v3/mutual-funds/#retrieving-orders) | Retrieve the list of all orders (open and executed) over the last 7 days
GET | [/mf/orders/:order_id](https://kite.trade/docs/connect/v3/mutual-funds/#retrieving-an-individual-order) | Retrieve an individual order
GET | [/mf/sips/](https://kite.trade/docs/connect/v3/mutual-funds/#retrieving-all-sips) | Retrieve the list of all open SIP orders
GET | [/mf/holdings](https://kite.trade/docs/connect/v3/mutual-funds/#holdings) | Retrieve the list of mutual fund holdings available in the DEMAT
GET | [/mf/instruments](https://kite.trade/docs/connect/v3/mutual-funds/#retrieving-the-full-instrument-list) | Retrieve the master list of all mutual funds available on the platform
Note
Dividend reinvestment schemes are currently not supported.
## Retrieving orders[¶](https://kite.trade/docs/connect/v3/mutual-funds/#retrieving-orders "Permanent link")
This API returns all orders placed in the last 7 days.
```
curl "https://api.kite.trade/mf/orders" \
    -H "X-Kite-Version: 3" \
    -H "Authorization: token api_key:access_token"

```

```
{
  "status": "success",
  "data": [
    {
      "status": "REJECTED",
      "purchase_type": "FRESH",
      "folio": null,
      "order_timestamp": "2021-06-30 08:33:07",
      "average_price": 0.0,
      "exchange_order_id": "254657127",
      "last_price": 30.6800,
      "tradingsymbol": "INF179K01VY8",
      "settlement_id": "2122061",
      "transaction_type": "BUY",
      "order_id": "271989e0-a64e-4cf3-b4e4-afb8f38dd203",
      "amount": 1000.0,
      "tag": null,
      "placed_by": "ZV8062",
      "exchange_timestamp": "2021-06-30",
      "variety": "amc_sip",
      "last_price_date": "2021-06-29",
      "status_message": "AMC SIP: Insufficient balance.",
      "fund": "HDFC Balanced Advantage Fund - Direct Plan",
      "quantity": 0.0
    },
    {
      "status": "REJECTED",
      "purchase_type": "ADDITIONAL",
      "folio": null,
      "order_timestamp": "2021-06-30 01:30:02",
      "average_price": 0.0,
      "exchange_order_id": null,
      "last_price": 52.7980,
      "tradingsymbol": "INF174K01LS2",
      "settlement_id": null,
      "transaction_type": "BUY",
      "order_id": "ef7e696c-2fa6-400b-b180-eb25e6a04ccf",
      "amount": 2000.0,
      "tag": "coinandroidsip",
      "placed_by": "ZV8062",
      "exchange_timestamp": null,
      "variety": "sip",
      "last_price_date": "2021-06-29",
      "status_message": "SIP: Insufficient balance.",
      "fund": "Kotak Flexicap Fund - Direct Plan",
      "quantity": 0.0
    },
    {
      "status": "OPEN",
      "purchase_type": "FRESH",
      "folio": null,
      "order_timestamp": "2021-06-29 12:20:28",
      "average_price": 0.0,
      "exchange_order_id": null,
      "last_price": 10.4324,
      "tradingsymbol": "INF761K01EE1",
      "settlement_id": null,
      "transaction_type": "BUY",
      "order_id": "2b6ad4b7-c84e-4c76-b459-f3a8994184f1",
      "amount": 5000.0,
      "tag": null,
      "placed_by": "ZV8062",
      "exchange_timestamp": null,
      "variety": "regular",
      "last_price_date": "2021-06-29",
      "status_message": "Insufficient fund. 1/5",
      "fund": "BOI AXA Arbitrage Fund - Direct Plan",
      "quantity": 0.0
    },
    {
      "status": "REJECTED",
      "purchase_type": "FRESH",
      "folio": null,
      "order_timestamp": "2021-06-29 08:36:41",
      "average_price": 0.0,
      "exchange_order_id": "254447867",
      "last_price": 271.7500,
      "tradingsymbol": "INF179K01WA6",
      "settlement_id": "2122060",
      "transaction_type": "BUY",
      "order_id": "40410882-b1f8-4938-bb08-4bef2765cbfb",
      "amount": 1000.0,
      "tag": null,
      "placed_by": "ZV8062",
      "exchange_timestamp": "2021-06-29",
      "variety": "amc_sip",
      "last_price_date": "2021-06-29",
      "status_message": "AMC SIP: Insufficient balance.",
      "fund": "HDFC Balanced Advantage Fund - Direct Plan",
      "quantity": 0.0
    },
    {
      "status": "OPEN",
      "purchase_type": "FRESH",
      "folio": null,
      "order_timestamp": "2021-06-24 15:37:27",
      "average_price": 0.0,
      "exchange_order_id": null,
      "last_price": 11.5182,
      "tradingsymbol": "INF109K01V59",
      "settlement_id": null,
      "transaction_type": "BUY",
      "order_id": "e67b8741-5054-4fd5-a2da-8c672e1f494a",
      "amount": 5000.0,
      "tag": null,
      "placed_by": "ZV8062",
      "exchange_timestamp": null,
      "variety": "regular",
      "last_price_date": "2021-06-29",
      "status_message": "Insufficient fund. 3/5",
      "fund": "ICICI Prudential Bond Fund - Direct Plan",
      "quantity": 0.0
    }
  ]
}

```

### Response attributes[¶](https://kite.trade/docs/connect/v3/mutual-funds/#response-attributes "Permanent link")
attribute |
---|---
`order_id`string | Unique order id
`exchange_order_id`null, string | Exchange generated order id
`tradingsymbol`string | ISIN of the fund
`status`null, string | Current status of the order. Most common values or COMPLETE, REJECTED, CANCELLED, and OPEN. There may be other values as well
`status_message`null, string | Textual description of the order's status. Failed orders come with human readable explanation
`folio`null, string | Folio number generated by AMC for the completed purchase order
`fund`string | Name of the fund
`order_timestamp`string | Timestamp at which the order was registered by the API
`exchange_timestamp`string | Date on which the order was registered by the exchange. Orders that don't reach the exchange have null timestamps
`settlement_id`string | Exchange settlement ID
`transaction_type`string | BUY or SELL
`amount`float64 | Amount placed for purchase of units
`variety`string | Order variety (regular, sip)
`purchase_type`null, string | FRESH or ADDITIONAL (null incase of SELL order)
`quantity`float64 | Number of units allotted or sold
`price`float64 | Buy or sell price
`last_price`float64 | Last available NAV price of the fund
`average_price`float64 | Allotted or sold NAV price
`placed_by`string | Id of the user that placed the order
`last_price_date`string | Date for which last NAV is available
`tag`string | Tag that was sent with an order to identify it (alphanumeric, max 8 chars)
## Retrieving an individual order[¶](https://kite.trade/docs/connect/v3/mutual-funds/#retrieving-an-individual-order "Permanent link")
While the orders list API returns orders within the last 7 days, given an order ID, this API will return the order details irrespective of its age.
```
curl  "https://api.kite.trade/mf/orders/123123"
    -H "X-Kite-Version: 3" \
    -H "Authorization: token api_key:access_token" \

```

```
{
  "status": "success",
  "data": {
    "status": "OPEN",
    "purchase_type": "FRESH",
    "exchange_order_id": null,
    "last_price": 10.4324,
    "order_timestamp": "2021-06-29 12:20:28",
    "fund": "BOI AXA Arbitrage Fund - Direct Plan",
    "tradingsymbol": "INF761K01EE1",
    "tag": null,
    "placed_by": "ZV8062",
    "last_price_date": "2021-06-29",
    "folio": null,
    "variety": "regular",
    "exchange_timestamp": null,
    "average_price": 0.0,
    "settlement_id": null,
    "transaction_type": "BUY",
    "order_id": "2b6ad4b7-c84e-4c76-b459-f3a8994184f1",
    "amount": 5000.0,
    "status_message": "Insufficient fund. 1/5",
    "quantity": 0
  }
}

```

## Retrieving all SIPs[¶](https://kite.trade/docs/connect/v3/mutual-funds/#retrieving-all-sips "Permanent link")
This API returns the list of all active and paused SIPs
```
curl "https://api.kite.trade/mf/sips"
    -H "X-Kite-Version: 3" \
    -H "Authorization: token api_key:access_token" \

```

```
{
"data": [
  {
    "status": "ACTIVE",
    "sip_reg_num": null,
    "created": "2021-05-05 05:56:27",
    "dividend_type": "idcw",
    "instalment_amount": 500.0,
    "fund": "Aditya Birla Sun Life Liquid Fund - Direct Plan",
    "instalments": -1,
    "next_instalment": "2021-05-12",
    "transaction_type": "BUY",
    "trigger_price": 0,
    "step_up": {
      "05-05": 10
    },
    "tradingsymbol": "INF209K01VD7",
    "tag": "coiniossip",
    "frequency": "weekly",
    "last_instalment": "2021-05-05 05:56:27",
    "pending_instalments": -1,
    "instalment_day": 0,
    "sip_type": "sip",
    "completed_instalments": 0,
    "sip_id": "892741486820670"
  },
  {
    "status": "ACTIVE",
    "sip_reg_num": null,
    "created": "2021-05-25 10:55:09",
    "dividend_type": "idcw",
    "instalment_amount": 1000.0,
    "fund": "HDFC Balanced Advantage Fund - Direct Plan",
    "instalments": -1,
    "next_instalment": "2021-06-01",
    "transaction_type": "BUY",
    "trigger_price": 0,
    "step_up": {
      "25-05": 10
    },
    "tradingsymbol": "INF179K01VY8",
    "tag": "coiniossip",
    "frequency": "weekly",
    "last_instalment": "2021-05-25 10:55:09",
    "pending_instalments": -1,
    "instalment_day": 0,
    "sip_type": "sip",
    "completed_instalments": 0,
    "sip_id": "109195857904698"
  },
  {
    "status": "ACTIVE",
    "sip_reg_num": "15158182",
    "created": "2021-05-22 10:45:29",
    "dividend_type": "idcw",
    "instalment_amount": 1000.0,
    "fund": "HDFC Balanced Advantage Fund - Direct Plan",
    "instalments": 9999,
    "next_instalment": "2021-07-12",
    "transaction_type": "BUY",
    "trigger_price": 0,
    "step_up": {},
    "tradingsymbol": "INF179K01VY8",
    "tag": "coinandroidsip",
    "frequency": "monthly",
    "last_instalment": "2021-06-10 08:37:11",
    "pending_instalments": 9998,
    "instalment_day": 10,
    "sip_type": "amc_sip",
    "completed_instalments": 1,
    "sip_id": "846479755969168"
  },
  {
    "status": "ACTIVE",
    "sip_reg_num": "16055666",
    "created": "2021-06-18 03:56:46",
    "dividend_type": "idcw",
    "instalment_amount": 1000.0,
    "fund": "HDFC Balanced Advantage Fund - Direct Plan",
    "instalments": 9999,
    "next_instalment": "2021-07-30",
    "transaction_type": "BUY",
    "trigger_price": 0,
    "step_up": {},
    "tradingsymbol": "INF179K01VY8",
    "tag": "coinandroidsip",
    "frequency": "monthly",
    "last_instalment": "2021-06-30 08:33:07",
    "pending_instalments": 9998,
    "instalment_day": 30,
    "sip_type": "amc_sip",
    "completed_instalments": 1,
    "sip_id": "749073272501476"
  },
  {
    "status": "ACTIVE",
    "sip_reg_num": null,
    "created": "2020-11-20 01:06:11",
    "dividend_type": "growth",
    "instalment_amount": 7427.0,
    "fund": "HDFC Hybrid Equity Fund - Direct Plan",
    "instalments": -1,
    "next_instalment": "2021-02-19",
    "transaction_type": "BUY",
    "trigger_price": 0,
    "step_up": {
      "20-11": 30
    },
    "tradingsymbol": "INF179K01XZ1",
    "tag": "coinandroidsip",
    "frequency": "quarterly",
    "last_instalment": "2020-11-20 01:06:11",
    "pending_instalments": -1,
    "instalment_day": 0,
    "sip_type": "sip",
    "completed_instalments": 0,
    "sip_id": "576440634181776"
  }]
}

```

### Response attributes[¶](https://kite.trade/docs/connect/v3/mutual-funds/#response-attributes_1 "Permanent link")
attribute |
---|---
`sip_id`string | Unique SIP id
`tradingsymbol`string | ISIN of the fund.
`fund`string | Name of the fund
`dividend_type`string | Dividend type (growth, payout)
`transaction_type`string | BUY or SELL
`status`string | ACTIVE, PAUSED or CANCELLED
`created`string | Timestamp at which the SIP was registered by the API
`frequency`string | Frequency at which order is triggered (monthly, weekly, or quarterly)
`next_instalment`string | Upcoming instalment date
`instalment_amount`int64 | Amount worth of units to purchase in each instalment
`instalments`int64 | Number of instalments (-1 in case of SIPs active until cancelled)
`last_instalment`string | Timestamp at which the last instalment was triggered
`pending_instalments`int64 | Number of instalments pending (-1 in case of SIPs active until cancelled)
`instalment_day`int64 | Calendar day in a month on which SIP order to be triggered (valid only incase of frequency monthly, else 0)
`completed_instalments`int64 | Total number of completed instalments from the start
`tag`string | Tag that was sent with an order to identify it (alphanumeric, max 8 chars)
## Holdings[¶](https://kite.trade/docs/connect/v3/mutual-funds/#holdings "Permanent link")
Holdings contain the user's portfolio of allotted mutual fund units.
```
curl "https://api.kite.trade/mf/holdings" \
    -H "X-Kite-Version: 3" \
    -H "Authorization: token api_key:access_token" \

```

```
{
  "status": "success",
  "data": [
    {
      "folio": "3108290884",
      "average_price": 78.43,
      "last_price": 84.86,
      "last_price_date": "",
      "pledged_quantity": 0,
      "fund": "INVESCO INDIA TAX PLAN - DIRECT PLAN",
      "tradingsymbol": "INF205K01NT8",
      "pnl": 0,
      "quantity": 382.488
    },
    {
      "folio": "5102495241",
      "average_price": 1874.101138,
      "last_price": 2081.4984,
      "last_price_date": "",
      "pledged_quantity": 0,
      "fund": "Indiabulls Liquid Fund - Direct Plan",
      "tradingsymbol": "INF666M01451",
      "pnl": 0,
      "quantity": 1.334
    },
    {
      "folio": "9104386836",
      "average_price": 116.7,
      "last_price": 101.13,
      "last_price_date": "",
      "pledged_quantity": 0,
      "fund": "BOI AXA TAX ADVANTAGE FUND - DIRECT PLAN",
      "tradingsymbol": "INF761K01884",
      "pnl": 0,
      "quantity": 257.057
    }
  ]
}

```

### Response attributes[¶](https://kite.trade/docs/connect/v3/mutual-funds/#response-attributes_2 "Permanent link")
attribute |
---|---
`folio`null, string | Folio number generated by AMC for the completed purchase order (null incase of SELL order)
`fund`string | Name of the fund
`tradingsymbol`string | ISIN of the fund.
`average_price`float64 | Allotted NAV price for a completed BUY order; Selling NAV price for completed SELL order
`last_price`float64 | Last available NAV price of the fund
`pnl`float64 | Net returns of the holding. Based on the last available NAV price.
`last_price_date`string | Date for which last NAV is available
`quantity`float64 | Quantity available in the client's holding for this ISIN.
## Retrieving the full instrument list[¶](https://kite.trade/docs/connect/v3/mutual-funds/#retrieving-the-full-instrument-list "Permanent link")
Unlike the rest of the calls that return JSON, the instrument list API returns a Gzipped CSV dump of mutual funds supported by Zerodha's
```
curl "https://api.kite.trade/mf/instruments" \
    -H "X-Kite-Version: 3" \
    -H "Authorization: token api_key:access_token" \

```

```
tradingsymbol,amc,name,purchase_allowed,redemption_allowed,minimum_purchase_amount,purchase_amount_multiplier,minimum_additional_purchase_amount,minimum_redemption_quantity,redemption_quantity_multiplier,dividend_type,scheme_type,plan,settlement_type,last_price,last_price_date
INF846K01DP8,AXISMUTUALFUND_MF,Axis Equity Fund - Direct Plan - Growth,1,1,5000.0,1.0,100.0,1.0,0.001,growth,equity,direct,T3,20.09,2016-11-11
INF846K01EW2,AXISMUTUALFUND_MF,Axis Long Term Equity Fund - Direct Growth,1,1,500.0,500.0,500.0,1.0,0.001,growth,elss,direct,T3,33.0425,2016-11-11
INF174K01LS2,KOTAKMAHINDRAMF,Kotak Select Focus Fund- Direct Plan - Growth,1,1,5000.0,1.0,1000.0,0.001,0.001,growth,equity,direct,T3,26.549,2016-11-11
INF174K01336,KOTAKMAHINDRAMF,Kotak Select Focus Fund-Growth,1,1,5000.0,0.01,1000.0,0.001,0.001,growth,equity,regular,T3,25.635,2016-11-11

```

### Response columns[¶](https://kite.trade/docs/connect/v3/mutual-funds/#response-columns "Permanent link")
column |
---|---
`tradingsymbol`string | ISIN of the fund
`amc`string | AMC code as per the exchange
`name`string | Fund name
`purchase_allowed`string |  `0` or `1`
`redemption_allowed`string |  `0` or `1`
`minimum_purchase_amount`float64 | Minimum purchase amount for the first BUY
`purchase_amount_multiplier`float64 | Buy amount should be in multiple of this value
`minimum_additional_purchase_amount`float64 | Minimum additional BUY amount
`minimum_redemption_quantity`float64 | Minimum SELL quantity
`redemption_quantity_multiplier`float64 | SELL quantity multiple
`dividend_type`string |  `growth` or `payout`
`scheme_type`string |  `equity`, `debt`, `elss`
`plan`string |  `direct` or `regular`
`settlement_type`string | Settlement type of the fund (`T1`, `T2` etc.)
`last_price`float64 | Last available NAV price of the fund
`last_price_date`string | Last available NAV's date
Copyright © 2015 - 2025, Zerodha Technology Pvt. Ltd.
Made with

