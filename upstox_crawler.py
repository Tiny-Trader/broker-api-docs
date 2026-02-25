"""
Upstox Open API Documentation Crawler - Fixed for relative links
"""

import asyncio
import re
from pathlib import Path
from urllib.parse import urlparse, urljoin
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode


BASE_URL = "https://upstox.com/developer/api-documentation/"
OUTPUT_DIR = Path(__file__).parent / "output" / "upstox-open-api"

# All documentation sections to crawl
DOC_SECTIONS = [
    "open-api",
    "authentication",
    "orders",
    "gtt-orders",
    "portfolio",
    "market-quote",
    "market-information",
    "historical-data",
    "instruments",
    "option-chain",
    "margins",
    "charges",
    "trade-profit-and-loss",
    "user",
    "login",
    "rate-limiting",
    "request-response",
    "sdk",
    "uplink-business/introduction",
    "mcp-integration",
    "sandbox",
    "expired-instruments",
    "announcements",
    "appendix",
]


def url_to_filepath(url: str) -> Path:
    """Convert URL to filesystem path preserving structure."""
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    
    # Remove developer/api-documentation prefix
    if path.startswith("developer/api-documentation/"):
        path = path.replace("developer/api-documentation/", "", 1).strip("/")
    
    # Handle paths
    if path == "" or path == "open-api":
        path = "README.md"
    elif not path.endswith(".md") and not path.endswith("/"):
        path = path + "/README.md"
    elif path.endswith("/"):
        path = path + "README.md"
    else:
        path = path.replace(".html", ".md")
    
    return OUTPUT_DIR / path


async def crawl_page(crawler: AsyncWebCrawler, url: str, visited: set) -> dict:
    """Crawl a single page and return its content."""
    if url in visited:
        return None
    
    visited.add(url)
    print(f"Crawling: {url}")
    
    try:
        config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            exclude_external_links=True,
            word_count_threshold=10,
        )
        
        result = await crawler.arun(url=url, config=config)
        
        if not result.success:
            print(f"  ❌ Failed: {url}")
            return None
        
        return {
            "url": url,
            "markdown": result.markdown,
            "html": result.html,
        }
    
    except Exception as e:
        print(f"  ❌ Error: {url} - {e}")
        return None


async def crawl_docs():
    """Main crawler function - crawl all known sections."""
    visited = set()
    results = {}
    
    browser_config = BrowserConfig(
        headless=True,
        verbose=False,
    )
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        for section in DOC_SECTIONS:
            url = f"{BASE_URL}{section}"
            
            if url in visited:
                continue
            
            result = await crawl_page(crawler, url, visited)
            
            if result:
                results[url] = result
                print(f"  ✅ Success: {len(result['markdown'])} chars")
    
    return results


def save_results(results: dict):
    """Save crawled content to markdown files."""
    for url, data in results.items():
        filepath = url_to_filepath(url)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        # Add frontmatter
        content = f"""---
source: {url}
scraped: true
---

{data['markdown']}
"""
        
        filepath.write_text(content, encoding="utf-8")
        print(f"Saved: {filepath.relative_to(OUTPUT_DIR)}")


async def main():
    """Entry point."""
    print(f"🕷️  Starting Upstox Open API docs crawler")
    print(f"Base URL: {BASE_URL}")
    print(f"Output: {OUTPUT_DIR}\n")
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    results = await crawl_docs()
    
    print(f"\n📊 Crawl complete: {len(results)} pages")
    
    save_results(results)
    
    print(f"\n✅ Done! Documentation saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
