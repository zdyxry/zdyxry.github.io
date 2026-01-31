#!/usr/bin/env node
/**
 * Fix missing posts that weren't migrated due to special characters in slugs
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Missing posts configuration
// Format: [hugo slug, astro filename, custom slug for URL]
const missingPosts = [
  // 1. I/O-bursts-with-QEMU-2.6 -> io-bursts-with-qemu-26
  {
    hugoFile: 'I-O-bursts-with-QEMU-2-6.md',
    astroFile: '2017-11-16-io-bursts-with-qemu-26.md',
    customSlug: 'io-bursts-with-qemu-26',
    date: '2017-11-16'
  },
  // 2. Linux-安全清理-/boot-分区 -> linux-安全清理-boot-分区
  {
    hugoFile: 'Linux-安全清理-boot-分区.md',
    astroFile: '2018-08-09-linux-安全清理-boot-分区.md',
    customSlug: 'linux-安全清理-boot-分区',
    date: '2018-08-09'
  },
  // 3. cluster-api-provider-vsphere-源码阅读 (has subpages, use main)
  {
    hugoFile: 'cluster-api-provider-vsphere-源码阅读/index.md',
    astroFile: '2019-08-16-cluster-api-provider-vsphere-源码阅读.md',
    customSlug: 'cluster-api-provider-vsphere-源码阅读',
    date: '2019-08-16'
  },
  // 4. 《图解密码技术》读书笔记
  {
    hugoFile: '《图解密码技术》读书笔记/index.md',
    astroFile: '2019-09-14-图解密码技术读书笔记.md',
    customSlug: '图解密码技术读书笔记',
    date: '2019-09-14'
  },
  // 5. ARM-服务器？能用？
  {
    hugoFile: 'ARM-服务器？能用？.md',
    astroFile: '2019-11-01-arm-服务器-能用.md',
    customSlug: 'arm-服务器-能用',
    date: '2019-11-01'
  },
  // 6. 如何捕捉-Ctrl-C-指令
  {
    hugoFile: '如何捕捉-Ctrl-C-指令.md',
    astroFile: '2019-11-23-如何捕捉-ctrl-c-指令.md',
    customSlug: '如何捕捉-ctrl-c-指令',
    date: '2019-11-23'
  },
  // 7. 为什么-flannel.1-丢失后不会自动重建 -> use existing file
  {
    hugoFile: '为什么你的-flannel-1-会消失/index.md',
    astroFile: '2020-01-03-为什么-flannel-1-丢失后不会自动重建.md',
    customSlug: '为什么-flannel-1-丢失后不会自动重建',
    date: '2020-01-03'
  },
  // 8. ThinkPad-T480-Ubuntu-19.10-连接多显示器方式
  {
    hugoFile: 'ThinkPad-T480-Ubuntu-19-10-连接多显示器方式/index.md',
    astroFile: '2020-01-12-thinkpad-t480-ubuntu-19-10-连接多显示器方式.md',
    customSlug: 'thinkpad-t480-ubuntu-19-10-连接多显示器方式',
    date: '2020-01-12'
  },
  // 9 & 10. bin/systemctl and lib/systemd/systemd - skip (these are subpaths, not real articles)
  // They're likely artifacts from the cluster-api article
  
  // 11. 论文阅读-Pingmesh
  {
    hugoFile: '论文阅读-《Pingmesh-A-Large-Scale-System-for-Data-Center-Network-Latency-Measurement-and-Analysis》/index.md',
    astroFile: '2020-03-26-论文阅读-pingmesh.md',
    customSlug: '论文阅读-pingmesh',
    date: '2020-03-26'
  },
  // 12 & 13. PodmanDocker-Compose-学习记录/cli and /config - subpaths, skip
  
  // 14. Celery/Kombu-MongoDB-连接异常调查记录
  {
    hugoFile: 'Celery-Kombu-MongoDB-连接异常调查记录.md',
    astroFile: '2022-05-09-celery-kombu-mongodb-连接异常调查记录.md',
    customSlug: 'celery-kombu-mongodb-连接异常调查记录',
    date: '2022-05-09'
  },
  // 15. 《毫无意义的工作》读书笔记
  {
    hugoFile: '《毫无意义的工作》读书笔记.md',
    astroFile: '2022-10-22-毫无意义的工作读书笔记.md',
    customSlug: '毫无意义的工作读书笔记',
    date: '2022-10-22'
  }
];

const hugoContentDir = path.join(__dirname, '..', 'content', 'posts');
const astroContentDir = path.join(__dirname, '..', 'astro-blog', 'src', 'content', 'posts');

// Process each missing post
for (const post of missingPosts) {
  const hugoPath = path.join(hugoContentDir, post.hugoFile);
  const astroPath = path.join(astroContentDir, post.astroFile);
  
  // Check if already exists in Astro
  if (fs.existsSync(astroPath)) {
    console.log(`✓ Already exists: ${post.astroFile}`);
    continue;
  }
  
  // Check if Hugo file exists
  if (!fs.existsSync(hugoPath)) {
    console.log(`✗ Hugo file not found: ${post.hugoFile}`);
    continue;
  }
  
  // Read Hugo content
  let content = fs.readFileSync(hugoPath, 'utf8');
  
  // Parse frontmatter
  const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!frontmatterMatch) {
    console.log(`✗ Invalid frontmatter: ${post.hugoFile}`);
    continue;
  }
  
  let [, frontmatter, body] = frontmatterMatch;
  
  // Update frontmatter
  // Convert date format
  frontmatter = frontmatter.replace(/^date:\s*.+$/m, `date: ${post.date}`);
  
  // Add custom slug
  if (!frontmatter.includes('customSlug:')) {
    frontmatter += `\ncustomSlug: ${post.customSlug}`;
  }
  
  // Reconstruct content
  const newContent = `---\n${frontmatter}\n---\n${body}`;
  
  // Write to Astro
  fs.writeFileSync(astroPath, newContent);
  console.log(`✓ Created: ${post.astroFile}`);
}

console.log('\nDone!');
