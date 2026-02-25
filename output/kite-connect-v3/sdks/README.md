---
source: https://kite.trade/docs/connect/v3/sdks/
scraped: true
---
Libraries and SDKs

 Kite Connect 3 / API documentation

# Libraries and SDKs[¶](https://kite.trade/docs/connect/v3/sdks/#libraries-and-sdks "Permanent link")
Below is a list of client libraries for Kite Connect written in various programming languages. These libraries allow you to interact with the APIs without having to make raw HTTP calls.
Language | Repository |  |
---|---|---|---
Python |  |  | [Documentation](https://kite.trade/docs/pykiteconnect/v4/)
Go |  |  |
Java |  |  | [Documentation](https://kite.trade/docs/javakiteconnect/v3/)
PHP |  |  | [Documentation](https://kite.trade/docs/phpkiteconnect/v3/classes/KiteConnect-KiteConnect.html)
Node.js |  |  | [Documentation](https://kite.trade/docs/kiteconnectjs/v3/)
.NET/C# |  |  | [Documentation](https://kite.trade/docs/kiteconnectdotnet/v3/)
## Version and API endpoint[¶](https://kite.trade/docs/connect/v3/sdks/#version-and-api-endpoint "Permanent link")
The current major stable version of the API is **3**. All requests go to it by default. It is recommended that a specific version be requested explicitly for production applications as major releases may break older implementations.
Note
This version is a KiteConnect backend API version and should not be confused with the specific library release version.
### Root API endpoint[¶](https://kite.trade/docs/connect/v3/sdks/#root-api-endpoint "Permanent link")
**`https://api.kite.trade`**
### Requesting a particular version[¶](https://kite.trade/docs/connect/v3/sdks/#requesting-a-particular-version "Permanent link")
To request a particular version of the API, set the HTTP header `X-Kite-version: v` where `v` is the version number, major or full (eg: 1 or 1.3 or 3)
Copyright © 2015 - 2025, Zerodha Technology Pvt. Ltd.
Made with

