#!/bin/bash

# URL 兼容性检查脚本
# 检查 Hugo 站点的 URL 在 Astro 站点中是否都存在（支持重定向）

OLD_SITE="https://zdyxry.github.io"
NEW_SITE="http://127.0.0.1:4321"
URLS_FILE="/tmp/hugo_urls.txt"
RESULTS_FILE="/tmp/migration_check_results.txt"

echo "=== 博客迁移 URL 兼容性检查 ==="
echo ""

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
> "$RESULTS_FILE"

while IFS= read -r url; do
    # 将 URL 转换为新站点路径
    path="${url#$OLD_SITE}"
    new_url="${NEW_SITE}${path}"
    
    # 检查 HTTP 状态码（跟随重定向）
    response=$(curl -s -L -o /dev/null -w "%{http_code}|%{url_effective}" "$new_url" 2>/dev/null)
    status=$(echo "$response" | cut -d'|' -f1)
    final_url=$(echo "$response" | cut -d'|' -f2)
    
    if [ "$status" = "200" ]; then
        # 检查是否发生了重定向
        if [ "$final_url" != "$new_url" ]; then
            # 提取新路径
            new_path="${final_url#$NEW_SITE}"
            echo "↪ $path → $new_path"
            echo "REDIRECT: $path → $new_path" >> "$RESULTS_FILE"
            ((REDIRECT_COUNT++))
        else
            echo "✓ $path" 
            echo "OK: $path" >> "$RESULTS_FILE"
            ((OK_COUNT++))
        fi
    else
        echo "✗ $path (HTTP $status)"
        echo "FAIL: $path (HTTP $status)" >> "$RESULTS_FILE"
        ((FAIL_COUNT++))
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
    exit 1
else
    echo "所有 URL 都已成功迁移（含重定向）!"
    exit 0
fi
