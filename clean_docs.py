"""
Clean up scraped markdown files by removing navigation noise.
"""

import re
from pathlib import Path


OUTPUT_DIR = Path(__file__).parent / "output" / "kite-connect-v3"


def clean_markdown(content: str) -> str:
    """Remove navigation noise from markdown content."""
    
    # Remove "Skip to content" links
    content = re.sub(r'\[ Skip to content \]\([^)]+\)\n?', '', content)
    
    # Remove logo/image links at the top
    content = re.sub(r'\[ !\[logo\]\([^)]+\) \]\([^)]+ "[^"]+"\)\n?', '', content)
    
    # Remove "Kite Connect 3 / API documentation" headers (standalone lines)
    content = re.sub(r'^Kite Connect 3 / API documentation\s*$', '', content, flags=re.MULTILINE)
    
    # Remove "Initializing search" and "Type to start searching" text
    content = re.sub(r'^Initializing search\s*$', '', content, flags=re.MULTILINE)
    content = re.sub(r'^Type to start searching\s*$', '', content, flags=re.MULTILINE)
    
    # Remove navigation sidebar blocks using a more robust approach
    # Find all navigation blocks (lists starting with "  *")
    lines = content.split('\n')
    cleaned_lines = []
    skip_until_blank = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Detect navigation sidebar pattern
        if re.match(r'^  \* ', line):
            # Check if this is followed by more nav items (sidebar block)
            if i + 1 < len(lines) and (re.match(r'^  \* ', lines[i+1]) or re.match(r'^    \* ', lines[i+1])):
                skip_until_blank = True
                i += 1
                continue
        
        # Skip lines until we hit a blank line or content
        if skip_until_blank:
            if line.strip() == '' or line.startswith('#'):
                skip_until_blank = False
            i += 1
            continue
        
        # Remove standalone navigation reference lines
        if re.match(r'^  \* \[.*\]\(https://kite\.trade/docs/connect/v3/', line):
            i += 1
            continue
        
        cleaned_lines.append(line)
        i += 1
    
    content = '\n'.join(cleaned_lines)
    
    # Remove multiple consecutive blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Remove trailing whitespace from each line
    content = '\n'.join(line.rstrip() for line in content.split('\n'))
    
    # Remove leading blank lines after frontmatter
    content = re.sub(r'^(---\n(?:.*\n)*?---\n)\n+', r'\1', content)
    
    # Remove title followed by " Kite Connect 3 / API documentation" on next line (with leading space)
    content = re.sub(r'^(\w+)\n Kite Connect 3 / API documentation\n', r'\1\n', content, flags=re.MULTILINE)
    
    # Also handle cases where there's an extra blank line before the noise
    content = re.sub(r'^(\w+)\n\n Kite Connect 3 / API documentation\n', r'\1\n\n', content, flags=re.MULTILINE)
    
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
            print(f"✓ {md_file.relative_to(OUTPUT_DIR)} (-{chars_removed} chars)")
            cleaned_count += 1
            total_chars_removed += chars_removed
        else:
            print(f"- {md_file.relative_to(OUTPUT_DIR)} (no change)")
    
    print(f"\n✅ Cleaned {cleaned_count} files, removed {total_chars_removed:,} characters total")


if __name__ == "__main__":
    clean_all_files()
