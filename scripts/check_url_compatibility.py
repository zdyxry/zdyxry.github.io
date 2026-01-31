#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "requests>=2.31.0",
#     "beautifulsoup4>=4.12.0",
#     "lxml>=5.0.0",
# ]
# ///
"""
URL compatibility checker for Hugo to Astro migration.
Crawls the Hugo site (production) and checks if all URLs exist in the Astro site (local preview).

Usage:
    uv run scripts/check_url_compatibility.py

Options:
    --hugo-url      Hugo site URL (default: https://zdyxry.github.io)
    --astro-url     Astro site URL (default: http://127.0.0.1:4321)
    --output        Output file for results (default: migration_check_results.json)
    --verbose       Enable verbose output
"""

import argparse
import json
import sys
import time
import urllib.parse
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

import requests
from bs4 import BeautifulSoup


@dataclass
class URLCheckResult:
    hugo_url: str
    astro_url: str
    hugo_status: int
    astro_status: int
    error: Optional[str] = None
    redirect_to: Optional[str] = None

    @property
    def is_ok(self) -> bool:
        return self.astro_status == 200 or (300 <= self.astro_status < 400)


@dataclass
class CheckReport:
    total_urls: int = 0
    ok_count: int = 0
    missing_count: int = 0
    redirect_count: int = 0
    error_count: int = 0
    results: list[URLCheckResult] = field(default_factory=list)
    missing_urls: list[URLCheckResult] = field(default_factory=list)
    by_category: dict[str, dict] = field(default_factory=lambda: defaultdict(lambda: {"ok": 0, "missing": 0}))


def normalize_url(url: str) -> str:
    """Normalize URL for comparison."""
    parsed = urllib.parse.urlparse(url)
    path = parsed.path
    # Ensure trailing slash for consistency
    if path and not path.endswith('/') and '.' not in path.split('/')[-1]:
        path = path + '/'
    return path


def get_all_urls_from_sitemap(base_url: str) -> list[str]:
    """Get all URLs from sitemap.xml."""
    sitemap_url = f"{base_url.rstrip('/')}/sitemap.xml"
    try:
        resp = requests.get(sitemap_url, timeout=30)
        if resp.status_code != 200:
            print(f"Warning: Could not fetch sitemap from {sitemap_url}")
            return []
        
        soup = BeautifulSoup(resp.content, 'lxml-xml')
        urls = []
        for loc in soup.find_all('loc'):
            urls.append(loc.text.strip())
        return urls
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return []


def crawl_site_for_urls(base_url: str, max_pages: int = 1000) -> set[str]:
    """Crawl site to find all internal URLs."""
    visited = set()
    to_visit = {base_url, f"{base_url}/"}
    found_urls = set()
    
    # Add common known paths
    common_paths = [
        "/", "/about/", "/friends/", "/running/", "/tags/", "/posts/",
        "/index.xml", "/atom.xml", "/sitemap.xml",
    ]
    for path in common_paths:
        to_visit.add(f"{base_url.rstrip('/')}{path}")
    
    parsed_base = urllib.parse.urlparse(base_url)
    base_domain = parsed_base.netloc
    
    while to_visit and len(visited) < max_pages:
        url = to_visit.pop()
        if url in visited:
            continue
        
        visited.add(url)
        
        try:
            resp = requests.get(url, timeout=10, allow_redirects=True)
            found_urls.add(url)
            
            if 'text/html' not in resp.headers.get('content-type', ''):
                continue
            
            soup = BeautifulSoup(resp.content, 'lxml')
            for link in soup.find_all('a', href=True):
                href = link['href']
                
                # Skip external links and anchors
                if href.startswith('#') or href.startswith('mailto:') or href.startswith('javascript:'):
                    continue
                
                # Resolve relative URLs
                full_url = urllib.parse.urljoin(url, href)
                parsed = urllib.parse.urlparse(full_url)
                
                # Only follow internal links
                if parsed.netloc == base_domain or not parsed.netloc:
                    clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                    if clean_url not in visited:
                        to_visit.add(clean_url)
                        
        except requests.RequestException:
            continue
    
    return found_urls


def categorize_url(path: str) -> str:
    """Categorize URL by type."""
    if path in ('/', ''):
        return 'home'
    elif path.startswith('/posts/') or (path.count('/') >= 4 and path[1:5].isdigit()):
        return 'post'
    elif path.startswith('/tags/'):
        return 'tag'
    elif '/running' in path:
        return 'running'
    elif '/about' in path:
        return 'about'
    elif '/friends' in path:
        return 'friends'
    elif path.endswith('.xml'):
        return 'feed'
    elif '/page/' in path:
        return 'pagination'
    else:
        return 'other'


def check_url(hugo_url: str, astro_base: str, path: str) -> URLCheckResult:
    """Check if a URL from Hugo site exists in Astro site."""
    hugo_full = hugo_url
    astro_full = f"{astro_base.rstrip('/')}{path}"
    
    hugo_status = 0
    astro_status = 0
    error = None
    redirect_to = None
    
    # Check Hugo site
    try:
        resp = requests.head(hugo_full, timeout=10, allow_redirects=False)
        hugo_status = resp.status_code
    except requests.RequestException as e:
        error = f"Hugo error: {e}"
    
    # Check Astro site
    try:
        resp = requests.get(astro_full, timeout=10, allow_redirects=False)
        astro_status = resp.status_code
        if 300 <= astro_status < 400:
            redirect_to = resp.headers.get('Location')
    except requests.RequestException as e:
        if error:
            error += f"; Astro error: {e}"
        else:
            error = f"Astro error: {e}"
    
    return URLCheckResult(
        hugo_url=hugo_full,
        astro_url=astro_full,
        hugo_status=hugo_status,
        astro_status=astro_status,
        error=error,
        redirect_to=redirect_to,
    )


def main():
    parser = argparse.ArgumentParser(description='Check URL compatibility between Hugo and Astro sites')
    parser.add_argument('--hugo-url', default='https://zdyxry.github.io', help='Hugo site URL')
    parser.add_argument('--astro-url', default='http://127.0.0.1:4321', help='Astro site URL')
    parser.add_argument('--output', default='migration_check_results.json', help='Output file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--check-sitemap-only', action='store_true', help='Only check URLs from sitemap')
    args = parser.parse_args()
    
    print(f"Hugo site: {args.hugo_url}")
    print(f"Astro site: {args.astro_url}")
    print()
    
    # Check if Astro site is running
    try:
        resp = requests.get(args.astro_url, timeout=5)
        print(f"✓ Astro site is accessible (status: {resp.status_code})")
    except requests.RequestException as e:
        print(f"✗ Cannot connect to Astro site at {args.astro_url}")
        print(f"  Please run: cd astro-blog && npm run preview")
        sys.exit(1)
    
    print()
    print("Collecting URLs from Hugo site...")
    
    # Get URLs from sitemap
    sitemap_urls = get_all_urls_from_sitemap(args.hugo_url)
    print(f"  Found {len(sitemap_urls)} URLs in sitemap")
    
    all_urls = set(sitemap_urls)
    
    # Also crawl the site for additional URLs
    if not args.check_sitemap_only:
        print("  Crawling site for additional URLs...")
        crawled_urls = crawl_site_for_urls(args.hugo_url, max_pages=500)
        all_urls.update(crawled_urls)
        print(f"  Found {len(crawled_urls)} URLs by crawling")
    
    print(f"\nTotal unique URLs to check: {len(all_urls)}")
    print()
    
    # Extract paths from URLs
    hugo_base_parsed = urllib.parse.urlparse(args.hugo_url)
    paths = set()
    for url in all_urls:
        parsed = urllib.parse.urlparse(url)
        if parsed.netloc == hugo_base_parsed.netloc or not parsed.netloc:
            paths.add(parsed.path or '/')
    
    # Sort paths for consistent output
    sorted_paths = sorted(paths)
    
    report = CheckReport()
    report.total_urls = len(sorted_paths)
    
    print("Checking URLs...")
    for i, path in enumerate(sorted_paths):
        if args.verbose or (i + 1) % 50 == 0:
            print(f"  [{i+1}/{len(sorted_paths)}] Checking: {path[:60]}...")
        
        hugo_full = f"{args.hugo_url.rstrip('/')}{path}"
        result = check_url(hugo_full, args.astro_url, path)
        report.results.append(result)
        
        category = categorize_url(path)
        
        if result.is_ok:
            report.ok_count += 1
            report.by_category[category]["ok"] += 1
            if result.redirect_to:
                report.redirect_count += 1
        elif result.error:
            report.error_count += 1
        else:
            report.missing_count += 1
            report.missing_urls.append(result)
            report.by_category[category]["missing"] += 1
            if args.verbose:
                print(f"    ✗ MISSING: {path} (Astro status: {result.astro_status})")
        
        # Small delay to avoid overwhelming the server
        time.sleep(0.05)
    
    print()
    print("=" * 60)
    print("RESULTS SUMMARY")
    print("=" * 60)
    print(f"Total URLs checked:  {report.total_urls}")
    print(f"OK (200/3xx):        {report.ok_count}")
    print(f"Missing (404):       {report.missing_count}")
    print(f"Redirects:           {report.redirect_count}")
    print(f"Errors:              {report.error_count}")
    print()
    
    print("By Category:")
    for cat, counts in sorted(report.by_category.items()):
        total = counts["ok"] + counts["missing"]
        missing_pct = (counts["missing"] / total * 100) if total else 0
        status = "✓" if counts["missing"] == 0 else "✗"
        print(f"  {status} {cat}: {counts['ok']}/{total} OK ({missing_pct:.1f}% missing)")
    
    print()
    
    if report.missing_urls:
        print("=" * 60)
        print(f"MISSING URLs ({len(report.missing_urls)} total)")
        print("=" * 60)
        
        # Group by category
        by_cat = defaultdict(list)
        for r in report.missing_urls:
            path = urllib.parse.urlparse(r.hugo_url).path
            cat = categorize_url(path)
            by_cat[cat].append(r)
        
        for cat, results in sorted(by_cat.items()):
            print(f"\n{cat.upper()} ({len(results)} missing):")
            for r in results[:20]:  # Show first 20
                path = urllib.parse.urlparse(r.hugo_url).path
                print(f"  - {path}")
            if len(results) > 20:
                print(f"  ... and {len(results) - 20} more")
    
    # Save full results to JSON
    output_data = {
        "summary": {
            "total": report.total_urls,
            "ok": report.ok_count,
            "missing": report.missing_count,
            "redirects": report.redirect_count,
            "errors": report.error_count,
        },
        "by_category": dict(report.by_category),
        "missing_urls": [
            {
                "hugo_url": r.hugo_url,
                "astro_url": r.astro_url,
                "hugo_status": r.hugo_status,
                "astro_status": r.astro_status,
                "path": urllib.parse.urlparse(r.hugo_url).path,
                "category": categorize_url(urllib.parse.urlparse(r.hugo_url).path),
            }
            for r in report.missing_urls
        ],
    }
    
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"\nFull results saved to: {args.output}")
    
    return 0 if report.missing_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
