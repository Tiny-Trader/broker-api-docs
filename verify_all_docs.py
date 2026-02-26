"""
Final verification script - Check all scraped documentation is complete.
"""

import os
import re
import asyncio
from pathlib import Path
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig


def verify_angel_one():
    """Verify Angel One SmartAPI scraping."""
    print("=" * 60)
    print("ANGEL ONE SMARTAPI VERIFICATION")
    print("=" * 60)
    
    # Read HTML sample for live site pages
    html_file = Path("angel_docs_html_sample.txt")
    if not html_file.exists():
        print("⚠️  angel_docs_html_sample.txt not found!")
        return
    
    html = html_file.read_text()
    live_pages = set()
    for match in re.findall(r'href="/docs/([^"]*)"', html):
        clean = match.rstrip('/').split('#')[0]
        if clean:
            live_pages.add(clean)
    
    # Get scraped directories
    scraped_dir = Path("output/angel-one-smartapi")
    scraped_pages = set()
    if scraped_dir.exists():
        for item in scraped_dir.iterdir():
            if item.is_dir():
                scraped_pages.add(item.name)
    
    print(f"\n📄 Live site pages: {len(live_pages)}")
    for p in sorted(live_pages):
        print(f"   {p}")
    
    print(f"\n📁 Scraped directories: {len(scraped_pages)}")
    for p in sorted(scraped_pages):
        print(f"   ✓ {p}")
    
    # Compare
    live_normalized = {p.lower().replace('-', '') for p in live_pages}
    scraped_normalized = {p.lower().replace('-', '') for p in scraped_pages}
    
    missing = live_normalized - scraped_normalized
    extra = scraped_normalized - live_normalized
    
    print("\n📊 Comparison:")
    if not missing:
        print("   ✅ ALL PAGES SCRAPED!")
    else:
        print(f"   ⚠️  Missing: {missing}")
    
    if extra:
        print(f"   ℹ️  Extra (not on live): {extra}")
    
    # Content stats
    total_lines = 0
    for md_file in scraped_dir.rglob("*.md"):
        total_lines += len(md_file.read_text().splitlines())
    
    print(f"\n📈 Content stats:")
    print(f"   Total lines: {total_lines:,}")
    print(f"   Files: {len(list(scraped_dir.rglob('*.md')))}")


async def verify_kite():
    """Verify Kite Connect scraping."""
    print("\n" + "=" * 60)
    print("KITE CONNECT V3 VERIFICATION")
    print("=" * 60)
    
    # Crawl to get live pages
    async with AsyncWebCrawler(config=BrowserConfig(headless=True, verbose=False)) as crawler:
        result = await crawler.arun(
            url="https://kite.trade/docs/connect/v3/",
            config=CrawlerRunConfig()
        )
        
        html = result.html or ""
        live_pages = set()
        
        # Find all internal links
        for match in re.findall(r'href="(https://kite\.trade/docs/connect/v3/[^"]*)"', html):
            clean = match.replace("https://kite.trade/docs/connect/v3/", "").rstrip('/')
            if clean and not clean.startswith('#'):
                live_pages.add(clean.split('#')[0])
        
        # Also check for relative links
        for match in re.findall(r'href="/docs/connect/v3/([^"]*)"', html):
            clean = match.rstrip('/')
            if clean and not clean.startswith('#'):
                live_pages.add(clean.split('#')[0])
    
    # Get scraped directories
    scraped_dir = Path("output/kite-connect-v3")
    scraped_pages = set()
    if scraped_dir.exists():
        for item in scraped_dir.iterdir():
            if item.is_dir():
                scraped_pages.add(item.name)
    
    print(f"\n📄 Live site pages found: {len(live_pages)}")
    for p in sorted(live_pages)[:10]:
        print(f"   {p}")
    if len(live_pages) > 10:
        print(f"   ... and {len(live_pages) - 10} more")
    
    print(f"\n📁 Scraped directories: {len(scraped_pages)}")
    for p in sorted(scraped_pages):
        print(f"   ✓ {p}")
    
    # Content stats
    total_lines = 0
    for md_file in scraped_dir.rglob("*.md"):
        total_lines += len(md_file.read_text().splitlines())
    
    print(f"\n📈 Content stats:")
    print(f"   Total lines: {total_lines:,}")
    print(f"   Files: {len(list(scraped_dir.rglob('*.md')))}")
    
    # Check key sections exist
    key_sections = ['orders', 'user', 'websocket', 'portfolio', 'market-quotes']
    print(f"\n🔑 Key sections check:")
    for section in key_sections:
        if section in scraped_pages:
            print(f"   ✓ {section}")
        else:
            print(f"   ⚠️  MISSING: {section}")


async def verify_upstox():
    """Verify Upstox Open API scraping."""
    print("\n" + "=" * 60)
    print("UPSTOX OPEN API VERIFICATION")
    print("=" * 60)
    
    # Known sections from the site
    expected_sections = {
        'open-api', 'authentication', 'orders', 'gtt-orders', 'portfolio',
        'market-quote', 'market-information', 'historical-data', 'instruments',
        'option-chain', 'margins', 'charges', 'trade-profit-and-loss', 'user',
        'login', 'rate-limiting', 'request-response', 'sdk',
        'uplink-business', 'mcp-integration', 'sandbox',
        'expired-instruments', 'announcements', 'appendix'
    }
    
    # Get scraped directories
    scraped_dir = Path("output/upstox-open-api")
    scraped_pages = set()
    if scraped_dir.exists():
        for item in scraped_dir.iterdir():
            if item.is_dir():
                scraped_pages.add(item.name.lower().replace('-', ''))
    
    print(f"\n📄 Expected sections: {len(expected_sections)}")
    
    print(f"\n📁 Scraped directories: {len([d for d in scraped_dir.iterdir() if d.is_dir()])}")
    for p in sorted(scraped_dir.iterdir()):
        if p.is_dir():
            print(f"   ✓ {p.name}")
    
    # Compare
    expected_normalized = {s.lower().replace('-', '') for s in expected_sections}
    
    missing = expected_normalized - scraped_pages
    extra = scraped_pages - expected_normalized
    
    print("\n📊 Comparison:")
    if not missing:
        print("   ✅ ALL PAGES SCRAPED!")
    else:
        print(f"   ⚠️  Missing: {missing}")
    
    if extra:
        print(f"   ℹ️  Extra: {extra}")
    
    # Content stats
    total_lines = 0
    for md_file in scraped_dir.rglob("*.md"):
        total_lines += len(md_file.read_text().splitlines())
    
    print(f"\n📈 Content stats:")
    print(f"   Total lines: {total_lines:,}")
    print(f"   Files: {len(list(scraped_dir.rglob('*.md')))}")


async def verify_groww():
    """Verify Groww Trade API scraping."""
    print("\n" + "=" * 60)
    print("GROWW TRADE API VERIFICATION")
    print("=" * 60)
    
    # Known sections from the site
    expected_sections = {
        'python-sdk', 'orders', 'smart-orders', 'portfolio', 'margin',
        'live-data', 'historical-data', 'backtesting', 'feed', 'instruments',
        'user', 'annexures', 'exceptions', 'changelog',
        'curl'
    }
    
    # Get scraped directories
    scraped_dir = Path("output/groww-trade-api")
    scraped_pages = set()
    if scraped_dir.exists():
        for item in scraped_dir.iterdir():
            if item.is_dir():
                scraped_pages.add(item.name.lower().replace('-', ''))
                # Also check subdirectories
                for subitem in item.iterdir():
                    if subitem.is_dir():
                        scraped_pages.add(f"{item.name}/{subitem.name}".lower().replace('-', ''))
    
    print(f"\n📄 Expected sections: {len(expected_sections)}")
    
    print(f"\n📁 Scraped structure:")
    for p in sorted(scraped_dir.iterdir()):
        if p.is_dir():
            print(f"   ✓ {p.name}/")
            for sub in sorted(p.iterdir()):
                if sub.is_dir():
                    print(f"      └── {sub.name}/")
    
    # Content stats
    total_lines = 0
    for md_file in scraped_dir.rglob("*.md"):
        total_lines += len(md_file.read_text().splitlines())
    
    print(f"\n📈 Content stats:")
    print(f"   Total lines: {total_lines:,}")
    print(f"   Files: {len(list(scraped_dir.rglob('*.md')))}")
    
    # Check key sections exist
    print(f"\n🔑 Key sections check:")
    key_sections = ['orders', 'portfolio', 'live-data', 'margin']
    for section in key_sections:
        found = any(section in str(p).lower() for p in scraped_dir.rglob('*.md'))
        if found:
            print(f"   ✓ {section}")
        else:
            print(f"   ⚠️  MISSING: {section}")


async def main():
    verify_angel_one()
    await verify_kite()
    await verify_upstox()
    await verify_groww()
    
    print("\n" + "=" * 60)
    print("VERIFICATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
