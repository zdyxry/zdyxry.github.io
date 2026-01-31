#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "requests>=2.31.0",
#     "beautifulsoup4>=4.12.0",
#     "lxml>=5.0.0",
#     "pyyaml>=6.0",
# ]
# ///
"""
Sync slugs from Hugo sitemap to Astro markdown files.
This script reads the actual Hugo URLs from sitemap and updates Astro files.

Usage:
    uv run scripts/sync_slugs_from_sitemap.py
    uv run scripts/sync_slugs_from_sitemap.py --dry-run
"""

import argparse
import re
import urllib.parse
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def get_hugo_urls(base_url: str) -> dict[str, dict]:
    """Get all post URLs from Hugo sitemap."""
    sitemap_url = f"{base_url.rstrip('/')}/sitemap.xml"
    resp = requests.get(sitemap_url, timeout=30)
    soup = BeautifulSoup(resp.content, 'lxml-xml')
    
    url_info = {}
    for loc in soup.find_all('loc'):
        url = loc.text.strip()
        parsed = urllib.parse.urlparse(url)
        path = urllib.parse.unquote(parsed.path)  # Decode URL encoding
        
        # Match pattern like /YYYY/MM/DD/slug/
        match = re.match(r'^/(\d{4})/(\d{2})/(\d{2})/(.+?)/?$', path)
        if match:
            year, month, day, slug = match.groups()
            date_key = f"{year}-{month}-{day}"
            url_info[date_key] = {
                'slug': slug,
                'path': path,
                'year': year,
                'month': month,
                'day': day,
            }
    
    return url_info


def extract_frontmatter(content: str) -> dict:
    """Extract frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}
    
    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        return {}
    
    fm_str = content[3:end_match.start() + 3]
    
    result = {}
    for line in fm_str.split('\n'):
        line = line.strip()
        if not line or line.startswith('-'):
            continue
        
        if ':' in line:
            parts = line.split(':', 1)
            key = parts[0].strip()
            value = parts[1].strip() if len(parts) > 1 else ''
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            result[key] = value
    
    return result


def parse_date_from_filename(filename: str) -> str | None:
    """Extract date from filename like 2018-05-29-xxx.md."""
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})-', filename)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    return None


def update_markdown_slug(filepath: Path, new_slug: str, dry_run: bool = False) -> bool:
    """Update the slug in a markdown file."""
    content = filepath.read_text(encoding='utf-8')
    fm = extract_frontmatter(content)
    
    current_slug = fm.get('slug', '')
    if current_slug == new_slug:
        return False  # No change needed
    
    # Update slug in content
    if 'slug:' in content[:2000]:
        new_content = re.sub(
            r'^slug:\s*["\']?[^"\'\n]*["\']?\s*$',
            f'slug: "{new_slug}"',
            content,
            count=1,
            flags=re.MULTILINE
        )
    else:
        new_content = re.sub(
            r'^(title:\s*.+)$',
            f'\\1\nslug: "{new_slug}"',
            content,
            count=1,
            flags=re.MULTILINE
        )
    
    if content == new_content:
        return False
    
    if not dry_run:
        filepath.write_text(new_content, encoding='utf-8')
    
    return True


def main():
    parser = argparse.ArgumentParser(description='Sync slugs from Hugo sitemap to Astro')
    parser.add_argument('--hugo-url', default='https://zdyxry.github.io', help='Hugo site URL')
    parser.add_argument('--astro-dir', default='astro-blog/src/content/posts', help='Astro content directory')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without writing')
    args = parser.parse_args()
    
    astro_dir = Path(args.astro_dir)
    
    print(f"Fetching Hugo sitemap from {args.hugo_url}...")
    hugo_urls = get_hugo_urls(args.hugo_url)
    print(f"Found {len(hugo_urls)} post URLs in Hugo sitemap")
    print()
    
    # Get all Astro files
    md_files = list(astro_dir.glob('*.md'))
    print(f"Found {len(md_files)} markdown files")
    print()
    
    # Group files by date
    files_by_date = {}
    for f in md_files:
        date_key = parse_date_from_filename(f.name)
        if date_key:
            files_by_date.setdefault(date_key, []).append(f)
    
    updated = 0
    skipped = 0
    not_found = 0
    
    for date_key, hugo_info in sorted(hugo_urls.items()):
        if date_key not in files_by_date:
            not_found += 1
            continue
        
        files = files_by_date[date_key]
        hugo_slug = hugo_info['slug']
        
        if len(files) == 1:
            # Single file for this date - update it
            md_file = files[0]
            if update_markdown_slug(md_file, hugo_slug, args.dry_run):
                print(f"✓ Updated: {md_file.name}")
                print(f"    New slug: {hugo_slug}")
                updated += 1
            else:
                skipped += 1
        else:
            # Multiple files - try to match by slug similarity
            matched = False
            for md_file in files:
                fm = extract_frontmatter(md_file.read_text(encoding='utf-8'))
                current_slug = fm.get('slug', '')
                
                # Check if slugs are similar (case-insensitive, normalize special chars)
                def normalize(s):
                    return re.sub(r'[^a-z0-9\u4e00-\u9fa5]', '', s.lower())
                
                if normalize(current_slug) == normalize(hugo_slug) or normalize(md_file.stem.split('-', 3)[-1] if '-' in md_file.stem else md_file.stem) == normalize(hugo_slug):
                    if update_markdown_slug(md_file, hugo_slug, args.dry_run):
                        print(f"✓ Updated: {md_file.name}")
                        print(f"    New slug: {hugo_slug}")
                        updated += 1
                        matched = True
                        break
            
            if not matched:
                skipped += len(files)
    
    print()
    print("=" * 60)
    print(f"Updated:   {updated}")
    print(f"Skipped:   {skipped}")
    print(f"Not found: {not_found}")
    
    if args.dry_run:
        print("\n(Dry run - no files modified)")


if __name__ == '__main__':
    main()
