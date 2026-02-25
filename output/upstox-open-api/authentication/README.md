---
source: https://upstox.com/developer/api-documentation/authentication
scraped: true
---
  * [](https://upstox.com/developer/api-documentation/)

![Login flow](https://upstox.com/developer/api-documentation/assets/images/loginflow-58e94762548c9142d35fe1d479df21bf.webp#block)
Upstox uses standard OAuth 2.0 for customer authentication and login.
All logins are handled by upstox.com. There is no public endpoint for other applications to directly log the customer into their upstox.com. For security and compliance purposes, all logins and logouts are handled exclusively by upstox.com.


## Perform Authentication[​](https://upstox.com/developer/api-documentation/authentication/#perform-authentication "Direct link to heading")
The login window is a web page hosted at the following link.
```
https://api.upstox.com/v2/login/authorization/dialog

```

Your client application must trigger the opening of the above URL using Webview (or similar technology) and pass the following parameters:
Parameter | Description
---|---
client_id | The API key obtained during the app generation process.
redirect_uri | The URL to which the user will be redirected post authentication; must match the URL provided during app generation.
state | An optional parameter. If specified, will be returned after authentication, allowing for state continuity between request and callback.
response_type | This value must always be `code`.
URL construction:
```
https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id=<Your-API-Key-Here>&redirect_uri=<Your-Redirect-URI-Here>&state=<Your-Optional-State-Parameter-Here>

```

Sample URL:
```
https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id=615b1297-d443-3b39-ba19-1927fbcdddc7&redirect_uri=https%3A%2F%2Fwww.trading.tech%2Flogin%2Fupstox-v2&state=RnJpIERlYyAxNiAyMDIyIDE1OjU4OjUxIEdNVCswNTMwIChJbmRpYSBTdGFuZGFyZCBUaW1lKQ%3D%3D

```

In OAuth, client_id means API Key (not customer UCC) and client_secret means API Secret.
  * In some cases, redirect URLs with .php or similar extensions might get blocked due to security reasons. So you can avoid putting the redirect at the end of the URL and place it somewhere in the middle of the URL.
  * If you encounter an `Invalid Credentials` error, it likely stems from inconsistencies in the request parameters (`client_id`, `redirect_uri`, and `response_type`) compared to the information registered during app creation. Ensure you verify these parameters and correct any discrepancies before making another attempt.

The user will be redirected to the default login page where they will be able to log in.
![Login page](https://upstox.com/developer/api-documentation/assets/images/loginpage-bd1c2065c2c8d2c720f0ed703dd48131.webp#block)
You also have the option to select [here](https://help.upstox.com/support/solutions/articles/260346-what-is-totp-and-how-to-enable-totp-for-my-account-from-upstox-web-platform-).


## Receive Auth Code[​](https://upstox.com/developer/api-documentation/authentication/#receive-auth-code "Direct link to heading")
Upon successful authentication, this API will redirect to the URL specified in the `redirect_url` parameter, with the `code` essential for the token generation included within the request parameters.
```
https://<redirect_uri>?code=mk404x&state=XX56849

```

Name | Description
---|---
code | Utilize this code to generate the `access_token` as part of the next step.
state | Provided optionally if it was initially included in the request URL parameters.


## Generate Access Token[​](https://upstox.com/developer/api-documentation/authentication/#generate-access-token "Direct link to heading")
Once the user has authenticated with us, they will be redirected to your redirect URL with an authorization code. The parameter will come as `code` (query parameter).
The authorization code is valid for a single use, regardless of whether the access token generation succeeds or encounters an issue.
The last step is to make a server-to-server call between your backend server and Upstox to get an `access_token` using the authorization code. This can be done by calling the following service:
```
https://api.upstox.com/v2/login/authorization/token

```

You will need to pass the following parameters:
Parameter | Description
---|---
code | The `code` is a unique parameter included in the URL upon a successful [Authorize API](https://upstox.com/developer/api-documentation/authorize) authentication.
client_id | The API key obtained during the app generation process.
client_secret | The API secret obtained during the app generation process. This private key remains confidential, known only to the application and the authorization server.
redirect_uri | The URL provided during app generation.
grant_type | This value must always be `authorization_code`.
URL construction:
```
curl -X 'POST' 'https://api.upstox.com/v2/login/authorization/token' \
-H 'accept: application/json' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'code=<Your-Auth-Code-Here>&client_id=<Your-API-Key-Here>&client_secret=<Your-API-Secret-Here>&redirect_uri=<Your-Redirect-URI-Here>&grant_type=authorization_code'

```

Finally this will return an access token for you. This access token can be successfully passed back to your front-end application to access the Upstox API.
## Semi-Automated Token Generation[​](https://upstox.com/developer/api-documentation/authentication/#semi-automated-token-generation "Direct link to heading")
For apps that automate authentication requests but require manual approval:
  1. Configure your app to trigger the **auth request** at a specific time as detailed **[Access Token Request API](https://upstox.com/developer/api-documentation/access-token-request#request)**.
  2. When notified on your mobile, approve the authentication by either:
     * Clicking the link in the notification
     * Visiting **[Upstox Developer Apps](https://account.upstox.com/developer/apps)** and approving the request
  3. Once approved, the access token is delivered to the **notifier URL** set during app creation.
  4. Ensure your app **listens on the notifier URL** and stores the token for further use.

For more details on implementation and usage, please refer to the [Access Token Request Documentation](https://upstox.com/developer/api-documentation/access-token-request).
## Manual Token Generation[​](https://upstox.com/developer/api-documentation/authentication/#manual-token-generation "Direct link to heading")
If your app is a small utility where manual input is feasible, you can generate an access token directly:
  * Visit [Upstox Developer Apps](https://account.upstox.com/developer/apps), click on the app you've created.
  * Click **Generate** to create a new access token
  * Copy the generated token and use it in your app

This is ideal for one-time or occasional API usage where automation isn’t required.


## Extended Token[​](https://upstox.com/developer/api-documentation/authentication/#extended-token "Direct link to heading")
Upstox APIs now support the generation of an extended token in addition to the standard access token.
An extended token is designed for long-term use, primarily for read-only API calls. It remains valid for one year from the date it is generated, or until the user revokes access to their account from pro.upstox.com, whichever occurs first. This token allows access to specific user trade data. Below is a list of APIs that can be utilized with the extended token:
#### Supported APIs[​](https://upstox.com/developer/api-documentation/authentication/#supported-apis "Direct link to heading")
  * [Get Positions](https://upstox.com/developer/api-documentation/get-positions)
  * [Get Holdings](https://upstox.com/developer/api-documentation/get-holdings)
  * [Get Order Details](https://upstox.com/developer/api-documentation/get-order-details)
  * [Get Order History](https://upstox.com/developer/api-documentation/get-order-history)
  * [Get Order Book](https://upstox.com/developer/api-documentation/get-order-book)

Extended tokens are available for multi-client applications upon request. If your app requires an extended token, please reach out to our support team for enrollment and further assistance.
[Previous Sandbox](https://upstox.com/developer/api-documentation/sandbox)[Next API Structure](https://upstox.com/developer/api-documentation/request-response)
  * [Perform Authentication](https://upstox.com/developer/api-documentation/authentication/#perform-authentication)
  * [Receive Auth Code](https://upstox.com/developer/api-documentation/authentication/#receive-auth-code)
  * [Generate Access Token](https://upstox.com/developer/api-documentation/authentication/#generate-access-token)
  * [Semi-Automated Token Generation](https://upstox.com/developer/api-documentation/authentication/#semi-automated-token-generation)
  * [Manual Token Generation](https://upstox.com/developer/api-documentation/authentication/#manual-token-generation)
  * [Extended Token](https://upstox.com/developer/api-documentation/authentication/#extended-token)

[Contact us](https://upstox.com/contact-us/)·[About us](https://upstox.com/about/)·[FAQ](https://help.upstox.com/support/solutions/folders/278252)·[API Community](https://community.upstox.com/c/developer-api/15)
Made with ❤️ in India | Copyright © 2026, Upstox. Built with

