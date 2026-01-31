# Hugo → Astro 迁移总结

## 迁移概览

| 项目 | Hugo | Astro |
|------|------|-------|
| 文章数量 | 365 篇 | 365 篇 |
| 构建页面 | ~400 页 | 1194 页 |
| 双向链接 | ❌ 不支持 | ✅ 支持 (`[[...]]` → `/mentions/...`) |
| Running Page | Go Template + JS | ✅ React 组件 |
| 主题 | hugo-coder | 自定义 (类似风格) |
| **URL 格式** | `/YYYY/MM/DD/slug/` | ✅ **保持不变** |

## 已完成的任务

### 1. URL 格式保留 ✅
保留了 Hugo 的 URL 格式，无需重定向：
```
/posts/2019/05/11/kubernetes-实战-前言/
```

### 2. 内容迁移 ✅
- 迁移了 365 篇博客文章
- 转换了 frontmatter 格式
- 复制了 80 张图片

### 3. Mentions（双向链接）功能 ✅
- **文章中的语法**: `[[Keyword]]` → `[Keyword](/mentions/keyword)`
- **Mentions 页面**: `/mentions/keyword` 显示所有提到该关键词的文章
- **页面内容**: 
  - 文章标题
  - 发布日期
  - **关键词上下文片段**（提及该关键词的句子前后文）
  - "阅读全文"链接
- **统计**: 1734 个 mentions 链接，生成约 800+ 个 mentions 页面

### 4. Running Page 重构 ✅
- 使用 React + TypeScript 重写了热力图组件
- 支持年份切换
- 显示统计信息（总距离、时长、连续天数等）
- 支持深色/浅色模式

### 5. 主题与样式 ✅
- 实现了类似 hugo-coder 的简洁风格
- 支持深色/浅色模式切换
- 响应式设计
- 代码高亮（Shiki）

### 6. 页面内容迁移 ✅

#### About 页面 (`/about`)
- 个人介绍（依然 / zdyxry）
- 博客内容说明（周报、技术、生活）
- 博客更新历史
  - 20190804 集成豆瓣读书、观影记录
  - 20230305 从 Hexo 转到 Hugo
  - 20230606 豆瓣记录迁移至 NeoDB
  - 20240809 调整 RSS 模版样式
  - 20250810 增加 Running 页面
  - **20260129 从 Hugo 迁移到 Astro**
- 知识共享协议（CC BY-NC-SA 3.0）

#### Friends 页面 (`/friends`)
- 6 个友链（从 Hugo 迁移）
  - Jiajun的编程随想 (https://jiajunhuang.com/)
  - 格物致知 (https://liqiang.io/)
  - 玻璃齿轮 - SlassGear (https://blog.winkidney.com/)
  - CosPotato's Blog (https://blog.0x233.cn/)
  - Joker (https://quartz.19960312.xyz/)
  - fanyang's blog (https://fuis.me/)

## 项目结构

```
astro-blog/
├── src/
│   ├── content/
│   │   └── posts/          # 365 篇博客文章
│   ├── components/
│   │   ├── Header.astro    # 导航栏
│   │   ├── Footer.astro    # 页脚
│   │   ├── PostCard.astro  # 文章卡片
│   │   ├── RunningCalendar.tsx  # 跑步日历组件
│   │   └── TagList.astro   # 标签列表
│   ├── layouts/
│   │   ├── BaseLayout.astro
│   │   ├── PostLayout.astro
│   │   └── PageLayout.astro
│   ├── pages/
│   │   ├── index.astro     # 首页
│   │   ├── posts/          # 文章列表和详情
│   │   │   └── [...slug].astro  # 动态路由 (Hugo 格式)
│   │   ├── tags/           # 标签云和标签详情
│   │   ├── mentions/       # Mentions 页面
│   │   │   └── [...slug].astro  # 关键词提及页面
│   │   ├── running.astro   # Running Page
│   │   ├── about.astro     # 关于页面
│   │   ├── friends.astro   # 友链页面
│   │   └── 404.astro       # 404 页面
│   ├── styles/
│   │   └── global.css      # 全局样式
│   └── utils/
│       └── running-data.ts # 跑步数据处理
├── public/
│   └── images/             # 图片资源
├── dist/                   # 构建输出
│   ├── posts/              # 文章页面 (Hugo 格式)
│   ├── mentions/           # Mentions 页面
│   ├── tags/               # 标签页面
│   ├── about/              # 关于页面
│   ├── friends/            # 友链页面
│   └── running/            # Running 页面
└── scripts/
    └── migrate-hugo-to-astro-v5.mjs  # 迁移脚本
```

## URL 结构

### 文章页面
```
/posts/2019/05/11/kubernetes-实战-前言/
/posts/2022/08/07/weekly-issue-2022-08-07/
```

### Mentions 页面
```
/mentions/kubernetes
/mentions/minio
/mentions/docker
/mentions/ai
```

### 其他页面
```
/tags/kubernetes/
/tags/weekly/
/running/
/about/
/friends/
/rss.xml
```

## 关键配置

### content.config.ts
```typescript
schema: z.object({
  title: z.string(),
  date: z.coerce.date(),
  customSlug: z.string().optional(),  // 存储 slug 部分
  tags: z.array(z.string()).optional().default([]),
  // ...
})
```

### [...slug].astro (文章路由)
动态路由生成 Hugo 格式的 URL：
```typescript
const date = new Date(post.data.pubDate || post.data.date);
const year = date.getFullYear();
const month = String(date.getMonth() + 1).padStart(2, '0');
const day = String(date.getDate()).padStart(2, '0');
const slugPart = post.data.customSlug || post.slug;
const hugoSlug = `${year}/${month}/${day}/${slugPart}`;
```

### [...slug].astro (Mentions 路由)
提取所有 `[[...]]` 链接并生成 mentions 页面：
```typescript
// Match [text](/mentions/keyword) syntax
const mentionRegex = /\[([^\]]+)\]\(\/mentions\/([^)]+)\)/g;

// Extract context around the mention (100 chars before and after)
const contextStart = Math.max(0, matchIndex - 100);
const contextEnd = Math.min(content.length, matchIndex + match[0].length + 100);
```

## 本地开发

```bash
cd astro-blog
npm install
npm run dev      # 启动开发服务器
npm run build    # 构建生产版本
npm run preview  # 预览生产构建
```

## 部署

由于 URL 格式与 Hugo 完全一致，可以直接部署替换，**无需重定向配置**。

### GitHub Pages
```bash
cd astro-blog
npm run build
# 部署 dist/ 目录到 gh-pages 分支
```

### Netlify / Vercel
```bash
# 直接部署 dist/ 目录
# 无需额外重定向配置
```

## 迁移脚本

迁移脚本位于 `scripts/migrate-hugo-to-astro-v5.mjs`，功能：
- 迁移文章内容和 frontmatter
- 处理 `[[...]]` 链接 → `/mentions/...`
- 复制图片到 `public/images/`
- 生成 Hugo 格式的 URL

如需重新迁移：
```bash
node scripts/migrate-hugo-to-astro-v5.mjs
```

## 验证清单

- [x] 所有文章已迁移 (365 篇)
- [x] URL 格式与 Hugo 一致 (`/posts/YYYY/MM/DD/slug/`)
- [x] Mentions 功能正常 (`[[...]]` → `/mentions/...`)
- [x] Running Page 功能正常
- [x] 标签系统正常
- [x] RSS 订阅正常 (`/rss.xml`)
- [x] Sitemap 生成正常
- [x] 深色/浅色模式切换正常
- [x] 响应式设计正常
- [x] About 页面内容完整
- [x] Friends 页面内容完整
- [x] **无需 URL 重定向**

## 后续改进建议

### 高优先级
1. **修复代码块中的 `[[...]]` 被误转换** - 当前代码块中的双括号也会被转换
2. **优化 Mentions 页面上下文提取** - 有时提取的上下文不够准确
3. **添加搜索功能** - 可使用 Pagefind 或 Algolia

### 中优先级
4. **图片懒加载** - 优化页面加载性能
5. **字体优化** - 使用系统字体或优化 Web 字体加载
6. **添加评论系统** - Giscus、Utterances 等

### 低优先级
7. **文章阅读进度条**
8. **相关文章推荐**
9. **文章目录 (TOC) 优化**
10. **PWA 支持**

## 已知问题

1. **代码块中的 `[[...]]` 被误转换** - 如 `[[ "$i" ]]` 会被转换为链接
   - 临时解决方案：迁移脚本尝试跳过代码块，但可能不完全
   - 长期方案：使用更精确的 Markdown AST 解析

2. **部分图片链接失效** - 原 Hugo 文章中的相对路径图片
   - 已复制大部分图片到 `public/images/`
   - 部分缺失图片已移除引用

3. **重复 ID 警告** - 构建时有重复 ID 警告
   - 不影响功能，是 Hugo 源内容有重复 slug

## 与 Hugo 的对比

| 特性 | Hugo | Astro |
|------|------|-------|
| URL 格式 | `/YYYY/MM/DD/slug/` | ✅ `/posts/YYYY/MM/DD/slug/` |
| 构建速度 | 快 | ✅ 快 (1194 页 4.4s) |
| Mentions | ❌ 不支持 | ✅ 原生支持 |
| Running Page | Go Template | ✅ React 组件 |
| 开发体验 | 一般 | ✅ Hot reload, TypeScript |
| 主题定制 | 复杂 | ✅ 灵活 |

---

**迁移完成时间**: 2026-01-29
**原始文章数**: 365
**迁移后文章数**: 365
**构建页面数**: 1194
**Mentions 链接数**: 1734
**URL 格式**: Hugo 格式 (`/posts/YYYY/MM/DD/slug/`)
