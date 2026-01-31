#!/usr/bin/env node

/**
 * Fix URL Mapping from Hugo Sitemap
 * 
 * This script fetches Hugo's actual URLs from the sitemap and creates proper mappings
 * to Astro's URLs based on date matching.
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const CONFIG = {
  sourceDir: '/var/home/yiran/projects/zdyxry.github.io/content/posts',
  urlMappingFile: '/var/home/yiran/projects/zdyxry.github.io/astro-blog/url-mapping.json',
  sitemapUrl: 'https://zdyxry.github.io/sitemap.xml',
};

/**
 * Parse frontmatter from content
 */
function parseFrontmatter(content) {
  const frontmatterRegex = /^---\s*\n([\s\S]*?)\n---\s*\n([\s\S]*)$/;
  const match = content.match(frontmatterRegex);
  
  if (!match) {
    return { data: {}, content: content };
  }

  const frontmatterText = match[1];
  const body = match[2];
  const data = {};

  const lines = frontmatterText.split('\n');
  let currentKey = null;
  let currentList = null;

  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed) continue;

    if (trimmed.startsWith('- ')) {
      if (currentList !== null) {
        currentList.push(trimmed.slice(2).trim());
      }
      continue;
    }

    const colonIndex = trimmed.indexOf(':');
    if (colonIndex > 0) {
      if (currentKey && currentList !== null) {
        data[currentKey] = currentList;
      }

      const key = trimmed.slice(0, colonIndex).trim();
      let value = trimmed.slice(colonIndex + 1).trim();

      if (value === '') {
        currentList = [];
        currentKey = key;
      } else {
        if (value.startsWith('"') && value.endsWith('"')) {
          value = value.slice(1, -1);
        } else if (value.startsWith("'") && value.endsWith("'")) {
          value = value.slice(1, -1);
        }
        data[key] = value;
        currentList = null;
        currentKey = null;
      }
    }
  }

  if (currentKey && currentList !== null) {
    data[currentKey] = currentList;
  }

  return { data, content: body };
}

/**
 * Extract date info from date string
 */
function extractDateInfo(dateStr) {
  let date = new Date(dateStr);
  
  if (isNaN(date.getTime())) {
    date = new Date();
  }
  
  return {
    year: date.getFullYear().toString(),
    month: String(date.getMonth() + 1).padStart(2, '0'),
    day: String(date.getDate()).padStart(2, '0'),
  };
}

/**
 * Generate Astro slug
 */
function generateAstroSlug(text) {
  if (!text) return 'untitled';
  
  return text
    .toString()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .trim()
    .replace(/[^\w\s\u4e00-\u9fa5-]/g, '')
    .replace(/[\s_-]+/g, '-')
    .replace(/^-+|-+$/g, '');
}

/**
 * Main function
 */
async function fixUrlMappingFromSitemap() {
  console.log('[INFO] Starting URL mapping fix from sitemap...');
  
  // Fetch Hugo's sitemap
  console.log(`[INFO] Fetching sitemap from ${CONFIG.sitemapUrl}...`);
  const response = await fetch(CONFIG.sitemapUrl);
  const sitemapXml = await response.text();
  
  // Extract URLs from sitemap
  const urlRegex = /<loc>([^<]+)<\/loc>/g;
  const hugoUrls = [];
  let match;
  
  while ((match = urlRegex.exec(sitemapXml)) !== null) {
    const url = match[1];
    const path = new URL(url).pathname;
    // Only include article URLs (YYYY/MM/DD/slug/)
    if (path.match(/^\/\d{4}\/\d{2}\/\d{2}\/[^/]+\/$/)) {
      hugoUrls.push(path);
    }
  }
  
  console.log(`[INFO] Found ${hugoUrls.length} article URLs in sitemap`);
  
  // Load existing URL mapping
  const urlMappingData = JSON.parse(fs.readFileSync(CONFIG.urlMappingFile, 'utf8'));
  const existingMappings = urlMappingData.mappings;
  
  console.log(`[INFO] Loaded ${Object.keys(existingMappings).length} existing mappings`);
  
  // Build a map of date -> Astro URL from existing mappings
  const dateToAstroUrl = new Map();
  
  for (const [hugoUrl, astroUrl] of Object.entries(existingMappings)) {
    const dateMatch = astroUrl.match(/\/posts\/(\d{4}\/\d{2}\/\d{2})\//);
    if (dateMatch) {
      const date = dateMatch[1];
      if (!dateToAstroUrl.has(date)) {
        dateToAstroUrl.set(date, astroUrl);
      }
    }
  }
  
  console.log(`[INFO] Built date mapping for ${dateToAstroUrl.size} dates`);
  
  // Process Hugo URLs and add missing mappings
  let addedCount = 0;
  let existingCount = 0;
  
  for (const hugoUrl of hugoUrls) {
    // Skip if mapping already exists
    if (existingMappings[hugoUrl]) {
      existingCount++;
      continue;
    }
    
    // Extract date from Hugo URL
    const dateMatch = hugoUrl.match(/^(\/\d{4}\/\d{2}\/\d{2})\//);
    if (!dateMatch) {
      console.log(`[WARN] Could not extract date from ${hugoUrl}`);
      continue;
    }
    
    const date = dateMatch[1].replace(/^\//, '');
    const astroUrl = dateToAstroUrl.get(date);
    
    if (astroUrl) {
      // Add the mapping
      existingMappings[hugoUrl] = astroUrl;
      console.log(`[SUCCESS] Added: ${hugoUrl} → ${astroUrl}`);
      addedCount++;
    } else {
      console.log(`[WARN] No Astro URL found for date ${date} (Hugo URL: ${hugoUrl})`);
    }
  }
  
  // Update the mapping file
  urlMappingData.count = Object.keys(existingMappings).length;
  urlMappingData.mappings = existingMappings;
  
  fs.writeFileSync(CONFIG.urlMappingFile, JSON.stringify(urlMappingData, null, 2), 'utf8');
  
  console.log('\n=== Fix Statistics ===');
  console.log(`Existing mappings: ${existingCount}`);
  console.log(`New mappings added: ${addedCount}`);
  console.log(`Total mappings: ${Object.keys(existingMappings).length}`);
  console.log('======================\n');
  
  console.log('[SUCCESS] URL mapping fix completed!');
}

fixUrlMappingFromSitemap().catch(error => {
  console.error(`[ERROR] Fix failed: ${error.message}`);
  process.exit(1);
});
