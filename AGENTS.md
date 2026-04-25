# AGENTS.md — zdyxry.github.io

## 项目概述

这是一个基于 **Astro 5** 的个人博客，从 Hugo 迁移而来。站点地址：`https://zdyxry.github.io`，部署分支为 `astro`。

## 技术栈

- **框架**: Astro 5 (静态输出 `output: 'static'`)
- **UI 组件**: Astro 组件 (`.astro`) + React (用于交互式组件)
- **内容格式**: Markdown (`.md`)，支持 MDX
- **样式**: 原生 CSS（`src/styles/global.css`），组件内 `<style>` 块
- **搜索**: Pagefind（构建后生成索引）
- **Markdown 插件**: `remark-wiki-link`（双链 `[[]]` 语法，解析到 `/mentions/` 路径）、`astro-expressive-code`
- **数据获取**: Python 脚本 (`garminconnect` / `httpx`) 通过 `uv run` 执行
- **部署**: GitHub Actions → `gh-pages` 分支

## 目录结构

```
src/
├── content/
│   └── posts/          # 博客文章 (.md)，文件名格式: YYYY-MM-DD-slug.md
├── content.config.ts   # Content Collection schema 定义
├── components/         # Astro 组件 (PascalCase.astro)
├── layouts/            # BaseLayout.astro, PostLayout.astro
├── pages/              # 路由页面
│   ├── [...slug].astro # 文章详情页 (Hugo 风格 URL)
│   ├── posts/          # 文章列表页
│   ├── tags/           # 标签页
│   ├── categories/     # 分类页
│   ├── series/         # 系列页
│   ├── mentions/       # Wiki-link 反链页
│   ├── og/             # OG 图片生成
│   ├── running.astro   # 跑步数据展示页
│   ├── search.astro    # 搜索页
│   ├── about.astro     # 关于页
│   ├── friends.astro   # 友链页
│   └── atom.xml.ts     # RSS feed
├── data/
│   └── running.json    # 跑步数据（由脚本生成，会被 CI 更新，支持 Garmin/COROS 混合）
├── styles/
│   └── global.css      # 全局样式
└── utils/
    ├── backlinks.ts    # 反链处理
    └── og-image.ts     # OG 图片生成
scripts/
├── get_garmin_data.py          # 从 Garmin Connect 拉取跑步数据
├── get_coros_data.py           # 从高驰 COROS 拉取跑步数据
└── calculate_vdot_for_existing.py  # 重算历史 VDOT 和训练负荷
```

## 内容与 Slug 约定

### 文章文件命名

文件名格式: `YYYY-MM-DD-slug.md`，存放于 `src/content/posts/`。

### Frontmatter Schema

定义在 `src/content.config.ts`，关键字段：

| 字段 | 类型 | 说明 |
|------|------|------|
| `title` | string (必需) | 文章标题 |
| `description` | string? | 文章描述 |
| `date` / `pubDate` | date | 发布日期，二者皆可（`pubDate` 优先） |
| `tags` | string[] | 标签列表，默认 `[]` |
| `draft` | boolean | 草稿标记，默认 `false` |
| `slug` | string? | 自定义 slug，用于 Hugo 兼容 URL |
| `customSlug` | string? | 自定义 slug（备用） |

### URL 生成规则

文章 URL 遵循 **Hugo 风格**：`/YYYY/MM/DD/slug/`

路由逻辑在 `src/pages/[...slug].astro` 中：
- 日期从 `pubDate` 或 `date` 提取
- slug 优先使用 frontmatter 的 `slug` 字段，否则使用 Astro 的 `post.slug`（即文件名去掉日期前缀）

### URL 重定向

`url-mapping.json` 定义旧 URL 到新 URL 的映射，`astro.config.mjs` 中的 `generateRedirectFiles()` 在构建时生成静态 HTML 重定向文件。

## 跑步数据管道

支持 **Garmin** 和 **COROS（高驰）** 两种数据源，输出格式完全一致，可混合合并到同一份 `running.json`。

### Garmin 数据流

1. `scripts/get_garmin_data.py` 通过 `garminconnect` 库登录 Garmin Connect
2. 拉取跑步活动数据，计算 VDOT 跑力和训练负荷
3. 输出到 `src/data/running.json`（默认合并模式，与已有数据合并）
4. `scripts/calculate_vdot_for_existing.py` 可重算所有历史记录的 VDOT（当 MAX_HR/RESTING_HR 调整时）

### COROS（高驰）数据流

1. `scripts/get_coros_data.py` 直接调用高驰 `teamcnapi.coros.com` API
2. 登录后分页获取活动列表，过滤 `sportType=101`（跑步）
3. 计算 VDOT 跑力和训练负荷（算法与 Garmin 脚本一致）
4. 输出到 `src/data/running.json`（默认合并模式，与已有数据合并）

### 环境变量

| 变量 | 说明 |
|------|------|
| `COROS_ACCOUNT` | 高驰账号（手机号/邮箱） |
| `COROS_PASSWORD` | 高驰明文密码（脚本内自动 MD5 加密） |
| `GARMIN_EMAIL` | Garmin 账户邮箱 |
| `GARMIN_PASSWORD` | Garmin 账户密码 |
| `MAX_HR` | 最大心率（默认 190） |
| `RESTING_HR` | 静息心率（默认 55） |

### 本地运行

```bash
# 高驰
uv run scripts/get_coros_data.py --days 30

# Garmin
uv run scripts/get_garmin_data.py --days 30
```

## GitHub Actions (CI/CD)

工作流文件: `.github/workflows/deploy.yaml`

- **触发条件**: push 到 `astro` 分支、PR、每日定时 `cron: '10 0 * * *'`（UTC 00:10）
- **流程**:
  1. `uv run scripts/get_coros_data.py --days 30` — 拉取最近 30 天高驰跑步数据
  2. `uv run scripts/get_garmin_data.py --days 30` — 若高驰步骤失败，回退拉取 Garmin 数据
  3. `python3 scripts/calculate_vdot_for_existing.py` — 重算 VDOT
  4. `npm ci && npm run build` — 构建 Astro 站点
  5. 部署到 `gh-pages` 分支（仅 `astro` 分支触发）

## Astro 自定义集成

在 `astro.config.mjs` 中定义了三个自定义集成：

1. **`generateRedirectFiles()`** — 构建后根据 `url-mapping.json` 生成静态 HTML 重定向
2. **`simplifySitemap()`** — 将 `sitemap-0.xml` 重命名为 `sitemap.xml`
3. **`pagefindIntegration()`** — 构建后运行 Pagefind 生成搜索索引

## 开发命令

```bash
npm run dev        # 启动开发服务器 (0.0.0.0:4321)
npm run build      # 构建静态站点到 dist/
npm run preview    # 预览构建结果 (0.0.0.0:4321)
```

## 编码约定

- 组件使用 **PascalCase** 命名（`PostCard.astro`、`Header.astro`）
- 页面使用 **kebab-case** 或 Astro 动态路由语法（`[...slug].astro`、`[tag].astro`）
- 中文内容为主，UI 文案使用中文
- CSS 使用 CSS 变量（`var(--text-primary)`、`var(--accent)` 等），定义在 `global.css`
- 不使用 Tailwind，样式全部为原生 CSS

## 注意事项

- `src/data/running.json` 由 CI 自动更新，不要手动编辑
- `backlinks.json` 是构建产物，记录 wiki-link 反链关系
- 文章从 Hugo 迁移而来，部分 frontmatter 同时包含 `date` 和 `slug` 以保持 URL 兼容
- Python 脚本使用 [PEP 723](https://peps.python.org/pep-0723/) inline metadata 声明依赖，通过 `uv run` 直接执行无需额外安装
