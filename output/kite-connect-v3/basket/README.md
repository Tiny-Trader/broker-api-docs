---
source: https://kite.trade/docs/connect/v3/basket/
scraped: true
---
Publisher - Offsite orders
 Kite Connect 3 / API documentation

# Offsite order execution[¶](https://kite.trade/docs/connect/v3/basket/#offsite-order-execution "Permanent link")
The offsite order execution feature allows you to redirect your users to Kite's exchange approved order page where they place orders and come back to your application seamlessly, like a payment gateway. This way, you do not have to build, maintain, and get exchange approvals for order execution screens. The [Kite Publisher](https://kite.trade/publisher) program utilizes offsite order execution to provide embeddable Javascript+HTML trade buttons that do not require any API integrations.
### Initiating orders[¶](https://kite.trade/docs/connect/v3/basket/#initiating-orders "Permanent link")
> Example JSON basket
```
[
  {
    "variety": "regular",
    "tradingsymbol": "INFY",
    "exchange": "NSE",
    "transaction_type": "BUY",
    "order_type": "MARKET",
    "quantity": 10,
    "readonly": false
  },
  {
    "variety": "regular",
    "tradingsymbol": "NIFTY15DECFUT",
    "exchange": "NFO",
    "transaction_type": "SELL",
    "order_type": "LIMIT",
    "price": 7845,
    "quantity": 1,
    "readonly": false
  },
  {
    "variety": "co",
    "tradingsymbol": "RELIANCE",
    "exchange": "NSE",
    "transaction_type": "BUY",
    "order_type": "LIMIT",
    "product": "MIS",
    "price": 915.15,
    "quantity": 1,
    "trigger_price": 910,
    "readonly": true
  }
]

```

> Posting the JSON basket
```
<form
  method="post"
  id="basket-form"
  action="https://kite.zerodha.com/connect/basket"
>
  <input type="hidden" name="api_key" value="xxx" />
  <input type="hidden" id="basket" name="data" value="" />
</form>

<script>
  document.getElementById("basket").value = your_basket;
  document.getElementById("basket-form").submit();
</script>

```

It is possible to send multiple orders which the user then confirms on a shopping basket like interface. You should prepare a JSON list of instruments to be traded with the required order parameters and `POST` it as a form field with the name `data` along with your `api_key` to **`https://kite.zerodha.com/connect/basket`**.
This is a browser / mobile (webview) request and has to happen at the user's end, although the basket preparation can happen in the backend. The easiest way to make the request is to create a hidden form, insert the JSON payload into it and submit it automatically using Javascript.
If you're preparing the basket client side on your web application, you can use the Kite Publisher [javascript plugin](https://kite.trade/docs/connect/v3/publisher/#generating-dynamic-buttons-with-javascript) to make things easier.
Note
You do not have to initiate a login using the login API to do offsite order execution. If a user is not already logged in, they'll be asked to login, otherwise, they'll be taken to the order basket directly. Either way, in the end, you will receive `status` and `request_token` at your `redirect_url` like in the login flow.
### Linking offsite execution to Kite Connect[¶](https://kite.trade/docs/connect/v3/basket/#linking-offsite-execution-to-kite-connect "Permanent link")
Offsite order execution follows the same flow as [login](https://kite.trade/docs/connect/v3/user/#login-flow), except for the order basket that appears after the login. Once the user is done placing orders, the basket will redirect back to your registered `redirect_login` along with a `request_key`, exactly like login. You are free to use this key to create a new Kite Connect session for further API interactions, or disregard it altogether.
### Request parameters[¶](https://kite.trade/docs/connect/v3/basket/#request-parameters "Permanent link")
parameter |
---|---
`variety` | Order variety (`regular`, `amo`, `co`. Defaults to `regular`)
`tradingsymbol` | Tradingsymbol of the instrument
`exchange` | Name of the exchange
`transaction_type` | BUY or SELL
`order_type` | Order type (MARKET, LIMIT etc.)
`quantity` | Quantity to transact
`product` | Margin product to use for the order (margins are blocked based on this)
`price` | For LIMIT orders
`trigger_price` | For SL, SL-M etc.
`disclosed_quantity` | Quantity to disclose publicly (for equity trades)
`validity` | Order validity
`readonly` | Default is `false`. If set to true, the UI does not allow the user to edit values such as quantity, price etc., and they can only review and execute.
`tag` | An optional tag to apply to an order to identify it (alphanumeric, max 20 chars)
Copyright © 2015 - 2025, Zerodha Technology Pvt. Ltd.
Made with

