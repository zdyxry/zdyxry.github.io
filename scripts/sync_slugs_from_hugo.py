#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pyyaml>=6.0",
# ]
# ///
"""
Sync slugs from Hugo content to Astro markdown files.
This script reads Hugo content files and updates corresponding Astro files 
to use the same slug (preserving original case).

Usage:
    uv run scripts/sync_slugs_from_hugo.py
    uv run scripts/sync_slugs_from_hugo.py --dry-run
"""

import argparse
import os
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class HugoPost:
    filepath: Path
    date: datetime
    slug: str  # The slug (from filename or folder name)
    title: str


def parse_hugo_date(date_str: str) -> datetime | None:
    """Parse date from Hugo frontmatter."""
    if not date_str:
        return None
    
    date_str = str(date_str).strip()
    
    # Try different formats
    formats = [
        '%Y-%m-%d %H:%M:%S',
        '%Y-%m-%d %H:%M',
        '%Y-%m-%dT%H:%M:%S.%fZ',
        '%Y-%m-%dT%H:%M:%S',
        '%Y-%m-%d',
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    
    return None


def extract_frontmatter(content: str) -> dict:
    """Extract frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}
    
    end_match = re.search(r'\n---\s*\n', content[3:])
    if not end_match:
        return {}
    
    fm_str = content[3:end_match.start() + 3]
    
    # Simple YAML parsing (just key: value pairs)
    result = {}
    current_key = None
    for line in fm_str.split('\n'):
        line = line.strip()
        if not line:
            continue
        
        # Check if it's a key-value pair
        if ':' in line and not line.startswith('-'):
            parts = line.split(':', 1)
            key = parts[0].strip()
            value = parts[1].strip() if len(parts) > 1 else ''
            # Remove quotes
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            result[key] = value
            current_key = key
    
    return result


def get_hugo_posts(hugo_content_dir: Path) -> list[HugoPost]:
    """Get all posts from Hugo content directory."""
    posts = []
    posts_dir = hugo_content_dir / 'posts'
    
    if not posts_dir.exists():
        print(f"Hugo posts directory not found: {posts_dir}")
        return posts
    
    for item in posts_dir.iterdir():
        if item.is_dir():
            # Folder-based post (e.g., /posts/My-Post-Title/)
            index_file = item / 'index.md'
            if index_file.exists():
                content = index_file.read_text(encoding='utf-8')
                fm = extract_frontmatter(content)
                date = parse_hugo_date(fm.get('date', ''))
                if date:
                    slug = item.name  # Folder name is the slug
                    posts.append(HugoPost(
                        filepath=index_file,
                        date=date,
                        slug=slug,
                        title=fm.get('title', '')
                    ))
        elif item.suffix == '.md':
            # File-based post (e.g., /posts/My-Post-Title.md)
            content = item.read_text(encoding='utf-8')
            fm = extract_frontmatter(content)
            date = parse_hugo_date(fm.get('date', ''))
            if date:
                slug = item.stem  # Filename without .md is the slug
                posts.append(HugoPost(
                    filepath=item,
                    date=date,
                    slug=slug,
                    title=fm.get('title', '')
                ))
    
    return posts


def get_astro_files(astro_content_dir: Path) -> dict[tuple[str, str], Path]:
    """Get Astro markdown files, indexed by (date, normalized_slug)."""
    files = {}
    
    for md_file in astro_content_dir.glob('*.md'):
        content = md_file.read_text(encoding='utf-8')
        fm = extract_frontmatter(content)
        
        date = parse_hugo_date(fm.get('date', '') or fm.get('pubDate', ''))
        slug = fm.get('slug', '') or fm.get('customSlug', '')
        
        if date and slug:
            date_str = date.strftime('%Y-%m-%d')
            # Normalize for matching
            normalized_slug = slug.lower()
            files[(date_str, normalized_slug)] = md_file
    
    return files


def update_astro_slug(filepath: Path, new_slug: str, dry_run: bool = False) -> bool:
    """Update the slug in an Astro markdown file."""
    content = filepath.read_text(encoding='utf-8')
    
    # Check current slug
    fm = extract_frontmatter(content)
    current_slug = fm.get('slug', '') or fm.get('customSlug', '')
    
    if current_slug == new_slug:
        return False  # No change needed
    
    # Update slug in content
    if 'slug:' in content[:1500]:
        # Replace existing slug line
        new_content = re.sub(
            r'^slug:\s*["\']?[^"\'\n]*["\']?\s*$',
            f'slug: "{new_slug}"',
            content,
            count=1,
            flags=re.MULTILINE
        )
    elif 'customSlug:' in content[:1500]:
        # Replace customSlug with slug
        new_content = re.sub(
            r'^customSlug:\s*["\']?[^"\'\n]*["\']?\s*$',
            f'slug: "{new_slug}"',
            content,
            count=1,
            flags=re.MULTILINE
        )
    else:
        # Add slug after title line
        new_content = re.sub(
            r'^(title:\s*.+)$',
            f'\\1\nslug: "{new_slug}"',
            content,
            count=1,
            flags=re.MULTILINE
        )
    
    if content == new_content:
        print(f"  ⚠ Could not update slug in {filepath.name}")
        return False
    
    if not dry_run:
        filepath.write_text(new_content, encoding='utf-8')
    
    return True


def main():
    parser = argparse.ArgumentParser(description='Sync slugs from Hugo to Astro')
    parser.add_argument('--hugo-dir', default='content', help='Hugo content directory')
    parser.add_argument('--astro-dir', default='astro-blog/src/content/posts', help='Astro content directory')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without writing')
    args = parser.parse_args()
    
    hugo_dir = Path(args.hugo_dir)
    astro_dir = Path(args.astro_dir)
    
    print(f"Hugo content dir: {hugo_dir}")
    print(f"Astro content dir: {astro_dir}")
    print()
    
    print("Reading Hugo posts...")
    hugo_posts = get_hugo_posts(hugo_dir)
    print(f"Found {len(hugo_posts)} Hugo posts")
    
    print("Reading Astro files...")
    astro_files = get_astro_files(astro_dir)
    print(f"Found {len(astro_files)} Astro files with date+slug")
    print()
    
    updated = 0
    not_found = 0
    skipped = 0
    
    for hugo_post in sorted(hugo_posts, key=lambda p: p.date):
        date_str = hugo_post.date.strftime('%Y-%m-%d')
        normalized_slug = hugo_post.slug.lower()
        key = (date_str, normalized_slug)
        
        if key in astro_files:
            astro_file = astro_files[key]
            
            if update_astro_slug(astro_file, hugo_post.slug, args.dry_run):
                print(f"✓ Updated: {astro_file.name}")
                print(f"    Slug: {normalized_slug} → {hugo_post.slug}")
                updated += 1
            else:
                skipped += 1
        else:
            # Try to match by date only if there's only one post that day
            date_matches = [(k, v) for k, v in astro_files.items() if k[0] == date_str]
            
            if len(date_matches) == 1:
                astro_file = date_matches[0][1]
                if update_astro_slug(astro_file, hugo_post.slug, args.dry_run):
                    print(f"✓ Updated (by date): {astro_file.name}")
                    print(f"    Slug: → {hugo_post.slug}")
                    updated += 1
                else:
                    skipped += 1
            else:
                not_found += 1
    
    print()
    print("=" * 60)
    print(f"Updated:   {updated}")
    print(f"Skipped:   {skipped} (already correct)")
    print(f"Not found: {not_found}")
    
    if args.dry_run:
        print("\n(Dry run - no files modified)")


if __name__ == '__main__':
    main()
