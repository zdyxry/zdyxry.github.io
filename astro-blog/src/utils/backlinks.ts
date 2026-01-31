import { getCollection } from 'astro:content';

interface Backlink {
  slug: string;
  title: string;
}

// Cache for backlinks
let backlinksCache: Map<string, Backlink[]> | null = null;

/**
 * Generate Hugo-style slug from post data
 * Format: YYYY/MM/DD/slug
 */
function generateHugoSlug(post: { data: { pubDate?: Date; date?: Date; customSlug?: string }; slug: string }): string {
  const date = new Date(post.data.pubDate || post.data.date || Date.now());
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  const slugPart = post.data.customSlug || post.slug;
  return `${year}/${month}/${day}/${slugPart}`;
}

/**
 * Extract wiki links from markdown content
 * Supports [[Page Name]] and [[Page Name|Display Text]] syntax
 */
function extractWikiLinks(content: string): string[] {
  const wikiLinkRegex = /\[\[([^\]|]+)(?:\|[^\]]+)?\]\]/g;
  const links: string[] = [];
  let match;
  
  while ((match = wikiLinkRegex.exec(content)) !== null) {
    // Normalize the link target (convert to slug)
    const target = match[1]
      .trim()
      .toLowerCase()
      .replace(/\s+/g, '-')
      .replace(/[^a-z0-9\u4e00-\u9fa5-]/g, '');
    links.push(target);
  }
  
  return links;
}

/**
 * Build a map of all backlinks
 */
async function buildBacklinksMap(): Promise<Map<string, Backlink[]>> {
  const posts = await getCollection('posts');
  const backlinksMap = new Map<string, Backlink[]>();
  
  // Build a map of slugs to hugoSlugs for lookup
  const slugToHugoMap = new Map<string, string>();
  for (const post of posts) {
    const hugoSlug = generateHugoSlug(post);
    const slugPart = post.data.customSlug || post.slug;
    slugToHugoMap.set(slugPart, hugoSlug);
    // Also map by normalized title
    const normalizedTitle = post.data.title
      .toLowerCase()
      .replace(/\s+/g, '-')
      .replace(/[^a-z0-9\u4e00-\u9fa5-]/g, '');
    slugToHugoMap.set(normalizedTitle, hugoSlug);
  }
  
  for (const post of posts) {
    const content = typeof post.body === 'string' ? post.body : '';
    const links = extractWikiLinks(content);
    const sourceHugoSlug = generateHugoSlug(post);
    
    for (const linkTarget of links) {
      // Find the target post's hugoSlug
      const targetHugoSlug = slugToHugoMap.get(linkTarget);
      if (!targetHugoSlug) continue;
      
      if (!backlinksMap.has(targetHugoSlug)) {
        backlinksMap.set(targetHugoSlug, []);
      }
      
      const existing = backlinksMap.get(targetHugoSlug)!;
      if (!existing.some(b => b.slug === sourceHugoSlug)) {
        existing.push({
          slug: sourceHugoSlug,
          title: post.data.title,
        });
      }
    }
  }
  
  return backlinksMap;
}

/**
 * Get backlinks for a specific post
 * @param hugoSlug - The Hugo-style slug (YYYY/MM/DD/slug)
 */
export async function getBacklinks(hugoSlug: string): Promise<Backlink[]> {
  if (!backlinksCache) {
    backlinksCache = await buildBacklinksMap();
  }
  
  return backlinksCache.get(hugoSlug) || [];
}

/**
 * Clear the backlinks cache (useful during development)
 */
export function clearBacklinksCache(): void {
  backlinksCache = null;
}
