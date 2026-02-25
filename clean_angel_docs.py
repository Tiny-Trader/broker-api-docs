"""
Clean up Angel One SmartAPI scraped markdown files - Aggressive version.
"""

import re
from pathlib import Path


OUTPUT_DIR = Path(__file__).parent / "output" / "angel-one-smartapi"


def clean_markdown(content: str) -> str:
    """Remove navigation noise from Angel One markdown content."""
    
    lines = content.split('\n')
    cleaned_lines = []
    
    # State tracking
    in_nav_block = False
    nav_block_count = 0
    lines_after_frontmatter = 0
    skip_until_heading = False
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Track lines after frontmatter
        if stripped and not stripped.startswith('---'):
            lines_after_frontmatter += 1
        
        # Detect navigation block: "*   * [API Documentation]"
        if re.match(r'^\*\s+\*\s+\[API Documentation\]', line):
            nav_block_count += 1
            if nav_block_count == 1:
                # First occurrence - keep as TOC might be useful
                cleaned_lines.append(line)
                in_nav_block = True
            else:
                # Second+ occurrence - skip entire block
                skip_until_heading = True
            continue
        
        # Skip lines in duplicate nav block until we hit heading or blank
        if skip_until_heading:
            if stripped == '' or line.startswith('#'):
                skip_until_heading = False
            continue
        
        # Remove top nav items (Enable TOTP, Forum, FAQ, SignUp, Login)
        if re.match(r'^\*\s+\[(Enable TOTP|Forum|FAQ|SignUp|Login)\]', line):
            continue
        
        # Remove inline nav bullets that are clearly menu items (not content)
        # Pattern: "* [Section Name](https://smartapi.angelbroking.com/docs/Section)"
        # Only in first 50 lines and followed by more nav items
        if lines_after_frontmatter < 50:
            if re.match(r'^\*\s+\[(Introduction|Response structure|Error Codes|User|GTT|Orders|Brokerage|Portfolio|EDIS|Postback|Margin|Market Data|Option Greeks|WebSocket|Instruments|Historical|Rate Limit|Top Gainers)\]', line):
                # Check if indented sub-items follow
                if i + 1 < len(lines) and '    * [' in lines[i + 1]:
                    in_nav_block = True
                    continue
        
        # If in first nav block and line is indented nav item, skip
        if in_nav_block and stripped.startswith('* [') and 'smartapi.angelbroking.com' in line:
            continue
        
        # Exit nav block on heading
        if line.startswith('#'):
            in_nav_block = False
        
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
