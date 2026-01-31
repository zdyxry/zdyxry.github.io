#!/usr/bin/env node

/**
 * Hugo to Astro Content Migration Script (v3)
 * 
 * Preserves Hugo URL format: /YYYY/MM/DD/slug/
 * Processes wiki links to use Hugo format
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Configuration
const CONFIG = {
  sourceDir: '/var/home/yiran/projects/zdyxry.github.io/content/posts',
  targetDir: '/var/home/yiran/projects/zdyxry.github.io/astro-blog/src/content/posts',
  imagesDir: '/var/home/yiran/projects/zdyxry.github.io/astro-blog/public/images',
  backlinksFile: '/var/home/yiran/projects/zdyxry.github.io/astro-blog/backlinks.json',
};

// Statistics
const stats = {
  processed: 0,
  errors: 0,
  imagesCopied: 0,
  backlinksFound: 0,
};

const logger = {
  info: (msg) => console.log(`[INFO] ${msg}`),
  warn: (msg) => console.log(`[WARN] ${msg}`),
  error: (msg) => console.error(`[ERROR] ${msg}`),
  success: (msg) => console.log(`[SUCCESS] ${msg}`),
};

function ensureDir(dir) {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

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

function generateSlug(title) {
  return title
    .toLowerCase()
    .replace(/[^\w\s\u4e00-\u9fa5-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .replace(/^-|-$/g, '');
}

function getHugoSlug(date, slug) {
  const d = new Date(date);
  const year = d.getFullYear();
  const month = String(d.getMonth() + 1).padStart(2, '0');
  const day = String(d.getDate()).padStart(2, '0');
  return `${year}/${month}/${day}/${slug}`;
}

function processWikiLinks(content, slugMap) {
  const backlinks = [];
  
  // Match [[link]] or [[link|text]]
  const wikiLinkRegex = /\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g;
  
  const processedContent = content.replace(wikiLinkRegex, (match, target, displayText) => {
    const linkText = displayText || target;
    const targetSlug = generateSlug(target);
    
    // Find matching post
    let foundHugoSlug = null;
    for (const [slug, data] of slugMap.entries()) {
      if (data.title === target || 
          generateSlug(data.title) === targetSlug ||
          slug === targetSlug) {
        foundHugoSlug = data.hugoSlug;
        break;
      }
    }
    
    if (foundHugoSlug) {
      backlinks.push({ target: targetSlug, text: linkText });
      stats.backlinksFound++;
      return `[${linkText}](/posts/${foundHugoSlug}/)`;
    }
    
    // If not found, keep as plain text
    return `[${linkText}]`;
  });
  
  return { content: processedContent, backlinks };
}

function copyImages(content, sourceDir) {
  const imageRegex = /!\[([^\]]*)\]\(([^)]+)\)/g;
  let processedContent = content;
  const matches = [...content.matchAll(imageRegex)];
  
  for (const match of matches) {
    const [fullMatch, alt, imagePath] = match;
    
    // Skip external URLs
    if (imagePath.startsWith('http') || imagePath.startsWith('//')) {
      continue;
    }
    
    // Resolve image path
    const resolvedPath = path.resolve(sourceDir, imagePath);
    
    if (fs.existsSync(resolvedPath)) {
      const ext = path.extname(resolvedPath);
      const newFileName = `${Date.now()}-${Math.random().toString(36).substr(2, 9)}${ext}`;
      const targetPath = path.join(CONFIG.imagesDir, newFileName);
      
      fs.copyFileSync(resolvedPath, targetPath);
      stats.imagesCopied++;
      
      // Update content
      processedContent = processedContent.replace(
        fullMatch,
        `![${alt}](/images/${newFileName})`
      );
    } else {
      logger.warn(`Image not found: ${imagePath}`);
    }
  }
  
  return processedContent;
}

async function collectSlugs(files) {
  const slugMap = new Map();
  
  for (const file of files) {
    const content = fs.readFileSync(file, 'utf8');
    const { data } = parseFrontmatter(content);
    
    const title = data.title || path.basename(file, '.md');
    const date = new Date(data.date || Date.now());
    const slug = data.slug || generateSlug(title);
    const hugoSlug = getHugoSlug(date, slug);
    
    slugMap.set(slug, {
      title,
      slug,
      hugoSlug,
      date,
      file,
    });
  }
  
  return slugMap;
}

async function migrateContent() {
  logger.info('Starting Hugo to Astro migration (v3 - Hugo URL format)...');
  logger.info(`Source: ${CONFIG.sourceDir}`);
  logger.info(`Target: ${CONFIG.targetDir}`);
  
  ensureDir(CONFIG.targetDir);
  ensureDir(CONFIG.imagesDir);
  
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
  logger.info(`Found ${files.length} markdown files`);
  
  // First pass: collect all slugs
  logger.info('Collecting slugs...');
  const slugMap = await collectSlugs(files);
  logger.info(`Collected ${slugMap.size} unique slugs`);
  
  // Second pass: process files
  logger.info('Processing files...');
  
  const allBacklinks = [];
  
  for (const [slug, slugData] of slugMap.entries()) {
    try {
      const { file, hugoSlug, date } = slugData;
      const content = fs.readFileSync(file, 'utf8');
      const { data, content: body } = parseFrontmatter(content);
      
      // Generate new filename: YYYY-MM-DD-slug.md (for file organization)
      const d = new Date(data.date || Date.now());
      const year = d.getFullYear();
      const month = String(d.getMonth() + 1).padStart(2, '0');
      const day = String(d.getDate()).padStart(2, '0');
      const fileSlug = data.slug || generateSlug(data.title || slug);
      const newFileName = `${year}-${month}-${day}-${fileSlug}.md`;
      
      // Process content
      let processedBody = body;
      
      // Copy images
      processedBody = copyImages(processedBody, path.dirname(file));
      
      // Process wiki links
      const { content: finalBody, backlinks } = processWikiLinks(processedBody, slugMap);
      
      // Build new frontmatter
      const newFrontmatter = {
        title: data.title || fileSlug,
        date: d.toISOString(),
        customSlug: fileSlug,
        tags: data.tags || [],
      };
      
      if (data.description) {
        newFrontmatter.description = data.description;
      }
      
      // Write file
      const frontmatterYaml = Object.entries(newFrontmatter)
        .map(([key, value]) => {
          if (Array.isArray(value)) {
            return `${key}:\n${value.map(v => `  - ${v}`).join('\n')}`;
          }
          return `${key}: ${value}`;
        })
        .join('\n');
      
      const newContent = `---\n${frontmatterYaml}\n---\n\n${finalBody}`;
      const targetPath = path.join(CONFIG.targetDir, newFileName);
      
      fs.writeFileSync(targetPath, newContent);
      
      // Store backlinks
      for (const backlink of backlinks) {
        allBacklinks.push({
          from: hugoSlug,
          to: backlink.target,
          text: backlink.text,
        });
      }
      
      stats.processed++;
      logger.success(`Created: ${targetPath}`);
      
    } catch (error) {
      stats.errors++;
      logger.error(`Failed to process ${slugData.file}: ${error.message}`);
    }
  }
  
  // Write backlinks file
  fs.writeFileSync(CONFIG.backlinksFile, JSON.stringify({
    generated: new Date().toISOString(),
    count: allBacklinks.length,
    links: allBacklinks,
  }, null, 2));
  
  // Print statistics
  console.log('\n=== Migration Statistics ===');
  console.log(`Files processed: ${stats.processed}`);
  console.log(`Errors: ${stats.errors}`);
  console.log(`Images copied: ${stats.imagesCopied}`);
  console.log(`Backlinks found: ${stats.backlinksFound}`);
  console.log('===========================\n');
  
  logger.info('Migration completed successfully!');
  logger.info(`URL format: /posts/YYYY/MM/DD/slug/`);
}

migrateContent().catch(error => {
  logger.error(`Migration failed: ${error.message}`);
  process.exit(1);
});
