#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "requests>=2.31.0",
#     "pyyaml>=6.0",
#     "beautifulsoup4>=4.12.0",
#     "lxml>=5.0.0",
# ]
# ///
"""
Fix slugs in Astro markdown files to match Hugo URLs.
Fetches the Hugo sitemap and updates each markdown file's slug to match.

Usage:
    uv run scripts/fix_slugs.py
"""

import os
import re
import urllib.parse
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup


def get_hugo_urls(base_url: str) -> dict[str, str]:
    """Get all post URLs from Hugo sitemap and extract slug info."""
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
            date_str = f"{year}-{month}-{day}"
            url_info[date_str] = {
                'slug': slug,
                'path': path,
                'year': year,
                'month': month,
                'day': day,
            }
    
    return url_info


def extract_frontmatter(content: str) -> tuple[dict, str, str]:
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}, '', content
    
    # Find the end of frontmatter
    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        return {}, '', content
    
    end_pos = end_match.start() + 3
    frontmatter_str = content[3:end_pos]
    body = content[end_pos + end_match.end() - end_match.start():]
    
    try:
        frontmatter = yaml.safe_load(frontmatter_str)
        if frontmatter is None:
            frontmatter = {}
    except yaml.YAMLError:
        frontmatter = {}
    
    return frontmatter, frontmatter_str, body


def parse_date_from_filename(filename: str) -> str | None:
    """Extract date from filename like 2018-05-29-xxx.md."""
    match = re.match(r'^(\d{4})-(\d{2})-(\d{2})-', filename)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    return None


def get_date_from_frontmatter(fm: dict) -> str | None:
    """Extract date from frontmatter."""
    date_str = fm.get('date') or fm.get('pubDate')
    if date_str:
        # Handle various date formats
        date_str = str(date_str)
        match = re.match(r'(\d{4})-(\d{2})-(\d{2})', date_str)
        if match:
            return f"{match.group(1)}-{match.group(2)}-{match.group(3)}"
    return None


def update_markdown_slug(filepath: Path, hugo_urls: dict[str, str], dry_run: bool = False) -> bool:
    """Update a markdown file's slug to match Hugo URL."""
    content = filepath.read_text(encoding='utf-8')
    frontmatter, fm_str, body = extract_frontmatter(content)
    
    if not frontmatter:
        print(f"  ⚠ No frontmatter: {filepath.name}")
        return False
    
    # Get date from filename or frontmatter
    date_key = parse_date_from_filename(filepath.name)
    if not date_key:
        date_key = get_date_from_frontmatter(frontmatter)
    
    if not date_key:
        print(f"  ⚠ No date found: {filepath.name}")
        return False
    
    # Check if we have a Hugo URL for this date
    if date_key not in hugo_urls:
        # Try to find by title matching
        print(f"  ⚠ No Hugo URL for date {date_key}: {filepath.name}")
        return False
    
    hugo_info = hugo_urls[date_key]
    hugo_slug = hugo_info['slug']
    current_slug = frontmatter.get('slug', frontmatter.get('customSlug', ''))
    
    # Check if slug needs update
    if current_slug == hugo_slug:
        return False  # Already correct
    
    print(f"  Updating: {filepath.name}")
    print(f"    Current slug: {current_slug or '(none)'}")
    print(f"    Hugo slug:    {hugo_slug}")
    
    if dry_run:
        return True
    
    # Update the frontmatter
    # Use simple string replacement to preserve YAML formatting
    if 'slug:' in content[:1000]:
        # Replace existing slug
        new_content = re.sub(
            r'^slug:\s*.*$',
            f'slug: "{hugo_slug}"',
            content,
            count=1,
            flags=re.MULTILINE
        )
    elif 'customSlug:' in content[:1000]:
        # Replace customSlug with slug
        new_content = re.sub(
            r'^customSlug:\s*.*$',
            f'slug: "{hugo_slug}"',
            content,
            count=1,
            flags=re.MULTILINE
        )
    else:
        # Add slug after title
        new_content = re.sub(
            r'^(title:\s*.+)$',
            f'\\1\nslug: "{hugo_slug}"',
            content,
            count=1,
            flags=re.MULTILINE
        )
    
    filepath.write_text(new_content, encoding='utf-8')
    return True


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Fix markdown slugs to match Hugo URLs')
    parser.add_argument('--hugo-url', default='https://zdyxry.github.io', help='Hugo site URL')
    parser.add_argument('--content-dir', default='astro-blog/src/content/posts', help='Content directory')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be changed without modifying files')
    args = parser.parse_args()
    
    print(f"Fetching Hugo sitemap from {args.hugo_url}...")
    hugo_urls = get_hugo_urls(args.hugo_url)
    print(f"Found {len(hugo_urls)} post URLs in Hugo sitemap")
    print()
    
    content_dir = Path(args.content_dir)
    if not content_dir.exists():
        print(f"Error: Content directory not found: {content_dir}")
        return 1
    
    md_files = list(content_dir.glob('*.md'))
    print(f"Found {len(md_files)} markdown files")
    print()
    
    # Build a map from date -> list of files (some dates may have multiple posts)
    files_by_date = {}
    for f in md_files:
        date_key = parse_date_from_filename(f.name)
        if date_key:
            files_by_date.setdefault(date_key, []).append(f)
    
    # For dates with multiple files or no match, we need to match by title
    updated = 0
    skipped = 0
    errors = 0
    
    for md_file in sorted(md_files):
        try:
            date_key = parse_date_from_filename(md_file.name)
            if date_key and len(files_by_date.get(date_key, [])) == 1:
                # Simple case: one file per date
                if update_markdown_slug(md_file, hugo_urls, args.dry_run):
                    updated += 1
                else:
                    skipped += 1
            else:
                # Need to match by content/title - skip for now
                skipped += 1
        except Exception as e:
            print(f"  ✗ Error processing {md_file.name}: {e}")
            errors += 1
    
    print()
    print("=" * 60)
    print(f"Updated: {updated}")
    print(f"Skipped: {skipped}")
    print(f"Errors:  {errors}")
    
    if args.dry_run:
        print("\n(Dry run - no files were modified)")
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())
