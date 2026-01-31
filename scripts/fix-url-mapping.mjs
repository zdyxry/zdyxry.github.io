#!/usr/bin/env node

/**
 * Fix URL Mapping Script
 * 
 * This script adds Hugo's original URL format (with slashes in slug) to url-mapping.json
 * Hugo preserves certain special characters like '/' in slugs, but our slugify function removes them.
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const CONFIG = {
  sourceDir: '/var/home/yiran/projects/zdyxry.github.io/content/posts',
  urlMappingFile: '/var/home/yiran/projects/zdyxry.github.io/astro-blog/url-mapping.json',
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
 * Generate Hugo's original slug from title (preserves special characters)
 * Hugo's slug generation is complex and depends on the theme/configuration.
 * This function tries to mimic Hugo's default behavior.
 */
function generateHugoOriginalSlug(title) {
  if (!title) return 'untitled';
  
  return title
    .toString()
    .trim()
    // Replace spaces with hyphens
    .replace(/\s+/g, '-')
    // Keep Chinese characters, letters, numbers, and some punctuation
    // Remove only certain special characters that Hugo typically removes
    .replace(/["'"<>\[\]{}|\\^`]/g, '');
}

/**
 * Generate slug the same way Astro does (slugify)
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
 * Main function
 */
async function fixUrlMapping() {
  console.log('[INFO] Starting URL mapping fix...');
  
  // Load existing URL mapping
  const urlMappingData = JSON.parse(fs.readFileSync(CONFIG.urlMappingFile, 'utf8'));
  const existingMappings = urlMappingData.mappings;
  
  console.log(`[INFO] Loaded ${Object.keys(existingMappings).length} existing mappings`);
  
  // Get all markdown files
  const files = [];
  
  function scanDir(dir) {
    const items = fs.readdirSync(dir);
    for (const item of items) {
      const fullPath = path.join(dir, item);
      const stat = fs.statSync(fullPath);
      
      if (stat.isDirectory()) {
        scanDir(fullPath);
      } else if (item.endsWith('.md')) {
        files.push(fullPath);
      }
    }
  }
  
  scanDir(CONFIG.sourceDir);
  console.log(`[INFO] Found ${files.length} markdown files`);
  
  let addedCount = 0;
  let skippedCount = 0;
  
  for (const file of files) {
    const content = fs.readFileSync(file, 'utf8');
    const { data } = parseFrontmatter(content);
    
    if (!data.title || !data.date) {
      console.log(`[WARN] Skipping ${file}: missing title or date`);
      continue;
    }
    
    const dateInfo = extractDateInfo(data.date);
    
    // Generate Hugo's original slug (from title, preserving special chars)
    const hugoOriginalSlug = generateHugoOriginalSlug(data.title);
    
    // Generate Astro slug (slugified)
    const astroSlug = data.slug ? generateAstroSlug(data.slug) : generateAstroSlug(data.title);
    
    // Generate URLs
    const hugoOriginalUrl = `/${dateInfo.year}/${dateInfo.month}/${dateInfo.day}/${hugoOriginalSlug}/`;
    const astroUrl = `/posts/${dateInfo.year}/${dateInfo.month}/${dateInfo.day}/${astroSlug}/`;
    
    // Check if this mapping already exists
    if (!existingMappings[hugoOriginalUrl]) {
      // Check if the slug contains special characters that Hugo preserves
      if (hugoOriginalSlug !== astroSlug && hugoOriginalSlug.includes('/')) {
        existingMappings[hugoOriginalUrl] = astroUrl;
        console.log(`[SUCCESS] Added mapping: ${hugoOriginalUrl} → ${astroUrl}`);
        addedCount++;
      } else {
        skippedCount++;
      }
    } else {
      skippedCount++;
    }
  }
  
  // Update the mapping file
  urlMappingData.count = Object.keys(existingMappings).length;
  urlMappingData.mappings = existingMappings;
  
  fs.writeFileSync(CONFIG.urlMappingFile, JSON.stringify(urlMappingData, null, 2), 'utf8');
  
  console.log('\n=== Fix Statistics ===');
  console.log(`New mappings added: ${addedCount}`);
  console.log(`Mappings skipped: ${skippedCount}`);
  console.log(`Total mappings: ${Object.keys(existingMappings).length}`);
  console.log('======================\n');
  
  console.log('[SUCCESS] URL mapping fix completed!');
}

fixUrlMapping().catch(error => {
  console.error(`[ERROR] Fix failed: ${error.message}`);
  process.exit(1);
});
