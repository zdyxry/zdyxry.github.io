#!/usr/bin/env node
/**
 * Generate URL mapping from Hugo to Astro
 * Hugo URL format: /YYYY/MM/DD/slug/ (slug from original filename, preserving case)
 * Astro URL format: /posts/YYYY/MM/DD/slug/ (slug is lowercase)
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Read all markdown files from Hugo content directory
const hugoContentDir = path.join(__dirname, '..', '..', 'content', 'posts');
const astroContentDir = path.join(__dirname, '..', 'src', 'content', 'posts');

function parseFrontMatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) return null;
  
  const fm = match[1];
  const result = {};
  
  // Parse date
  const dateMatch = fm.match(/date:\s*(.+)/);
  if (dateMatch) {
    result.date = new Date(dateMatch[1].trim());
  }
  
  return result;
}

function generateMappings() {
  const mappings = {};
  let caseVariants = 0;
  
  // Get all Hugo posts
  const hugoFiles = fs.readdirSync(hugoContentDir).filter(f => f.endsWith('.md'));
  
  for (const filename of hugoFiles) {
    // Skip non-post files
    if (filename.startsWith('_')) continue;
    
    const hugoPath = path.join(hugoContentDir, filename);
    const content = fs.readFileSync(hugoPath, 'utf8');
    const fm = parseFrontMatter(content);
    
    if (!fm || !fm.date) {
      console.warn(`Warning: No date found in ${filename}`);
      continue;
    }
    
    const date = fm.date;
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    
    // Hugo slug: from filename (remove .md, preserve case)
    const hugoSlug = filename.replace(/\.md$/, '');
    
    // Astro slug: lowercase
    const astroSlug = hugoSlug.toLowerCase();
    
    // Build URLs
    const hugoUrl = `/${year}/${month}/${day}/${hugoSlug}/`;
    const astroUrl = `/posts/${year}/${month}/${day}/${astroSlug}/`;
    
    // Add mapping
    mappings[hugoUrl] = astroUrl;
    
    // If Hugo slug has uppercase letters, also add lowercase variant
    if (hugoSlug !== astroSlug) {
      const hugoUrlLower = `/${year}/${month}/${day}/${astroSlug}/`;
      mappings[hugoUrlLower] = astroUrl;
      caseVariants++;
    }
  }
  
  return { mappings, caseVariants };
}

function main() {
  console.log('Generating URL mappings...\n');
  
  const { mappings, caseVariants } = generateMappings();
  
  const mappingData = {
    generated: new Date().toISOString(),
    count: Object.keys(mappings).length,
    caseVariants,
    mappings
  };
  
  const outputPath = path.join(__dirname, '..', 'url-mapping.json');
  fs.writeFileSync(outputPath, JSON.stringify(mappingData, null, 2));
  
  console.log(`✅ Generated URL mapping file:`);
  console.log(`   - Total mappings: ${mappingData.count}`);
  console.log(`   - Case variants: ${caseVariants}`);
  console.log(`   - Output: ${outputPath}`);
  
  // Show some examples
  console.log('\nSample mappings:');
  const entries = Object.entries(mappings).slice(0, 5);
  for (const [old, new_] of entries) {
    console.log(`   ${old} → ${new_}`);
  }
  
  // Show case variant examples
  const caseVariantEntries = Object.entries(mappings).filter(([old, new_]) => {
    const slug = old.split('/')[4];
    return slug && slug !== slug.toLowerCase();
  }).slice(0, 5);
  
  if (caseVariantEntries.length > 0) {
    console.log('\nCase variant examples:');
    for (const [old, new_] of caseVariantEntries) {
      console.log(`   ${old} → ${new_}`);
    }
  }
}

main();
