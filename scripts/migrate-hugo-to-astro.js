#!/usr/bin/env node

/**
 * Hugo to Astro Content Migration Script
 * 
 * This script migrates content from Hugo format to Astro format.
 * Features:
 * - Frontmatter conversion (Hugo → Astro)
 * - Bidirectional link processing [[link]] → [link](/posts/slug)
 * - Image copying to public/images/
 * - URL mapping generation
 * - Backlinks tracking
 */

const fs = require('fs');
const path = require('path');

// Configuration
const CONFIG = {
  sourceDir: '/var/home/yiran/projects/zdyxry.github.io/content/posts',
  targetDir: '/var/home/yiran/projects/zdyxry.github.io/astro-blog/src/content/posts',
  imagesDir: '/var/home/yiran/projects/zdyxry.github.io/astro-blog/public/images',
  backlinksFile: '/var/home/yiran/projects/zdyxry.github.io/astro-blog/backlinks.json',
  urlMappingFile: '/var/home/yiran/projects/zdyxry.github.io/astro-blog/url-mapping.json',
};

// Statistics
const stats = {
  processed: 0,
  skipped: 0,
  errors: 0,
  imagesCopied: 0,
  backlinksFound: 0,
};

/**
 * Logger utility
 */
const logger = {
  info: (msg) => console.log(`[INFO] ${msg}`),
  warn: (msg) => console.log(`[WARN] ${msg}`),
  error: (msg) => console.error(`[ERROR] ${msg}`),
  success: (msg) => console.log(`[SUCCESS] ${msg}`),
  debug: (msg) => process.env.DEBUG && console.log(`[DEBUG] ${msg}`),
};

/**
 * Ensure directory exists
 */
function ensureDir(dir) {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
    logger.info(`Created directory: ${dir}`);
  }
}

/**
 * Parse frontmatter from content (fallback if gray-matter is not available)
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

  // Simple YAML-like parsing
  const lines = frontmatterText.split('\n');
  let currentKey = null;
  let currentList = null;

  for (const line of lines) {
    const trimmed = line.trim();
    
    // Skip empty lines
    if (!trimmed) continue;

    // Check for list item
    if (trimmed.startsWith('- ')) {
      if (currentList !== null) {
        currentList.push(trimmed.slice(2).trim());
      }
      continue;
    }

    // Check for key-value pair
    const colonIndex = trimmed.indexOf(':');
    if (colonIndex > 0) {
      // Save previous list if exists
      if (currentKey && currentList !== null) {
        data[currentKey] = currentList;
      }

      const key = trimmed.slice(0, colonIndex).trim();
      let value = trimmed.slice(colonIndex + 1).trim();

      // Check if next lines are list items
      currentKey = key;
      if (value === '') {
        currentList = [];
      } else {
        currentList = null;
        // Remove quotes if present
        if ((value.startsWith('"') && value.endsWith('"')) ||
            (value.startsWith("'") && value.endsWith("'"))) {
          value = value.slice(1, -1);
        }
        data[key] = value;
      }
    }
  }

  // Save last list if exists
  if (currentKey && currentList !== null) {
    data[currentKey] = currentList;
  }

  return { data, content: body };
}

/**
 * Try to use gray-matter if available, otherwise use fallback
 */
function matter(content) {
  try {
    const grayMatter = require('gray-matter');
    return grayMatter(content);
  } catch (e) {
    return parseFrontmatter(content);
  }
}

/**
 * Convert date to ISO 8601 format
 */
function toISODate(dateStr) {
  if (!dateStr) return new Date().toISOString();
  
  const date = new Date(dateStr);
  if (isNaN(date.getTime())) {
    logger.warn(`Invalid date: ${dateStr}, using current date`);
    return new Date().toISOString();
  }
  
  return date.toISOString();
}

/**
 * Extract date components from date string or filename
 */
function extractDateInfo(dateStr, filename) {
  let date = new Date(dateStr);
  
  // Try to extract from filename if date is invalid
  if (isNaN(date.getTime())) {
    const dateMatch = filename.match(/(\d{4})-(\d{2})-(\d{2})/);
    if (dateMatch) {
      date = new Date(`${dateMatch[1]}-${dateMatch[2]}-${dateMatch[3]}`);
    }
  }
  
  // Default to current date if still invalid
  if (isNaN(date.getTime())) {
    date = new Date();
  }
  
  return {
    year: date.getFullYear().toString(),
    month: String(date.getMonth() + 1).padStart(2, '0'),
    day: String(date.getDate()).padStart(2, '0'),
    iso: date.toISOString(),
  };
}

/**
 * Generate slug from title or filename
 */
function generateSlug(data, filename) {
  // Use existing slug if available
  if (data.slug) {
    return slugify(data.slug);
  }

  // Try to extract from filename (remove date prefix)
  const nameWithoutExt = path.basename(filename, path.extname(filename));
  const datePrefixMatch = nameWithoutExt.match(/^\d{4}-\d{2}-\d{2}-(.+)$/);
  if (datePrefixMatch) {
    return slugify(datePrefixMatch[1]);
  }

  // Use title
  if (data.title) {
    return slugify(data.title);
  }

  // Fallback to filename
  return slugify(nameWithoutExt);
}

/**
 * Create URL-friendly slug
 * Supports Chinese characters by keeping them as-is
 */
function slugify(text) {
  if (!text) return 'untitled';
  
  return text
    .toString()
    .normalize('NFD')                    // Normalize unicode
    .replace(/[\u0300-\u036f]/g, '')     // Remove diacritics
    .toLowerCase()
    .trim()
    // Keep Chinese characters, letters, numbers, spaces and hyphens
    .replace(/[^\w\s\u4e00-\u9fa5-]/g, '')
    .replace(/[\s_-]+/g, '-')            // Replace spaces and underscores with -
    .replace(/^-+|-+$/g, '');            // Remove leading/trailing -
}

/**
 * Generate Hugo URL from date and slug
 */
function generateHugoUrl(dateInfo, slug) {
  return `/${dateInfo.year}/${dateInfo.month}/${dateInfo.day}/${slug}/`;
}

/**
 * Generate Astro URL from date and slug
 */
function generateAstroUrl(dateInfo, slug) {
  return `/posts/${dateInfo.year}/${dateInfo.month}/${dateInfo.day}/${slug}/`;
}

/**
 * Convert frontmatter from Hugo to Astro format
 */
function convertFrontmatter(data, slug, dateInfo) {
  const astroData = {
    title: data.title || 'Untitled',
    date: dateInfo.iso,
    slug: slug,
  };

  // Add optional fields
  if (data.tags && Array.isArray(data.tags) && data.tags.length > 0) {
    astroData.tags = data.tags;
  }

  if (data.description) {
    astroData.description = data.description;
  }

  if (data.draft) {
    astroData.draft = data.draft;
  }

  if (data.categories && Array.isArray(data.categories) && data.categories.length > 0) {
    astroData.categories = data.categories;
  }

  return astroData;
}

/**
 * Serialize frontmatter to YAML-like format
 */
function serializeFrontmatter(data) {
  const lines = ['---'];
  
  for (const [key, value] of Object.entries(data)) {
    if (Array.isArray(value)) {
      lines.push(`${key}:`);
      for (const item of value) {
        lines.push(`  - ${item}`);
      }
    } else if (typeof value === 'boolean') {
      lines.push(`${key}: ${value}`);
    } else if (typeof value === 'string' && (value.includes(':') || value.includes('"') || value.includes("'"))) {
      lines.push(`${key}: "${value.replace(/"/g, '\\"')}"`);
    } else {
      lines.push(`${key}: ${value}`);
    }
  }
  
  lines.push('---');
  return lines.join('\n');
}

/**
 * Find bidirectional links in content
 */
function findBidirectionalLinks(content) {
  const links = [];
  // Match [[link text]] or [[link text|display text]]
  const regex = /\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g;
  let match;
  
  while ((match = regex.exec(content)) !== null) {
    links.push({
      full: match[0],
      target: match[1].trim(),
      display: match[2] ? match[2].trim() : match[1].trim(),
    });
  }
  
  return links;
}

/**
 * Convert bidirectional links to standard markdown links
 */
function convertBidirectionalLinks(content, slugMap, currentSlug) {
  const links = findBidirectionalLinks(content);
  const backlinks = [];
  
  for (const link of links) {
    const targetSlug = slugify(link.target);
    const astroLink = `[${link.display}](/posts/${targetSlug})`;
    
    // Track backlink
    backlinks.push({
      from: currentSlug,
      to: targetSlug,
      text: link.display,
    });
    
    // Replace in content
    content = content.replace(link.full, astroLink);
  }
  
  return { content, backlinks };
}

/**
 * Process images in content
 */
function processImages(content, sourceDir, postImagesDir) {
  const imageRegex = /!\[([^\]]*)\]\(([^)]+)\)/g;
  const images = [];
  let match;
  
  while ((match = imageRegex.exec(content)) !== null) {
    const altText = match[1];
    const imagePath = match[2];
    
    // Skip external URLs
    if (imagePath.startsWith('http://') || imagePath.startsWith('https://')) {
      continue;
    }
    
    // Skip data URIs
    if (imagePath.startsWith('data:')) {
      continue;
    }
    
    images.push({
      full: match[0],
      alt: altText,
      path: imagePath,
    });
  }
  
  return images;
}

/**
 * Copy image and return new path
 */
function copyImage(imagePath, sourceDir, postImagesDir) {
  // Resolve source path
  let sourcePath;
  if (path.isAbsolute(imagePath)) {
    sourcePath = imagePath;
  } else {
    sourcePath = path.join(sourceDir, imagePath);
  }
  
  if (!fs.existsSync(sourcePath)) {
    logger.warn(`Image not found: ${sourcePath}`);
    return null;
  }
  
  // Generate unique filename
  const ext = path.extname(imagePath);
  const baseName = path.basename(imagePath, ext);
  const timestamp = Date.now();
  const newFileName = `${baseName}-${timestamp}${ext}`;
  const targetPath = path.join(postImagesDir, newFileName);
  
  // Copy file
  try {
    fs.copyFileSync(sourcePath, targetPath);
    stats.imagesCopied++;
    return `/images/${newFileName}`;
  } catch (err) {
    logger.error(`Failed to copy image: ${err.message}`);
    return null;
  }
}

/**
 * Fix relative links in content
 */
function fixRelativeLinks(content, sourceSlug) {
  // Fix relative markdown links
  // Convert [text](./other-post) to [text](/posts/other-post-slug)
  const relativeLinkRegex = /\[([^\]]+)\]\(\.\/([^)]+)\)/g;
  
  content = content.replace(relativeLinkRegex, (match, text, linkPath) => {
    // Remove .md extension if present
    const cleanPath = linkPath.replace(/\.md$/, '');
    const targetSlug = slugify(path.basename(cleanPath));
    return `[${text}](/posts/${targetSlug})`;
  });
  
  return content;
}

/**
 * Get all markdown files recursively
 */
function getMarkdownFiles(dir, files = []) {
  const items = fs.readdirSync(dir);
  
  for (const item of items) {
    const fullPath = path.join(dir, item);
    const stat = fs.statSync(fullPath);
    
    if (stat.isDirectory()) {
      getMarkdownFiles(fullPath, files);
    } else if (item.endsWith('.md')) {
      files.push(fullPath);
    }
  }
  
  return files;
}

/**
 * First pass: collect all slugs for link resolution
 */
function collectSlugs(files) {
  const slugMap = new Map();
  
  for (const file of files) {
    try {
      const content = fs.readFileSync(file, 'utf-8');
      const parsed = matter(content);
      const filename = path.basename(file);
      const slug = generateSlug(parsed.data, filename);
      
      // Handle duplicates
      if (slugMap.has(slug)) {
        const counter = (slugMap.get(slug).count || 0) + 1;
        const uniqueSlug = `${slug}-${counter}`;
        slugMap.set(slug, { file, count: counter });
        slugMap.set(uniqueSlug, { file, count: 0 });
        logger.warn(`Duplicate slug detected: ${slug}, using ${uniqueSlug}`);
      } else {
        slugMap.set(slug, { file, count: 0 });
      }
    } catch (err) {
      logger.error(`Failed to collect slug for ${file}: ${err.message}`);
    }
  }
  
  return slugMap;
}

/**
 * Process a single markdown file
 */
function processFile(filePath, slugMap) {
  try {
    logger.info(`Processing: ${filePath}`);
    
    const content = fs.readFileSync(filePath, 'utf-8');
    const parsed = matter(content);
    const filename = path.basename(filePath);
    const sourceDir = path.dirname(filePath);
    
    // Generate slug
    let slug = generateSlug(parsed.data, filename);
    
    // Handle duplicate slugs
    if (slugMap.has(`${slug}-1`)) {
      const counter = 1;
      slug = `${slug}-${counter}`;
    }
    
    // Extract date info
    const dateInfo = extractDateInfo(parsed.data.date, filename);
    
    // Convert frontmatter
    const astroFrontmatter = convertFrontmatter(parsed.data, slug, dateInfo);
    
    // Process content
    let body = parsed.content;
    
    // Convert bidirectional links
    const { content: convertedBody, backlinks } = convertBidirectionalLinks(body, slugMap, slug);
    body = convertedBody;
    
    // Process images
    const images = processImages(body, sourceDir, CONFIG.imagesDir);
    for (const img of images) {
      const newPath = copyImage(img.path, sourceDir, CONFIG.imagesDir);
      if (newPath) {
        const newImageTag = `![${img.alt}](${newPath})`;
        body = body.replace(img.full, newImageTag);
      }
    }
    
    // Fix relative links
    body = fixRelativeLinks(body, slug);
    
    // Generate output filename
    const outputFilename = `${dateInfo.year}-${dateInfo.month}-${dateInfo.day}-${slug}.md`;
    const outputPath = path.join(CONFIG.targetDir, outputFilename);
    
    // Generate URLs
    const hugoUrl = generateHugoUrl(dateInfo, slug);
    const astroUrl = generateAstroUrl(dateInfo, slug);
    
    // Combine frontmatter and body
    const outputContent = `${serializeFrontmatter(astroFrontmatter)}\n\n${body}`;
    
    // Write file
    fs.writeFileSync(outputPath, outputContent, 'utf-8');
    
    stats.processed++;
    stats.backlinksFound += backlinks.length;
    
    logger.success(`Created: ${outputPath}`);
    
    return {
      slug,
      hugoUrl,
      astroUrl,
      backlinks,
      outputPath,
    };
  } catch (err) {
    stats.errors++;
    logger.error(`Failed to process ${filePath}: ${err.message}`);
    return null;
  }
}

/**
 * Main migration function
 */
async function migrate() {
  logger.info('Starting Hugo to Astro migration...');
  logger.info(`Source: ${CONFIG.sourceDir}`);
  logger.info(`Target: ${CONFIG.targetDir}`);
  
  // Check source directory
  if (!fs.existsSync(CONFIG.sourceDir)) {
    logger.error(`Source directory does not exist: ${CONFIG.sourceDir}`);
    process.exit(1);
  }
  
  // Create target directories
  ensureDir(CONFIG.targetDir);
  ensureDir(CONFIG.imagesDir);
  ensureDir(path.dirname(CONFIG.backlinksFile));
  
  // Get all markdown files
  const files = getMarkdownFiles(CONFIG.sourceDir);
  logger.info(`Found ${files.length} markdown files`);
  
  if (files.length === 0) {
    logger.warn('No markdown files found. Exiting.');
    return;
  }
  
  // First pass: collect all slugs
  logger.info('Collecting slugs...');
  const slugMap = collectSlugs(files);
  logger.info(`Collected ${slugMap.size} unique slugs`);
  
  // Second pass: process files
  logger.info('Processing files...');
  const results = [];
  const allBacklinks = [];
  const urlMappings = {};
  
  for (const file of files) {
    const result = processFile(file, slugMap);
    if (result) {
      results.push(result);
      allBacklinks.push(...result.backlinks);
      urlMappings[result.hugoUrl] = result.astroUrl;
    }
  }
  
  // Write backlinks.json
  const backlinksData = {
    generated: new Date().toISOString(),
    count: allBacklinks.length,
    links: allBacklinks,
  };
  fs.writeFileSync(CONFIG.backlinksFile, JSON.stringify(backlinksData, null, 2), 'utf-8');
  logger.success(`Created backlinks file: ${CONFIG.backlinksFile}`);
  
  // Write url-mapping.json
  const urlMappingData = {
    generated: new Date().toISOString(),
    count: Object.keys(urlMappings).length,
    mappings: urlMappings,
  };
  fs.writeFileSync(CONFIG.urlMappingFile, JSON.stringify(urlMappingData, null, 2), 'utf-8');
  logger.success(`Created URL mapping file: ${CONFIG.urlMappingFile}`);
  
  // Print statistics
  logger.info('');
  logger.info('=== Migration Statistics ===');
  logger.info(`Files processed: ${stats.processed}`);
  logger.info(`Files skipped: ${stats.skipped}`);
  logger.info(`Errors: ${stats.errors}`);
  logger.info(`Images copied: ${stats.imagesCopied}`);
  logger.info(`Backlinks found: ${stats.backlinksFound}`);
  logger.info('===========================');
  
  if (stats.errors > 0) {
    logger.warn('Migration completed with errors. Please review the logs above.');
    process.exit(1);
  } else {
    logger.success('Migration completed successfully!');
  }
}

// Run migration
migrate().catch((err) => {
  logger.error(`Migration failed: ${err.message}`);
  console.error(err);
  process.exit(1);
});
