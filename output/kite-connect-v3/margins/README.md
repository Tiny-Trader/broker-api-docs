---
source: https://kite.trade/docs/connect/v3/margins/
scraped: true
---
Margin calculation
 Kite Connect 3 / API documentation

# Margin calculation[¶](https://kite.trade/docs/connect/v3/margins/#margin-calculation "Permanent link")
Margin calculation APIs lets you calculate `span`, `exposure`, `option premium`, `additional`, `bo`, `cash`, `var`, `pnl` values for a list of orders.
type | endpoint |
---|---|---
POST | [/margins/orders](https://kite.trade/docs/connect/v3/margins/#order-margins) | Calculates margins for each order considering the existing positions and open orders
POST | [/margins/basket](https://kite.trade/docs/connect/v3/margins/#basket-margins) | Calculates margins for spread orders
POST | [/charges/orders](https://kite.trade/docs/connect/v3/margins/#virtual-contract-note) | Calculates order-wise charges for orderbook
Note
Requests to the above endpoints are JSON POST and it needs `application/json` header.
## Order margins[¶](https://kite.trade/docs/connect/v3/margins/#order-margins "Permanent link")
[Request order structure](https://kite.trade/docs/connect/v3/margins/#order-structure)
[Response margin structure](https://kite.trade/docs/connect/v3/margins/#margin-structure)
```
curl https://api.kite.trade/margins/orders \
    -H 'X-Kite-Version: 3' \
    -H 'Authorization: token api_key:access_token' \
    -H 'Content-Type: application/json' \
    -d '[
    {
        "exchange": "NSE",
        "tradingsymbol": "INFY",
        "transaction_type": "BUY",
        "variety": "regular",
        "product": "CNC",
        "order_type": "MARKET",
        "quantity": 1,
        "price": 0,
        "trigger_price": 0
    }
]'

```

Query parameters are as follows.
parameter |
---|---
mode |  `compact` - Compact mode will only give the total margins
```
{
  "status": "success",
  "data": [
    {
      "type": "equity",
      "tradingsymbol": "INFY",
      "exchange": "NSE",
      "span": 0,
      "exposure": 0,
      "option_premium": 0,
      "additional": 0,
      "bo": 0,
      "cash": 0,
      "var": 1498,
      "pnl": {
        "realised": 0,
        "unrealised": 0
      },
      "leverage": 1,
      "charges": {
        "transaction_tax": 1.498,
        "transaction_tax_type": "stt",
        "exchange_turnover_charge": 0.051681,
        "sebi_turnover_charge": 0.001498,
        "brokerage": 0.01,
        "stamp_duty": 0.22,
        "gst": {
          "igst": 0.011372219999999999,
          "cgst": 0,
          "sgst": 0,
          "total": 0.011372219999999999
        },
        "total": 1.79255122
      },
      "total": 1498
    }
  ]
}

```

### Order structure[¶](https://kite.trade/docs/connect/v3/margins/#order-structure "Permanent link")
parameter |
---|---
exchange | Name of the exchange
transaction_type |  `BUY`/`SELL`
variety | Order variety (regular, amo, co etc.)
product | Margin product to use for the order (margins are blocked based on this)
order_type | Order type (MARKET, LIMIT etc.)
quantity | Quantity of the order
price | Price at which the order is going to be placed (LIMIT orders)
trigger_price | Trigger price (for SL, SL-M, CO orders)
### Margin structure[¶](https://kite.trade/docs/connect/v3/margins/#margin-structure "Permanent link")
parameter |
---|---
type |  `equity`/`commodity`
tradingsymbol | Trading symbol of the instrument
exchange | Name of the exchange
span | SPAN margins
exposure | Exposure margins
option_premium | Option premium
additional | Additional margins
bo | BO margins
cash | Cash credit
var | VAR
pnl | Realised and unrealised profit and loss
leverage | Margin leverage allowed for the trade
charges | The [breakdown of the various charges](https://kite.trade/docs/connect/v3/margins/#charges-structure) that will be applied to an order
total | Total margin block
#### Charges structure[¶](https://kite.trade/docs/connect/v3/margins/#charges-structure "Permanent link")
Field | Definition
---|---
total | Total charges
transaction_tax | Tax levied for each transaction on the exchanges
transaction_tax_type | Type of transaction tax
exchange_turnover_charge | Charge levied by the exchange on the total turnover of the day
sebi_turnover_charge | Charge levied by SEBI on the total turnover of the day
brokerage | The brokerage charge for a particular trade
stamp_duty | Duty levied on the transaction value by Government of India
gst.igst | Integrated Goods and Services Tax levied by the government
gst.cgst | Central Goods and Services Tax levied by the government
gst.sgst | State Goods and Services Tax levied by the government
gst.total | Total GST
## Basket margins[¶](https://kite.trade/docs/connect/v3/margins/#basket-margins "Permanent link")
```
curl https://api.kite.trade/margins/basket?consider_positions=true \
    -H 'X-Kite-Version: 3' \
    -H 'Authorization: token api_key:access_token' \
    -H 'Content-Type: application/json' \
    -d '[
    {
        "exchange": "NFO",
        "tradingsymbol": "NIFTY23JUL20600CE",
        "transaction_type": "SELL",
        "variety": "regular",
        "product": "NRML",
        "order_type": "MARKET",
        "quantity": 75,
        "price": 0,
        "trigger_price": 0
    },
    {
        "exchange": "NFO",
        "tradingsymbol": "NIFTY23JUL20700CE",
        "transaction_type": "BUY",
        "variety": "regular",
        "product": "NRML",
        "order_type": "MARKET",
        "quantity": 75,
        "price": 0,
        "trigger_price": 0
    }
]'

```

Query parameters are as follows.
parameter |
---|---
consider_positions | Boolean to consider users positions
mode |  `compact` - Compact mode will only give the total margins
```
{
  "status": "success",
  "data": {
    "initial": {
      "type": "",
      "tradingsymbol": "",
      "exchange": "",
      "span": 66832.5,
      "exposure": 29151.225000000002,
      "option_premium": 521.25,
      "additional": 0,
      "bo": 0,
      "cash": 0,
      "var": 0,
      "pnl": {
        "realised": 0,
        "unrealised": 0
      },
      "leverage": 0,
      "charges": {
        "transaction_tax": 0,
        "transaction_tax_type": "",
        "exchange_turnover_charge": 0,
        "sebi_turnover_charge": 0,
        "brokerage": 0,
        "stamp_duty": 0,
        "gst": {
          "igst": 0,
          "cgst": 0,
          "sgst": 0,
          "total": 0
        },
        "total": 0
      },
      "total": 96504.975
    },
    "final": {
      "type": "",
      "tradingsymbol": "",
      "exchange": "",
      "span": 7788.000000000007,
      "exposure": 29151.225000000002,
      "option_premium": -2152.5,
      "additional": 0,
      "bo": 0,
      "cash": 0,
      "var": 0,
      "pnl": {
        "realised": 0,
        "unrealised": 0
      },
      "leverage": 0,
      "charges": {
        "transaction_tax": 0,
        "transaction_tax_type": "",
        "exchange_turnover_charge": 0,
        "sebi_turnover_charge": 0,
        "brokerage": 0,
        "stamp_duty": 0,
        "gst": {
          "igst": 0,
          "cgst": 0,
          "sgst": 0,
          "total": 0
        },
        "total": 0
      },
      "total": 34786.725000000006
    },
    "orders": [
      {
        "type": "equity",
        "tradingsymbol": "NIFTY23JUL20600CE",
        "exchange": "NFO",
        "span": 66832.5,
        "exposure": 29151.225000000002,
        "option_premium": 0,
        "additional": 0,
        "bo": 0,
        "cash": 0,
        "var": 0,
        "pnl": {
          "realised": 0,
          "unrealised": 0
        },
        "leverage": 1,
        "charges": {
          "transaction_tax": 1.67109375,
          "transaction_tax_type": "stt",
          "exchange_turnover_charge": 1.336875,
          "sebi_turnover_charge": 0.00267375,
          "brokerage": 20,
          "stamp_duty": 0,
          "gst": {
            "igst": 3.8411187749999995,
            "cgst": 0,
            "sgst": 0,
            "total": 3.8411187749999995
          },
          "total": 26.851761274999998
        },
        "total": 95983.725
      },
      {
        "type": "equity",
        "tradingsymbol": "NIFTY23JUL20700CE",
        "exchange": "NFO",
        "span": 0,
        "exposure": 0,
        "option_premium": 521.25,
        "additional": 0,
        "bo": 0,
        "cash": 0,
        "var": 0,
        "pnl": {
          "realised": 0,
          "unrealised": 0
        },
        "leverage": 1,
        "charges": {
          "transaction_tax": 0,
          "transaction_tax_type": "stt",
          "exchange_turnover_charge": 0.260625,
          "sebi_turnover_charge": 0.00052125,
          "brokerage": 20,
          "stamp_duty": 0,
          "gst": {
            "igst": 3.6470063249999995,
            "cgst": 0,
            "sgst": 0,
            "total": 3.6470063249999995
          },
          "total": 23.908152575
        },
        "total": 521.25
      }
    ],
    "charges": {
      "transaction_tax": 0,
      "transaction_tax_type": "",
      "exchange_turnover_charge": 0,
      "sebi_turnover_charge": 0.003195,
      "brokerage": 40,
      "stamp_duty": 0,
      "gst": {
        "igst": 0,
        "cgst": 0,
        "sgst": 0,
        "total": 0
      },
      "total": 0
    }
  }
}

```

Response structure is as follows.
parameter |
---|---
initial | Total [margins](https://kite.trade/docs/connect/v3/margins/#margin-structure) required to execute the orders
final | Total [margins](https://kite.trade/docs/connect/v3/margins/#margin-structure) with the spread benefit
orders | Individual [margins](https://kite.trade/docs/connect/v3/margins/#margin-structure) per order
charges | Final [charges](https://kite.trade/docs/connect/v3/margins/#charges-structure) block
Note
The final charges block can be ignored as it may not include `transaction_tax` charges because baskets can contain both mcx and equity instruments, with different tax types (STT or CTT). Users can refer to the individual [order charges response](https://kite.trade/docs/connect/v3/margins/#charges-structure) in the orders block.
## Virtual contract note[¶](https://kite.trade/docs/connect/v3/margins/#virtual-contract-note "Permanent link")
A virtual contract provides detailed charges order-wise for brokerage, STT, stamp duty, exchange transaction charges, SEBI turnover charge, and GST.
```
curl https://api.kite.trade/charges/orders \
    -H 'X-Kite-Version: 3' \
    -H 'Authorization: token api_key:access_token' \
    -H 'Content-Type: application/json' \
    -d '[
  {
    "order_id": "111111111",
    "exchange": "NSE",
    "tradingsymbol": "SBIN",
    "transaction_type": "BUY",
    "variety": "regular",
    "product": "CNC",
    "order_type": "MARKET",
    "quantity": 1,
    "average_price": 560
  },
  {
    "order_id": "2222222222",
    "exchange": "MCX",
    "tradingsymbol": "GOLDPETAL23JULFUT",
    "transaction_type": "SELL",
    "variety": "regular",
    "product": "NRML",
    "order_type": "LIMIT",
    "quantity": 1,
    "average_price": 5862
  },
  {
    "order_id": "3333333333",
    "exchange": "NFO",
    "tradingsymbol": "NIFTY2371317900PE",
    "transaction_type": "BUY",
    "variety": "regular",
    "product": "NRML",
    "order_type": "LIMIT",
    "quantity": 100,
    "average_price": 1.5
  }
]'

```

### Order structure[¶](https://kite.trade/docs/connect/v3/margins/#order-structure_1 "Permanent link")
parameter |
---|---
`order_id`string | Unique order ID (It can be any random string to calculate charges for an imaginary order)
`exchange`string | Name of the exchange
`tradingsymbol`string | Exchange tradingsymbol of the instrument
`transaction_type`string |  `BUY`/`SELL`
`variety`string | Order variety (regular, amo, co etc.)
`product`string | Margin product to use for the order (margins are blocked based on this)
`order_type`string | Order type (MARKET, LIMIT etc.)
`quantity`int64 | Quantity of the order
`average_price`float64 | Average price at which the order was executed (Note: Should be non-zero).
```
{
  "status": "success",
  "data": [
    {
      "transaction_type": "BUY",
      "tradingsymbol": "SBIN",
      "exchange": "NSE",
      "variety": "regular",
      "product": "CNC",
      "order_type": "MARKET",
      "quantity": 1,
      "price": 560,
      "charges": {
        "transaction_tax": 0.56,
        "transaction_tax_type": "stt",
        "exchange_turnover_charge": 0.01876,
        "sebi_turnover_charge": 0.00056,
        "brokerage": 0,
        "stamp_duty": 0,
        "gst": {
          "igst": 0.0033767999999999997,
          "cgst": 0,
          "sgst": 0,
          "total": 0.0033767999999999997
        },
        "total": 0.5826968
      }
    },
    {
      "transaction_type": "SELL",
      "tradingsymbol": "GOLDPETAL23JULFUT",
      "exchange": "MCX",
      "variety": "regular",
      "product": "NRML",
      "order_type": "LIMIT",
      "quantity": 1,
      "price": 5862,
      "charges": {
        "transaction_tax": 0.5862,
        "transaction_tax_type": "ctt",
        "exchange_turnover_charge": 0.152412,
        "sebi_turnover_charge": 0.005862,
        "brokerage": 1.7586,
        "stamp_duty": 0,
        "gst": {
          "igst": 0.34503732,
          "cgst": 0,
          "sgst": 0,
          "total": 0.34503732
        },
        "total": 2.84811132
      }
    },
    {
      "transaction_type": "BUY",
      "tradingsymbol": "NIFTY2371317900PE",
      "exchange": "NFO",
      "variety": "regular",
      "product": "NRML",
      "order_type": "LIMIT",
      "quantity": 100,
      "price": 1.5,
      "charges": {
        "transaction_tax": 0,
        "transaction_tax_type": "stt",
        "exchange_turnover_charge": 0.07575,
        "sebi_turnover_charge": 0.00015,
        "brokerage": 20,
        "stamp_duty": 0,
        "gst": {
          "igst": 3.613527,
          "cgst": 0,
          "sgst": 0,
          "total": 3.613527
        },
        "total": 23.689427000000002
      }
    }
  ]
}

```

### Response attributes[¶](https://kite.trade/docs/connect/v3/margins/#response-attributes "Permanent link")
attribute |
---|---
`transaction_type`string | Type of transaction being processed(BUY/SELL).
`tradingsymbol`string | Exchange tradingsymbol of the instrument
`exchange`string | Name of the exchange
`variety`string | Order variety (regular, amo, co etc.)
`product`string | Margin product to use for the order (margins are blocked based on this)
`order_type`string | Order type (MARKET, LIMIT etc.)
`quantity`int64 | Quantity of the order
`price`float64 | Price at which the order is completed
`charges`map | The [breakdown of the various charges](https://kite.trade/docs/connect/v3/margins/#charges-structure) that will be applied to an order
Copyright © 2015 - 2025, Zerodha Technology Pvt. Ltd.
Made with

