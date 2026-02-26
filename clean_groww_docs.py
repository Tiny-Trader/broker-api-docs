"""
Clean up Groww scraped markdown files.
"""

import re
from pathlib import Path


OUTPUT_DIR = Path(__file__).parent / "output" / "groww-trade-api"


def clean_markdown(content: str) -> str:
    """Remove navigation noise from Groww markdown content."""
    
    lines = content.split('\n')
    cleaned_lines = []
    in_nav_block = False
    
    for line in lines:
        # Remove "Skip to content" links
        if re.match(r'\[Skip to content\]', line):
            continue
        
        # Remove logo/header links
        if re.match(r'\[!\[.*?\]\([^)]+\)\]\([^)]+\)', line):
            continue
        
        # Remove navigation sidebar patterns
        if re.match(r'^-+\s+\[', line) and 'docs' in line:
            in_nav_block = True
            continue
        
        # Skip nav block until we hit content
        if in_nav_block:
            if line.strip() == '' or line.startswith('#'):
                in_nav_block = False
            else:
                continue
        
        # Remove "On this page" sections
        if re.match(r'^##? On this page', line, re.IGNORECASE):
            in_nav_block = True
            continue
        
        # Remove breadcrumb navigation
        if re.match(r'^You are here:', line, re.IGNORECASE):
            continue
        if '›' in line and 'docs' in line.lower():
            if line.count('›') > 1:
                continue
        
        # Remove "Edit this page" links
        if re.match(r'^Edit this page', line, re.IGNORECASE):
            continue
        
        # Remove footer-like content
        if re.match(r'^Built with', line, re.IGNORECASE):
            continue
        if re.match(r'^Made with', line, re.IGNORECASE):
            continue
        if 'Copyright ©' in line and 'Groww' in line:
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
