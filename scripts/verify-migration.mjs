// 迁移验证脚本
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// 读取原始 URL 列表
const originalUrls = fs.readFileSync('/tmp/urls_clean.txt', 'utf8')
    .split('\n')
    .filter(url => url.trim());

// 读取 URL 映射
const mapping = JSON.parse(fs.readFileSync(
    path.join(__dirname, '..', 'astro-blog', 'url-mapping.json'),
    'utf8'
));

// 统计信息
const stats = {
    totalOriginalUrls: originalUrls.length,
    articleUrls: 0,
    tagUrls: 0,
    otherUrls: 0,
    mappedUrls: 0,
    unmappedUrls: [],
    sampleMappings: []
};

// 分类 URL
for (const url of originalUrls) {
    if (url.match(/\/\d{4}\/\d{2}\/\d{2}\//)) {
        stats.articleUrls++;
        const pathOnly = new URL(url).pathname;
        if (mapping.mappings[pathOnly]) {
            stats.mappedUrls++;
        } else {
            stats.unmappedUrls.push(url);
        }
    } else if (url.includes('/tags/')) {
        stats.tagUrls++;
    } else {
        stats.otherUrls++;
    }
}

// 获取样本映射
stats.sampleMappings = Object.entries(mapping.mappings).slice(0, 5);

// 输出报告
console.log('╔════════════════════════════════════════════════════════════╗');
console.log('║              Hugo → Astro 迁移验证报告                      ║');
console.log('╚════════════════════════════════════════════════════════════╝\n');

console.log('📊 URL 统计:\n');
console.log(`  原始 URL 总数:     ${stats.totalOriginalUrls}`);
console.log(`  文章 URL:          ${stats.articleUrls}`);
console.log(`  标签 URL:          ${stats.tagUrls}`);
console.log(`  其他 URL:          ${stats.otherUrls}`);
console.log(`  已映射 URL:        ${stats.mappedUrls}`);
console.log(`  未映射 URL:        ${stats.unmappedUrls.length}`);

console.log('\n📋 样本 URL 映射:\n');
for (const [oldUrl, newUrl] of stats.sampleMappings) {
    console.log(`  ${oldUrl}`);
    console.log(`  → ${newUrl}\n`);
}

if (stats.unmappedUrls.length > 0) {
    console.log('\n⚠️  未映射的 URL (前 10 个):\n');
    for (const url of stats.unmappedUrls.slice(0, 10)) {
        console.log(`  - ${url}`);
    }
}

console.log('\n✅ 关键检查项:\n');
console.log(`  [${stats.mappedUrls === stats.articleUrls ? '✓' : '✗'}] 所有文章 URL 已映射`);
console.log(`  [${fs.existsSync(path.join(__dirname, '..', 'astro-blog', 'dist')) ? '✓' : '✗'}] 构建目录存在`);
console.log(`  [${fs.existsSync(path.join(__dirname, '..', 'astro-blog', 'dist', '_redirects')) ? '✓' : '✗'}] 重定向配置已生成`);
console.log(`  [${fs.existsSync(path.join(__dirname, '..', 'astro-blog', 'dist', 'sitemap-index.xml')) ? '✓' : '✗'}] Sitemap 已生成`);

console.log('\n📁 生成的文件:\n');
console.log('  - astro-blog/dist/ (构建输出)');
console.log('  - astro-blog/dist/_redirects (Netlify 重定向)');
console.log('  - astro-blog/vercel.json (Vercel 配置)');
console.log('  - astro-blog/url-mapping.json (URL 映射表)');
console.log('  - astro-blog/backlinks.json (双向链接数据)');

console.log('\n🚀 下一步:\n');
console.log('  1. 测试本地预览: cd astro-blog && npm run preview');
console.log('  2. 部署到 GitHub Pages / Netlify / Vercel');
console.log('  3. 验证重定向是否正常工作');
console.log('  4. 更新 DNS / 域名配置');

console.log('\n══════════════════════════════════════════════════════════════\n');
