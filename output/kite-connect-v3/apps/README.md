---
source: https://kite.trade/docs/connect/v3/apps/
scraped: true
---
Mobile and Desktop apps

 Kite Connect 3 / API documentation

# Mobile and Desktop apps[¶](https://kite.trade/docs/connect/v3/apps/#mobile-and-desktop-apps "Permanent link")
As described in the [authentication](https://kite.trade/docs/connect/v3/user/#authentication-and-token-exchange) section, the login flow ends with a redirect to your registered `redirect_url` with the `request_token` after a successful login. When this redirect end point is a web application, it is easy to get the token and exchange it for an `access_token`. When it's a desktop or a mobile application without a server backend, the approach is different.
Similar to how Google and Facebook authentication flows work on mobile apps, you will need to open a webview (browser view) component from within your application pointing to the login url. The entire login flow will happen within this webview. As it's an in-app component, you will have a certain level of control over it, including reading the current location (URL) of the component. It is then possible to monitor location changes using a change event or a poll timer to determine when the redirect happens, and extract the `request_token` from the URL.
Note
Don't forget to enable cookie (and 3rd party cookie) support in your webview or the login may not work.
In essence:
If you intent on distributing your mobile or desktop application to the public, do not embed the api_secret in the application. Use a server backend to do the token exchange on behalf of your application.
Copyright © 2015 - 2025, Zerodha Technology Pvt. Ltd.
Made with

