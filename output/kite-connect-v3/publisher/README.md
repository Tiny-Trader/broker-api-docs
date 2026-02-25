---
source: https://kite.trade/docs/connect/v3/publisher/
scraped: true
---
Publisher JS plugin

 Kite Connect 3 / API documentation

# Publisher JS Plugin[¶](https://kite.trade/docs/connect/v3/publisher/#publisher-js-plugin "Permanent link")
Warning
The publisher JS plugin will not function in the iOS WebView due to Safari's new cookie policy, which blocks cross-domain cookie management in iframes. You will need to implement [offsite order execution](https://kite.trade/docs/connect/v3/basket/). We recommend using [offsite order execution](https://kite.trade/docs/connect/v3/basket/) for all [Kite Publisher](https://kite.trade/publisher/) use cases.
The [Kite Publisher](https://kite.trade/publisher) Javascript plugin lets you add one-click trade buttons to your webpage. It works like a basket combined with a payment gateway, where an inline popup opens on your webpage, guides the user through a trade, and lands the user back on your page. As described in the offsite order execution section, it is possible to capture the `request_token` from this flow to start a Kite Connect session as well.
You can add one or more stocks to the basket (maximum 10) dynamically using the Javascript plugin, or embed simple static buttons using plain HTML.
## Getting started[¶](https://kite.trade/docs/connect/v3/publisher/#getting-started "Permanent link")
```
<script src="https://kite.trade/publisher.js?v=3"></script>

```

Include Kite Publisher on your webpage by pasting the following script tag at the end of your webpage, just before the closing `</body>` tag. You only need to include this once to render any number of buttons on a page.
## Branded HTML5 buttons[¶](https://kite.trade/docs/connect/v3/publisher/#branded-html5-buttons "Permanent link")
```
<!--  A link that initiates a buy (market) of the SBIN stock //-->
<kite-button
  href="#"
  data-kite="your_api_key"
  data-exchange="NSE"
  data-tradingsymbol="SBIN"
  data-transaction_type="BUY"
  data-quantity="1"
  data-order_type="MARKET"
  >Buy SBI stock</kite-button
>

```

You can use the custom `<kite-button>` HTML5 tag to render branded Kite buttons that initiate a trade with a single click. The branded buttons work in a similar fashion to social media buttons, and you can include as many as you want on a page.
## Custom HTML5 buttons[¶](https://kite.trade/docs/connect/v3/publisher/#custom-html5-buttons "Permanent link")
```
<!--  A link that initiates a buy (market) of the SBIN stock //-->
<a
  href="#"
  data-kite="your_api_key"
  data-exchange="NSE"
  data-tradingsymbol="SBIN"
  data-transaction_type="BUY"
  data-quantity="1"
  data-order_type="MARKET"
  >Buy SBI stock</a
>

<!--  A button that initiates a sell (LIMIT) of the RELIANCE stock //-->
<button
  data-kite="your_api_key"
  data-exchange="NSE"
  data-tradingsymbol="RELIANCE"
  data-transaction_type="SELL"
  data-quantity="1"
  data-order_type="LIMIT"
  data-price="100"
>
  Buy RELIANCE
</button>

<!--  A button that initiates a CO of the RELIANCE stock //-->
<button
  data-kite="your_api_key"
  data-exchange="NSE"
  data-tradingsymbol="RELIANCE"
  data-transaction_type="BUY"
  data-quantity="1"
  data-order_type="LIMIT"
  data-variety="co"
  data-product="MIS"
  data-price="915"
  data-trigger_price="910"
>
  Buy RELIANCE (Cover Order)
</button>

```

You can use the HTML5 data attributes on any HTML element and turn it into a trade button which gets invoked with a single click. The examples on the right show a link and a button being turned into trade buttons.
## Generating dynamic buttons with Javascript[¶](https://kite.trade/docs/connect/v3/publisher/#generating-dynamic-buttons-with-javascript "Permanent link")
```
<!-- A Kite button will be generated inside this container //-->
<p id="default-button"></p>

<!-- The basket will be linked to this element's onClick //-->
<button id="custom-button">Buy the basket</button>

<!-- Include the plugin //-->
<script src="https://kite.trade/publisher.js?v=3"></script>

<script>
  // Only run your custom code once KiteConnect has fully initialised.
  // Use KiteConnect.ready() to achieve this.
  KiteConnect.ready(function () {
    // Initialize a new Kite instance.
    // You can initialize multiple instances if you need.
    var kite = new KiteConnect("your_api_key");

    // Add a stock to the basket
    kite.add({
      exchange: "NSE",
      tradingsymbol: "INFY",
      quantity: 5,
      transaction_type: "BUY",
      order_type: "MARKET",
    });

    // Add another stock
    kite.add({
      exchange: "NSE",
      tradingsymbol: "SBIN",
      quantity: 1,
      order_type: "LIMIT",
      transaction_type: "SELL",
      price: 105,
    });

    // Add a Cover Order
    kite.add({
      tradingsymbol: "RELIANCE",
      exchange: "NSE",
      transaction_type: "BUY",
      order_type: "LIMIT",
      product: "MIS",
      price: 915.15,
      quantity: 1,
      variety: "co",
      trigger_price: 910,
      readonly: true,
    });

    // Register an (optional) callback.
    kite.finished(function (status, request_token) {
      alert("Finished. Status is " + status);
    });

    // Render the in-built button inside a given target
    kite.renderButton("#default-button");

    // OR, link the basket to any existing element you want
    kite.link("#custom-button");
  });
</script>

```

You can create a basket of stocks and get the plugin to render a Kite button that executes it, or link the basket to your own button (or any HTML element).
The plugin loads it's assets asynchronously, so it's important that you initialise your custom KiteConnect calls after it has fully loaded. You need to use the `KiteConnect.ready()` function to achieve this.
Note
Include your custom code after the publisher.js inclusion. Also, make sure to wrap your code in `KiteConnect.ready()`
### Parameters[¶](https://kite.trade/docs/connect/v3/publisher/#parameters "Permanent link")
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
`tag` | An optional tag to apply to an order to identify it (alphanumeric, max 8 chars)
### Methods[¶](https://kite.trade/docs/connect/v3/publisher/#methods "Permanent link")
method | arguments |
---|---|---
`KiteConnect.ready()` | `function()` | Safe wrapper for all API calls that waits asynchronously for all assets to load.
`add()` | `entry` | Adds an object literal {} with the parameters mentioned in the previous section represeting a single trading entry to the basket.
`get()` |  | Returns an array[] of all added entries.
`count()` |  | Returns the number of added entries.
`setOption()` | `key, value` | Sets the value for certain supported keys.
| `redirect_url` | A redirect URL to override the registered Kite Connect redirect URL (using `setOption()`). The value can be a single '#', a 127.0.0.1 url for testing, or a fully qualified URL belonging to the same domain as the registered URL.
`renderButton()` | `element_selector` | Renders a branded Kite button in the given target element, which when clicked, will start the transaction in an overlay popup. `element_selector` is an HTML selector, for example, `#buy-button`, `.buttons` etc.
`link()` | `element_selector` | Links the basket to the given HTML element, which when clicked, will start the transaction in an overlay popup. `element_selector` is an HTML selector, for example, `#buy-button`, `.buttons` etc.
`html()` |  | Returns a serialized HTML form with the necessary hidden fields and the basket payload which can be written to the document body and submitted to initiate the transaction.
`finished()` | `function(status, request_token)` | Register a callback which is triggered after order placement is finished.
`authHoldings()` | `request_id, callback(data)` | Request ID from [the holdings authorisation call](https://kite.trade/docs/connect/v3/portfolio/#holdings-authorisation) along with an optional callback function that triggers when the holdings authorisation flow finishes.
Copyright © 2015 - 2025, Zerodha Technology Pvt. Ltd.
Made with

