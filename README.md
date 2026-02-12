# 个人博客

基于 [Astro](https://astro.build) 构建的静态博客网站。

## 技术栈

- **框架**: [Astro](https://astro.build) v5.16.16
- **UI 框架**: React 19
- **内容格式**: MDX
- **样式**: CSS
- **搜索**: Pagefind
- **代码高亮**: Shiki (github-dark 主题)

## 功能特性

- 📝 支持 MDX 格式的博客文章
- 🔍 基于 Pagefind 的全文搜索
- 🏷️ 标签和分类系统
- 👤 作者页面
- 📊 文章系列（Series）
- 🔗 Wiki 链接支持
- 📰 RSS/Atom 订阅
- 🗺️ 站点地图（Sitemap）
- 🔄 文章重定向支持
- 💬 文章引用（Mentions）

## 项目结构

```text
/
├── public/                 # 静态资源
├── src/
│   ├── components/         # Astro/React 组件
│   ├── content/           # 内容集合
│   │   └── posts/         # 博客文章（373+ 篇）
│   ├── data/              # 数据文件
│   ├── layouts/           # 页面布局
│   ├── pages/             # 路由页面
│   │   ├── index.astro    # 首页
│   │   ├── about.astro    # 关于页面
│   │   ├── friends.astro  # 友链页面
│   │   ├── running.astro  # 跑步记录
│   │   ├── search.astro   # 搜索页面
│   │   ├── posts/         # 文章列表
│   │   ├── tags/          # 标签页面
│   │   ├── categories/    # 分类页面
│   │   ├── authors/       # 作者页面
│   │   ├── series/        # 系列页面
│   │   └── mentions/      # 引用页面
│   ├── styles/            # 样式文件
│   └── utils/             # 工具函数
├── astro.config.mjs       # Astro 配置
├── backlinks.json         # 反向链接数据
└── package.json
```

## 常用命令

| 命令                | 动作                                           |
| :------------------ | :--------------------------------------------- |
| `npm install`       | 安装依赖                                       |
| `npm run dev`       | 启动开发服务器（http://localhost:4321）        |
| `npm run build`     | 构建生产站点到 `./dist/`                       |
| `npm run preview`   | 本地预览构建结果                               |
| `npm run astro ...` | 运行 Astro CLI 命令                            |

## 配置说明

- **站点地址**: `https://zdyxry.github.io`
- **输出模式**: 静态生成（Static）
- **文章集合**: 使用 Astro Content Collections 管理
- **搜索索引**: 构建时自动生成 Pagefind 索引

## 开发注意事项

1. 文章内容存放在 `src/content/posts/` 目录下
2. 使用 Wiki 链接语法 `[[文章标题]]` 创建内部链接
3. 构建时会自动生成搜索索引和站点地图
4. URL 重定向配置在 `url-mapping.json` 中

## 许可证

MIT
