---
source: https://upstox.com/developer/api-documentation/sandbox
scraped: true
---
  * [](https://upstox.com/developer/api-documentation/)

## What is the Sandbox App?[​](https://upstox.com/developer/api-documentation/sandbox/#what-is-the-sandbox-app "Direct link to heading")
To simplify the integration process for developers working with the Upstox APIs, we have developed a sandbox environment that closely emulates the actual API integration experience. This setup allows developers to fully integrate and test their applications end-to-end on the payload before even connecting to the live market. In the sandbox, you can test strategies and integrations comprehensively without incurring any costs and without any time restrictions, unlike the live system which operates only during defined periods.
In simple terms, using the sandbox APIs ensures that you have thoroughly tested all your code and its interactions within the API before executing actual orders in the live market.
We will be rolling out the sandbox feature in a phased manner, so it is advisable to check the documentation regularly for updates on the availability of additional sandbox APIs.
## Create a Sandbox App and Generate a Token[​](https://upstox.com/developer/api-documentation/sandbox/#create-a-sandbox-app-and-generate-a-token "Direct link to heading")
Follow these steps to set up a sandbox app and generate an access token for API execution:
  1. **Access the Sandbox Section** - Visit the [Upstox Developer Apps](https://account.upstox.com/developer/apps#sandbox) page to view the sandbox section. Here, you can manage your app and token.
![Sandbox Dashboard](https://upstox.com/developer/api-documentation/assets/images/sand_1-8679dcb69bbd3fb81594dfacaedeb07c.png)
  2. **Start the App Creation Process** - Click the **New Sandbox App** button to open the application form. This form will allow you to specify the details of your new sandbox app. Note that the redirect URL and postback URL fields are included to collect data and currently do not serve any functional purpose for the sandbox app. These fields are mandatory for the live app and will soon mimic their functionality in the sandbox environment as well. We recommend filling out these URLs now to avoid having to update this information when the feature is fully implemented in the sandbox.
![App Creation Form](https://upstox.com/developer/api-documentation/assets/images/sand_2-671d1513ad71c8856c0afc56a1cfd1f3.png)
  3. **Complete the App Form** - Fill in the required fields in the form to define your sandbox app’s settings and features. After entering the information, click **Continue** to create your new sandbox app.
![Filled App Form](https://upstox.com/developer/api-documentation/assets/images/sand_3-3a6cfbb2dc16acc2327c77e9cffcec92.png)
  4. **Generate Your Access Token** - Navigate to your newly created sandbox app, and click the **Generate** button. This will create a new access token that you can use to authenticate API requests.
![Generate Token](https://upstox.com/developer/api-documentation/assets/images/sand_4-639d3c675a71b8ac14fe82eeaa7680ca.png)
  5. **Copy Your Access Token** - Once the token is generated, it will be displayed on the screen. Copy this token, which will be valid for 30 days, for use in your sandbox API executions.
![Token Display](https://upstox.com/developer/api-documentation/assets/images/sand_5-bd23327400df1446f62f66c5269c450a.png)

  * Only one sandbox app is permitted per user, ensuring focused and manageable testing environments.
  * Sandbox access tokens are exclusively for sandbox orders and cannot be used for live transactions.



## Identifying APIs with Sandbox Capability[​](https://upstox.com/developer/api-documentation/sandbox/#identifying-apis-with-sandbox-capability "Direct link to heading")
This section will guide you on how to identify APIs that have the sandbox feature enabled in the API documentation. As we progress towards making all APIs sandbox capable, the 'Sandbox enabled' flag will eventually be phased out. For now, here's how to spot and utilize APIs with sandbox capabilities from the documentation:
  1. **Look for the Sandbox Flag** - An API with sandbox capabilities will display a 'Sandbox enabled' flag next to the page title.
![Sandbox Flag](https://upstox.com/developer/api-documentation/assets/images/sand_6-53bed7dfb4e80333dcfc8ccca4c106d8.png)
  2. **Check the Request Setup** - A section with request-related fields will be present, often pre-filled with a sample payload, if applicable. Enter your sandbox token, generated as described in the previous sections, and click the 'Send API Request' button to proceed.
![Request Fields](https://upstox.com/developer/api-documentation/assets/images/sand_7-6d5dcb2b95067df18cfa0c0b48bbfd27.png)
  3. **Review the API Response** - Once executed, the response section will appear, showing the data received from the API. This is how you can confirm that the sandbox API is functioning as expected.
![API Response](https://upstox.com/developer/api-documentation/assets/images/sand_8-7023c03d58eef6dbb71de28c2b2bed4d.png)

### Sandbox enabled APIs[​](https://upstox.com/developer/api-documentation/sandbox/#sandbox-enabled-apis "Direct link to heading")
To facilitate easy navigation, we have listed APIs with sandbox capabilities within our documentation or developer portal.
  * [Place Order](https://upstox.com/developer/api-documentation/place-order)
  * [Place Order V3](https://upstox.com/developer/api-documentation/v3/place-order)
  * [Place Multi Order](https://upstox.com/developer/api-documentation/place-multi-order)
  * [Modify Order](https://upstox.com/developer/api-documentation/modify-order)
  * [Modify Order V3](https://upstox.com/developer/api-documentation/v3/modify-order)
  * [Cancel Order](https://upstox.com/developer/api-documentation/cancel-order)
  * [Cancel Order V3](https://upstox.com/developer/api-documentation/v3/cancel-order)

[Previous API Documentation – Fast Secure Free – Upstox](https://upstox.com/developer/api-documentation/open-api)[Next Authentication](https://upstox.com/developer/api-documentation/authentication)
  * [What is the Sandbox App?](https://upstox.com/developer/api-documentation/sandbox/#what-is-the-sandbox-app)
  * [Create a Sandbox App and Generate a Token](https://upstox.com/developer/api-documentation/sandbox/#create-a-sandbox-app-and-generate-a-token)
  * [Identifying APIs with Sandbox Capability](https://upstox.com/developer/api-documentation/sandbox/#identifying-apis-with-sandbox-capability)
    * [Sandbox enabled APIs](https://upstox.com/developer/api-documentation/sandbox/#sandbox-enabled-apis)

[Contact us](https://upstox.com/contact-us/)·[About us](https://upstox.com/about/)·[FAQ](https://help.upstox.com/support/solutions/folders/278252)·[API Community](https://community.upstox.com/c/developer-api/15)
Made with ❤️ in India | Copyright © 2026, Upstox. Built with

