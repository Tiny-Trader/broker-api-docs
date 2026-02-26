# Indian Broker API Documentation Scraper

A collection of Crawl4AI-based scrapers to download and maintain offline copies of Indian stock broker API documentation.

## 📊 Scraped Brokers

| Broker | Sections | Lines | Status |
|--------|----------|-------|--------|
| **Kite Connect v3** (Zerodha) | 18 | ~4,700 | ✅ Complete |
| **Angel One SmartAPI** | 19 | ~161,740 | ✅ Complete |
| **Upstox Open API** | 24 | ~1,200 | ✅ Complete |

**Total:** 61 files, ~167,640 lines of documentation

---

## 📁 Output Structure

```
output/
├── kite-connect-v3/          # Zerodha Kite Connect
│   ├── orders/README.md
│   ├── user/README.md
│   ├── websocket/README.md
│   └── ... (18 sections)
│
├── angel-one-smartapi/       # Angel One
│   ├── Orders/README.md
│   ├── User/README.md
│   ├── Gtt/README.md
│   └── ... (19 sections)
│
└── upstox-open-api/          # Upstox
    ├── orders/README.md
    ├── gtt-orders/README.md
    ├── authentication/README.md
    └── ... (24 sections)
```

---

## 🚀 Quick Start

### Prerequisites

```bash
# Install Crawl4AI
pip install crawl4ai

# Install Playwright browser
playwright install chromium
```

### Re-Scrape Documentation

**Kite Connect (Zerodha):**
```bash
python kite_crawler.py
python clean_docs.py
```

**Angel One SmartAPI:**
```bash
python angel_crawler.py
python clean_angel_docs.py
```

**Upstox Open API:**
```bash
python upstox_crawler.py
python clean_upstox_docs.py
```

### Verify All Documentation

```bash
python verify_all_docs.py
```

---

## 📋 Available Scripts

| Script | Purpose | Broker |
|--------|---------|--------|
| `kite_crawler.py` | Scrape Kite Connect docs | Zerodha |
| `angel_crawler.py` | Scrape Angel One docs | Angel Broking |
| `upstox_crawler.py` | Scrape Upstox docs | Upstox |
| `clean_docs.py` | Clean Kite markdown | Zerodha |
| `clean_angel_docs.py` | Clean Angel markdown | Angel Broking |
| `clean_upstox_docs.py` | Clean Upstox markdown | Upstox |
| `verify_all_docs.py` | Verify completeness | All |

---

## 🔄 Refresh Documentation

### Full Refresh (All Brokers)

```bash
# Re-scrape everything
python kite_crawler.py
python angel_crawler.py
python upstox_crawler.py

# Clean all
python clean_docs.py
python clean_angel_docs.py
python clean_upstox_docs.py

# Verify
python verify_all_docs.py

# Commit updates
git add output/
git commit -m "Refresh all broker docs - $(date +%Y-%m-%d)"
```

### Fresh Start (Delete & Re-scrape)

```bash
# Delete existing output
rm -rf output/kite-connect-v3
rm -rf output/angel-one-smartapi
rm -rf output/upstox-open-api

# Re-scrape from scratch
python kite_crawler.py && python clean_docs.py
python angel_crawler.py && python clean_angel_docs.py
python upstox_crawler.py && python clean_upstox_docs.py
```

---

## ➕ Adding New Brokers

To scrape a new broker's documentation:

1. **Copy existing crawler as template:**
   ```bash
   cp kite_crawler.py newbroker_crawler.py
   ```

2. **Edit the configuration:**
   ```python
   # In newbroker_crawler.py, change:
   BASE_URL = "https://api.newbroker.com/docs/"
   OUTPUT_DIR = Path(__file__).parent / "output" / "newbroker-api"
   ```

3. **Run the crawler:**
   ```bash
   python newbroker_crawler.py
   ```

4. **Create cleanup script if needed** (depends on site's HTML structure)

5. **Commit:**
   ```bash
   git add newbroker_crawler.py output/newbroker-api/
   git commit -m "Add NewBroker API documentation"
   ```

---

## 📅 Maintenance Schedule

| Frequency | Action |
|-----------|--------|
| **Monthly** | Check broker API changelogs for updates |
| **Quarterly** | Full re-scrape of all documentation |
| **After announcements** | Re-scrape affected broker |

---

## 🛠️ Technology Stack

- **Crawl4AI** - Async web crawler with JavaScript rendering
- **Playwright** - Headless browser automation
- **Python 3.10+** - Runtime environment

---

## 📝 Documentation Topics Covered

### Common Sections Across Brokers:
- ✅ Authentication & Login
- ✅ Orders (Regular, GTT, AMO, CO)
- ✅ Portfolio & Holdings
- ✅ Market Data & Quotes
- ✅ Historical Data
- ✅ User Profile & Funds
- ✅ Margins & Charges
- ✅ WebSocket Streaming
- ✅ Rate Limiting
- ✅ Error Codes
- ✅ SDKs & Libraries

---

## ⚠️ Notes

1. **Navigation Cleanup:** Some markdown files may contain residual navigation links. Cleanup scripts remove most noise automatically.

2. **Dynamic Content:** All scrapers use headless browsers to handle JavaScript-rendered documentation sites.

3. **Rate Limiting:** Scrapers respect website load times. Don't run too frequently to avoid being blocked.

4. **API Changes:** Broker APIs evolve. Re-scrape quarterly or after major announcements.

---

## 📄 License

This repository contains scraped documentation for **personal/offline use only**. All content copyright belongs to respective brokers:
- Zerodha (Kite Connect)
- Angel One (SmartAPI)
- Upstox (Open API)

For production use, always refer to official documentation:
- [Kite Connect](https://kite.trade/docs/connect/v3/)
- [Angel One SmartAPI](https://smartapi.angelbroking.com/docs)
- [Upstox Open API](https://upstox.com/developer/api-documentation/open-api)

---

## 🤝 Contributing

Found a broker with missing docs? Want to add a new scraper?

1. Fork the repository
2. Create a new crawler script
3. Test thoroughly
4. Submit a pull request

---

**Last Updated:** 2026-02-26
