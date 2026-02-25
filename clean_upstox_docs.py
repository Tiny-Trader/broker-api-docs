"""
Clean up Upstox scraped markdown files - Aggressive version.
"""

import re
from pathlib import Path


OUTPUT_DIR = Path(__file__).parent / "output" / "upstox-open-api"


def clean_markdown(content: str) -> str:
    """Remove navigation noise from Upstox markdown content."""
    
    lines = content.split('\n')
    cleaned_lines = []
    in_nav_block = False
    nav_block_count = 0
    lines_processed = 0
    
    for i, line in enumerate(lines):
        lines_processed += 1
        
        # Remove "Skip to main content" links
        if re.match(r'\[Skip to main content\]', line):
            continue
        
        # Remove Upstox Plus banner
        if '🚀 Introducing Upstox Plus' in line:
            continue
        
        # Remove logo/header links
        if re.match(r'\[ !\[Upstox\]', line):
            continue
        
        # Remove top navigation bar (Developer APIs, Business APIs, etc.)
        if re.match(r'\[Developer APIs\].*\[Business APIs\]', line):
            continue
        
        # Detect navigation block start (bulleted list with multiple API links)
        if re.match(r'^  \* \[Developer API\]', line):
            nav_block_count += 1
            if nav_block_count == 1:
                # First occurrence might be useful TOC, but skip for clean output
                pass
            in_nav_block = True
            continue
        
        # Skip navigation block lines
        if in_nav_block:
            # Nav items start with "    * [Section]"
            if re.match(r'^    +\* \[', line):
                continue
            # End of nav block on empty line or heading
            if line.strip() == '' or line.startswith('#'):
                in_nav_block = False
            continue
        
        # Remove "On this page" sections
        if re.match(r'^On this page', line, re.IGNORECASE):
            in_nav_block = True
            continue
        
        # Remove breadcrumb "Home › ..."
        if re.match(r'^Home\s*›', line):
            continue
        
        # Remove "Edit this page" links
        if re.match(r'^Edit this page', line, re.IGNORECASE):
            continue
        
        # Remove "Last updated" lines
        if re.match(r'^Last updated', line, re.IGNORECASE):
            continue
        
        # Remove footer-like links (Community, Apps)
        if re.match(r'^\[Community\]', line):
            continue
        if re.match(r'^\[Apps\]', line):
            continue
        
        cleaned_lines.append(line)
    
    content = '\n'.join(cleaned_lines)
    
    # Remove multiple consecutive blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Remove trailing whitespace
    content = '\n'.join(line.rstrip() for line in content.split('\n'))
    
    # Remove leading blank lines after frontmatter
    content = re.sub(r'^(---\n(?:.*\n)*?---\n)\n+', r'\1', content)
    
    return content


def clean_all_files():
    """Clean all markdown files in the output directory."""
    cleaned_count = 0
    total_chars_removed = 0
    
    for md_file in OUTPUT_DIR.rglob('*.md'):
        original_content = md_file.read_text(encoding='utf-8')
        cleaned_content = clean_markdown(original_content)
        
        chars_removed = len(original_content) - len(cleaned_content)
        if chars_removed > 0:
            md_file.write_text(cleaned_content, encoding='utf-8')
            print(f"✓ {md_file.relative_to(OUTPUT_DIR)} (-{chars_removed:,} chars)")
            cleaned_count += 1
            total_chars_removed += chars_removed
        else:
            print(f"- {md_file.relative_to(OUTPUT_DIR)} (no change)")
    
    print(f"\n✅ Cleaned {cleaned_count} files, removed {total_chars_removed:,} characters total")


if __name__ == "__main__":
    clean_all_files()
