#!/usr/bin/env node
/**
 * Content migration script
 * 
 * This script helps migrate content from other platforms to Astro.
 * Currently supports:
 * - Markdown files with frontmatter
 * - Hugo content format
 */

import * as fs from 'fs';
import * as path from 'path';

interface MigrationOptions {
  sourceDir: string;
  targetDir: string;
  format?: 'hugo' | 'markdown';
}

/**
 * Parse Hugo frontmatter and convert to Astro format
 */
function convertHugoFrontmatter(content: string): string {
  // Hugo uses +++ for TOML frontmatter, convert to --- for YAML
  if (content.startsWith('+++')) {
    const endIndex = content.indexOf('+++', 3);
    if (endIndex !== -1) {
      const tomlContent = content.slice(3, endIndex).trim();
      const body = content.slice(endIndex + 3).trim();
      
      // Simple TOML to YAML conversion
      const yamlContent = tomlContent
        .split('\n')
        .map(line => {
          // Convert key = "value" to key: value
          const match = line.match(/^(.+?)\s*=\s*"(.+)"$/);
          if (match) {
            return `${match[1].trim()}: "${match[2]}"`;
          }
          // Convert key = value (non-string) to key: value
          const match2 = line.match(/^(.+?)\s*=\s*(.+)$/);
          if (match2) {
            return `${match2[1].trim()}: ${match2[2].trim()}`;
          }
          return line;
        })
        .join('\n');
      
      return `---\n${yamlContent}\n---\n\n${body}`;
    }
  }
  
  return content;
}

/**
 * Process a single file
 */
function processFile(filePath: string, targetDir: string, format: string): void {
  const content = fs.readFileSync(filePath, 'utf-8');
  const fileName = path.basename(filePath);
  const targetPath = path.join(targetDir, fileName);
  
  let processedContent = content;
  
  if (format === 'hugo') {
    processedContent = convertHugoFrontmatter(content);
  }
  
  fs.writeFileSync(targetPath, processedContent);
  console.log(`✓ Migrated: ${fileName}`);
}

/**
 * Main migration function
 */
async function migrate(options: MigrationOptions): Promise<void> {
  const { sourceDir, targetDir, format = 'markdown' } = options;
  
  // Ensure target directory exists
  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }
  
  // Read source directory
  const files = fs.readdirSync(sourceDir);
  const markdownFiles = files.filter(f => f.endsWith('.md') || f.endsWith('.mdx'));
  
  console.log(`Found ${markdownFiles.length} markdown files to migrate\n`);
  
  for (const file of markdownFiles) {
    const filePath = path.join(sourceDir, file);
    processFile(filePath, targetDir, format);
  }
  
  console.log('\n✅ Migration complete!');
}

// CLI usage
if (require.main === module) {
  const args = process.argv.slice(2);
  
  if (args.length < 2) {
    console.log('Usage: ts-node migrate-content.ts <source-dir> <target-dir> [format]');
    console.log('  format: hugo | markdown (default: markdown)');
    process.exit(1);
  }
  
  const [sourceDir, targetDir, format = 'markdown'] = args;
  
  migrate({
    sourceDir: path.resolve(sourceDir),
    targetDir: path.resolve(targetDir),
    format: format as 'hugo' | 'markdown',
  }).catch(console.error);
}

export { migrate, convertHugoFrontmatter };
