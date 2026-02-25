"""
Kite Connect Documentation Crawler
Scrapes https://kite.trade/docs/connect/v3/ and saves as structured markdown
"""

import asyncio
import os
import re
from pathlib import Path
from urllib.parse import urlparse, urljoin
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode


BASE_URL = "https://kite.trade/docs/connect/v3/"
OUTPUT_DIR = Path(__file__).parent / "output" / "kite-connect-v3"


def url_to_filepath(url: str) -> Path:
    """Convert URL to filesystem path preserving structure."""
    parsed = urlparse(url)
    path = parsed.path.strip("/")

    # Remove docs/connect/v3 prefix
    if path.startswith("docs/connect/v3/"):
        path = path.replace("docs/connect/v3/", "", 1).strip("/")
    elif path.startswith("connect/v3/"):
        path = path.replace("connect/v3/", "", 1).strip("/")

    # Handle index pages
    if path.endswith("index.html"):
        path = path.replace("index.html", "README.md")
    elif path == "":
        path = "README.md"
    elif not path.endswith(".md") and not path.endswith("/"):
        path = path + "/README.md"
    elif path.endswith("/"):
        path = path + "README.md"
    else:
        path = path.replace(".html", ".md")

    return OUTPUT_DIR / path


def extract_doc_links(html: str, base_url: str) -> list[str]:
    """Extract internal documentation links from HTML."""
    import re
    from html.parser import HTMLParser
    
    links = []
    
    class LinkParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == "a":
                attrs_dict = dict(attrs)
                href = attrs_dict.get("href", "")
                
                # Skip external, anchor, javascript, mailto links
                if not href or href.startswith(("#", "javascript:", "mailto:", "http")):
                    if not href.startswith(base_url.rstrip("/")):
                        return
                
                # Normalize URL
                full_url = urljoin(base_url, href)
                if full_url.startswith(base_url.rstrip("/")):
                    links.append(full_url)
    
    LinkParser().feed(html)
    return list(set(links))


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
            word_count_threshold=10,  # Skip very short content
        )
        
        result = await crawler.arun(url=url, config=config)
        
        if not result.success:
            print(f"  ❌ Failed: {url}")
            return None
        
        return {
            "url": url,
            "markdown": result.markdown,
            "html": result.html,
            "links": extract_doc_links(result.html or "", url),
        }
    
    except Exception as e:
        print(f"  ❌ Error: {url} - {e}")
        return None


async def crawl_docs():
    """Main crawler function."""
    visited = set()
    to_crawl = [BASE_URL]
    results = {}
    
    browser_config = BrowserConfig(
        headless=True,
        verbose=False,
    )
    
    async with AsyncWebCrawler(config=browser_config) as crawler:
        while to_crawl:
            url = to_crawl.pop(0)
            
            if url in visited:
                continue
            
            result = await crawl_page(crawler, url, visited)
            
            if result:
                results[url] = result
                print(f"  ✅ Success: {len(result['markdown'])} chars")
                
                # Add new links to crawl queue
                for link in result["links"]:
                    # Clean fragment identifiers
                    clean_link = link.split("#")[0]
                    if clean_link not in visited and clean_link not in to_crawl:
                        to_crawl.append(clean_link)
    
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
    print(f"🕷️  Starting Kite Connect docs crawler")
    print(f"Base URL: {BASE_URL}")
    print(f"Output: {OUTPUT_DIR}\n")
    
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    results = await crawl_docs()
    
    print(f"\n📊 Crawl complete: {len(results)} pages")
    
    save_results(results)
    
    print(f"\n✅ Done! Documentation saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
