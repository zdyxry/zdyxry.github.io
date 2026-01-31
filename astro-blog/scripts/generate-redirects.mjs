// 生成重定向配置脚本
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// 读取 URL 映射
const mappingPath = path.join(__dirname, '..', 'url-mapping.json');
const mapping = JSON.parse(fs.readFileSync(mappingPath, 'utf8'));

// 生成 _redirects 文件 (用于 Netlify)
function generateNetlifyRedirects() {
    const lines = [];
    
    for (const [oldUrl, newUrl] of Object.entries(mapping.mappings)) {
        // 确保 URL 以 / 结尾
        const oldPath = oldUrl.endsWith('/') ? oldUrl : oldUrl + '/';
        const newPath = newUrl.endsWith('/') ? newUrl : newUrl + '/';
        lines.push(`${oldPath} ${newPath} 301`);
    }
    
    // RSS 重定向：旧链接指向新链接
    lines.push('/rss.xml /atom.xml 301');
    
    const content = lines.join('\n');
    fs.writeFileSync(path.join(__dirname, '..', 'dist', '_redirects'), content);
    console.log('Generated: dist/_redirects');
}

// 生成 vercel.json 重定向配置
function generateVercelRedirects() {
    const redirects = [];
    
    for (const [oldUrl, newUrl] of Object.entries(mapping.mappings)) {
        redirects.push({
            source: oldUrl,
            destination: newUrl,
            permanent: true
        });
    }
    
    // RSS 重定向：旧链接指向新链接
    redirects.push({
        source: '/rss.xml',
        destination: '/atom.xml',
        permanent: true
    });
    
    const config = { redirects };
    fs.writeFileSync(
        path.join(__dirname, '..', 'vercel.json'),
        JSON.stringify(config, null, 2)
    );
    console.log('Generated: vercel.json');
}

// 生成静态 HTML 重定向文件 (用于 GitHub Pages)
function generateStaticRedirects() {
    const redirectsDir = path.join(__dirname, '..', 'dist', 'redirects');
    if (!fs.existsSync(redirectsDir)) {
        fs.mkdirSync(redirectsDir, { recursive: true });
    }
    
    let count = 0;
    for (const [oldUrl, newUrl] of Object.entries(mapping.mappings)) {
        // 解析旧 URL: /YYYY/MM/DD/slug/
        const match = oldUrl.match(/^\/(\d{4})\/(\d{2})\/(\d{2})\/(.+?)\/$/);
        if (!match) continue;
        
        const [, year, month, day, slug] = match;
        
        // 创建目录结构
        const dirPath = path.join(redirectsDir, year, month, day, slug);
        if (!fs.existsSync(dirPath)) {
            fs.mkdirSync(dirPath, { recursive: true });
        }
        
        // 创建 index.html 重定向文件
        const html = `<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url=${newUrl}">
    <link rel="canonical" href="${newUrl}">
    <title>Redirecting...</title>
</head>
<body>
    <p>Redirecting to <a href="${newUrl}">${newUrl}</a>...</p>
</body>
</html>`;
        
        fs.writeFileSync(path.join(dirPath, 'index.html'), html);
        count++;
    }
    
    console.log(`Generated: ${count} static redirect files in dist/redirects/`);
}

// 生成重定向报告
function generateReport() {
    const report = {
        generated: new Date().toISOString(),
        totalRedirects: mapping.count,
        hugoUrlPattern: '/YYYY/MM/DD/slug/',
        astroUrlPattern: '/posts/slug/',
        sampleMappings: Object.entries(mapping.mappings).slice(0, 5).map(([old, new_]) => ({ old, new: new_ }))
    };
    
    fs.writeFileSync(
        path.join(__dirname, '..', 'redirect-report.json'),
        JSON.stringify(report, null, 2)
    );
    console.log('Generated: redirect-report.json');
}

// 主函数
function main() {
    console.log('Generating redirect configurations...\n');
    
    generateNetlifyRedirects();
    generateVercelRedirects();
    generateStaticRedirects();
    generateReport();
    
    console.log('\n✅ All redirect configurations generated successfully!');
    console.log(`\nTotal redirects: ${mapping.count}`);
    console.log('\nFiles generated:');
    console.log('  - dist/_redirects (Netlify)');
    console.log('  - vercel.json (Vercel)');
    console.log('  - dist/redirects/ (Static HTML redirects for GitHub Pages)');
    console.log('  - redirect-report.json');
}

main();
