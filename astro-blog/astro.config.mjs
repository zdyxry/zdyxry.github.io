import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import react from '@astrojs/react';
import wikiLinkPlugin from 'remark-wiki-link';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Load URL mappings for redirects
function loadRedirects() {
  const mappingPath = path.join(__dirname, 'url-mapping.json');
  if (!fs.existsSync(mappingPath)) {
    return {};
  }
  
  const mappingData = JSON.parse(fs.readFileSync(mappingPath, 'utf8'));
  const redirects = {};
  
  for (const [oldPath, newPath] of Object.entries(mappingData.mappings)) {
    // Remove trailing slashes for consistency
    const oldPathClean = oldPath.replace(/\/$/, '');
    const newPathClean = newPath.replace(/\/$/, '');
    
    redirects[oldPathClean] = newPathClean;
    
    // Also add version without trailing slash if it has one
    if (oldPath.endsWith('/')) {
      redirects[oldPathClean] = newPathClean;
    }
  }
  
  return redirects;
}

const redirects = loadRedirects();

// Integration to generate static HTML redirect files
function generateRedirectFiles() {
  return {
    name: 'generate-redirect-files',
    hooks: {
      'astro:build:done': async ({ dir }) => {
        const outDir = fileURLToPath(dir);
        
        for (const [oldPath, newPath] of Object.entries(redirects)) {
          // Create the directory structure
          const oldPathWithoutLeadingSlash = oldPath.replace(/^\//, '');
          const redirectDir = path.join(outDir, oldPathWithoutLeadingSlash);
          
          // Ensure directory exists
          fs.mkdirSync(redirectDir, { recursive: true });
          
          // Create index.html with meta refresh redirect
          const redirectHtml = `<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url=${newPath}">
  <link rel="canonical" href="${newPath}">
  <script>window.location.href = "${newPath}";</script>
  <title>Redirecting...</title>
</head>
<body>
  <p>Redirecting to <a href="${newPath}">${newPath}</a>...</p>
</body>
</html>`;
          
          fs.writeFileSync(path.join(redirectDir, 'index.html'), redirectHtml);
        }
        
        console.log(`Generated ${Object.keys(redirects).length} redirect files`);
      }
    }
  };
}

// Integration to generate Pagefind search index
function pagefindIntegration() {
  return {
    name: 'pagefind',
    hooks: {
      'astro:build:done': async ({ dir }) => {
        const outDir = fileURLToPath(dir);
        const { execSync } = await import('child_process');
        
        try {
          execSync(`npx pagefind --site "${outDir}"`, { stdio: 'inherit' });
          console.log('Pagefind index generated successfully');
        } catch (error) {
          console.error('Failed to generate Pagefind index:', error);
        }
      }
    }
  };
}

// https://astro.build/config
export default defineConfig({
  site: 'https://zdyxry.github.io',
  base: '/',
  output: 'static',
  outDir: 'dist',
  redirects,
  integrations: [
    mdx(),
    sitemap(),
    react(),
    generateRedirectFiles(),
    pagefindIntegration(),
  ],
  markdown: {
    remarkPlugins: [
      // Wiki-link support
      [wikiLinkPlugin, {
        pageResolver: (name) => [name.toLowerCase().replace(/\s+/g, '-')],
        hrefTemplate: (permalink) => `/mentions/${permalink}`,
      }],
    ],
    shikiConfig: {
      theme: 'github-dark',
      wrap: true,
    },
  },
  vite: {
    ssr: {
      noExternal: ['remark-wiki-link'],
    },
  },
});
