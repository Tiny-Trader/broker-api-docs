---
source: https://upstox.com/developer/api-documentation/mcp-integration
scraped: true
---
  * [](https://upstox.com/developer/api-documentation/)

The Upstox Model Context Protocol (MCP) integration enables AI assistants like Claude and VS Code to access your trading account data directly. This transforms generic AI tools into personalized financial advisors that understand your specific portfolio, positions, and market context.
## What is Model Context Protocol (MCP)?[​](https://upstox.com/developer/api-documentation/mcp-integration/#what-is-model-context-protocol-mcp "Direct link to heading")
Model Context Protocol (MCP) enables AI assistants to access your account-specific trading data in real-time, creating context-aware conversations about your actual investments. Instead of generic market advice, you get insights based on your holdings, positions, and account status.
MCP provides these capabilities:
  * **Account-scoped insights** : Analysis of your actual portfolio composition, performance, and risk exposure
  * **Real-time market context** : Current prices, volumes, and market movements integrated into your conversations
  * **Conversational API access** : Natural language queries that map to precise API calls and data retrieval
  * **Personalized research** : Stock analysis that considers how potential investments fit with your existing holdings

The fundamental advantage: traditional AI assistants work with publicly available information only. MCP-enabled assistants understand your specific financial situation, making their guidance relevant to your actual investment decisions.
**Compatible AI platforms** include Claude Desktop and VS Code with GitHub Copilot, giving you flexibility in choosing your preferred development or analysis environment.
## Setup Overview[​](https://upstox.com/developer/api-documentation/mcp-integration/#setup-overview "Direct link to heading")
Connect your Upstox account to AI assistants in minutes:
  1. **Select AI client** : [Claude Desktop](https://upstox.com/developer/api-documentation/mcp-integration/#claude-desktop) or [VS Code with GitHub Copilot](https://upstox.com/developer/api-documentation/mcp-integration/#vs-code-with-github-copilot)
  2. **Install dependencies** : Download from
  3. **Add MCP configuration** : Insert Upstox server details in your AI client settings
  4. **Authorize account** : Complete OAuth flow to securely link your trading account
  5. **Begin analysis** : Start asking questions about your portfolio and market data

Jump to [Claude Desktop setup](https://upstox.com/developer/api-documentation/mcp-integration/#claude-desktop) for the most popular integration or [VS Code setup](https://upstox.com/developer/api-documentation/mcp-integration/#vs-code-with-github-copilot) for developers.
## Prerequisites[​](https://upstox.com/developer/api-documentation/mcp-integration/#prerequisites "Direct link to heading")
Before setting up MCP integration, ensure you have:
  * An active Upstox trading account (non-dormant status) - [Learn about Upstox API authentication](https://upstox.com/developer/api-documentation/authentication)
  * Node.js installed on your computer
  * One of the supported AI clients:
    * Claude Desktop application
    * VS Code with GitHub Copilot extension
  * Familiarity with [Upstox API basics](https://upstox.com/developer/api-documentation/open-api) and [developer documentation](https://upstox.com/developer/api-documentation/)

## Setting up Upstox MCP[​](https://upstox.com/developer/api-documentation/mcp-integration/#setting-up-upstox-mcp "Direct link to heading")
### Claude Desktop[​](https://upstox.com/developer/api-documentation/mcp-integration/#claude-desktop "Direct link to heading")
**Install Node.js**
  * Download and install Node.js from
  * Verify installation by opening Command Prompt/Terminal and typing `node --version`

**Configure Claude Desktop**
  * Open Claude Desktop application
  * Go to Settings (gear icon)
  * Click on _Developer_ in the left sidebar
  * Click _Edit Config_
  * Add the following configuration:

```
{
    "mcpServers": {
        "Upstox MCP": {
            "command": "npx",
            "args": ["mcp-remote", "https://mcp.upstox.com/mcp"]
        }
    }
}

```

  * Save and restart Claude Desktop

**Verify Connection**
  * In Claude Desktop, look for the tools/hammer icon in the chat interface
  * Click it to verify Upstox MCP tools are available
  * Follow the authorization prompts to connect to your Upstox account

You can verify the connection by checking that "Upstox MCP" appears in your connectors list:
![Claude Desktop showing the &#39;Upstox MCP&#39; connector with account-scoped tools enabled for portfolio and quote access](https://upstox.com/developer/api-documentation/assets/images/claude-upstox-connector-6b2658a346a2d62e63cfdef6346d880b.webp#block)
When successfully connected, you should see the Upstox MCP tools available in Claude:
![Upstox MCP tools listed in Claude after connecting - portfolio, margins, and market data resources visible in the UI](https://upstox.com/developer/api-documentation/assets/images/claude-upstox-tools-329400970640d0c71ec0eb274f769516.webp#block)
### VS Code with GitHub Copilot[​](https://upstox.com/developer/api-documentation/mcp-integration/#vs-code-with-github-copilot "Direct link to heading")
**Prerequisites**
  * Visual Studio Code installed
  * Node.js installed
  * VS Code GitHub Copilot extension

**Configuration Steps**
  1. Open VS Code settings (File > Preferences > Settings, or press `Ctrl+,`)
  2. Search for "copilot chat mcp" or navigate to the GitHub Copilot Chat configuration
  3. Click on _Edit in settings.json_
  4. Add the following configuration to your settings.json file:

```
{
    "mcp": {
        "inputs": [],
        "servers": {
            "Upstox MCP": {
                "url": "https://mcp.upstox.com/mcp"
            }
        }
    }
}

```

  1. Save the settings file and restart VS Code
  2. Open the Copilot Chat panel and use the `/mcp` command to verify that Upstox is listed as an available MCP server
  3. When prompted, authorize your Upstox account to connect with VS Code

If you are a developer, you can also run the Upstox MCP server on your local machine for development and testing. Follow the setup steps in the
## Capabilities with Upstox MCP[​](https://upstox.com/developer/api-documentation/mcp-integration/#capabilities-with-upstox-mcp "Direct link to heading")
Once connected, your AI assistant can provide natural language analysis of your trading account and market data:
### Portfolio Insights[​](https://upstox.com/developer/api-documentation/mcp-integration/#portfolio-insights "Direct link to heading")
  * **Position breakdown** : Detailed view of current holdings with performance metrics
  * **Profit/loss tracking** : P&L analysis across custom time periods
  * **Diversification analysis** : Sector and asset allocation assessment
  * **Benchmark comparison** : Performance relative to market indices

### Account Data[​](https://upstox.com/developer/api-documentation/mcp-integration/#account-data "Direct link to heading")
  * **Available margins** : Real-time buying power and margin utilization - [See margin APIs](https://upstox.com/developer/api-documentation/margin)
  * **Profile information** : Account status and configuration details - [User profile APIs](https://upstox.com/developer/api-documentation/user)
  * **Activity summaries** : Daily trading and P&L overviews

### Market Research[​](https://upstox.com/developer/api-documentation/mcp-integration/#market-research "Direct link to heading")
  * **Individual stock analysis** : Research securities in context of your existing portfolio
  * **Technical indicators** : Chart analysis and trend identification

## Example Use Cases[​](https://upstox.com/developer/api-documentation/mcp-integration/#example-use-cases "Direct link to heading")
Here are some examples of how you can interact with your AI assistant using Upstox MCP:
### Stock Analysis and Hold/Sell Decision[​](https://upstox.com/developer/api-documentation/mcp-integration/#stock-analysis-and-holdsell-decision "Direct link to heading")
**Ask your AI** : "Check the stocks based on their current trends, valuations, Technicals etc and tell me if I should continue holding it or not"
### Corporate Governance Analysis[​](https://upstox.com/developer/api-documentation/mcp-integration/#corporate-governance-analysis "Direct link to heading")
**Ask your AI** : "Go through the latest board meetings and AGM/EGMs of the stocks in my company and derive the health of my portfolio"
### Professional Investment Model Analysis[​](https://upstox.com/developer/api-documentation/mcp-integration/#professional-investment-model-analysis "Direct link to heading")
**Ask your AI** : "Run investment models of Goldman Sacch and other top PMSs on my Portfolio and give me a deep down of the analysis"
### Portfolio Correlation Analysis[​](https://upstox.com/developer/api-documentation/mcp-integration/#portfolio-correlation-analysis "Direct link to heading")
**Ask your AI** : "Find the correlation (beta) of my portfolio to the NIFTY index over the last 3 years. Show it to me on a chart with Week on week and QoQ timeframes"
## Responsible Usage Guidelines[​](https://upstox.com/developer/api-documentation/mcp-integration/#responsible-usage-guidelines "Direct link to heading")
  * **Multiple Sources** : Use AI insights as one of many research tools in your investment process
  * **Verify Data** : Cross-check important information directly with the Upstox platform
  * **Independent Research** : Conduct your own fundamental and technical analysis
  * **Professional Advice** : Consult with qualified financial advisors for major investment decisions
  * **Risk Management** : Maintain proper risk management regardless of AI recommendations
  * **Stay Informed** : Keep up with market news and developments beyond AI analysis

## Authentication and Security[​](https://upstox.com/developer/api-documentation/mcp-integration/#authentication-and-security "Direct link to heading")
**Initial Authorization**
First-time setup requires OAuth authorization to securely link your Upstox account. This ensures your trading data access is controlled and authenticated.
**Daily Reconnection Policy**
For security, you must re-authorize your account connection daily. This prevents unauthorized access and ensures data freshness.
## Current Limitations[​](https://upstox.com/developer/api-documentation/mcp-integration/#current-limitations "Direct link to heading")
**Read-Only Access** : The MCP integration provides read-only access to your account data. You cannot place orders, modify positions, or execute trades through the AI assistant.
**Daily Re-authorization** : Account connections expire daily and require re-authentication for security.
**Feature Scope** : Supports portfolio analysis, account data, and market research.
## Troubleshooting[​](https://upstox.com/developer/api-documentation/mcp-integration/#troubleshooting "Direct link to heading")
### Connection Issues[​](https://upstox.com/developer/api-documentation/mcp-integration/#connection-issues "Direct link to heading")
If you're having trouble connecting:
  1. Verify Node.js is properly installed (`node --version`)
  2. Check that your Upstox account is active and not dormant
  3. Ensure you're using the correct MCP server URL: `https://mcp.upstox.com/mcp`
  4. Restart your AI client after configuration changes

### Authentication Problems[​](https://upstox.com/developer/api-documentation/mcp-integration/#authentication-problems "Direct link to heading")
If authorization fails:
  1. Check your internet connection
  2. Verify your Upstox login credentials work on the main platform
  3. Try disconnecting and reconnecting your account
  4. Clear browser cache if using web-based authentication

### AI Response Issues[​](https://upstox.com/developer/api-documentation/mcp-integration/#ai-response-issues "Direct link to heading")
If AI responses seem incorrect or incomplete:
  1. Remember that AI can make mistakes - always verify important information
  2. Try rephrasing your question more specifically
  3. Cross-check data directly with your Upstox account
  4. Consider asking for clarification or additional details

### Daily Reconnection[​](https://upstox.com/developer/api-documentation/mcp-integration/#daily-reconnection "Direct link to heading")
If you're prompted to reconnect:
  1. This is normal security behavior - reconnect once per day
  2. Use the same authorization process as initial setup
  3. Your AI assistant will regain access to your current data

## Support and Community[​](https://upstox.com/developer/api-documentation/mcp-integration/#support-and-community "Direct link to heading")
For technical support with MCP integration or general API questions, visit the [Upstox Developer Community](https://community.upstox.com/c/developer-api/15).
For account-specific issues, contact Upstox customer support through your trading platform.
**Related Documentation:**
  * [Upstox API Overview](https://upstox.com/developer/api-documentation/open-api) - Complete API documentation
  * [Authentication Guide](https://upstox.com/developer/api-documentation/authentication) - Learn about OAuth and API keys
  * [WebSocket Implementation](https://upstox.com/developer/api-documentation/websocket) - Real-time market data streaming
  * [Example Code](https://upstox.com/developer/api-documentation/example-code/introduction) - Sample implementations
  * [SDK Documentation](https://upstox.com/developer/api-documentation/sdk) - Official software development kits

## Frequently Asked Questions (FAQ)[​](https://upstox.com/developer/api-documentation/mcp-integration/#frequently-asked-questions-faq "Direct link to heading")
### How to integrate Upstox API with Claude AI?[​](https://upstox.com/developer/api-documentation/mcp-integration/#how-to-integrate-upstox-api-with-claude-ai "Direct link to heading")
To integrate Upstox API with Claude AI, install Node.js, configure Claude Desktop with the Upstox MCP server URL (`https://mcp.upstox.com/mcp`), and authenticate your Upstox trading account through the secure OAuth flow.
### Can I use Upstox MCP with VS Code?[​](https://upstox.com/developer/api-documentation/mcp-integration/#can-i-use-upstox-mcp-with-vs-code "Direct link to heading")
Yes, Upstox MCP works with VS Code through the GitHub Copilot extension. Add the MCP server configuration to your VS Code settings.json and use the `/mcp` command to access Upstox trading data.
### Is Upstox MCP integration free?[​](https://upstox.com/developer/api-documentation/mcp-integration/#is-upstox-mcp-integration-free "Direct link to heading")
Yes, connecting your Upstox account to AI assistants via MCP is completely free. You only need an active Upstox trading account and one of the supported AI clients.
### What Upstox API data can I access through MCP?[​](https://upstox.com/developer/api-documentation/mcp-integration/#what-upstox-api-data-can-i-access-through-mcp "Direct link to heading")
Through Upstox MCP, you can access portfolio holdings, positions, profit & loss data, account margins, market quotes, and historical trading information in real-time.
### How often do I need to reconnect Upstox MCP?[​](https://upstox.com/developer/api-documentation/mcp-integration/#how-often-do-i-need-to-reconnect-upstox-mcp "Direct link to heading")
For security purposes, you need to reconnect your Upstox account once per day. This ensures your trading data remains secure and prevents unauthorized access.
### Can I place trades through Upstox MCP?[​](https://upstox.com/developer/api-documentation/mcp-integration/#can-i-place-trades-through-upstox-mcp "Direct link to heading")
No, Upstox MCP provides read-only access to your account data. You cannot place orders, modify positions, or execute trades through the AI assistant for security reasons.
### Which AI assistants support Upstox MCP?[​](https://upstox.com/developer/api-documentation/mcp-integration/#which-ai-assistants-support-upstox-mcp "Direct link to heading")
Currently, Upstox MCP is supported by Claude Desktop and VS Code with GitHub Copilot extension. Support for additional AI platforms may be added in the future.
### What should I do if Upstox MCP authentication fails?[​](https://upstox.com/developer/api-documentation/mcp-integration/#what-should-i-do-if-upstox-mcp-authentication-fails "Direct link to heading")
If authentication fails, check your internet connection, verify your Upstox credentials work on the main platform, try disconnecting and reconnecting.
### How does Upstox MCP compare to other trading API integrations?[​](https://upstox.com/developer/api-documentation/mcp-integration/#how-does-upstox-mcp-compare-to-other-trading-api-integrations "Direct link to heading")
Upstox MCP offers seamless natural language interaction with your trading data, real-time portfolio analysis, and integration with popular AI assistants, making it more accessible than traditional API implementations.
### What are the system requirements for Upstox MCP?[​](https://upstox.com/developer/api-documentation/mcp-integration/#what-are-the-system-requirements-for-upstox-mcp "Direct link to heading")
You need Node.js installed on your computer, an active Upstox trading account (non-dormant), and either Claude Desktop or VS Code with GitHub Copilot extension.
### What if I have multiple Node.js or npx versions installed (for example via nvm)?[​](https://upstox.com/developer/api-documentation/mcp-integration/#what-if-i-have-multiple-nodejs-or-npx-versions-installed-for-example-via-nvm "Direct link to heading")
If you have multiple versions of `node` and `npx` installed (for example via `nvm`), your AI client might pick the wrong binary when starting the MCP server. This can lead to startup errors similar to those described in this
In this case, configure your MCP server by pointing directly to the full paths of `node` and `npx` instead of relying on the default `npx` on your `PATH`. For example:
```
{
  "mcpServers": {
    "mcp-server-upstox-api": {
      "command": "/Users/name/.nvm/versions/node/v20.19.4/bin/node",
      "args": [
        "/Users/name/.nvm/versions/node/v20.19.4/bin/npx",
        "mcp-remote",
        "https://mcp.upstox.com/mcp"
      ]
    }
  }
}

```

Adjust the paths and URL to match your local Node.js installation and MCP endpoint.
* * *
## Important Disclaimers[​](https://upstox.com/developer/api-documentation/mcp-integration/#important-disclaimers "Direct link to heading")
AI-generated analysis serves as research support, not investment advice. Always:
  * Verify information independently and conduct your own due diligence
  * Cross-check AI outputs with multiple sources and professional analysis
  * Consult qualified financial advisors for major investment decisions
  * Recognize that AI responses may contain errors or incomplete information
  * Treat AI insights as research starting points, not final guidance

Although MCP provides real-time account access, confirm critical information directly through the Upstox platform before taking action.
**Usage Terms** : This integration offers data access for analytical purposes only. Investment outcomes remain your responsibility. Neither Upstox nor AI platforms bear liability for decisions based on AI-generated insights.
[Previous Build using Sandbox](https://upstox.com/developer/api-documentation/build-using-sandbox)[Next Instruments](https://upstox.com/developer/api-documentation/instruments)
  * [What is Model Context Protocol (MCP)?](https://upstox.com/developer/api-documentation/mcp-integration/#what-is-model-context-protocol-mcp)
  * [Setup Overview](https://upstox.com/developer/api-documentation/mcp-integration/#setup-overview)
  * [Prerequisites](https://upstox.com/developer/api-documentation/mcp-integration/#prerequisites)
  * [Setting up Upstox MCP](https://upstox.com/developer/api-documentation/mcp-integration/#setting-up-upstox-mcp)
    * [Claude Desktop](https://upstox.com/developer/api-documentation/mcp-integration/#claude-desktop)
    * [VS Code with GitHub Copilot](https://upstox.com/developer/api-documentation/mcp-integration/#vs-code-with-github-copilot)
  * [Capabilities with Upstox MCP](https://upstox.com/developer/api-documentation/mcp-integration/#capabilities-with-upstox-mcp)
    * [Portfolio Insights](https://upstox.com/developer/api-documentation/mcp-integration/#portfolio-insights)
    * [Account Data](https://upstox.com/developer/api-documentation/mcp-integration/#account-data)
    * [Market Research](https://upstox.com/developer/api-documentation/mcp-integration/#market-research)
  * [Example Use Cases](https://upstox.com/developer/api-documentation/mcp-integration/#example-use-cases)
    * [Stock Analysis and Hold/Sell Decision](https://upstox.com/developer/api-documentation/mcp-integration/#stock-analysis-and-holdsell-decision)
    * [Corporate Governance Analysis](https://upstox.com/developer/api-documentation/mcp-integration/#corporate-governance-analysis)
    * [Professional Investment Model Analysis](https://upstox.com/developer/api-documentation/mcp-integration/#professional-investment-model-analysis)
    * [Portfolio Correlation Analysis](https://upstox.com/developer/api-documentation/mcp-integration/#portfolio-correlation-analysis)
  * [Responsible Usage Guidelines](https://upstox.com/developer/api-documentation/mcp-integration/#responsible-usage-guidelines)
  * [Authentication and Security](https://upstox.com/developer/api-documentation/mcp-integration/#authentication-and-security)
  * [Current Limitations](https://upstox.com/developer/api-documentation/mcp-integration/#current-limitations)
  * [Troubleshooting](https://upstox.com/developer/api-documentation/mcp-integration/#troubleshooting)
    * [Connection Issues](https://upstox.com/developer/api-documentation/mcp-integration/#connection-issues)
    * [Authentication Problems](https://upstox.com/developer/api-documentation/mcp-integration/#authentication-problems)
    * [AI Response Issues](https://upstox.com/developer/api-documentation/mcp-integration/#ai-response-issues)
    * [Daily Reconnection](https://upstox.com/developer/api-documentation/mcp-integration/#daily-reconnection)
  * [Support and Community](https://upstox.com/developer/api-documentation/mcp-integration/#support-and-community)
  * [Frequently Asked Questions (FAQ)](https://upstox.com/developer/api-documentation/mcp-integration/#frequently-asked-questions-faq)
    * [How to integrate Upstox API with Claude AI?](https://upstox.com/developer/api-documentation/mcp-integration/#how-to-integrate-upstox-api-with-claude-ai)
    * [Can I use Upstox MCP with VS Code?](https://upstox.com/developer/api-documentation/mcp-integration/#can-i-use-upstox-mcp-with-vs-code)
    * [Is Upstox MCP integration free?](https://upstox.com/developer/api-documentation/mcp-integration/#is-upstox-mcp-integration-free)
    * [What Upstox API data can I access through MCP?](https://upstox.com/developer/api-documentation/mcp-integration/#what-upstox-api-data-can-i-access-through-mcp)
    * [How often do I need to reconnect Upstox MCP?](https://upstox.com/developer/api-documentation/mcp-integration/#how-often-do-i-need-to-reconnect-upstox-mcp)
    * [Can I place trades through Upstox MCP?](https://upstox.com/developer/api-documentation/mcp-integration/#can-i-place-trades-through-upstox-mcp)
    * [Which AI assistants support Upstox MCP?](https://upstox.com/developer/api-documentation/mcp-integration/#which-ai-assistants-support-upstox-mcp)
    * [What should I do if Upstox MCP authentication fails?](https://upstox.com/developer/api-documentation/mcp-integration/#what-should-i-do-if-upstox-mcp-authentication-fails)
    * [How does Upstox MCP compare to other trading API integrations?](https://upstox.com/developer/api-documentation/mcp-integration/#how-does-upstox-mcp-compare-to-other-trading-api-integrations)
    * [What are the system requirements for Upstox MCP?](https://upstox.com/developer/api-documentation/mcp-integration/#what-are-the-system-requirements-for-upstox-mcp)
    * [What if I have multiple Node.js or npx versions installed (for example via nvm)?](https://upstox.com/developer/api-documentation/mcp-integration/#what-if-i-have-multiple-nodejs-or-npx-versions-installed-for-example-via-nvm)
  * [Important Disclaimers](https://upstox.com/developer/api-documentation/mcp-integration/#important-disclaimers)

[Contact us](https://upstox.com/contact-us/)·[About us](https://upstox.com/about/)·[FAQ](https://help.upstox.com/support/solutions/folders/278252)·[API Community](https://community.upstox.com/c/developer-api/15)
Made with ❤️ in India | Copyright © 2026, Upstox. Built with

