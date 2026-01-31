#!/bin/bash

# URL 兼容性检查脚本 v2
# 使用 url-mapping.json 来正确检查 Hugo URL 到 Astro URL 的映射

OLD_SITE="https://zdyxry.github.io"
NEW_SITE="http://127.0.0.1:4321"
URL_MAPPING_FILE="/var/home/yiran/projects/zdyxry.github.io/astro-blog/url-mapping.json"
URLS_FILE="/tmp/hugo_urls.txt"
RESULTS_FILE="/tmp/migration_check_results.txt"

echo "=== 博客迁移 URL 兼容性检查 v2 ==="
echo ""

# 检查 url-mapping.json 是否存在
if [ ! -f "$URL_MAPPING_FILE" ]; then
    echo "错误: URL 映射文件不存在: $URL_MAPPING_FILE"
    exit 1
fi

# 1. 爬取原站点所有 URL
echo "[1/3] 爬取原站点 URL..."

# 使用 curl 获取 sitemap
curl -s "${OLD_SITE}/sitemap.xml" | grep -oP '(?<=<loc>)[^<]+' > "$URLS_FILE"

# 补充一些重要的固定 URL
echo "${OLD_SITE}/index.xml" >> "$URLS_FILE"
echo "${OLD_SITE}/posts/" >> "$URLS_FILE"
echo "${OLD_SITE}/tags/" >> "$URLS_FILE"
echo "${OLD_SITE}/categories/" >> "$URLS_FILE"

# 获取所有 tag 页面
curl -s "${OLD_SITE}/tags/" | grep -oP 'href="(/tags/[^"]+)"' | sed 's/href="//' | sed 's/"$//' | while read path; do
    echo "${OLD_SITE}${path}" >> "$URLS_FILE"
done

# 去重
sort -u "$URLS_FILE" -o "$URLS_FILE"

TOTAL_URLS=$(wc -l < "$URLS_FILE")
echo "   找到 $TOTAL_URLS 个唯一 URL"
echo ""

# 2. 检查每个 URL 在新站点是否存在
echo "[2/3] 检查新站点 URL 可用性..."
echo ""

OK_COUNT=0
FAIL_COUNT=0
REDIRECT_COUNT=0
NOT_IN_MAPPING=0
> "$RESULTS_FILE"

while IFS= read -r url; do
    # 提取路径
    path="${url#$OLD_SITE}"
    
    # 在 url-mapping.json 中查找映射（尝试原始路径和 URL 编码路径）
    mapped_path=$(node -e "
        const fs = require('fs');
        const mapping = JSON.parse(fs.readFileSync('$URL_MAPPING_FILE', 'utf8'));
        // Try the path as-is (URL encoded)
        if (mapping.mappings['$path']) {
            console.log(mapping.mappings['$path']);
            return;
        }
        // Try URL decoded path
        const decoded = decodeURIComponent('$path');
        if (mapping.mappings[decoded]) {
            console.log(mapping.mappings[decoded]);
            return;
        }
        console.log('');
    ")
    
    if [ -n "$mapped_path" ]; then
        # 有映射，检查映射后的 URL
        new_url="${NEW_SITE}${mapped_path}"
        status=$(curl -s -o /dev/null -w "%{http_code}" "$new_url" 2>/dev/null)
        
        if [ "$status" = "200" ]; then
            echo "↪ $path → $mapped_path"
            echo "REDIRECT: $path → $mapped_path" >> "$RESULTS_FILE"
            ((REDIRECT_COUNT++))
        else
            echo "✗ $path (映射存在但目标返回 HTTP $status)"
            echo "FAIL: $path (映射存在但目标返回 HTTP $status)" >> "$RESULTS_FILE"
            ((FAIL_COUNT++))
        fi
    else
        # 没有映射，尝试直接访问（可能是特殊页面如 /about, /tags 等）
        new_url="${NEW_SITE}${path}"
        status=$(curl -s -o /dev/null -w "%{http_code}" "$new_url" 2>/dev/null)
        
        if [ "$status" = "200" ]; then
            echo "✓ $path"
            echo "OK: $path" >> "$RESULTS_FILE"
            ((OK_COUNT++))
        else
            echo "✗ $path (HTTP $status, 无映射)"
            echo "FAIL: $path (HTTP $status, 无映射)" >> "$RESULTS_FILE"
            ((FAIL_COUNT++))
        fi
    fi
done < "$URLS_FILE"

# 3. 输出汇总
echo ""
echo "[3/3] 检查结果汇总"
echo "===================="
echo "总 URL 数: $TOTAL_URLS"
echo "直接成功: $OK_COUNT"
echo "重定向成功: $REDIRECT_COUNT"
echo "失败: $FAIL_COUNT"
echo ""

if [ "$FAIL_COUNT" -gt 0 ]; then
    echo "失败的 URL:"
    grep "^FAIL" "$RESULTS_FILE" | sed 's/FAIL: /  /'
    echo ""
    
    # 保存失败的 URL 到文件
    grep "^FAIL" "$RESULTS_FILE" | sed 's/FAIL: //' > /var/home/yiran/projects/zdyxry.github.io/scripts/failed_urls.txt
    echo "失败的 URL 已保存到: scripts/failed_urls.txt"
    exit 1
else
    echo "所有 URL 都已成功迁移（含重定向）!"
    exit 0
fi
